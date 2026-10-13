---
url: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient
title: Class v1beta1.DataLabelingServiceClient (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:47.115750+00:00
---

# Class v1beta1.DataLabelingServiceClient (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.DataLabelingServiceClient (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.2.2  3.1.1  2.3.0  2.2.7 

Service for the AI Platform Data Labeling API. v1beta1

## Package

[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DataLabelingServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DataLabelingServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### dataLabelingServiceStub
    
    
    dataLabelingServiceStub?: Promise<{
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

### annotatedDatasetPath(project, dataset, annotatedDataset)
    
    
    annotatedDatasetPath(project: string, dataset: string, annotatedDataset: string): string;

Return a fully-qualified annotatedDataset resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`dataset` |  `string`   
  
`annotatedDataset` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### annotationSpecSetPath(project, annotationSpecSet)
    
    
    annotationSpecSetPath(project: string, annotationSpecSet: string): string;

Return a fully-qualified annotationSpecSet resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`annotationSpecSet` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### checkCreateInstructionProgress(name)
    
    
    checkCreateInstructionProgress(name: string): Promise<LROperation<protos.google.cloud.datalabeling.v1beta1.Instruction, protos.google.cloud.datalabeling.v1beta1.CreateInstructionMetadata>>;

Check the status of the long running operation returned by `createInstruction()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.datalabeling.v1beta1.Instruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.instruction), [protos.google.cloud.datalabeling.v1beta1.CreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.createinstructionmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Instruction resource parent, format:
       *  projects/{project_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. Instruction of how to perform the labeling task.
       */
      // const instruction = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callCreateInstruction() {
        // Construct request
        const request = {
          parent,
          instruction,
        };
    
        // Run request
        const [operation] = await datalabelingClient.createInstruction(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateInstruction();
    
    

### checkExportDataProgress(name)
    
    
    checkExportDataProgress(name: string): Promise<LROperation<protos.google.cloud.datalabeling.v1beta1.ExportDataOperationResponse, protos.google.cloud.datalabeling.v1beta1.ExportDataOperationMetadata>>;

Check the status of the long running operation returned by `exportData()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.datalabeling.v1beta1.ExportDataOperationResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.exportdataoperationresponse), [protos.google.cloud.datalabeling.v1beta1.ExportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.exportdataoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Dataset resource name, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const name = 'abc123'
      /**
       *  Required. Annotated dataset resource name. DataItem in
       *  Dataset and their annotations in specified annotated dataset will be
       *  exported. It's in format of
       *  projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
       *  {annotated_dataset_id}
       */
      // const annotatedDataset = 'abc123'
      /**
       *  Optional. Filter is not supported at this moment.
       */
      // const filter = 'abc123'
      /**
       *  Required. Specify the output destination.
       */
      // const outputConfig = {}
      /**
       *  Email of the user who started the export task and should be notified by
       *  email. If empty no notification will be sent.
       */
      // const userEmailAddress = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callExportData() {
        // Construct request
        const request = {
          name,
          annotatedDataset,
          outputConfig,
        };
    
        // Run request
        const [operation] = await datalabelingClient.exportData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportData();
    
    

### checkImportDataProgress(name)
    
    
    checkImportDataProgress(name: string): Promise<LROperation<protos.google.cloud.datalabeling.v1beta1.ImportDataOperationResponse, protos.google.cloud.datalabeling.v1beta1.ImportDataOperationMetadata>>;

Check the status of the long running operation returned by `importData()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.datalabeling.v1beta1.ImportDataOperationResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.importdataoperationresponse), [protos.google.cloud.datalabeling.v1beta1.ImportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.importdataoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Dataset resource name, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const name = 'abc123'
      /**
       *  Required. Specify the input source of the data.
       */
      // const inputConfig = {}
      /**
       *  Email of the user who started the import task and should be notified by
       *  email. If empty no notification will be sent.
       */
      // const userEmailAddress = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callImportData() {
        // Construct request
        const request = {
          name,
          inputConfig,
        };
    
        // Run request
        const [operation] = await datalabelingClient.importData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportData();
    
    

### checkLabelImageProgress(name)
    
    
    checkLabelImageProgress(name: string): Promise<LROperation<protos.google.cloud.datalabeling.v1beta1.AnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.LabelOperationMetadata>>;

Check the status of the long running operation returned by `labelImage()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.datalabeling.v1beta1.AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset), [protos.google.cloud.datalabeling.v1beta1.LabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labeloperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Configuration for image classification task.
       *  One of image_classification_config, bounding_poly_config,
       *  polyline_config and segmentation_config are required.
       */
      // const imageClassificationConfig = {}
      /**
       *  Configuration for bounding box and bounding poly task.
       *  One of image_classification_config, bounding_poly_config,
       *  polyline_config and segmentation_config are required.
       */
      // const boundingPolyConfig = {}
      /**
       *  Configuration for polyline task.
       *  One of image_classification_config, bounding_poly_config,
       *  polyline_config and segmentation_config are required.
       */
      // const polylineConfig = {}
      /**
       *  Configuration for segmentation task.
       *  One of image_classification_config, bounding_poly_config,
       *  polyline_config and segmentation_config are required.
       */
      // const segmentationConfig = {}
      /**
       *  Required. Name of the dataset to request labeling task, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. Basic human annotation config.
       */
      // const basicConfig = {}
      /**
       *  Required. The type of image labeling task.
       */
      // const feature = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callLabelImage() {
        // Construct request
        const request = {
          parent,
          basicConfig,
          feature,
        };
    
        // Run request
        const [operation] = await datalabelingClient.labelImage(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callLabelImage();
    
    

### checkLabelTextProgress(name)
    
    
    checkLabelTextProgress(name: string): Promise<LROperation<protos.google.cloud.datalabeling.v1beta1.AnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.LabelOperationMetadata>>;

Check the status of the long running operation returned by `labelText()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.datalabeling.v1beta1.AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset), [protos.google.cloud.datalabeling.v1beta1.LabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labeloperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Configuration for text classification task.
       *  One of text_classification_config and text_entity_extraction_config
       *  is required.
       */
      // const textClassificationConfig = {}
      /**
       *  Configuration for entity extraction task.
       *  One of text_classification_config and text_entity_extraction_config
       *  is required.
       */
      // const textEntityExtractionConfig = {}
      /**
       *  Required. Name of the data set to request labeling task, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. Basic human annotation config.
       */
      // const basicConfig = {}
      /**
       *  Required. The type of text labeling task.
       */
      // const feature = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callLabelText() {
        // Construct request
        const request = {
          parent,
          basicConfig,
          feature,
        };
    
        // Run request
        const [operation] = await datalabelingClient.labelText(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callLabelText();
    
    

### checkLabelVideoProgress(name)
    
    
    checkLabelVideoProgress(name: string): Promise<LROperation<protos.google.cloud.datalabeling.v1beta1.AnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.LabelOperationMetadata>>;

Check the status of the long running operation returned by `labelVideo()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.datalabeling.v1beta1.AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset), [protos.google.cloud.datalabeling.v1beta1.LabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.labeloperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Configuration for video classification task.
       *  One of video_classification_config, object_detection_config,
       *  object_tracking_config and event_config is required.
       */
      // const videoClassificationConfig = {}
      /**
       *  Configuration for video object detection task.
       *  One of video_classification_config, object_detection_config,
       *  object_tracking_config and event_config is required.
       */
      // const objectDetectionConfig = {}
      /**
       *  Configuration for video object tracking task.
       *  One of video_classification_config, object_detection_config,
       *  object_tracking_config and event_config is required.
       */
      // const objectTrackingConfig = {}
      /**
       *  Configuration for video event task.
       *  One of video_classification_config, object_detection_config,
       *  object_tracking_config and event_config is required.
       */
      // const eventConfig = {}
      /**
       *  Required. Name of the dataset to request labeling task, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. Basic human annotation config.
       */
      // const basicConfig = {}
      /**
       *  Required. The type of video labeling task.
       */
      // const feature = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callLabelVideo() {
        // Construct request
        const request = {
          parent,
          basicConfig,
          feature,
        };
    
        // Run request
        const [operation] = await datalabelingClient.labelVideo(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callLabelVideo();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createAnnotationSpecSet(request, options)
    
    
    createAnnotationSpecSet(request?: protos.google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet,
            (protos.google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest | undefined),
            {} | undefined
        ]>;

Creates an annotation spec set by providing a set of labels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateannotationspecsetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotationspecset), ([protos.google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateannotationspecsetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotationspecset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. AnnotationSpecSet resource parent, format:
       *  projects/{project_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. Annotation spec set to create. Annotation specs must be included.
       *  Only one annotation spec will be accepted for annotation specs with same
       *  display_name.
       */
      // const annotationSpecSet = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callCreateAnnotationSpecSet() {
        // Construct request
        const request = {
          parent,
          annotationSpecSet,
        };
    
        // Run request
        const response = await datalabelingClient.createAnnotationSpecSet(request);
        console.log(response);
      }
    
      callCreateAnnotationSpecSet();
    
    

### createAnnotationSpecSet(request, options, callback)
    
    
    createAnnotationSpecSet(request: protos.google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet, protos.google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateannotationspecsetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotationspecset), [protos.google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateannotationspecsetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAnnotationSpecSet(request, callback)
    
    
    createAnnotationSpecSet(request: protos.google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet, protos.google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateannotationspecsetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotationspecset), [protos.google.cloud.datalabeling.v1beta1.ICreateAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateannotationspecsetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataset(request, options)
    
    
    createDataset(request?: protos.google.cloud.datalabeling.v1beta1.ICreateDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IDataset,
            (protos.google.cloud.datalabeling.v1beta1.ICreateDatasetRequest | undefined),
            {} | undefined
        ]>;

Creates dataset. If success return a Dataset resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreatedatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataset), ([protos.google.cloud.datalabeling.v1beta1.ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreatedatasetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Dataset resource parent, format:
       *  projects/{project_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. The dataset to be created.
       */
      // const dataset = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callCreateDataset() {
        // Construct request
        const request = {
          parent,
          dataset,
        };
    
        // Run request
        const response = await datalabelingClient.createDataset(request);
        console.log(response);
      }
    
      callCreateDataset();
    
    

### createDataset(request, options, callback)
    
    
    createDataset(request: protos.google.cloud.datalabeling.v1beta1.ICreateDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IDataset, protos.google.cloud.datalabeling.v1beta1.ICreateDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreatedatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataset), [protos.google.cloud.datalabeling.v1beta1.ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreatedatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataset(request, callback)
    
    
    createDataset(request: protos.google.cloud.datalabeling.v1beta1.ICreateDatasetRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IDataset, protos.google.cloud.datalabeling.v1beta1.ICreateDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreatedatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataset), [protos.google.cloud.datalabeling.v1beta1.ICreateDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreatedatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvaluationJob(request, options)
    
    
    createEvaluationJob(request?: protos.google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IEvaluationJob,
            (protos.google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest | undefined),
            {} | undefined
        ]>;

Creates an evaluation job.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateevaluationjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob), ([protos.google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateevaluationjobrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Evaluation job resource parent. Format:
       *  "projects/{project_id}"
       */
      // const parent = 'abc123'
      /**
       *  Required. The evaluation job to create.
       */
      // const job = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callCreateEvaluationJob() {
        // Construct request
        const request = {
          parent,
          job,
        };
    
        // Run request
        const response = await datalabelingClient.createEvaluationJob(request);
        console.log(response);
      }
    
      callCreateEvaluationJob();
    
    

### createEvaluationJob(request, options, callback)
    
    
    createEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IEvaluationJob, protos.google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateevaluationjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob), [protos.google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvaluationJob(request, callback)
    
    
    createEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IEvaluationJob, protos.google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateevaluationjobrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob), [protos.google.cloud.datalabeling.v1beta1.ICreateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInstruction(request, options)
    
    
    createInstruction(request?: protos.google.cloud.datalabeling.v1beta1.ICreateInstructionRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.datalabeling.v1beta1.IInstruction, protos.google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates an instruction for how data should be labeled.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.datalabeling.v1beta1.IInstruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iinstruction), [protos.google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Instruction resource parent, format:
       *  projects/{project_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. Instruction of how to perform the labeling task.
       */
      // const instruction = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callCreateInstruction() {
        // Construct request
        const request = {
          parent,
          instruction,
        };
    
        // Run request
        const [operation] = await datalabelingClient.createInstruction(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateInstruction();
    
    

### createInstruction(request, options, callback)
    
    
    createInstruction(request: protos.google.cloud.datalabeling.v1beta1.ICreateInstructionRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IInstruction, protos.google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IInstruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iinstruction), [protos.google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createInstruction(request, callback)
    
    
    createInstruction(request: protos.google.cloud.datalabeling.v1beta1.ICreateInstructionRequest, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IInstruction, protos.google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IInstruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iinstruction), [protos.google.cloud.datalabeling.v1beta1.ICreateInstructionMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.icreateinstructionmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### dataItemPath(project, dataset, dataItem)
    
    
    dataItemPath(project: string, dataset: string, dataItem: string): string;

Return a fully-qualified dataItem resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`dataset` |  `string`   
  
`dataItem` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### datasetPath(project, dataset)
    
    
    datasetPath(project: string, dataset: string): string;

Return a fully-qualified dataset resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`dataset` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteAnnotatedDataset(request, options)
    
    
    deleteAnnotatedDataset(request?: protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest | undefined),
            {} | undefined
        ]>;

Deletes an annotated dataset by resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotateddatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), ([protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotateddatasetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the annotated dataset to delete, format:
       *  projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
       *  {annotated_dataset_id}
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callDeleteAnnotatedDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.deleteAnnotatedDataset(request);
        console.log(response);
      }
    
      callDeleteAnnotatedDataset();
    
    

### deleteAnnotatedDataset(request, options, callback)
    
    
    deleteAnnotatedDataset(request: protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotateddatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotateddatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAnnotatedDataset(request, callback)
    
    
    deleteAnnotatedDataset(request: protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotateddatasetrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotateddatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAnnotationSpecSet(request, options)
    
    
    deleteAnnotationSpecSet(request?: protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest | undefined),
            {} | undefined
        ]>;

Deletes an annotation spec set by resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotationspecsetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), ([protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotationspecsetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. AnnotationSpec resource name, format:
       *  `projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}`.
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callDeleteAnnotationSpecSet() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.deleteAnnotationSpecSet(request);
        console.log(response);
      }
    
      callDeleteAnnotationSpecSet();
    
    

### deleteAnnotationSpecSet(request, options, callback)
    
    
    deleteAnnotationSpecSet(request: protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotationspecsetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotationspecsetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAnnotationSpecSet(request, callback)
    
    
    deleteAnnotationSpecSet(request: protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotationspecsetrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IDeleteAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteannotationspecsetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataset(request, options)
    
    
    deleteDataset(request?: protos.google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest | undefined),
            {} | undefined
        ]>;

Deletes a dataset by resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideletedatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), ([protos.google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideletedatasetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Dataset resource name, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callDeleteDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.deleteDataset(request);
        console.log(response);
      }
    
      callDeleteDataset();
    
    

### deleteDataset(request, options, callback)
    
    
    deleteDataset(request: protos.google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideletedatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideletedatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataset(request, callback)
    
    
    deleteDataset(request: protos.google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideletedatasetrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IDeleteDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideletedatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationJob(request, options)
    
    
    deleteEvaluationJob(request?: protos.google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest | undefined),
            {} | undefined
        ]>;

Stops and deletes an evaluation job.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteevaluationjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), ([protos.google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteevaluationjobrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the evaluation job that is going to be deleted. Format:
       *  "projects/{project_id}/evaluationJobs/{evaluation_job_id}"
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callDeleteEvaluationJob() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.deleteEvaluationJob(request);
        console.log(response);
      }
    
      callDeleteEvaluationJob();
    
    

### deleteEvaluationJob(request, options, callback)
    
    
    deleteEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteevaluationjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEvaluationJob(request, callback)
    
    
    deleteEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteevaluationjobrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IDeleteEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInstruction(request, options)
    
    
    deleteInstruction(request?: protos.google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest | undefined),
            {} | undefined
        ]>;

Deletes an instruction object by resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteinstructionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), ([protos.google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteinstructionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Instruction resource name, format:
       *  projects/{project_id}/instructions/{instruction_id}
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callDeleteInstruction() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.deleteInstruction(request);
        console.log(response);
      }
    
      callDeleteInstruction();
    
    

### deleteInstruction(request, options, callback)
    
    
    deleteInstruction(request: protos.google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteinstructionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteinstructionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteInstruction(request, callback)
    
    
    deleteInstruction(request: protos.google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteinstructionrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IDeleteInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ideleteinstructionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### evaluationJobPath(project, evaluationJob)
    
    
    evaluationJobPath(project: string, evaluationJob: string): string;

Return a fully-qualified evaluationJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`evaluationJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### evaluationPath(project, dataset, evaluation)
    
    
    evaluationPath(project: string, dataset: string, evaluation: string): string;

Return a fully-qualified evaluation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`dataset` |  `string`   
  
`evaluation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### examplePath(project, dataset, annotatedDataset, example)
    
    
    examplePath(project: string, dataset: string, annotatedDataset: string, example: string): string;

Return a fully-qualified example resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`dataset` |  `string`   
  
`annotatedDataset` |  `string`   
  
`example` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### exportData(request, options)
    
    
    exportData(request?: protos.google.cloud.datalabeling.v1beta1.IExportDataRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.datalabeling.v1beta1.IExportDataOperationResponse, protos.google.cloud.datalabeling.v1beta1.IExportDataOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Exports data and annotations from dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.datalabeling.v1beta1.IExportDataOperationResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdataoperationresponse), [protos.google.cloud.datalabeling.v1beta1.IExportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Dataset resource name, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const name = 'abc123'
      /**
       *  Required. Annotated dataset resource name. DataItem in
       *  Dataset and their annotations in specified annotated dataset will be
       *  exported. It's in format of
       *  projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
       *  {annotated_dataset_id}
       */
      // const annotatedDataset = 'abc123'
      /**
       *  Optional. Filter is not supported at this moment.
       */
      // const filter = 'abc123'
      /**
       *  Required. Specify the output destination.
       */
      // const outputConfig = {}
      /**
       *  Email of the user who started the export task and should be notified by
       *  email. If empty no notification will be sent.
       */
      // const userEmailAddress = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callExportData() {
        // Construct request
        const request = {
          name,
          annotatedDataset,
          outputConfig,
        };
    
        // Run request
        const [operation] = await datalabelingClient.exportData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callExportData();
    
    

### exportData(request, options, callback)
    
    
    exportData(request: protos.google.cloud.datalabeling.v1beta1.IExportDataRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IExportDataOperationResponse, protos.google.cloud.datalabeling.v1beta1.IExportDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IExportDataOperationResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdataoperationresponse), [protos.google.cloud.datalabeling.v1beta1.IExportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### exportData(request, callback)
    
    
    exportData(request: protos.google.cloud.datalabeling.v1beta1.IExportDataRequest, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IExportDataOperationResponse, protos.google.cloud.datalabeling.v1beta1.IExportDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdatarequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IExportDataOperationResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdataoperationresponse), [protos.google.cloud.datalabeling.v1beta1.IExportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotatedDataset(request, options)
    
    
    getAnnotatedDataset(request?: protos.google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset,
            (protos.google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest | undefined),
            {} | undefined
        ]>;

Gets an annotated dataset by resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotateddatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), ([protos.google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotateddatasetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the annotated dataset to get, format:
       *  projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
       *  {annotated_dataset_id}
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callGetAnnotatedDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.getAnnotatedDataset(request);
        console.log(response);
      }
    
      callGetAnnotatedDataset();
    
    

### getAnnotatedDataset(request, options, callback)
    
    
    getAnnotatedDataset(request: protos.google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotateddatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotateddatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotatedDataset(request, callback)
    
    
    getAnnotatedDataset(request: protos.google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotateddatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.IGetAnnotatedDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotateddatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotationSpecSet(request, options)
    
    
    getAnnotationSpecSet(request?: protos.google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet,
            (protos.google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest | undefined),
            {} | undefined
        ]>;

Gets an annotation spec set by resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotationspecsetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotationspecset), ([protos.google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotationspecsetrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotationspecset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. AnnotationSpecSet resource name, format:
       *  projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callGetAnnotationSpecSet() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.getAnnotationSpecSet(request);
        console.log(response);
      }
    
      callGetAnnotationSpecSet();
    
    

### getAnnotationSpecSet(request, options, callback)
    
    
    getAnnotationSpecSet(request: protos.google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet, protos.google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotationspecsetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotationspecset), [protos.google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotationspecsetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAnnotationSpecSet(request, callback)
    
    
    getAnnotationSpecSet(request: protos.google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet, protos.google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotationspecsetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotationspecset), [protos.google.cloud.datalabeling.v1beta1.IGetAnnotationSpecSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetannotationspecsetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataItem(request, options)
    
    
    getDataItem(request?: protos.google.cloud.datalabeling.v1beta1.IGetDataItemRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IDataItem,
            protos.google.cloud.datalabeling.v1beta1.IGetDataItemRequest | undefined,
            {} | undefined
        ]>;

Gets a data item in a dataset by resource name. This API can be called after data are imported into dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataItemRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdataitemrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataitem), [protos.google.cloud.datalabeling.v1beta1.IGetDataItemRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdataitemrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataitem). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the data item to get, format:
       *  projects/{project_id}/datasets/{dataset_id}/dataItems/{data_item_id}
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callGetDataItem() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.getDataItem(request);
        console.log(response);
      }
    
      callGetDataItem();
    
    

### getDataItem(request, options, callback)
    
    
    getDataItem(request: protos.google.cloud.datalabeling.v1beta1.IGetDataItemRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IDataItem, protos.google.cloud.datalabeling.v1beta1.IGetDataItemRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataItemRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdataitemrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataitem), [protos.google.cloud.datalabeling.v1beta1.IGetDataItemRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdataitemrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataItem(request, callback)
    
    
    getDataItem(request: protos.google.cloud.datalabeling.v1beta1.IGetDataItemRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IDataItem, protos.google.cloud.datalabeling.v1beta1.IGetDataItemRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataItemRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdataitemrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataitem), [protos.google.cloud.datalabeling.v1beta1.IGetDataItemRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdataitemrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request, options)
    
    
    getDataset(request?: protos.google.cloud.datalabeling.v1beta1.IGetDatasetRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IDataset,
            protos.google.cloud.datalabeling.v1beta1.IGetDatasetRequest | undefined,
            {} | undefined
        ]>;

Gets dataset by resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdatasetrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataset), [protos.google.cloud.datalabeling.v1beta1.IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdatasetrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataset). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Dataset resource name, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callGetDataset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.getDataset(request);
        console.log(response);
      }
    
      callGetDataset();
    
    

### getDataset(request, options, callback)
    
    
    getDataset(request: protos.google.cloud.datalabeling.v1beta1.IGetDatasetRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IDataset, protos.google.cloud.datalabeling.v1beta1.IGetDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdatasetrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataset), [protos.google.cloud.datalabeling.v1beta1.IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataset(request, callback)
    
    
    getDataset(request: protos.google.cloud.datalabeling.v1beta1.IGetDatasetRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IDataset, protos.google.cloud.datalabeling.v1beta1.IGetDatasetRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdatasetrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataset), [protos.google.cloud.datalabeling.v1beta1.IGetDatasetRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetdatasetrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluation(request, options)
    
    
    getEvaluation(request?: protos.google.cloud.datalabeling.v1beta1.IGetEvaluationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IEvaluation,
            (protos.google.cloud.datalabeling.v1beta1.IGetEvaluationRequest | undefined),
            {} | undefined
        ]>;

Gets an evaluation by resource name (to search, use ).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluation), ([protos.google.cloud.datalabeling.v1beta1.IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Evaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluation). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the evaluation. Format:
       *  "projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}'
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callGetEvaluation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.getEvaluation(request);
        console.log(response);
      }
    
      callGetEvaluation();
    
    

### getEvaluation(request, options, callback)
    
    
    getEvaluation(request: protos.google.cloud.datalabeling.v1beta1.IGetEvaluationRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IEvaluation, protos.google.cloud.datalabeling.v1beta1.IGetEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluation), [protos.google.cloud.datalabeling.v1beta1.IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluation(request, callback)
    
    
    getEvaluation(request: protos.google.cloud.datalabeling.v1beta1.IGetEvaluationRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IEvaluation, protos.google.cloud.datalabeling.v1beta1.IGetEvaluationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluation), [protos.google.cloud.datalabeling.v1beta1.IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationJob(request, options)
    
    
    getEvaluationJob(request?: protos.google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IEvaluationJob,
            (protos.google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest | undefined),
            {} | undefined
        ]>;

Gets an evaluation job by resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob), ([protos.google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationjobrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the evaluation job. Format:
       *  "projects/{project_id}/evaluationJobs/{evaluation_job_id}"
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callGetEvaluationJob() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.getEvaluationJob(request);
        console.log(response);
      }
    
      callGetEvaluationJob();
    
    

### getEvaluationJob(request, options, callback)
    
    
    getEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IEvaluationJob, protos.google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob), [protos.google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluationJob(request, callback)
    
    
    getEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IEvaluationJob, protos.google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationjobrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob), [protos.google.cloud.datalabeling.v1beta1.IGetEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getExample(request, options)
    
    
    getExample(request?: protos.google.cloud.datalabeling.v1beta1.IGetExampleRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IExample,
            protos.google.cloud.datalabeling.v1beta1.IGetExampleRequest | undefined,
            {} | undefined
        ]>;

Gets an example by resource name, including both data and annotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetexamplerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IExample](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexample), [protos.google.cloud.datalabeling.v1beta1.IGetExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetexamplerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Example](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.example). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of example, format:
       *  projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
       *  {annotated_dataset_id}/examples/{example_id}
       */
      // const name = 'abc123'
      /**
       *  Optional. An expression for filtering Examples. Filter by
       *  annotation_spec.display_name is supported. Format
       *  "annotation_spec.display_name = {display_name}"
       */
      // const filter = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callGetExample() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.getExample(request);
        console.log(response);
      }
    
      callGetExample();
    
    

### getExample(request, options, callback)
    
    
    getExample(request: protos.google.cloud.datalabeling.v1beta1.IGetExampleRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IExample, protos.google.cloud.datalabeling.v1beta1.IGetExampleRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetexamplerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IExample](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexample), [protos.google.cloud.datalabeling.v1beta1.IGetExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetexamplerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getExample(request, callback)
    
    
    getExample(request: protos.google.cloud.datalabeling.v1beta1.IGetExampleRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IExample, protos.google.cloud.datalabeling.v1beta1.IGetExampleRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetexamplerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IExample](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexample), [protos.google.cloud.datalabeling.v1beta1.IGetExampleRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetexamplerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstruction(request, options)
    
    
    getInstruction(request?: protos.google.cloud.datalabeling.v1beta1.IGetInstructionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IInstruction,
            (protos.google.cloud.datalabeling.v1beta1.IGetInstructionRequest | undefined),
            {} | undefined
        ]>;

Gets an instruction by resource name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetinstructionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IInstruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iinstruction), ([protos.google.cloud.datalabeling.v1beta1.IGetInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetinstructionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Instruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.instruction). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Instruction resource name, format:
       *  projects/{project_id}/instructions/{instruction_id}
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callGetInstruction() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.getInstruction(request);
        console.log(response);
      }
    
      callGetInstruction();
    
    

### getInstruction(request, options, callback)
    
    
    getInstruction(request: protos.google.cloud.datalabeling.v1beta1.IGetInstructionRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IInstruction, protos.google.cloud.datalabeling.v1beta1.IGetInstructionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetinstructionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IInstruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iinstruction), [protos.google.cloud.datalabeling.v1beta1.IGetInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetinstructionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstruction(request, callback)
    
    
    getInstruction(request: protos.google.cloud.datalabeling.v1beta1.IGetInstructionRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IInstruction, protos.google.cloud.datalabeling.v1beta1.IGetInstructionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetinstructionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IInstruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iinstruction), [protos.google.cloud.datalabeling.v1beta1.IGetInstructionRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.igetinstructionrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### importData(request, options)
    
    
    importData(request?: protos.google.cloud.datalabeling.v1beta1.IImportDataRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.datalabeling.v1beta1.IImportDataOperationResponse, protos.google.cloud.datalabeling.v1beta1.IImportDataOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Imports data into dataset based on source locations defined in request. It can be called multiple times for the same dataset. Each dataset can only have one long running operation running on it. For example, no labeling task (also long running operation) can be started while importing is still ongoing. Vice versa.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.datalabeling.v1beta1.IImportDataOperationResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdataoperationresponse), [protos.google.cloud.datalabeling.v1beta1.IImportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Dataset resource name, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const name = 'abc123'
      /**
       *  Required. Specify the input source of the data.
       */
      // const inputConfig = {}
      /**
       *  Email of the user who started the import task and should be notified by
       *  email. If empty no notification will be sent.
       */
      // const userEmailAddress = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callImportData() {
        // Construct request
        const request = {
          name,
          inputConfig,
        };
    
        // Run request
        const [operation] = await datalabelingClient.importData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportData();
    
    

### importData(request, options, callback)
    
    
    importData(request: protos.google.cloud.datalabeling.v1beta1.IImportDataRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IImportDataOperationResponse, protos.google.cloud.datalabeling.v1beta1.IImportDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IImportDataOperationResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdataoperationresponse), [protos.google.cloud.datalabeling.v1beta1.IImportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importData(request, callback)
    
    
    importData(request: protos.google.cloud.datalabeling.v1beta1.IImportDataRequest, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IImportDataOperationResponse, protos.google.cloud.datalabeling.v1beta1.IImportDataOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdatarequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IImportDataOperationResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdataoperationresponse), [protos.google.cloud.datalabeling.v1beta1.IImportDataOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iimportdataoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
  
### instructionPath(project, instruction)
    
    
    instructionPath(project: string, instruction: string): string;

Return a fully-qualified instruction resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instruction` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### labelImage(request, options)
    
    
    labelImage(request?: protos.google.cloud.datalabeling.v1beta1.ILabelImageRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Starts a labeling task for image. The type of image labeling task is configured by feature in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelimagerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Configuration for image classification task.
       *  One of image_classification_config, bounding_poly_config,
       *  polyline_config and segmentation_config are required.
       */
      // const imageClassificationConfig = {}
      /**
       *  Configuration for bounding box and bounding poly task.
       *  One of image_classification_config, bounding_poly_config,
       *  polyline_config and segmentation_config are required.
       */
      // const boundingPolyConfig = {}
      /**
       *  Configuration for polyline task.
       *  One of image_classification_config, bounding_poly_config,
       *  polyline_config and segmentation_config are required.
       */
      // const polylineConfig = {}
      /**
       *  Configuration for segmentation task.
       *  One of image_classification_config, bounding_poly_config,
       *  polyline_config and segmentation_config are required.
       */
      // const segmentationConfig = {}
      /**
       *  Required. Name of the dataset to request labeling task, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. Basic human annotation config.
       */
      // const basicConfig = {}
      /**
       *  Required. The type of image labeling task.
       */
      // const feature = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callLabelImage() {
        // Construct request
        const request = {
          parent,
          basicConfig,
          feature,
        };
    
        // Run request
        const [operation] = await datalabelingClient.labelImage(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callLabelImage();
    
    

### labelImage(request, options, callback)
    
    
    labelImage(request: protos.google.cloud.datalabeling.v1beta1.ILabelImageRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelimagerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### labelImage(request, callback)
    
    
    labelImage(request: protos.google.cloud.datalabeling.v1beta1.ILabelImageRequest, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelImageRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelimagerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### labelText(request, options)
    
    
    labelText(request?: protos.google.cloud.datalabeling.v1beta1.ILabelTextRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Starts a labeling task for text. The type of text labeling task is configured by feature in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeltextrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Configuration for text classification task.
       *  One of text_classification_config and text_entity_extraction_config
       *  is required.
       */
      // const textClassificationConfig = {}
      /**
       *  Configuration for entity extraction task.
       *  One of text_classification_config and text_entity_extraction_config
       *  is required.
       */
      // const textEntityExtractionConfig = {}
      /**
       *  Required. Name of the data set to request labeling task, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. Basic human annotation config.
       */
      // const basicConfig = {}
      /**
       *  Required. The type of text labeling task.
       */
      // const feature = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callLabelText() {
        // Construct request
        const request = {
          parent,
          basicConfig,
          feature,
        };
    
        // Run request
        const [operation] = await datalabelingClient.labelText(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callLabelText();
    
    

### labelText(request, options, callback)
    
    
    labelText(request: protos.google.cloud.datalabeling.v1beta1.ILabelTextRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeltextrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### labelText(request, callback)
    
    
    labelText(request: protos.google.cloud.datalabeling.v1beta1.ILabelTextRequest, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelTextRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeltextrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### labelVideo(request, options)
    
    
    labelVideo(request?: protos.google.cloud.datalabeling.v1beta1.ILabelVideoRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Starts a labeling task for video. The type of video labeling task is configured by feature in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelVideoRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelvideorequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Configuration for video classification task.
       *  One of video_classification_config, object_detection_config,
       *  object_tracking_config and event_config is required.
       */
      // const videoClassificationConfig = {}
      /**
       *  Configuration for video object detection task.
       *  One of video_classification_config, object_detection_config,
       *  object_tracking_config and event_config is required.
       */
      // const objectDetectionConfig = {}
      /**
       *  Configuration for video object tracking task.
       *  One of video_classification_config, object_detection_config,
       *  object_tracking_config and event_config is required.
       */
      // const objectTrackingConfig = {}
      /**
       *  Configuration for video event task.
       *  One of video_classification_config, object_detection_config,
       *  object_tracking_config and event_config is required.
       */
      // const eventConfig = {}
      /**
       *  Required. Name of the dataset to request labeling task, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. Basic human annotation config.
       */
      // const basicConfig = {}
      /**
       *  Required. The type of video labeling task.
       */
      // const feature = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callLabelVideo() {
        // Construct request
        const request = {
          parent,
          basicConfig,
          feature,
        };
    
        // Run request
        const [operation] = await datalabelingClient.labelVideo(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callLabelVideo();
    
    

### labelVideo(request, options, callback)
    
    
    labelVideo(request: protos.google.cloud.datalabeling.v1beta1.ILabelVideoRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelVideoRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelvideorequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### labelVideo(request, callback)
    
    
    labelVideo(request: protos.google.cloud.datalabeling.v1beta1.ILabelVideoRequest, callback: Callback<LROperation<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset, protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILabelVideoRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabelvideorequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset), [protos.google.cloud.datalabeling.v1beta1.ILabelOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilabeloperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnnotatedDatasets(request, options)
    
    
    listAnnotatedDatasets(request?: protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset[],
            protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest | null,
            protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsResponse
        ]>;

Lists annotated datasets for a dataset. Pagination is supported.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotatedDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset)[], [protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsrequest) | null, [protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAnnotatedDatasetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAnnotatedDatasets(request, options, callback)
    
    
    listAnnotatedDatasets(request: protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest, protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotatedDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsrequest), [protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnnotatedDatasets(request, callback)
    
    
    listAnnotatedDatasets(request: protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest, protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotatedDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsrequest), [protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnnotatedDatasetsAsync(request, options)
    
    
    listAnnotatedDatasetsAsync(request?: protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset>;

Equivalent to `listAnnotatedDatasets`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotatedDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.datalabeling.v1beta1.IAnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotateddataset)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the dataset to list annotated datasets, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const parent = 'abc123'
      /**
       *  Optional. Filter is not supported at this moment.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer results than
       *  requested. Default value is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results for the server to return.
       *  Typically obtained by
       *  ListAnnotatedDatasetsResponse.next_page_token google.cloud.datalabeling.v1beta1.ListAnnotatedDatasetsResponse.next_page_token  of the previous
       *  DataLabelingService.ListAnnotatedDatasets  call.
       *  Return first page if empty.
       */
      // const pageToken = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callListAnnotatedDatasets() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = datalabelingClient.[listAnnotatedDatasetsAsync](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAnnotatedDatasets();
    
    

### listAnnotatedDatasetsStream(request, options)
    
    
    listAnnotatedDatasetsStream(request?: protos.google.cloud.datalabeling.v1beta1.IListAnnotatedDatasetsRequest, options?: CallOptions): Transform;

Equivalent to `listAnnotatedDatasets`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotatedDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotateddatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [AnnotatedDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotateddataset) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAnnotatedDatasetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAnnotationSpecSets(request, options)
    
    
    listAnnotationSpecSets(request?: protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet[],
            protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest | null,
            protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsResponse
        ]>;

Lists annotation spec sets for a project. Pagination is supported.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationSpecSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotationspecset)[], [protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsrequest) | null, [protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [AnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotationspecset). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAnnotationSpecSetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAnnotationSpecSets(request, options, callback)
    
    
    listAnnotationSpecSets(request: protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest, protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationSpecSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsrequest), [protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotationspecset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnnotationSpecSets(request, callback)
    
    
    listAnnotationSpecSets(request: protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest, protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationSpecSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsrequest), [protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotationspecset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAnnotationSpecSetsAsync(request, options)
    
    
    listAnnotationSpecSetsAsync(request?: protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet>;

Equivalent to `listAnnotationSpecSets`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationSpecSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.datalabeling.v1beta1.IAnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iannotationspecset)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [AnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotationspecset). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent of AnnotationSpecSet resource, format:
       *  projects/{project_id}
       */
      // const parent = 'abc123'
      /**
       *  Optional. Filter is not supported at this moment.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer results than
       *  requested. Default value is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results for the server to return.
       *  Typically obtained by
       *  ListAnnotationSpecSetsResponse.next_page_token google.cloud.datalabeling.v1beta1.ListAnnotationSpecSetsResponse.next_page_token  of the previous
       *  DataLabelingService.ListAnnotationSpecSets  call.
       *  Return first page if empty.
       */
      // const pageToken = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callListAnnotationSpecSets() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = datalabelingClient.[listAnnotationSpecSetsAsync](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAnnotationSpecSets();
    
    

### listAnnotationSpecSetsStream(request, options)
    
    
    listAnnotationSpecSetsStream(request?: protos.google.cloud.datalabeling.v1beta1.IListAnnotationSpecSetsRequest, options?: CallOptions): Transform;

Equivalent to `listAnnotationSpecSets`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAnnotationSpecSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistannotationspecsetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [AnnotationSpecSet](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.annotationspecset) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAnnotationSpecSetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataItems(request, options)
    
    
    listDataItems(request?: protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IDataItem[],
            protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest | null,
            protos.google.cloud.datalabeling.v1beta1.IListDataItemsResponse
        ]>;

Lists data items in a dataset. This API can be called after data are imported into dataset. Pagination is supported.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataitem)[], [protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsrequest) | null, [protos.google.cloud.datalabeling.v1beta1.IListDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [DataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataitem). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDataItemsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataItems(request, options, callback)
    
    
    listDataItems(request: protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest, protos.google.cloud.datalabeling.v1beta1.IListDataItemsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IDataItem>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsrequest), [protos.google.cloud.datalabeling.v1beta1.IListDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataitem)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataItems(request, callback)
    
    
    listDataItems(request: protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest, protos.google.cloud.datalabeling.v1beta1.IListDataItemsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IDataItem>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsrequest), [protos.google.cloud.datalabeling.v1beta1.IListDataItemsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataitem)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataItemsAsync(request, options)
    
    
    listDataItemsAsync(request?: protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.datalabeling.v1beta1.IDataItem>;

Equivalent to `listDataItems`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.datalabeling.v1beta1.IDataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataitem)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [DataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataitem). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the dataset to list data items, format:
       *  projects/{project_id}/datasets/{dataset_id}
       */
      // const parent = 'abc123'
      /**
       *  Optional. Filter is not supported at this moment.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer results than
       *  requested. Default value is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results for the server to return.
       *  Typically obtained by
       *  ListDataItemsResponse.next_page_token google.cloud.datalabeling.v1beta1.ListDataItemsResponse.next_page_token  of the previous
       *  DataLabelingService.ListDataItems  call.
       *  Return first page if empty.
       */
      // const pageToken = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callListDataItems() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = datalabelingClient.[listDataItemsAsync](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDataItems();
    
    

### listDataItemsStream(request, options)
    
    
    listDataItemsStream(request?: protos.google.cloud.datalabeling.v1beta1.IListDataItemsRequest, options?: CallOptions): Transform;

Equivalent to `listDataItems`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdataitemsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [DataItem](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataitem) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDataItemsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDatasets(request, options)
    
    
    listDatasets(request?: protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IDataset[],
            protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest | null,
            protos.google.cloud.datalabeling.v1beta1.IListDatasetsResponse
        ]>;

Lists datasets under a project. Pagination is supported.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataset)[], [protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsrequest) | null, [protos.google.cloud.datalabeling.v1beta1.IListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataset). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDatasetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDatasets(request, options, callback)
    
    
    listDatasets(request: protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest, protos.google.cloud.datalabeling.v1beta1.IListDatasetsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IDataset>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsrequest), [protos.google.cloud.datalabeling.v1beta1.IListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasets(request, callback)
    
    
    listDatasets(request: protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest, protos.google.cloud.datalabeling.v1beta1.IListDatasetsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IDataset>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsrequest), [protos.google.cloud.datalabeling.v1beta1.IListDatasetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataset)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDatasetsAsync(request, options)
    
    
    listDatasetsAsync(request?: protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.datalabeling.v1beta1.IDataset>;

Equivalent to `listDatasets`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.datalabeling.v1beta1.IDataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.idataset)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataset). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Dataset resource parent, format:
       *  projects/{project_id}
       */
      // const parent = 'abc123'
      /**
       *  Optional. Filter on dataset is not supported at this moment.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer results than
       *  requested. Default value is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results for the server to return.
       *  Typically obtained by
       *  ListDatasetsResponse.next_page_token google.cloud.datalabeling.v1beta1.ListDatasetsResponse.next_page_token  of the previous
       *  DataLabelingService.ListDatasets  call.
       *  Returns the first page if empty.
       */
      // const pageToken = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callListDatasets() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = datalabelingClient.[listDatasetsAsync](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDatasets();
    
    

### listDatasetsStream(request, options)
    
    
    listDatasetsStream(request?: protos.google.cloud.datalabeling.v1beta1.IListDatasetsRequest, options?: CallOptions): Transform;

Equivalent to `listDatasets`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDatasetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistdatasetsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Dataset](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.dataset) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDatasetsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluationJobs(request, options)
    
    
    listEvaluationJobs(request?: protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IEvaluationJob[],
            protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest | null,
            protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsResponse
        ]>;

Lists all evaluation jobs within a project with possible filters. Pagination is supported.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob)[], [protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsrequest) | null, [protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listEvaluationJobsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listEvaluationJobs(request, options, callback)
    
    
    listEvaluationJobs(request: protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest, protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IEvaluationJob>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsrequest), [protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationJobs(request, callback)
    
    
    listEvaluationJobs(request: protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest, protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IEvaluationJob>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsrequest), [protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationJobsAsync(request, options)
    
    
    listEvaluationJobsAsync(request?: protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.datalabeling.v1beta1.IEvaluationJob>;

Equivalent to `listEvaluationJobs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Evaluation job resource parent. Format:
       *  "projects/{project_id}"
       */
      // const parent = 'abc123'
      /**
       *  Optional. You can filter the jobs to list by model_id (also known as
       *  model_name, as described in
       *  EvaluationJob.modelVersion google.cloud.datalabeling.v1beta1.EvaluationJob.model_version) or by
       *  evaluation job state (as described in EvaluationJob.state google.cloud.datalabeling.v1beta1.EvaluationJob.state). To filter
       *  by both criteria, use the `AND` operator or the `OR` operator. For example,
       *  you can use the following string for your filter:
       *  "evaluation_job.model_id = {model_name} AND
       *  evaluation_job.state = {evaluation_job_state}"
       */
      // const filter = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer results than
       *  requested. Default value is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results for the server to return.
       *  Typically obtained by the
       *  nextPageToken google.cloud.datalabeling.v1beta1.ListEvaluationJobsResponse.next_page_token  in the response
       *  to the previous request. The request returns the first page if this is
       *  empty.
       */
      // const pageToken = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callListEvaluationJobs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = datalabelingClient.[listEvaluationJobsAsync](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListEvaluationJobs();
    
    

### listEvaluationJobsStream(request, options)
    
    
    listEvaluationJobsStream(request?: protos.google.cloud.datalabeling.v1beta1.IListEvaluationJobsRequest, options?: CallOptions): Transform;

Equivalent to `listEvaluationJobs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistevaluationjobsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listEvaluationJobsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listExamples(request, options)
    
    
    listExamples(request?: protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IExample[],
            protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest | null,
            protos.google.cloud.datalabeling.v1beta1.IListExamplesResponse
        ]>;

Lists examples in an annotated dataset. Pagination is supported.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IExample](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexample)[], [protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesrequest) | null, [protos.google.cloud.datalabeling.v1beta1.IListExamplesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Example](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.example). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listExamplesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listExamples(request, options, callback)
    
    
    listExamples(request: protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest, protos.google.cloud.datalabeling.v1beta1.IListExamplesResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IExample>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesrequest), [protos.google.cloud.datalabeling.v1beta1.IListExamplesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IExample](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexample)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listExamples(request, callback)
    
    
    listExamples(request: protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest, protos.google.cloud.datalabeling.v1beta1.IListExamplesResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IExample>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesrequest), [protos.google.cloud.datalabeling.v1beta1.IListExamplesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IExample](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexample)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listExamplesAsync(request, options)
    
    
    listExamplesAsync(request?: protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.datalabeling.v1beta1.IExample>;

Equivalent to `listExamples`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.datalabeling.v1beta1.IExample](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iexample)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Example](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.example). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Example resource parent.
       */
      // const parent = 'abc123'
      /**
       *  Optional. An expression for filtering Examples. For annotated datasets that
       *  have annotation spec set, filter by
       *  annotation_spec.display_name is supported. Format
       *  "annotation_spec.display_name = {display_name}"
       */
      // const filter = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer results than
       *  requested. Default value is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results for the server to return.
       *  Typically obtained by
       *  ListExamplesResponse.next_page_token google.cloud.datalabeling.v1beta1.ListExamplesResponse.next_page_token  of the previous
       *  DataLabelingService.ListExamples  call.
       *  Return first page if empty.
       */
      // const pageToken = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callListExamples() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = datalabelingClient.[listExamplesAsync](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListExamples();
    
    

### listExamplesStream(request, options)
    
    
    listExamplesStream(request?: protos.google.cloud.datalabeling.v1beta1.IListExamplesRequest, options?: CallOptions): Transform;

Equivalent to `listExamples`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExamplesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistexamplesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Example](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.example) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listExamplesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listInstructions(request, options)
    
    
    listInstructions(request?: protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IInstruction[],
            protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest | null,
            protos.google.cloud.datalabeling.v1beta1.IListInstructionsResponse
        ]>;

Lists instructions for a project. Pagination is supported.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstructionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IInstruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iinstruction)[], [protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsrequest) | null, [protos.google.cloud.datalabeling.v1beta1.IListInstructionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Instruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.instruction). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listInstructionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listInstructions(request, options, callback)
    
    
    listInstructions(request: protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest, protos.google.cloud.datalabeling.v1beta1.IListInstructionsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IInstruction>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstructionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsrequest), [protos.google.cloud.datalabeling.v1beta1.IListInstructionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IInstruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iinstruction)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstructions(request, callback)
    
    
    listInstructions(request: protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest, protos.google.cloud.datalabeling.v1beta1.IListInstructionsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IInstruction>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstructionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsrequest), [protos.google.cloud.datalabeling.v1beta1.IListInstructionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IInstruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iinstruction)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstructionsAsync(request, options)
    
    
    listInstructionsAsync(request?: protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.datalabeling.v1beta1.IInstruction>;

Equivalent to `listInstructions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstructionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.datalabeling.v1beta1.IInstruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iinstruction)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Instruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.instruction). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Instruction resource parent, format:
       *  projects/{project_id}
       */
      // const parent = 'abc123'
      /**
       *  Optional. Filter is not supported at this moment.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer results than
       *  requested. Default value is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results for the server to return.
       *  Typically obtained by
       *  ListInstructionsResponse.next_page_token google.cloud.datalabeling.v1beta1.ListInstructionsResponse.next_page_token  of the previous
       *  DataLabelingService.ListInstructions  call.
       *  Return first page if empty.
       */
      // const pageToken = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callListInstructions() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = datalabelingClient.[listInstructionsAsync](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListInstructions();
    
    

### listInstructionsStream(request, options)
    
    
    listInstructionsStream(request?: protos.google.cloud.datalabeling.v1beta1.IListInstructionsRequest, options?: CallOptions): Transform;

Equivalent to `listInstructions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstructionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ilistinstructionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Instruction](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.instruction) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listInstructionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAnnotatedDatasetFromAnnotatedDatasetName(annotatedDatasetName)
    
    
    matchAnnotatedDatasetFromAnnotatedDatasetName(annotatedDatasetName: string): string | number;

Parse the annotated_dataset from AnnotatedDataset resource.

**Parameter**  
---  
**Name** | **Description**  
`annotatedDatasetName` |  `string`   
A fully-qualified path representing AnnotatedDataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the annotated_dataset.  
  
### matchAnnotatedDatasetFromExampleName(exampleName)
    
    
    matchAnnotatedDatasetFromExampleName(exampleName: string): string | number;

Parse the annotated_dataset from Example resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleName` |  `string`   
A fully-qualified path representing Example resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the annotated_dataset.  
  
### matchAnnotationSpecSetFromAnnotationSpecSetName(annotationSpecSetName)
    
    
    matchAnnotationSpecSetFromAnnotationSpecSetName(annotationSpecSetName: string): string | number;

Parse the annotation_spec_set from AnnotationSpecSet resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecSetName` |  `string`   
A fully-qualified path representing AnnotationSpecSet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the annotation_spec_set.  
  
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
  
### matchDatasetFromAnnotatedDatasetName(annotatedDatasetName)
    
    
    matchDatasetFromAnnotatedDatasetName(annotatedDatasetName: string): string | number;

Parse the dataset from AnnotatedDataset resource.

**Parameter**  
---  
**Name** | **Description**  
`annotatedDatasetName` |  `string`   
A fully-qualified path representing AnnotatedDataset resource.  
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
  
### matchDatasetFromEvaluationName(evaluationName)
    
    
    matchDatasetFromEvaluationName(evaluationName: string): string | number;

Parse the dataset from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchDatasetFromExampleName(exampleName)
    
    
    matchDatasetFromExampleName(exampleName: string): string | number;

Parse the dataset from Example resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleName` |  `string`   
A fully-qualified path representing Example resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchEvaluationFromEvaluationName(evaluationName)
    
    
    matchEvaluationFromEvaluationName(evaluationName: string): string | number;

Parse the evaluation from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation.  
  
### matchEvaluationJobFromEvaluationJobName(evaluationJobName)
    
    
    matchEvaluationJobFromEvaluationJobName(evaluationJobName: string): string | number;

Parse the evaluation_job from EvaluationJob resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationJobName` |  `string`   
A fully-qualified path representing EvaluationJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation_job.  
  
### matchExampleFromExampleName(exampleName)
    
    
    matchExampleFromExampleName(exampleName: string): string | number;

Parse the example from Example resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleName` |  `string`   
A fully-qualified path representing Example resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the example.  
  
### matchInstructionFromInstructionName(instructionName)
    
    
    matchInstructionFromInstructionName(instructionName: string): string | number;

Parse the instruction from Instruction resource.

**Parameter**  
---  
**Name** | **Description**  
`instructionName` |  `string`   
A fully-qualified path representing Instruction resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the instruction.  
  
### matchProjectFromAnnotatedDatasetName(annotatedDatasetName)
    
    
    matchProjectFromAnnotatedDatasetName(annotatedDatasetName: string): string | number;

Parse the project from AnnotatedDataset resource.

**Parameter**  
---  
**Name** | **Description**  
`annotatedDatasetName` |  `string`   
A fully-qualified path representing AnnotatedDataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAnnotationSpecSetName(annotationSpecSetName)
    
    
    matchProjectFromAnnotationSpecSetName(annotationSpecSetName: string): string | number;

Parse the project from AnnotationSpecSet resource.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecSetName` |  `string`   
A fully-qualified path representing AnnotationSpecSet resource.  
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
  
### matchProjectFromEvaluationJobName(evaluationJobName)
    
    
    matchProjectFromEvaluationJobName(evaluationJobName: string): string | number;

Parse the project from EvaluationJob resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationJobName` |  `string`   
A fully-qualified path representing EvaluationJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEvaluationName(evaluationName)
    
    
    matchProjectFromEvaluationName(evaluationName: string): string | number;

Parse the project from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromExampleName(exampleName)
    
    
    matchProjectFromExampleName(exampleName: string): string | number;

Parse the project from Example resource.

**Parameter**  
---  
**Name** | **Description**  
`exampleName` |  `string`   
A fully-qualified path representing Example resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromInstructionName(instructionName)
    
    
    matchProjectFromInstructionName(instructionName: string): string | number;

Parse the project from Instruction resource.

**Parameter**  
---  
**Name** | **Description**  
`instructionName` |  `string`   
A fully-qualified path representing Instruction resource.  
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
  
### pauseEvaluationJob(request, options)
    
    
    pauseEvaluationJob(request?: protos.google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest | undefined),
            {} | undefined
        ]>;

Pauses an evaluation job. Pausing an evaluation job that is already in a `PAUSED` state is a no-op.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ipauseevaluationjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), ([protos.google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ipauseevaluationjobrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the evaluation job that is going to be paused. Format:
       *  "projects/{project_id}/evaluationJobs/{evaluation_job_id}"
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callPauseEvaluationJob() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.pauseEvaluationJob(request);
        console.log(response);
      }
    
      callPauseEvaluationJob();
    
    

### pauseEvaluationJob(request, options, callback)
    
    
    pauseEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ipauseevaluationjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ipauseevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pauseEvaluationJob(request, callback)
    
    
    pauseEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPauseEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ipauseevaluationjobrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IPauseEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ipauseevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### resumeEvaluationJob(request, options)
    
    
    resumeEvaluationJob(request?: protos.google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest | undefined),
            {} | undefined
        ]>;

Resumes a paused evaluation job. A deleted evaluation job can't be resumed. Resuming a running or scheduled evaluation job is a no-op.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iresumeevaluationjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), ([protos.google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iresumeevaluationjobrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the evaluation job that is going to be resumed. Format:
       *  "projects/{project_id}/evaluationJobs/{evaluation_job_id}"
       */
      // const name = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callResumeEvaluationJob() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await datalabelingClient.resumeEvaluationJob(request);
        console.log(response);
      }
    
      callResumeEvaluationJob();
    
    

### resumeEvaluationJob(request, options, callback)
    
    
    resumeEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iresumeevaluationjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iresumeevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumeEvaluationJob(request, callback)
    
    
    resumeEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumeEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iresumeevaluationjobrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.protobuf.iempty), [protos.google.cloud.datalabeling.v1beta1.IResumeEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iresumeevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchEvaluations(request, options)
    
    
    searchEvaluations(request?: protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IEvaluation[],
            protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest | null,
            protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsResponse
        ]>;

Searches [evaluations](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluation) within a project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluation)[], [protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsrequest) | null, [protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Evaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluation). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `searchEvaluationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### searchEvaluations(request, options, callback)
    
    
    searchEvaluations(request: protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest, protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IEvaluation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsrequest), [protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchEvaluations(request, callback)
    
    
    searchEvaluations(request: protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest, protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.IEvaluation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsrequest), [protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchEvaluationsAsync(request, options)
    
    
    searchEvaluationsAsync(request?: protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.datalabeling.v1beta1.IEvaluation>;

Equivalent to `searchEvaluations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.datalabeling.v1beta1.IEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Evaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluation). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Evaluation search parent (project ID). Format:
       *  "projects/{project_id}"
       */
      // const parent = 'abc123'
      /**
       *  Optional. To search evaluations, you can filter by the following:
       *  * evaluation_job.evaluation_job_id (the last part of
       *    EvaluationJob.name google.cloud.datalabeling.v1beta1.EvaluationJob.name)
       *  * evaluation_job.model_id (the {model_name} portion
       *    of EvaluationJob.modelVersion google.cloud.datalabeling.v1beta1.EvaluationJob.model_version)
       *  * evaluation_job.evaluation_job_run_time_start (Minimum
       *    threshold for the
       *    evaluationJobRunTime google.cloud.datalabeling.v1beta1.Evaluation.evaluation_job_run_time  that created
       *    the evaluation)
       *  * evaluation_job.evaluation_job_run_time_end (Maximum
       *    threshold for the
       *    evaluationJobRunTime google.cloud.datalabeling.v1beta1.Evaluation.evaluation_job_run_time  that created
       *    the evaluation)
       *  * evaluation_job.job_state (EvaluationJob.state google.cloud.datalabeling.v1beta1.EvaluationJob.state)
       *  * annotation_spec.display_name (the Evaluation contains a
       *    metric for the annotation spec with this
       *    displayName google.cloud.datalabeling.v1beta1.AnnotationSpec.display_name)
       *  To filter by multiple critiera, use the `AND` operator or the `OR`
       *  operator. The following examples shows a string that filters by several
       *  critiera:
       *  "evaluation_job.evaluation_job_id =
       *  {evaluation_job_id} AND evaluation_job.model_id =
       *  {model_name} AND
       *  evaluation_job.evaluation_job_run_time_start =
       *  {timestamp_1} AND
       *  evaluation_job.evaluation_job_run_time_end =
       *  {timestamp_2} AND annotation_spec.display_name =
       *  {display_name}"
       */
      // const filter = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer results than
       *  requested. Default value is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results for the server to return.
       *  Typically obtained by the
       *  nextPageToken google.cloud.datalabeling.v1beta1.SearchEvaluationsResponse.next_page_token  of the response
       *  to a previous search request.
       *  If you don't specify this field, the API call requests the first page of
       *  the search.
       */
      // const pageToken = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callSearchEvaluations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = datalabelingClient.[searchEvaluationsAsync](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callSearchEvaluations();
    
    

### searchEvaluationsStream(request, options)
    
    
    searchEvaluationsStream(request?: protos.google.cloud.datalabeling.v1beta1.ISearchEvaluationsRequest, options?: CallOptions): Transform;

Equivalent to `searchEvaluations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchevaluationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Evaluation](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluation) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `searchEvaluationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### searchExampleComparisons(request, options)
    
    
    searchExampleComparisons(request?: protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.SearchExampleComparisonsResponse.IExampleComparison[],
            protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest | null,
            protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsResponse
        ]>;

Searches example comparisons from an evaluation. The return format is a list of example comparisons that show ground truth and prediction(s) for a single input. Search by providing an evaluation ID.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchExampleComparisonsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.SearchExampleComparisonsResponse.IExampleComparison](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.searchexamplecomparisonsresponse.iexamplecomparison)[], [protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsrequest) | null, [protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `searchExampleComparisonsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### searchExampleComparisons(request, options, callback)
    
    
    searchExampleComparisons(request: protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest, protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.SearchExampleComparisonsResponse.IExampleComparison>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchExampleComparisonsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsrequest), [protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.SearchExampleComparisonsResponse.IExampleComparison](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.searchexamplecomparisonsresponse.iexamplecomparison)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchExampleComparisons(request, callback)
    
    
    searchExampleComparisons(request: protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest, callback: PaginationCallback<protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest, protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsResponse | null | undefined, protos.google.cloud.datalabeling.v1beta1.SearchExampleComparisonsResponse.IExampleComparison>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchExampleComparisonsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsrequest), [protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsresponse) | null | undefined, [protos.google.cloud.datalabeling.v1beta1.SearchExampleComparisonsResponse.IExampleComparison](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.searchexamplecomparisonsresponse.iexamplecomparison)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchExampleComparisonsAsync(request, options)
    
    
    searchExampleComparisonsAsync(request?: protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.datalabeling.v1beta1.SearchExampleComparisonsResponse.IExampleComparison>;

Equivalent to `searchExampleComparisons`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchExampleComparisonsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.datalabeling.v1beta1.SearchExampleComparisonsResponse.IExampleComparison](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.searchexamplecomparisonsresponse.iexamplecomparison)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the Evaluation google.cloud.datalabeling.v1beta1.Evaluation  resource to search for example
       *  comparisons from. Format:
       *  "projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}"
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer results than
       *  requested. Default value is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results for the server to return.
       *  Typically obtained by the
       *  nextPageToken SearchExampleComparisons.next_page_token  of the response
       *  to a previous search rquest.
       *  If you don't specify this field, the API call requests the first page of
       *  the search.
       */
      // const pageToken = 'abc123'
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callSearchExampleComparisons() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = datalabelingClient.[searchExampleComparisonsAsync](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/v1beta1.datalabelingserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callSearchExampleComparisons();
    
    

### searchExampleComparisonsStream(request, options)
    
    
    searchExampleComparisonsStream(request?: protos.google.cloud.datalabeling.v1beta1.ISearchExampleComparisonsRequest, options?: CallOptions): Transform;

Equivalent to `searchExampleComparisons`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchExampleComparisonsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.isearchexamplecomparisonsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `searchExampleComparisonsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### updateEvaluationJob(request, options)
    
    
    updateEvaluationJob(request?: protos.google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest, options?: CallOptions): Promise<[
            protos.google.cloud.datalabeling.v1beta1.IEvaluationJob,
            (protos.google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest | undefined),
            {} | undefined
        ]>;

Updates an evaluation job. You can only update certain fields of the job's [EvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjobconfig): `humanAnnotationConfig.instruction`, `exampleCount`, and `exampleSamplePercentage`.

If you want to change any other aspect of the evaluation job, you must delete the job and create a new one.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iupdateevaluationjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob), ([protos.google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iupdateevaluationjobrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Evaluation job that is going to be updated.
       */
      // const evaluationJob = {}
      /**
       *  Optional. Mask for which fields to update. You can only provide the
       *  following fields:
       *  * `evaluationJobConfig.humanAnnotationConfig.instruction`
       *  * `evaluationJobConfig.exampleCount`
       *  * `evaluationJobConfig.exampleSamplePercentage`
       *  You can provide more than one of these fields by separating them with
       *  commas.
       */
      // const updateMask = {}
    
      // Imports the Datalabeling library
      const {DataLabelingServiceClient} = require('[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const datalabelingClient = new [DataLabelingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)();
    
      async function callUpdateEvaluationJob() {
        // Construct request
        const request = {
          evaluationJob,
        };
    
        // Run request
        const response = await datalabelingClient.updateEvaluationJob(request);
        console.log(response);
      }
    
      callUpdateEvaluationJob();
    
    

### updateEvaluationJob(request, options, callback)
    
    
    updateEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest, options: CallOptions, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IEvaluationJob, protos.google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iupdateevaluationjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob), [protos.google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iupdateevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEvaluationJob(request, callback)
    
    
    updateEvaluationJob(request: protos.google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest, callback: Callback<protos.google.cloud.datalabeling.v1beta1.IEvaluationJob, protos.google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iupdateevaluationjobrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.datalabeling.v1beta1.IEvaluationJob](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjob), [protos.google.cloud.datalabeling.v1beta1.IUpdateEvaluationJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.iupdateevaluationjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
