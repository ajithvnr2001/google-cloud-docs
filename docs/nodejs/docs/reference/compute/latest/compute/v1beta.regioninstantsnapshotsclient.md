---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.regioninstantsnapshotsclient
title: Class v1beta.RegionInstantSnapshotsClient (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:16.407703+00:00
---

# Class v1beta.RegionInstantSnapshotsClient (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/v1beta.regioninstantsnapshotsclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.RegionInstantSnapshotsClient (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

The RegionInstantSnapshots API. v1beta

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of RegionInstantSnapshotsClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new RegionInstantSnapshotsClient({fallback: true}, gax); ```  
  
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

### regionInstantSnapshotsStub
    
    
    regionInstantSnapshotsStub?: Promise<{
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
    
    
    delete(request?: protos.google.cloud.compute.v1beta.IDeleteRegionInstantSnapshotRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Deletes the specified InstantSnapshot resource. Keep in mind that deleting a single instantSnapshot might not necessarily delete all the data on that instantSnapshot. If any data on the instantSnapshot that is marked for deletion is needed for subsequent instantSnapshots, the data will be moved to the next corresponding instantSnapshot.

For more information, seeDeleting instantSnapshots.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregioninstantsnapshotrequest)`   
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
       *  Name of the InstantSnapshot resource to delete.
       */
      // const instantSnapshot = 'abc123'
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  The name of the region for this request.
       */
      // const region = 'us-central1'
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
      const {RegionInstantSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionInstantSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callDelete() {
        // Construct request
        const request = {
          instantSnapshot,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.delete(request);
        console.log(response);
      }
    
      callDelete();
    
    

### delete(request, options, callback)
    
    
    delete(request: protos.google.cloud.compute.v1beta.IDeleteRegionInstantSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IDeleteRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregioninstantsnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IDeleteRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request, callback)
    
    
    delete(request: protos.google.cloud.compute.v1beta.IDeleteRegionInstantSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IDeleteRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregioninstantsnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IDeleteRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request, options)
    
    
    get(request?: protos.google.cloud.compute.v1beta.IGetRegionInstantSnapshotRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IInstantSnapshot,
            (protos.google.cloud.compute.v1beta.IGetRegionInstantSnapshotRequest | undefined),
            {} | undefined
        ]>;

Returns the specified InstantSnapshot resource in the specified region.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregioninstantsnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IInstantSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstantsnapshot), ([protos.google.cloud.compute.v1beta.IGetRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregioninstantsnapshotrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Name of the InstantSnapshot resource to return.
       */
      // const instantSnapshot = 'abc123'
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  The name of the region for this request.
       */
      // const region = 'us-central1'
    
      // Imports the Compute library
      const {RegionInstantSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionInstantSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGet() {
        // Construct request
        const request = {
          instantSnapshot,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.get(request);
        console.log(response);
      }
    
      callGet();
    
    

### get(request, options, callback)
    
    
    get(request: protos.google.cloud.compute.v1beta.IGetRegionInstantSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IInstantSnapshot, protos.google.cloud.compute.v1beta.IGetRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregioninstantsnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IInstantSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstantsnapshot), [protos.google.cloud.compute.v1beta.IGetRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request, callback)
    
    
    get(request: protos.google.cloud.compute.v1beta.IGetRegionInstantSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IInstantSnapshot, protos.google.cloud.compute.v1beta.IGetRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregioninstantsnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IInstantSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstantsnapshot), [protos.google.cloud.compute.v1beta.IGetRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, options)
    
    
    getIamPolicy(request?: protos.google.cloud.compute.v1beta.IGetIamPolicyRegionInstantSnapshotRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IPolicy,
            (protos.google.cloud.compute.v1beta.IGetIamPolicyRegionInstantSnapshotRequest | undefined),
            {} | undefined
        ]>;

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregioninstantsnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), ([protos.google.cloud.compute.v1beta.IGetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregioninstantsnapshotrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  The name of the region for this request.
       */
      // const region = 'us-central1'
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
    
      // Imports the Compute library
      const {RegionInstantSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionInstantSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callGetIamPolicy() {
        // Construct request
        const request = {
          project,
          region,
          resource,
        };
    
        // Run request
        const response = await computeClient.getIamPolicy(request);
        console.log(response);
      }
    
      callGetIamPolicy();
    
    

### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: protos.google.cloud.compute.v1beta.IGetIamPolicyRegionInstantSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.IGetIamPolicyRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregioninstantsnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.IGetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, callback)
    
    
    getIamPolicy(request: protos.google.cloud.compute.v1beta.IGetIamPolicyRegionInstantSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.IGetIamPolicyRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregioninstantsnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.IGetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetiampolicyregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### insert(request, options)
    
    
    insert(request?: protos.google.cloud.compute.v1beta.IInsertRegionInstantSnapshotRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Creates an instant snapshot in the specified region.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregioninstantsnapshotrequest)`   
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
       *  The body resource for this request
       */
      // const instantSnapshotResource = {}
      /**
       *  Project ID for this request.
       */
      // const project = 'my-project'
      /**
       *  Name of the region for this request.
       */
      // const region = 'us-central1'
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
      const {RegionInstantSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionInstantSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callInsert() {
        // Construct request
        const request = {
          instantSnapshotResource,
          project,
          region,
        };
    
        // Run request
        const response = await computeClient.insert(request);
        console.log(response);
      }
    
      callInsert();
    
    

### insert(request, options, callback)
    
    
    insert(request: protos.google.cloud.compute.v1beta.IInsertRegionInstantSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IInsertRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregioninstantsnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IInsertRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request, callback)
    
    
    insert(request: protos.google.cloud.compute.v1beta.IInsertRegionInstantSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.IInsertRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregioninstantsnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.IInsertRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request, options)
    
    
    list(request?: protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IInstantSnapshot[],
            protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest | null,
            protos.google.cloud.compute.v1beta.IInstantSnapshotList
        ]>;

Retrieves the list of InstantSnapshot resources contained within the specified region.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionInstantSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregioninstantsnapshotsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IInstantSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstantsnapshot)[], [protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregioninstantsnapshotsrequest) | null, [protos.google.cloud.compute.v1beta.IInstantSnapshotList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstantsnapshotlist) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### list(request, options, callback)
    
    
    list(request: protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest, protos.google.cloud.compute.v1beta.IInstantSnapshotList | null | undefined, protos.google.cloud.compute.v1beta.IInstantSnapshot>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionInstantSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregioninstantsnapshotsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregioninstantsnapshotsrequest), [protos.google.cloud.compute.v1beta.IInstantSnapshotList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstantsnapshotlist) | null | undefined, [protos.google.cloud.compute.v1beta.IInstantSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstantsnapshot)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request, callback)
    
    
    list(request: protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest, callback: PaginationCallback<protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest, protos.google.cloud.compute.v1beta.IInstantSnapshotList | null | undefined, protos.google.cloud.compute.v1beta.IInstantSnapshot>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionInstantSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregioninstantsnapshotsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregioninstantsnapshotsrequest), [protos.google.cloud.compute.v1beta.IInstantSnapshotList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstantsnapshotlist) | null | undefined, [protos.google.cloud.compute.v1beta.IInstantSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstantsnapshot)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAsync(request, options)
    
    
    listAsync(request?: protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.compute.v1beta.IInstantSnapshot>;

Equivalent to `list`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionInstantSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregioninstantsnapshotsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.compute.v1beta.IInstantSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstantsnapshot)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
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
  * The name of the region for this request. _/ // const region = 'us-central1' /_ *
  * Opt-in for partial success behavior which provides partial results in case
  * of failure. The default value is false.
  * For example, when partial success behavior is enabled, aggregatedList for a
  * single zone scope either returns all resources in the zone or no resources,
  * with an error code. */ // const returnPartialSuccess = true

// Imports the Compute library const {RegionInstantSnapshotsClient} = require('@google-cloud/compute').v1beta;

// Instantiates a client const computeClient = new RegionInstantSnapshotsClient();

async function callList() { // Construct request const request = { project, region, };

// Run request const iterable = computeClient.listAsync(request); for await (const response of iterable) { console.log(response); } }

callList();




` `

### listStream(request, options)
    
    
    listStream(request?: protos.google.cloud.compute.v1beta.IListRegionInstantSnapshotsRequest, options?: CallOptions): Transform;

Equivalent to `list`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionInstantSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistregioninstantsnapshotsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### setIamPolicy(request, options)
    
    
    setIamPolicy(request?: protos.google.cloud.compute.v1beta.ISetIamPolicyRegionInstantSnapshotRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.IPolicy,
            (protos.google.cloud.compute.v1beta.ISetIamPolicyRegionInstantSnapshotRequest | undefined),
            {} | undefined
        ]>;

Sets the access control policy on the specified resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregioninstantsnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), ([protos.google.cloud.compute.v1beta.ISetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregioninstantsnapshotrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  The name of the region for this request.
       */
      // const region = 'us-central1'
      /**
       *  The body resource for this request
       */
      // const regionSetPolicyRequestResource = {}
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
    
      // Imports the Compute library
      const {RegionInstantSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionInstantSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callSetIamPolicy() {
        // Construct request
        const request = {
          project,
          region,
          regionSetPolicyRequestResource,
          resource,
        };
    
        // Run request
        const response = await computeClient.setIamPolicy(request);
        console.log(response);
      }
    
      callSetIamPolicy();
    
    

### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: protos.google.cloud.compute.v1beta.ISetIamPolicyRegionInstantSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.ISetIamPolicyRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregioninstantsnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.ISetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, callback)
    
    
    setIamPolicy(request: protos.google.cloud.compute.v1beta.ISetIamPolicyRegionInstantSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IPolicy, protos.google.cloud.compute.v1beta.ISetIamPolicyRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregioninstantsnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ipolicy), [protos.google.cloud.compute.v1beta.ISetIamPolicyRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetiampolicyregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLabels(request, options)
    
    
    setLabels(request?: protos.google.cloud.compute.v1beta.ISetLabelsRegionInstantSnapshotRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.compute.v1beta.IOperation, null>,
            protos.google.cloud.compute.v1beta.IOperation | undefined,
            {} | undefined
        ]>;

Sets the labels on a instantSnapshot in the given region. To learn more about labels, read the Labeling Resources documentation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetlabelsregioninstantsnapshotrequest)`   
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
       *  The region for this request.
       */
      // const region = 'us-central1'
      /**
       *  The body resource for this request
       */
      // const regionSetLabelsRequestResource = {}
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
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
    
      // Imports the Compute library
      const {RegionInstantSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionInstantSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callSetLabels() {
        // Construct request
        const request = {
          project,
          region,
          regionSetLabelsRequestResource,
          resource,
        };
    
        // Run request
        const response = await computeClient.setLabels(request);
        console.log(response);
      }
    
      callSetLabels();
    
    

### setLabels(request, options, callback)
    
    
    setLabels(request: protos.google.cloud.compute.v1beta.ISetLabelsRegionInstantSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.ISetLabelsRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetlabelsregioninstantsnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.ISetLabelsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetlabelsregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLabels(request, callback)
    
    
    setLabels(request: protos.google.cloud.compute.v1beta.ISetLabelsRegionInstantSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.IOperation, protos.google.cloud.compute.v1beta.ISetLabelsRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetlabelsregioninstantsnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ioperation), [protos.google.cloud.compute.v1beta.ISetLabelsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetlabelsregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, options)
    
    
    testIamPermissions(request?: protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionInstantSnapshotRequest, options?: CallOptions): Promise<[
            protos.google.cloud.compute.v1beta.ITestPermissionsResponse,
            (protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionInstantSnapshotRequest | undefined),
            {} | undefined
        ]>;

Returns permissions that a caller has on the specified resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregioninstantsnapshotrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), ([protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregioninstantsnapshotrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.testpermissionsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  The name of the region for this request.
       */
      // const region = 'us-central1'
      /**
       *  Name or id of the resource for this request.
       */
      // const resource = 'abc123'
      /**
       *  The body resource for this request
       */
      // const testPermissionsRequestResource = {}
    
      // Imports the Compute library
      const {RegionInstantSnapshotsClient} = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const computeClient = new [RegionInstantSnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      async function callTestIamPermissions() {
        // Construct request
        const request = {
          project,
          region,
          resource,
          testPermissionsRequestResource,
        };
    
        // Run request
        const response = await computeClient.testIamPermissions(request);
        console.log(response);
      }
    
      callTestIamPermissions();
    
    

### testIamPermissions(request, options, callback)
    
    
    testIamPermissions(request: protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionInstantSnapshotRequest, options: CallOptions, callback: Callback<protos.google.cloud.compute.v1beta.ITestPermissionsResponse, protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregioninstantsnapshotrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), [protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, callback)
    
    
    testIamPermissions(request: protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionInstantSnapshotRequest, callback: Callback<protos.google.cloud.compute.v1beta.ITestPermissionsResponse, protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionInstantSnapshotRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregioninstantsnapshotrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.compute.v1beta.ITestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestpermissionsresponse), [protos.google.cloud.compute.v1beta.ITestIamPermissionsRegionInstantSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsregioninstantsnapshotrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
