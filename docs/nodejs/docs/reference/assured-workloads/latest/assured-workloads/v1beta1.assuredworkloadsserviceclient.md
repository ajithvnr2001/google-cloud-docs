---
url: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/v1beta1.assuredworkloadsserviceclient
title: Class v1beta1.AssuredWorkloadsServiceClient (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:03.208729+00:00
---

# Class v1beta1.AssuredWorkloadsServiceClient (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/v1beta1.assuredworkloadsserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.AssuredWorkloadsServiceClient (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.6.2  3.5.0  3.4.1  3.2.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.6 

Service to manage AssuredWorkloads. v1beta1

## Package

[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of AssuredWorkloadsServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new AssuredWorkloadsServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### assuredWorkloadsServiceStub
    
    
    assuredWorkloadsServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### analyzeWorkloadMove(request, options)
    
    
    analyzeWorkloadMove(request?: protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveRequest, options?: CallOptions): Promise<[
            protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveResponse,
            (protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveRequest | undefined),
            {} | undefined
        ]>;

Analyze if the source Assured Workloads can be moved to the target Assured Workload

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeWorkloadMoveRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ianalyzeworkloadmoverequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ianalyzeworkloadmoveresponse), ([protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ianalyzeworkloadmoverequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [AnalyzeWorkloadMoveResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.analyzeworkloadmoveresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The source type is a project-based workload. Specify the workloads's
       *  relative resource name, formatted as:
       *  "organizations/{ORGANIZATION_ID}/locations/{LOCATION_ID}/workloads/{WORKLOAD_ID}"
       *  For example:
       *  "organizations/123/locations/us-east1/workloads/assured-workload-1"
       */
      // const source = 'abc123'
      /**
       *  The source type is a project. Specify the project's relative resource
       *  name, formatted as either a project number or a project ID:
       *  "projects/{PROJECT_NUMBER}" or "projects/{PROJECT_ID}"
       *  For example:
       *  "projects/951040570662" when specifying a project number, or
       *  "projects/my-project-123" when specifying a project ID.
       */
      // const project = 'my-project'
      /**
       *  Required. The resource ID of the folder-based destination workload. This workload is
       *  where the source project will hypothetically be moved to. Specify the
       *  workload's relative resource name, formatted as:
       *  "organizations/{ORGANIZATION_ID}/locations/{LOCATION_ID}/workloads/{WORKLOAD_ID}"
       *  For example:
       *  "organizations/123/locations/us-east1/workloads/assured-workload-2"
       */
      // const target = 'abc123'
    
      // Imports the Assuredworkloads library
      const {AssuredWorkloadsServiceClient} = require('[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const assuredworkloadsClient = new [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)();
    
      async function callAnalyzeWorkloadMove() {
        // Construct request
        const request = {
          target,
        };
    
        // Run request
        const response = await assuredworkloadsClient.analyzeWorkloadMove(request);
        console.log(response);
      }
    
      callAnalyzeWorkloadMove();
    
    

### analyzeWorkloadMove(request, options, callback)
    
    
    analyzeWorkloadMove(request: protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveRequest, options: CallOptions, callback: Callback<protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveResponse, protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeWorkloadMoveRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ianalyzeworkloadmoverequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ianalyzeworkloadmoveresponse), [protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ianalyzeworkloadmoverequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### analyzeWorkloadMove(request, callback)
    
    
    analyzeWorkloadMove(request: protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveRequest, callback: Callback<protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveResponse, protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAnalyzeWorkloadMoveRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ianalyzeworkloadmoverequest)`   
  
`callback` |  `Callback<[protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ianalyzeworkloadmoveresponse), [protos.google.cloud.assuredworkloads.v1beta1.IAnalyzeWorkloadMoveRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ianalyzeworkloadmoverequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreateWorkloadProgress(name)
    
    
    checkCreateWorkloadProgress(name: string): Promise<LROperation<protos.google.cloud.assuredworkloads.v1beta1.Workload, protos.google.cloud.assuredworkloads.v1beta1.CreateWorkloadOperationMetadata>>;

Check the status of the long running operation returned by `createWorkload()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.assuredworkloads.v1beta1.Workload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.workload-class), [protos.google.cloud.assuredworkloads.v1beta1.CreateWorkloadOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.createworkloadoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the new Workload's parent.
       *  Must be of the form `organizations/{org_id}/locations/{location_id}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Assured Workload to create
       */
      // const workload = {}
      /**
       *  Optional. A identifier associated with the workload and underlying projects which
       *  allows for the break down of billing costs for a workload. The value
       *  provided for the identifier will add a label to the workload and contained
       *  projects with the identifier as the value.
       */
      // const externalId = 'abc123'
    
      // Imports the Assuredworkloads library
      const {AssuredWorkloadsServiceClient} = require('[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const assuredworkloadsClient = new [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)();
    
      async function callCreateWorkload() {
        // Construct request
        const request = {
          parent,
          workload,
        };
    
        // Run request
        const [operation] = await assuredworkloadsClient.createWorkload(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateWorkload();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createWorkload(request, options)
    
    
    createWorkload(request?: protos.google.cloud.assuredworkloads.v1beta1.ICreateWorkloadRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.assuredworkloads.v1beta1.IWorkload, protos.google.cloud.assuredworkloads.v1beta1.ICreateWorkloadOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates Assured Workload.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.icreateworkloadrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload), [protos.google.cloud.assuredworkloads.v1beta1.ICreateWorkloadOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.icreateworkloadoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the new Workload's parent.
       *  Must be of the form `organizations/{org_id}/locations/{location_id}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Assured Workload to create
       */
      // const workload = {}
      /**
       *  Optional. A identifier associated with the workload and underlying projects which
       *  allows for the break down of billing costs for a workload. The value
       *  provided for the identifier will add a label to the workload and contained
       *  projects with the identifier as the value.
       */
      // const externalId = 'abc123'
    
      // Imports the Assuredworkloads library
      const {AssuredWorkloadsServiceClient} = require('[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const assuredworkloadsClient = new [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)();
    
      async function callCreateWorkload() {
        // Construct request
        const request = {
          parent,
          workload,
        };
    
        // Run request
        const [operation] = await assuredworkloadsClient.createWorkload(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateWorkload();
    
    

### createWorkload(request, options, callback)
    
    
    createWorkload(request: protos.google.cloud.assuredworkloads.v1beta1.ICreateWorkloadRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.assuredworkloads.v1beta1.IWorkload, protos.google.cloud.assuredworkloads.v1beta1.ICreateWorkloadOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.icreateworkloadrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload), [protos.google.cloud.assuredworkloads.v1beta1.ICreateWorkloadOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.icreateworkloadoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkload(request, callback)
    
    
    createWorkload(request: protos.google.cloud.assuredworkloads.v1beta1.ICreateWorkloadRequest, callback: Callback<LROperation<protos.google.cloud.assuredworkloads.v1beta1.IWorkload, protos.google.cloud.assuredworkloads.v1beta1.ICreateWorkloadOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.icreateworkloadrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload), [protos.google.cloud.assuredworkloads.v1beta1.ICreateWorkloadOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.icreateworkloadoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deleteWorkload(request, options)
    
    
    deleteWorkload(request?: protos.google.cloud.assuredworkloads.v1beta1.IDeleteWorkloadRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.assuredworkloads.v1beta1.IDeleteWorkloadRequest | undefined),
            {} | undefined
        ]>;

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error. In addition to assuredworkloads.workload.delete permission, the user should also have orgpolicy.policy.set permission on the deleted folder to remove Assured Workloads OrgPolicies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ideleteworkloadrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.iempty), ([protos.google.cloud.assuredworkloads.v1beta1.IDeleteWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ideleteworkloadrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The `name` field is used to identify the workload.
       *  Format:
       *  organizations/{org_id}/locations/{location_id}/workloads/{workload_id}
       */
      // const name = 'abc123'
      /**
       *  Optional. The etag of the workload.
       *  If this is provided, it must match the server's etag.
       */
      // const etag = 'abc123'
    
      // Imports the Assuredworkloads library
      const {AssuredWorkloadsServiceClient} = require('[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const assuredworkloadsClient = new [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)();
    
      async function callDeleteWorkload() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await assuredworkloadsClient.deleteWorkload(request);
        console.log(response);
      }
    
      callDeleteWorkload();
    
    

### deleteWorkload(request, options, callback)
    
    
    deleteWorkload(request: protos.google.cloud.assuredworkloads.v1beta1.IDeleteWorkloadRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.assuredworkloads.v1beta1.IDeleteWorkloadRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ideleteworkloadrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.iempty), [protos.google.cloud.assuredworkloads.v1beta1.IDeleteWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ideleteworkloadrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkload(request, callback)
    
    
    deleteWorkload(request: protos.google.cloud.assuredworkloads.v1beta1.IDeleteWorkloadRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.assuredworkloads.v1beta1.IDeleteWorkloadRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ideleteworkloadrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.iempty), [protos.google.cloud.assuredworkloads.v1beta1.IDeleteWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ideleteworkloadrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.operation)]>` |   
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
  
### getWorkload(request, options)
    
    
    getWorkload(request?: protos.google.cloud.assuredworkloads.v1beta1.IGetWorkloadRequest, options?: CallOptions): Promise<[
            protos.google.cloud.assuredworkloads.v1beta1.IWorkload,
            (protos.google.cloud.assuredworkloads.v1beta1.IGetWorkloadRequest | undefined),
            {} | undefined
        ]>;

Gets Assured Workload associated with a CRM Node

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.igetworkloadrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload), ([protos.google.cloud.assuredworkloads.v1beta1.IGetWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.igetworkloadrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Workload to fetch. This is the workloads's
       *  relative path in the API, formatted as
       *  "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}".
       *  For example,
       *  "organizations/123/locations/us-east1/workloads/assured-workload-1".
       */
      // const name = 'abc123'
    
      // Imports the Assuredworkloads library
      const {AssuredWorkloadsServiceClient} = require('[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const assuredworkloadsClient = new [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)();
    
      async function callGetWorkload() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await assuredworkloadsClient.getWorkload(request);
        console.log(response);
      }
    
      callGetWorkload();
    
    

### getWorkload(request, options, callback)
    
    
    getWorkload(request: protos.google.cloud.assuredworkloads.v1beta1.IGetWorkloadRequest, options: CallOptions, callback: Callback<protos.google.cloud.assuredworkloads.v1beta1.IWorkload, protos.google.cloud.assuredworkloads.v1beta1.IGetWorkloadRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.igetworkloadrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload), [protos.google.cloud.assuredworkloads.v1beta1.IGetWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.igetworkloadrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkload(request, callback)
    
    
    getWorkload(request: protos.google.cloud.assuredworkloads.v1beta1.IGetWorkloadRequest, callback: Callback<protos.google.cloud.assuredworkloads.v1beta1.IWorkload, protos.google.cloud.assuredworkloads.v1beta1.IGetWorkloadRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.igetworkloadrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload), [protos.google.cloud.assuredworkloads.v1beta1.IGetWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.igetworkloadrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listWorkloads(request, options)
    
    
    listWorkloads(request?: protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.assuredworkloads.v1beta1.IWorkload[],
            protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest | null,
            protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsResponse
        ]>;

Lists Assured Workloads under a CRM Node.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload)[], [protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsrequest) | null, [protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listWorkloadsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkloads(request, options, callback)
    
    
    listWorkloads(request: protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest, protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsResponse | null | undefined, protos.google.cloud.assuredworkloads.v1beta1.IWorkload>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsrequest), [protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsresponse) | null | undefined, [protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkloads(request, callback)
    
    
    listWorkloads(request: protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest, callback: PaginationCallback<protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest, protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsResponse | null | undefined, protos.google.cloud.assuredworkloads.v1beta1.IWorkload>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsrequest), [protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsresponse) | null | undefined, [protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkloadsAsync(request, options)
    
    
    listWorkloadsAsync(request?: protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.assuredworkloads.v1beta1.IWorkload>;

Equivalent to `listWorkloads`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent Resource to list workloads from.
       *  Must be of the form `organizations/{org_id}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Page size.
       */
      // const pageSize = 1234
      /**
       *  Page token returned from previous request. Page token contains context from
       *  previous request. Page token needs to be passed in the second and following
       *  requests.
       */
      // const pageToken = 'abc123'
      /**
       *  A custom filter for filtering by properties of a workload. At this time,
       *  only filtering by labels is supported.
       */
      // const filter = 'abc123'
    
      // Imports the Assuredworkloads library
      const {AssuredWorkloadsServiceClient} = require('[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const assuredworkloadsClient = new [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)();
    
      async function callListWorkloads() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = assuredworkloadsClient.listWorkloadsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListWorkloads();
    
    

### listWorkloadsStream(request, options)
    
    
    listWorkloadsStream(request?: protos.google.cloud.assuredworkloads.v1beta1.IListWorkloadsRequest, options?: CallOptions): Transform;

Equivalent to `listWorkloads`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.ilistworkloadsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listWorkloadsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchLocationFromWorkloadName(workloadName)
    
    
    matchLocationFromWorkloadName(workloadName: string): string | number;

Parse the location from Workload resource.

**Parameter**  
---  
**Name** | **Description**  
`workloadName` |  `string`   
A fully-qualified path representing Workload resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchOrganizationFromWorkloadName(workloadName)
    
    
    matchOrganizationFromWorkloadName(workloadName: string): string | number;

Parse the organization from Workload resource.

**Parameter**  
---  
**Name** | **Description**  
`workloadName` |  `string`   
A fully-qualified path representing Workload resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchWorkloadFromWorkloadName(workloadName)
    
    
    matchWorkloadFromWorkloadName(workloadName: string): string | number;

Parse the workload from Workload resource.

**Parameter**  
---  
**Name** | **Description**  
`workloadName` |  `string`   
A fully-qualified path representing Workload resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the workload.  
  
### restrictAllowedResources(request, options)
    
    
    restrictAllowedResources(request?: protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse,
            (protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesRequest | undefined),
            {} | undefined
        ]>;

Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestrictAllowedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesresponse), ([protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.restrictallowedresourcesresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Workload. This is the workloads's
       *  relative path in the API, formatted as
       *  "organizations/{organization_id}/locations/{location_id}/workloads/{workload_id}".
       *  For example,
       *  "organizations/123/locations/us-east1/workloads/assured-workload-1".
       */
      // const name = 'abc123'
      /**
       *  Required. The type of restriction for using gcp products in the Workload environment.
       */
      // const restrictionType = {}
    
      // Imports the Assuredworkloads library
      const {AssuredWorkloadsServiceClient} = require('[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const assuredworkloadsClient = new [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)();
    
      async function callRestrictAllowedResources() {
        // Construct request
        const request = {
          name,
          restrictionType,
        };
    
        // Run request
        const response = await assuredworkloadsClient.restrictAllowedResources(request);
        console.log(response);
      }
    
      callRestrictAllowedResources();
    
    

### restrictAllowedResources(request, options, callback)
    
    
    restrictAllowedResources(request: protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesRequest, options: CallOptions, callback: Callback<protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse, protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestrictAllowedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesresponse), [protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restrictAllowedResources(request, callback)
    
    
    restrictAllowedResources(request: protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesRequest, callback: Callback<protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse, protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestrictAllowedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesresponse), [protos.google.cloud.assuredworkloads.v1beta1.IRestrictAllowedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.irestrictallowedresourcesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWorkload(request, options)
    
    
    updateWorkload(request?: protos.google.cloud.assuredworkloads.v1beta1.IUpdateWorkloadRequest, options?: CallOptions): Promise<[
            protos.google.cloud.assuredworkloads.v1beta1.IWorkload,
            (protos.google.cloud.assuredworkloads.v1beta1.IUpdateWorkloadRequest | undefined),
            {} | undefined
        ]>;

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iupdateworkloadrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload), ([protos.google.cloud.assuredworkloads.v1beta1.IUpdateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iupdateworkloadrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workload to update.
       *  The workload's `name` field is used to identify the workload to be updated.
       *  Format:
       *  organizations/{org_id}/locations/{location_id}/workloads/{workload_id}
       */
      // const workload = {}
      /**
       *  Required. The list of fields to be updated.
       */
      // const updateMask = {}
    
      // Imports the Assuredworkloads library
      const {AssuredWorkloadsServiceClient} = require('[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const assuredworkloadsClient = new [AssuredWorkloadsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)();
    
      async function callUpdateWorkload() {
        // Construct request
        const request = {
          workload,
          updateMask,
        };
    
        // Run request
        const response = await assuredworkloadsClient.updateWorkload(request);
        console.log(response);
      }
    
      callUpdateWorkload();
    
    

### updateWorkload(request, options, callback)
    
    
    updateWorkload(request: protos.google.cloud.assuredworkloads.v1beta1.IUpdateWorkloadRequest, options: CallOptions, callback: Callback<protos.google.cloud.assuredworkloads.v1beta1.IWorkload, protos.google.cloud.assuredworkloads.v1beta1.IUpdateWorkloadRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iupdateworkloadrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload), [protos.google.cloud.assuredworkloads.v1beta1.IUpdateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iupdateworkloadrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWorkload(request, callback)
    
    
    updateWorkload(request: protos.google.cloud.assuredworkloads.v1beta1.IUpdateWorkloadRequest, callback: Callback<protos.google.cloud.assuredworkloads.v1beta1.IWorkload, protos.google.cloud.assuredworkloads.v1beta1.IUpdateWorkloadRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iupdateworkloadrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.assuredworkloads.v1beta1.IWorkload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload), [protos.google.cloud.assuredworkloads.v1beta1.IUpdateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iupdateworkloadrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### workloadPath(organization, location, workload)
    
    
    workloadPath(organization: string, location: string, workload: string): string;

Return a fully-qualified workload resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`location` |  `string`   
  
`workload` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
