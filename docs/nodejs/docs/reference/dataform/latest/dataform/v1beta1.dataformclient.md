---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/v1beta1.dataformclient
title: Class v1beta1.DataformClient (3.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:09.950831+00:00
---

# Class v1beta1.DataformClient (3.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/v1beta1.dataformclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.DataformClient (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

Dataform is a service to develop, create, document, test, and update curated tables in BigQuery. v1beta1

## Package

[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DataformClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DataformClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### dataformStub
    
    
    dataformStub?: Promise<{
            [name: string]: Function;
        }>;

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

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### cancelWorkflowInvocation(request, options)
    
    
    cancelWorkflowInvocation(request?: protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationResponse,
            (protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationRequest | undefined),
            {} | undefined
        ]>;

Requests cancellation of a running WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icancelworkflowinvocationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icancelworkflowinvocationresponse), ([protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icancelworkflowinvocationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [CancelWorkflowInvocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.cancelworkflowinvocationresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workflow invocation resource's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCancelWorkflowInvocation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.cancelWorkflowInvocation(request);
        console.log(response);
      }
    
      callCancelWorkflowInvocation();
    
    

### cancelWorkflowInvocation(request, options, callback)
    
    
    cancelWorkflowInvocation(request: protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationResponse, protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icancelworkflowinvocationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icancelworkflowinvocationresponse), [protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icancelworkflowinvocationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelWorkflowInvocation(request, callback)
    
    
    cancelWorkflowInvocation(request: protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationResponse, protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icancelworkflowinvocationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icancelworkflowinvocationresponse), [protos.google.cloud.dataform.v1beta1.ICancelWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icancelworkflowinvocationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkDeleteFolderTreeProgress(name)
    
    
    checkDeleteFolderTreeProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata>>;

Check the status of the long running operation returned by `deleteFolderTree()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty), [protos.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.deletefoldertreemetadata-class)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Folder's name.
       *  Format: projects/{project}/locations/{location}/folders/{folder}
       */
      // const name = 'abc123'
      /**
       *  Optional. If `false` (default): The operation will fail if any
       *  Repository within the folder hierarchy has associated Release Configs or
       *  Workflow Configs.
       *  If `true`: The operation will attempt to delete everything, including any
       *  Release Configs and Workflow Configs linked to Repositories within the
       *  folder hierarchy. This permanently removes schedules and resources.
       */
      // const force = true
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteFolderTree() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataformClient.deleteFolderTree(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteFolderTree();
    
    

### checkDeleteRepositoryLongRunningProgress(name)
    
    
    checkDeleteRepositoryLongRunningProgress(name: string): Promise<LROperation<protos.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningResponse, protos.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningMetadata>>;

Check the status of the long running operation returned by `deleteRepositoryLongRunning()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.deleterepositorylongrunningresponse), [protos.google.cloud.dataform.v1beta1.DeleteRepositoryLongRunningMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.deleterepositorylongrunningmetadata-class)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. If set to true, child resources of this repository (compilation
       *  results and workflow invocations) will also be deleted. Otherwise, the
       *  request will only succeed if the repository has no child resources.
       *  **Note:** *This flag doesn't support deletion of workspaces, release
       *  configs or workflow configs. If any of such resources exists in the
       *  repository, the request will fail.*
       */
      // const force = true
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteRepositoryLongRunning() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataformClient.deleteRepositoryLongRunning(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteRepositoryLongRunning();
    
    

### checkDeleteTeamFolderTreeProgress(name)
    
    
    checkDeleteTeamFolderTreeProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata>>;

Check the status of the long running operation returned by `deleteTeamFolderTree()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty), [protos.google.cloud.dataform.v1beta1.DeleteFolderTreeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.deletefoldertreemetadata-class)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The TeamFolder's name.
       *  Format: projects/{project}/locations/{location}/teamFolders/{team_folder}
       */
      // const name = 'abc123'
      /**
       *  Optional. If `false` (default): The operation will fail if any
       *  Repository within the folder hierarchy has associated Release Configs or
       *  Workflow Configs.
       *  If `true`: The operation will attempt to delete everything, including any
       *  Release Configs and Workflow Configs linked to Repositories within the
       *  folder hierarchy. This permanently removes schedules and resources.
       */
      // const force = true
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteTeamFolderTree() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataformClient.deleteTeamFolderTree(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTeamFolderTree();
    
    

### checkMoveFolderProgress(name)
    
    
    checkMoveFolderProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.dataform.v1beta1.MoveFolderMetadata>>;

Check the status of the long running operation returned by `moveFolder()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty), [protos.google.cloud.dataform.v1beta1.MoveFolderMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.movefoldermetadata-class)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The full resource name of the Folder to move.
       */
      // const name = 'abc123'
      /**
       *  Optional. The name of the Folder, TeamFolder, or root location to move the
       *  Folder to. Can be in the format of: "" to move into the root User folder,
       *  `projects/* /locations/* /folders/*`, `projects/* /locations/* /teamFolders/*`
       */
      // const destinationContainingFolder = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callMoveFolder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataformClient.moveFolder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callMoveFolder();
    
    

### checkMoveRepositoryProgress(name)
    
    
    checkMoveRepositoryProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.dataform.v1beta1.MoveRepositoryMetadata>>;

Check the status of the long running operation returned by `moveRepository()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty), [protos.google.cloud.dataform.v1beta1.MoveRepositoryMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.moverepositorymetadata-class)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The full resource name of the repository to move.
       */
      // const name = 'abc123'
      /**
       *  Optional. The name of the Folder, TeamFolder, or root location to move the
       *  repository to. Can be in the format of: "" to move into the root User
       *  folder, `projects/* /locations/* /folders/*`,
       *  `projects/* /locations/* /teamFolders/*`
       */
      // const destinationContainingFolder = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callMoveRepository() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataformClient.moveRepository(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callMoveRepository();
    
    

### checkoutWorkspaceBranch(request, options)
    
    
    checkoutWorkspaceBranch(request?: protos.google.cloud.dataform.v1beta1.ICheckoutWorkspaceBranchRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.dataform.v1beta1.ICheckoutWorkspaceBranchRequest | undefined),
            {} | undefined
        ]>;

Checkout a branch in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icheckoutworkspacebranchrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), ([protos.google.cloud.dataform.v1beta1.ICheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icheckoutworkspacebranchrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace resource name.
       *  Format:
       *  projects/{project}/locations/{location}/repositories/{repository}/workspaces/{workspace}
       */
      // const name = 'abc123'
      /**
       *  Required. The name of the branch in the Git repository to which the
       *  workspace should be checked out.
       */
      // const branch = 'abc123'
      /**
       *  Optional. If set to true and the branch does not exist, it will be created.
       *  Otherwise, an error will be thrown.
       */
      // const createIfNotExists = true
      /**
       *  Optional. The name of the branch in the Git repository from which the new
       *  branch should be created. If left unset, the workspace's current branch
       *  name will be used. Accepts only branch names from FetchWorkspaceBranches
       *  response, and can only be set if `create_if_not_exists` is true. Oherwise,
       *  an error will be thrown.
       */
      // const sourceBranch = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCheckoutWorkspaceBranch() {
        // Construct request
        const request = {
          name,
          branch,
        };
    
        // Run request
        const response = await dataformClient.checkoutWorkspaceBranch(request);
        console.log(response);
      }
    
      callCheckoutWorkspaceBranch();
    
    

### checkoutWorkspaceBranch(request, options, callback)
    
    
    checkoutWorkspaceBranch(request: protos.google.cloud.dataform.v1beta1.ICheckoutWorkspaceBranchRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.ICheckoutWorkspaceBranchRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icheckoutworkspacebranchrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.ICheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icheckoutworkspacebranchrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkoutWorkspaceBranch(request, callback)
    
    
    checkoutWorkspaceBranch(request: protos.google.cloud.dataform.v1beta1.ICheckoutWorkspaceBranchRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.ICheckoutWorkspaceBranchRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icheckoutworkspacebranchrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.ICheckoutWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icheckoutworkspacebranchrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### commitRepositoryChanges(request, options)
    
    
    commitRepositoryChanges(request?: protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesResponse,
            (protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesRequest | undefined),
            {} | undefined
        ]>;

Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitRepositoryChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitrepositorychangesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitrepositorychangesresponse), ([protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitrepositorychangesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [CommitRepositoryChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.commitrepositorychangesresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository's name.
       */
      // const name = 'abc123'
      /**
       *  Required. The changes to commit to the repository.
       */
      // const commitMetadata = {}
      /**
       *  Optional. The commit SHA which must be the repository's current HEAD before
       *  applying this commit; otherwise this request will fail. If unset, no
       *  validation on the current HEAD commit SHA is performed.
       */
      // const requiredHeadCommitSha = 'abc123'
      /**
       *  Optional. A map to the path of the file to the operation. The path is the
       *  full file path including filename, from repository root.
       */
      // const fileOperations = [1,2,3,4]
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCommitRepositoryChanges() {
        // Construct request
        const request = {
          name,
          commitMetadata,
        };
    
        // Run request
        const response = await dataformClient.commitRepositoryChanges(request);
        console.log(response);
      }
    
      callCommitRepositoryChanges();
    
    

### commitRepositoryChanges(request, options, callback)
    
    
    commitRepositoryChanges(request: protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesResponse, protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitRepositoryChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitrepositorychangesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitrepositorychangesresponse), [protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitrepositorychangesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### commitRepositoryChanges(request, callback)
    
    
    commitRepositoryChanges(request: protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesResponse, protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitRepositoryChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitrepositorychangesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitrepositorychangesresponse), [protos.google.cloud.dataform.v1beta1.ICommitRepositoryChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitrepositorychangesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### commitWorkspaceChanges(request, options)
    
    
    commitWorkspaceChanges(request?: protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesResponse,
            (protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesRequest | undefined),
            {} | undefined
        ]>;

Applies a Git commit for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitworkspacechangesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitworkspacechangesresponse), ([protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitworkspacechangesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [CommitWorkspaceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.commitworkspacechangesresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const name = 'abc123'
      /**
       *  Required. The commit's author.
       */
      // const author = {}
      /**
       *  Optional. The commit's message.
       */
      // const commitMessage = 'abc123'
      /**
       *  Optional. Full file paths to commit including filename, rooted at workspace
       *  root. If left empty, all files will be committed.
       */
      // const paths = ['abc','def']
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCommitWorkspaceChanges() {
        // Construct request
        const request = {
          name,
          author,
        };
    
        // Run request
        const response = await dataformClient.commitWorkspaceChanges(request);
        console.log(response);
      }
    
      callCommitWorkspaceChanges();
    
    

### commitWorkspaceChanges(request, options, callback)
    
    
    commitWorkspaceChanges(request: protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesResponse, protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitworkspacechangesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitworkspacechangesresponse), [protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitworkspacechangesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### commitWorkspaceChanges(request, callback)
    
    
    commitWorkspaceChanges(request: protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesResponse, protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitworkspacechangesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitworkspacechangesresponse), [protos.google.cloud.dataform.v1beta1.ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitworkspacechangesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### compilationResultPath(project, location, repository, compilationResult)
    
    
    compilationResultPath(project: string, location: string, repository: string, compilationResult: string): string;

Return a fully-qualified compilationResult resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`repository` |  `string`   
  
`compilationResult` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### computeRepositoryAccessTokenStatus(request, options)
    
    
    computeRepositoryAccessTokenStatus(request?: protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusResponse,
            (protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusRequest | undefined),
            {} | undefined
        ]>;

Computes a Repository's Git access token status.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icomputerepositoryaccesstokenstatusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icomputerepositoryaccesstokenstatusresponse), ([protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icomputerepositoryaccesstokenstatusrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callComputeRepositoryAccessTokenStatus() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.computeRepositoryAccessTokenStatus(request);
        console.log(response);
      }
    
      callComputeRepositoryAccessTokenStatus();
    
    

### computeRepositoryAccessTokenStatus(request, options, callback)
    
    
    computeRepositoryAccessTokenStatus(request: protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusResponse, protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icomputerepositoryaccesstokenstatusrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icomputerepositoryaccesstokenstatusresponse), [protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icomputerepositoryaccesstokenstatusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### computeRepositoryAccessTokenStatus(request, callback)
    
    
    computeRepositoryAccessTokenStatus(request: protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusResponse, protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icomputerepositoryaccesstokenstatusrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icomputerepositoryaccesstokenstatusresponse), [protos.google.cloud.dataform.v1beta1.IComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icomputerepositoryaccesstokenstatusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### configPath(project, location)
    
    
    configPath(project: string, location: string): string;

Return a fully-qualified config resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createCompilationResult(request, options)
    
    
    createCompilationResult(request?: protos.google.cloud.dataform.v1beta1.ICreateCompilationResultRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ICompilationResult,
            (protos.google.cloud.dataform.v1beta1.ICreateCompilationResultRequest | undefined),
            {} | undefined
        ]>;

Creates a new CompilationResult in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatecompilationresultrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresult), ([protos.google.cloud.dataform.v1beta1.ICreateCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatecompilationresultrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository in which to create the compilation result. Must be
       *  in the format `projects/* /locations/* /repositories/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The compilation result to create.
       */
      // const compilationResult = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCreateCompilationResult() {
        // Construct request
        const request = {
          parent,
          compilationResult,
        };
    
        // Run request
        const response = await dataformClient.createCompilationResult(request);
        console.log(response);
      }
    
      callCreateCompilationResult();
    
    

### createCompilationResult(request, options, callback)
    
    
    createCompilationResult(request: protos.google.cloud.dataform.v1beta1.ICreateCompilationResultRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.ICompilationResult, protos.google.cloud.dataform.v1beta1.ICreateCompilationResultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatecompilationresultrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresult), [protos.google.cloud.dataform.v1beta1.ICreateCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatecompilationresultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCompilationResult(request, callback)
    
    
    createCompilationResult(request: protos.google.cloud.dataform.v1beta1.ICreateCompilationResultRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.ICompilationResult, protos.google.cloud.dataform.v1beta1.ICreateCompilationResultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatecompilationresultrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresult), [protos.google.cloud.dataform.v1beta1.ICreateCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatecompilationresultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFolder(request, options)
    
    
    createFolder(request?: protos.google.cloud.dataform.v1beta1.ICreateFolderRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IFolder,
            protos.google.cloud.dataform.v1beta1.ICreateFolderRequest | undefined,
            {} | undefined
        ]>;

Creates a new Folder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatefolderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifolder), [protos.google.cloud.dataform.v1beta1.ICreateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatefolderrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Folder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.folder). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The location in which to create the Folder. Must be in the format
       *  `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The Folder to create.
       */
      // const folder = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCreateFolder() {
        // Construct request
        const request = {
          parent,
          folder,
        };
    
        // Run request
        const response = await dataformClient.createFolder(request);
        console.log(response);
      }
    
      callCreateFolder();
    
    

### createFolder(request, options, callback)
    
    
    createFolder(request: protos.google.cloud.dataform.v1beta1.ICreateFolderRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IFolder, protos.google.cloud.dataform.v1beta1.ICreateFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatefolderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifolder), [protos.google.cloud.dataform.v1beta1.ICreateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatefolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFolder(request, callback)
    
    
    createFolder(request: protos.google.cloud.dataform.v1beta1.ICreateFolderRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IFolder, protos.google.cloud.dataform.v1beta1.ICreateFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatefolderrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifolder), [protos.google.cloud.dataform.v1beta1.ICreateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatefolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createReleaseConfig(request, options)
    
    
    createReleaseConfig(request?: protos.google.cloud.dataform.v1beta1.ICreateReleaseConfigRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IReleaseConfig,
            (protos.google.cloud.dataform.v1beta1.ICreateReleaseConfigRequest | undefined),
            {} | undefined
        ]>;

Creates a new ReleaseConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatereleaseconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig), ([protos.google.cloud.dataform.v1beta1.ICreateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatereleaseconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository in which to create the release config. Must be in
       *  the format `projects/* /locations/* /repositories/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The release config to create.
       */
      // const releaseConfig = {}
      /**
       *  Required. The ID to use for the release config, which will become the final
       *  component of the release config's resource name.
       */
      // const releaseConfigId = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCreateReleaseConfig() {
        // Construct request
        const request = {
          parent,
          releaseConfig,
          releaseConfigId,
        };
    
        // Run request
        const response = await dataformClient.createReleaseConfig(request);
        console.log(response);
      }
    
      callCreateReleaseConfig();
    
    

### createReleaseConfig(request, options, callback)
    
    
    createReleaseConfig(request: protos.google.cloud.dataform.v1beta1.ICreateReleaseConfigRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IReleaseConfig, protos.google.cloud.dataform.v1beta1.ICreateReleaseConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatereleaseconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig), [protos.google.cloud.dataform.v1beta1.ICreateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatereleaseconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createReleaseConfig(request, callback)
    
    
    createReleaseConfig(request: protos.google.cloud.dataform.v1beta1.ICreateReleaseConfigRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IReleaseConfig, protos.google.cloud.dataform.v1beta1.ICreateReleaseConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatereleaseconfigrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig), [protos.google.cloud.dataform.v1beta1.ICreateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreatereleaseconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRepository(request, options)
    
    
    createRepository(request?: protos.google.cloud.dataform.v1beta1.ICreateRepositoryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IRepository,
            protos.google.cloud.dataform.v1beta1.ICreateRepositoryRequest | undefined,
            {} | undefined
        ]>;

Creates a new Repository in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreaterepositoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository), [protos.google.cloud.dataform.v1beta1.ICreateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreaterepositoryrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The location in which to create the repository. Must be in the
       *  format `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The repository to create.
       */
      // const repository = {}
      /**
       *  Required. The ID to use for the repository, which will become the final
       *  component of the repository's resource name.
       */
      // const repositoryId = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCreateRepository() {
        // Construct request
        const request = {
          parent,
          repository,
          repositoryId,
        };
    
        // Run request
        const response = await dataformClient.createRepository(request);
        console.log(response);
      }
    
      callCreateRepository();
    
    

### createRepository(request, options, callback)
    
    
    createRepository(request: protos.google.cloud.dataform.v1beta1.ICreateRepositoryRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IRepository, protos.google.cloud.dataform.v1beta1.ICreateRepositoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreaterepositoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository), [protos.google.cloud.dataform.v1beta1.ICreateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreaterepositoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRepository(request, callback)
    
    
    createRepository(request: protos.google.cloud.dataform.v1beta1.ICreateRepositoryRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IRepository, protos.google.cloud.dataform.v1beta1.ICreateRepositoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreaterepositoryrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository), [protos.google.cloud.dataform.v1beta1.ICreateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreaterepositoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTeamFolder(request, options)
    
    
    createTeamFolder(request?: protos.google.cloud.dataform.v1beta1.ICreateTeamFolderRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ITeamFolder,
            protos.google.cloud.dataform.v1beta1.ICreateTeamFolderRequest | undefined,
            {} | undefined
        ]>;

Creates a new TeamFolder in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateteamfolderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ITeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iteamfolder), [protos.google.cloud.dataform.v1beta1.ICreateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateteamfolderrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.teamfolder). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The location in which to create the TeamFolder. Must be in the
       *  format `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The TeamFolder to create.
       */
      // const teamFolder = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCreateTeamFolder() {
        // Construct request
        const request = {
          parent,
          teamFolder,
        };
    
        // Run request
        const response = await dataformClient.createTeamFolder(request);
        console.log(response);
      }
    
      callCreateTeamFolder();
    
    

### createTeamFolder(request, options, callback)
    
    
    createTeamFolder(request: protos.google.cloud.dataform.v1beta1.ICreateTeamFolderRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.ITeamFolder, protos.google.cloud.dataform.v1beta1.ICreateTeamFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateteamfolderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ITeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iteamfolder), [protos.google.cloud.dataform.v1beta1.ICreateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateteamfolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTeamFolder(request, callback)
    
    
    createTeamFolder(request: protos.google.cloud.dataform.v1beta1.ICreateTeamFolderRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.ITeamFolder, protos.google.cloud.dataform.v1beta1.ICreateTeamFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateteamfolderrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ITeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iteamfolder), [protos.google.cloud.dataform.v1beta1.ICreateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateteamfolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkflowConfig(request, options)
    
    
    createWorkflowConfig(request?: protos.google.cloud.dataform.v1beta1.ICreateWorkflowConfigRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkflowConfig,
            (protos.google.cloud.dataform.v1beta1.ICreateWorkflowConfigRequest | undefined),
            {} | undefined
        ]>;

Creates a new WorkflowConfig in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig), ([protos.google.cloud.dataform.v1beta1.ICreateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository in which to create the workflow config. Must be in
       *  the format `projects/* /locations/* /repositories/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The workflow config to create.
       */
      // const workflowConfig = {}
      /**
       *  Required. The ID to use for the workflow config, which will become the
       *  final component of the workflow config's resource name.
       */
      // const workflowConfigId = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCreateWorkflowConfig() {
        // Construct request
        const request = {
          parent,
          workflowConfig,
          workflowConfigId,
        };
    
        // Run request
        const response = await dataformClient.createWorkflowConfig(request);
        console.log(response);
      }
    
      callCreateWorkflowConfig();
    
    

### createWorkflowConfig(request, options, callback)
    
    
    createWorkflowConfig(request: protos.google.cloud.dataform.v1beta1.ICreateWorkflowConfigRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkflowConfig, protos.google.cloud.dataform.v1beta1.ICreateWorkflowConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig), [protos.google.cloud.dataform.v1beta1.ICreateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkflowConfig(request, callback)
    
    
    createWorkflowConfig(request: protos.google.cloud.dataform.v1beta1.ICreateWorkflowConfigRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkflowConfig, protos.google.cloud.dataform.v1beta1.ICreateWorkflowConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowconfigrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig), [protos.google.cloud.dataform.v1beta1.ICreateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkflowInvocation(request, options)
    
    
    createWorkflowInvocation(request?: protos.google.cloud.dataform.v1beta1.ICreateWorkflowInvocationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkflowInvocation,
            (protos.google.cloud.dataform.v1beta1.ICreateWorkflowInvocationRequest | undefined),
            {} | undefined
        ]>;

Creates a new WorkflowInvocation in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowinvocationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocation), ([protos.google.cloud.dataform.v1beta1.ICreateWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowinvocationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository in which to create the workflow invocation. Must
       *  be in the format `projects/* /locations/* /repositories/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The workflow invocation resource to create.
       */
      // const workflowInvocation = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCreateWorkflowInvocation() {
        // Construct request
        const request = {
          parent,
          workflowInvocation,
        };
    
        // Run request
        const response = await dataformClient.createWorkflowInvocation(request);
        console.log(response);
      }
    
      callCreateWorkflowInvocation();
    
    

### createWorkflowInvocation(request, options, callback)
    
    
    createWorkflowInvocation(request: protos.google.cloud.dataform.v1beta1.ICreateWorkflowInvocationRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkflowInvocation, protos.google.cloud.dataform.v1beta1.ICreateWorkflowInvocationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowinvocationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocation), [protos.google.cloud.dataform.v1beta1.ICreateWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowinvocationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkflowInvocation(request, callback)
    
    
    createWorkflowInvocation(request: protos.google.cloud.dataform.v1beta1.ICreateWorkflowInvocationRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkflowInvocation, protos.google.cloud.dataform.v1beta1.ICreateWorkflowInvocationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowinvocationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocation), [protos.google.cloud.dataform.v1beta1.ICreateWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkflowinvocationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkspace(request, options)
    
    
    createWorkspace(request?: protos.google.cloud.dataform.v1beta1.ICreateWorkspaceRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkspace,
            protos.google.cloud.dataform.v1beta1.ICreateWorkspaceRequest | undefined,
            {} | undefined
        ]>;

Creates a new Workspace in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkspacerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkspace), [protos.google.cloud.dataform.v1beta1.ICreateWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkspacerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Workspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.workspace). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository in which to create the workspace. Must be in the
       *  format `projects/* /locations/* /repositories/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The workspace to create.
       */
      // const workspace = {}
      /**
       *  Required. The ID to use for the workspace, which will become the final
       *  component of the workspace's resource name.
       */
      // const workspaceId = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callCreateWorkspace() {
        // Construct request
        const request = {
          parent,
          workspace,
          workspaceId,
        };
    
        // Run request
        const response = await dataformClient.createWorkspace(request);
        console.log(response);
      }
    
      callCreateWorkspace();
    
    

### createWorkspace(request, options, callback)
    
    
    createWorkspace(request: protos.google.cloud.dataform.v1beta1.ICreateWorkspaceRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkspace, protos.google.cloud.dataform.v1beta1.ICreateWorkspaceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkspacerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkspace), [protos.google.cloud.dataform.v1beta1.ICreateWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkspacerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkspace(request, callback)
    
    
    createWorkspace(request: protos.google.cloud.dataform.v1beta1.ICreateWorkspaceRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkspace, protos.google.cloud.dataform.v1beta1.ICreateWorkspaceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkspacerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkspace), [protos.google.cloud.dataform.v1beta1.ICreateWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icreateworkspacerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cryptoKeyPath(project, location, keyRing, cryptoKey)
    
    
    cryptoKeyPath(project: string, location: string, keyRing: string, cryptoKey: string): string;

Return a fully-qualified cryptoKey resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`keyRing` |  `string`   
  
`cryptoKey` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### cryptoKeyVersionPath(project, location, keyRing, cryptoKey, cryptoKeyVersion)
    
    
    cryptoKeyVersionPath(project: string, location: string, keyRing: string, cryptoKey: string, cryptoKeyVersion: string): string;

Return a fully-qualified cryptoKeyVersion resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`keyRing` |  `string`   
  
`cryptoKey` |  `string`   
  
`cryptoKeyVersion` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteBranch(request, options)
    
    
    deleteBranch(request?: protos.google.cloud.dataform.v1beta1.IDeleteBranchRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IDeleteBranchResponse,
            protos.google.cloud.dataform.v1beta1.IDeleteBranchRequest | undefined,
            {} | undefined
        ]>;

Deletes a branch in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletebranchrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IDeleteBranchResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletebranchresponse), [protos.google.cloud.dataform.v1beta1.IDeleteBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletebranchrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DeleteBranchResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.deletebranchresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace resource name.
       *  Format:
       *  projects/{project}/locations/{location}/repositories/{repository}/workspaces/{workspace}
       */
      // const name = 'abc123'
      /**
       *  Required. The name of the branch in the Git repository to delete.
       */
      // const branch = 'abc123'
      /**
       *  Optional. If set to true, any non-pushed commits on the branch will be
       *  deleted. Upstream branch name will be the same as the branch to delete.
       */
      // const force = true
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteBranch() {
        // Construct request
        const request = {
          name,
          branch,
        };
    
        // Run request
        const response = await dataformClient.deleteBranch(request);
        console.log(response);
      }
    
      callDeleteBranch();
    
    

### deleteBranch(request, options, callback)
    
    
    deleteBranch(request: protos.google.cloud.dataform.v1beta1.IDeleteBranchRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IDeleteBranchResponse, protos.google.cloud.dataform.v1beta1.IDeleteBranchRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletebranchrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IDeleteBranchResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletebranchresponse), [protos.google.cloud.dataform.v1beta1.IDeleteBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletebranchrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBranch(request, callback)
    
    
    deleteBranch(request: protos.google.cloud.dataform.v1beta1.IDeleteBranchRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IDeleteBranchResponse, protos.google.cloud.dataform.v1beta1.IDeleteBranchRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletebranchrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IDeleteBranchResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletebranchresponse), [protos.google.cloud.dataform.v1beta1.IDeleteBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletebranchrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFolder(request, options)
    
    
    deleteFolder(request?: protos.google.cloud.dataform.v1beta1.IDeleteFolderRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.dataform.v1beta1.IDeleteFolderRequest | undefined,
            {} | undefined
        ]>;

Deletes a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefolderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefolderrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Folder's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteFolder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.deleteFolder(request);
        console.log(response);
      }
    
      callDeleteFolder();
    
    

### deleteFolder(request, options, callback)
    
    
    deleteFolder(request: protos.google.cloud.dataform.v1beta1.IDeleteFolderRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefolderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFolder(request, callback)
    
    
    deleteFolder(request: protos.google.cloud.dataform.v1beta1.IDeleteFolderRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefolderrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFolderTree(request, options)
    
    
    deleteFolderTree(request?: protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFolderTreeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefoldertreerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefoldertreemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Folder's name.
       *  Format: projects/{project}/locations/{location}/folders/{folder}
       */
      // const name = 'abc123'
      /**
       *  Optional. If `false` (default): The operation will fail if any
       *  Repository within the folder hierarchy has associated Release Configs or
       *  Workflow Configs.
       *  If `true`: The operation will attempt to delete everything, including any
       *  Release Configs and Workflow Configs linked to Repositories within the
       *  folder hierarchy. This permanently removes schedules and resources.
       */
      // const force = true
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteFolderTree() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataformClient.deleteFolderTree(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteFolderTree();
    
    

### deleteFolderTree(request, options, callback)
    
    
    deleteFolderTree(request: protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFolderTreeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefoldertreerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefoldertreemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFolderTree(request, callback)
    
    
    deleteFolderTree(request: protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFolderTreeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefoldertreerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefoldertreemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deleteReleaseConfig(request, options)
    
    
    deleteReleaseConfig(request?: protos.google.cloud.dataform.v1beta1.IDeleteReleaseConfigRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.dataform.v1beta1.IDeleteReleaseConfigRequest | undefined),
            {} | undefined
        ]>;

Deletes a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletereleaseconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), ([protos.google.cloud.dataform.v1beta1.IDeleteReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletereleaseconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The release config's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteReleaseConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.deleteReleaseConfig(request);
        console.log(response);
      }
    
      callDeleteReleaseConfig();
    
    

### deleteReleaseConfig(request, options, callback)
    
    
    deleteReleaseConfig(request: protos.google.cloud.dataform.v1beta1.IDeleteReleaseConfigRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteReleaseConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletereleaseconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletereleaseconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteReleaseConfig(request, callback)
    
    
    deleteReleaseConfig(request: protos.google.cloud.dataform.v1beta1.IDeleteReleaseConfigRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteReleaseConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletereleaseconfigrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletereleaseconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRepository(request, options)
    
    
    deleteRepository(request?: protos.google.cloud.dataform.v1beta1.IDeleteRepositoryRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.dataform.v1beta1.IDeleteRepositoryRequest | undefined,
            {} | undefined
        ]>;

Deletes a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositoryrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. If set to true, child resources of this repository (compilation
       *  results and workflow invocations) will also be deleted. Otherwise, the
       *  request will only succeed if the repository has no child resources.
       *  **Note:** *This flag doesn't support deletion of workspaces, release
       *  configs or workflow configs. If any of such resources exists in the
       *  repository, the request will fail.*.
       */
      // const force = true
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteRepository() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.deleteRepository(request);
        console.log(response);
      }
    
      callDeleteRepository();
    
    

### deleteRepository(request, options, callback)
    
    
    deleteRepository(request: protos.google.cloud.dataform.v1beta1.IDeleteRepositoryRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteRepositoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRepository(request, callback)
    
    
    deleteRepository(request: protos.google.cloud.dataform.v1beta1.IDeleteRepositoryRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteRepositoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositoryrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRepositoryLongRunning(request, options)
    
    
    deleteRepositoryLongRunning(request?: protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningResponse, protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single repository asynchronously.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRepositoryLongRunningRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositorylongrunningrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositorylongrunningresponse), [protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositorylongrunningmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. If set to true, child resources of this repository (compilation
       *  results and workflow invocations) will also be deleted. Otherwise, the
       *  request will only succeed if the repository has no child resources.
       *  **Note:** *This flag doesn't support deletion of workspaces, release
       *  configs or workflow configs. If any of such resources exists in the
       *  repository, the request will fail.*
       */
      // const force = true
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteRepositoryLongRunning() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataformClient.deleteRepositoryLongRunning(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteRepositoryLongRunning();
    
    

### deleteRepositoryLongRunning(request, options, callback)
    
    
    deleteRepositoryLongRunning(request: protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningResponse, protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRepositoryLongRunningRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositorylongrunningrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositorylongrunningresponse), [protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositorylongrunningmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRepositoryLongRunning(request, callback)
    
    
    deleteRepositoryLongRunning(request: protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningRequest, callback: Callback<LROperation<protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningResponse, protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRepositoryLongRunningRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositorylongrunningrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositorylongrunningresponse), [protos.google.cloud.dataform.v1beta1.IDeleteRepositoryLongRunningMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleterepositorylongrunningmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTeamFolder(request, options)
    
    
    deleteTeamFolder(request?: protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderRequest | undefined,
            {} | undefined
        ]>;

Deletes a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteteamfolderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteteamfolderrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The TeamFolder's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteTeamFolder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.deleteTeamFolder(request);
        console.log(response);
      }
    
      callDeleteTeamFolder();
    
    

### deleteTeamFolder(request, options, callback)
    
    
    deleteTeamFolder(request: protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteteamfolderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteteamfolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTeamFolder(request, callback)
    
    
    deleteTeamFolder(request: protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteteamfolderrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteteamfolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTeamFolderTree(request, options)
    
    
    deleteTeamFolderTree(request?: protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderTreeRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTeamFolderTreeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteteamfoldertreerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefoldertreemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The TeamFolder's name.
       *  Format: projects/{project}/locations/{location}/teamFolders/{team_folder}
       */
      // const name = 'abc123'
      /**
       *  Optional. If `false` (default): The operation will fail if any
       *  Repository within the folder hierarchy has associated Release Configs or
       *  Workflow Configs.
       *  If `true`: The operation will attempt to delete everything, including any
       *  Release Configs and Workflow Configs linked to Repositories within the
       *  folder hierarchy. This permanently removes schedules and resources.
       */
      // const force = true
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteTeamFolderTree() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataformClient.deleteTeamFolderTree(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteTeamFolderTree();
    
    

### deleteTeamFolderTree(request, options, callback)
    
    
    deleteTeamFolderTree(request: protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderTreeRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTeamFolderTreeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteteamfoldertreerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefoldertreemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTeamFolderTree(request, callback)
    
    
    deleteTeamFolderTree(request: protos.google.cloud.dataform.v1beta1.IDeleteTeamFolderTreeRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTeamFolderTreeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteteamfoldertreerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteFolderTreeMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideletefoldertreemetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkflowConfig(request, options)
    
    
    deleteWorkflowConfig(request?: protos.google.cloud.dataform.v1beta1.IDeleteWorkflowConfigRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.dataform.v1beta1.IDeleteWorkflowConfigRequest | undefined),
            {} | undefined
        ]>;

Deletes a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), ([protos.google.cloud.dataform.v1beta1.IDeleteWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workflow config's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteWorkflowConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.deleteWorkflowConfig(request);
        console.log(response);
      }
    
      callDeleteWorkflowConfig();
    
    

### deleteWorkflowConfig(request, options, callback)
    
    
    deleteWorkflowConfig(request: protos.google.cloud.dataform.v1beta1.IDeleteWorkflowConfigRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteWorkflowConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkflowConfig(request, callback)
    
    
    deleteWorkflowConfig(request: protos.google.cloud.dataform.v1beta1.IDeleteWorkflowConfigRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteWorkflowConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowconfigrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkflowInvocation(request, options)
    
    
    deleteWorkflowInvocation(request?: protos.google.cloud.dataform.v1beta1.IDeleteWorkflowInvocationRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.dataform.v1beta1.IDeleteWorkflowInvocationRequest | undefined),
            {} | undefined
        ]>;

Deletes a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowinvocationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), ([protos.google.cloud.dataform.v1beta1.IDeleteWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowinvocationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workflow invocation resource's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteWorkflowInvocation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.deleteWorkflowInvocation(request);
        console.log(response);
      }
    
      callDeleteWorkflowInvocation();
    
    

### deleteWorkflowInvocation(request, options, callback)
    
    
    deleteWorkflowInvocation(request: protos.google.cloud.dataform.v1beta1.IDeleteWorkflowInvocationRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteWorkflowInvocationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowinvocationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowinvocationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkflowInvocation(request, callback)
    
    
    deleteWorkflowInvocation(request: protos.google.cloud.dataform.v1beta1.IDeleteWorkflowInvocationRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteWorkflowInvocationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowinvocationrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkflowinvocationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkspace(request, options)
    
    
    deleteWorkspace(request?: protos.google.cloud.dataform.v1beta1.IDeleteWorkspaceRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.dataform.v1beta1.IDeleteWorkspaceRequest | undefined,
            {} | undefined
        ]>;

Deletes a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkspacerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkspacerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace resource's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callDeleteWorkspace() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.deleteWorkspace(request);
        console.log(response);
      }
    
      callDeleteWorkspace();
    
    

### deleteWorkspace(request, options, callback)
    
    
    deleteWorkspace(request: protos.google.cloud.dataform.v1beta1.IDeleteWorkspaceRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteWorkspaceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkspacerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkspacerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkspace(request, callback)
    
    
    deleteWorkspace(request: protos.google.cloud.dataform.v1beta1.IDeleteWorkspaceRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IDeleteWorkspaceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkspacerequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IDeleteWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ideleteworkspacerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchCurrentWorkspaceBranch(request, options)
    
    
    fetchCurrentWorkspaceBranch(request?: protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchResponse,
            (protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchRequest | undefined),
            {} | undefined
        ]>;

Fetches the current branch of a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchcurrentworkspacebranchrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchcurrentworkspacebranchresponse), ([protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchcurrentworkspacebranchrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FetchCurrentWorkspaceBranchResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.fetchcurrentworkspacebranchresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace resource name.
       *  Format:
       *  projects/{project}/locations/{location}/repositories/{repository}/workspaces/{workspace}
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callFetchCurrentWorkspaceBranch() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.fetchCurrentWorkspaceBranch(request);
        console.log(response);
      }
    
      callFetchCurrentWorkspaceBranch();
    
    

### fetchCurrentWorkspaceBranch(request, options, callback)
    
    
    fetchCurrentWorkspaceBranch(request: protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchResponse, protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchcurrentworkspacebranchrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchcurrentworkspacebranchresponse), [protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchcurrentworkspacebranchrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchCurrentWorkspaceBranch(request, callback)
    
    
    fetchCurrentWorkspaceBranch(request: protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchResponse, protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchcurrentworkspacebranchrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchcurrentworkspacebranchresponse), [protos.google.cloud.dataform.v1beta1.IFetchCurrentWorkspaceBranchRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchcurrentworkspacebranchrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchFileDiff(request, options)
    
    
    fetchFileDiff(request?: protos.google.cloud.dataform.v1beta1.IFetchFileDiffRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IFetchFileDiffResponse,
            protos.google.cloud.dataform.v1beta1.IFetchFileDiffRequest | undefined,
            {} | undefined
        ]>;

Fetches Git diff for an uncommitted file in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchFileDiffRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilediffrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IFetchFileDiffResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilediffresponse), [protos.google.cloud.dataform.v1beta1.IFetchFileDiffRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilediffrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FetchFileDiffResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.fetchfilediffresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Required. The file's full path including filename, relative to the
       *  workspace root.
       */
      // const path = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callFetchFileDiff() {
        // Construct request
        const request = {
          workspace,
          path,
        };
    
        // Run request
        const response = await dataformClient.fetchFileDiff(request);
        console.log(response);
      }
    
      callFetchFileDiff();
    
    

### fetchFileDiff(request, options, callback)
    
    
    fetchFileDiff(request: protos.google.cloud.dataform.v1beta1.IFetchFileDiffRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IFetchFileDiffResponse, protos.google.cloud.dataform.v1beta1.IFetchFileDiffRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchFileDiffRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilediffrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFetchFileDiffResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilediffresponse), [protos.google.cloud.dataform.v1beta1.IFetchFileDiffRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilediffrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchFileDiff(request, callback)
    
    
    fetchFileDiff(request: protos.google.cloud.dataform.v1beta1.IFetchFileDiffRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IFetchFileDiffResponse, protos.google.cloud.dataform.v1beta1.IFetchFileDiffRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchFileDiffRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilediffrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFetchFileDiffResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilediffresponse), [protos.google.cloud.dataform.v1beta1.IFetchFileDiffRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilediffrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchFileGitStatuses(request, options)
    
    
    fetchFileGitStatuses(request?: protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesResponse,
            (protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesRequest | undefined),
            {} | undefined
        ]>;

Fetches Git statuses for the files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchFileGitStatusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilegitstatusesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilegitstatusesresponse), ([protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilegitstatusesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callFetchFileGitStatuses() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.fetchFileGitStatuses(request);
        console.log(response);
      }
    
      callFetchFileGitStatuses();
    
    

### fetchFileGitStatuses(request, options, callback)
    
    
    fetchFileGitStatuses(request: protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesResponse, protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchFileGitStatusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilegitstatusesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilegitstatusesresponse), [protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilegitstatusesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchFileGitStatuses(request, callback)
    
    
    fetchFileGitStatuses(request: protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesResponse, protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchFileGitStatusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilegitstatusesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilegitstatusesresponse), [protos.google.cloud.dataform.v1beta1.IFetchFileGitStatusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchfilegitstatusesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchGitAheadBehind(request, options)
    
    
    fetchGitAheadBehind(request?: protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindResponse,
            (protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindRequest | undefined),
            {} | undefined
        ]>;

Fetches Git ahead/behind against a remote branch.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchGitAheadBehindRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchgitaheadbehindrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchgitaheadbehindresponse), ([protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchgitaheadbehindrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FetchGitAheadBehindResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.fetchgitaheadbehindresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. The name of the branch in the Git remote against which this
       *  workspace should be compared. If left unset, the repository's default
       *  branch name will be used.
       */
      // const remoteBranch = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callFetchGitAheadBehind() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.fetchGitAheadBehind(request);
        console.log(response);
      }
    
      callFetchGitAheadBehind();
    
    

### fetchGitAheadBehind(request, options, callback)
    
    
    fetchGitAheadBehind(request: protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindResponse, protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchGitAheadBehindRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchgitaheadbehindrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchgitaheadbehindresponse), [protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchgitaheadbehindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchGitAheadBehind(request, callback)
    
    
    fetchGitAheadBehind(request: protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindResponse, protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchGitAheadBehindRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchgitaheadbehindrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchgitaheadbehindresponse), [protos.google.cloud.dataform.v1beta1.IFetchGitAheadBehindRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchgitaheadbehindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchRemoteBranches(request, options)
    
    
    fetchRemoteBranches(request?: protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesResponse,
            (protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesRequest | undefined),
            {} | undefined
        ]>;

Fetches a Repository's remote branches.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchRemoteBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchremotebranchesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchremotebranchesresponse), ([protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchremotebranchesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [FetchRemoteBranchesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.fetchremotebranchesresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callFetchRemoteBranches() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.fetchRemoteBranches(request);
        console.log(response);
      }
    
      callFetchRemoteBranches();
    
    

### fetchRemoteBranches(request, options, callback)
    
    
    fetchRemoteBranches(request: protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesResponse, protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchRemoteBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchremotebranchesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchremotebranchesresponse), [protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchremotebranchesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchRemoteBranches(request, callback)
    
    
    fetchRemoteBranches(request: protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesResponse, protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchRemoteBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchremotebranchesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchremotebranchesresponse), [protos.google.cloud.dataform.v1beta1.IFetchRemoteBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchremotebranchesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchRepositoryHistory(request, options)
    
    
    fetchRepositoryHistory(request?: protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ICommitLogEntry[],
            protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest | null,
            protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryResponse
        ]>;

Fetches a Repository's history of commits. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchRepositoryHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ICommitLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitlogentry)[], [protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryrequest) | null, [protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [CommitLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.commitlogentry). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `fetchRepositoryHistoryAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchRepositoryHistory(request, options, callback)
    
    
    fetchRepositoryHistory(request: protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest, protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryResponse | null | undefined, protos.google.cloud.dataform.v1beta1.ICommitLogEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchRepositoryHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryrequest), [protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.ICommitLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitlogentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchRepositoryHistory(request, callback)
    
    
    fetchRepositoryHistory(request: protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest, protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryResponse | null | undefined, protos.google.cloud.dataform.v1beta1.ICommitLogEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchRepositoryHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryrequest), [protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.ICommitLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitlogentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchRepositoryHistoryAsync(request, options)
    
    
    fetchRepositoryHistoryAsync(request?: protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.ICommitLogEntry>;

Equivalent to `fetchRepositoryHistory`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchRepositoryHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.ICommitLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icommitlogentry)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [CommitLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.commitlogentry). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. Maximum number of commits to return. The server may return fewer
       *  items than requested. If unspecified, the server will pick an appropriate
       *  default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `FetchRepositoryHistory`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `FetchRepositoryHistory`,
       *  with the exception of `page_size`, must match the call that provided the
       *  page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callFetchRepositoryHistory() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const iterable = dataformClient.fetchRepositoryHistoryAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callFetchRepositoryHistory();
    
    

### fetchRepositoryHistoryStream(request, options)
    
    
    fetchRepositoryHistoryStream(request?: protos.google.cloud.dataform.v1beta1.IFetchRepositoryHistoryRequest, options?: CallOptions): Transform;

Equivalent to `fetchRepositoryHistory`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchRepositoryHistoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchrepositoryhistoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [CommitLogEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.commitlogentry) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `fetchRepositoryHistoryAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchWorkspaceBranches(request, options)
    
    
    fetchWorkspaceBranches(request?: protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IBranchMetadata[],
            protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest | null,
            protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesResponse
        ]>;

Fetches branches in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchWorkspaceBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IBranchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ibranchmetadata)[], [protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesrequest) | null, [protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [BranchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.branchmetadata). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `fetchWorkspaceBranchesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchWorkspaceBranches(request, options, callback)
    
    
    fetchWorkspaceBranches(request: protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest, protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IBranchMetadata>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchWorkspaceBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesrequest), [protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IBranchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ibranchmetadata)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchWorkspaceBranches(request, callback)
    
    
    fetchWorkspaceBranches(request: protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest, protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IBranchMetadata>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchWorkspaceBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesrequest), [protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IBranchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ibranchmetadata)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchWorkspaceBranchesAsync(request, options)
    
    
    fetchWorkspaceBranchesAsync(request?: protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.IBranchMetadata>;

Equivalent to `fetchWorkspaceBranches`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchWorkspaceBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.IBranchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ibranchmetadata)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [BranchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.branchmetadata). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace resource name.
       *  Format:
       *  projects/{project}/locations/{location}/repositories/{repository}/workspaces/{workspace}
       */
      // const name = 'abc123'
      /**
       *  Optional. Filter for the returned list.
       */
      // const filter = {}
      /**
       *  Optional. Maximum number of branches to return. The server may return fewer
       *  items than requested. If unspecified, the server will pick an appropriate
       *  default. The maximum value is 1000; values above 1000 will be coerced to
       *  1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `FetchWorkspaceBranches`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `FetchWorkspaceBranches`,
       *  with the exception of `page_size`, must match the call that provided the
       *  page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callFetchWorkspaceBranches() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const iterable = dataformClient.[fetchWorkspaceBranchesAsync](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/v1beta1.dataformclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callFetchWorkspaceBranches();
    
    

### fetchWorkspaceBranchesStream(request, options)
    
    
    fetchWorkspaceBranchesStream(request?: protos.google.cloud.dataform.v1beta1.IFetchWorkspaceBranchesRequest, options?: CallOptions): Transform;

Equivalent to `fetchWorkspaceBranches`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchWorkspaceBranchesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifetchworkspacebranchesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [BranchMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.branchmetadata) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `fetchWorkspaceBranchesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### folderPath(project, location, folder)
    
    
    folderPath(project: string, location: string, folder: string): string;

Return a fully-qualified folder resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`folder` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getCompilationResult(request, options)
    
    
    getCompilationResult(request?: protos.google.cloud.dataform.v1beta1.IGetCompilationResultRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ICompilationResult,
            (protos.google.cloud.dataform.v1beta1.IGetCompilationResultRequest | undefined),
            {} | undefined
        ]>;

Fetches a single CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetcompilationresultrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresult), ([protos.google.cloud.dataform.v1beta1.IGetCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetcompilationresultrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The compilation result's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callGetCompilationResult() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.getCompilationResult(request);
        console.log(response);
      }
    
      callGetCompilationResult();
    
    

### getCompilationResult(request, options, callback)
    
    
    getCompilationResult(request: protos.google.cloud.dataform.v1beta1.IGetCompilationResultRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.ICompilationResult, protos.google.cloud.dataform.v1beta1.IGetCompilationResultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetcompilationresultrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresult), [protos.google.cloud.dataform.v1beta1.IGetCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetcompilationresultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCompilationResult(request, callback)
    
    
    getCompilationResult(request: protos.google.cloud.dataform.v1beta1.IGetCompilationResultRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.ICompilationResult, protos.google.cloud.dataform.v1beta1.IGetCompilationResultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetcompilationresultrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresult), [protos.google.cloud.dataform.v1beta1.IGetCompilationResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetcompilationresultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConfig(request, options)
    
    
    getConfig(request?: protos.google.cloud.dataform.v1beta1.IGetConfigRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IConfig,
            protos.google.cloud.dataform.v1beta1.IGetConfigRequest | undefined,
            {} | undefined
        ]>;

Get default config for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iconfig), [protos.google.cloud.dataform.v1beta1.IGetConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetconfigrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Config](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.config). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The config name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callGetConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.getConfig(request);
        console.log(response);
      }
    
      callGetConfig();
    
    

### getConfig(request, options, callback)
    
    
    getConfig(request: protos.google.cloud.dataform.v1beta1.IGetConfigRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IConfig, protos.google.cloud.dataform.v1beta1.IGetConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iconfig), [protos.google.cloud.dataform.v1beta1.IGetConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConfig(request, callback)
    
    
    getConfig(request: protos.google.cloud.dataform.v1beta1.IGetConfigRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IConfig, protos.google.cloud.dataform.v1beta1.IGetConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetconfigrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iconfig), [protos.google.cloud.dataform.v1beta1.IGetConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFolder(request, options)
    
    
    getFolder(request?: protos.google.cloud.dataform.v1beta1.IGetFolderRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IFolder,
            protos.google.cloud.dataform.v1beta1.IGetFolderRequest | undefined,
            {} | undefined
        ]>;

Fetches a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetfolderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifolder), [protos.google.cloud.dataform.v1beta1.IGetFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetfolderrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Folder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.folder). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Folder's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callGetFolder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.getFolder(request);
        console.log(response);
      }
    
      callGetFolder();
    
    

### getFolder(request, options, callback)
    
    
    getFolder(request: protos.google.cloud.dataform.v1beta1.IGetFolderRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IFolder, protos.google.cloud.dataform.v1beta1.IGetFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetfolderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifolder), [protos.google.cloud.dataform.v1beta1.IGetFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetfolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFolder(request, callback)
    
    
    getFolder(request: protos.google.cloud.dataform.v1beta1.IGetFolderRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IFolder, protos.google.cloud.dataform.v1beta1.IGetFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetfolderrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifolder), [protos.google.cloud.dataform.v1beta1.IGetFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetfolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, options)
    
    
    getIamPolicy(request?: protos.google.iam.v1.IGetIamPolicyRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1.IPolicy,
            protos.google.iam.v1.IGetIamPolicyRequest | undefined,
            {} | undefined
        ]>;

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.igetiampolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.igetiampolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  REQUIRED: The resource for which the policy is being requested.
       *  See the operation documentation for the appropriate value for this field.
       */
      // const resource = 'abc123'
      /**
       *  OPTIONAL: A `GetPolicyOptions` object for specifying options to
       *  `GetIamPolicy`.
       */
      // const options = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callGetIamPolicy() {
        // Construct request
        const request = {
          resource,
        };
    
        // Run request
        const response = await dataformClient.getIamPolicy(request);
        console.log(response);
      }
    
      callGetIamPolicy();
    
    

### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: protos.google.iam.v1.IGetIamPolicyRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.IGetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.igetiampolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.igetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, callback)
    
    
    getIamPolicy(request: protos.google.iam.v1.IGetIamPolicyRequest, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.IGetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.igetiampolicyrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.igetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.operation)]>` |   
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
  
### getReleaseConfig(request, options)
    
    
    getReleaseConfig(request?: protos.google.cloud.dataform.v1beta1.IGetReleaseConfigRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IReleaseConfig,
            protos.google.cloud.dataform.v1beta1.IGetReleaseConfigRequest | undefined,
            {} | undefined
        ]>;

Fetches a single ReleaseConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetreleaseconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig), [protos.google.cloud.dataform.v1beta1.IGetReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetreleaseconfigrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The release config's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callGetReleaseConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.getReleaseConfig(request);
        console.log(response);
      }
    
      callGetReleaseConfig();
    
    

### getReleaseConfig(request, options, callback)
    
    
    getReleaseConfig(request: protos.google.cloud.dataform.v1beta1.IGetReleaseConfigRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IReleaseConfig, protos.google.cloud.dataform.v1beta1.IGetReleaseConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetreleaseconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig), [protos.google.cloud.dataform.v1beta1.IGetReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetreleaseconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getReleaseConfig(request, callback)
    
    
    getReleaseConfig(request: protos.google.cloud.dataform.v1beta1.IGetReleaseConfigRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IReleaseConfig, protos.google.cloud.dataform.v1beta1.IGetReleaseConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetreleaseconfigrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig), [protos.google.cloud.dataform.v1beta1.IGetReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetreleaseconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRepository(request, options)
    
    
    getRepository(request?: protos.google.cloud.dataform.v1beta1.IGetRepositoryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IRepository,
            protos.google.cloud.dataform.v1beta1.IGetRepositoryRequest | undefined,
            {} | undefined
        ]>;

Fetches a single Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetrepositoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository), [protos.google.cloud.dataform.v1beta1.IGetRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetrepositoryrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callGetRepository() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.getRepository(request);
        console.log(response);
      }
    
      callGetRepository();
    
    

### getRepository(request, options, callback)
    
    
    getRepository(request: protos.google.cloud.dataform.v1beta1.IGetRepositoryRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IRepository, protos.google.cloud.dataform.v1beta1.IGetRepositoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetrepositoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository), [protos.google.cloud.dataform.v1beta1.IGetRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetrepositoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRepository(request, callback)
    
    
    getRepository(request: protos.google.cloud.dataform.v1beta1.IGetRepositoryRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IRepository, protos.google.cloud.dataform.v1beta1.IGetRepositoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetrepositoryrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository), [protos.google.cloud.dataform.v1beta1.IGetRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetrepositoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTeamFolder(request, options)
    
    
    getTeamFolder(request?: protos.google.cloud.dataform.v1beta1.IGetTeamFolderRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ITeamFolder,
            protos.google.cloud.dataform.v1beta1.IGetTeamFolderRequest | undefined,
            {} | undefined
        ]>;

Fetches a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetteamfolderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ITeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iteamfolder), [protos.google.cloud.dataform.v1beta1.IGetTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetteamfolderrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.teamfolder). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The TeamFolder's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callGetTeamFolder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.getTeamFolder(request);
        console.log(response);
      }
    
      callGetTeamFolder();
    
    

### getTeamFolder(request, options, callback)
    
    
    getTeamFolder(request: protos.google.cloud.dataform.v1beta1.IGetTeamFolderRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.ITeamFolder, protos.google.cloud.dataform.v1beta1.IGetTeamFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetteamfolderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ITeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iteamfolder), [protos.google.cloud.dataform.v1beta1.IGetTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetteamfolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTeamFolder(request, callback)
    
    
    getTeamFolder(request: protos.google.cloud.dataform.v1beta1.IGetTeamFolderRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.ITeamFolder, protos.google.cloud.dataform.v1beta1.IGetTeamFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetteamfolderrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ITeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iteamfolder), [protos.google.cloud.dataform.v1beta1.IGetTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetteamfolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkflowConfig(request, options)
    
    
    getWorkflowConfig(request?: protos.google.cloud.dataform.v1beta1.IGetWorkflowConfigRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkflowConfig,
            (protos.google.cloud.dataform.v1beta1.IGetWorkflowConfigRequest | undefined),
            {} | undefined
        ]>;

Fetches a single WorkflowConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig), ([protos.google.cloud.dataform.v1beta1.IGetWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workflow config's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callGetWorkflowConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.getWorkflowConfig(request);
        console.log(response);
      }
    
      callGetWorkflowConfig();
    
    

### getWorkflowConfig(request, options, callback)
    
    
    getWorkflowConfig(request: protos.google.cloud.dataform.v1beta1.IGetWorkflowConfigRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkflowConfig, protos.google.cloud.dataform.v1beta1.IGetWorkflowConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig), [protos.google.cloud.dataform.v1beta1.IGetWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkflowConfig(request, callback)
    
    
    getWorkflowConfig(request: protos.google.cloud.dataform.v1beta1.IGetWorkflowConfigRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkflowConfig, protos.google.cloud.dataform.v1beta1.IGetWorkflowConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowconfigrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig), [protos.google.cloud.dataform.v1beta1.IGetWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkflowInvocation(request, options)
    
    
    getWorkflowInvocation(request?: protos.google.cloud.dataform.v1beta1.IGetWorkflowInvocationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkflowInvocation,
            (protos.google.cloud.dataform.v1beta1.IGetWorkflowInvocationRequest | undefined),
            {} | undefined
        ]>;

Fetches a single WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowinvocationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocation), ([protos.google.cloud.dataform.v1beta1.IGetWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowinvocationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workflow invocation resource's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callGetWorkflowInvocation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.getWorkflowInvocation(request);
        console.log(response);
      }
    
      callGetWorkflowInvocation();
    
    

### getWorkflowInvocation(request, options, callback)
    
    
    getWorkflowInvocation(request: protos.google.cloud.dataform.v1beta1.IGetWorkflowInvocationRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkflowInvocation, protos.google.cloud.dataform.v1beta1.IGetWorkflowInvocationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowinvocationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocation), [protos.google.cloud.dataform.v1beta1.IGetWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowinvocationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkflowInvocation(request, callback)
    
    
    getWorkflowInvocation(request: protos.google.cloud.dataform.v1beta1.IGetWorkflowInvocationRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkflowInvocation, protos.google.cloud.dataform.v1beta1.IGetWorkflowInvocationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowinvocationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocation), [protos.google.cloud.dataform.v1beta1.IGetWorkflowInvocationRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkflowinvocationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkspace(request, options)
    
    
    getWorkspace(request?: protos.google.cloud.dataform.v1beta1.IGetWorkspaceRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkspace,
            protos.google.cloud.dataform.v1beta1.IGetWorkspaceRequest | undefined,
            {} | undefined
        ]>;

Fetches a single Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkspacerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkspace), [protos.google.cloud.dataform.v1beta1.IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkspacerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Workspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.workspace). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const name = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callGetWorkspace() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.getWorkspace(request);
        console.log(response);
      }
    
      callGetWorkspace();
    
    

### getWorkspace(request, options, callback)
    
    
    getWorkspace(request: protos.google.cloud.dataform.v1beta1.IGetWorkspaceRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkspace, protos.google.cloud.dataform.v1beta1.IGetWorkspaceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkspacerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkspace), [protos.google.cloud.dataform.v1beta1.IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkspacerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkspace(request, callback)
    
    
    getWorkspace(request: protos.google.cloud.dataform.v1beta1.IGetWorkspaceRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkspace, protos.google.cloud.dataform.v1beta1.IGetWorkspaceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkspacerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkspace), [protos.google.cloud.dataform.v1beta1.IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.igetworkspacerequest) | null | undefined, {} | null | undefined>`   
  
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
  
### installNpmPackages(request, options)
    
    
    installNpmPackages(request?: protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesResponse,
            (protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesRequest | undefined),
            {} | undefined
        ]>;

Installs dependency NPM packages (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInstallNpmPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iinstallnpmpackagesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iinstallnpmpackagesresponse), ([protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iinstallnpmpackagesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [InstallNpmPackagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.installnpmpackagesresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Optional. The pipeline options which defines the pipeline type and path
       *  within the Git repository.
       */
      // const pipelineConfig = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callInstallNpmPackages() {
        // Construct request
        const request = {
          workspace,
        };
    
        // Run request
        const response = await dataformClient.installNpmPackages(request);
        console.log(response);
      }
    
      callInstallNpmPackages();
    
    

### installNpmPackages(request, options, callback)
    
    
    installNpmPackages(request: protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesResponse, protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInstallNpmPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iinstallnpmpackagesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iinstallnpmpackagesresponse), [protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iinstallnpmpackagesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### installNpmPackages(request, callback)
    
    
    installNpmPackages(request: protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesResponse, protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInstallNpmPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iinstallnpmpackagesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iinstallnpmpackagesresponse), [protos.google.cloud.dataform.v1beta1.IInstallNpmPackagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iinstallnpmpackagesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCompilationResults(request, options)
    
    
    listCompilationResults(request?: protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ICompilationResult[],
            protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest | null,
            protos.google.cloud.dataform.v1beta1.IListCompilationResultsResponse
        ]>;

Lists CompilationResults in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCompilationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresult)[], [protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsrequest) | null, [protos.google.cloud.dataform.v1beta1.IListCompilationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listCompilationResultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listCompilationResults(request, options, callback)
    
    
    listCompilationResults(request: protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest, protos.google.cloud.dataform.v1beta1.IListCompilationResultsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.ICompilationResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCompilationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsrequest), [protos.google.cloud.dataform.v1beta1.IListCompilationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCompilationResults(request, callback)
    
    
    listCompilationResults(request: protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest, protos.google.cloud.dataform.v1beta1.IListCompilationResultsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.ICompilationResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCompilationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsrequest), [protos.google.cloud.dataform.v1beta1.IListCompilationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCompilationResultsAsync(request, options)
    
    
    listCompilationResultsAsync(request?: protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.ICompilationResult>;

Equivalent to `listCompilationResults`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCompilationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresult)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository in which to list compilation results. Must be in
       *  the format `projects/* /locations/* /repositories/*`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum number of compilation results to return. The server may
       *  return fewer items than requested. If unspecified, the server will pick an
       *  appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `ListCompilationResults`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListCompilationResults`,
       *  with the exception of `page_size`, must match the call that provided the
       *  page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. This field only supports ordering by `name` and `create_time`.
       *  If unspecified, the server will choose the ordering.
       *  If specified, the default order is ascending for the `name` field.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Filter for the returned list.
       */
      // const filter = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callListCompilationResults() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = dataformClient.listCompilationResultsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListCompilationResults();
    
    

### listCompilationResultsStream(request, options)
    
    
    listCompilationResultsStream(request?: protos.google.cloud.dataform.v1beta1.IListCompilationResultsRequest, options?: CallOptions): Transform;

Equivalent to `listCompilationResults`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCompilationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistcompilationresultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listCompilationResultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listReleaseConfigs(request, options)
    
    
    listReleaseConfigs(request?: protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IReleaseConfig[],
            protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest | null,
            protos.google.cloud.dataform.v1beta1.IListReleaseConfigsResponse
        ]>;

Lists ReleaseConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleaseConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig)[], [protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsrequest) | null, [protos.google.cloud.dataform.v1beta1.IListReleaseConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listReleaseConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listReleaseConfigs(request, options, callback)
    
    
    listReleaseConfigs(request: protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest, protos.google.cloud.dataform.v1beta1.IListReleaseConfigsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IReleaseConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleaseConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsrequest), [protos.google.cloud.dataform.v1beta1.IListReleaseConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReleaseConfigs(request, callback)
    
    
    listReleaseConfigs(request: protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest, protos.google.cloud.dataform.v1beta1.IListReleaseConfigsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IReleaseConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleaseConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsrequest), [protos.google.cloud.dataform.v1beta1.IListReleaseConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReleaseConfigsAsync(request, options)
    
    
    listReleaseConfigsAsync(request?: protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.IReleaseConfig>;

Equivalent to `listReleaseConfigs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleaseConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository in which to list release configs. Must be in the
       *  format `projects/* /locations/* /repositories/*`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum number of release configs to return. The server may
       *  return fewer items than requested. If unspecified, the server will pick an
       *  appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `ListReleaseConfigs` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListReleaseConfigs`,
       *  with the exception of `page_size`, must match the call that provided the
       *  page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callListReleaseConfigs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = dataformClient.listReleaseConfigsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListReleaseConfigs();
    
    

### listReleaseConfigsStream(request, options)
    
    
    listReleaseConfigsStream(request?: protos.google.cloud.dataform.v1beta1.IListReleaseConfigsRequest, options?: CallOptions): Transform;

Equivalent to `listReleaseConfigs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleaseConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistreleaseconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listReleaseConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listRepositories(request, options)
    
    
    listRepositories(request?: protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IRepository[],
            protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest | null,
            protos.google.cloud.dataform.v1beta1.IListRepositoriesResponse
        ]>;

Lists Repositories in a given project and location.

**Note:** *This method can return repositories not shown in the [Dataform UI](https://console.cloud.google.com/bigquery/dataform)*.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRepositoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository)[], [protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesrequest) | null, [protos.google.cloud.dataform.v1beta1.IListRepositoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listRepositoriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listRepositories(request, options, callback)
    
    
    listRepositories(request: protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest, protos.google.cloud.dataform.v1beta1.IListRepositoriesResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IRepository>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRepositoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesrequest), [protos.google.cloud.dataform.v1beta1.IListRepositoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRepositories(request, callback)
    
    
    listRepositories(request: protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest, protos.google.cloud.dataform.v1beta1.IListRepositoriesResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IRepository>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRepositoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesrequest), [protos.google.cloud.dataform.v1beta1.IListRepositoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRepositoriesAsync(request, options)
    
    
    listRepositoriesAsync(request?: protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.IRepository>;

Equivalent to `listRepositories`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRepositoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The location in which to list repositories. Must be in the format
       *  `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum number of repositories to return. The server may return
       *  fewer items than requested. If unspecified, the server will pick an
       *  appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `ListRepositories` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListRepositories`,
       *  with the exception of `page_size`, must match the call that provided the
       *  page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. This field only supports ordering by `name`. If unspecified, the
       *  server will choose the ordering. If specified, the default order is
       *  ascending for the `name` field.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Filter for the returned list.
       */
      // const filter = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callListRepositories() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = dataformClient.listRepositoriesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListRepositories();
    
    

### listRepositoriesStream(request, options)
    
    
    listRepositoriesStream(request?: protos.google.cloud.dataform.v1beta1.IListRepositoriesRequest, options?: CallOptions): Transform;

Equivalent to `listRepositories`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRepositoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistrepositoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listRepositoriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkflowConfigs(request, options)
    
    
    listWorkflowConfigs(request?: protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkflowConfig[],
            protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest | null,
            protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsResponse
        ]>;

Lists WorkflowConfigs in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig)[], [protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsrequest) | null, [protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listWorkflowConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkflowConfigs(request, options, callback)
    
    
    listWorkflowConfigs(request: protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest, protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IWorkflowConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsrequest), [protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkflowConfigs(request, callback)
    
    
    listWorkflowConfigs(request: protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest, protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IWorkflowConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsrequest), [protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkflowConfigsAsync(request, options)
    
    
    listWorkflowConfigsAsync(request?: protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.IWorkflowConfig>;

Equivalent to `listWorkflowConfigs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository in which to list workflow configs. Must be in the
       *  format `projects/* /locations/* /repositories/*`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum number of workflow configs to return. The server may
       *  return fewer items than requested. If unspecified, the server will pick an
       *  appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `ListWorkflowConfigs` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListWorkflowConfigs`,
       *  with the exception of `page_size`, must match the call that provided the
       *  page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callListWorkflowConfigs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = dataformClient.listWorkflowConfigsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListWorkflowConfigs();
    
    

### listWorkflowConfigsStream(request, options)
    
    
    listWorkflowConfigsStream(request?: protos.google.cloud.dataform.v1beta1.IListWorkflowConfigsRequest, options?: CallOptions): Transform;

Equivalent to `listWorkflowConfigs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listWorkflowConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkflowInvocations(request, options)
    
    
    listWorkflowInvocations(request?: protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkflowInvocation[],
            protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest | null,
            protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsResponse
        ]>;

Lists WorkflowInvocations in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowInvocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocation)[], [protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsrequest) | null, [protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listWorkflowInvocationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkflowInvocations(request, options, callback)
    
    
    listWorkflowInvocations(request: protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest, protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IWorkflowInvocation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowInvocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsrequest), [protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IWorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkflowInvocations(request, callback)
    
    
    listWorkflowInvocations(request: protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest, protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IWorkflowInvocation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowInvocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsrequest), [protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IWorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkflowInvocationsAsync(request, options)
    
    
    listWorkflowInvocationsAsync(request?: protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.IWorkflowInvocation>;

Equivalent to `listWorkflowInvocations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowInvocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.IWorkflowInvocation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource of the WorkflowInvocation type. Must be in
       *  the format `projects/* /locations/* /repositories/*`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum number of workflow invocations to return. The server may
       *  return fewer items than requested. If unspecified, the server will pick an
       *  appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `ListWorkflowInvocations`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `ListWorkflowInvocations`, with the exception of `page_size`, must match
       *  the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. This field only supports ordering by `name`. If unspecified, the
       *  server will choose the ordering. If specified, the default order is
       *  ascending for the `name` field.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Filter for the returned list.
       */
      // const filter = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callListWorkflowInvocations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = dataformClient.listWorkflowInvocationsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListWorkflowInvocations();
    
    

### listWorkflowInvocationsStream(request, options)
    
    
    listWorkflowInvocationsStream(request?: protos.google.cloud.dataform.v1beta1.IListWorkflowInvocationsRequest, options?: CallOptions): Transform;

Equivalent to `listWorkflowInvocations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkflowInvocationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkflowinvocationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listWorkflowInvocationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkspaces(request, options)
    
    
    listWorkspaces(request?: protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkspace[],
            protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest | null,
            protos.google.cloud.dataform.v1beta1.IListWorkspacesResponse
        ]>;

Lists Workspaces in a given Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkspace)[], [protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesrequest) | null, [protos.google.cloud.dataform.v1beta1.IListWorkspacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Workspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.workspace). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listWorkspacesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkspaces(request, options, callback)
    
    
    listWorkspaces(request: protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest, protos.google.cloud.dataform.v1beta1.IListWorkspacesResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IWorkspace>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesrequest), [protos.google.cloud.dataform.v1beta1.IListWorkspacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkspace)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkspaces(request, callback)
    
    
    listWorkspaces(request: protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest, protos.google.cloud.dataform.v1beta1.IListWorkspacesResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IWorkspace>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesrequest), [protos.google.cloud.dataform.v1beta1.IListWorkspacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkspace)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkspacesAsync(request, options)
    
    
    listWorkspacesAsync(request?: protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.IWorkspace>;

Equivalent to `listWorkspaces`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkspace)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Workspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.workspace). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository in which to list workspaces. Must be in the
       *  format `projects/* /locations/* /repositories/*`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum number of workspaces to return. The server may return
       *  fewer items than requested. If unspecified, the server will pick an
       *  appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `ListWorkspaces` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListWorkspaces`, with
       *  the exception of `page_size`, must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. This field only supports ordering by `name`. If unspecified, the
       *  server will choose the ordering. If specified, the default order is
       *  ascending for the `name` field.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Filter for the returned list.
       */
      // const filter = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callListWorkspaces() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = dataformClient.listWorkspacesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListWorkspaces();
    
    

### listWorkspacesStream(request, options)
    
    
    listWorkspacesStream(request?: protos.google.cloud.dataform.v1beta1.IListWorkspacesRequest, options?: CallOptions): Transform;

Equivalent to `listWorkspaces`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ilistworkspacesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Workspace](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.workspace) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listWorkspacesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### makeDirectory(request, options)
    
    
    makeDirectory(request?: protos.google.cloud.dataform.v1beta1.IMakeDirectoryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IMakeDirectoryResponse,
            protos.google.cloud.dataform.v1beta1.IMakeDirectoryRequest | undefined,
            {} | undefined
        ]>;

Creates a directory inside a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMakeDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imakedirectoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IMakeDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imakedirectoryresponse), [protos.google.cloud.dataform.v1beta1.IMakeDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imakedirectoryrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MakeDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.makedirectoryresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Required. The directory's full path including directory name, relative to
       *  the workspace root.
       */
      // const path = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callMakeDirectory() {
        // Construct request
        const request = {
          workspace,
          path,
        };
    
        // Run request
        const response = await dataformClient.makeDirectory(request);
        console.log(response);
      }
    
      callMakeDirectory();
    
    

### makeDirectory(request, options, callback)
    
    
    makeDirectory(request: protos.google.cloud.dataform.v1beta1.IMakeDirectoryRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IMakeDirectoryResponse, protos.google.cloud.dataform.v1beta1.IMakeDirectoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMakeDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imakedirectoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IMakeDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imakedirectoryresponse), [protos.google.cloud.dataform.v1beta1.IMakeDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imakedirectoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### makeDirectory(request, callback)
    
    
    makeDirectory(request: protos.google.cloud.dataform.v1beta1.IMakeDirectoryRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IMakeDirectoryResponse, protos.google.cloud.dataform.v1beta1.IMakeDirectoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMakeDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imakedirectoryrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IMakeDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imakedirectoryresponse), [protos.google.cloud.dataform.v1beta1.IMakeDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imakedirectoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### matchCompilationResultFromCompilationResultName(compilationResultName)
    
    
    matchCompilationResultFromCompilationResultName(compilationResultName: string): string | number;

Parse the compilation_result from CompilationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`compilationResultName` |  `string`   
A fully-qualified path representing CompilationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the compilation_result.  
  
### matchCryptoKeyFromCryptoKeyName(cryptoKeyName)
    
    
    matchCryptoKeyFromCryptoKeyName(cryptoKeyName: string): string | number;

Parse the crypto_key from CryptoKey resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyName` |  `string`   
A fully-qualified path representing CryptoKey resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the crypto_key.  
  
### matchCryptoKeyFromCryptoKeyVersionName(cryptoKeyVersionName)
    
    
    matchCryptoKeyFromCryptoKeyVersionName(cryptoKeyVersionName: string): string | number;

Parse the crypto_key from CryptoKeyVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyVersionName` |  `string`   
A fully-qualified path representing CryptoKeyVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the crypto_key.  
  
### matchCryptoKeyVersionFromCryptoKeyVersionName(cryptoKeyVersionName)
    
    
    matchCryptoKeyVersionFromCryptoKeyVersionName(cryptoKeyVersionName: string): string | number;

Parse the crypto_key_version from CryptoKeyVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyVersionName` |  `string`   
A fully-qualified path representing CryptoKeyVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the crypto_key_version.  
  
### matchFolderFromFolderName(folderName)
    
    
    matchFolderFromFolderName(folderName: string): string | number;

Parse the folder from Folder resource.

**Parameter**  
---  
**Name** | **Description**  
`folderName` |  `string`   
A fully-qualified path representing Folder resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the folder.  
  
### matchKeyRingFromCryptoKeyName(cryptoKeyName)
    
    
    matchKeyRingFromCryptoKeyName(cryptoKeyName: string): string | number;

Parse the key_ring from CryptoKey resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyName` |  `string`   
A fully-qualified path representing CryptoKey resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the key_ring.  
  
### matchKeyRingFromCryptoKeyVersionName(cryptoKeyVersionName)
    
    
    matchKeyRingFromCryptoKeyVersionName(cryptoKeyVersionName: string): string | number;

Parse the key_ring from CryptoKeyVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyVersionName` |  `string`   
A fully-qualified path representing CryptoKeyVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the key_ring.  
  
### matchLocationFromCompilationResultName(compilationResultName)
    
    
    matchLocationFromCompilationResultName(compilationResultName: string): string | number;

Parse the location from CompilationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`compilationResultName` |  `string`   
A fully-qualified path representing CompilationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromConfigName(configName)
    
    
    matchLocationFromConfigName(configName: string): string | number;

Parse the location from Config resource.

**Parameter**  
---  
**Name** | **Description**  
`configName` |  `string`   
A fully-qualified path representing Config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCryptoKeyName(cryptoKeyName)
    
    
    matchLocationFromCryptoKeyName(cryptoKeyName: string): string | number;

Parse the location from CryptoKey resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyName` |  `string`   
A fully-qualified path representing CryptoKey resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCryptoKeyVersionName(cryptoKeyVersionName)
    
    
    matchLocationFromCryptoKeyVersionName(cryptoKeyVersionName: string): string | number;

Parse the location from CryptoKeyVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyVersionName` |  `string`   
A fully-qualified path representing CryptoKeyVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromFolderName(folderName)
    
    
    matchLocationFromFolderName(folderName: string): string | number;

Parse the location from Folder resource.

**Parameter**  
---  
**Name** | **Description**  
`folderName` |  `string`   
A fully-qualified path representing Folder resource.  
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
  
### matchLocationFromReleaseConfigName(releaseConfigName)
    
    
    matchLocationFromReleaseConfigName(releaseConfigName: string): string | number;

Parse the location from ReleaseConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`releaseConfigName` |  `string`   
A fully-qualified path representing ReleaseConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRepositoryName(repositoryName)
    
    
    matchLocationFromRepositoryName(repositoryName: string): string | number;

Parse the location from Repository resource.

**Parameter**  
---  
**Name** | **Description**  
`repositoryName` |  `string`   
A fully-qualified path representing Repository resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTeamFolderName(teamFolderName)
    
    
    matchLocationFromTeamFolderName(teamFolderName: string): string | number;

Parse the location from TeamFolder resource.

**Parameter**  
---  
**Name** | **Description**  
`teamFolderName` |  `string`   
A fully-qualified path representing TeamFolder resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromWorkflowConfigName(workflowConfigName)
    
    
    matchLocationFromWorkflowConfigName(workflowConfigName: string): string | number;

Parse the location from WorkflowConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`workflowConfigName` |  `string`   
A fully-qualified path representing WorkflowConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromWorkflowInvocationName(workflowInvocationName)
    
    
    matchLocationFromWorkflowInvocationName(workflowInvocationName: string): string | number;

Parse the location from WorkflowInvocation resource.

**Parameter**  
---  
**Name** | **Description**  
`workflowInvocationName` |  `string`   
A fully-qualified path representing WorkflowInvocation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromWorkspaceName(workspaceName)
    
    
    matchLocationFromWorkspaceName(workspaceName: string): string | number;

Parse the location from Workspace resource.

**Parameter**  
---  
**Name** | **Description**  
`workspaceName` |  `string`   
A fully-qualified path representing Workspace resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
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
  
### matchProjectFromCompilationResultName(compilationResultName)
    
    
    matchProjectFromCompilationResultName(compilationResultName: string): string | number;

Parse the project from CompilationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`compilationResultName` |  `string`   
A fully-qualified path representing CompilationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromConfigName(configName)
    
    
    matchProjectFromConfigName(configName: string): string | number;

Parse the project from Config resource.

**Parameter**  
---  
**Name** | **Description**  
`configName` |  `string`   
A fully-qualified path representing Config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCryptoKeyName(cryptoKeyName)
    
    
    matchProjectFromCryptoKeyName(cryptoKeyName: string): string | number;

Parse the project from CryptoKey resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyName` |  `string`   
A fully-qualified path representing CryptoKey resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCryptoKeyVersionName(cryptoKeyVersionName)
    
    
    matchProjectFromCryptoKeyVersionName(cryptoKeyVersionName: string): string | number;

Parse the project from CryptoKeyVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`cryptoKeyVersionName` |  `string`   
A fully-qualified path representing CryptoKeyVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromFolderName(folderName)
    
    
    matchProjectFromFolderName(folderName: string): string | number;

Parse the project from Folder resource.

**Parameter**  
---  
**Name** | **Description**  
`folderName` |  `string`   
A fully-qualified path representing Folder resource.  
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
  
### matchProjectFromReleaseConfigName(releaseConfigName)
    
    
    matchProjectFromReleaseConfigName(releaseConfigName: string): string | number;

Parse the project from ReleaseConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`releaseConfigName` |  `string`   
A fully-qualified path representing ReleaseConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRepositoryName(repositoryName)
    
    
    matchProjectFromRepositoryName(repositoryName: string): string | number;

Parse the project from Repository resource.

**Parameter**  
---  
**Name** | **Description**  
`repositoryName` |  `string`   
A fully-qualified path representing Repository resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSecretVersionName(secretVersionName)
    
    
    matchProjectFromSecretVersionName(secretVersionName: string): string | number;

Parse the project from SecretVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`secretVersionName` |  `string`   
A fully-qualified path representing SecretVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTeamFolderName(teamFolderName)
    
    
    matchProjectFromTeamFolderName(teamFolderName: string): string | number;

Parse the project from TeamFolder resource.

**Parameter**  
---  
**Name** | **Description**  
`teamFolderName` |  `string`   
A fully-qualified path representing TeamFolder resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromWorkflowConfigName(workflowConfigName)
    
    
    matchProjectFromWorkflowConfigName(workflowConfigName: string): string | number;

Parse the project from WorkflowConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`workflowConfigName` |  `string`   
A fully-qualified path representing WorkflowConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromWorkflowInvocationName(workflowInvocationName)
    
    
    matchProjectFromWorkflowInvocationName(workflowInvocationName: string): string | number;

Parse the project from WorkflowInvocation resource.

**Parameter**  
---  
**Name** | **Description**  
`workflowInvocationName` |  `string`   
A fully-qualified path representing WorkflowInvocation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromWorkspaceName(workspaceName)
    
    
    matchProjectFromWorkspaceName(workspaceName: string): string | number;

Parse the project from Workspace resource.

**Parameter**  
---  
**Name** | **Description**  
`workspaceName` |  `string`   
A fully-qualified path representing Workspace resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchReleaseConfigFromReleaseConfigName(releaseConfigName)
    
    
    matchReleaseConfigFromReleaseConfigName(releaseConfigName: string): string | number;

Parse the release_config from ReleaseConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`releaseConfigName` |  `string`   
A fully-qualified path representing ReleaseConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the release_config.  
  
### matchRepositoryFromCompilationResultName(compilationResultName)
    
    
    matchRepositoryFromCompilationResultName(compilationResultName: string): string | number;

Parse the repository from CompilationResult resource.

**Parameter**  
---  
**Name** | **Description**  
`compilationResultName` |  `string`   
A fully-qualified path representing CompilationResult resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the repository.  
  
### matchRepositoryFromReleaseConfigName(releaseConfigName)
    
    
    matchRepositoryFromReleaseConfigName(releaseConfigName: string): string | number;

Parse the repository from ReleaseConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`releaseConfigName` |  `string`   
A fully-qualified path representing ReleaseConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the repository.  
  
### matchRepositoryFromRepositoryName(repositoryName)
    
    
    matchRepositoryFromRepositoryName(repositoryName: string): string | number;

Parse the repository from Repository resource.

**Parameter**  
---  
**Name** | **Description**  
`repositoryName` |  `string`   
A fully-qualified path representing Repository resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the repository.  
  
### matchRepositoryFromWorkflowConfigName(workflowConfigName)
    
    
    matchRepositoryFromWorkflowConfigName(workflowConfigName: string): string | number;

Parse the repository from WorkflowConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`workflowConfigName` |  `string`   
A fully-qualified path representing WorkflowConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the repository.  
  
### matchRepositoryFromWorkflowInvocationName(workflowInvocationName)
    
    
    matchRepositoryFromWorkflowInvocationName(workflowInvocationName: string): string | number;

Parse the repository from WorkflowInvocation resource.

**Parameter**  
---  
**Name** | **Description**  
`workflowInvocationName` |  `string`   
A fully-qualified path representing WorkflowInvocation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the repository.  
  
### matchRepositoryFromWorkspaceName(workspaceName)
    
    
    matchRepositoryFromWorkspaceName(workspaceName: string): string | number;

Parse the repository from Workspace resource.

**Parameter**  
---  
**Name** | **Description**  
`workspaceName` |  `string`   
A fully-qualified path representing Workspace resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the repository.  
  
### matchSecretFromSecretVersionName(secretVersionName)
    
    
    matchSecretFromSecretVersionName(secretVersionName: string): string | number;

Parse the secret from SecretVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`secretVersionName` |  `string`   
A fully-qualified path representing SecretVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the secret.  
  
### matchTeamFolderFromTeamFolderName(teamFolderName)
    
    
    matchTeamFolderFromTeamFolderName(teamFolderName: string): string | number;

Parse the team_folder from TeamFolder resource.

**Parameter**  
---  
**Name** | **Description**  
`teamFolderName` |  `string`   
A fully-qualified path representing TeamFolder resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the team_folder.  
  
### matchVersionFromSecretVersionName(secretVersionName)
    
    
    matchVersionFromSecretVersionName(secretVersionName: string): string | number;

Parse the version from SecretVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`secretVersionName` |  `string`   
A fully-qualified path representing SecretVersion resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the version.  
  
### matchWorkflowConfigFromWorkflowConfigName(workflowConfigName)
    
    
    matchWorkflowConfigFromWorkflowConfigName(workflowConfigName: string): string | number;

Parse the workflow_config from WorkflowConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`workflowConfigName` |  `string`   
A fully-qualified path representing WorkflowConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the workflow_config.  
  
### matchWorkflowInvocationFromWorkflowInvocationName(workflowInvocationName)
    
    
    matchWorkflowInvocationFromWorkflowInvocationName(workflowInvocationName: string): string | number;

Parse the workflow_invocation from WorkflowInvocation resource.

**Parameter**  
---  
**Name** | **Description**  
`workflowInvocationName` |  `string`   
A fully-qualified path representing WorkflowInvocation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the workflow_invocation.  
  
### matchWorkspaceFromWorkspaceName(workspaceName)
    
    
    matchWorkspaceFromWorkspaceName(workspaceName: string): string | number;

Parse the workspace from Workspace resource.

**Parameter**  
---  
**Name** | **Description**  
`workspaceName` |  `string`   
A fully-qualified path representing Workspace resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the workspace.  
  
### moveDirectory(request, options)
    
    
    moveDirectory(request?: protos.google.cloud.dataform.v1beta1.IMoveDirectoryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IMoveDirectoryResponse,
            protos.google.cloud.dataform.v1beta1.IMoveDirectoryRequest | undefined,
            {} | undefined
        ]>;

Moves a directory (inside a Workspace), and all of its contents, to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovedirectoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IMoveDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovedirectoryresponse), [protos.google.cloud.dataform.v1beta1.IMoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovedirectoryrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MoveDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.movedirectoryresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Required. The directory's full path including directory name, relative to
       *  the workspace root.
       */
      // const path = 'abc123'
      /**
       *  Required. The new path for the directory including directory name, rooted
       *  at workspace root.
       */
      // const newPath = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callMoveDirectory() {
        // Construct request
        const request = {
          workspace,
          path,
          newPath,
        };
    
        // Run request
        const response = await dataformClient.moveDirectory(request);
        console.log(response);
      }
    
      callMoveDirectory();
    
    

### moveDirectory(request, options, callback)
    
    
    moveDirectory(request: protos.google.cloud.dataform.v1beta1.IMoveDirectoryRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IMoveDirectoryResponse, protos.google.cloud.dataform.v1beta1.IMoveDirectoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovedirectoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IMoveDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovedirectoryresponse), [protos.google.cloud.dataform.v1beta1.IMoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovedirectoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveDirectory(request, callback)
    
    
    moveDirectory(request: protos.google.cloud.dataform.v1beta1.IMoveDirectoryRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IMoveDirectoryResponse, protos.google.cloud.dataform.v1beta1.IMoveDirectoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovedirectoryrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IMoveDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovedirectoryresponse), [protos.google.cloud.dataform.v1beta1.IMoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovedirectoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveFile(request, options)
    
    
    moveFile(request?: protos.google.cloud.dataform.v1beta1.IMoveFileRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IMoveFileResponse,
            protos.google.cloud.dataform.v1beta1.IMoveFileRequest | undefined,
            {} | undefined
        ]>;

Moves a file (inside a Workspace) to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefilerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IMoveFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefileresponse), [protos.google.cloud.dataform.v1beta1.IMoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefilerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MoveFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.movefileresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Required. The file's full path including filename, relative to the
       *  workspace root.
       */
      // const path = 'abc123'
      /**
       *  Required. The file's new path including filename, relative to the workspace
       *  root.
       */
      // const newPath = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callMoveFile() {
        // Construct request
        const request = {
          workspace,
          path,
          newPath,
        };
    
        // Run request
        const response = await dataformClient.moveFile(request);
        console.log(response);
      }
    
      callMoveFile();
    
    

### moveFile(request, options, callback)
    
    
    moveFile(request: protos.google.cloud.dataform.v1beta1.IMoveFileRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IMoveFileResponse, protos.google.cloud.dataform.v1beta1.IMoveFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefilerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IMoveFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefileresponse), [protos.google.cloud.dataform.v1beta1.IMoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveFile(request, callback)
    
    
    moveFile(request: protos.google.cloud.dataform.v1beta1.IMoveFileRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IMoveFileResponse, protos.google.cloud.dataform.v1beta1.IMoveFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefilerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IMoveFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefileresponse), [protos.google.cloud.dataform.v1beta1.IMoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveFolder(request, options)
    
    
    moveFolder(request?: protos.google.cloud.dataform.v1beta1.IMoveFolderRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IMoveFolderMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Moves a Folder to a new Folder, TeamFolder, or the root location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefolderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IMoveFolderMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefoldermetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The full resource name of the Folder to move.
       */
      // const name = 'abc123'
      /**
       *  Optional. The name of the Folder, TeamFolder, or root location to move the
       *  Folder to. Can be in the format of: "" to move into the root User folder,
       *  `projects/* /locations/* /folders/*`, `projects/* /locations/* /teamFolders/*`
       */
      // const destinationContainingFolder = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callMoveFolder() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataformClient.moveFolder(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callMoveFolder();
    
    

### moveFolder(request, options, callback)
    
    
    moveFolder(request: protos.google.cloud.dataform.v1beta1.IMoveFolderRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IMoveFolderMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefolderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IMoveFolderMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefoldermetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveFolder(request, callback)
    
    
    moveFolder(request: protos.google.cloud.dataform.v1beta1.IMoveFolderRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IMoveFolderMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefolderrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IMoveFolderMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imovefoldermetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveRepository(request, options)
    
    
    moveRepository(request?: protos.google.cloud.dataform.v1beta1.IMoveRepositoryRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IMoveRepositoryMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Moves a Repository to a new location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imoverepositoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IMoveRepositoryMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imoverepositorymetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The full resource name of the repository to move.
       */
      // const name = 'abc123'
      /**
       *  Optional. The name of the Folder, TeamFolder, or root location to move the
       *  repository to. Can be in the format of: "" to move into the root User
       *  folder, `projects/* /locations/* /folders/*`,
       *  `projects/* /locations/* /teamFolders/*`
       */
      // const destinationContainingFolder = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callMoveRepository() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataformClient.moveRepository(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callMoveRepository();
    
    

### moveRepository(request, options, callback)
    
    
    moveRepository(request: protos.google.cloud.dataform.v1beta1.IMoveRepositoryRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IMoveRepositoryMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imoverepositoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IMoveRepositoryMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imoverepositorymetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### moveRepository(request, callback)
    
    
    moveRepository(request: protos.google.cloud.dataform.v1beta1.IMoveRepositoryRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.dataform.v1beta1.IMoveRepositoryMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imoverepositoryrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.protobuf.iempty), [protos.google.cloud.dataform.v1beta1.IMoveRepositoryMetadata](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.imoverepositorymetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### pullGitCommits(request, options)
    
    
    pullGitCommits(request?: protos.google.cloud.dataform.v1beta1.IPullGitCommitsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IPullGitCommitsResponse,
            protos.google.cloud.dataform.v1beta1.IPullGitCommitsRequest | undefined,
            {} | undefined
        ]>;

Pulls Git commits from the Repository's remote into a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IPullGitCommitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsresponse), [protos.google.cloud.dataform.v1beta1.IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [PullGitCommitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.pullgitcommitsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. The name of the branch in the Git remote from which to pull
       *  commits. If left unset, the repository's default branch name will be used.
       */
      // const remoteBranch = 'abc123'
      /**
       *  Required. The author of any merge commit which may be created as a result
       *  of merging fetched Git commits into this workspace.
       */
      // const author = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callPullGitCommits() {
        // Construct request
        const request = {
          name,
          author,
        };
    
        // Run request
        const response = await dataformClient.pullGitCommits(request);
        console.log(response);
      }
    
      callPullGitCommits();
    
    

### pullGitCommits(request, options, callback)
    
    
    pullGitCommits(request: protos.google.cloud.dataform.v1beta1.IPullGitCommitsRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IPullGitCommitsResponse, protos.google.cloud.dataform.v1beta1.IPullGitCommitsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IPullGitCommitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsresponse), [protos.google.cloud.dataform.v1beta1.IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pullGitCommits(request, callback)
    
    
    pullGitCommits(request: protos.google.cloud.dataform.v1beta1.IPullGitCommitsRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IPullGitCommitsResponse, protos.google.cloud.dataform.v1beta1.IPullGitCommitsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IPullGitCommitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsresponse), [protos.google.cloud.dataform.v1beta1.IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pushGitCommits(request, options)
    
    
    pushGitCommits(request?: protos.google.cloud.dataform.v1beta1.IPushGitCommitsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IPushGitCommitsResponse,
            protos.google.cloud.dataform.v1beta1.IPushGitCommitsRequest | undefined,
            {} | undefined
        ]>;

Pushes Git commits from a Workspace to the Repository's remote.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPushGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipushgitcommitsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IPushGitCommitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipushgitcommitsresponse), [protos.google.cloud.dataform.v1beta1.IPushGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipushgitcommitsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [PushGitCommitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.pushgitcommitsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. The name of the branch in the Git remote to which commits should
       *  be pushed. If left unset, the repository's default branch name will be
       *  used.
       */
      // const remoteBranch = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callPushGitCommits() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.pushGitCommits(request);
        console.log(response);
      }
    
      callPushGitCommits();
    
    

### pushGitCommits(request, options, callback)
    
    
    pushGitCommits(request: protos.google.cloud.dataform.v1beta1.IPushGitCommitsRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IPushGitCommitsResponse, protos.google.cloud.dataform.v1beta1.IPushGitCommitsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPushGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipushgitcommitsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IPushGitCommitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipushgitcommitsresponse), [protos.google.cloud.dataform.v1beta1.IPushGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipushgitcommitsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pushGitCommits(request, callback)
    
    
    pushGitCommits(request: protos.google.cloud.dataform.v1beta1.IPushGitCommitsRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IPushGitCommitsResponse, protos.google.cloud.dataform.v1beta1.IPushGitCommitsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPushGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipushgitcommitsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IPushGitCommitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipushgitcommitsresponse), [protos.google.cloud.dataform.v1beta1.IPushGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipushgitcommitsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryCompilationResultActions(request, options)
    
    
    queryCompilationResultActions(request?: protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ICompilationResultAction[],
            protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest | null,
            protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsResponse
        ]>;

Returns CompilationResultActions in a given CompilationResult.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCompilationResultActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ICompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresultaction)[], [protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsrequest) | null, [protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `queryCompilationResultActionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryCompilationResultActions(request, options, callback)
    
    
    queryCompilationResultActions(request: protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest, protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.ICompilationResultAction>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCompilationResultActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsrequest), [protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.ICompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresultaction)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryCompilationResultActions(request, callback)
    
    
    queryCompilationResultActions(request: protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest, protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.ICompilationResultAction>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCompilationResultActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsrequest), [protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.ICompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresultaction)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryCompilationResultActionsAsync(request, options)
    
    
    queryCompilationResultActionsAsync(request?: protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.ICompilationResultAction>;

Equivalent to `queryCompilationResultActions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCompilationResultActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.ICompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.icompilationresultaction)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The compilation result's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. Maximum number of compilation results to return. The server may
       *  return fewer items than requested. If unspecified, the server will pick an
       *  appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous
       *  `QueryCompilationResultActions` call. Provide this to retrieve the
       *  subsequent page.
       *  When paginating, all other parameters provided to
       *  `QueryCompilationResultActions`, with the exception of `page_size`, must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Optional filter for the returned list. Filtering is only
       *  currently supported on the `file_path` field.
       */
      // const filter = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callQueryCompilationResultActions() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const iterable = dataformClient.queryCompilationResultActionsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callQueryCompilationResultActions();
    
    

### queryCompilationResultActionsStream(request, options)
    
    
    queryCompilationResultActionsStream(request?: protos.google.cloud.dataform.v1beta1.IQueryCompilationResultActionsRequest, options?: CallOptions): Transform;

Equivalent to `queryCompilationResultActions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCompilationResultActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerycompilationresultactionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `queryCompilationResultActionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryDirectoryContents(request, options)
    
    
    queryDirectoryContents(request?: protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IDirectoryEntry[],
            protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest | null,
            protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsResponse
        ]>;

Returns the contents of a given Workspace directory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IDirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.idirectoryentry)[], [protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsrequest) | null, [protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [DirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.directoryentry). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `queryDirectoryContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryDirectoryContents(request, options, callback)
    
    
    queryDirectoryContents(request: protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest, protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IDirectoryEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsrequest), [protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IDirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.idirectoryentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryDirectoryContents(request, callback)
    
    
    queryDirectoryContents(request: protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest, protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IDirectoryEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsrequest), [protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IDirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.idirectoryentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryDirectoryContentsAsync(request, options)
    
    
    queryDirectoryContentsAsync(request?: protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.IDirectoryEntry>;

Equivalent to `queryDirectoryContents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.IDirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.idirectoryentry)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [DirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.directoryentry). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Optional. The directory's full path including directory name, relative to
       *  the workspace root. If left unset, the workspace root is used.
       */
      // const path = 'abc123'
      /**
       *  Optional. Maximum number of paths to return. The server may return fewer
       *  items than requested. If unspecified, the server will pick an appropriate
       *  default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `QueryDirectoryContents`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `QueryDirectoryContents`, with the exception of `page_size`, must match the
       *  call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Specifies the metadata to return for each directory entry.
       *  If unspecified, the default is `DIRECTORY_CONTENTS_VIEW_BASIC`.
       *  Currently the `DIRECTORY_CONTENTS_VIEW_METADATA` view is not supported by
       *  CMEK-protected workspaces.
       */
      // const view = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callQueryDirectoryContents() {
        // Construct request
        const request = {
          workspace,
        };
    
        // Run request
        const iterable = dataformClient.queryDirectoryContentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callQueryDirectoryContents();
    
    

### queryDirectoryContentsStream(request, options)
    
    
    queryDirectoryContentsStream(request?: protos.google.cloud.dataform.v1beta1.IQueryDirectoryContentsRequest, options?: CallOptions): Transform;

Equivalent to `queryDirectoryContents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iquerydirectorycontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [DirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.directoryentry) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `queryDirectoryContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryFolderContents(request, options)
    
    
    queryFolderContents(request?: protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.QueryFolderContentsResponse.IFolderContentsEntry[],
            protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest | null,
            protos.google.cloud.dataform.v1beta1.IQueryFolderContentsResponse
        ]>;

Returns the contents of a given Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.QueryFolderContentsResponse.IFolderContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryfoldercontentsresponse.ifoldercontentsentry)[], [protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsrequest) | null, [protos.google.cloud.dataform.v1beta1.IQueryFolderContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `queryFolderContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryFolderContents(request, options, callback)
    
    
    queryFolderContents(request: protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest, protos.google.cloud.dataform.v1beta1.IQueryFolderContentsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.QueryFolderContentsResponse.IFolderContentsEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsrequest), [protos.google.cloud.dataform.v1beta1.IQueryFolderContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.QueryFolderContentsResponse.IFolderContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryfoldercontentsresponse.ifoldercontentsentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryFolderContents(request, callback)
    
    
    queryFolderContents(request: protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest, protos.google.cloud.dataform.v1beta1.IQueryFolderContentsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.QueryFolderContentsResponse.IFolderContentsEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsrequest), [protos.google.cloud.dataform.v1beta1.IQueryFolderContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.QueryFolderContentsResponse.IFolderContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryfoldercontentsresponse.ifoldercontentsentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryFolderContentsAsync(request, options)
    
    
    queryFolderContentsAsync(request?: protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.QueryFolderContentsResponse.IFolderContentsEntry>;

Equivalent to `queryFolderContents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.QueryFolderContentsResponse.IFolderContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryfoldercontentsresponse.ifoldercontentsentry)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the Folder to list contents for.
       *  Format: projects/* /locations/* /folders/*
       */
      // const folder = 'abc123'
      /**
       *  Optional. Maximum number of paths to return. The server may return fewer
       *  items than requested. If unspecified, the server will pick an appropriate
       *  default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `QueryFolderContents` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `QueryFolderContents`, with the exception of `page_size`, must match the
       *  call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Field to additionally sort results by.
       *  Will order Folders before Repositories, and then by `order_by` in ascending
       *  order. Supported keywords: display_name (default), create_time,
       *  last_modified_time.
       *  Examples:
       *  * `orderBy="display_name"`
       *  * `orderBy="display_name desc"`
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Optional filtering for the returned list. Filtering is currently
       *  only supported on the `display_name` field.
       *  Example:
       *  * `filter="display_name="MyFolder""`
       */
      // const filter = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callQueryFolderContents() {
        // Construct request
        const request = {
          folder,
        };
    
        // Run request
        const iterable = dataformClient.queryFolderContentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callQueryFolderContents();
    
    

### queryFolderContentsStream(request, options)
    
    
    queryFolderContentsStream(request?: protos.google.cloud.dataform.v1beta1.IQueryFolderContentsRequest, options?: CallOptions): Transform;

Equivalent to `queryFolderContents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryfoldercontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `queryFolderContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryRepositoryDirectoryContents(request, options)
    
    
    queryRepositoryDirectoryContents(request?: protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IDirectoryEntry[],
            protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest | null,
            protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsResponse
        ]>;

Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IDirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.idirectoryentry)[], [protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsrequest) | null, [protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [DirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.directoryentry). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `queryRepositoryDirectoryContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryRepositoryDirectoryContents(request, options, callback)
    
    
    queryRepositoryDirectoryContents(request: protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest, protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IDirectoryEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsrequest), [protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IDirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.idirectoryentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryRepositoryDirectoryContents(request, callback)
    
    
    queryRepositoryDirectoryContents(request: protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest, protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IDirectoryEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsrequest), [protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IDirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.idirectoryentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryRepositoryDirectoryContentsAsync(request, options)
    
    
    queryRepositoryDirectoryContentsAsync(request?: protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.IDirectoryEntry>;

Equivalent to `queryRepositoryDirectoryContents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.IDirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.idirectoryentry)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [DirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.directoryentry). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. The Commit SHA for the commit to query from. If unset, the
       *  directory will be queried from HEAD.
       */
      // const commitSha = 'abc123'
      /**
       *  Optional. The directory's full path including directory name, relative to
       *  root. If left unset, the root is used.
       */
      // const path = 'abc123'
      /**
       *  Optional. Maximum number of paths to return. The server may return fewer
       *  items than requested. If unspecified, the server will pick an appropriate
       *  default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous
       *  `QueryRepositoryDirectoryContents` call. Provide this to retrieve the
       *  subsequent page.
       *  When paginating, all other parameters provided to
       *  `QueryRepositoryDirectoryContents`, with the exception of `page_size`, must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callQueryRepositoryDirectoryContents() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const iterable = dataformClient.queryRepositoryDirectoryContentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callQueryRepositoryDirectoryContents();
    
    

### queryRepositoryDirectoryContentsStream(request, options)
    
    
    queryRepositoryDirectoryContentsStream(request?: protos.google.cloud.dataform.v1beta1.IQueryRepositoryDirectoryContentsRequest, options?: CallOptions): Transform;

Equivalent to `queryRepositoryDirectoryContents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryrepositorydirectorycontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [DirectoryEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.directoryentry) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `queryRepositoryDirectoryContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryTeamFolderContents(request, options)
    
    
    queryTeamFolderContents(request?: protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.QueryTeamFolderContentsResponse.ITeamFolderContentsEntry[],
            protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest | null,
            protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsResponse
        ]>;

Returns the contents of a given TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryTeamFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.QueryTeamFolderContentsResponse.ITeamFolderContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryteamfoldercontentsresponse.iteamfoldercontentsentry)[], [protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsrequest) | null, [protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `queryTeamFolderContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryTeamFolderContents(request, options, callback)
    
    
    queryTeamFolderContents(request: protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest, protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.QueryTeamFolderContentsResponse.ITeamFolderContentsEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryTeamFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsrequest), [protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.QueryTeamFolderContentsResponse.ITeamFolderContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryteamfoldercontentsresponse.iteamfoldercontentsentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryTeamFolderContents(request, callback)
    
    
    queryTeamFolderContents(request: protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest, protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.QueryTeamFolderContentsResponse.ITeamFolderContentsEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryTeamFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsrequest), [protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.QueryTeamFolderContentsResponse.ITeamFolderContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryteamfoldercontentsresponse.iteamfoldercontentsentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryTeamFolderContentsAsync(request, options)
    
    
    queryTeamFolderContentsAsync(request?: protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.QueryTeamFolderContentsResponse.ITeamFolderContentsEntry>;

Equivalent to `queryTeamFolderContents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryTeamFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.QueryTeamFolderContentsResponse.ITeamFolderContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryteamfoldercontentsresponse.iteamfoldercontentsentry)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the TeamFolder to list contents for.
       *  Format: `projects/* /locations/* /teamFolders/*`.
       */
      // const teamFolder = 'abc123'
      /**
       *  Optional. Maximum number of paths to return. The server may return fewer
       *  items than requested. If unspecified, the server will pick an appropriate
       *  default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `QueryTeamFolderContents`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `QueryTeamFolderContents`, with the exception of `page_size`, must match
       *  the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Field to additionally sort results by.
       *  Will order Folders before Repositories, and then by `order_by` in ascending
       *  order. Supported keywords: `display_name` (default), `create_time`,
       *  last_modified_time.
       *  Examples:
       *  * `orderBy="display_name"`
       *  * `orderBy="display_name desc"`
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Optional filtering for the returned list. Filtering is currently
       *  only supported on the `display_name` field.
       *  Example:
       *  * `filter="display_name="MyFolder""`
       */
      // const filter = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callQueryTeamFolderContents() {
        // Construct request
        const request = {
          teamFolder,
        };
    
        // Run request
        const iterable = dataformClient.queryTeamFolderContentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callQueryTeamFolderContents();
    
    

### queryTeamFolderContentsStream(request, options)
    
    
    queryTeamFolderContentsStream(request?: protos.google.cloud.dataform.v1beta1.IQueryTeamFolderContentsRequest, options?: CallOptions): Transform;

Equivalent to `queryTeamFolderContents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryTeamFolderContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryteamfoldercontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `queryTeamFolderContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryUserRootContents(request, options)
    
    
    queryUserRootContents(request?: protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.QueryUserRootContentsResponse.IRootContentsEntry[],
            protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest | null,
            protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsResponse
        ]>;

Returns the contents of a caller's root folder in a given location. The root folder contains all resources that are created by the user and not contained in any other folder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryUserRootContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.QueryUserRootContentsResponse.IRootContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryuserrootcontentsresponse.irootcontentsentry)[], [protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsrequest) | null, [protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `queryUserRootContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryUserRootContents(request, options, callback)
    
    
    queryUserRootContents(request: protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest, protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.QueryUserRootContentsResponse.IRootContentsEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryUserRootContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsrequest), [protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.QueryUserRootContentsResponse.IRootContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryuserrootcontentsresponse.irootcontentsentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryUserRootContents(request, callback)
    
    
    queryUserRootContents(request: protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest, protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.QueryUserRootContentsResponse.IRootContentsEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryUserRootContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsrequest), [protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.QueryUserRootContentsResponse.IRootContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryuserrootcontentsresponse.irootcontentsentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryUserRootContentsAsync(request, options)
    
    
    queryUserRootContentsAsync(request?: protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.QueryUserRootContentsResponse.IRootContentsEntry>;

Equivalent to `queryUserRootContents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryUserRootContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.QueryUserRootContentsResponse.IRootContentsEntry](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.queryuserrootcontentsresponse.irootcontentsentry)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Location of the user root folder to list contents for.
       *  Format: projects/* /locations/*
       */
      // const location = 'abc123'
      /**
       *  Optional. Maximum number of paths to return. The server may return fewer
       *  items than requested. If unspecified, the server will pick an appropriate
       *  default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `QueryUserRootContents` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `QueryUserRootFolderContents`, with the exception of `page_size`, must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Field to additionally sort results by.
       *  Will order Folders before Repositories, and then by `order_by` in ascending
       *  order. Supported keywords: display_name (default), created_at,
       *  last_modified_at. Examples:
       *  * `orderBy="display_name"`
       *  * `orderBy="display_name desc"`
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Optional filtering for the returned list. Filtering is currently
       *  only supported on the `display_name` field.
       *  Example:
       *  * `filter="display_name="MyFolder""`
       */
      // const filter = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callQueryUserRootContents() {
        // Construct request
        const request = {
          location,
        };
    
        // Run request
        const iterable = dataformClient.queryUserRootContentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callQueryUserRootContents();
    
    

### queryUserRootContentsStream(request, options)
    
    
    queryUserRootContentsStream(request?: protos.google.cloud.dataform.v1beta1.IQueryUserRootContentsRequest, options?: CallOptions): Transform;

Equivalent to `queryUserRootContents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryUserRootContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryuserrootcontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `queryUserRootContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryWorkflowInvocationActions(request, options)
    
    
    queryWorkflowInvocationActions(request?: protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkflowInvocationAction[],
            protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest | null,
            protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsResponse
        ]>;

Returns WorkflowInvocationActions in a given WorkflowInvocation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkflowInvocationAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocationaction)[], [protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsrequest) | null, [protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `queryWorkflowInvocationActionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### queryWorkflowInvocationActions(request, options, callback)
    
    
    queryWorkflowInvocationActions(request: protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest, protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IWorkflowInvocationAction>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsrequest), [protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IWorkflowInvocationAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocationaction)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryWorkflowInvocationActions(request, callback)
    
    
    queryWorkflowInvocationActions(request: protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest, protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsResponse | null | undefined, protos.google.cloud.dataform.v1beta1.IWorkflowInvocationAction>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsrequest), [protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.IWorkflowInvocationAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocationaction)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryWorkflowInvocationActionsAsync(request, options)
    
    
    queryWorkflowInvocationActionsAsync(request?: protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.IWorkflowInvocationAction>;

Equivalent to `queryWorkflowInvocationActions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.IWorkflowInvocationAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowinvocationaction)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workflow invocation's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. Maximum number of workflow invocations to return. The server may
       *  return fewer items than requested. If unspecified, the server will pick an
       *  appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous
       *  `QueryWorkflowInvocationActions` call. Provide this to retrieve the
       *  subsequent page.
       *  When paginating, all other parameters provided to
       *  `QueryWorkflowInvocationActions`, with the exception of `page_size`, must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callQueryWorkflowInvocationActions() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const iterable = dataformClient.queryWorkflowInvocationActionsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callQueryWorkflowInvocationActions();
    
    

### queryWorkflowInvocationActionsStream(request, options)
    
    
    queryWorkflowInvocationActionsStream(request?: protos.google.cloud.dataform.v1beta1.IQueryWorkflowInvocationActionsRequest, options?: CallOptions): Transform;

Equivalent to `queryWorkflowInvocationActions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iqueryworkflowinvocationactionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `queryWorkflowInvocationActionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### readFile(request, options)
    
    
    readFile(request?: protos.google.cloud.dataform.v1beta1.IReadFileRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IReadFileResponse,
            protos.google.cloud.dataform.v1beta1.IReadFileRequest | undefined,
            {} | undefined
        ]>;

Returns the contents of a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadfilerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IReadFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadfileresponse), [protos.google.cloud.dataform.v1beta1.IReadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadfilerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ReadFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.readfileresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Required. The file's full path including filename, relative to the
       *  workspace root.
       */
      // const path = 'abc123'
      /**
       *  Optional. The Git revision of the file to return. If left empty, the
       *  current contents of `path` will be returned.
       */
      // const revision = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callReadFile() {
        // Construct request
        const request = {
          workspace,
          path,
        };
    
        // Run request
        const response = await dataformClient.readFile(request);
        console.log(response);
      }
    
      callReadFile();
    
    

### readFile(request, options, callback)
    
    
    readFile(request: protos.google.cloud.dataform.v1beta1.IReadFileRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IReadFileResponse, protos.google.cloud.dataform.v1beta1.IReadFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadfilerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IReadFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadfileresponse), [protos.google.cloud.dataform.v1beta1.IReadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadfilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readFile(request, callback)
    
    
    readFile(request: protos.google.cloud.dataform.v1beta1.IReadFileRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IReadFileResponse, protos.google.cloud.dataform.v1beta1.IReadFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadfilerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IReadFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadfileresponse), [protos.google.cloud.dataform.v1beta1.IReadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadfilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readRepositoryFile(request, options)
    
    
    readRepositoryFile(request?: protos.google.cloud.dataform.v1beta1.IReadRepositoryFileRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IReadRepositoryFileResponse,
            (protos.google.cloud.dataform.v1beta1.IReadRepositoryFileRequest | undefined),
            {} | undefined
        ]>;

Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadRepositoryFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadrepositoryfilerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IReadRepositoryFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadrepositoryfileresponse), ([protos.google.cloud.dataform.v1beta1.IReadRepositoryFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadrepositoryfilerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ReadRepositoryFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.readrepositoryfileresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The repository's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. The commit SHA for the commit to read from. If unset, the file
       *  will be read from HEAD.
       */
      // const commitSha = 'abc123'
      /**
       *  Required. Full file path to read including filename, from repository root.
       */
      // const path = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callReadRepositoryFile() {
        // Construct request
        const request = {
          name,
          path,
        };
    
        // Run request
        const response = await dataformClient.readRepositoryFile(request);
        console.log(response);
      }
    
      callReadRepositoryFile();
    
    

### readRepositoryFile(request, options, callback)
    
    
    readRepositoryFile(request: protos.google.cloud.dataform.v1beta1.IReadRepositoryFileRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IReadRepositoryFileResponse, protos.google.cloud.dataform.v1beta1.IReadRepositoryFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadRepositoryFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadrepositoryfilerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IReadRepositoryFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadrepositoryfileresponse), [protos.google.cloud.dataform.v1beta1.IReadRepositoryFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadrepositoryfilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### readRepositoryFile(request, callback)
    
    
    readRepositoryFile(request: protos.google.cloud.dataform.v1beta1.IReadRepositoryFileRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IReadRepositoryFileResponse, protos.google.cloud.dataform.v1beta1.IReadRepositoryFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReadRepositoryFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadrepositoryfilerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IReadRepositoryFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadrepositoryfileresponse), [protos.google.cloud.dataform.v1beta1.IReadRepositoryFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireadrepositoryfilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### releaseConfigPath(project, location, repository, releaseConfig)
    
    
    releaseConfigPath(project: string, location: string, repository: string, releaseConfig: string): string;

Return a fully-qualified releaseConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`repository` |  `string`   
  
`releaseConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### removeDirectory(request, options)
    
    
    removeDirectory(request?: protos.google.cloud.dataform.v1beta1.IRemoveDirectoryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IRemoveDirectoryResponse,
            protos.google.cloud.dataform.v1beta1.IRemoveDirectoryRequest | undefined,
            {} | undefined
        ]>;

Deletes a directory (inside a Workspace) and all of its contents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovedirectoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IRemoveDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovedirectoryresponse), [protos.google.cloud.dataform.v1beta1.IRemoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovedirectoryrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RemoveDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.removedirectoryresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Required. The directory's full path including directory name, relative to
       *  the workspace root.
       */
      // const path = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callRemoveDirectory() {
        // Construct request
        const request = {
          workspace,
          path,
        };
    
        // Run request
        const response = await dataformClient.removeDirectory(request);
        console.log(response);
      }
    
      callRemoveDirectory();
    
    

### removeDirectory(request, options, callback)
    
    
    removeDirectory(request: protos.google.cloud.dataform.v1beta1.IRemoveDirectoryRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IRemoveDirectoryResponse, protos.google.cloud.dataform.v1beta1.IRemoveDirectoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovedirectoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IRemoveDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovedirectoryresponse), [protos.google.cloud.dataform.v1beta1.IRemoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovedirectoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeDirectory(request, callback)
    
    
    removeDirectory(request: protos.google.cloud.dataform.v1beta1.IRemoveDirectoryRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IRemoveDirectoryResponse, protos.google.cloud.dataform.v1beta1.IRemoveDirectoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovedirectoryrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IRemoveDirectoryResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovedirectoryresponse), [protos.google.cloud.dataform.v1beta1.IRemoveDirectoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovedirectoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeFile(request, options)
    
    
    removeFile(request?: protos.google.cloud.dataform.v1beta1.IRemoveFileRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IRemoveFileResponse,
            protos.google.cloud.dataform.v1beta1.IRemoveFileRequest | undefined,
            {} | undefined
        ]>;

Deletes a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovefilerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IRemoveFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovefileresponse), [protos.google.cloud.dataform.v1beta1.IRemoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovefilerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [RemoveFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.removefileresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Required. The file's full path including filename, relative to the
       *  workspace root.
       */
      // const path = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callRemoveFile() {
        // Construct request
        const request = {
          workspace,
          path,
        };
    
        // Run request
        const response = await dataformClient.removeFile(request);
        console.log(response);
      }
    
      callRemoveFile();
    
    

### removeFile(request, options, callback)
    
    
    removeFile(request: protos.google.cloud.dataform.v1beta1.IRemoveFileRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IRemoveFileResponse, protos.google.cloud.dataform.v1beta1.IRemoveFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovefilerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IRemoveFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovefileresponse), [protos.google.cloud.dataform.v1beta1.IRemoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovefilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeFile(request, callback)
    
    
    removeFile(request: protos.google.cloud.dataform.v1beta1.IRemoveFileRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IRemoveFileResponse, protos.google.cloud.dataform.v1beta1.IRemoveFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovefilerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IRemoveFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovefileresponse), [protos.google.cloud.dataform.v1beta1.IRemoveFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iremovefilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### repositoryPath(project, location, repository)
    
    
    repositoryPath(project: string, location: string, repository: string): string;

Return a fully-qualified repository resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`repository` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### resetWorkspaceChanges(request, options)
    
    
    resetWorkspaceChanges(request?: protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesResponse,
            (protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesRequest | undefined),
            {} | undefined
        ]>;

Performs a Git reset for uncommitted files in a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResetWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iresetworkspacechangesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iresetworkspacechangesresponse), ([protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iresetworkspacechangesrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ResetWorkspaceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.resetworkspacechangesresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const name = 'abc123'
      /**
       *  Optional. Full file paths to reset back to their committed state including
       *  filename, rooted at workspace root. If left empty, all files will be reset.
       */
      // const paths = ['abc','def']
      /**
       *  Optional. If set to true, untracked files will be deleted.
       */
      // const clean = true
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callResetWorkspaceChanges() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.resetWorkspaceChanges(request);
        console.log(response);
      }
    
      callResetWorkspaceChanges();
    
    

### resetWorkspaceChanges(request, options, callback)
    
    
    resetWorkspaceChanges(request: protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesResponse, protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResetWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iresetworkspacechangesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iresetworkspacechangesresponse), [protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iresetworkspacechangesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resetWorkspaceChanges(request, callback)
    
    
    resetWorkspaceChanges(request: protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesResponse, protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResetWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iresetworkspacechangesrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iresetworkspacechangesresponse), [protos.google.cloud.dataform.v1beta1.IResetWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iresetworkspacechangesrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchFiles(request, options)
    
    
    searchFiles(request?: protos.google.cloud.dataform.v1beta1.ISearchFilesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ISearchResult[],
            protos.google.cloud.dataform.v1beta1.ISearchFilesRequest | null,
            protos.google.cloud.dataform.v1beta1.ISearchFilesResponse
        ]>;

Finds the contents of a given Workspace directory by filter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ISearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchresult)[], [protos.google.cloud.dataform.v1beta1.ISearchFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesrequest) | null, [protos.google.cloud.dataform.v1beta1.ISearchFilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [SearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.searchresult). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `searchFilesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### searchFiles(request, options, callback)
    
    
    searchFiles(request: protos.google.cloud.dataform.v1beta1.ISearchFilesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.ISearchFilesRequest, protos.google.cloud.dataform.v1beta1.ISearchFilesResponse | null | undefined, protos.google.cloud.dataform.v1beta1.ISearchResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.ISearchFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesrequest), [protos.google.cloud.dataform.v1beta1.ISearchFilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.ISearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchFiles(request, callback)
    
    
    searchFiles(request: protos.google.cloud.dataform.v1beta1.ISearchFilesRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.ISearchFilesRequest, protos.google.cloud.dataform.v1beta1.ISearchFilesResponse | null | undefined, protos.google.cloud.dataform.v1beta1.ISearchResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.ISearchFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesrequest), [protos.google.cloud.dataform.v1beta1.ISearchFilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.ISearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchFilesAsync(request, options)
    
    
    searchFilesAsync(request?: protos.google.cloud.dataform.v1beta1.ISearchFilesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.ISearchResult>;

Equivalent to `searchFiles`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.ISearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchresult)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [SearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.searchresult). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Optional. Maximum number of search results to return. The server may return
       *  fewer items than requested. If unspecified, the server will pick an
       *  appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `SearchFilesRequest`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `SearchFilesRequest`,
       *  with the exception of `page_size`, must match the call that provided the
       *  page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Optional filter for the returned list in filtering format.
       *  Filtering is only currently supported on the `path` field.
       *  See https://google.aip.dev/160 for details.
       */
      // const filter = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callSearchFiles() {
        // Construct request
        const request = {
          workspace,
        };
    
        // Run request
        const iterable = dataformClient.searchFilesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callSearchFiles();
    
    

### searchFilesStream(request, options)
    
    
    searchFilesStream(request?: protos.google.cloud.dataform.v1beta1.ISearchFilesRequest, options?: CallOptions): Transform;

Equivalent to `searchFiles`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchfilesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [SearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.searchresult) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `searchFilesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### searchTeamFolders(request, options)
    
    
    searchTeamFolders(request?: protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.SearchTeamFoldersResponse.ITeamFolderSearchResult[],
            protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest | null,
            protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersResponse
        ]>;

Returns all TeamFolders in a given location that the caller has access to and match the provided filter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchTeamFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.SearchTeamFoldersResponse.ITeamFolderSearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.searchteamfoldersresponse.iteamfoldersearchresult)[], [protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersrequest) | null, [protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `searchTeamFoldersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### searchTeamFolders(request, options, callback)
    
    
    searchTeamFolders(request: protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest, protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersResponse | null | undefined, protos.google.cloud.dataform.v1beta1.SearchTeamFoldersResponse.ITeamFolderSearchResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchTeamFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersrequest), [protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.SearchTeamFoldersResponse.ITeamFolderSearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.searchteamfoldersresponse.iteamfoldersearchresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchTeamFolders(request, callback)
    
    
    searchTeamFolders(request: protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest, callback: PaginationCallback<protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest, protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersResponse | null | undefined, protos.google.cloud.dataform.v1beta1.SearchTeamFoldersResponse.ITeamFolderSearchResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchTeamFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersrequest), [protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersresponse) | null | undefined, [protos.google.cloud.dataform.v1beta1.SearchTeamFoldersResponse.ITeamFolderSearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.searchteamfoldersresponse.iteamfoldersearchresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchTeamFoldersAsync(request, options)
    
    
    searchTeamFoldersAsync(request?: protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dataform.v1beta1.SearchTeamFoldersResponse.ITeamFolderSearchResult>;

Equivalent to `searchTeamFolders`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchTeamFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dataform.v1beta1.SearchTeamFoldersResponse.ITeamFolderSearchResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.searchteamfoldersresponse.iteamfoldersearchresult)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Location in which to query TeamFolders.
       *  Format: `projects/* /locations/*`.
       */
      // const location = 'abc123'
      /**
       *  Optional. Maximum number of `TeamFolders` to return. The server may return
       *  fewer items than requested. If unspecified, the server will pick a default
       *  of `page_size` = 50.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token received from a previous `SearchTeamFolders` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `SearchTeamFolders`, with the exception of `page_size`, must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Field to additionally sort results by.
       *  Supported keywords: `display_name` (default), `create_time`,
       *  `last_modified_time`. Examples:
       *  * `orderBy="display_name"`
       *  * `orderBy="display_name desc"`
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Optional filtering for the returned list. Filtering is currently
       *  only supported on the `display_name` field.
       *  Example:
       *  * `filter="display_name="MyFolder""`
       */
      // const filter = 'abc123'
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callSearchTeamFolders() {
        // Construct request
        const request = {
          location,
        };
    
        // Run request
        const iterable = dataformClient.searchTeamFoldersAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callSearchTeamFolders();
    
    

### searchTeamFoldersStream(request, options)
    
    
    searchTeamFoldersStream(request?: protos.google.cloud.dataform.v1beta1.ISearchTeamFoldersRequest, options?: CallOptions): Transform;

Equivalent to `searchTeamFolders`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchTeamFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isearchteamfoldersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `searchTeamFoldersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### secretVersionPath(project, secret, version)
    
    
    secretVersionPath(project: string, secret: string, version: string): string;

Return a fully-qualified secretVersion resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`secret` |  `string`   
  
`version` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### setIamPolicy(request, options)
    
    
    setIamPolicy(request?: protos.google.iam.v1.ISetIamPolicyRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1.IPolicy,
            protos.google.iam.v1.ISetIamPolicyRequest | undefined,
            {} | undefined
        ]>;

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.isetiampolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.isetiampolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  REQUIRED: The resource for which the policy is being specified.
       *  See the operation documentation for the appropriate value for this field.
       */
      // const resource = 'abc123'
      /**
       *  REQUIRED: The complete policy to be applied to the `resource`. The size of
       *  the policy is limited to a few 10s of KB. An empty policy is a
       *  valid policy but certain Cloud Platform services (such as Projects)
       *  might reject them.
       */
      // const policy = {}
      /**
       *  OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only
       *  the fields in the mask will be modified. If no mask is provided, the
       *  following default mask is used:
       *  `paths: "bindings, etag"`
       */
      // const updateMask = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callSetIamPolicy() {
        // Construct request
        const request = {
          resource,
          policy,
        };
    
        // Run request
        const response = await dataformClient.setIamPolicy(request);
        console.log(response);
      }
    
      callSetIamPolicy();
    
    

### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: protos.google.iam.v1.ISetIamPolicyRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.ISetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.isetiampolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.isetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, callback)
    
    
    setIamPolicy(request: protos.google.iam.v1.ISetIamPolicyRequest, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.ISetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.isetiampolicyrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.isetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### syncWorkspaceRefs(request, options)
    
    
    syncWorkspaceRefs(request?: protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsResponse,
            (protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsRequest | undefined),
            {} | undefined
        ]>;

Syncs the refs of a Workspace.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISyncWorkspaceRefsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isyncworkspacerefsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isyncworkspacerefsresponse), ([protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isyncworkspacerefsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [SyncWorkspaceRefsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.syncworkspacerefsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace resource name.
       *  Format:
       *  projects/{project}/locations/{location}/repositories/{repository}/workspaces/{workspace}
       */
      // const name = 'abc123'
      /**
       *  Optional. The name of the branch in the Git remote to which the refs should
       *  be fetched for. If left unset, all remote branches will be fetched.
       */
      // const remoteBranchName = 'abc123'
      /**
       *  Optional. Can be used to deepen the commit history of shallow clones.
       *  Git documentation:
       *  https://git-scm.com/docs/git-fetch#Documentation/git-fetch.txt---deependepth
       */
      // const deepen = 1234
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callSyncWorkspaceRefs() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await dataformClient.syncWorkspaceRefs(request);
        console.log(response);
      }
    
      callSyncWorkspaceRefs();
    
    

### syncWorkspaceRefs(request, options, callback)
    
    
    syncWorkspaceRefs(request: protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsResponse, protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISyncWorkspaceRefsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isyncworkspacerefsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isyncworkspacerefsresponse), [protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isyncworkspacerefsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### syncWorkspaceRefs(request, callback)
    
    
    syncWorkspaceRefs(request: protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsResponse, protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISyncWorkspaceRefsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isyncworkspacerefsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isyncworkspacerefsresponse), [protos.google.cloud.dataform.v1beta1.ISyncWorkspaceRefsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.isyncworkspacerefsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### teamFolderPath(project, location, teamFolder)
    
    
    teamFolderPath(project: string, location: string, teamFolder: string): string;

Return a fully-qualified teamFolder resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`teamFolder` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### testIamPermissions(request, options)
    
    
    testIamPermissions(request?: protos.google.iam.v1.ITestIamPermissionsRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1.ITestIamPermissionsResponse,
            protos.google.iam.v1.ITestIamPermissionsRequest | undefined,
            {} | undefined
        ]>;

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.ITestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsresponse), [protos.google.iam.v1.ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.testiampermissionsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  REQUIRED: The resource for which the policy detail is being requested.
       *  See the operation documentation for the appropriate value for this field.
       */
      // const resource = 'abc123'
      /**
       *  The set of permissions to check for the `resource`. Permissions with
       *  wildcards (such as '*' or 'storage.*') are not allowed. For more
       *  information see
       *  IAM Overview (https://cloud.google.com/iam/docs/overview#permissions).
       */
      // const permissions = ['abc','def']
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callTestIamPermissions() {
        // Construct request
        const request = {
          resource,
          permissions,
        };
    
        // Run request
        const response = await dataformClient.testIamPermissions(request);
        console.log(response);
      }
    
      callTestIamPermissions();
    
    

### testIamPermissions(request, options, callback)
    
    
    testIamPermissions(request: protos.google.iam.v1.ITestIamPermissionsRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.ITestIamPermissionsResponse, protos.google.iam.v1.ITestIamPermissionsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.ITestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsresponse), [protos.google.iam.v1.ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, callback)
    
    
    testIamPermissions(request: protos.google.iam.v1.ITestIamPermissionsRequest, callback: Callback<protos.google.iam.v1.ITestIamPermissionsResponse, protos.google.iam.v1.ITestIamPermissionsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.ITestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsresponse), [protos.google.iam.v1.ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.iam.v1.itestiampermissionsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConfig(request, options)
    
    
    updateConfig(request?: protos.google.cloud.dataform.v1beta1.IUpdateConfigRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IConfig,
            protos.google.cloud.dataform.v1beta1.IUpdateConfigRequest | undefined,
            {} | undefined
        ]>;

Update default config for a given project and location.

**Note:** *This method does not fully implement [AIP/134](<https://google.aip.dev/134>). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iconfig), [protos.google.cloud.dataform.v1beta1.IUpdateConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateconfigrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Config](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.config). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The config to update.
       */
      // const config = {}
      /**
       *  Optional. Specifies the fields to be updated in the config.
       */
      // const updateMask = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callUpdateConfig() {
        // Construct request
        const request = {
          config,
        };
    
        // Run request
        const response = await dataformClient.updateConfig(request);
        console.log(response);
      }
    
      callUpdateConfig();
    
    

### updateConfig(request, options, callback)
    
    
    updateConfig(request: protos.google.cloud.dataform.v1beta1.IUpdateConfigRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IConfig, protos.google.cloud.dataform.v1beta1.IUpdateConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iconfig), [protos.google.cloud.dataform.v1beta1.IUpdateConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConfig(request, callback)
    
    
    updateConfig(request: protos.google.cloud.dataform.v1beta1.IUpdateConfigRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IConfig, protos.google.cloud.dataform.v1beta1.IUpdateConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateconfigrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iconfig), [protos.google.cloud.dataform.v1beta1.IUpdateConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFolder(request, options)
    
    
    updateFolder(request?: protos.google.cloud.dataform.v1beta1.IUpdateFolderRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IFolder,
            protos.google.cloud.dataform.v1beta1.IUpdateFolderRequest | undefined,
            {} | undefined
        ]>;

Updates a single Folder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatefolderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifolder), [protos.google.cloud.dataform.v1beta1.IUpdateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatefolderrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Folder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.folder). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Specifies the fields to be updated in the Folder. If left unset,
       *  all fields that can be updated, will be updated. A few fields cannot be
       *  updated and will be ignored if specified in the update_mask (e.g.
       *  parent_name, team_folder_name).
       */
      // const updateMask = {}
      /**
       *  Required. The updated Folder.
       */
      // const folder = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callUpdateFolder() {
        // Construct request
        const request = {
          folder,
        };
    
        // Run request
        const response = await dataformClient.updateFolder(request);
        console.log(response);
      }
    
      callUpdateFolder();
    
    

### updateFolder(request, options, callback)
    
    
    updateFolder(request: protos.google.cloud.dataform.v1beta1.IUpdateFolderRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IFolder, protos.google.cloud.dataform.v1beta1.IUpdateFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatefolderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifolder), [protos.google.cloud.dataform.v1beta1.IUpdateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatefolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFolder(request, callback)
    
    
    updateFolder(request: protos.google.cloud.dataform.v1beta1.IUpdateFolderRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IFolder, protos.google.cloud.dataform.v1beta1.IUpdateFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatefolderrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ifolder), [protos.google.cloud.dataform.v1beta1.IUpdateFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatefolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateReleaseConfig(request, options)
    
    
    updateReleaseConfig(request?: protos.google.cloud.dataform.v1beta1.IUpdateReleaseConfigRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IReleaseConfig,
            (protos.google.cloud.dataform.v1beta1.IUpdateReleaseConfigRequest | undefined),
            {} | undefined
        ]>;

Updates a single ReleaseConfig.

**Note:** *This method does not fully implement [AIP/134](<https://google.aip.dev/134>). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatereleaseconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig), ([protos.google.cloud.dataform.v1beta1.IUpdateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatereleaseconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Specifies the fields to be updated in the release config. If left
       *  unset, all fields will be updated.
       */
      // const updateMask = {}
      /**
       *  Required. The release config to update.
       */
      // const releaseConfig = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callUpdateReleaseConfig() {
        // Construct request
        const request = {
          releaseConfig,
        };
    
        // Run request
        const response = await dataformClient.updateReleaseConfig(request);
        console.log(response);
      }
    
      callUpdateReleaseConfig();
    
    

### updateReleaseConfig(request, options, callback)
    
    
    updateReleaseConfig(request: protos.google.cloud.dataform.v1beta1.IUpdateReleaseConfigRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IReleaseConfig, protos.google.cloud.dataform.v1beta1.IUpdateReleaseConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatereleaseconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig), [protos.google.cloud.dataform.v1beta1.IUpdateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatereleaseconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateReleaseConfig(request, callback)
    
    
    updateReleaseConfig(request: protos.google.cloud.dataform.v1beta1.IUpdateReleaseConfigRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IReleaseConfig, protos.google.cloud.dataform.v1beta1.IUpdateReleaseConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatereleaseconfigrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IReleaseConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ireleaseconfig), [protos.google.cloud.dataform.v1beta1.IUpdateReleaseConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdatereleaseconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRepository(request, options)
    
    
    updateRepository(request?: protos.google.cloud.dataform.v1beta1.IUpdateRepositoryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IRepository,
            protos.google.cloud.dataform.v1beta1.IUpdateRepositoryRequest | undefined,
            {} | undefined
        ]>;

Updates a single Repository.

**Note:** *This method does not fully implement [AIP/134](<https://google.aip.dev/134>). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdaterepositoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository), [protos.google.cloud.dataform.v1beta1.IUpdateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdaterepositoryrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Specifies the fields to be updated in the repository. If left
       *  unset, all fields will be updated.
       */
      // const updateMask = {}
      /**
       *  Required. The repository to update.
       */
      // const repository = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callUpdateRepository() {
        // Construct request
        const request = {
          repository,
        };
    
        // Run request
        const response = await dataformClient.updateRepository(request);
        console.log(response);
      }
    
      callUpdateRepository();
    
    

### updateRepository(request, options, callback)
    
    
    updateRepository(request: protos.google.cloud.dataform.v1beta1.IUpdateRepositoryRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IRepository, protos.google.cloud.dataform.v1beta1.IUpdateRepositoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdaterepositoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository), [protos.google.cloud.dataform.v1beta1.IUpdateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdaterepositoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRepository(request, callback)
    
    
    updateRepository(request: protos.google.cloud.dataform.v1beta1.IUpdateRepositoryRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IRepository, protos.google.cloud.dataform.v1beta1.IUpdateRepositoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdaterepositoryrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IRepository](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.irepository), [protos.google.cloud.dataform.v1beta1.IUpdateRepositoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdaterepositoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTeamFolder(request, options)
    
    
    updateTeamFolder(request?: protos.google.cloud.dataform.v1beta1.IUpdateTeamFolderRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.ITeamFolder,
            protos.google.cloud.dataform.v1beta1.IUpdateTeamFolderRequest | undefined,
            {} | undefined
        ]>;

Updates a single TeamFolder.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateteamfolderrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.ITeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iteamfolder), [protos.google.cloud.dataform.v1beta1.IUpdateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateteamfolderrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.teamfolder). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Specifies the fields to be updated in the Folder. If left unset,
       *  all fields will be updated.
       */
      // const updateMask = {}
      /**
       *  Required. The updated TeamFolder.
       */
      // const teamFolder = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callUpdateTeamFolder() {
        // Construct request
        const request = {
          teamFolder,
        };
    
        // Run request
        const response = await dataformClient.updateTeamFolder(request);
        console.log(response);
      }
    
      callUpdateTeamFolder();
    
    

### updateTeamFolder(request, options, callback)
    
    
    updateTeamFolder(request: protos.google.cloud.dataform.v1beta1.IUpdateTeamFolderRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.ITeamFolder, protos.google.cloud.dataform.v1beta1.IUpdateTeamFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateteamfolderrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ITeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iteamfolder), [protos.google.cloud.dataform.v1beta1.IUpdateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateteamfolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTeamFolder(request, callback)
    
    
    updateTeamFolder(request: protos.google.cloud.dataform.v1beta1.IUpdateTeamFolderRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.ITeamFolder, protos.google.cloud.dataform.v1beta1.IUpdateTeamFolderRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateteamfolderrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.ITeamFolder](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iteamfolder), [protos.google.cloud.dataform.v1beta1.IUpdateTeamFolderRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateteamfolderrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWorkflowConfig(request, options)
    
    
    updateWorkflowConfig(request?: protos.google.cloud.dataform.v1beta1.IUpdateWorkflowConfigRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWorkflowConfig,
            (protos.google.cloud.dataform.v1beta1.IUpdateWorkflowConfigRequest | undefined),
            {} | undefined
        ]>;

Updates a single WorkflowConfig.

**Note:** *This method does not fully implement [AIP/134](<https://google.aip.dev/134>). The wildcard entry (*) is treated as a bad request, and when the `field_mask` is omitted, the request is treated as a full update on all modifiable fields.*

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateworkflowconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig), ([protos.google.cloud.dataform.v1beta1.IUpdateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateworkflowconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Specifies the fields to be updated in the workflow config. If
       *  left unset, all fields will be updated.
       */
      // const updateMask = {}
      /**
       *  Required. The workflow config to update.
       */
      // const workflowConfig = {}
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callUpdateWorkflowConfig() {
        // Construct request
        const request = {
          workflowConfig,
        };
    
        // Run request
        const response = await dataformClient.updateWorkflowConfig(request);
        console.log(response);
      }
    
      callUpdateWorkflowConfig();
    
    

### updateWorkflowConfig(request, options, callback)
    
    
    updateWorkflowConfig(request: protos.google.cloud.dataform.v1beta1.IUpdateWorkflowConfigRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkflowConfig, protos.google.cloud.dataform.v1beta1.IUpdateWorkflowConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateworkflowconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig), [protos.google.cloud.dataform.v1beta1.IUpdateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateworkflowconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWorkflowConfig(request, callback)
    
    
    updateWorkflowConfig(request: protos.google.cloud.dataform.v1beta1.IUpdateWorkflowConfigRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IWorkflowConfig, protos.google.cloud.dataform.v1beta1.IUpdateWorkflowConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateworkflowconfigrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWorkflowConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iworkflowconfig), [protos.google.cloud.dataform.v1beta1.IUpdateWorkflowConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iupdateworkflowconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### workflowConfigPath(project, location, repository, workflowConfig)
    
    
    workflowConfigPath(project: string, location: string, repository: string, workflowConfig: string): string;

Return a fully-qualified workflowConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`repository` |  `string`   
  
`workflowConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### workflowInvocationPath(project, location, repository, workflowInvocation)
    
    
    workflowInvocationPath(project: string, location: string, repository: string, workflowInvocation: string): string;

Return a fully-qualified workflowInvocation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`repository` |  `string`   
  
`workflowInvocation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### workspacePath(project, location, repository, workspace)
    
    
    workspacePath(project: string, location: string, repository: string, workspace: string): string;

Return a fully-qualified workspace resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`repository` |  `string`   
  
`workspace` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### writeFile(request, options)
    
    
    writeFile(request?: protos.google.cloud.dataform.v1beta1.IWriteFileRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dataform.v1beta1.IWriteFileResponse,
            protos.google.cloud.dataform.v1beta1.IWriteFileRequest | undefined,
            {} | undefined
        ]>;

Writes to a file (inside a Workspace).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iwritefilerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dataform.v1beta1.IWriteFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iwritefileresponse), [protos.google.cloud.dataform.v1beta1.IWriteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iwritefilerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [WriteFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.writefileresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The workspace's name.
       */
      // const workspace = 'abc123'
      /**
       *  Required. The file.
       */
      // const path = 'abc123'
      /**
       *  Required. The file's contents.
       */
      // const contents = Buffer.from('string')
    
      // Imports the Dataform library
      const {DataformClient} = require('[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const dataformClient = new [DataformClient](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)();
    
      async function callWriteFile() {
        // Construct request
        const request = {
          workspace,
          path,
          contents,
        };
    
        // Run request
        const response = await dataformClient.writeFile(request);
        console.log(response);
      }
    
      callWriteFile();
    
    

### writeFile(request, options, callback)
    
    
    writeFile(request: protos.google.cloud.dataform.v1beta1.IWriteFileRequest, options: CallOptions, callback: Callback<protos.google.cloud.dataform.v1beta1.IWriteFileResponse, protos.google.cloud.dataform.v1beta1.IWriteFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iwritefilerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWriteFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iwritefileresponse), [protos.google.cloud.dataform.v1beta1.IWriteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iwritefilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### writeFile(request, callback)
    
    
    writeFile(request: protos.google.cloud.dataform.v1beta1.IWriteFileRequest, callback: Callback<protos.google.cloud.dataform.v1beta1.IWriteFileResponse, protos.google.cloud.dataform.v1beta1.IWriteFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IWriteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iwritefilerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dataform.v1beta1.IWriteFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iwritefileresponse), [protos.google.cloud.dataform.v1beta1.IWriteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.iwritefilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
