---
url: https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/v1beta.dataobjectserviceclient
title: Class v1beta.DataObjectServiceClient (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:05.347850+00:00
---

# Class v1beta.DataObjectServiceClient (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/v1beta.dataobjectserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.DataObjectServiceClient (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.13.0  0.8.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 

Service for creating and managing data objects. v1beta

## Package

[@google-cloud/vectorsearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DataObjectServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DataObjectServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### dataObjectServiceStub
    
    
    dataObjectServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### descriptors
    
    
    descriptors: Descriptors;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### locationsClient
    
    
    locationsClient: LocationsClient;

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

### batchCreateDataObjects(request, options)
    
    
    batchCreateDataObjects(request?: protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsResponse,
            (protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsRequest | undefined),
            {} | undefined
        ]>;

Creates a batch of dataObjects.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchcreatedataobjectsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchcreatedataobjectsresponse), ([protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchcreatedataobjectsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchCreateDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.batchcreatedataobjectsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Collection to create the DataObjects in.
       *  Format: `projects/{project}/locations/{location}/collections/{collection}`.
       *  The parent field in the CreateDataObjectRequest messages must match this
       *  field.
       */
      // const parent = 'abc123'
      /**
       *  Required. The request message specifying the resources to create.
       *  A maximum of 1000 DataObjects can be created in a batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Vectorsearch library
      const {DataObjectServiceClient} = require('[@google-cloud/vectorsearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const vectorsearchClient = new [DataObjectServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)();
    
      async function callBatchCreateDataObjects() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const response = await vectorsearchClient.batchCreateDataObjects(request);
        console.log(response);
      }
    
      callBatchCreateDataObjects();
    
    

### batchCreateDataObjects(request, options, callback)
    
    
    batchCreateDataObjects(request: protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsRequest, options: CallOptions, callback: Callback<protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsResponse, protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchcreatedataobjectsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchcreatedataobjectsresponse), [protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchcreatedataobjectsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateDataObjects(request, callback)
    
    
    batchCreateDataObjects(request: protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsRequest, callback: Callback<protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsResponse, protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchcreatedataobjectsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchcreatedataobjectsresponse), [protos.google.cloud.vectorsearch.v1beta.IBatchCreateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchcreatedataobjectsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteDataObjects(request, options)
    
    
    batchDeleteDataObjects(request?: protos.google.cloud.vectorsearch.v1beta.IBatchDeleteDataObjectsRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.vectorsearch.v1beta.IBatchDeleteDataObjectsRequest | undefined),
            {} | undefined
        ]>;

Deletes dataObjects in a batch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchdeletedataobjectsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.protobuf.iempty), ([protos.google.cloud.vectorsearch.v1beta.IBatchDeleteDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchdeletedataobjectsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Collection to delete the DataObjects in.
       *  Format: `projects/{project}/locations/{location}/collections/{collection}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The request message specifying the resources to delete.
       *  A maximum of 1000 DataObjects can be deleted in a batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Vectorsearch library
      const {DataObjectServiceClient} = require('[@google-cloud/vectorsearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const vectorsearchClient = new [DataObjectServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)();
    
      async function callBatchDeleteDataObjects() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const response = await vectorsearchClient.batchDeleteDataObjects(request);
        console.log(response);
      }
    
      callBatchDeleteDataObjects();
    
    

### batchDeleteDataObjects(request, options, callback)
    
    
    batchDeleteDataObjects(request: protos.google.cloud.vectorsearch.v1beta.IBatchDeleteDataObjectsRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.vectorsearch.v1beta.IBatchDeleteDataObjectsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchdeletedataobjectsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.protobuf.iempty), [protos.google.cloud.vectorsearch.v1beta.IBatchDeleteDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchdeletedataobjectsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteDataObjects(request, callback)
    
    
    batchDeleteDataObjects(request: protos.google.cloud.vectorsearch.v1beta.IBatchDeleteDataObjectsRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.vectorsearch.v1beta.IBatchDeleteDataObjectsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchdeletedataobjectsrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.protobuf.iempty), [protos.google.cloud.vectorsearch.v1beta.IBatchDeleteDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchdeletedataobjectsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateDataObjects(request, options)
    
    
    batchUpdateDataObjects(request?: protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsResponse,
            (protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsRequest | undefined),
            {} | undefined
        ]>;

Updates dataObjects in a batch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchupdatedataobjectsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchupdatedataobjectsresponse), ([protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchupdatedataobjectsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchUpdateDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.batchupdatedataobjectsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Collection to update the DataObjects in.
       *  Format: `projects/{project}/locations/{location}/collections/{collection}`.
       *  The parent field in the UpdateDataObjectRequest messages must match this
       *  field.
       */
      // const parent = 'abc123'
      /**
       *  Required. The request message specifying the resources to update.
       *  A maximum of 1000 DataObjects can be updated in a batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Vectorsearch library
      const {DataObjectServiceClient} = require('[@google-cloud/vectorsearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const vectorsearchClient = new [DataObjectServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)();
    
      async function callBatchUpdateDataObjects() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const response = await vectorsearchClient.batchUpdateDataObjects(request);
        console.log(response);
      }
    
      callBatchUpdateDataObjects();
    
    

### batchUpdateDataObjects(request, options, callback)
    
    
    batchUpdateDataObjects(request: protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsRequest, options: CallOptions, callback: Callback<protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsResponse, protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchupdatedataobjectsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchupdatedataobjectsresponse), [protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchupdatedataobjectsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateDataObjects(request, callback)
    
    
    batchUpdateDataObjects(request: protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsRequest, callback: Callback<protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsResponse, protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchupdatedataobjectsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsResponse](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchupdatedataobjectsresponse), [protos.google.cloud.vectorsearch.v1beta.IBatchUpdateDataObjectsRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ibatchupdatedataobjectsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### collectionPath(project, location, collection)
    
    
    collectionPath(project: string, location: string, collection: string): string;

Return a fully-qualified collection resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createDataObject(request, options)
    
    
    createDataObject(request?: protos.google.cloud.vectorsearch.v1beta.ICreateDataObjectRequest, options?: CallOptions): Promise<[
            protos.google.cloud.vectorsearch.v1beta.IDataObject,
            (protos.google.cloud.vectorsearch.v1beta.ICreateDataObjectRequest | undefined),
            {} | undefined
        ]>;

Creates a dataObject.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.icreatedataobjectrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.vectorsearch.v1beta.IDataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.idataobject), ([protos.google.cloud.vectorsearch.v1beta.ICreateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.icreatedataobjectrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.dataobject). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Collection to create the DataObject in.
       *  Format: `projects/{project}/locations/{location}/collections/{collection}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The id of the dataObject to create.
       *  The id must be 1-63 characters long, and comply with
       *  RFC1035 (https://www.ietf.org/rfc/rfc1035.txt).
       *  Specifically, it must be 1-63 characters long and match the regular
       *  expression `[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?`.
       */
      // const dataObjectId = 'abc123'
      /**
       *  Required. The DataObject to create.
       */
      // const dataObject = {}
    
      // Imports the Vectorsearch library
      const {DataObjectServiceClient} = require('[@google-cloud/vectorsearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const vectorsearchClient = new [DataObjectServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)();
    
      async function callCreateDataObject() {
        // Construct request
        const request = {
          parent,
          dataObjectId,
          dataObject,
        };
    
        // Run request
        const response = await vectorsearchClient.createDataObject(request);
        console.log(response);
      }
    
      callCreateDataObject();
    
    

### createDataObject(request, options, callback)
    
    
    createDataObject(request: protos.google.cloud.vectorsearch.v1beta.ICreateDataObjectRequest, options: CallOptions, callback: Callback<protos.google.cloud.vectorsearch.v1beta.IDataObject, protos.google.cloud.vectorsearch.v1beta.ICreateDataObjectRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.icreatedataobjectrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.vectorsearch.v1beta.IDataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.idataobject), [protos.google.cloud.vectorsearch.v1beta.ICreateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.icreatedataobjectrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataObject(request, callback)
    
    
    createDataObject(request: protos.google.cloud.vectorsearch.v1beta.ICreateDataObjectRequest, callback: Callback<protos.google.cloud.vectorsearch.v1beta.IDataObject, protos.google.cloud.vectorsearch.v1beta.ICreateDataObjectRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.icreatedataobjectrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.vectorsearch.v1beta.IDataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.idataobject), [protos.google.cloud.vectorsearch.v1beta.ICreateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.icreatedataobjectrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### dataObjectPath(project, location, collection, dataObject)
    
    
    dataObjectPath(project: string, location: string, collection: string, dataObject: string): string;

Return a fully-qualified dataObject resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataObject` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteDataObject(request, options)
    
    
    deleteDataObject(request?: protos.google.cloud.vectorsearch.v1beta.IDeleteDataObjectRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.vectorsearch.v1beta.IDeleteDataObjectRequest | undefined),
            {} | undefined
        ]>;

Deletes a dataObject.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ideletedataobjectrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.protobuf.iempty), ([protos.google.cloud.vectorsearch.v1beta.IDeleteDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ideletedataobjectrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the DataObject resource to be deleted.
       *  Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}`
       */
      // const name = 'abc123'
      /**
       *  Optional. The current etag of the DataObject.
       *  If an etag is provided and does not match the current etag of the
       *  DataObject, deletion will be blocked and an ABORTED error will be returned.
       */
      // const etag = 'abc123'
    
      // Imports the Vectorsearch library
      const {DataObjectServiceClient} = require('[@google-cloud/vectorsearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const vectorsearchClient = new [DataObjectServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)();
    
      async function callDeleteDataObject() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await vectorsearchClient.deleteDataObject(request);
        console.log(response);
      }
    
      callDeleteDataObject();
    
    

### deleteDataObject(request, options, callback)
    
    
    deleteDataObject(request: protos.google.cloud.vectorsearch.v1beta.IDeleteDataObjectRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.vectorsearch.v1beta.IDeleteDataObjectRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ideletedataobjectrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.protobuf.iempty), [protos.google.cloud.vectorsearch.v1beta.IDeleteDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ideletedataobjectrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataObject(request, callback)
    
    
    deleteDataObject(request: protos.google.cloud.vectorsearch.v1beta.IDeleteDataObjectRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.vectorsearch.v1beta.IDeleteDataObjectRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ideletedataobjectrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.protobuf.iempty), [protos.google.cloud.vectorsearch.v1beta.IDeleteDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.ideletedataobjectrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataObject(request, options)
    
    
    getDataObject(request?: protos.google.cloud.vectorsearch.v1beta.IGetDataObjectRequest, options?: CallOptions): Promise<[
            protos.google.cloud.vectorsearch.v1beta.IDataObject,
            protos.google.cloud.vectorsearch.v1beta.IGetDataObjectRequest | undefined,
            {} | undefined
        ]>;

Gets a data object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.igetdataobjectrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.vectorsearch.v1beta.IDataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.idataobject), [protos.google.cloud.vectorsearch.v1beta.IGetDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.igetdataobjectrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.dataobject). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the DataObject resource.
       *  Format:
       *  `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}`
       */
      // const name = 'abc123'
    
      // Imports the Vectorsearch library
      const {DataObjectServiceClient} = require('[@google-cloud/vectorsearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const vectorsearchClient = new [DataObjectServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)();
    
      async function callGetDataObject() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await vectorsearchClient.getDataObject(request);
        console.log(response);
      }
    
      callGetDataObject();
    
    

### getDataObject(request, options, callback)
    
    
    getDataObject(request: protos.google.cloud.vectorsearch.v1beta.IGetDataObjectRequest, options: CallOptions, callback: Callback<protos.google.cloud.vectorsearch.v1beta.IDataObject, protos.google.cloud.vectorsearch.v1beta.IGetDataObjectRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.igetdataobjectrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.vectorsearch.v1beta.IDataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.idataobject), [protos.google.cloud.vectorsearch.v1beta.IGetDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.igetdataobjectrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataObject(request, callback)
    
    
    getDataObject(request: protos.google.cloud.vectorsearch.v1beta.IGetDataObjectRequest, callback: Callback<protos.google.cloud.vectorsearch.v1beta.IDataObject, protos.google.cloud.vectorsearch.v1beta.IGetDataObjectRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.igetdataobjectrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.vectorsearch.v1beta.IDataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.idataobject), [protos.google.cloud.vectorsearch.v1beta.IGetDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.igetdataobjectrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### indexPath(project, location, collection, index)
    
    
    indexPath(project: string, location: string, collection: string, index: string): string;

Return a fully-qualified index resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
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
    

### matchCollectionFromCollectionName(collectionName)
    
    
    matchCollectionFromCollectionName(collectionName: string): string | number;

Parse the collection from Collection resource.

**Parameter**  
---  
**Name** | **Description**  
`collectionName` |  `string`   
A fully-qualified path representing Collection resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromDataObjectName(dataObjectName)
    
    
    matchCollectionFromDataObjectName(dataObjectName: string): string | number;

Parse the collection from DataObject resource.

**Parameter**  
---  
**Name** | **Description**  
`dataObjectName` |  `string`   
A fully-qualified path representing DataObject resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromIndexName(indexName)
    
    
    matchCollectionFromIndexName(indexName: string): string | number;

Parse the collection from Index resource.

**Parameter**  
---  
**Name** | **Description**  
`indexName` |  `string`   
A fully-qualified path representing Index resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchDataObjectFromDataObjectName(dataObjectName)
    
    
    matchDataObjectFromDataObjectName(dataObjectName: string): string | number;

Parse the dataObject from DataObject resource.

**Parameter**  
---  
**Name** | **Description**  
`dataObjectName` |  `string`   
A fully-qualified path representing DataObject resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataObject.  
  
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
  
### matchLocationFromCollectionName(collectionName)
    
    
    matchLocationFromCollectionName(collectionName: string): string | number;

Parse the location from Collection resource.

**Parameter**  
---  
**Name** | **Description**  
`collectionName` |  `string`   
A fully-qualified path representing Collection resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDataObjectName(dataObjectName)
    
    
    matchLocationFromDataObjectName(dataObjectName: string): string | number;

Parse the location from DataObject resource.

**Parameter**  
---  
**Name** | **Description**  
`dataObjectName` |  `string`   
A fully-qualified path representing DataObject resource.  
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
  
### matchProjectFromCollectionName(collectionName)
    
    
    matchProjectFromCollectionName(collectionName: string): string | number;

Parse the project from Collection resource.

**Parameter**  
---  
**Name** | **Description**  
`collectionName` |  `string`   
A fully-qualified path representing Collection resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDataObjectName(dataObjectName)
    
    
    matchProjectFromDataObjectName(dataObjectName: string): string | number;

Parse the project from DataObject resource.

**Parameter**  
---  
**Name** | **Description**  
`dataObjectName` |  `string`   
A fully-qualified path representing DataObject resource.  
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
  
### updateDataObject(request, options)
    
    
    updateDataObject(request?: protos.google.cloud.vectorsearch.v1beta.IUpdateDataObjectRequest, options?: CallOptions): Promise<[
            protos.google.cloud.vectorsearch.v1beta.IDataObject,
            (protos.google.cloud.vectorsearch.v1beta.IUpdateDataObjectRequest | undefined),
            {} | undefined
        ]>;

Updates a dataObject.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.iupdatedataobjectrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.vectorsearch.v1beta.IDataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.idataobject), ([protos.google.cloud.vectorsearch.v1beta.IUpdateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.iupdatedataobjectrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.dataobject). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The DataObject which replaces the resource on the server.
       */
      // const dataObject = {}
      /**
       *  Optional. The update mask applies to the resource. See
       *  google.protobuf.FieldMask google.protobuf.FieldMask.
       */
      // const updateMask = {}
    
      // Imports the Vectorsearch library
      const {DataObjectServiceClient} = require('[@google-cloud/vectorsearch](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const vectorsearchClient = new [DataObjectServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/overview.html)();
    
      async function callUpdateDataObject() {
        // Construct request
        const request = {
          dataObject,
        };
    
        // Run request
        const response = await vectorsearchClient.updateDataObject(request);
        console.log(response);
      }
    
      callUpdateDataObject();
    
    

### updateDataObject(request, options, callback)
    
    
    updateDataObject(request: protos.google.cloud.vectorsearch.v1beta.IUpdateDataObjectRequest, options: CallOptions, callback: Callback<protos.google.cloud.vectorsearch.v1beta.IDataObject, protos.google.cloud.vectorsearch.v1beta.IUpdateDataObjectRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.iupdatedataobjectrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.vectorsearch.v1beta.IDataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.idataobject), [protos.google.cloud.vectorsearch.v1beta.IUpdateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.iupdatedataobjectrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataObject(request, callback)
    
    
    updateDataObject(request: protos.google.cloud.vectorsearch.v1beta.IUpdateDataObjectRequest, callback: Callback<protos.google.cloud.vectorsearch.v1beta.IDataObject, protos.google.cloud.vectorsearch.v1beta.IUpdateDataObjectRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.iupdatedataobjectrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.vectorsearch.v1beta.IDataObject](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.idataobject), [protos.google.cloud.vectorsearch.v1beta.IUpdateDataObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/vectorsearch/latest/vectorsearch/protos.google.cloud.vectorsearch.v1beta.iupdatedataobjectrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
