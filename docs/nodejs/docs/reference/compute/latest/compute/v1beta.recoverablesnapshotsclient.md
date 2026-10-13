---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.recoverablesnapshotsclient
title: Class v1beta.RecoverableSnapshotsClient (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:15:20.003385+00:00
---

# Class v1beta.RecoverableSnapshotsClient (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.recoverablesnapshotsclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.RecoverableSnapshotsClient (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

The RecoverableSnapshots API. v1beta

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of RecoverableSnapshotsClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new RecoverableSnapshotsClient({fallback: true}, gax); ```  
  
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

### port
    
    
    static get port(): number;

The port for this API service.

### recoverableSnapshotsStub
    
    
    recoverableSnapshotsStub?: Promise<{
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

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### delete(request, options)
    
    
    delete(request?: protos.google.cloud.compute.v1beta.IDeleteRecoverableSnapshotRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Deletes the specified RecoverableSnapshot. Deleting a recoverable snapshot will delete the underlying PD snapshot and is irreversible.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleterecoverablesnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the recoverable Snapshot resource to delete.
       */
      // const recoverableSnapshot = 'abc123'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Compute library
      const {RecoverableSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RecoverableSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.recoverablesnapshotsclient.html)();
    
      async function callDelete() {
        // Construct request
        const request = {
          project,
          recoverableSnapshot,
        };
    
        // Run request
        const response = await computeClient.delete(request);
        console.log(response);
      }
    
      callDelete();
    
    

### delete(request, options, callback)
    
    
    delete(request: protos.google.cloud.compute.v1beta.IDeleteRecoverableSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IDeleteRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleterecoverablesnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IDeleteRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleterecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request, callback)
    
    
    delete(request: protos.google.cloud.compute.v1beta.IDeleteRecoverableSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IDeleteRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleterecoverablesnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IDeleteRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleterecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request, options)
    
    
    get(request?: protos.google.cloud.compute.v1beta.IGetRecoverableSnapshotRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IRecoverableSnapshot,
            (protos.google.cloud.compute.v1beta.IGetRecoverableSnapshotRequest | undefined),
            {} | undefined
        ]>;

Returns the specified RecoverableSnapshot resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrecoverablesnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IRecoverableSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverablesnapshot), ([protos.google.cloud.compute.v1beta.IGetRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrecoverablesnapshotrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the Snapshot resource to return.
       */
      // const recoverableSnapshot = 'abc123'
    
      // Imports the Compute library
      const {RecoverableSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RecoverableSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.recoverablesnapshotsclient.html)();
    
      async function callGet() {
        // Construct request
        const request = {
          project,
          recoverableSnapshot,
        };
    
        // Run request
        const response = await computeClient.get(request);
        console.log(response);
      }
    
      callGet();
    
    

### get(request, options, callback)
    
    
    get(request: protos.google.cloud.compute.v1beta.IGetRecoverableSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IRecoverableSnapshot, protos.google.cloud.compute.v1beta.IGetRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrecoverablesnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IRecoverableSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverablesnapshot), [protos.google.cloud.compute.v1beta.IGetRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request, callback)
    
    
    get(request: protos.google.cloud.compute.v1beta.IGetRecoverableSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IRecoverableSnapshot, protos.google.cloud.compute.v1beta.IGetRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrecoverablesnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IRecoverableSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverablesnapshot), [protos.google.cloud.compute.v1beta.IGetRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetrecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, options)
    
    
    getIamPolicy(request?: protos.google.cloud.compute.v1beta.IGetIamPolicyRecoverableSnapshotRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IPolicy,
            (protos.google.cloud.compute.v1beta.IGetIamPolicyRecoverableSnapshotRequest | undefined),
            {} | undefined
        ]>;

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyrecoverablesnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), ([protos.google.cloud.compute.v1beta.IGetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyrecoverablesnapshotrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Requested IAM Policy version.
       */
      // const optionsRequestedPolicyVersion = 1234
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
    
      // Imports the Compute library
      const {RecoverableSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RecoverableSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.recoverablesnapshotsclient.html)();
    
      async function callGetIamPolicy() {
        // Construct request
        const request = {
          project,
          resource,
        };
    
        // Run request
        const response = await computeClient.getIamPolicy(request);
        console.log(response);
      }
    
      callGetIamPolicy();
    
    

### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: protos.google.cloud.compute.v1beta.IGetIamPolicyRecoverableSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.IGetIamPolicyRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyrecoverablesnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.IGetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyrecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, callback)
    
    
    getIamPolicy(request: protos.google.cloud.compute.v1beta.IGetIamPolicyRecoverableSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.IGetIamPolicyRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyrecoverablesnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.IGetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyrecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### list(request, options)
    
    
    list(request?: protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IRecoverableSnapshot[],
            protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest | null,
            protos.google.cloud.compute.v1beta.IRecoverableSnapshotList
        ]>;

Retrieves a list of all of the RecoverableSnapshots in your project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRecoverableSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistrecoverablesnapshotsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IRecoverableSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverablesnapshot)[], [protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistrecoverablesnapshotsrequest) | null, [protos.google.cloud.compute.v1beta.IRecoverableSnapshotList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverablesnapshotlist) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### list(request, options, callback)
    
    
    list(request: protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest, protos.google.cloud.compute.v1beta.IRecoverableSnapshotList | null | undefined, protos.google.cloud.compute.v1beta.IRecoverableSnapshot>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRecoverableSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistrecoverablesnapshotsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistrecoverablesnapshotsrequest), [protos.google.cloud.compute.v1beta.IRecoverableSnapshotList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverablesnapshotlist) | null | undefined, [protos.google.cloud.compute.v1beta.IRecoverableSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverablesnapshot)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request, callback)
    
    
    list(request: protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest, callback: PaginationCallback<protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest, protos.google.cloud.compute.v1beta.IRecoverableSnapshotList | null | undefined, protos.google.cloud.compute.v1beta.IRecoverableSnapshot>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRecoverableSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistrecoverablesnapshotsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistrecoverablesnapshotsrequest), [protos.google.cloud.compute.v1beta.IRecoverableSnapshotList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverablesnapshotlist) | null | undefined, [protos.google.cloud.compute.v1beta.IRecoverableSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverablesnapshot)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAsync(request, options)
    
    
    listAsync(request?: protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.compute.v1beta.IRecoverableSnapshot>;

Equivalent to `list`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRecoverableSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistrecoverablesnapshotsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.compute.v1beta.IRecoverableSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverablesnapshot)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  A filter expression that filters resources listed in the response. Most
       *  Compute resources support two types of filter expressions:
       *  expressions that support regular expressions and expressions that follow
       *  API improvement proposal AIP-160.
       *  These two types of filter expressions cannot be mixed in one request.
       *  If you want to use AIP-160, your expression must specify the field name, an
       *  operator, and the value that you want to use for filtering. The value
       *  must be a string, a number, or a boolean. The operator
       *  must be either `=`, `!=`, `>`, `<`,><=`, `="">=` or `:`.
       *  For example, if you are filtering Compute Engine instances, you can
       *  exclude instances named `example-instance` by specifying
       *  `name != example-instance`.
       *  The `:*` comparison can be used to test whether a key has been defined.
       *  For example, to find all objects with `owner` label use:
       *  
    
    
       *  labels.owner:*
       *  

`

  * You can also filter nested fields. For example, you could specify
  * `scheduling.automaticRestart = false` to include instances only
  * if they are not scheduled for automatic restarts. You can use filtering
  * on nested fields to filter based onresource labels.
  * To filter on multiple expressions, provide each separate expression within
  * parentheses. For example:
  *   * (scheduling.automaticRestart = true)
  * (cpuPlatform = "Intel Skylake")
  *   * By default, each expression is an `AND` expression. However, you
  * can include `AND` and `OR` expressions explicitly.
  * For example:
  *   * (cpuPlatform = "Intel Skylake") OR
  * (cpuPlatform = "Intel Broadwell") AND
  * (scheduling.automaticRestart = true)
  *   * If you want to use a regular expression, use the `eq` (equal) or `ne`
  * (not equal) operator against a single un-parenthesized expression with or
  * without quotes or against multiple parenthesized expressions. Examples:
  * `fieldname eq unquoted literal`
  * `fieldname eq 'single quoted literal'`
  * `fieldname eq "double quoted literal"`
  * `(fieldname1 eq literal) (fieldname2 ne "literal")`
  * The literal value is interpreted as a regular expression using GoogleRE2 library syntax.
  * The literal value must match the entire field.
  * For example, to filter for instances that do not end with name "instance",
  * you would use `name ne .*instance`.
  * You cannot combine constraints on multiple fields using regular
  * expressions. _/ // const filter = 'abc123' /_ *
  * The maximum number of results per page that should be returned.
  * If the number of available results is larger than `maxResults`,
  * Compute Engine returns a `nextPageToken` that can be used to get
  * the next page of results in subsequent list requests. Acceptable values are
  * `0` to `500`, inclusive. (Default: `500`) _/ // const maxResults = 1234 /_ *
  * Sorts list results by a certain order. By default, results
  * are returned in alphanumerical order based on the resource name.
  * You can also sort results in descending order based on the creation
  * timestamp using `orderBy="creationTimestamp desc"`. This sorts
  * results based on the `creationTimestamp` field in
  * reverse chronological order (newest result first). Use this to sort
  * resources like operations so that the newest operation is returned first.
  * Currently, only sorting by `name` or
  * `creationTimestamp desc` is supported. _/ // const orderBy = 'abc123' /_ *
  * Specifies a page token to use. Set `pageToken` to the
  * `nextPageToken` returned by a previous list request to get
  * the next page of results. _/ // const pageToken = 'abc123' /_ *
  * Project ID for this request. _/ // const project = 'my-project' /_ *
  * Opt-in for partial success behavior which provides partial results in case
  * of failure. The default value is false.
  * For example, when partial success behavior is enabled, aggregatedList for a
  * single zone scope either returns all resources in the zone or no resources,
  * with an error code. */ // const returnPartialSuccess = true

// Imports the Compute library const {RecoverableSnapshotsClient} = require('@google-cloud/compute').v1beta;

// Instantiates a client const computeClient = new RecoverableSnapshotsClient();

async function callList() { // Construct request const request = { project, };

// Run request const iterable = computeClient.listAsync(request); for await (const response of iterable) { console.log(response); } }

callList();




` `

### listStream(request, options)
    
    
    listStream(request?: protos.google.cloud.compute.v1beta.IListRecoverableSnapshotsRequest, options?: CallOptions): Transform;

Equivalent to `list`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRecoverableSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistrecoverablesnapshotsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### recover(request, options)
    
    
    recover(request?: protos.google.cloud.compute.v1beta.IRecoverRecoverableSnapshotRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Recovers the specified RecoverableSnapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecoverRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverrecoverablesnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), null>, [protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples. This method is considered to be in beta. This means while stable it is still a work-in-progress and under active development, and might get backwards-incompatible changes at any time. `.promise()` is not supported yet.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Project Id of the request
       */
      // const project = 'my-project'
      /**
       *  Name of the recoverable resource to recover
       */
      // const recoverableSnapshot = 'abc123'
      /**
       *  An optional request ID to identify requests. Specify a unique request ID so
       *  that if you must retry your request, the server will know to ignore the
       *  request if it has already been completed.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same
       *  request ID, the server can check if original operation with the same
       *  request ID was received, and if so, will ignore the second request. This
       *  prevents clients from accidentally creating duplicate commitments.
       *  The request ID must be
       *  a valid UUID with the exception that zero UUID is not supported
       *  (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. Name of the snapshot after the recovery
       *  The name will be 1-63 characters long, and comply withRFC1035.
       *  Specifically, the name will be 1-63 characters long and match the regular
       *  expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first
       *  character will be a lowercase letter, and all following characters can be
       *  a dash, lowercase letter, or digit, except the last character, which cannot
       *  be a dash.
       */
      // const snapshotName = 'abc123'
    
      // Imports the Compute library
      const {RecoverableSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RecoverableSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.recoverablesnapshotsclient.html)();
    
      async function callRecover() {
        // Construct request
        const request = {
          project,
          recoverableSnapshot,
        };
    
        // Run request
        const response = await computeClient.recover(request);
        console.log(response);
      }
    
      callRecover();
    
    

### recover(request, options, callback)
    
    
    recover(request: protos.google.cloud.compute.v1beta.IRecoverRecoverableSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRecoverRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecoverRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverrecoverablesnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRecoverRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverrecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### recover(request, callback)
    
    
    recover(request: protos.google.cloud.compute.v1beta.IRecoverRecoverableSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IRecoverRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRecoverRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverrecoverablesnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IRecoverRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.irecoverrecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, options)
    
    
    setIamPolicy(request?: protos.google.cloud.compute.v1beta.ISetIamPolicyRecoverableSnapshotRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IPolicy,
            (protos.google.cloud.compute.v1beta.ISetIamPolicyRecoverableSnapshotRequest | undefined),
            {} | undefined
        ]>;

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyrecoverablesnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), ([protos.google.cloud.compute.v1beta.ISetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyrecoverablesnapshotrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The body resource for this request
       */
      // const globalSetPolicyRequestResource = {}
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
    
      // Imports the Compute library
      const {RecoverableSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RecoverableSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.recoverablesnapshotsclient.html)();
    
      async function callSetIamPolicy() {
        // Construct request
        const request = {
          globalSetPolicyRequestResource,
          project,
          resource,
        };
    
        // Run request
        const response = await computeClient.setIamPolicy(request);
        console.log(response);
      }
    
      callSetIamPolicy();
    
    

### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: protos.google.cloud.compute.v1beta.ISetIamPolicyRecoverableSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.ISetIamPolicyRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyrecoverablesnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.ISetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyrecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, callback)
    
    
    setIamPolicy(request: protos.google.cloud.compute.v1beta.ISetIamPolicyRecoverableSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.ISetIamPolicyRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyrecoverablesnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.ISetIamPolicyRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyrecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, options)
    
    
    testIamPermissions(request?: protos.google.cloud.compute.v1beta.ITestIamPermissionsRecoverableSnapshotRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.ITestPermissionsResponse,
            (protos.google.cloud.compute.v1beta.ITestIamPermissionsRecoverableSnapshotRequest | undefined),
            {} | undefined
        ]>;

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsrecoverablesnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), ([protos.google.cloud.compute.v1beta.ITestIamPermissionsRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsrecoverablesnapshotrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.testpermissionsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
      /**
       *  The body resource for this request
       */
      // const testPermissionsRequestResource = {}
    
      // Imports the Compute library
      const {RecoverableSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RecoverableSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.recoverablesnapshotsclient.html)();
    
      async function callTestIamPermissions() {
        // Construct request
        const request = {
          project,
          resource,
          testPermissionsRequestResource,
        };
    
        // Run request
        const response = await computeClient.testIamPermissions(request);
        console.log(response);
      }
    
      callTestIamPermissions();
    
    

### testIamPermissions(request, options, callback)
    
    
    testIamPermissions(request: protos.google.cloud.compute.v1beta.ITestIamPermissionsRecoverableSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.ITestPermissionsResponse, protos.google.cloud.compute.v1beta.ITestIamPermissionsRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsrecoverablesnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), [protos.google.cloud.compute.v1beta.ITestIamPermissionsRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsrecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, callback)
    
    
    testIamPermissions(request: protos.google.cloud.compute.v1beta.ITestIamPermissionsRecoverableSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.ITestPermissionsResponse, protos.google.cloud.compute.v1beta.ITestIamPermissionsRecoverableSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsrecoverablesnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), [protos.google.cloud.compute.v1beta.ITestIamPermissionsRecoverableSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsrecoverablesnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
