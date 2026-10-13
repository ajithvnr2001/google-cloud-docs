---
url: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/v1beta.backupdrclient
title: Class v1beta.BackupDRClient (0.12.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:58.727622+00:00
---

# Class v1beta.BackupDRClient (0.12.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/v1beta.backupdrclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.BackupDRClient (0.12.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.12.0  0.9.0  0.8.0  0.7.0  0.6.0  0.1.0 

The BackupDR Service v1beta

## Package

[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of BackupDRClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new BackupDRClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### backupDRStub
    
    
    backupDRStub?: Promise<{
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

### appliedAutoProtectionPolicyPath(project, location, appliedAutoProtectionPolicy)
    
    
    appliedAutoProtectionPolicyPath(project: string, location: string, appliedAutoProtectionPolicy: string): string;

Return a fully-qualified appliedAutoProtectionPolicy resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`appliedAutoProtectionPolicy` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### autoProtectionPolicyBindingPath(project, location, autoProtectionPolicy, binding)
    
    
    autoProtectionPolicyBindingPath(project: string, location: string, autoProtectionPolicy: string, binding: string): string;

Return a fully-qualified autoProtectionPolicyBinding resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`autoProtectionPolicy` |  `string`   
  
`binding` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### autoProtectionPolicyPath(project, location, autoProtectionPolicy)
    
    
    autoProtectionPolicyPath(project: string, location: string, autoProtectionPolicy: string): string;

Return a fully-qualified autoProtectionPolicy resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`autoProtectionPolicy` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### backupPath(project, location, backupvault, datasource, backup)
    
    
    backupPath(project: string, location: string, backupvault: string, datasource: string, backup: string): string;

Return a fully-qualified backup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupvault` |  `string`   
  
`datasource` |  `string`   
  
`backup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### backupPlanAssociationPath(project, location, backupPlanAssociation)
    
    
    backupPlanAssociationPath(project: string, location: string, backupPlanAssociation: string): string;

Return a fully-qualified backupPlanAssociation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupPlanAssociation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### backupPlanPath(project, location, backupPlan)
    
    
    backupPlanPath(project: string, location: string, backupPlan: string): string;

Return a fully-qualified backupPlan resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupPlan` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### backupPlanRevisionPath(project, location, backupPlan, revision)
    
    
    backupPlanRevisionPath(project: string, location: string, backupPlan: string, revision: string): string;

Return a fully-qualified backupPlanRevision resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupPlan` |  `string`   
  
`revision` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### backupVaultPath(project, location, backupvault)
    
    
    backupVaultPath(project: string, location: string, backupvault: string): string;

Return a fully-qualified backupVault resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupvault` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### bindingMatchingResourcePath(project, location, autoProtectionPolicy, binding, matchingResource)
    
    
    bindingMatchingResourcePath(project: string, location: string, autoProtectionPolicy: string, binding: string, matchingResource: string): string;

Return a fully-qualified bindingMatchingResource resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`autoProtectionPolicy` |  `string`   
  
`binding` |  `string`   
  
`matchingResource` |  `string`   
  
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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreateAutoProtectionPolicyBindingProgress(name)
    
    
    checkCreateAutoProtectionPolicyBindingProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.AutoProtectionPolicyBinding, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createAutoProtectionPolicyBinding()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.AutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.autoprotectionpolicybinding-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this binding will be created.
       *  Format:
       *  projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID to use for the binding.
       *  This will become the final component of the binding's resource name.
       */
      // const autoProtectionPolicyBindingId = 'abc123'
      /**
       *  Required. The AutoProtectionPolicyBinding resource to create.
       */
      // const autoProtectionPolicyBinding = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateAutoProtectionPolicyBinding() {
        // Construct request
        const request = {
          parent,
          autoProtectionPolicyBindingId,
          autoProtectionPolicyBinding,
        };
    
        // Run request
        const [operation] = await backupdrClient.createAutoProtectionPolicyBinding(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateAutoProtectionPolicyBinding();
    
    

### checkCreateAutoProtectionPolicyProgress(name)
    
    
    checkCreateAutoProtectionPolicyProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.AutoProtectionPolicy, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createAutoProtectionPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.AutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.autoprotectionpolicy-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this policy will be created.
       *  Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID to use for the policy.
       *  This will become the final component of the policy's resource name.
       */
      // const autoProtectionPolicyId = 'abc123'
      /**
       *  Required. The AutoProtectionPolicy resource to create.
       */
      // const autoProtectionPolicy = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateAutoProtectionPolicy() {
        // Construct request
        const request = {
          parent,
          autoProtectionPolicyId,
          autoProtectionPolicy,
        };
    
        // Run request
        const [operation] = await backupdrClient.createAutoProtectionPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateAutoProtectionPolicy();
    
    

### checkCreateBackupPlanAssociationProgress(name)
    
    
    checkCreateBackupPlanAssociationProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.BackupPlanAssociation, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createBackupPlanAssociation()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.BackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.backupplanassociation-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The backup plan association project and location in the format
       *  `projects/{project_id}/locations/{location}`. In Backup and DR locations
       *  map to Google Cloud regions, for example **us-central1**.
       */
      // const parent = 'abc123'
      /**
       *  Required. The name of the backup plan association to create. The name must
       *  be unique for the specified project and location.
       */
      // const backupPlanAssociationId = 'abc123'
      /**
       *  Required. The resource being created
       */
      // const backupPlanAssociation = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateBackupPlanAssociation() {
        // Construct request
        const request = {
          parent,
          backupPlanAssociationId,
          backupPlanAssociation,
        };
    
        // Run request
        const [operation] = await backupdrClient.createBackupPlanAssociation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateBackupPlanAssociation();
    
    

### checkCreateBackupPlanProgress(name)
    
    
    checkCreateBackupPlanProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.BackupPlan, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createBackupPlan()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.BackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.backupplan-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The `BackupPlan` project and location in the format
       *  `projects/{project}/locations/{location}`. In Google Cloud Backup and DR
       *  locations map to Google Cloud regions, for example **us-central1**.
       */
      // const parent = 'abc123'
      /**
       *  Required. The name of the `BackupPlan` to create. The name must be unique
       *  for the specified project and location.The name must start with a lowercase
       *  letter followed by up to 62 lowercase letters, numbers, or hyphens.
       *  Pattern, /[a-z][a-z0-9-]{,62}/.
       */
      // const backupPlanId = 'abc123'
      /**
       *  Required. The `BackupPlan` resource object to create.
       */
      // const backupPlan = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateBackupPlan() {
        // Construct request
        const request = {
          parent,
          backupPlanId,
          backupPlan,
        };
    
        // Run request
        const [operation] = await backupdrClient.createBackupPlan(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateBackupPlan();
    
    

### checkCreateBackupVaultProgress(name)
    
    
    checkCreateBackupVaultProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.BackupVault, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createBackupVault()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.BackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.backupvault-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Value for parent.
       */
      // const parent = 'abc123'
      /**
       *  Required. ID of the requesting object
       *  If auto-generating ID server-side, remove this field and
       *  backup_vault_id from the method_signature of Create RPC
       */
      // const backupVaultId = 'abc123'
      /**
       *  Required. The resource being created
       */
      // const backupVault = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. Only validate the request, but do not perform mutations.
       *  The default is 'false'.
       */
      // const validateOnly = true
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateBackupVault() {
        // Construct request
        const request = {
          parent,
          backupVaultId,
          backupVault,
        };
    
        // Run request
        const [operation] = await backupdrClient.createBackupVault(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateBackupVault();
    
    

### checkCreateManagementServerProgress(name)
    
    
    checkCreateManagementServerProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.ManagementServer, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createManagementServer()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.ManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.managementserver-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The management server project and location in the format
       *  'projects/{project_id}/locations/{location}'. In Google Cloud Backup and DR
       *  locations map to Google Cloud regions, for example **us-central1**.
       */
      // const parent = 'abc123'
      /**
       *  Required. The name of the management server to create. The name must be
       *  unique for the specified project and location.
       */
      // const managementServerId = 'abc123'
      /**
       *  Required. A management server
       *  resource google.cloud.backupdr.v1.ManagementServer 
       */
      // const managementServer = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateManagementServer() {
        // Construct request
        const request = {
          parent,
          managementServerId,
          managementServer,
        };
    
        // Run request
        const [operation] = await backupdrClient.createManagementServer(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateManagementServer();
    
    

### checkDeleteAutoProtectionPolicyProgress(name)
    
    
    checkDeleteAutoProtectionPolicyProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deleteAutoProtectionPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the policy to delete.
       *  Format:
       *  projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
       */
      // const name = 'abc123'
      /**
       *  The current etag of the AutoProtectionPolicy.
       *  If an etag is provided and does not match the current etag of the
       *  connection, the request will be rejected with an ABORTED error.
       */
      // const etag = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteAutoProtectionPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteAutoProtectionPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteAutoProtectionPolicy();
    
    

### checkDeleteBackupPlanAssociationProgress(name)
    
    
    checkDeleteBackupPlanAssociationProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deleteBackupPlanAssociation()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the backup plan association resource, in the format
       *  `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. This field is exclusively used by Backup and DR's auto-protection
       *  feature. The resource name of the `AutoProtectionPolicyBinding` that
       *  triggered the deletion of this association.
       *  Format:
       *  `projects/{project}/locations/{location}/autoProtectionPolicies/{policy}/bindings/{binding}`.
       */
      // const autoProtectionPolicyBinding = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteBackupPlanAssociation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteBackupPlanAssociation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteBackupPlanAssociation();
    
    

### checkDeleteBackupPlanProgress(name)
    
    
    checkDeleteBackupPlanProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deleteBackupPlan()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the `BackupPlan` to delete.
       *  Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteBackupPlan() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteBackupPlan(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteBackupPlan();
    
    

### checkDeleteBackupProgress(name)
    
    
    checkDeleteBackupProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.Backup, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deleteBackup()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.Backup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.backup-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteBackup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteBackup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteBackup();
    
    

### checkDeleteBackupVaultProgress(name)
    
    
    checkDeleteBackupVaultProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deleteBackupVault()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. If set to true, any data source from this backup vault will also
       *  be deleted.
       */
      // const force = true
      /**
       *  The current etag of the backup vault.
       *  If an etag is provided and does not match the current etag of the
       *  connection, deletion will be blocked.
       */
      // const etag = 'abc123'
      /**
       *  Optional. Only validate the request, but do not perform mutations.
       *  The default is 'false'.
       */
      // const validateOnly = true
      /**
       *  Optional. If true and the BackupVault is not found, the request will
       *  succeed but no action will be taken.
       */
      // const allowMissing = true
      /**
       *  Optional. If set to true, backupvault deletion will proceed even if there
       *  are backup plans referencing the backupvault. The default is 'false'.
       */
      // const ignoreBackupPlanReferences = true
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteBackupVault() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteBackupVault(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteBackupVault();
    
    

### checkDeleteManagementServerProgress(name)
    
    
    checkDeleteManagementServerProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deleteManagementServer()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteManagementServer() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteManagementServer(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteManagementServer();
    
    

### checkInitializeServiceProgress(name)
    
    
    checkInitializeServiceProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.InitializeServiceResponse, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `initializeService()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.InitializeServiceResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.initializeserviceresponse), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The configuration for initializing a Cloud SQL instance.
       */
      // const cloudSqlInstanceInitializationConfig = {}
      /**
       *  Required. The resource name of the serviceConfig used to initialize the
       *  service. The location must be the location of the BackupVault.
       *  Format: `projects/{project_id}/locations/{location}/serviceConfig`.
       */
      // const name = 'abc123'
      /**
       *  Required. The resource type to which the default service config will be
       *  applied. Examples include, "compute.googleapis.com/Instance" and
       *  "storage.googleapis.com/Bucket".
       */
      // const resourceType = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. The location where the BackupPlan will be created. This field is
       *  required for multi-region BackupVaults and is optional for regional
       *  BackupVaults. It is useful when creating a Backup Vault in a multi-region,
       *  allowing the BackupPlan to reside in a specific region within that
       *  multi-region. If this field is not provided, the BackupPlan will be created
       *  in the same location as specified in the `name` field.
       */
      // const backupPlanLocation = 'abc123'
      /**
       *  Optional. If set, validates the request and returns the result, but does
       *  not actually run it.
       */
      // const validateOnly = true
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callInitializeService() {
        // Construct request
        const request = {
          name,
          resourceType,
        };
    
        // Run request
        const [operation] = await backupdrClient.initializeService(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callInitializeService();
    
    

### checkInitiateDeleteAutoProtectionPolicyBindingProgress(name)
    
    
    checkInitiateDeleteAutoProtectionPolicyBindingProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.AutoProtectionPolicyBinding, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `initiateDeleteAutoProtectionPolicyBinding()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.AutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.autoprotectionpolicybinding-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the binding to delete.
       *  Format:
       *  projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callInitiateDeleteAutoProtectionPolicyBinding() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.initiateDeleteAutoProtectionPolicyBinding(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callInitiateDeleteAutoProtectionPolicyBinding();
    
    

### checkRestoreBackupProgress(name)
    
    
    checkRestoreBackupProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.RestoreBackupResponse, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `restoreBackup()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.RestoreBackupResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.restorebackupresponse), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Compute Engine target environment to be used during restore.
       */
      // const computeInstanceTargetEnvironment = {}
      /**
       *  Disk target environment to be used during restore.
       */
      // const diskTargetEnvironment = {}
      /**
       *  Region disk target environment to be used during restore.
       */
      // const regionDiskTargetEnvironment = {}
      /**
       *  Compute Engine instance properties to be overridden during restore.
       */
      // const computeInstanceRestoreProperties = {}
      /**
       *  Disk properties to be overridden during restore.
       */
      // const diskRestoreProperties = {}
      /**
       *  Required. The resource name of the Backup instance, in the format
       *  'projects/* /locations/* /backupVaults/* /dataSources/* /backups/'.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. A field mask used to clear server-side default values
       *  for fields within the `instance_properties` oneof.
       *  When a field in this mask is cleared, the server will not apply its
       *  default logic (like inheriting a value from the source) for that field.
       *  The most common current use case is clearing default encryption keys.
       *  Examples of field mask paths:
       *  - Compute Instance Disks:
       *  `compute_instance_restore_properties.disks.*.disk_encryption_key`
       *  - Single Disk: `disk_restore_properties.disk_encryption_key`
       */
      // const clearOverridesFieldMask = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callRestoreBackup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.restoreBackup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRestoreBackup();
    
    

### checkTriggerBackupProgress(name)
    
    
    checkTriggerBackupProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.BackupPlanAssociation, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `triggerBackup()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.BackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.backupplanassociation-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the backup plan association resource, in the format
       *  `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`
       */
      // const name = 'abc123'
      /**
       *  Optional. backup rule_id for which a backup needs to be triggered.
       *  If not specified, on-demand backup with custom retention will be triggered.
       */
      // const ruleId = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. The duration for which backup data will be kept, while taking an
       *  on-demand backup with custom retention. It is defined in "days".
       *  It is mutually exclusive with rule_id. This field is required if
       *  rule_id is not provided.
       */
      // const customRetentionDays = 1234
      /**
       *  Optional. Labels to be applied on the backup.
       */
      // const labels = [1,2,3,4]
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callTriggerBackup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.triggerBackup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callTriggerBackup();
    
    

### checkUpdateAutoProtectionPolicyProgress(name)
    
    
    checkUpdateAutoProtectionPolicyProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.AutoProtectionPolicy, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `updateAutoProtectionPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.AutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.autoprotectionpolicy-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The policy to update.
       */
      // const autoProtectionPolicy = {}
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  AutoProtectionPolicy resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateAutoProtectionPolicy() {
        // Construct request
        const request = {
          autoProtectionPolicy,
          updateMask,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateAutoProtectionPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateAutoProtectionPolicy();
    
    

### checkUpdateBackupPlanAssociationProgress(name)
    
    
    checkUpdateBackupPlanAssociationProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.BackupPlanAssociation, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `updateBackupPlanAssociation()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.BackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.backupplanassociation-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource being updated
       */
      // const backupPlanAssociation = {}
      /**
       *  Required. The list of fields to update.
       *  Field mask is used to specify the fields to be overwritten in the
       *  BackupPlanAssociation resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then the request will fail.
       *  Currently backup_plan_association.backup_plan is the only supported field.
       */
      // const updateMask = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateBackupPlanAssociation() {
        // Construct request
        const request = {
          backupPlanAssociation,
          updateMask,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateBackupPlanAssociation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateBackupPlanAssociation();
    
    

### checkUpdateBackupPlanProgress(name)
    
    
    checkUpdateBackupPlanProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.BackupPlan, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `updateBackupPlan()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.BackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.backupplan-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource being updated
       */
      // const backupPlan = {}
      /**
       *  Required. The list of fields to update.
       *  Field mask is used to specify the fields to be overwritten in the
       *  BackupPlan resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then the request will fail.
       *  Currently, these fields are supported in update: description, schedules,
       *  retention period, adding and removing Backup Rules.
       */
      // const updateMask = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateBackupPlan() {
        // Construct request
        const request = {
          backupPlan,
          updateMask,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateBackupPlan(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateBackupPlan();
    
    

### checkUpdateBackupProgress(name)
    
    
    checkUpdateBackupProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.Backup, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `updateBackup()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.Backup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.backup-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  Backup resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then the request will fail.
       */
      // const updateMask = {}
      /**
       *  Required. The resource being updated
       */
      // const backup = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateBackup() {
        // Construct request
        const request = {
          updateMask,
          backup,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateBackup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateBackup();
    
    

### checkUpdateBackupVaultProgress(name)
    
    
    checkUpdateBackupVaultProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.BackupVault, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `updateBackupVault()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.BackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.backupvault-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  BackupVault resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then the request will fail.
       */
      // const updateMask = {}
      /**
       *  Required. The resource being updated
       */
      // const backupVault = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. Only validate the request, but do not perform mutations.
       *  The default is 'false'.
       */
      // const validateOnly = true
      /**
       *  Optional. If set to true, will not check plan duration against backup vault
       *  enforcement duration.
       */
      // const force = true
      /**
       *  Optional. If set to true, we will force update access restriction even if
       *  some non compliant data sources are present. The default is 'false'.
       */
      // const forceUpdateAccessRestriction = true
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateBackupVault() {
        // Construct request
        const request = {
          updateMask,
          backupVault,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateBackupVault(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateBackupVault();
    
    

### checkUpdateDataSourceProgress(name)
    
    
    checkUpdateDataSourceProgress(name: string): Promise<LROperation<protos.google.cloud.backupdr.v1beta.DataSource, protos.google.cloud.backupdr.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `updateDataSource()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.backupdr.v1beta.DataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.datasource-class), [protos.google.cloud.backupdr.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  DataSource resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then the request will fail.
       */
      // const updateMask = {}
      /**
       *  Required. The resource being updated
       */
      // const dataSource = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. Enable upsert.
       */
      // const allowMissing = true
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateDataSource() {
        // Construct request
        const request = {
          updateMask,
          dataSource,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateDataSource(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateDataSource();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createAutoProtectionPolicy(request, options)
    
    
    createAutoProtectionPolicy(request?: protos.google.cloud.backupdr.v1beta.ICreateAutoProtectionPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new AutoProtectionPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreateautoprotectionpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this policy will be created.
       *  Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID to use for the policy.
       *  This will become the final component of the policy's resource name.
       */
      // const autoProtectionPolicyId = 'abc123'
      /**
       *  Required. The AutoProtectionPolicy resource to create.
       */
      // const autoProtectionPolicy = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateAutoProtectionPolicy() {
        // Construct request
        const request = {
          parent,
          autoProtectionPolicyId,
          autoProtectionPolicy,
        };
    
        // Run request
        const [operation] = await backupdrClient.createAutoProtectionPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateAutoProtectionPolicy();
    
    

### createAutoProtectionPolicy(request, options, callback)
    
    
    createAutoProtectionPolicy(request: protos.google.cloud.backupdr.v1beta.ICreateAutoProtectionPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreateautoprotectionpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAutoProtectionPolicy(request, callback)
    
    
    createAutoProtectionPolicy(request: protos.google.cloud.backupdr.v1beta.ICreateAutoProtectionPolicyRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreateautoprotectionpolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAutoProtectionPolicyBinding(request, options)
    
    
    createAutoProtectionPolicyBinding(request?: protos.google.cloud.backupdr.v1beta.ICreateAutoProtectionPolicyBindingRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new AutoProtectionPolicyBinding in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreateautoprotectionpolicybindingrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource where this binding will be created.
       *  Format:
       *  projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID to use for the binding.
       *  This will become the final component of the binding's resource name.
       */
      // const autoProtectionPolicyBindingId = 'abc123'
      /**
       *  Required. The AutoProtectionPolicyBinding resource to create.
       */
      // const autoProtectionPolicyBinding = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateAutoProtectionPolicyBinding() {
        // Construct request
        const request = {
          parent,
          autoProtectionPolicyBindingId,
          autoProtectionPolicyBinding,
        };
    
        // Run request
        const [operation] = await backupdrClient.createAutoProtectionPolicyBinding(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateAutoProtectionPolicyBinding();
    
    

### createAutoProtectionPolicyBinding(request, options, callback)
    
    
    createAutoProtectionPolicyBinding(request: protos.google.cloud.backupdr.v1beta.ICreateAutoProtectionPolicyBindingRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreateautoprotectionpolicybindingrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAutoProtectionPolicyBinding(request, callback)
    
    
    createAutoProtectionPolicyBinding(request: protos.google.cloud.backupdr.v1beta.ICreateAutoProtectionPolicyBindingRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreateautoprotectionpolicybindingrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBackupPlan(request, options)
    
    
    createBackupPlan(request?: protos.google.cloud.backupdr.v1beta.ICreateBackupPlanRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlan, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Create a BackupPlan

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatebackupplanrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The `BackupPlan` project and location in the format
       *  `projects/{project}/locations/{location}`. In Google Cloud Backup and DR
       *  locations map to Google Cloud regions, for example **us-central1**.
       */
      // const parent = 'abc123'
      /**
       *  Required. The name of the `BackupPlan` to create. The name must be unique
       *  for the specified project and location.The name must start with a lowercase
       *  letter followed by up to 62 lowercase letters, numbers, or hyphens.
       *  Pattern, /[a-z][a-z0-9-]{,62}/.
       */
      // const backupPlanId = 'abc123'
      /**
       *  Required. The `BackupPlan` resource object to create.
       */
      // const backupPlan = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateBackupPlan() {
        // Construct request
        const request = {
          parent,
          backupPlanId,
          backupPlan,
        };
    
        // Run request
        const [operation] = await backupdrClient.createBackupPlan(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateBackupPlan();
    
    

### createBackupPlan(request, options, callback)
    
    
    createBackupPlan(request: protos.google.cloud.backupdr.v1beta.ICreateBackupPlanRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlan, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatebackupplanrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBackupPlan(request, callback)
    
    
    createBackupPlan(request: protos.google.cloud.backupdr.v1beta.ICreateBackupPlanRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlan, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatebackupplanrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBackupPlanAssociation(request, options)
    
    
    createBackupPlanAssociation(request?: protos.google.cloud.backupdr.v1beta.ICreateBackupPlanAssociationRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Create a BackupPlanAssociation

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatebackupplanassociationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The backup plan association project and location in the format
       *  `projects/{project_id}/locations/{location}`. In Backup and DR locations
       *  map to Google Cloud regions, for example **us-central1**.
       */
      // const parent = 'abc123'
      /**
       *  Required. The name of the backup plan association to create. The name must
       *  be unique for the specified project and location.
       */
      // const backupPlanAssociationId = 'abc123'
      /**
       *  Required. The resource being created
       */
      // const backupPlanAssociation = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateBackupPlanAssociation() {
        // Construct request
        const request = {
          parent,
          backupPlanAssociationId,
          backupPlanAssociation,
        };
    
        // Run request
        const [operation] = await backupdrClient.createBackupPlanAssociation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateBackupPlanAssociation();
    
    

### createBackupPlanAssociation(request, options, callback)
    
    
    createBackupPlanAssociation(request: protos.google.cloud.backupdr.v1beta.ICreateBackupPlanAssociationRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatebackupplanassociationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBackupPlanAssociation(request, callback)
    
    
    createBackupPlanAssociation(request: protos.google.cloud.backupdr.v1beta.ICreateBackupPlanAssociationRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatebackupplanassociationrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBackupVault(request, options)
    
    
    createBackupVault(request?: protos.google.cloud.backupdr.v1beta.ICreateBackupVaultRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IBackupVault, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new BackupVault in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatebackupvaultrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Value for parent.
       */
      // const parent = 'abc123'
      /**
       *  Required. ID of the requesting object
       *  If auto-generating ID server-side, remove this field and
       *  backup_vault_id from the method_signature of Create RPC
       */
      // const backupVaultId = 'abc123'
      /**
       *  Required. The resource being created
       */
      // const backupVault = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. Only validate the request, but do not perform mutations.
       *  The default is 'false'.
       */
      // const validateOnly = true
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateBackupVault() {
        // Construct request
        const request = {
          parent,
          backupVaultId,
          backupVault,
        };
    
        // Run request
        const [operation] = await backupdrClient.createBackupVault(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateBackupVault();
    
    

### createBackupVault(request, options, callback)
    
    
    createBackupVault(request: protos.google.cloud.backupdr.v1beta.ICreateBackupVaultRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupVault, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatebackupvaultrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBackupVault(request, callback)
    
    
    createBackupVault(request: protos.google.cloud.backupdr.v1beta.ICreateBackupVaultRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupVault, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatebackupvaultrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createManagementServer(request, options)
    
    
    createManagementServer(request?: protos.google.cloud.backupdr.v1beta.ICreateManagementServerRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IManagementServer, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new ManagementServer in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatemanagementserverrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The management server project and location in the format
       *  'projects/{project_id}/locations/{location}'. In Google Cloud Backup and DR
       *  locations map to Google Cloud regions, for example **us-central1**.
       */
      // const parent = 'abc123'
      /**
       *  Required. The name of the management server to create. The name must be
       *  unique for the specified project and location.
       */
      // const managementServerId = 'abc123'
      /**
       *  Required. A management server
       *  resource google.cloud.backupdr.v1.ManagementServer 
       */
      // const managementServer = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callCreateManagementServer() {
        // Construct request
        const request = {
          parent,
          managementServerId,
          managementServer,
        };
    
        // Run request
        const [operation] = await backupdrClient.createManagementServer(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateManagementServer();
    
    

### createManagementServer(request, options, callback)
    
    
    createManagementServer(request: protos.google.cloud.backupdr.v1beta.ICreateManagementServerRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IManagementServer, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatemanagementserverrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createManagementServer(request, callback)
    
    
    createManagementServer(request: protos.google.cloud.backupdr.v1beta.ICreateManagementServerRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IManagementServer, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.icreatemanagementserverrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### dataSourcePath(project, location, backupvault, datasource)
    
    
    dataSourcePath(project: string, location: string, backupvault: string, datasource: string): string;

Return a fully-qualified dataSource resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backupvault` |  `string`   
  
`datasource` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### dataSourceReferencePath(project, location, dataSourceReference)
    
    
    dataSourceReferencePath(project: string, location: string, dataSourceReference: string): string;

Return a fully-qualified dataSourceReference resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataSourceReference` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteAutoProtectionPolicy(request, options)
    
    
    deleteAutoProtectionPolicy(request?: protos.google.cloud.backupdr.v1beta.IDeleteAutoProtectionPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single AutoProtectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideleteautoprotectionpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the policy to delete.
       *  Format:
       *  projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
       */
      // const name = 'abc123'
      /**
       *  The current etag of the AutoProtectionPolicy.
       *  If an etag is provided and does not match the current etag of the
       *  connection, the request will be rejected with an ABORTED error.
       */
      // const etag = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteAutoProtectionPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteAutoProtectionPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteAutoProtectionPolicy();
    
    

### deleteAutoProtectionPolicy(request, options, callback)
    
    
    deleteAutoProtectionPolicy(request: protos.google.cloud.backupdr.v1beta.IDeleteAutoProtectionPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideleteautoprotectionpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAutoProtectionPolicy(request, callback)
    
    
    deleteAutoProtectionPolicy(request: protos.google.cloud.backupdr.v1beta.IDeleteAutoProtectionPolicyRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideleteautoprotectionpolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackup(request, options)
    
    
    deleteBackup(request?: protos.google.cloud.backupdr.v1beta.IDeleteBackupRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IBackup, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackuprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteBackup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteBackup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteBackup();
    
    

### deleteBackup(request, options, callback)
    
    
    deleteBackup(request: protos.google.cloud.backupdr.v1beta.IDeleteBackupRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackup, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackuprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackup(request, callback)
    
    
    deleteBackup(request: protos.google.cloud.backupdr.v1beta.IDeleteBackupRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackup, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackuprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackupPlan(request, options)
    
    
    deleteBackupPlan(request?: protos.google.cloud.backupdr.v1beta.IDeleteBackupPlanRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single BackupPlan.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackupplanrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the `BackupPlan` to delete.
       *  Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteBackupPlan() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteBackupPlan(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteBackupPlan();
    
    

### deleteBackupPlan(request, options, callback)
    
    
    deleteBackupPlan(request: protos.google.cloud.backupdr.v1beta.IDeleteBackupPlanRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackupplanrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackupPlan(request, callback)
    
    
    deleteBackupPlan(request: protos.google.cloud.backupdr.v1beta.IDeleteBackupPlanRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackupplanrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackupPlanAssociation(request, options)
    
    
    deleteBackupPlanAssociation(request?: protos.google.cloud.backupdr.v1beta.IDeleteBackupPlanAssociationRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single BackupPlanAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackupplanassociationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the backup plan association resource, in the format
       *  `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. This field is exclusively used by Backup and DR's auto-protection
       *  feature. The resource name of the `AutoProtectionPolicyBinding` that
       *  triggered the deletion of this association.
       *  Format:
       *  `projects/{project}/locations/{location}/autoProtectionPolicies/{policy}/bindings/{binding}`.
       */
      // const autoProtectionPolicyBinding = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteBackupPlanAssociation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteBackupPlanAssociation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteBackupPlanAssociation();
    
    

### deleteBackupPlanAssociation(request, options, callback)
    
    
    deleteBackupPlanAssociation(request: protos.google.cloud.backupdr.v1beta.IDeleteBackupPlanAssociationRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackupplanassociationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackupPlanAssociation(request, callback)
    
    
    deleteBackupPlanAssociation(request: protos.google.cloud.backupdr.v1beta.IDeleteBackupPlanAssociationRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackupplanassociationrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackupVault(request, options)
    
    
    deleteBackupVault(request?: protos.google.cloud.backupdr.v1beta.IDeleteBackupVaultRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a BackupVault.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackupvaultrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. If set to true, any data source from this backup vault will also
       *  be deleted.
       */
      // const force = true
      /**
       *  The current etag of the backup vault.
       *  If an etag is provided and does not match the current etag of the
       *  connection, deletion will be blocked.
       */
      // const etag = 'abc123'
      /**
       *  Optional. Only validate the request, but do not perform mutations.
       *  The default is 'false'.
       */
      // const validateOnly = true
      /**
       *  Optional. If true and the BackupVault is not found, the request will
       *  succeed but no action will be taken.
       */
      // const allowMissing = true
      /**
       *  Optional. If set to true, backupvault deletion will proceed even if there
       *  are backup plans referencing the backupvault. The default is 'false'.
       */
      // const ignoreBackupPlanReferences = true
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteBackupVault() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteBackupVault(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteBackupVault();
    
    

### deleteBackupVault(request, options, callback)
    
    
    deleteBackupVault(request: protos.google.cloud.backupdr.v1beta.IDeleteBackupVaultRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackupvaultrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBackupVault(request, callback)
    
    
    deleteBackupVault(request: protos.google.cloud.backupdr.v1beta.IDeleteBackupVaultRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletebackupvaultrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteManagementServer(request, options)
    
    
    deleteManagementServer(request?: protos.google.cloud.backupdr.v1beta.IDeleteManagementServerRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single ManagementServer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletemanagementserverrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callDeleteManagementServer() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.deleteManagementServer(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteManagementServer();
    
    

### deleteManagementServer(request, options, callback)
    
    
    deleteManagementServer(request: protos.google.cloud.backupdr.v1beta.IDeleteManagementServerRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletemanagementserverrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteManagementServer(request, callback)
    
    
    deleteManagementServer(request: protos.google.cloud.backupdr.v1beta.IDeleteManagementServerRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ideletemanagementserverrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.iempty), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### fetchBackupPlanAssociationsForResourceType(request, options)
    
    
    fetchBackupPlanAssociationsForResourceType(request?: protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation[],
            protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest | null,
            protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeResponse
        ]>;

List BackupPlanAssociations for a given resource type.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation)[], [protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperequest) | null, [protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperesponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `fetchBackupPlanAssociationsForResourceTypeAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchBackupPlanAssociationsForResourceType(request, options, callback)
    
    
    fetchBackupPlanAssociationsForResourceType(request: protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest, protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperequest), [protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperesponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchBackupPlanAssociationsForResourceType(request, callback)
    
    
    fetchBackupPlanAssociationsForResourceType(request: protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest, protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperequest), [protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperesponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchBackupPlanAssociationsForResourceTypeAsync(request, options)
    
    
    fetchBackupPlanAssociationsForResourceTypeAsync(request?: protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation>;

Equivalent to `fetchBackupPlanAssociationsForResourceType`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name.
       *  Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Required. The type of the Google Cloud resource.
       *  Ex: sql.googleapis.com/Instance
       */
      // const resourceType = 'abc123'
      /**
       *  Optional. The maximum number of BackupPlanAssociations to return. The
       *  service may return fewer than this value. If unspecified, at most 50
       *  BackupPlanAssociations will be returned. The maximum value is 100; values
       *  above 100 will be coerced to 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous call of
       *  `FetchBackupPlanAssociationsForResourceType`.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `FetchBackupPlanAssociationsForResourceType` must match
       *  the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A filter expression that filters the results fetched in the
       *  response. The expression must specify the field name, a comparison
       *  operator, and the value that you want to use for filtering. Supported
       *  fields:
       *  * resource
       *  * backup_plan
       *  * state
       *  * data_source
       *  * cloud_sql_instance_backup_plan_association_properties.instance_create_time
       */
      // const filter = 'abc123'
      /**
       *  Optional. A comma-separated list of fields to order by, sorted in ascending
       *  order. Use "desc" after a field name for descending.
       *  Supported fields:
       *  * name
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callFetchBackupPlanAssociationsForResourceType() {
        // Construct request
        const request = {
          parent,
          resourceType,
        };
    
        // Run request
        const iterable = backupdrClient.fetchBackupPlanAssociationsForResourceTypeAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callFetchBackupPlanAssociationsForResourceType();
    
    

### fetchBackupPlanAssociationsForResourceTypeStream(request, options)
    
    
    fetchBackupPlanAssociationsForResourceTypeStream(request?: protos.google.cloud.backupdr.v1beta.IFetchBackupPlanAssociationsForResourceTypeRequest, options?: CallOptions): Transform;

Equivalent to `fetchBackupPlanAssociationsForResourceType`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupplanassociationsforresourcetyperequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `fetchBackupPlanAssociationsForResourceTypeAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchBackupsForResourceType(request, options)
    
    
    fetchBackupsForResourceType(request?: protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackup[],
            protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest | null,
            protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeResponse
        ]>;

Fetch Backups for a given resource type.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup)[], [protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperequest) | null, [protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperesponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `fetchBackupsForResourceTypeAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchBackupsForResourceType(request, options, callback)
    
    
    fetchBackupsForResourceType(request: protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest, protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperequest), [protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperesponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchBackupsForResourceType(request, callback)
    
    
    fetchBackupsForResourceType(request: protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest, protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperequest), [protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperesponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchBackupsForResourceTypeAsync(request, options)
    
    
    fetchBackupsForResourceTypeAsync(request?: protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IBackup>;

Equivalent to `fetchBackupsForResourceType`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Datasources are the parent resource for the backups.
       *  Format:
       *  projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId}
       */
      // const parent = 'abc123'
      /**
       *  Required. The type of the GCP resource.
       *  Ex: sqladmin.googleapis.com/Instance
       */
      // const resourceType = 'abc123'
      /**
       *  Optional. The maximum number of Backups to return. The service may
       *  return fewer than this value. If unspecified, at most 50
       *  Backups will be returned. The maximum value is 100; values
       *  above 100 will be coerced to 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous call of
       *  `FetchBackupsForResourceType`.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `FetchBackupsForResourceType` must match
       *  the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A filter expression that filters the results fetched in the
       *  response. The expression must specify the field name, a comparison
       *  operator, and the value that you want to use for filtering. Supported
       *  fields:
       *  * name
       *  * state
       *  * backup_type
       *  * create_time
       *  * expire_time
       *  * enforced_retention_end_time
       *  * gcp_backup_plan_info.backup_plan
       *  * cloud_sql_instance_backup_properties.instance_tier
       *  * cloud_sql_instance_backup_properties.database_installed_version
       */
      // const filter = 'abc123'
      /**
       *  Optional. A comma-separated list of fields to order by, sorted in ascending
       *  order. Use "desc" after a field name for descending.
       *  Supported fields:
       *  * name
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. This parameter is used to specify the view of the backup.
       *  If not specified, the default view is BASIC.
       */
      // const view = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callFetchBackupsForResourceType() {
        // Construct request
        const request = {
          parent,
          resourceType,
        };
    
        // Run request
        const iterable = backupdrClient.fetchBackupsForResourceTypeAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callFetchBackupsForResourceType();
    
    

### fetchBackupsForResourceTypeStream(request, options)
    
    
    fetchBackupsForResourceTypeStream(request?: protos.google.cloud.backupdr.v1beta.IFetchBackupsForResourceTypeRequest, options?: CallOptions): Transform;

Equivalent to `fetchBackupsForResourceType`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchbackupsforresourcetyperequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `fetchBackupsForResourceTypeAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchDataSourceReferencesForResourceType(request, options)
    
    
    fetchDataSourceReferencesForResourceType(request?: protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IDataSourceReference[],
            protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest | null,
            protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeResponse
        ]>;

Fetch DataSourceReferences for a given project, location and resource type.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference)[], [protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperequest) | null, [protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperesponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [DataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.datasourcereference). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `fetchDataSourceReferencesForResourceTypeAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchDataSourceReferencesForResourceType(request, options, callback)
    
    
    fetchDataSourceReferencesForResourceType(request: protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest, protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IDataSourceReference>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperequest), [protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperesponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchDataSourceReferencesForResourceType(request, callback)
    
    
    fetchDataSourceReferencesForResourceType(request: protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest, protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IDataSourceReference>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperequest), [protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperesponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchDataSourceReferencesForResourceTypeAsync(request, options)
    
    
    fetchDataSourceReferencesForResourceTypeAsync(request?: protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IDataSourceReference>;

Equivalent to `fetchDataSourceReferencesForResourceType`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [DataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.datasourcereference). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name.
       *  Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Required. The type of the Google Cloud resource.
       *  Ex: sql.googleapis.com/Instance
       */
      // const resourceType = 'abc123'
      /**
       *  Optional. The maximum number of DataSourceReferences to return. The service
       *  may return fewer than this value. If unspecified, at most 50
       *  DataSourceReferences will be returned. The maximum value is 100; values
       *  above 100 will be coerced to 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous call of
       *  `FetchDataSourceReferencesForResourceType`.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `FetchDataSourceReferencesForResourceType` must match
       *  the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A filter expression that filters the results fetched in the
       *  response. The expression must specify the field name, a comparison
       *  operator, and the value that you want to use for filtering. Supported
       *  fields:
       *  * data_source
       *  * data_source_gcp_resource_info.gcp_resourcename
       *  * data_source_backup_config_state
       *  * data_source_backup_count
       *  * data_source_backup_config_info.last_backup_state
       *  * data_source_gcp_resource_info.gcp_resourcename
       *  * data_source_gcp_resource_info.type
       *  * data_source_gcp_resource_info.location
       *  * data_source_gcp_resource_info.cloud_sql_instance_properties.instance_create_time
       */
      // const filter = 'abc123'
      /**
       *  Optional. A comma-separated list of fields to order by, sorted in ascending
       *  order. Use "desc" after a field name for descending.
       *  Supported fields:
       *  * name
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callFetchDataSourceReferencesForResourceType() {
        // Construct request
        const request = {
          parent,
          resourceType,
        };
    
        // Run request
        const iterable = backupdrClient.fetchDataSourceReferencesForResourceTypeAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callFetchDataSourceReferencesForResourceType();
    
    

### fetchDataSourceReferencesForResourceTypeStream(request, options)
    
    
    fetchDataSourceReferencesForResourceTypeStream(request?: protos.google.cloud.backupdr.v1beta.IFetchDataSourceReferencesForResourceTypeRequest, options?: CallOptions): Transform;

Equivalent to `fetchDataSourceReferencesForResourceType`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchdatasourcereferencesforresourcetyperequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [DataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.datasourcereference) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `fetchDataSourceReferencesForResourceTypeAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchUsableBackupVaults(request, options)
    
    
    fetchUsableBackupVaults(request?: protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackupVault[],
            protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest | null,
            protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsResponse
        ]>;

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchUsableBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault)[], [protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsrequest) | null, [protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `fetchUsableBackupVaultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### fetchUsableBackupVaults(request, options, callback)
    
    
    fetchUsableBackupVaults(request: protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest, protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupVault>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchUsableBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsrequest), [protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchUsableBackupVaults(request, callback)
    
    
    fetchUsableBackupVaults(request: protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest, protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupVault>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchUsableBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsrequest), [protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchUsableBackupVaultsAsync(request, options)
    
    
    fetchUsableBackupVaultsAsync(request?: protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IBackupVault>;

Equivalent to `fetchUsableBackupVaults`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchUsableBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve backupvault stores
       *  information, in the format 'projects/{project_id}/locations/{location}'. In
       *  Google Cloud Backup and DR, locations map to Google Cloud regions, for
       *  example
       *  **us-central1**.
       *  To retrieve backupvault stores for all locations, use "-" for the
       *  '{location}' value.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callFetchUsableBackupVaults() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.fetchUsableBackupVaultsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callFetchUsableBackupVaults();
    
    

### fetchUsableBackupVaultsStream(request, options)
    
    
    fetchUsableBackupVaultsStream(request?: protos.google.cloud.backupdr.v1beta.IFetchUsableBackupVaultsRequest, options?: CallOptions): Transform;

Equivalent to `fetchUsableBackupVaults`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchUsableBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ifetchusablebackupvaultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `fetchUsableBackupVaultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### getAutoProtectionPolicy(request, options)
    
    
    getAutoProtectionPolicy(request?: protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy,
            (protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single AutoProtectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy), ([protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the policy to retrieve.
       *  Format:
       *  projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetAutoProtectionPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getAutoProtectionPolicy(request);
        console.log(response);
      }
    
      callGetAutoProtectionPolicy();
    
    

### getAutoProtectionPolicy(request, options, callback)
    
    
    getAutoProtectionPolicy(request: protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy, protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy), [protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAutoProtectionPolicy(request, callback)
    
    
    getAutoProtectionPolicy(request: protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy, protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy), [protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAutoProtectionPolicyBinding(request, options)
    
    
    getAutoProtectionPolicyBinding(request?: protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyBindingRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding,
            (protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyBindingRequest | undefined),
            {} | undefined
        ]>;

Returns the auto protection policy binding read from the CCFE tables.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicybindingrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding), ([protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicybindingrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the binding to retrieve.
       *  Format:
       *  projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetAutoProtectionPolicyBinding() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getAutoProtectionPolicyBinding(request);
        console.log(response);
      }
    
      callGetAutoProtectionPolicyBinding();
    
    

### getAutoProtectionPolicyBinding(request, options, callback)
    
    
    getAutoProtectionPolicyBinding(request: protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyBindingRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding, protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyBindingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicybindingrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding), [protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicybindingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAutoProtectionPolicyBinding(request, callback)
    
    
    getAutoProtectionPolicyBinding(request: protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyBindingRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding, protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyBindingRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicybindingrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding), [protos.google.cloud.backupdr.v1beta.IGetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetautoprotectionpolicybindingrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackup(request, options)
    
    
    getBackup(request?: protos.google.cloud.backupdr.v1beta.IGetBackupRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackup,
            protos.google.cloud.backupdr.v1beta.IGetBackupRequest | undefined,
            {} | undefined
        ]>;

Gets details of a Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackuprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup), [protos.google.cloud.backupdr.v1beta.IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackuprequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the data source resource name, in the format
       *  'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}'
       */
      // const name = 'abc123'
      /**
       *  Optional. Reserved for future use to provide a BASIC & FULL view of Backup
       *  resource.
       */
      // const view = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetBackup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getBackup(request);
        console.log(response);
      }
    
      callGetBackup();
    
    

### getBackup(request, options, callback)
    
    
    getBackup(request: protos.google.cloud.backupdr.v1beta.IGetBackupRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IBackup, protos.google.cloud.backupdr.v1beta.IGetBackupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackuprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup), [protos.google.cloud.backupdr.v1beta.IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackuprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackup(request, callback)
    
    
    getBackup(request: protos.google.cloud.backupdr.v1beta.IGetBackupRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IBackup, protos.google.cloud.backupdr.v1beta.IGetBackupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackuprequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup), [protos.google.cloud.backupdr.v1beta.IGetBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackuprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackupPlan(request, options)
    
    
    getBackupPlan(request?: protos.google.cloud.backupdr.v1beta.IGetBackupPlanRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackupPlan,
            protos.google.cloud.backupdr.v1beta.IGetBackupPlanRequest | undefined,
            {} | undefined
        ]>;

Gets details of a single BackupPlan.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan), [protos.google.cloud.backupdr.v1beta.IGetBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the `BackupPlan` to retrieve.
       *  Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetBackupPlan() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getBackupPlan(request);
        console.log(response);
      }
    
      callGetBackupPlan();
    
    

### getBackupPlan(request, options, callback)
    
    
    getBackupPlan(request: protos.google.cloud.backupdr.v1beta.IGetBackupPlanRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IBackupPlan, protos.google.cloud.backupdr.v1beta.IGetBackupPlanRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan), [protos.google.cloud.backupdr.v1beta.IGetBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackupPlan(request, callback)
    
    
    getBackupPlan(request: protos.google.cloud.backupdr.v1beta.IGetBackupPlanRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IBackupPlan, protos.google.cloud.backupdr.v1beta.IGetBackupPlanRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan), [protos.google.cloud.backupdr.v1beta.IGetBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackupPlanAssociation(request, options)
    
    
    getBackupPlanAssociation(request?: protos.google.cloud.backupdr.v1beta.IGetBackupPlanAssociationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation,
            (protos.google.cloud.backupdr.v1beta.IGetBackupPlanAssociationRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single BackupPlanAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanassociationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), ([protos.google.cloud.backupdr.v1beta.IGetBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanassociationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the backup plan association resource, in the format
       *  `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetBackupPlanAssociation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getBackupPlanAssociation(request);
        console.log(response);
      }
    
      callGetBackupPlanAssociation();
    
    

### getBackupPlanAssociation(request, options, callback)
    
    
    getBackupPlanAssociation(request: protos.google.cloud.backupdr.v1beta.IGetBackupPlanAssociationRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IGetBackupPlanAssociationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanassociationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IGetBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanassociationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackupPlanAssociation(request, callback)
    
    
    getBackupPlanAssociation(request: protos.google.cloud.backupdr.v1beta.IGetBackupPlanAssociationRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IGetBackupPlanAssociationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanassociationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IGetBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanassociationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackupPlanRevision(request, options)
    
    
    getBackupPlanRevision(request?: protos.google.cloud.backupdr.v1beta.IGetBackupPlanRevisionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackupPlanRevision,
            (protos.google.cloud.backupdr.v1beta.IGetBackupPlanRevisionRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single BackupPlanRevision.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupPlanRevisionRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrevisionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackupPlanRevision](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanrevision), ([protos.google.cloud.backupdr.v1beta.IGetBackupPlanRevisionRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrevisionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the `BackupPlanRevision` to retrieve.
       *  Format:
       *  `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetBackupPlanRevision() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getBackupPlanRevision(request);
        console.log(response);
      }
    
      callGetBackupPlanRevision();
    
    

### getBackupPlanRevision(request, options, callback)
    
    
    getBackupPlanRevision(request: protos.google.cloud.backupdr.v1beta.IGetBackupPlanRevisionRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IBackupPlanRevision, protos.google.cloud.backupdr.v1beta.IGetBackupPlanRevisionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupPlanRevisionRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrevisionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBackupPlanRevision](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanrevision), [protos.google.cloud.backupdr.v1beta.IGetBackupPlanRevisionRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrevisionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackupPlanRevision(request, callback)
    
    
    getBackupPlanRevision(request: protos.google.cloud.backupdr.v1beta.IGetBackupPlanRevisionRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IBackupPlanRevision, protos.google.cloud.backupdr.v1beta.IGetBackupPlanRevisionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupPlanRevisionRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrevisionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBackupPlanRevision](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanrevision), [protos.google.cloud.backupdr.v1beta.IGetBackupPlanRevisionRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupplanrevisionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackupVault(request, options)
    
    
    getBackupVault(request?: protos.google.cloud.backupdr.v1beta.IGetBackupVaultRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackupVault,
            protos.google.cloud.backupdr.v1beta.IGetBackupVaultRequest | undefined,
            {} | undefined
        ]>;

Gets details of a BackupVault.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupvaultrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault), [protos.google.cloud.backupdr.v1beta.IGetBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupvaultrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the backupvault store resource name, in the format
       *  'projects/{project_id}/locations/{location}/backupVaults/{resource_name}'
       */
      // const name = 'abc123'
      /**
       *  Optional. Reserved for future use to provide a BASIC & FULL view of Backup
       *  Vault
       */
      // const view = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetBackupVault() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getBackupVault(request);
        console.log(response);
      }
    
      callGetBackupVault();
    
    

### getBackupVault(request, options, callback)
    
    
    getBackupVault(request: protos.google.cloud.backupdr.v1beta.IGetBackupVaultRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IBackupVault, protos.google.cloud.backupdr.v1beta.IGetBackupVaultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupvaultrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault), [protos.google.cloud.backupdr.v1beta.IGetBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupvaultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBackupVault(request, callback)
    
    
    getBackupVault(request: protos.google.cloud.backupdr.v1beta.IGetBackupVaultRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IBackupVault, protos.google.cloud.backupdr.v1beta.IGetBackupVaultRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupvaultrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault), [protos.google.cloud.backupdr.v1beta.IGetBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbackupvaultrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBindingMatchingResource(request, options)
    
    
    getBindingMatchingResource(request?: protos.google.cloud.backupdr.v1beta.IGetBindingMatchingResourceRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBindingMatchingResource,
            (protos.google.cloud.backupdr.v1beta.IGetBindingMatchingResourceRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single Binding Matching Resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBindingMatchingResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbindingmatchingresourcerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibindingmatchingresource), ([protos.google.cloud.backupdr.v1beta.IGetBindingMatchingResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbindingmatchingresourcerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.bindingmatchingresource). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the matching resource to retrieve.
       *  Format:
       *  projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetBindingMatchingResource() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getBindingMatchingResource(request);
        console.log(response);
      }
    
      callGetBindingMatchingResource();
    
    

### getBindingMatchingResource(request, options, callback)
    
    
    getBindingMatchingResource(request: protos.google.cloud.backupdr.v1beta.IGetBindingMatchingResourceRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IBindingMatchingResource, protos.google.cloud.backupdr.v1beta.IGetBindingMatchingResourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBindingMatchingResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbindingmatchingresourcerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibindingmatchingresource), [protos.google.cloud.backupdr.v1beta.IGetBindingMatchingResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbindingmatchingresourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBindingMatchingResource(request, callback)
    
    
    getBindingMatchingResource(request: protos.google.cloud.backupdr.v1beta.IGetBindingMatchingResourceRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IBindingMatchingResource, protos.google.cloud.backupdr.v1beta.IGetBindingMatchingResourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBindingMatchingResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbindingmatchingresourcerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IBindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibindingmatchingresource), [protos.google.cloud.backupdr.v1beta.IGetBindingMatchingResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetbindingmatchingresourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataSource(request, options)
    
    
    getDataSource(request?: protos.google.cloud.backupdr.v1beta.IGetDataSourceRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IDataSource,
            protos.google.cloud.backupdr.v1beta.IGetDataSourceRequest | undefined,
            {} | undefined
        ]>;

Gets details of a DataSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasource), [protos.google.cloud.backupdr.v1beta.IGetDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the data source resource name, in the format
       *  'projects/{project_id}/locations/{location}/backupVaults/{resource_name}/dataSource/{resource_name}'
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetDataSource() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getDataSource(request);
        console.log(response);
      }
    
      callGetDataSource();
    
    

### getDataSource(request, options, callback)
    
    
    getDataSource(request: protos.google.cloud.backupdr.v1beta.IGetDataSourceRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IDataSource, protos.google.cloud.backupdr.v1beta.IGetDataSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasource), [protos.google.cloud.backupdr.v1beta.IGetDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataSource(request, callback)
    
    
    getDataSource(request: protos.google.cloud.backupdr.v1beta.IGetDataSourceRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IDataSource, protos.google.cloud.backupdr.v1beta.IGetDataSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasource), [protos.google.cloud.backupdr.v1beta.IGetDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataSourceReference(request, options)
    
    
    getDataSourceReference(request?: protos.google.cloud.backupdr.v1beta.IGetDataSourceReferenceRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IDataSourceReference,
            (protos.google.cloud.backupdr.v1beta.IGetDataSourceReferenceRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single DataSourceReference.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSourceReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcereferencerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference), ([protos.google.cloud.backupdr.v1beta.IGetDataSourceReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcereferencerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.datasourcereference). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the DataSourceReference to retrieve.
       *  Format:
       *  projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetDataSourceReference() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getDataSourceReference(request);
        console.log(response);
      }
    
      callGetDataSourceReference();
    
    

### getDataSourceReference(request, options, callback)
    
    
    getDataSourceReference(request: protos.google.cloud.backupdr.v1beta.IGetDataSourceReferenceRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IDataSourceReference, protos.google.cloud.backupdr.v1beta.IGetDataSourceReferenceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSourceReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcereferencerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference), [protos.google.cloud.backupdr.v1beta.IGetDataSourceReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcereferencerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataSourceReference(request, callback)
    
    
    getDataSourceReference(request: protos.google.cloud.backupdr.v1beta.IGetDataSourceReferenceRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IDataSourceReference, protos.google.cloud.backupdr.v1beta.IGetDataSourceReferenceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSourceReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcereferencerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference), [protos.google.cloud.backupdr.v1beta.IGetDataSourceReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetdatasourcereferencerequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getManagementServer(request, options)
    
    
    getManagementServer(request?: protos.google.cloud.backupdr.v1beta.IGetManagementServerRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IManagementServer,
            (protos.google.cloud.backupdr.v1beta.IGetManagementServerRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single ManagementServer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetmanagementserverrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver), ([protos.google.cloud.backupdr.v1beta.IGetManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetmanagementserverrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the management server resource name, in the format
       *  'projects/{project_id}/locations/{location}/managementServers/{resource_name}'
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callGetManagementServer() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await backupdrClient.getManagementServer(request);
        console.log(response);
      }
    
      callGetManagementServer();
    
    

### getManagementServer(request, options, callback)
    
    
    getManagementServer(request: protos.google.cloud.backupdr.v1beta.IGetManagementServerRequest, options: CallOptions, callback: Callback<protos.google.cloud.backupdr.v1beta.IManagementServer, protos.google.cloud.backupdr.v1beta.IGetManagementServerRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetmanagementserverrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver), [protos.google.cloud.backupdr.v1beta.IGetManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetmanagementserverrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getManagementServer(request, callback)
    
    
    getManagementServer(request: protos.google.cloud.backupdr.v1beta.IGetManagementServerRequest, callback: Callback<protos.google.cloud.backupdr.v1beta.IManagementServer, protos.google.cloud.backupdr.v1beta.IGetManagementServerRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetmanagementserverrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver), [protos.google.cloud.backupdr.v1beta.IGetManagementServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.igetmanagementserverrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.operation)]>` |   
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
  
### initializeService(request, options)
    
    
    initializeService(request?: protos.google.cloud.backupdr.v1beta.IInitializeServiceRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IInitializeServiceResponse, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Initializes the service related config for a project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInitializeServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iinitializeservicerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IInitializeServiceResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iinitializeserviceresponse), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The configuration for initializing a Cloud SQL instance.
       */
      // const cloudSqlInstanceInitializationConfig = {}
      /**
       *  Required. The resource name of the serviceConfig used to initialize the
       *  service. The location must be the location of the BackupVault.
       *  Format: `projects/{project_id}/locations/{location}/serviceConfig`.
       */
      // const name = 'abc123'
      /**
       *  Required. The resource type to which the default service config will be
       *  applied. Examples include, "compute.googleapis.com/Instance" and
       *  "storage.googleapis.com/Bucket".
       */
      // const resourceType = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. The location where the BackupPlan will be created. This field is
       *  required for multi-region BackupVaults and is optional for regional
       *  BackupVaults. It is useful when creating a Backup Vault in a multi-region,
       *  allowing the BackupPlan to reside in a specific region within that
       *  multi-region. If this field is not provided, the BackupPlan will be created
       *  in the same location as specified in the `name` field.
       */
      // const backupPlanLocation = 'abc123'
      /**
       *  Optional. If set, validates the request and returns the result, but does
       *  not actually run it.
       */
      // const validateOnly = true
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callInitializeService() {
        // Construct request
        const request = {
          name,
          resourceType,
        };
    
        // Run request
        const [operation] = await backupdrClient.initializeService(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callInitializeService();
    
    

### initializeService(request, options, callback)
    
    
    initializeService(request: protos.google.cloud.backupdr.v1beta.IInitializeServiceRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IInitializeServiceResponse, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInitializeServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iinitializeservicerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IInitializeServiceResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iinitializeserviceresponse), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### initializeService(request, callback)
    
    
    initializeService(request: protos.google.cloud.backupdr.v1beta.IInitializeServiceRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IInitializeServiceResponse, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInitializeServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iinitializeservicerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IInitializeServiceResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iinitializeserviceresponse), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### initiateDeleteAutoProtectionPolicyBinding(request, options)
    
    
    initiateDeleteAutoProtectionPolicyBinding(request?: protos.google.cloud.backupdr.v1beta.IInitiateDeleteAutoProtectionPolicyBindingRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

InitiateDeleteAutoProtectionPolicyBinding initiates delete for AutoProtectionPolicy Binding

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInitiateDeleteAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iinitiatedeleteautoprotectionpolicybindingrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the binding to delete.
       *  Format:
       *  projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}
       */
      // const name = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callInitiateDeleteAutoProtectionPolicyBinding() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.initiateDeleteAutoProtectionPolicyBinding(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callInitiateDeleteAutoProtectionPolicyBinding();
    
    

### initiateDeleteAutoProtectionPolicyBinding(request, options, callback)
    
    
    initiateDeleteAutoProtectionPolicyBinding(request: protos.google.cloud.backupdr.v1beta.IInitiateDeleteAutoProtectionPolicyBindingRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInitiateDeleteAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iinitiatedeleteautoprotectionpolicybindingrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### initiateDeleteAutoProtectionPolicyBinding(request, callback)
    
    
    initiateDeleteAutoProtectionPolicyBinding(request: protos.google.cloud.backupdr.v1beta.IInitiateDeleteAutoProtectionPolicyBindingRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInitiateDeleteAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iinitiatedeleteautoprotectionpolicybindingrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAppliedAutoProtectionPolicies(request, options)
    
    
    listAppliedAutoProtectionPolicies(request?: protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IAppliedAutoProtectionPolicy[],
            protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest | null,
            protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesResponse
        ]>;

Lists AppliedAutoProtectionPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IAppliedAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iappliedautoprotectionpolicy)[], [protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesrequest) | null, [protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAppliedAutoProtectionPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAppliedAutoProtectionPolicies(request, options, callback)
    
    
    listAppliedAutoProtectionPolicies(request: protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest, protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IAppliedAutoProtectionPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesrequest), [protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IAppliedAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iappliedautoprotectionpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAppliedAutoProtectionPolicies(request, callback)
    
    
    listAppliedAutoProtectionPolicies(request: protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest, protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IAppliedAutoProtectionPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesrequest), [protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IAppliedAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iappliedautoprotectionpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAppliedAutoProtectionPoliciesAsync(request, options)
    
    
    listAppliedAutoProtectionPoliciesAsync(request?: protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IAppliedAutoProtectionPolicy>;

Equivalent to `listAppliedAutoProtectionPolicies`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IAppliedAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iappliedautoprotectionpolicy)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve the list of
       *  applied policies. Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of applied policies to return in a single
       *  page.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous
       *  `ListAppliedAutoProtectionPolicies` call.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A filter expression that filters resources listed in the
       *  response.
       */
      // const filter = 'abc123'
      /**
       *  Optional. An expression that sorts the results in the response.
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListAppliedAutoProtectionPolicies() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.[listAppliedAutoProtectionPoliciesAsync](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/v1beta.backupdrclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAppliedAutoProtectionPolicies();
    
    

### listAppliedAutoProtectionPoliciesStream(request, options)
    
    
    listAppliedAutoProtectionPoliciesStream(request?: protos.google.cloud.backupdr.v1beta.IListAppliedAutoProtectionPoliciesRequest, options?: CallOptions): Transform;

Equivalent to `listAppliedAutoProtectionPolicies`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistappliedautoprotectionpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAppliedAutoProtectionPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAutoProtectionPolicies(request, options)
    
    
    listAutoProtectionPolicies(request?: protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy[],
            protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest | null,
            protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesResponse
        ]>;

Lists AutoProtectionPolicies for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy)[], [protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesrequest) | null, [protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAutoProtectionPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAutoProtectionPolicies(request, options, callback)
    
    
    listAutoProtectionPolicies(request: protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest, protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesrequest), [protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAutoProtectionPolicies(request, callback)
    
    
    listAutoProtectionPolicies(request: protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest, protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesrequest), [protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAutoProtectionPoliciesAsync(request, options)
    
    
    listAutoProtectionPoliciesAsync(request?: protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy>;

Equivalent to `listAutoProtectionPolicies`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve the list of
       *  policies. Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of policies to return in a single page.
       *  If unspecified, a server-default value will be used.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous
       *  `ListAutoProtectionPolicies` call. Provide this to retrieve the subsequent
       *  page.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A filter expression that filters resources listed in the
       *  response. The following fields are filterable:
       */
      // const filter = 'abc123'
      /**
       *  Optional. An expression that sorts the results in the response. The
       *  following fields are sortable:
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListAutoProtectionPolicies() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.[listAutoProtectionPoliciesAsync](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/v1beta.backupdrclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAutoProtectionPolicies();
    
    

### listAutoProtectionPoliciesStream(request, options)
    
    
    listAutoProtectionPoliciesStream(request?: protos.google.cloud.backupdr.v1beta.IListAutoProtectionPoliciesRequest, options?: CallOptions): Transform;

Equivalent to `listAutoProtectionPolicies`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAutoProtectionPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAutoProtectionPolicyBindings(request, options)
    
    
    listAutoProtectionPolicyBindings(request?: protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding[],
            protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest | null,
            protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsResponse
        ]>;

Returns the auto protection policy bindings read from the CCFE tables.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding)[], [protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsrequest) | null, [protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAutoProtectionPolicyBindingsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAutoProtectionPolicyBindings(request, options, callback)
    
    
    listAutoProtectionPolicyBindings(request: protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest, protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsrequest), [protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAutoProtectionPolicyBindings(request, callback)
    
    
    listAutoProtectionPolicyBindings(request: protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest, protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsrequest), [protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAutoProtectionPolicyBindingsAsync(request, options)
    
    
    listAutoProtectionPolicyBindingsAsync(request?: protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding>;

Equivalent to `listAutoProtectionPolicyBindings`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicyBinding](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicybinding)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve the list of
       *  policies. Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of policies to return in a single page.
       *  If unspecified, a server-default value will be used.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous
       *  `ListAutoProtectionPolicies` call. Provide this to retrieve the subsequent
       *  page.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A filter expression that filters resources listed in the
       *  response. The following fields are filterable:
       */
      // const filter = 'abc123'
      /**
       *  Optional. An expression that sorts the results in the response. The
       *  following fields are sortable:
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListAutoProtectionPolicyBindings() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.[listAutoProtectionPolicyBindingsAsync](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/v1beta.backupdrclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAutoProtectionPolicyBindings();
    
    

### listAutoProtectionPolicyBindingsStream(request, options)
    
    
    listAutoProtectionPolicyBindingsStream(request?: protos.google.cloud.backupdr.v1beta.IListAutoProtectionPolicyBindingsRequest, options?: CallOptions): Transform;

Equivalent to `listAutoProtectionPolicyBindings`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistautoprotectionpolicybindingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAutoProtectionPolicyBindingsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBackupPlanAssociations(request, options)
    
    
    listBackupPlanAssociations(request?: protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation[],
            protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest | null,
            protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsResponse
        ]>;

Lists BackupPlanAssociations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlanAssociationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation)[], [protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsrequest) | null, [protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listBackupPlanAssociationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBackupPlanAssociations(request, options, callback)
    
    
    listBackupPlanAssociations(request: protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest, protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlanAssociationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsrequest), [protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupPlanAssociations(request, callback)
    
    
    listBackupPlanAssociations(request: protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest, protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlanAssociationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsrequest), [protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupPlanAssociationsAsync(request, options)
    
    
    listBackupPlanAssociationsAsync(request?: protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation>;

Equivalent to `listBackupPlanAssociations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlanAssociationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve backup Plan
       *  Associations information, in the format
       *  `projects/{project_id}/locations/{location}`. In Backup and DR, locations
       *  map to Google Cloud regions, for example **us-central1**. To retrieve
       *  backup plan associations for all locations, use "-" for the
       *  `{location}` value.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results
       */
      // const filter = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListBackupPlanAssociations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.listBackupPlanAssociationsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListBackupPlanAssociations();
    
    

### listBackupPlanAssociationsStream(request, options)
    
    
    listBackupPlanAssociationsStream(request?: protos.google.cloud.backupdr.v1beta.IListBackupPlanAssociationsRequest, options?: CallOptions): Transform;

Equivalent to `listBackupPlanAssociations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlanAssociationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanassociationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listBackupPlanAssociationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBackupPlanRevisions(request, options)
    
    
    listBackupPlanRevisions(request?: protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackupPlanRevision[],
            protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest | null,
            protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsResponse
        ]>;

Lists BackupPlanRevisions in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlanRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackupPlanRevision](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanrevision)[], [protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsrequest) | null, [protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listBackupPlanRevisionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBackupPlanRevisions(request, options, callback)
    
    
    listBackupPlanRevisions(request: protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest, protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupPlanRevision>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlanRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsrequest), [protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupPlanRevision](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanrevision)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupPlanRevisions(request, callback)
    
    
    listBackupPlanRevisions(request: protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest, protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupPlanRevision>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlanRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsrequest), [protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupPlanRevision](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanrevision)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupPlanRevisionsAsync(request, options)
    
    
    listBackupPlanRevisionsAsync(request?: protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IBackupPlanRevision>;

Equivalent to `listBackupPlanRevisions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlanRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IBackupPlanRevision](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanrevision)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve
       *  `BackupPlanRevisions` information. Format:
       *  `projects/{project}/locations/{location}/backupPlans/{backup_plan}`. In
       *  Google Cloud Backup and DR, locations map to Google Cloud regions, for e.g.
       *  **us-central1**.
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of `BackupPlans` to return in a single
       *  response. If not specified, a default value will be chosen by the service.
       *  Note that the response may include a partial list and a caller should
       *  only rely on the response's
       *  next_page_token google.cloud.backupdr.v1beta.ListBackupPlansResponse.next_page_token 
       *  to determine if there are more instances left to be queried.
       */
      // const pageSize = 1234
      /**
       *  Optional. The value of
       *  next_page_token google.cloud.backupdr.v1beta.ListBackupPlansResponse.next_page_token 
       *  received from a previous `ListBackupPlans` call.
       *  Provide this to retrieve the subsequent page in a multi-page list of
       *  results. When paginating, all other parameters provided to
       *  `ListBackupPlans` must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListBackupPlanRevisions() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.listBackupPlanRevisionsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListBackupPlanRevisions();
    
    

### listBackupPlanRevisionsStream(request, options)
    
    
    listBackupPlanRevisionsStream(request?: protos.google.cloud.backupdr.v1beta.IListBackupPlanRevisionsRequest, options?: CallOptions): Transform;

Equivalent to `listBackupPlanRevisions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlanRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplanrevisionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listBackupPlanRevisionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBackupPlans(request, options)
    
    
    listBackupPlans(request?: protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackupPlan[],
            protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest | null,
            protos.google.cloud.backupdr.v1beta.IListBackupPlansResponse
        ]>;

Lists BackupPlans in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlansRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan)[], [protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansrequest) | null, [protos.google.cloud.backupdr.v1beta.IListBackupPlansResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listBackupPlansAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBackupPlans(request, options, callback)
    
    
    listBackupPlans(request: protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest, protos.google.cloud.backupdr.v1beta.IListBackupPlansResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupPlan>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlansRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansrequest), [protos.google.cloud.backupdr.v1beta.IListBackupPlansResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupPlans(request, callback)
    
    
    listBackupPlans(request: protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest, protos.google.cloud.backupdr.v1beta.IListBackupPlansResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupPlan>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlansRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansrequest), [protos.google.cloud.backupdr.v1beta.IListBackupPlansResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupPlansAsync(request, options)
    
    
    listBackupPlansAsync(request?: protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IBackupPlan>;

Equivalent to `listBackupPlans`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlansRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve `BackupPlans`
       *  information. Format: `projects/{project}/locations/{location}`. In Google
       *  Cloud Backup and DR, locations map to Google Cloud regions, for e.g.
       *  **us-central1**. To retrieve backup plans for all locations, use "-" for
       *  the
       *  `{location}` value.
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of `BackupPlans` to return in a single
       *  response. If not specified, a default value will be chosen by the service.
       *  Note that the response may include a partial list and a caller should
       *  only rely on the response's
       *  next_page_token google.cloud.backupdr.v1beta.ListBackupPlansResponse.next_page_token 
       *  to determine if there are more instances left to be queried.
       */
      // const pageSize = 1234
      /**
       *  Optional. The value of
       *  next_page_token google.cloud.backupdr.v1beta.ListBackupPlansResponse.next_page_token 
       *  received from a previous `ListBackupPlans` call.
       *  Provide this to retrieve the subsequent page in a multi-page list of
       *  results. When paginating, all other parameters provided to
       *  `ListBackupPlans` must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Field match expression used to filter the results.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Field by which to sort the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListBackupPlans() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.listBackupPlansAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListBackupPlans();
    
    

### listBackupPlansStream(request, options)
    
    
    listBackupPlansStream(request?: protos.google.cloud.backupdr.v1beta.IListBackupPlansRequest, options?: CallOptions): Transform;

Equivalent to `listBackupPlans`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupPlansRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupplansrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listBackupPlansAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBackups(request, options)
    
    
    listBackups(request?: protos.google.cloud.backupdr.v1beta.IListBackupsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackup[],
            protos.google.cloud.backupdr.v1beta.IListBackupsRequest | null,
            protos.google.cloud.backupdr.v1beta.IListBackupsResponse
        ]>;

Lists Backups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup)[], [protos.google.cloud.backupdr.v1beta.IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsrequest) | null, [protos.google.cloud.backupdr.v1beta.IListBackupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listBackupsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBackups(request, options, callback)
    
    
    listBackups(request: protos.google.cloud.backupdr.v1beta.IListBackupsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBackupsRequest, protos.google.cloud.backupdr.v1beta.IListBackupsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsrequest), [protos.google.cloud.backupdr.v1beta.IListBackupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackups(request, callback)
    
    
    listBackups(request: protos.google.cloud.backupdr.v1beta.IListBackupsRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBackupsRequest, protos.google.cloud.backupdr.v1beta.IListBackupsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsrequest), [protos.google.cloud.backupdr.v1beta.IListBackupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupsAsync(request, options)
    
    
    listBackupsAsync(request?: protos.google.cloud.backupdr.v1beta.IListBackupsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IBackup>;

Equivalent to `listBackups`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve backup
       *  information, in the format
       *  'projects/{project_id}/locations/{location}'. In Google Cloud Backup and
       *  DR, locations map to Google Cloud regions, for example
       *  **us-central1**.
       *  To retrieve data sources for all locations, use "-" for the
       *  '{location}' value.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Reserved for future use to provide a BASIC & FULL view of Backup
       *  resource.
       */
      // const view = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListBackups() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.listBackupsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListBackups();
    
    

### listBackupsStream(request, options)
    
    
    listBackupsStream(request?: protos.google.cloud.backupdr.v1beta.IListBackupsRequest, options?: CallOptions): Transform;

Equivalent to `listBackups`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listBackupsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBackupVaults(request, options)
    
    
    listBackupVaults(request?: protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBackupVault[],
            protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest | null,
            protos.google.cloud.backupdr.v1beta.IListBackupVaultsResponse
        ]>;

Lists BackupVaults in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault)[], [protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsrequest) | null, [protos.google.cloud.backupdr.v1beta.IListBackupVaultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listBackupVaultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBackupVaults(request, options, callback)
    
    
    listBackupVaults(request: protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest, protos.google.cloud.backupdr.v1beta.IListBackupVaultsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupVault>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsrequest), [protos.google.cloud.backupdr.v1beta.IListBackupVaultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupVaults(request, callback)
    
    
    listBackupVaults(request: protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest, protos.google.cloud.backupdr.v1beta.IListBackupVaultsResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBackupVault>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsrequest), [protos.google.cloud.backupdr.v1beta.IListBackupVaultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBackupVaultsAsync(request, options)
    
    
    listBackupVaultsAsync(request?: protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IBackupVault>;

Equivalent to `listBackupVaults`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve backupvault stores
       *  information, in the format 'projects/{project_id}/locations/{location}'. In
       *  Google Cloud Backup and DR, locations map to Google Cloud regions, for
       *  example
       *  **us-central1**.
       *  To retrieve backupvault stores for all locations, use "-" for the
       *  '{location}' value.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
      /**
       *  Optional. Reserved for future use to provide a BASIC & FULL view of Backup
       *  Vault.
       */
      // const view = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListBackupVaults() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.listBackupVaultsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListBackupVaults();
    
    

### listBackupVaultsStream(request, options)
    
    
    listBackupVaultsStream(request?: protos.google.cloud.backupdr.v1beta.IListBackupVaultsRequest, options?: CallOptions): Transform;

Equivalent to `listBackupVaults`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBackupVaultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbackupvaultsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listBackupVaultsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBindingMatchingResources(request, options)
    
    
    listBindingMatchingResources(request?: protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IBindingMatchingResource[],
            protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest | null,
            protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesResponse
        ]>;

Lists Binding Matching Resources for a given AutoProtectionPolicyBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBindingMatchingResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IBindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibindingmatchingresource)[], [protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesrequest) | null, [protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [BindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.bindingmatchingresource). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listBindingMatchingResourcesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listBindingMatchingResources(request, options, callback)
    
    
    listBindingMatchingResources(request: protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest, protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBindingMatchingResource>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBindingMatchingResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesrequest), [protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibindingmatchingresource)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBindingMatchingResources(request, callback)
    
    
    listBindingMatchingResources(request: protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest, protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IBindingMatchingResource>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBindingMatchingResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesrequest), [protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IBindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibindingmatchingresource)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBindingMatchingResourcesAsync(request, options)
    
    
    listBindingMatchingResourcesAsync(request?: protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IBindingMatchingResource>;

Equivalent to `listBindingMatchingResources`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBindingMatchingResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IBindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibindingmatchingresource)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [BindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.bindingmatchingresource). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project, location, auto protection policy and binding for
       *  which to retrieve `BindingMatchingResources` information. Format:
       *  `projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}`.
       *  In Google Cloud Backup and DR, locations map to Google Cloud regions, for
       *  example **us-central1**.
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of `BindingMatchingResources` to return in a
       *  single response. The default page size is 100 and maximum page size is 200.
       *  Note that the response may include a partial list and a caller should
       *  only rely on the response's
       *  next_page_token google.cloud.backupdr.v1beta.ListBindingMatchingResourcesResponse.next_page_token 
       *  to determine if there are more instances left to be queried.
       */
      // const pageSize = 1234
      /**
       *  Optional. The value of
       *  next_page_token google.cloud.backupdr.v1beta.ListBindingMatchingResourcesResponse.next_page_token 
       *  received from a previous `ListBindingMatchingResources` call. Provide this
       *  to retrieve the subsequent page in a multi-page list of results. When
       *  paginating, all other parameters provided to `ListBindingMatchingResources`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Field match expression used to filter the results.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Field by which to sort the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListBindingMatchingResources() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.[listBindingMatchingResourcesAsync](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/v1beta.backupdrclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListBindingMatchingResources();
    
    

### listBindingMatchingResourcesStream(request, options)
    
    
    listBindingMatchingResourcesStream(request?: protos.google.cloud.backupdr.v1beta.IListBindingMatchingResourcesRequest, options?: CallOptions): Transform;

Equivalent to `listBindingMatchingResources`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBindingMatchingResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistbindingmatchingresourcesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [BindingMatchingResource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.bindingmatchingresource) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listBindingMatchingResourcesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataSourceReferences(request, options)
    
    
    listDataSourceReferences(request?: protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IDataSourceReference[],
            protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest | null,
            protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesResponse
        ]>;

Lists DataSourceReferences for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourceReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference)[], [protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesrequest) | null, [protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [DataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.datasourcereference). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDataSourceReferencesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataSourceReferences(request, options, callback)
    
    
    listDataSourceReferences(request: protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest, protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IDataSourceReference>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourceReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesrequest), [protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataSourceReferences(request, callback)
    
    
    listDataSourceReferences(request: protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest, protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IDataSourceReference>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourceReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesrequest), [protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataSourceReferencesAsync(request, options)
    
    
    listDataSourceReferencesAsync(request?: protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IDataSourceReference>;

Equivalent to `listDataSourceReferences`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourceReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IDataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasourcereference)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [DataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.datasourcereference). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name.
       *  Format: projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of DataSourceReferences to return. The service
       *  may return fewer than this value. If unspecified, at most 50
       *  DataSourceReferences will be returned. The maximum value is 100; values
       *  above 100 will be coerced to 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListDataSourceReferences`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `ListDataSourceReferences` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A filter expression that filters the results listed in the
       *  response. The expression must specify the field name, a comparison
       *  operator, and the value that you want to use for filtering.
       *  The following field and operator combinations are supported:
       *  * data_source_gcp_resource_info.gcp_resourcename with `=`, `!=`
       *  * data_source_gcp_resource_info.type with `=`, `!=`
       */
      // const filter = 'abc123'
      /**
       *  Optional. A comma-separated list of fields to order by, sorted in ascending
       *  order. Use "desc" after a field name for descending.
       *  Supported fields:
       *  * data_source
       *  * data_source_gcp_resource_info.gcp_resourcename
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListDataSourceReferences() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.listDataSourceReferencesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDataSourceReferences();
    
    

### listDataSourceReferencesStream(request, options)
    
    
    listDataSourceReferencesStream(request?: protos.google.cloud.backupdr.v1beta.IListDataSourceReferencesRequest, options?: CallOptions): Transform;

Equivalent to `listDataSourceReferences`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourceReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcereferencesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [DataSourceReference](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.datasourcereference) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDataSourceReferencesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataSources(request, options)
    
    
    listDataSources(request?: protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IDataSource[],
            protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest | null,
            protos.google.cloud.backupdr.v1beta.IListDataSourcesResponse
        ]>;

Lists DataSources in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasource)[], [protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesrequest) | null, [protos.google.cloud.backupdr.v1beta.IListDataSourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDataSourcesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDataSources(request, options, callback)
    
    
    listDataSources(request: protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest, protos.google.cloud.backupdr.v1beta.IListDataSourcesResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IDataSource>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesrequest), [protos.google.cloud.backupdr.v1beta.IListDataSourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasource)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataSources(request, callback)
    
    
    listDataSources(request: protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest, protos.google.cloud.backupdr.v1beta.IListDataSourcesResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IDataSource>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesrequest), [protos.google.cloud.backupdr.v1beta.IListDataSourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasource)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataSourcesAsync(request, options)
    
    
    listDataSourcesAsync(request?: protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IDataSource>;

Equivalent to `listDataSources`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasource)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve data
       *  sources information, in the format
       *  'projects/{project_id}/locations/{location}'. In Google Cloud Backup and
       *  DR, locations map to Google Cloud regions, for example
       *  **us-central1**.
       *  To retrieve data sources for all locations, use "-" for the
       *  '{location}' value.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListDataSources() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.listDataSourcesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDataSources();
    
    

### listDataSourcesStream(request, options)
    
    
    listDataSourcesStream(request?: protos.google.cloud.backupdr.v1beta.IListDataSourcesRequest, options?: CallOptions): Transform;

Equivalent to `listDataSources`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistdatasourcesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDataSourcesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
    

### listManagementServers(request, options)
    
    
    listManagementServers(request?: protos.google.cloud.backupdr.v1beta.IListManagementServersRequest, options?: CallOptions): Promise<[
            protos.google.cloud.backupdr.v1beta.IManagementServer[],
            protos.google.cloud.backupdr.v1beta.IListManagementServersRequest | null,
            protos.google.cloud.backupdr.v1beta.IListManagementServersResponse
        ]>;

Lists ManagementServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListManagementServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver)[], [protos.google.cloud.backupdr.v1beta.IListManagementServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversrequest) | null, [protos.google.cloud.backupdr.v1beta.IListManagementServersResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listManagementServersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listManagementServers(request, options, callback)
    
    
    listManagementServers(request: protos.google.cloud.backupdr.v1beta.IListManagementServersRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListManagementServersRequest, protos.google.cloud.backupdr.v1beta.IListManagementServersResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IManagementServer>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListManagementServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListManagementServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversrequest), [protos.google.cloud.backupdr.v1beta.IListManagementServersResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listManagementServers(request, callback)
    
    
    listManagementServers(request: protos.google.cloud.backupdr.v1beta.IListManagementServersRequest, callback: PaginationCallback<protos.google.cloud.backupdr.v1beta.IListManagementServersRequest, protos.google.cloud.backupdr.v1beta.IListManagementServersResponse | null | undefined, protos.google.cloud.backupdr.v1beta.IManagementServer>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListManagementServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.backupdr.v1beta.IListManagementServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversrequest), [protos.google.cloud.backupdr.v1beta.IListManagementServersResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversresponse) | null | undefined, [protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listManagementServersAsync(request, options)
    
    
    listManagementServersAsync(request?: protos.google.cloud.backupdr.v1beta.IListManagementServersRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.backupdr.v1beta.IManagementServer>;

Equivalent to `listManagementServers`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListManagementServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.backupdr.v1beta.IManagementServer](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.imanagementserver)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location for which to retrieve management servers
       *  information, in the format 'projects/{project_id}/locations/{location}'.
       *  In Google Cloud Backup and DR, locations map to Google Cloud regions, for
       *  example
       *  **us-central1**. To retrieve management servers for all locations, use "-"
       *  for the
       *  '{location}' value.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results.
       */
      // const orderBy = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callListManagementServers() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = backupdrClient.listManagementServersAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListManagementServers();
    
    

### listManagementServersStream(request, options)
    
    
    listManagementServersStream(request?: protos.google.cloud.backupdr.v1beta.IListManagementServersRequest, options?: CallOptions): Transform;

Equivalent to `listManagementServers`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListManagementServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ilistmanagementserversrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listManagementServersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
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
  
### managementServerPath(project, location, managementserver)
    
    
    managementServerPath(project: string, location: string, managementserver: string): string;

Return a fully-qualified managementServer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`managementserver` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### matchAppliedAutoProtectionPolicyFromAppliedAutoProtectionPolicyName(appliedAutoProtectionPolicyName)
    
    
    matchAppliedAutoProtectionPolicyFromAppliedAutoProtectionPolicyName(appliedAutoProtectionPolicyName: string): string | number;

Parse the applied_auto_protection_policy from AppliedAutoProtectionPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`appliedAutoProtectionPolicyName` |  `string`   
A fully-qualified path representing AppliedAutoProtectionPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the applied_auto_protection_policy.  
  
### matchAutoProtectionPolicyFromAutoProtectionPolicyBindingName(autoProtectionPolicyBindingName)
    
    
    matchAutoProtectionPolicyFromAutoProtectionPolicyBindingName(autoProtectionPolicyBindingName: string): string | number;

Parse the auto_protection_policy from AutoProtectionPolicyBinding resource.

**Parameter**  
---  
**Name** | **Description**  
`autoProtectionPolicyBindingName` |  `string`   
A fully-qualified path representing AutoProtectionPolicyBinding resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the auto_protection_policy.  
  
### matchAutoProtectionPolicyFromAutoProtectionPolicyName(autoProtectionPolicyName)
    
    
    matchAutoProtectionPolicyFromAutoProtectionPolicyName(autoProtectionPolicyName: string): string | number;

Parse the auto_protection_policy from AutoProtectionPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`autoProtectionPolicyName` |  `string`   
A fully-qualified path representing AutoProtectionPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the auto_protection_policy.  
  
### matchAutoProtectionPolicyFromBindingMatchingResourceName(bindingMatchingResourceName)
    
    
    matchAutoProtectionPolicyFromBindingMatchingResourceName(bindingMatchingResourceName: string): string | number;

Parse the auto_protection_policy from BindingMatchingResource resource.

**Parameter**  
---  
**Name** | **Description**  
`bindingMatchingResourceName` |  `string`   
A fully-qualified path representing BindingMatchingResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the auto_protection_policy.  
  
### matchBackupFromBackupName(backupName)
    
    
    matchBackupFromBackupName(backupName: string): string | number;

Parse the backup from Backup resource.

**Parameter**  
---  
**Name** | **Description**  
`backupName` |  `string`   
A fully-qualified path representing Backup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the backup.  
  
### matchBackupPlanAssociationFromBackupPlanAssociationName(backupPlanAssociationName)
    
    
    matchBackupPlanAssociationFromBackupPlanAssociationName(backupPlanAssociationName: string): string | number;

Parse the backup_plan_association from BackupPlanAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanAssociationName` |  `string`   
A fully-qualified path representing BackupPlanAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the backup_plan_association.  
  
### matchBackupPlanFromBackupPlanName(backupPlanName)
    
    
    matchBackupPlanFromBackupPlanName(backupPlanName: string): string | number;

Parse the backup_plan from BackupPlan resource.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanName` |  `string`   
A fully-qualified path representing BackupPlan resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the backup_plan.  
  
### matchBackupPlanFromBackupPlanRevisionName(backupPlanRevisionName)
    
    
    matchBackupPlanFromBackupPlanRevisionName(backupPlanRevisionName: string): string | number;

Parse the backup_plan from BackupPlanRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanRevisionName` |  `string`   
A fully-qualified path representing BackupPlanRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the backup_plan.  
  
### matchBackupvaultFromBackupName(backupName)
    
    
    matchBackupvaultFromBackupName(backupName: string): string | number;

Parse the backupvault from Backup resource.

**Parameter**  
---  
**Name** | **Description**  
`backupName` |  `string`   
A fully-qualified path representing Backup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the backupvault.  
  
### matchBackupvaultFromBackupVaultName(backupVaultName)
    
    
    matchBackupvaultFromBackupVaultName(backupVaultName: string): string | number;

Parse the backupvault from BackupVault resource.

**Parameter**  
---  
**Name** | **Description**  
`backupVaultName` |  `string`   
A fully-qualified path representing BackupVault resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the backupvault.  
  
### matchBackupvaultFromDataSourceName(dataSourceName)
    
    
    matchBackupvaultFromDataSourceName(dataSourceName: string): string | number;

Parse the backupvault from DataSource resource.

**Parameter**  
---  
**Name** | **Description**  
`dataSourceName` |  `string`   
A fully-qualified path representing DataSource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the backupvault.  
  
### matchBindingFromAutoProtectionPolicyBindingName(autoProtectionPolicyBindingName)
    
    
    matchBindingFromAutoProtectionPolicyBindingName(autoProtectionPolicyBindingName: string): string | number;

Parse the binding from AutoProtectionPolicyBinding resource.

**Parameter**  
---  
**Name** | **Description**  
`autoProtectionPolicyBindingName` |  `string`   
A fully-qualified path representing AutoProtectionPolicyBinding resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the binding.  
  
### matchBindingFromBindingMatchingResourceName(bindingMatchingResourceName)
    
    
    matchBindingFromBindingMatchingResourceName(bindingMatchingResourceName: string): string | number;

Parse the binding from BindingMatchingResource resource.

**Parameter**  
---  
**Name** | **Description**  
`bindingMatchingResourceName` |  `string`   
A fully-qualified path representing BindingMatchingResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the binding.  
  
### matchDatasourceFromBackupName(backupName)
    
    
    matchDatasourceFromBackupName(backupName: string): string | number;

Parse the datasource from Backup resource.

**Parameter**  
---  
**Name** | **Description**  
`backupName` |  `string`   
A fully-qualified path representing Backup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the datasource.  
  
### matchDatasourceFromDataSourceName(dataSourceName)
    
    
    matchDatasourceFromDataSourceName(dataSourceName: string): string | number;

Parse the datasource from DataSource resource.

**Parameter**  
---  
**Name** | **Description**  
`dataSourceName` |  `string`   
A fully-qualified path representing DataSource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the datasource.  
  
### matchDataSourceReferenceFromDataSourceReferenceName(dataSourceReferenceName)
    
    
    matchDataSourceReferenceFromDataSourceReferenceName(dataSourceReferenceName: string): string | number;

Parse the data_source_reference from DataSourceReference resource.

**Parameter**  
---  
**Name** | **Description**  
`dataSourceReferenceName` |  `string`   
A fully-qualified path representing DataSourceReference resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_source_reference.  
  
### matchLocationFromAppliedAutoProtectionPolicyName(appliedAutoProtectionPolicyName)
    
    
    matchLocationFromAppliedAutoProtectionPolicyName(appliedAutoProtectionPolicyName: string): string | number;

Parse the location from AppliedAutoProtectionPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`appliedAutoProtectionPolicyName` |  `string`   
A fully-qualified path representing AppliedAutoProtectionPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromAutoProtectionPolicyBindingName(autoProtectionPolicyBindingName)
    
    
    matchLocationFromAutoProtectionPolicyBindingName(autoProtectionPolicyBindingName: string): string | number;

Parse the location from AutoProtectionPolicyBinding resource.

**Parameter**  
---  
**Name** | **Description**  
`autoProtectionPolicyBindingName` |  `string`   
A fully-qualified path representing AutoProtectionPolicyBinding resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromAutoProtectionPolicyName(autoProtectionPolicyName)
    
    
    matchLocationFromAutoProtectionPolicyName(autoProtectionPolicyName: string): string | number;

Parse the location from AutoProtectionPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`autoProtectionPolicyName` |  `string`   
A fully-qualified path representing AutoProtectionPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBackupName(backupName)
    
    
    matchLocationFromBackupName(backupName: string): string | number;

Parse the location from Backup resource.

**Parameter**  
---  
**Name** | **Description**  
`backupName` |  `string`   
A fully-qualified path representing Backup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBackupPlanAssociationName(backupPlanAssociationName)
    
    
    matchLocationFromBackupPlanAssociationName(backupPlanAssociationName: string): string | number;

Parse the location from BackupPlanAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanAssociationName` |  `string`   
A fully-qualified path representing BackupPlanAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBackupPlanName(backupPlanName)
    
    
    matchLocationFromBackupPlanName(backupPlanName: string): string | number;

Parse the location from BackupPlan resource.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanName` |  `string`   
A fully-qualified path representing BackupPlan resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBackupPlanRevisionName(backupPlanRevisionName)
    
    
    matchLocationFromBackupPlanRevisionName(backupPlanRevisionName: string): string | number;

Parse the location from BackupPlanRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanRevisionName` |  `string`   
A fully-qualified path representing BackupPlanRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBackupVaultName(backupVaultName)
    
    
    matchLocationFromBackupVaultName(backupVaultName: string): string | number;

Parse the location from BackupVault resource.

**Parameter**  
---  
**Name** | **Description**  
`backupVaultName` |  `string`   
A fully-qualified path representing BackupVault resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBindingMatchingResourceName(bindingMatchingResourceName)
    
    
    matchLocationFromBindingMatchingResourceName(bindingMatchingResourceName: string): string | number;

Parse the location from BindingMatchingResource resource.

**Parameter**  
---  
**Name** | **Description**  
`bindingMatchingResourceName` |  `string`   
A fully-qualified path representing BindingMatchingResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDataSourceName(dataSourceName)
    
    
    matchLocationFromDataSourceName(dataSourceName: string): string | number;

Parse the location from DataSource resource.

**Parameter**  
---  
**Name** | **Description**  
`dataSourceName` |  `string`   
A fully-qualified path representing DataSource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDataSourceReferenceName(dataSourceReferenceName)
    
    
    matchLocationFromDataSourceReferenceName(dataSourceReferenceName: string): string | number;

Parse the location from DataSourceReference resource.

**Parameter**  
---  
**Name** | **Description**  
`dataSourceReferenceName` |  `string`   
A fully-qualified path representing DataSourceReference resource.  
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
  
### matchLocationFromManagementServerName(managementServerName)
    
    
    matchLocationFromManagementServerName(managementServerName: string): string | number;

Parse the location from ManagementServer resource.

**Parameter**  
---  
**Name** | **Description**  
`managementServerName` |  `string`   
A fully-qualified path representing ManagementServer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromResourceBackupConfigName(resourceBackupConfigName)
    
    
    matchLocationFromResourceBackupConfigName(resourceBackupConfigName: string): string | number;

Parse the location from ResourceBackupConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`resourceBackupConfigName` |  `string`   
A fully-qualified path representing ResourceBackupConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchManagementserverFromManagementServerName(managementServerName)
    
    
    matchManagementserverFromManagementServerName(managementServerName: string): string | number;

Parse the managementserver from ManagementServer resource.

**Parameter**  
---  
**Name** | **Description**  
`managementServerName` |  `string`   
A fully-qualified path representing ManagementServer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the managementserver.  
  
### matchMatchingResourceFromBindingMatchingResourceName(bindingMatchingResourceName)
    
    
    matchMatchingResourceFromBindingMatchingResourceName(bindingMatchingResourceName: string): string | number;

Parse the matching_resource from BindingMatchingResource resource.

**Parameter**  
---  
**Name** | **Description**  
`bindingMatchingResourceName` |  `string`   
A fully-qualified path representing BindingMatchingResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the matching_resource.  
  
### matchProjectFromAppliedAutoProtectionPolicyName(appliedAutoProtectionPolicyName)
    
    
    matchProjectFromAppliedAutoProtectionPolicyName(appliedAutoProtectionPolicyName: string): string | number;

Parse the project from AppliedAutoProtectionPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`appliedAutoProtectionPolicyName` |  `string`   
A fully-qualified path representing AppliedAutoProtectionPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAutoProtectionPolicyBindingName(autoProtectionPolicyBindingName)
    
    
    matchProjectFromAutoProtectionPolicyBindingName(autoProtectionPolicyBindingName: string): string | number;

Parse the project from AutoProtectionPolicyBinding resource.

**Parameter**  
---  
**Name** | **Description**  
`autoProtectionPolicyBindingName` |  `string`   
A fully-qualified path representing AutoProtectionPolicyBinding resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAutoProtectionPolicyName(autoProtectionPolicyName)
    
    
    matchProjectFromAutoProtectionPolicyName(autoProtectionPolicyName: string): string | number;

Parse the project from AutoProtectionPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`autoProtectionPolicyName` |  `string`   
A fully-qualified path representing AutoProtectionPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBackupName(backupName)
    
    
    matchProjectFromBackupName(backupName: string): string | number;

Parse the project from Backup resource.

**Parameter**  
---  
**Name** | **Description**  
`backupName` |  `string`   
A fully-qualified path representing Backup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBackupPlanAssociationName(backupPlanAssociationName)
    
    
    matchProjectFromBackupPlanAssociationName(backupPlanAssociationName: string): string | number;

Parse the project from BackupPlanAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanAssociationName` |  `string`   
A fully-qualified path representing BackupPlanAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBackupPlanName(backupPlanName)
    
    
    matchProjectFromBackupPlanName(backupPlanName: string): string | number;

Parse the project from BackupPlan resource.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanName` |  `string`   
A fully-qualified path representing BackupPlan resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBackupPlanRevisionName(backupPlanRevisionName)
    
    
    matchProjectFromBackupPlanRevisionName(backupPlanRevisionName: string): string | number;

Parse the project from BackupPlanRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanRevisionName` |  `string`   
A fully-qualified path representing BackupPlanRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBackupVaultName(backupVaultName)
    
    
    matchProjectFromBackupVaultName(backupVaultName: string): string | number;

Parse the project from BackupVault resource.

**Parameter**  
---  
**Name** | **Description**  
`backupVaultName` |  `string`   
A fully-qualified path representing BackupVault resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBindingMatchingResourceName(bindingMatchingResourceName)
    
    
    matchProjectFromBindingMatchingResourceName(bindingMatchingResourceName: string): string | number;

Parse the project from BindingMatchingResource resource.

**Parameter**  
---  
**Name** | **Description**  
`bindingMatchingResourceName` |  `string`   
A fully-qualified path representing BindingMatchingResource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDataSourceName(dataSourceName)
    
    
    matchProjectFromDataSourceName(dataSourceName: string): string | number;

Parse the project from DataSource resource.

**Parameter**  
---  
**Name** | **Description**  
`dataSourceName` |  `string`   
A fully-qualified path representing DataSource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDataSourceReferenceName(dataSourceReferenceName)
    
    
    matchProjectFromDataSourceReferenceName(dataSourceReferenceName: string): string | number;

Parse the project from DataSourceReference resource.

**Parameter**  
---  
**Name** | **Description**  
`dataSourceReferenceName` |  `string`   
A fully-qualified path representing DataSourceReference resource.  
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
  
### matchProjectFromManagementServerName(managementServerName)
    
    
    matchProjectFromManagementServerName(managementServerName: string): string | number;

Parse the project from ManagementServer resource.

**Parameter**  
---  
**Name** | **Description**  
`managementServerName` |  `string`   
A fully-qualified path representing ManagementServer resource.  
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
  
### matchProjectFromResourceBackupConfigName(resourceBackupConfigName)
    
    
    matchProjectFromResourceBackupConfigName(resourceBackupConfigName: string): string | number;

Parse the project from ResourceBackupConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`resourceBackupConfigName` |  `string`   
A fully-qualified path representing ResourceBackupConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchResourceBackupConfigFromResourceBackupConfigName(resourceBackupConfigName)
    
    
    matchResourceBackupConfigFromResourceBackupConfigName(resourceBackupConfigName: string): string | number;

Parse the resource_backup_config from ResourceBackupConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`resourceBackupConfigName` |  `string`   
A fully-qualified path representing ResourceBackupConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the resource_backup_config.  
  
### matchRevisionFromBackupPlanRevisionName(backupPlanRevisionName)
    
    
    matchRevisionFromBackupPlanRevisionName(backupPlanRevisionName: string): string | number;

Parse the revision from BackupPlanRevision resource.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanRevisionName` |  `string`   
A fully-qualified path representing BackupPlanRevision resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the revision.  
  
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
  
### resourceBackupConfigPath(project, location, resourceBackupConfig)
    
    
    resourceBackupConfigPath(project: string, location: string, resourceBackupConfig: string): string;

Return a fully-qualified resourceBackupConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`resourceBackupConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### restoreBackup(request, options)
    
    
    restoreBackup(request?: protos.google.cloud.backupdr.v1beta.IRestoreBackupRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IRestoreBackupResponse, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Restore from a Backup

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.irestorebackuprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IRestoreBackupResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.irestorebackupresponse), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Compute Engine target environment to be used during restore.
       */
      // const computeInstanceTargetEnvironment = {}
      /**
       *  Disk target environment to be used during restore.
       */
      // const diskTargetEnvironment = {}
      /**
       *  Region disk target environment to be used during restore.
       */
      // const regionDiskTargetEnvironment = {}
      /**
       *  Compute Engine instance properties to be overridden during restore.
       */
      // const computeInstanceRestoreProperties = {}
      /**
       *  Disk properties to be overridden during restore.
       */
      // const diskRestoreProperties = {}
      /**
       *  Required. The resource name of the Backup instance, in the format
       *  'projects/* /locations/* /backupVaults/* /dataSources/* /backups/'.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. A field mask used to clear server-side default values
       *  for fields within the `instance_properties` oneof.
       *  When a field in this mask is cleared, the server will not apply its
       *  default logic (like inheriting a value from the source) for that field.
       *  The most common current use case is clearing default encryption keys.
       *  Examples of field mask paths:
       *  - Compute Instance Disks:
       *  `compute_instance_restore_properties.disks.*.disk_encryption_key`
       *  - Single Disk: `disk_restore_properties.disk_encryption_key`
       */
      // const clearOverridesFieldMask = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callRestoreBackup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.restoreBackup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callRestoreBackup();
    
    

### restoreBackup(request, options, callback)
    
    
    restoreBackup(request: protos.google.cloud.backupdr.v1beta.IRestoreBackupRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IRestoreBackupResponse, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.irestorebackuprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IRestoreBackupResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.irestorebackupresponse), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restoreBackup(request, callback)
    
    
    restoreBackup(request: protos.google.cloud.backupdr.v1beta.IRestoreBackupRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IRestoreBackupResponse, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestoreBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.irestorebackuprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IRestoreBackupResponse](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.irestorebackupresponse), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### triggerBackup(request, options)
    
    
    triggerBackup(request?: protos.google.cloud.backupdr.v1beta.ITriggerBackupRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Triggers a new Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITriggerBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.itriggerbackuprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the backup plan association resource, in the format
       *  `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`
       */
      // const name = 'abc123'
      /**
       *  Optional. backup rule_id for which a backup needs to be triggered.
       *  If not specified, on-demand backup with custom retention will be triggered.
       */
      // const ruleId = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. The duration for which backup data will be kept, while taking an
       *  on-demand backup with custom retention. It is defined in "days".
       *  It is mutually exclusive with rule_id. This field is required if
       *  rule_id is not provided.
       */
      // const customRetentionDays = 1234
      /**
       *  Optional. Labels to be applied on the backup.
       */
      // const labels = [1,2,3,4]
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callTriggerBackup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await backupdrClient.triggerBackup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callTriggerBackup();
    
    

### triggerBackup(request, options, callback)
    
    
    triggerBackup(request: protos.google.cloud.backupdr.v1beta.ITriggerBackupRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITriggerBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.itriggerbackuprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### triggerBackup(request, callback)
    
    
    triggerBackup(request: protos.google.cloud.backupdr.v1beta.ITriggerBackupRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITriggerBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.itriggerbackuprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAutoProtectionPolicy(request, options)
    
    
    updateAutoProtectionPolicy(request?: protos.google.cloud.backupdr.v1beta.IUpdateAutoProtectionPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single AutoProtectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdateautoprotectionpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The policy to update.
       */
      // const autoProtectionPolicy = {}
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  AutoProtectionPolicy resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateAutoProtectionPolicy() {
        // Construct request
        const request = {
          autoProtectionPolicy,
          updateMask,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateAutoProtectionPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateAutoProtectionPolicy();
    
    

### updateAutoProtectionPolicy(request, options, callback)
    
    
    updateAutoProtectionPolicy(request: protos.google.cloud.backupdr.v1beta.IUpdateAutoProtectionPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdateautoprotectionpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAutoProtectionPolicy(request, callback)
    
    
    updateAutoProtectionPolicy(request: protos.google.cloud.backupdr.v1beta.IUpdateAutoProtectionPolicyRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAutoProtectionPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdateautoprotectionpolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IAutoProtectionPolicy](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iautoprotectionpolicy), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBackup(request, options)
    
    
    updateBackup(request?: protos.google.cloud.backupdr.v1beta.IUpdateBackupRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IBackup, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the settings of a Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackuprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  Backup resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then the request will fail.
       */
      // const updateMask = {}
      /**
       *  Required. The resource being updated
       */
      // const backup = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateBackup() {
        // Construct request
        const request = {
          updateMask,
          backup,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateBackup(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateBackup();
    
    

### updateBackup(request, options, callback)
    
    
    updateBackup(request: protos.google.cloud.backupdr.v1beta.IUpdateBackupRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackup, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackuprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBackup(request, callback)
    
    
    updateBackup(request: protos.google.cloud.backupdr.v1beta.IUpdateBackupRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackup, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackuprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackup](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackup), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBackupPlan(request, options)
    
    
    updateBackupPlan(request?: protos.google.cloud.backupdr.v1beta.IUpdateBackupPlanRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlan, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Update a BackupPlan.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackupplanrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource being updated
       */
      // const backupPlan = {}
      /**
       *  Required. The list of fields to update.
       *  Field mask is used to specify the fields to be overwritten in the
       *  BackupPlan resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then the request will fail.
       *  Currently, these fields are supported in update: description, schedules,
       *  retention period, adding and removing Backup Rules.
       */
      // const updateMask = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateBackupPlan() {
        // Construct request
        const request = {
          backupPlan,
          updateMask,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateBackupPlan(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateBackupPlan();
    
    

### updateBackupPlan(request, options, callback)
    
    
    updateBackupPlan(request: protos.google.cloud.backupdr.v1beta.IUpdateBackupPlanRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlan, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackupplanrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBackupPlan(request, callback)
    
    
    updateBackupPlan(request: protos.google.cloud.backupdr.v1beta.IUpdateBackupPlanRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlan, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackupplanrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlan](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplan), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBackupPlanAssociation(request, options)
    
    
    updateBackupPlanAssociation(request?: protos.google.cloud.backupdr.v1beta.IUpdateBackupPlanAssociationRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Update a BackupPlanAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackupplanassociationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource being updated
       */
      // const backupPlanAssociation = {}
      /**
       *  Required. The list of fields to update.
       *  Field mask is used to specify the fields to be overwritten in the
       *  BackupPlanAssociation resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then the request will fail.
       *  Currently backup_plan_association.backup_plan is the only supported field.
       */
      // const updateMask = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and t
       *  he request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateBackupPlanAssociation() {
        // Construct request
        const request = {
          backupPlanAssociation,
          updateMask,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateBackupPlanAssociation(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateBackupPlanAssociation();
    
    

### updateBackupPlanAssociation(request, options, callback)
    
    
    updateBackupPlanAssociation(request: protos.google.cloud.backupdr.v1beta.IUpdateBackupPlanAssociationRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackupplanassociationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBackupPlanAssociation(request, callback)
    
    
    updateBackupPlanAssociation(request: protos.google.cloud.backupdr.v1beta.IUpdateBackupPlanAssociationRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackupplanassociationrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupPlanAssociation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupplanassociation), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBackupVault(request, options)
    
    
    updateBackupVault(request?: protos.google.cloud.backupdr.v1beta.IUpdateBackupVaultRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IBackupVault, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the settings of a BackupVault.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackupvaultrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  BackupVault resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then the request will fail.
       */
      // const updateMask = {}
      /**
       *  Required. The resource being updated
       */
      // const backupVault = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. Only validate the request, but do not perform mutations.
       *  The default is 'false'.
       */
      // const validateOnly = true
      /**
       *  Optional. If set to true, will not check plan duration against backup vault
       *  enforcement duration.
       */
      // const force = true
      /**
       *  Optional. If set to true, we will force update access restriction even if
       *  some non compliant data sources are present. The default is 'false'.
       */
      // const forceUpdateAccessRestriction = true
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateBackupVault() {
        // Construct request
        const request = {
          updateMask,
          backupVault,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateBackupVault(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateBackupVault();
    
    

### updateBackupVault(request, options, callback)
    
    
    updateBackupVault(request: protos.google.cloud.backupdr.v1beta.IUpdateBackupVaultRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupVault, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackupvaultrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBackupVault(request, callback)
    
    
    updateBackupVault(request: protos.google.cloud.backupdr.v1beta.IUpdateBackupVaultRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IBackupVault, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBackupVaultRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatebackupvaultrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IBackupVault](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ibackupvault), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataSource(request, options)
    
    
    updateDataSource(request?: protos.google.cloud.backupdr.v1beta.IUpdateDataSourceRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.backupdr.v1beta.IDataSource, protos.google.cloud.backupdr.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the settings of a DataSource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatedatasourcerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.backupdr.v1beta.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasource), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Field mask is used to specify the fields to be overwritten in the
       *  DataSource resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then the request will fail.
       */
      // const updateMask = {}
      /**
       *  Required. The resource being updated
       */
      // const dataSource = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Optional. Enable upsert.
       */
      // const allowMissing = true
    
      // Imports the Backupdr library
      const {BackupDRClient} = require('[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const backupdrClient = new [BackupDRClient](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)();
    
      async function callUpdateDataSource() {
        // Construct request
        const request = {
          updateMask,
          dataSource,
        };
    
        // Run request
        const [operation] = await backupdrClient.updateDataSource(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateDataSource();
    
    

### updateDataSource(request, options, callback)
    
    
    updateDataSource(request: protos.google.cloud.backupdr.v1beta.IUpdateDataSourceRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IDataSource, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatedatasourcerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasource), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataSource(request, callback)
    
    
    updateDataSource(request: protos.google.cloud.backupdr.v1beta.IUpdateDataSourceRequest, callback: Callback<LROperation<protos.google.cloud.backupdr.v1beta.IDataSource, protos.google.cloud.backupdr.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.iupdatedatasourcerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.backupdr.v1beta.IDataSource](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.idatasource), [protos.google.cloud.backupdr.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
