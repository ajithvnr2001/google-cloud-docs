---
url: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/v1beta.osconfigserviceclient
title: Class v1beta.OsConfigServiceClient (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:24.554395+00:00
---

# Class v1beta.OsConfigServiceClient (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/v1beta.osconfigserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.OsConfigServiceClient (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.2.2  2.1.2  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.6 

OS Config API

The OS Config service is a server-side component that you can use to manage package installations and patch jobs for virtual machine instances. v1beta

## Package

[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of OsConfigServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new OsConfigServiceClient({fallback: true}, gax); ```  
  
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

### osConfigServiceStub
    
    
    osConfigServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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

### cancelPatchJob(request, options)
    
    
    cancelPatchJob(request?: protos.google.cloud.osconfig.v1beta.ICancelPatchJobRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchJob,
            protos.google.cloud.osconfig.v1beta.ICancelPatchJobRequest | undefined,
            {} | undefined
        ]>;

Cancel a patch job. The patch job must be active. Canceled patch jobs cannot be restarted.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icancelpatchjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob), [protos.google.cloud.osconfig.v1beta.ICancelPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icancelpatchjobrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the patch in the form `projects/* /patchJobs/*`
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callCancelPatchJob() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.cancelPatchJob(request);
        console.log(response);
      }
    
      callCancelPatchJob();
    
    

### cancelPatchJob(request, options, callback)
    
    
    cancelPatchJob(request: protos.google.cloud.osconfig.v1beta.ICancelPatchJobRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchJob, protos.google.cloud.osconfig.v1beta.ICancelPatchJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icancelpatchjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob), [protos.google.cloud.osconfig.v1beta.ICancelPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icancelpatchjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelPatchJob(request, callback)
    
    
    cancelPatchJob(request: protos.google.cloud.osconfig.v1beta.ICancelPatchJobRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchJob, protos.google.cloud.osconfig.v1beta.ICancelPatchJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icancelpatchjobrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob), [protos.google.cloud.osconfig.v1beta.ICancelPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icancelpatchjobrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### createGuestPolicy(request, options)
    
    
    createGuestPolicy(request?: protos.google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IGuestPolicy,
            protos.google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest | undefined,
            {} | undefined
        ]>;

Create an OS Config guest policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreateguestpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy), [protos.google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreateguestpolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.guestpolicy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the parent using one of the following forms:
       *  `projects/{project_number}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The logical name of the guest policy in the project
       *  with the following restrictions:
       *  * Must contain only lowercase letters, numbers, and hyphens.
       *  * Must start with a letter.
       *  * Must be between 1-63 characters.
       *  * Must end with a number or a letter.
       *  * Must be unique within the project.
       */
      // const guestPolicyId = 'abc123'
      /**
       *  Required. The GuestPolicy to create.
       */
      // const guestPolicy = {}
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callCreateGuestPolicy() {
        // Construct request
        const request = {
          parent,
          guestPolicyId,
          guestPolicy,
        };
    
        // Run request
        const response = await osconfigClient.createGuestPolicy(request);
        console.log(response);
      }
    
      callCreateGuestPolicy();
    
    

### createGuestPolicy(request, options, callback)
    
    
    createGuestPolicy(request: protos.google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IGuestPolicy, protos.google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreateguestpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy), [protos.google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreateguestpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGuestPolicy(request, callback)
    
    
    createGuestPolicy(request: protos.google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IGuestPolicy, protos.google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreateguestpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy), [protos.google.cloud.osconfig.v1beta.ICreateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreateguestpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPatchDeployment(request, options)
    
    
    createPatchDeployment(request?: protos.google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchDeployment,
            (protos.google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest | undefined),
            {} | undefined
        ]>;

Create an OS Config patch deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreatepatchdeploymentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), ([protos.google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreatepatchdeploymentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project to apply this patch deployment to in the form `projects/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. A name for the patch deployment in the project. When creating a name
       *  the following rules apply:
       *  * Must contain only lowercase letters, numbers, and hyphens.
       *  * Must start with a letter.
       *  * Must be between 1-63 characters.
       *  * Must end with a number or a letter.
       *  * Must be unique within the project.
       */
      // const patchDeploymentId = 'abc123'
      /**
       *  Required. The patch deployment to create.
       */
      // const patchDeployment = {}
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callCreatePatchDeployment() {
        // Construct request
        const request = {
          parent,
          patchDeploymentId,
          patchDeployment,
        };
    
        // Run request
        const response = await osconfigClient.createPatchDeployment(request);
        console.log(response);
      }
    
      callCreatePatchDeployment();
    
    

### createPatchDeployment(request, options, callback)
    
    
    createPatchDeployment(request: protos.google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchDeployment, protos.google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreatepatchdeploymentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), [protos.google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreatepatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPatchDeployment(request, callback)
    
    
    createPatchDeployment(request: protos.google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchDeployment, protos.google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreatepatchdeploymentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), [protos.google.cloud.osconfig.v1beta.ICreatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.icreatepatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGuestPolicy(request, options)
    
    
    deleteGuestPolicy(request?: protos.google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest | undefined,
            {} | undefined
        ]>;

Delete an OS Config guest policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideleteguestpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.iempty), [protos.google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideleteguestpolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the guest policy  using one of the following forms:
       *  `projects/{project_number}/guestPolicies/{guest_policy_id}`.
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callDeleteGuestPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.deleteGuestPolicy(request);
        console.log(response);
      }
    
      callDeleteGuestPolicy();
    
    

### deleteGuestPolicy(request, options, callback)
    
    
    deleteGuestPolicy(request: protos.google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideleteguestpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.iempty), [protos.google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideleteguestpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGuestPolicy(request, callback)
    
    
    deleteGuestPolicy(request: protos.google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideleteguestpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.iempty), [protos.google.cloud.osconfig.v1beta.IDeleteGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideleteguestpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePatchDeployment(request, options)
    
    
    deletePatchDeployment(request?: protos.google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest | undefined),
            {} | undefined
        ]>;

Delete an OS Config patch deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideletepatchdeploymentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.iempty), ([protos.google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideletepatchdeploymentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the patch deployment in the form
       *  `projects/* /patchDeployments/*`.
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callDeletePatchDeployment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.deletePatchDeployment(request);
        console.log(response);
      }
    
      callDeletePatchDeployment();
    
    

### deletePatchDeployment(request, options, callback)
    
    
    deletePatchDeployment(request: protos.google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideletepatchdeploymentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.iempty), [protos.google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideletepatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePatchDeployment(request, callback)
    
    
    deletePatchDeployment(request: protos.google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideletepatchdeploymentrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.iempty), [protos.google.cloud.osconfig.v1beta.IDeletePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ideletepatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### executePatchJob(request, options)
    
    
    executePatchJob(request?: protos.google.cloud.osconfig.v1beta.IExecutePatchJobRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchJob,
            protos.google.cloud.osconfig.v1beta.IExecutePatchJobRequest | undefined,
            {} | undefined
        ]>;

Patch VM instances by creating and running a patch job.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExecutePatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iexecutepatchjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob), [protos.google.cloud.osconfig.v1beta.IExecutePatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iexecutepatchjobrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project in which to run this patch in the form `projects/*`
       */
      // const parent = 'abc123'
      /**
       *  Description of the patch job. Length of the description is limited
       *  to 1024 characters.
       */
      // const description = 'abc123'
      /**
       *  Required. Instances to patch, either explicitly or filtered by some criteria such
       *  as zone or labels.
       */
      // const instanceFilter = {}
      /**
       *  Patch configuration being applied. If omitted, instances are
       *  patched using the default configurations.
       */
      // const patchConfig = {}
      /**
       *  Duration of the patch job. After the duration ends, the patch job
       *  times out.
       */
      // const duration = {}
      /**
       *  If this patch is a dry-run only, instances are contacted but
       *  will do nothing.
       */
      // const dryRun = true
      /**
       *  Display name for this patch job. This does not have to be unique.
       */
      // const displayName = 'abc123'
      /**
       *  Rollout strategy of the patch job.
       */
      // const rollout = {}
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callExecutePatchJob() {
        // Construct request
        const request = {
          parent,
          instanceFilter,
        };
    
        // Run request
        const response = await osconfigClient.executePatchJob(request);
        console.log(response);
      }
    
      callExecutePatchJob();
    
    

### executePatchJob(request, options, callback)
    
    
    executePatchJob(request: protos.google.cloud.osconfig.v1beta.IExecutePatchJobRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchJob, protos.google.cloud.osconfig.v1beta.IExecutePatchJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExecutePatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iexecutepatchjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob), [protos.google.cloud.osconfig.v1beta.IExecutePatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iexecutepatchjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### executePatchJob(request, callback)
    
    
    executePatchJob(request: protos.google.cloud.osconfig.v1beta.IExecutePatchJobRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchJob, protos.google.cloud.osconfig.v1beta.IExecutePatchJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExecutePatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iexecutepatchjobrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob), [protos.google.cloud.osconfig.v1beta.IExecutePatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iexecutepatchjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGuestPolicy(request, options)
    
    
    getGuestPolicy(request?: protos.google.cloud.osconfig.v1beta.IGetGuestPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IGuestPolicy,
            protos.google.cloud.osconfig.v1beta.IGetGuestPolicyRequest | undefined,
            {} | undefined
        ]>;

Get an OS Config guest policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetguestpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy), [protos.google.cloud.osconfig.v1beta.IGetGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetguestpolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.guestpolicy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the guest policy using one of the following forms:
       *  `projects/{project_number}/guestPolicies/{guest_policy_id}`.
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callGetGuestPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.getGuestPolicy(request);
        console.log(response);
      }
    
      callGetGuestPolicy();
    
    

### getGuestPolicy(request, options, callback)
    
    
    getGuestPolicy(request: protos.google.cloud.osconfig.v1beta.IGetGuestPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IGuestPolicy, protos.google.cloud.osconfig.v1beta.IGetGuestPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetguestpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy), [protos.google.cloud.osconfig.v1beta.IGetGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetguestpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGuestPolicy(request, callback)
    
    
    getGuestPolicy(request: protos.google.cloud.osconfig.v1beta.IGetGuestPolicyRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IGuestPolicy, protos.google.cloud.osconfig.v1beta.IGetGuestPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetguestpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy), [protos.google.cloud.osconfig.v1beta.IGetGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetguestpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPatchDeployment(request, options)
    
    
    getPatchDeployment(request?: protos.google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchDeployment,
            (protos.google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest | undefined),
            {} | undefined
        ]>;

Get an OS Config patch deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchdeploymentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), ([protos.google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchdeploymentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the patch deployment in the form
       *  `projects/* /patchDeployments/*`.
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callGetPatchDeployment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.getPatchDeployment(request);
        console.log(response);
      }
    
      callGetPatchDeployment();
    
    

### getPatchDeployment(request, options, callback)
    
    
    getPatchDeployment(request: protos.google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchDeployment, protos.google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchdeploymentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), [protos.google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPatchDeployment(request, callback)
    
    
    getPatchDeployment(request: protos.google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchDeployment, protos.google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchdeploymentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), [protos.google.cloud.osconfig.v1beta.IGetPatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPatchJob(request, options)
    
    
    getPatchJob(request?: protos.google.cloud.osconfig.v1beta.IGetPatchJobRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchJob,
            protos.google.cloud.osconfig.v1beta.IGetPatchJobRequest | undefined,
            {} | undefined
        ]>;

Get the patch job. This can be used to track the progress of an ongoing patch job or review the details of completed jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchjobrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob), [protos.google.cloud.osconfig.v1beta.IGetPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchjobrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the patch in the form `projects/* /patchJobs/*`
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callGetPatchJob() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.getPatchJob(request);
        console.log(response);
      }
    
      callGetPatchJob();
    
    

### getPatchJob(request, options, callback)
    
    
    getPatchJob(request: protos.google.cloud.osconfig.v1beta.IGetPatchJobRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchJob, protos.google.cloud.osconfig.v1beta.IGetPatchJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchjobrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob), [protos.google.cloud.osconfig.v1beta.IGetPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchjobrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPatchJob(request, callback)
    
    
    getPatchJob(request: protos.google.cloud.osconfig.v1beta.IGetPatchJobRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchJob, protos.google.cloud.osconfig.v1beta.IGetPatchJobRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchjobrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob), [protos.google.cloud.osconfig.v1beta.IGetPatchJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.igetpatchjobrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### guestPolicyPath(project, guestPolicy)
    
    
    guestPolicyPath(project: string, guestPolicy: string): string;

Return a fully-qualified guestPolicy resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`guestPolicy` |  `string`   
  
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
  
### listGuestPolicies(request, options)
    
    
    listGuestPolicies(request?: protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IGuestPolicy[],
            protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest | null,
            protos.google.cloud.osconfig.v1beta.IListGuestPoliciesResponse
        ]>;

Get a page of OS Config guest policies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGuestPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy)[], [protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesrequest) | null, [protos.google.cloud.osconfig.v1beta.IListGuestPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [GuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.guestpolicy). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listGuestPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listGuestPolicies(request, options, callback)
    
    
    listGuestPolicies(request: protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest, protos.google.cloud.osconfig.v1beta.IListGuestPoliciesResponse | null | undefined, protos.google.cloud.osconfig.v1beta.IGuestPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGuestPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesrequest), [protos.google.cloud.osconfig.v1beta.IListGuestPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesresponse) | null | undefined, [protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGuestPolicies(request, callback)
    
    
    listGuestPolicies(request: protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest, callback: PaginationCallback<protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest, protos.google.cloud.osconfig.v1beta.IListGuestPoliciesResponse | null | undefined, protos.google.cloud.osconfig.v1beta.IGuestPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGuestPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesrequest), [protos.google.cloud.osconfig.v1beta.IListGuestPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesresponse) | null | undefined, [protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGuestPoliciesAsync(request, options)
    
    
    listGuestPoliciesAsync(request?: protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.osconfig.v1beta.IGuestPolicy>;

Equivalent to `listGuestPolicies`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGuestPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [GuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.guestpolicy). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the parent using one of the following forms:
       *  `projects/{project_number}`.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of guest policies to return.
       */
      // const pageSize = 1234
      /**
       *  A pagination token returned from a previous call to `ListGuestPolicies`
       *  that indicates where this listing should continue from.
       */
      // const pageToken = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callListGuestPolicies() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = osconfigClient.[listGuestPoliciesAsync](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/v1beta.osconfigserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListGuestPolicies();
    
    

### listGuestPoliciesStream(request, options)
    
    
    listGuestPoliciesStream(request?: protos.google.cloud.osconfig.v1beta.IListGuestPoliciesRequest, options?: CallOptions): Transform;

Equivalent to `listGuestPolicies`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGuestPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistguestpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [GuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.guestpolicy) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listGuestPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPatchDeployments(request, options)
    
    
    listPatchDeployments(request?: protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchDeployment[],
            protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest | null,
            protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsResponse
        ]>;

Get a page of OS Config patch deployments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment)[], [protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsrequest) | null, [protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listPatchDeploymentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPatchDeployments(request, options, callback)
    
    
    listPatchDeployments(request: protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest, protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsResponse | null | undefined, protos.google.cloud.osconfig.v1beta.IPatchDeployment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsrequest), [protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsresponse) | null | undefined, [protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPatchDeployments(request, callback)
    
    
    listPatchDeployments(request: protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest, callback: PaginationCallback<protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest, protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsResponse | null | undefined, protos.google.cloud.osconfig.v1beta.IPatchDeployment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsrequest), [protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsresponse) | null | undefined, [protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPatchDeploymentsAsync(request, options)
    
    
    listPatchDeploymentsAsync(request?: protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.osconfig.v1beta.IPatchDeployment>;

Equivalent to `listPatchDeployments`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the parent in the form `projects/*`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of patch deployments to return. Default is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A pagination token returned from a previous call to ListPatchDeployments
       *  that indicates where this listing should continue from.
       */
      // const pageToken = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callListPatchDeployments() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = osconfigClient.listPatchDeploymentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListPatchDeployments();
    
    

### listPatchDeploymentsStream(request, options)
    
    
    listPatchDeploymentsStream(request?: protos.google.cloud.osconfig.v1beta.IListPatchDeploymentsRequest, options?: CallOptions): Transform;

Equivalent to `listPatchDeployments`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchdeploymentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listPatchDeploymentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPatchJobInstanceDetails(request, options)
    
    
    listPatchJobInstanceDetails(request?: protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchJobInstanceDetails[],
            protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest | null,
            protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsResponse
        ]>;

Get a list of instance details for a given patch job.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchJobInstanceDetails](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjobinstancedetails)[], [protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsrequest) | null, [protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [PatchJobInstanceDetails](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchjobinstancedetails). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listPatchJobInstanceDetailsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPatchJobInstanceDetails(request, options, callback)
    
    
    listPatchJobInstanceDetails(request: protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest, protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsResponse | null | undefined, protos.google.cloud.osconfig.v1beta.IPatchJobInstanceDetails>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsrequest), [protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsresponse) | null | undefined, [protos.google.cloud.osconfig.v1beta.IPatchJobInstanceDetails](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjobinstancedetails)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPatchJobInstanceDetails(request, callback)
    
    
    listPatchJobInstanceDetails(request: protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest, callback: PaginationCallback<protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest, protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsResponse | null | undefined, protos.google.cloud.osconfig.v1beta.IPatchJobInstanceDetails>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsrequest), [protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsresponse) | null | undefined, [protos.google.cloud.osconfig.v1beta.IPatchJobInstanceDetails](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjobinstancedetails)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPatchJobInstanceDetailsAsync(request, options)
    
    
    listPatchJobInstanceDetailsAsync(request?: protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.osconfig.v1beta.IPatchJobInstanceDetails>;

Equivalent to `listPatchJobInstanceDetails`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.osconfig.v1beta.IPatchJobInstanceDetails](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjobinstancedetails)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [PatchJobInstanceDetails](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchjobinstancedetails). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent for the instances are in the form of `projects/* /patchJobs/*`.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of instance details records to return.  Default is 100.
       */
      // const pageSize = 1234
      /**
       *  A pagination token returned from a previous call
       *  that indicates where this listing should continue from.
       */
      // const pageToken = 'abc123'
      /**
       *  A filter expression that filters results listed in the response. This
       *  field supports filtering results by instance zone, name, state, or
       *  `failure_reason`.
       */
      // const filter = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callListPatchJobInstanceDetails() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = osconfigClient.listPatchJobInstanceDetailsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListPatchJobInstanceDetails();
    
    

### listPatchJobInstanceDetailsStream(request, options)
    
    
    listPatchJobInstanceDetailsStream(request?: protos.google.cloud.osconfig.v1beta.IListPatchJobInstanceDetailsRequest, options?: CallOptions): Transform;

Equivalent to `listPatchJobInstanceDetails`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobinstancedetailsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [PatchJobInstanceDetails](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.patchjobinstancedetails) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listPatchJobInstanceDetailsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPatchJobs(request, options)
    
    
    listPatchJobs(request?: protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchJob[],
            protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest | null,
            protos.google.cloud.osconfig.v1beta.IListPatchJobsResponse
        ]>;

Get a list of patch jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob)[], [protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsrequest) | null, [protos.google.cloud.osconfig.v1beta.IListPatchJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listPatchJobsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPatchJobs(request, options, callback)
    
    
    listPatchJobs(request: protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest, protos.google.cloud.osconfig.v1beta.IListPatchJobsResponse | null | undefined, protos.google.cloud.osconfig.v1beta.IPatchJob>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsrequest), [protos.google.cloud.osconfig.v1beta.IListPatchJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsresponse) | null | undefined, [protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPatchJobs(request, callback)
    
    
    listPatchJobs(request: protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest, callback: PaginationCallback<protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest, protos.google.cloud.osconfig.v1beta.IListPatchJobsResponse | null | undefined, protos.google.cloud.osconfig.v1beta.IPatchJob>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsrequest), [protos.google.cloud.osconfig.v1beta.IListPatchJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsresponse) | null | undefined, [protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPatchJobsAsync(request, options)
    
    
    listPatchJobsAsync(request?: protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.osconfig.v1beta.IPatchJob>;

Equivalent to `listPatchJobs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.osconfig.v1beta.IPatchJob](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchjob)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. In the form of `projects/*`
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of instance status to return.
       */
      // const pageSize = 1234
      /**
       *  A pagination token returned from a previous call
       *  that indicates where this listing should continue from.
       */
      // const pageToken = 'abc123'
      /**
       *  If provided, this field specifies the criteria that must be met by patch
       *  jobs to be included in the response.
       *  Currently, filtering is only available on the patch_deployment field.
       */
      // const filter = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callListPatchJobs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = osconfigClient.listPatchJobsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListPatchJobs();
    
    

### listPatchJobsStream(request, options)
    
    
    listPatchJobsStream(request?: protos.google.cloud.osconfig.v1beta.IListPatchJobsRequest, options?: CallOptions): Transform;

Equivalent to `listPatchJobs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPatchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilistpatchjobsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listPatchJobsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### lookupEffectiveGuestPolicy(request, options)
    
    
    lookupEffectiveGuestPolicy(request?: protos.google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IEffectiveGuestPolicy,
            (protos.google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest | undefined),
            {} | undefined
        ]>;

Lookup the effective guest policy that applies to a VM instance. This lookup merges all policies that are assigned to the instance ancestry.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEffectiveGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilookupeffectiveguestpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IEffectiveGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ieffectiveguestpolicy), ([protos.google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilookupeffectiveguestpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The VM instance whose policies are being looked up.
       */
      // const instance = 'abc123'
      /**
       *  Short name of the OS running on the instance. The OS Config agent only
       *  provides this field for targeting if OS Inventory is enabled for that
       *  instance.
       */
      // const osShortName = 'abc123'
      /**
       *  Version of the OS running on the instance. The OS Config agent only
       *  provides this field for targeting if OS Inventory is enabled for that
       *  VM instance.
       */
      // const osVersion = 'abc123'
      /**
       *  Architecture of OS running on the instance. The OS Config agent only
       *  provides this field for targeting if OS Inventory is enabled for that
       *  instance.
       */
      // const osArchitecture = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callLookupEffectiveGuestPolicy() {
        // Construct request
        const request = {
          instance,
        };
    
        // Run request
        const response = await osconfigClient.lookupEffectiveGuestPolicy(request);
        console.log(response);
      }
    
      callLookupEffectiveGuestPolicy();
    
    

### lookupEffectiveGuestPolicy(request, options, callback)
    
    
    lookupEffectiveGuestPolicy(request: protos.google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IEffectiveGuestPolicy, protos.google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEffectiveGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilookupeffectiveguestpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IEffectiveGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ieffectiveguestpolicy), [protos.google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilookupeffectiveguestpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lookupEffectiveGuestPolicy(request, callback)
    
    
    lookupEffectiveGuestPolicy(request: protos.google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IEffectiveGuestPolicy, protos.google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILookupEffectiveGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilookupeffectiveguestpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IEffectiveGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ieffectiveguestpolicy), [protos.google.cloud.osconfig.v1beta.ILookupEffectiveGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ilookupeffectiveguestpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### matchGuestPolicyFromGuestPolicyName(guestPolicyName)
    
    
    matchGuestPolicyFromGuestPolicyName(guestPolicyName: string): string | number;

Parse the guest_policy from GuestPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`guestPolicyName` |  `string`   
A fully-qualified path representing GuestPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the guest_policy.  
  
### matchPatchDeploymentFromPatchDeploymentName(patchDeploymentName)
    
    
    matchPatchDeploymentFromPatchDeploymentName(patchDeploymentName: string): string | number;

Parse the patch_deployment from PatchDeployment resource.

**Parameter**  
---  
**Name** | **Description**  
`patchDeploymentName` |  `string`   
A fully-qualified path representing PatchDeployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the patch_deployment.  
  
### matchPatchJobFromPatchJobName(patchJobName)
    
    
    matchPatchJobFromPatchJobName(patchJobName: string): string | number;

Parse the patch_job from PatchJob resource.

**Parameter**  
---  
**Name** | **Description**  
`patchJobName` |  `string`   
A fully-qualified path representing PatchJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the patch_job.  
  
### matchProjectFromGuestPolicyName(guestPolicyName)
    
    
    matchProjectFromGuestPolicyName(guestPolicyName: string): string | number;

Parse the project from GuestPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`guestPolicyName` |  `string`   
A fully-qualified path representing GuestPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPatchDeploymentName(patchDeploymentName)
    
    
    matchProjectFromPatchDeploymentName(patchDeploymentName: string): string | number;

Parse the project from PatchDeployment resource.

**Parameter**  
---  
**Name** | **Description**  
`patchDeploymentName` |  `string`   
A fully-qualified path representing PatchDeployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPatchJobName(patchJobName)
    
    
    matchProjectFromPatchJobName(patchJobName: string): string | number;

Parse the project from PatchJob resource.

**Parameter**  
---  
**Name** | **Description**  
`patchJobName` |  `string`   
A fully-qualified path representing PatchJob resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### patchDeploymentPath(project, patchDeployment)
    
    
    patchDeploymentPath(project: string, patchDeployment: string): string;

Return a fully-qualified patchDeployment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`patchDeployment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### patchJobPath(project, patchJob)
    
    
    patchJobPath(project: string, patchJob: string): string;

Return a fully-qualified patchJob resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`patchJob` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### pausePatchDeployment(request, options)
    
    
    pausePatchDeployment(request?: protos.google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchDeployment,
            (protos.google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest | undefined),
            {} | undefined
        ]>;

Change state of patch deployment to "PAUSED". Patch deployment in paused state doesn't generate patch jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPausePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipausepatchdeploymentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), ([protos.google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipausepatchdeploymentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the patch deployment in the form
       *  `projects/* /patchDeployments/*`.
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callPausePatchDeployment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.pausePatchDeployment(request);
        console.log(response);
      }
    
      callPausePatchDeployment();
    
    

### pausePatchDeployment(request, options, callback)
    
    
    pausePatchDeployment(request: protos.google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchDeployment, protos.google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPausePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipausepatchdeploymentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), [protos.google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipausepatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pausePatchDeployment(request, callback)
    
    
    pausePatchDeployment(request: protos.google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchDeployment, protos.google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPausePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipausepatchdeploymentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), [protos.google.cloud.osconfig.v1beta.IPausePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipausepatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumePatchDeployment(request, options)
    
    
    resumePatchDeployment(request?: protos.google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchDeployment,
            (protos.google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest | undefined),
            {} | undefined
        ]>;

Change state of patch deployment back to "ACTIVE". Patch deployment in active state continues to generate patch jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iresumepatchdeploymentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), ([protos.google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iresumepatchdeploymentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the patch deployment in the form
       *  `projects/* /patchDeployments/*`.
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callResumePatchDeployment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.resumePatchDeployment(request);
        console.log(response);
      }
    
      callResumePatchDeployment();
    
    

### resumePatchDeployment(request, options, callback)
    
    
    resumePatchDeployment(request: protos.google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchDeployment, protos.google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iresumepatchdeploymentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), [protos.google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iresumepatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resumePatchDeployment(request, callback)
    
    
    resumePatchDeployment(request: protos.google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchDeployment, protos.google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResumePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iresumepatchdeploymentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), [protos.google.cloud.osconfig.v1beta.IResumePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iresumepatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGuestPolicy(request, options)
    
    
    updateGuestPolicy(request?: protos.google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IGuestPolicy,
            protos.google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest | undefined,
            {} | undefined
        ]>;

Update an OS Config guest policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdateguestpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy), [protos.google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdateguestpolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.guestpolicy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The updated GuestPolicy.
       */
      // const guestPolicy = {}
      /**
       *  Field mask that controls which fields of the guest policy should be
       *  updated.
       */
      // const updateMask = {}
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callUpdateGuestPolicy() {
        // Construct request
        const request = {
          guestPolicy,
        };
    
        // Run request
        const response = await osconfigClient.updateGuestPolicy(request);
        console.log(response);
      }
    
      callUpdateGuestPolicy();
    
    

### updateGuestPolicy(request, options, callback)
    
    
    updateGuestPolicy(request: protos.google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IGuestPolicy, protos.google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdateguestpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy), [protos.google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdateguestpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGuestPolicy(request, callback)
    
    
    updateGuestPolicy(request: protos.google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IGuestPolicy, protos.google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdateguestpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IGuestPolicy](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iguestpolicy), [protos.google.cloud.osconfig.v1beta.IUpdateGuestPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdateguestpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePatchDeployment(request, options)
    
    
    updatePatchDeployment(request?: protos.google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1beta.IPatchDeployment,
            (protos.google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest | undefined),
            {} | undefined
        ]>;

Update an OS Config patch deployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdatepatchdeploymentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), ([protos.google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdatepatchdeploymentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The patch deployment to Update.
       */
      // const patchDeployment = {}
      /**
       *  Optional. Field mask that controls which fields of the patch deployment should be
       *  updated.
       */
      // const updateMask = {}
    
      // Imports the Osconfig library
      const {OsConfigServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callUpdatePatchDeployment() {
        // Construct request
        const request = {
          patchDeployment,
        };
    
        // Run request
        const response = await osconfigClient.updatePatchDeployment(request);
        console.log(response);
      }
    
      callUpdatePatchDeployment();
    
    

### updatePatchDeployment(request, options, callback)
    
    
    updatePatchDeployment(request: protos.google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchDeployment, protos.google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdatepatchdeploymentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), [protos.google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdatepatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePatchDeployment(request, callback)
    
    
    updatePatchDeployment(request: protos.google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest, callback: Callback<protos.google.cloud.osconfig.v1beta.IPatchDeployment, protos.google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdatepatchdeploymentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1beta.IPatchDeployment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.ipatchdeployment), [protos.google.cloud.osconfig.v1beta.IUpdatePatchDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1beta.iupdatepatchdeploymentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
