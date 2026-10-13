---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/v1alpha.sitesearchengineserviceclient
title: Class v1alpha.SiteSearchEngineServiceClient (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:02:17.636644+00:00
---

# Class v1alpha.SiteSearchEngineServiceClient (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/v1alpha.sitesearchengineserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.SiteSearchEngineServiceClient (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Service for managing site search related resources. v1alpha

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of SiteSearchEngineServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new SiteSearchEngineServiceClient({fallback: true}, gax); ```  
  
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

### siteSearchEngineServiceStub
    
    
    siteSearchEngineServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### aclConfigPath(project, location)
    
    
    aclConfigPath(project: string, location: string): string;

Return a fully-qualified aclConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### batchCreateTargetSites(request, options)
    
    
    batchCreateTargetSites(request?: protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSitesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSitesResponse, protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSiteMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates in a batch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchcreatetargetsitesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchcreatetargetsitesresponse), [protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchcreatetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource shared by all TargetSites being created.
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.
       *  The parent field in the CreateBookRequest messages must either be empty or
       *  match this field.
       */
      // const parent = 'abc123'
      /**
       *  Required. The request message specifying the resources to create.
       *  A maximum of 20 TargetSites can be created in a batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callBatchCreateTargetSites() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.batchCreateTargetSites(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchCreateTargetSites();
    
    

### batchCreateTargetSites(request, options, callback)
    
    
    batchCreateTargetSites(request: protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSitesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSitesResponse, protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSiteMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchcreatetargetsitesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchcreatetargetsitesresponse), [protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchcreatetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateTargetSites(request, callback)
    
    
    batchCreateTargetSites(request: protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSitesRequest, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSitesResponse, protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSiteMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchcreatetargetsitesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchcreatetargetsitesresponse), [protos.google.cloud.discoveryengine.v1alpha.IBatchCreateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchcreatetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchVerifyTargetSites(request, options)
    
    
    batchVerifyTargetSites(request?: protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesResponse, protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Verify target sites' ownership and validity. This API sends all the target sites under site search engine for verification.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchVerifyTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchverifytargetsitesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchverifytargetsitesresponse), [protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchverifytargetsitesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource shared by all TargetSites being verified.
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.
       */
      // const parent = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callBatchVerifyTargetSites() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.batchVerifyTargetSites(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchVerifyTargetSites();
    
    

### batchVerifyTargetSites(request, options, callback)
    
    
    batchVerifyTargetSites(request: protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesResponse, protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchVerifyTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchverifytargetsitesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchverifytargetsitesresponse), [protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchverifytargetsitesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchVerifyTargetSites(request, callback)
    
    
    batchVerifyTargetSites(request: protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesRequest, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesResponse, protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchVerifyTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchverifytargetsitesrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchverifytargetsitesresponse), [protos.google.cloud.discoveryengine.v1alpha.IBatchVerifyTargetSitesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ibatchverifytargetsitesmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkBatchCreateTargetSitesProgress(name)
    
    
    checkBatchCreateTargetSitesProgress(name: string): Promise<LROperation<protos.google.cloud.discoveryengine.v1alpha.BatchCreateTargetSitesResponse, protos.google.cloud.discoveryengine.v1alpha.BatchCreateTargetSiteMetadata>>;

Check the status of the long running operation returned by `batchCreateTargetSites()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.discoveryengine.v1alpha.BatchCreateTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.batchcreatetargetsitesresponse), [protos.google.cloud.discoveryengine.v1alpha.BatchCreateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.batchcreatetargetsitemetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource shared by all TargetSites being created.
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.
       *  The parent field in the CreateBookRequest messages must either be empty or
       *  match this field.
       */
      // const parent = 'abc123'
      /**
       *  Required. The request message specifying the resources to create.
       *  A maximum of 20 TargetSites can be created in a batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callBatchCreateTargetSites() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.batchCreateTargetSites(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchCreateTargetSites();
    
    

### checkBatchVerifyTargetSitesProgress(name)
    
    
    checkBatchVerifyTargetSitesProgress(name: string): Promise<LROperation<protos.google.cloud.discoveryengine.v1alpha.BatchVerifyTargetSitesResponse, protos.google.cloud.discoveryengine.v1alpha.BatchVerifyTargetSitesMetadata>>;

Check the status of the long running operation returned by `batchVerifyTargetSites()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.discoveryengine.v1alpha.BatchVerifyTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.batchverifytargetsitesresponse), [protos.google.cloud.discoveryengine.v1alpha.BatchVerifyTargetSitesMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.batchverifytargetsitesmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource shared by all TargetSites being verified.
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.
       */
      // const parent = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callBatchVerifyTargetSites() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.batchVerifyTargetSites(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callBatchVerifyTargetSites();
    
    

### checkCreateTargetSiteProgress(name)
    
    
    checkCreateTargetSiteProgress(name: string): Promise<LROperation<protos.google.cloud.discoveryengine.v1alpha.TargetSite, protos.google.cloud.discoveryengine.v1alpha.CreateTargetSiteMetadata>>;

Check the status of the long running operation returned by `createTargetSite()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.discoveryengine.v1alpha.TargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.targetsite-class), [protos.google.cloud.discoveryengine.v1alpha.CreateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.createtargetsitemetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent resource name of
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite, such as
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The TargetSite google.cloud.discoveryengine.v1alpha.TargetSite 
       *  to create.
       */
      // const targetSite = {}
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callCreateTargetSite() {
        // Construct request
        const request = {
          parent,
          targetSite,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.createTargetSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateTargetSite();
    
    

### checkDeleteTargetSiteProgress(name)
    
    
    checkDeleteTargetSiteProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.discoveryengine.v1alpha.DeleteTargetSiteMetadata>>;

Check the status of the long running operation returned by `deleteTargetSite()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), [protos.google.cloud.discoveryengine.v1alpha.DeleteTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.deletetargetsitemetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite, such as
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`.
       *  If the caller does not have permission to access the
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite, regardless
       *  of whether or not it exists, a PERMISSION_DENIED error is returned.
       *  If the requested
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite  does not
       *  exist, a NOT_FOUND error is returned.
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callDeleteTargetSite() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.deleteTargetSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTargetSite();
    
    

### checkDisableAdvancedSiteSearchProgress(name)
    
    
    checkDisableAdvancedSiteSearchProgress(name: string): Promise<LROperation<protos.google.cloud.discoveryengine.v1alpha.DisableAdvancedSiteSearchResponse, protos.google.cloud.discoveryengine.v1alpha.DisableAdvancedSiteSearchMetadata>>;

Check the status of the long running operation returned by `disableAdvancedSiteSearch()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.discoveryengine.v1alpha.DisableAdvancedSiteSearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.disableadvancedsitesearchresponse), [protos.google.cloud.discoveryengine.v1alpha.DisableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.disableadvancedsitesearchmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of the
       *  SiteSearchEngine google.cloud.discoveryengine.v1alpha.SiteSearchEngine,
       *  such as
       *  `projects/{project}/locations/{location}/dataStores/{data_store_id}/siteSearchEngine`.
       */
      // const siteSearchEngine = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callDisableAdvancedSiteSearch() {
        // Construct request
        const request = {
          siteSearchEngine,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.disableAdvancedSiteSearch(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDisableAdvancedSiteSearch();
    
    

### checkEnableAdvancedSiteSearchProgress(name)
    
    
    checkEnableAdvancedSiteSearchProgress(name: string): Promise<LROperation<protos.google.cloud.discoveryengine.v1alpha.EnableAdvancedSiteSearchResponse, protos.google.cloud.discoveryengine.v1alpha.EnableAdvancedSiteSearchMetadata>>;

Check the status of the long running operation returned by `enableAdvancedSiteSearch()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.discoveryengine.v1alpha.EnableAdvancedSiteSearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.enableadvancedsitesearchresponse), [protos.google.cloud.discoveryengine.v1alpha.EnableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.enableadvancedsitesearchmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of the
       *  SiteSearchEngine google.cloud.discoveryengine.v1alpha.SiteSearchEngine,
       *  such as
       *  `projects/{project}/locations/{location}/dataStores/{data_store_id}/siteSearchEngine`.
       */
      // const siteSearchEngine = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callEnableAdvancedSiteSearch() {
        // Construct request
        const request = {
          siteSearchEngine,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.enableAdvancedSiteSearch(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callEnableAdvancedSiteSearch();
    
    

### checkRecrawlUrisProgress(name)
    
    
    checkRecrawlUrisProgress(name: string): Promise<LROperation<protos.google.cloud.discoveryengine.v1alpha.RecrawlUrisResponse, protos.google.cloud.discoveryengine.v1alpha.RecrawlUrisMetadata>>;

Check the status of the long running operation returned by `recrawlUris()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.discoveryengine.v1alpha.RecrawlUrisResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.recrawlurisresponse-class), [protos.google.cloud.discoveryengine.v1alpha.RecrawlUrisMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.recrawlurismetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of the
       *  SiteSearchEngine google.cloud.discoveryengine.v1alpha.SiteSearchEngine,
       *  such as
       *  `projects/* /locations/* /collections/* /dataStores/* /siteSearchEngine`.
       */
      // const siteSearchEngine = 'abc123'
      /**
       *  Required. List of URIs to crawl. At most 10K URIs are supported, otherwise
       *  an INVALID_ARGUMENT error is thrown. Each URI should match at least one
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite  in
       *  `site_search_engine`.
       */
      // const uris = ['abc','def']
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callRecrawlUris() {
        // Construct request
        const request = {
          siteSearchEngine,
          uris,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.recrawlUris(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRecrawlUris();
    
    

### checkSetUriPatternDocumentDataProgress(name)
    
    
    checkSetUriPatternDocumentDataProgress(name: string): Promise<LROperation<protos.google.cloud.discoveryengine.v1alpha.SetUriPatternDocumentDataResponse, protos.google.cloud.discoveryengine.v1alpha.SetUriPatternDocumentDataMetadata>>;

Check the status of the long running operation returned by `setUriPatternDocumentData()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.discoveryengine.v1alpha.SetUriPatternDocumentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.seturipatterndocumentdataresponse), [protos.google.cloud.discoveryengine.v1alpha.SetUriPatternDocumentDataMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.seturipatterndocumentdatametadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of the
       *  SiteSearchEngine google.cloud.discoveryengine.v1alpha.SiteSearchEngine,
       *  such as
       *  `projects/* /locations/* /collections/* /dataStores/* /siteSearchEngine`.
       */
      // const siteSearchEngine = 'abc123'
      /**
       *  Document data keyed by URI pattern. Each entry must be consistent with
       *  the Schema google.cloud.discoveryengine.v1alpha.Schema. For example:
       *  Schema google.cloud.discoveryengine.v1alpha.Schema  = {
       *  "type": "object",
       *  "properties": {
       *    "Categories": {
       *      "type": "array",
       *      "items": {
       *        "retrievable": true,
       *        "type": "string"
       *      }
       *    }
       *  }
       *  document_data_map = {
       *    "www.url1.com/*": {
       *      "Categories": "category1", "category2" 
       *    },
       *    "www.url2.com/*": {
       *      "Categories": "category3" 
       *    }
       *  }
       */
      // const documentDataMap = [1,2,3,4]
      /**
       *  If true, clears the document data map. If true,
       *  SetUriPatternDocumentDataRequest.document_data_map google.cloud.discoveryengine.v1alpha.SetUriPatternDocumentDataRequest.document_data_map 
       *  must be empty.
       */
      // const emptyDocumentDataMap = true
      /**
       *  Optional. If not provided, the current
       *  Schema google.cloud.discoveryengine.v1alpha.Schema  is used. If provided,
       *  validates and updates the
       *  Schema google.cloud.discoveryengine.v1alpha.Schema. If validation fails,
       *  an error is returned.
       */
      // const schema = {}
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callSetUriPatternDocumentData() {
        // Construct request
        const request = {
          siteSearchEngine,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.setUriPatternDocumentData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSetUriPatternDocumentData();
    
    

### checkUpdateTargetSiteProgress(name)
    
    
    checkUpdateTargetSiteProgress(name: string): Promise<LROperation<protos.google.cloud.discoveryengine.v1alpha.TargetSite, protos.google.cloud.discoveryengine.v1alpha.UpdateTargetSiteMetadata>>;

Check the status of the long running operation returned by `updateTargetSite()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.discoveryengine.v1alpha.TargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.targetsite-class), [protos.google.cloud.discoveryengine.v1alpha.UpdateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.updatetargetsitemetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The target site to update.
       *  If the caller does not have permission to update the
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite, regardless
       *  of whether or not it exists, a PERMISSION_DENIED error is returned.
       *  If the TargetSite google.cloud.discoveryengine.v1alpha.TargetSite  to
       *  update does not exist, a NOT_FOUND error is returned.
       */
      // const targetSite = {}
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callUpdateTargetSite() {
        // Construct request
        const request = {
          targetSite,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.updateTargetSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateTargetSite();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createTargetSite(request, options)
    
    
    createTargetSite(request?: protos.google.cloud.discoveryengine.v1alpha.ICreateTargetSiteRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.discoveryengine.v1alpha.ITargetSite, protos.google.cloud.discoveryengine.v1alpha.ICreateTargetSiteMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreatetargetsiterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite), [protos.google.cloud.discoveryengine.v1alpha.ICreateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreatetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent resource name of
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite, such as
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The TargetSite google.cloud.discoveryengine.v1alpha.TargetSite 
       *  to create.
       */
      // const targetSite = {}
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callCreateTargetSite() {
        // Construct request
        const request = {
          parent,
          targetSite,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.createTargetSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateTargetSite();
    
    

### createTargetSite(request, options, callback)
    
    
    createTargetSite(request: protos.google.cloud.discoveryengine.v1alpha.ICreateTargetSiteRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.ITargetSite, protos.google.cloud.discoveryengine.v1alpha.ICreateTargetSiteMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreatetargetsiterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite), [protos.google.cloud.discoveryengine.v1alpha.ICreateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreatetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTargetSite(request, callback)
    
    
    createTargetSite(request: protos.google.cloud.discoveryengine.v1alpha.ICreateTargetSiteRequest, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.ITargetSite, protos.google.cloud.discoveryengine.v1alpha.ICreateTargetSiteMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreatetargetsiterequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite), [protos.google.cloud.discoveryengine.v1alpha.ICreateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.icreatetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deleteTargetSite(request, options)
    
    
    deleteTargetSite(request?: protos.google.cloud.discoveryengine.v1alpha.IDeleteTargetSiteRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1alpha.IDeleteTargetSiteMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ideletetargetsiterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1alpha.IDeleteTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ideletetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite, such as
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`.
       *  If the caller does not have permission to access the
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite, regardless
       *  of whether or not it exists, a PERMISSION_DENIED error is returned.
       *  If the requested
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite  does not
       *  exist, a NOT_FOUND error is returned.
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callDeleteTargetSite() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.deleteTargetSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTargetSite();
    
    

### deleteTargetSite(request, options, callback)
    
    
    deleteTargetSite(request: protos.google.cloud.discoveryengine.v1alpha.IDeleteTargetSiteRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1alpha.IDeleteTargetSiteMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ideletetargetsiterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1alpha.IDeleteTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ideletetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTargetSite(request, callback)
    
    
    deleteTargetSite(request: protos.google.cloud.discoveryengine.v1alpha.IDeleteTargetSiteRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1alpha.IDeleteTargetSiteMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ideletetargetsiterequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1alpha.IDeleteTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ideletetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disableAdvancedSiteSearch(request, options)
    
    
    disableAdvancedSiteSearch(request?: protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchResponse, protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Downgrade from advanced site search to basic site search.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.idisableadvancedsitesearchrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.idisableadvancedsitesearchresponse), [protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.idisableadvancedsitesearchmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of the
       *  SiteSearchEngine google.cloud.discoveryengine.v1alpha.SiteSearchEngine,
       *  such as
       *  `projects/{project}/locations/{location}/dataStores/{data_store_id}/siteSearchEngine`.
       */
      // const siteSearchEngine = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callDisableAdvancedSiteSearch() {
        // Construct request
        const request = {
          siteSearchEngine,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.disableAdvancedSiteSearch(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDisableAdvancedSiteSearch();
    
    

### disableAdvancedSiteSearch(request, options, callback)
    
    
    disableAdvancedSiteSearch(request: protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchResponse, protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.idisableadvancedsitesearchrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.idisableadvancedsitesearchresponse), [protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.idisableadvancedsitesearchmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disableAdvancedSiteSearch(request, callback)
    
    
    disableAdvancedSiteSearch(request: protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchRequest, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchResponse, protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.idisableadvancedsitesearchrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.idisableadvancedsitesearchresponse), [protos.google.cloud.discoveryengine.v1alpha.IDisableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.idisableadvancedsitesearchmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enableAdvancedSiteSearch(request, options)
    
    
    enableAdvancedSiteSearch(request?: protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchResponse, protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Upgrade from basic site search to advanced site search.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ienableadvancedsitesearchrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ienableadvancedsitesearchresponse), [protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ienableadvancedsitesearchmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of the
       *  SiteSearchEngine google.cloud.discoveryengine.v1alpha.SiteSearchEngine,
       *  such as
       *  `projects/{project}/locations/{location}/dataStores/{data_store_id}/siteSearchEngine`.
       */
      // const siteSearchEngine = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callEnableAdvancedSiteSearch() {
        // Construct request
        const request = {
          siteSearchEngine,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.enableAdvancedSiteSearch(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callEnableAdvancedSiteSearch();
    
    

### enableAdvancedSiteSearch(request, options, callback)
    
    
    enableAdvancedSiteSearch(request: protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchResponse, protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ienableadvancedsitesearchrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ienableadvancedsitesearchresponse), [protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ienableadvancedsitesearchmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enableAdvancedSiteSearch(request, callback)
    
    
    enableAdvancedSiteSearch(request: protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchRequest, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchResponse, protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ienableadvancedsitesearchrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ienableadvancedsitesearchresponse), [protos.google.cloud.discoveryengine.v1alpha.IEnableAdvancedSiteSearchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ienableadvancedsitesearchmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enginePath(project, location, collection, engine)
    
    
    enginePath(project: string, location: string, collection: string, engine: string): string;

Return a fully-qualified engine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### evaluationPath(project, location, evaluation)
    
    
    evaluationPath(project: string, location: string, evaluation: string): string;

Return a fully-qualified evaluation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`evaluation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### fetchDomainVerificationStatus(request, options)
    
    
    fetchDomainVerificationStatus(request?: protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1alpha.ITargetSite[],
            protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest | null,
            protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusResponse
        ]>;

Returns list of target sites with its domain verification status. This method can only be called under data store with BASIC_SITE_SEARCH state at the moment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDomainVerificationStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite)[], [protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusrequest) | null, [protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `fetchDomainVerificationStatusAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchDomainVerificationStatus(request, options, callback)
    
    
    fetchDomainVerificationStatus(request: protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest, protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusResponse | null | undefined, protos.google.cloud.discoveryengine.v1alpha.ITargetSite>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDomainVerificationStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusrequest), [protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchDomainVerificationStatus(request, callback)
    
    
    fetchDomainVerificationStatus(request: protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest, protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusResponse | null | undefined, protos.google.cloud.discoveryengine.v1alpha.ITargetSite>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDomainVerificationStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusrequest), [protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchDomainVerificationStatusAsync(request, options)
    
    
    fetchDomainVerificationStatusAsync(request?: protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.discoveryengine.v1alpha.ITargetSite>;

Equivalent to `fetchDomainVerificationStatus`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDomainVerificationStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The site search engine resource under which we fetch all the
       *  domain verification status.
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.
       */
      // const siteSearchEngine = 'abc123'
      /**
       *  Requested page size. Server may return fewer items than requested. If
       *  unspecified, server will pick an appropriate default. The maximum value is
       *  1000; values above 1000 will be coerced to 1000.
       *  If this field is negative, an INVALID_ARGUMENT error is returned.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `FetchDomainVerificationStatus`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `FetchDomainVerificationStatus` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callFetchDomainVerificationStatus() {
        // Construct request
        const request = {
          siteSearchEngine,
        };
    
        // Run request
        const iterable = discoveryengineClient.fetchDomainVerificationStatusAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callFetchDomainVerificationStatus();
    
    

### fetchDomainVerificationStatusStream(request, options)
    
    
    fetchDomainVerificationStatusStream(request?: protos.google.cloud.discoveryengine.v1alpha.IFetchDomainVerificationStatusRequest, options?: CallOptions): Transform;

Equivalent to `fetchDomainVerificationStatus`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDomainVerificationStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ifetchdomainverificationstatusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `fetchDomainVerificationStatusAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)]>` |   
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
  
### getSiteSearchEngine(request, options)
    
    
    getSiteSearchEngine(request?: protos.google.cloud.discoveryengine.v1alpha.IGetSiteSearchEngineRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1alpha.ISiteSearchEngine,
            (protos.google.cloud.discoveryengine.v1alpha.IGetSiteSearchEngineRequest | undefined),
            {} | undefined
        ]>;

Gets the [SiteSearchEngine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.sitesearchengine).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSiteSearchEngineRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetsitesearchenginerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1alpha.ISiteSearchEngine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isitesearchengine), ([protos.google.cloud.discoveryengine.v1alpha.IGetSiteSearchEngineRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetsitesearchenginerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [SiteSearchEngine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.sitesearchengine). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of
       *  SiteSearchEngine google.cloud.discoveryengine.v1alpha.SiteSearchEngine,
       *  such as
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.
       *  If the caller does not have permission to access the SiteSearchEngine,
       *  regardless of whether or not it exists, a PERMISSION_DENIED error is
       *  returned.
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callGetSiteSearchEngine() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await discoveryengineClient.getSiteSearchEngine(request);
        console.log(response);
      }
    
      callGetSiteSearchEngine();
    
    

### getSiteSearchEngine(request, options, callback)
    
    
    getSiteSearchEngine(request: protos.google.cloud.discoveryengine.v1alpha.IGetSiteSearchEngineRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1alpha.ISiteSearchEngine, protos.google.cloud.discoveryengine.v1alpha.IGetSiteSearchEngineRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSiteSearchEngineRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetsitesearchenginerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1alpha.ISiteSearchEngine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isitesearchengine), [protos.google.cloud.discoveryengine.v1alpha.IGetSiteSearchEngineRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetsitesearchenginerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSiteSearchEngine(request, callback)
    
    
    getSiteSearchEngine(request: protos.google.cloud.discoveryengine.v1alpha.IGetSiteSearchEngineRequest, callback: Callback<protos.google.cloud.discoveryengine.v1alpha.ISiteSearchEngine, protos.google.cloud.discoveryengine.v1alpha.IGetSiteSearchEngineRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSiteSearchEngineRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetsitesearchenginerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1alpha.ISiteSearchEngine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isitesearchengine), [protos.google.cloud.discoveryengine.v1alpha.IGetSiteSearchEngineRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetsitesearchenginerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTargetSite(request, options)
    
    
    getTargetSite(request?: protos.google.cloud.discoveryengine.v1alpha.IGetTargetSiteRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1alpha.ITargetSite,
            (protos.google.cloud.discoveryengine.v1alpha.IGetTargetSiteRequest | undefined),
            {} | undefined
        ]>;

Gets a .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igettargetsiterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite), ([protos.google.cloud.discoveryengine.v1alpha.IGetTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igettargetsiterequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite, such as
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`.
       *  If the caller does not have permission to access the
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite, regardless
       *  of whether or not it exists, a PERMISSION_DENIED error is returned.
       *  If the requested
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite  does not
       *  exist, a NOT_FOUND error is returned.
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callGetTargetSite() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await discoveryengineClient.getTargetSite(request);
        console.log(response);
      }
    
      callGetTargetSite();
    
    

### getTargetSite(request, options, callback)
    
    
    getTargetSite(request: protos.google.cloud.discoveryengine.v1alpha.IGetTargetSiteRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1alpha.ITargetSite, protos.google.cloud.discoveryengine.v1alpha.IGetTargetSiteRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igettargetsiterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite), [protos.google.cloud.discoveryengine.v1alpha.IGetTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igettargetsiterequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTargetSite(request, callback)
    
    
    getTargetSite(request: protos.google.cloud.discoveryengine.v1alpha.IGetTargetSiteRequest, callback: Callback<protos.google.cloud.discoveryengine.v1alpha.ITargetSite, protos.google.cloud.discoveryengine.v1alpha.IGetTargetSiteRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igettargetsiterequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite), [protos.google.cloud.discoveryengine.v1alpha.IGetTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igettargetsiterequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUriPatternDocumentData(request, options)
    
    
    getUriPatternDocumentData(request?: protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataResponse,
            (protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataRequest | undefined),
            {} | undefined
        ]>;

Gets the URI Pattern to Document data mapping for an Advanced Site Search DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUriPatternDocumentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igeturipatterndocumentdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igeturipatterndocumentdataresponse), ([protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igeturipatterndocumentdatarequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GetUriPatternDocumentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.geturipatterndocumentdataresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of the
       *  SiteSearchEngine google.cloud.discoveryengine.v1alpha.SiteSearchEngine,
       *  such as
       *  `projects/* /locations/* /collections/* /dataStores/* /siteSearchEngine`.
       */
      // const siteSearchEngine = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callGetUriPatternDocumentData() {
        // Construct request
        const request = {
          siteSearchEngine,
        };
    
        // Run request
        const response = await discoveryengineClient.getUriPatternDocumentData(request);
        console.log(response);
      }
    
      callGetUriPatternDocumentData();
    
    

### getUriPatternDocumentData(request, options, callback)
    
    
    getUriPatternDocumentData(request: protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataResponse, protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUriPatternDocumentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igeturipatterndocumentdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igeturipatterndocumentdataresponse), [protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igeturipatterndocumentdatarequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUriPatternDocumentData(request, callback)
    
    
    getUriPatternDocumentData(request: protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataRequest, callback: Callback<protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataResponse, protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUriPatternDocumentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igeturipatterndocumentdatarequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igeturipatterndocumentdataresponse), [protos.google.cloud.discoveryengine.v1alpha.IGetUriPatternDocumentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igeturipatterndocumentdatarequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listTargetSites(request, options)
    
    
    listTargetSites(request?: protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1alpha.ITargetSite[],
            protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest | null,
            protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesResponse
        ]>;

Gets a list of s.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite)[], [protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesrequest) | null, [protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listTargetSitesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTargetSites(request, options, callback)
    
    
    listTargetSites(request: protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest, protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesResponse | null | undefined, protos.google.cloud.discoveryengine.v1alpha.ITargetSite>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesrequest), [protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTargetSites(request, callback)
    
    
    listTargetSites(request: protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest, protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesResponse | null | undefined, protos.google.cloud.discoveryengine.v1alpha.ITargetSite>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesrequest), [protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTargetSitesAsync(request, options)
    
    
    listTargetSitesAsync(request?: protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.discoveryengine.v1alpha.ITargetSite>;

Equivalent to `listTargetSites`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent site search engine resource name, such as
       *  `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.
       *  If the caller does not have permission to list
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite s under this
       *  site search engine, regardless of whether or not this branch exists, a
       *  PERMISSION_DENIED error is returned.
       */
      // const parent = 'abc123'
      /**
       *  Requested page size. Server may return fewer items than requested. If
       *  unspecified, server will pick an appropriate default. The maximum value is
       *  1000; values above 1000 will be coerced to 1000.
       *  If this field is negative, an INVALID_ARGUMENT error is returned.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListTargetSites` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListTargetSites`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callListTargetSites() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = discoveryengineClient.listTargetSitesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListTargetSites();
    
    

### listTargetSitesStream(request, options)
    
    
    listTargetSitesStream(request?: protos.google.cloud.discoveryengine.v1alpha.IListTargetSitesRequest, options?: CallOptions): Transform;

Equivalent to `listTargetSites`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTargetSitesRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.ilisttargetsitesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listTargetSitesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAnswerFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchAnswerFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchAnswerFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchAnswerFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchAnswerFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchAnswerFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchBranchFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchBranchFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the branch from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchBranchFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the branch from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchBranchFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the branch from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchBranchFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the branch from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchChunkFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchChunkFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the chunk from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchChunkFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchChunkFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the chunk from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchCollectionFromEngineName(engineName)
    
    
    matchCollectionFromEngineName(engineName: string): string | number;

Parse the collection from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchCollectionFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchCollectionFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchCollectionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchCollectionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchControlFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchControlFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the control from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchControlFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchControlFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the control from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchControlFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchControlFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the control from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchConversationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchConversationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the conversation from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchConversationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the conversation from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchConversationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the conversation from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchCustomTuningModelFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchCustomTuningModelFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the custom_tuning_model from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_tuning_model.  
  
### matchCustomTuningModelFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchCustomTuningModelFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the custom_tuning_model from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_tuning_model.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchDataStoreFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the data_store from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchDataStoreFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the data_store from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchDataStoreFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the data_store from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchDataStoreFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the data_store from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchDataStoreFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the data_store from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchDataStoreFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the data_store from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchDataStoreFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the data_store from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchDataStoreFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchDataStoreFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the data_store from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchDataStoreFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchDataStoreFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchDataStoreFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchDataStoreFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the document from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the document from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchDocumentFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the document from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchDocumentFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the document from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchEngineFromEngineName(engineName)
    
    
    matchEngineFromEngineName(engineName: string): string | number;

Parse the engine from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchEngineFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchEngineFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchEngineFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchEngineFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchEngineFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
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
  
### matchLocationFromAclConfigName(aclConfigName)
    
    
    matchLocationFromAclConfigName(aclConfigName: string): string | number;

Parse the location from AclConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`aclConfigName` |  `string`   
A fully-qualified path representing AclConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEngineName(engineName)
    
    
    matchLocationFromEngineName(engineName: string): string | number;

Parse the location from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEvaluationName(evaluationName)
    
    
    matchLocationFromEvaluationName(evaluationName: string): string | number;

Parse the location from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the location from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchLocationFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the location from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchLocationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the location from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchLocationFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchLocationFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the location from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchLocationFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the location from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchLocationFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the location from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchLocationFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the location from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchLocationFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the location from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchLocationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the location from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchLocationFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the location from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchLocationFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the location from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchLocationFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the location from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchLocationFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the location from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchLocationFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the location from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchLocationFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the location from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchLocationFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the location from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchLocationFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the location from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchLocationFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the location from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSampleQueryName(sampleQueryName)
    
    
    matchLocationFromSampleQueryName(sampleQueryName: string): string | number;

Parse the location from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchLocationFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the location from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchProjectFromAclConfigName(aclConfigName)
    
    
    matchProjectFromAclConfigName(aclConfigName: string): string | number;

Parse the project from AclConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`aclConfigName` |  `string`   
A fully-qualified path representing AclConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEngineName(engineName)
    
    
    matchProjectFromEngineName(engineName: string): string | number;

Parse the project from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
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
  
### matchProjectFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the project from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchProjectFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the project from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchProjectFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the project from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchProjectFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchProjectFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the project from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchProjectFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the project from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchProjectFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the project from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchProjectFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the project from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchProjectFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the project from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchProjectFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the project from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchProjectFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the project from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchProjectFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the project from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchProjectFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the project from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchProjectFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the project from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchProjectFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the project from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchProjectFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the project from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchProjectFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the project from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchProjectFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the project from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchProjectFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the project from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
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
  
### matchProjectFromSampleQueryName(sampleQueryName)
    
    
    matchProjectFromSampleQueryName(sampleQueryName: string): string | number;

Parse the project from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchProjectFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the project from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchSampleQueryFromSampleQueryName(sampleQueryName)
    
    
    matchSampleQueryFromSampleQueryName(sampleQueryName: string): string | number;

Parse the sample_query from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query.  
  
### matchSampleQuerySetFromSampleQueryName(sampleQueryName)
    
    
    matchSampleQuerySetFromSampleQueryName(sampleQueryName: string): string | number;

Parse the sample_query_set from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query_set.  
  
### matchSampleQuerySetFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchSampleQuerySetFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the sample_query_set from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query_set.  
  
### matchSchemaFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchSchemaFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the schema from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the schema.  
  
### matchSchemaFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchSchemaFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the schema from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the schema.  
  
### matchServingConfigFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchServingConfigFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchServingConfigFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchServingConfigFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchServingConfigFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchServingConfigFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchSessionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchSessionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the session from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchSessionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the session from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchSessionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the session from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchSessionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the session from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchSessionFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the session from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchSessionFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the session from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchTargetSiteFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchTargetSiteFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the target_site from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the target_site.  
  
### matchTargetSiteFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchTargetSiteFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the target_site from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the target_site.  
  
### projectLocationCollectionDataStoreBranchDocumentChunkPath(project, location, collection, dataStore, branch, document, chunk)
    
    
    projectLocationCollectionDataStoreBranchDocumentChunkPath(project: string, location: string, collection: string, dataStore: string, branch: string, document: string, chunk: string): string;

Return a fully-qualified projectLocationCollectionDataStoreBranchDocumentChunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreBranchDocumentPath(project, location, collection, dataStore, branch, document)
    
    
    projectLocationCollectionDataStoreBranchDocumentPath(project: string, location: string, collection: string, dataStore: string, branch: string, document: string): string;

Return a fully-qualified projectLocationCollectionDataStoreBranchDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreControlPath(project, location, collection, dataStore, control)
    
    
    projectLocationCollectionDataStoreControlPath(project: string, location: string, collection: string, dataStore: string, control: string): string;

Return a fully-qualified projectLocationCollectionDataStoreControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreConversationPath(project, location, collection, dataStore, conversation)
    
    
    projectLocationCollectionDataStoreConversationPath(project: string, location: string, collection: string, dataStore: string, conversation: string): string;

Return a fully-qualified projectLocationCollectionDataStoreConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreCustomTuningModelPath(project, location, collection, dataStore, customTuningModel)
    
    
    projectLocationCollectionDataStoreCustomTuningModelPath(project: string, location: string, collection: string, dataStore: string, customTuningModel: string): string;

Return a fully-qualified projectLocationCollectionDataStoreCustomTuningModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`customTuningModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreDocumentProcessingConfigPath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStoreDocumentProcessingConfigPath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStoreDocumentProcessingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStorePath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStorePath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSchemaPath(project, location, collection, dataStore, schema)
    
    
    projectLocationCollectionDataStoreSchemaPath(project: string, location: string, collection: string, dataStore: string, schema: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`schema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreServingConfigPath(project, location, collection, dataStore, servingConfig)
    
    
    projectLocationCollectionDataStoreServingConfigPath(project: string, location: string, collection: string, dataStore: string, servingConfig: string): string;

Return a fully-qualified projectLocationCollectionDataStoreServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSessionAnswerPath(project, location, collection, dataStore, session, answer)
    
    
    projectLocationCollectionDataStoreSessionAnswerPath(project: string, location: string, collection: string, dataStore: string, session: string, answer: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSessionsPath(project, location, collection, dataStore, session)
    
    
    projectLocationCollectionDataStoreSessionsPath(project: string, location: string, collection: string, dataStore: string, session: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSiteSearchEnginePath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStoreSiteSearchEnginePath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSiteSearchEngine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSiteSearchEngineTargetSitePath(project, location, collection, dataStore, targetSite)
    
    
    projectLocationCollectionDataStoreSiteSearchEngineTargetSitePath(project: string, location: string, collection: string, dataStore: string, targetSite: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSiteSearchEngineTargetSite resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`targetSite` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineControlPath(project, location, collection, engine, control)
    
    
    projectLocationCollectionEngineControlPath(project: string, location: string, collection: string, engine: string, control: string): string;

Return a fully-qualified projectLocationCollectionEngineControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineConversationPath(project, location, collection, engine, conversation)
    
    
    projectLocationCollectionEngineConversationPath(project: string, location: string, collection: string, engine: string, conversation: string): string;

Return a fully-qualified projectLocationCollectionEngineConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineServingConfigPath(project, location, collection, engine, servingConfig)
    
    
    projectLocationCollectionEngineServingConfigPath(project: string, location: string, collection: string, engine: string, servingConfig: string): string;

Return a fully-qualified projectLocationCollectionEngineServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineSessionAnswerPath(project, location, collection, engine, session, answer)
    
    
    projectLocationCollectionEngineSessionAnswerPath(project: string, location: string, collection: string, engine: string, session: string, answer: string): string;

Return a fully-qualified projectLocationCollectionEngineSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineSessionsPath(project, location, collection, engine, session)
    
    
    projectLocationCollectionEngineSessionsPath(project: string, location: string, collection: string, engine: string, session: string): string;

Return a fully-qualified projectLocationCollectionEngineSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreBranchDocumentChunkPath(project, location, dataStore, branch, document, chunk)
    
    
    projectLocationDataStoreBranchDocumentChunkPath(project: string, location: string, dataStore: string, branch: string, document: string, chunk: string): string;

Return a fully-qualified projectLocationDataStoreBranchDocumentChunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreBranchDocumentPath(project, location, dataStore, branch, document)
    
    
    projectLocationDataStoreBranchDocumentPath(project: string, location: string, dataStore: string, branch: string, document: string): string;

Return a fully-qualified projectLocationDataStoreBranchDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreControlPath(project, location, dataStore, control)
    
    
    projectLocationDataStoreControlPath(project: string, location: string, dataStore: string, control: string): string;

Return a fully-qualified projectLocationDataStoreControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreConversationPath(project, location, dataStore, conversation)
    
    
    projectLocationDataStoreConversationPath(project: string, location: string, dataStore: string, conversation: string): string;

Return a fully-qualified projectLocationDataStoreConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreCustomTuningModelPath(project, location, dataStore, customTuningModel)
    
    
    projectLocationDataStoreCustomTuningModelPath(project: string, location: string, dataStore: string, customTuningModel: string): string;

Return a fully-qualified projectLocationDataStoreCustomTuningModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`customTuningModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreDocumentProcessingConfigPath(project, location, dataStore)
    
    
    projectLocationDataStoreDocumentProcessingConfigPath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStoreDocumentProcessingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStorePath(project, location, dataStore)
    
    
    projectLocationDataStorePath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSchemaPath(project, location, dataStore, schema)
    
    
    projectLocationDataStoreSchemaPath(project: string, location: string, dataStore: string, schema: string): string;

Return a fully-qualified projectLocationDataStoreSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`schema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreServingConfigPath(project, location, dataStore, servingConfig)
    
    
    projectLocationDataStoreServingConfigPath(project: string, location: string, dataStore: string, servingConfig: string): string;

Return a fully-qualified projectLocationDataStoreServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSessionAnswerPath(project, location, dataStore, session, answer)
    
    
    projectLocationDataStoreSessionAnswerPath(project: string, location: string, dataStore: string, session: string, answer: string): string;

Return a fully-qualified projectLocationDataStoreSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSessionsPath(project, location, dataStore, session)
    
    
    projectLocationDataStoreSessionsPath(project: string, location: string, dataStore: string, session: string): string;

Return a fully-qualified projectLocationDataStoreSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSiteSearchEnginePath(project, location, dataStore)
    
    
    projectLocationDataStoreSiteSearchEnginePath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStoreSiteSearchEngine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSiteSearchEngineTargetSitePath(project, location, dataStore, targetSite)
    
    
    projectLocationDataStoreSiteSearchEngineTargetSitePath(project: string, location: string, dataStore: string, targetSite: string): string;

Return a fully-qualified projectLocationDataStoreSiteSearchEngineTargetSite resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`targetSite` |  `string`   
  
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
  
### recrawlUris(request, options)
    
    
    recrawlUris(request?: protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisResponse, protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Request on-demand recrawl for a list of URIs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecrawlUrisRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.irecrawlurisrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.irecrawlurisresponse), [protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.irecrawlurismetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of the
       *  SiteSearchEngine google.cloud.discoveryengine.v1alpha.SiteSearchEngine,
       *  such as
       *  `projects/* /locations/* /collections/* /dataStores/* /siteSearchEngine`.
       */
      // const siteSearchEngine = 'abc123'
      /**
       *  Required. List of URIs to crawl. At most 10K URIs are supported, otherwise
       *  an INVALID_ARGUMENT error is thrown. Each URI should match at least one
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite  in
       *  `site_search_engine`.
       */
      // const uris = ['abc','def']
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callRecrawlUris() {
        // Construct request
        const request = {
          siteSearchEngine,
          uris,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.recrawlUris(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRecrawlUris();
    
    

### recrawlUris(request, options, callback)
    
    
    recrawlUris(request: protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisResponse, protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecrawlUrisRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.irecrawlurisrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.irecrawlurisresponse), [protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.irecrawlurismetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### recrawlUris(request, callback)
    
    
    recrawlUris(request: protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisRequest, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisResponse, protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecrawlUrisRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.irecrawlurisrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.irecrawlurisresponse), [protos.google.cloud.discoveryengine.v1alpha.IRecrawlUrisMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.irecrawlurismetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### sampleQueryPath(project, location, sampleQuerySet, sampleQuery)
    
    
    sampleQueryPath(project: string, location: string, sampleQuerySet: string, sampleQuery: string): string;

Return a fully-qualified sampleQuery resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sampleQuerySet` |  `string`   
  
`sampleQuery` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### sampleQuerySetPath(project, location, sampleQuerySet)
    
    
    sampleQuerySetPath(project: string, location: string, sampleQuerySet: string): string;

Return a fully-qualified sampleQuerySet resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sampleQuerySet` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### setUriPatternDocumentData(request, options)
    
    
    setUriPatternDocumentData(request?: protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataResponse, protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Sets the URI Pattern to Document data mapping for an Advanced Site Search DataStore.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetUriPatternDocumentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iseturipatterndocumentdatarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iseturipatterndocumentdataresponse), [protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iseturipatterndocumentdatametadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of the
       *  SiteSearchEngine google.cloud.discoveryengine.v1alpha.SiteSearchEngine,
       *  such as
       *  `projects/* /locations/* /collections/* /dataStores/* /siteSearchEngine`.
       */
      // const siteSearchEngine = 'abc123'
      /**
       *  Document data keyed by URI pattern. Each entry must be consistent with
       *  the Schema google.cloud.discoveryengine.v1alpha.Schema. For example:
       *  Schema google.cloud.discoveryengine.v1alpha.Schema  = {
       *  "type": "object",
       *  "properties": {
       *    "Categories": {
       *      "type": "array",
       *      "items": {
       *        "retrievable": true,
       *        "type": "string"
       *      }
       *    }
       *  }
       *  document_data_map = {
       *    "www.url1.com/*": {
       *      "Categories": "category1", "category2" 
       *    },
       *    "www.url2.com/*": {
       *      "Categories": "category3" 
       *    }
       *  }
       */
      // const documentDataMap = [1,2,3,4]
      /**
       *  If true, clears the document data map. If true,
       *  SetUriPatternDocumentDataRequest.document_data_map google.cloud.discoveryengine.v1alpha.SetUriPatternDocumentDataRequest.document_data_map 
       *  must be empty.
       */
      // const emptyDocumentDataMap = true
      /**
       *  Optional. If not provided, the current
       *  Schema google.cloud.discoveryengine.v1alpha.Schema  is used. If provided,
       *  validates and updates the
       *  Schema google.cloud.discoveryengine.v1alpha.Schema. If validation fails,
       *  an error is returned.
       */
      // const schema = {}
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callSetUriPatternDocumentData() {
        // Construct request
        const request = {
          siteSearchEngine,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.setUriPatternDocumentData(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callSetUriPatternDocumentData();
    
    

### setUriPatternDocumentData(request, options, callback)
    
    
    setUriPatternDocumentData(request: protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataResponse, protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetUriPatternDocumentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iseturipatterndocumentdatarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iseturipatterndocumentdataresponse), [protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iseturipatterndocumentdatametadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setUriPatternDocumentData(request, callback)
    
    
    setUriPatternDocumentData(request: protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataRequest, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataResponse, protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetUriPatternDocumentDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iseturipatterndocumentdatarequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iseturipatterndocumentdataresponse), [protos.google.cloud.discoveryengine.v1alpha.ISetUriPatternDocumentDataMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iseturipatterndocumentdatametadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTargetSite(request, options)
    
    
    updateTargetSite(request?: protos.google.cloud.discoveryengine.v1alpha.IUpdateTargetSiteRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.discoveryengine.v1alpha.ITargetSite, protos.google.cloud.discoveryengine.v1alpha.IUpdateTargetSiteMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates a .

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iupdatetargetsiterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite), [protos.google.cloud.discoveryengine.v1alpha.IUpdateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iupdatetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The target site to update.
       *  If the caller does not have permission to update the
       *  TargetSite google.cloud.discoveryengine.v1alpha.TargetSite, regardless
       *  of whether or not it exists, a PERMISSION_DENIED error is returned.
       *  If the TargetSite google.cloud.discoveryengine.v1alpha.TargetSite  to
       *  update does not exist, a NOT_FOUND error is returned.
       */
      // const targetSite = {}
    
      // Imports the Discoveryengine library
      const {SiteSearchEngineServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SiteSearchEngineServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callUpdateTargetSite() {
        // Construct request
        const request = {
          targetSite,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.updateTargetSite(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateTargetSite();
    
    

### updateTargetSite(request, options, callback)
    
    
    updateTargetSite(request: protos.google.cloud.discoveryengine.v1alpha.IUpdateTargetSiteRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.ITargetSite, protos.google.cloud.discoveryengine.v1alpha.IUpdateTargetSiteMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iupdatetargetsiterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite), [protos.google.cloud.discoveryengine.v1alpha.IUpdateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iupdatetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTargetSite(request, callback)
    
    
    updateTargetSite(request: protos.google.cloud.discoveryengine.v1alpha.IUpdateTargetSiteRequest, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1alpha.ITargetSite, protos.google.cloud.discoveryengine.v1alpha.IUpdateTargetSiteMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTargetSiteRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iupdatetargetsiterequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1alpha.ITargetSite](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.itargetsite), [protos.google.cloud.discoveryengine.v1alpha.IUpdateTargetSiteMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.iupdatetargetsitemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
