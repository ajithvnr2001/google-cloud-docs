---
url: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/v1alpha.osconfigzonalserviceclient
title: Class v1alpha.OsConfigZonalServiceClient (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:25.582553+00:00
---

# Class v1alpha.OsConfigZonalServiceClient (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/v1alpha.osconfigzonalserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.OsConfigZonalServiceClient (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.2.2  2.1.2  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.6 

Zonal OS Config API

The OS Config service is the server-side component that allows users to manage package installations and patch jobs for Compute Engine VM instances. v1alpha

## Package

[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of OsConfigZonalServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new OsConfigZonalServiceClient({fallback: true}, gax); ```  
  
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

### operationsClient
    
    
    operationsClient: gax.OperationsClient;

### osConfigZonalServiceStub
    
    
    osConfigZonalServiceStub?: Promise<{
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

### checkCreateOSPolicyAssignmentProgress(name)
    
    
    checkCreateOSPolicyAssignmentProgress(name: string): Promise<LROperation<protos.google.cloud.osconfig.v1alpha.OSPolicyAssignment, protos.google.cloud.osconfig.v1alpha.OSPolicyAssignmentOperationMetadata>>;

Check the status of the long running operation returned by `createOSPolicyAssignment()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.osconfig.v1alpha.OSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicyassignment-class), [protos.google.cloud.osconfig.v1alpha.OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicyassignmentoperationmetadata-class)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name in the form:
       *  projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Required. The OS policy assignment to be created.
       */
      // const osPolicyAssignment = {}
      /**
       *  Required. The logical name of the OS policy assignment in the project
       *  with the following restrictions:
       *  * Must contain only lowercase letters, numbers, and hyphens.
       *  * Must start with a letter.
       *  * Must be between 1-63 characters.
       *  * Must end with a number or a letter.
       *  * Must be unique within the project.
       */
      // const osPolicyAssignmentId = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callCreateOSPolicyAssignment() {
        // Construct request
        const request = {
          parent,
          osPolicyAssignment,
          osPolicyAssignmentId,
        };
    
        // Run request
        const [operation] = await osconfigClient.createOSPolicyAssignment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateOSPolicyAssignment();
    
    

### checkDeleteOSPolicyAssignmentProgress(name)
    
    
    checkDeleteOSPolicyAssignmentProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.osconfig.v1alpha.OSPolicyAssignmentOperationMetadata>>;

Check the status of the long running operation returned by `deleteOSPolicyAssignment()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.empty), [protos.google.cloud.osconfig.v1alpha.OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicyassignmentoperationmetadata-class)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the OS policy assignment to be deleted
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callDeleteOSPolicyAssignment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await osconfigClient.deleteOSPolicyAssignment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteOSPolicyAssignment();
    
    

### checkUpdateOSPolicyAssignmentProgress(name)
    
    
    checkUpdateOSPolicyAssignmentProgress(name: string): Promise<LROperation<protos.google.cloud.osconfig.v1alpha.OSPolicyAssignment, protos.google.cloud.osconfig.v1alpha.OSPolicyAssignmentOperationMetadata>>;

Check the status of the long running operation returned by `updateOSPolicyAssignment()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.osconfig.v1alpha.OSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicyassignment-class), [protos.google.cloud.osconfig.v1alpha.OSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ospolicyassignmentoperationmetadata-class)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The updated OS policy assignment.
       */
      // const osPolicyAssignment = {}
      /**
       *  Optional. Field mask that controls which fields of the assignment should be updated.
       */
      // const updateMask = {}
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callUpdateOSPolicyAssignment() {
        // Construct request
        const request = {
          osPolicyAssignment,
        };
    
        // Run request
        const [operation] = await osconfigClient.updateOSPolicyAssignment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateOSPolicyAssignment();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createOSPolicyAssignment(request, options)
    
    
    createOSPolicyAssignment(request?: protos.google.cloud.osconfig.v1alpha.ICreateOSPolicyAssignmentRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Create an OS policy assignment.

This method also creates the first revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](<https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel>).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.icreateospolicyassignmentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment), [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name in the form:
       *  projects/{project}/locations/{location}
       */
      // const parent = 'abc123'
      /**
       *  Required. The OS policy assignment to be created.
       */
      // const osPolicyAssignment = {}
      /**
       *  Required. The logical name of the OS policy assignment in the project
       *  with the following restrictions:
       *  * Must contain only lowercase letters, numbers, and hyphens.
       *  * Must start with a letter.
       *  * Must be between 1-63 characters.
       *  * Must end with a number or a letter.
       *  * Must be unique within the project.
       */
      // const osPolicyAssignmentId = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callCreateOSPolicyAssignment() {
        // Construct request
        const request = {
          parent,
          osPolicyAssignment,
          osPolicyAssignmentId,
        };
    
        // Run request
        const [operation] = await osconfigClient.createOSPolicyAssignment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateOSPolicyAssignment();
    
    

### createOSPolicyAssignment(request, options, callback)
    
    
    createOSPolicyAssignment(request: protos.google.cloud.osconfig.v1alpha.ICreateOSPolicyAssignmentRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.icreateospolicyassignmentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment), [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createOSPolicyAssignment(request, callback)
    
    
    createOSPolicyAssignment(request: protos.google.cloud.osconfig.v1alpha.ICreateOSPolicyAssignmentRequest, callback: Callback<LROperation<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.icreateospolicyassignmentrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment), [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteOSPolicyAssignment(request, options)
    
    
    deleteOSPolicyAssignment(request?: protos.google.cloud.osconfig.v1alpha.IDeleteOSPolicyAssignmentRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Delete the OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](<https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel>).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ideleteospolicyassignmentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.iempty), [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the OS policy assignment to be deleted
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callDeleteOSPolicyAssignment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await osconfigClient.deleteOSPolicyAssignment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteOSPolicyAssignment();
    
    

### deleteOSPolicyAssignment(request, options, callback)
    
    
    deleteOSPolicyAssignment(request: protos.google.cloud.osconfig.v1alpha.IDeleteOSPolicyAssignmentRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ideleteospolicyassignmentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.iempty), [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteOSPolicyAssignment(request, callback)
    
    
    deleteOSPolicyAssignment(request: protos.google.cloud.osconfig.v1alpha.IDeleteOSPolicyAssignmentRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ideleteospolicyassignmentrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.protobuf.iempty), [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstanceOSPoliciesCompliance(request, options)
    
    
    getInstanceOSPoliciesCompliance(request?: protos.google.cloud.osconfig.v1alpha.IGetInstanceOSPoliciesComplianceRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance,
            (protos.google.cloud.osconfig.v1alpha.IGetInstanceOSPoliciesComplianceRequest | undefined),
            {} | undefined
        ]>;

Get OS policies compliance data for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinstanceospoliciescompliancerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinstanceospoliciescompliance), ([protos.google.cloud.osconfig.v1alpha.IGetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinstanceospoliciescompliancerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. API resource name for instance OS policies compliance resource.
       *  Format:
       *  `projects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}`
       *  For `{project}`, either Compute Engine project-number or project-id can be
       *  provided.
       *  For `{instance}`, either Compute Engine VM instance-id or instance-name can
       *  be provided.
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callGetInstanceOSPoliciesCompliance() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.getInstanceOSPoliciesCompliance(request);
        console.log(response);
      }
    
      callGetInstanceOSPoliciesCompliance();
    
    

### getInstanceOSPoliciesCompliance(request, options, callback)
    
    
    getInstanceOSPoliciesCompliance(request: protos.google.cloud.osconfig.v1alpha.IGetInstanceOSPoliciesComplianceRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance, protos.google.cloud.osconfig.v1alpha.IGetInstanceOSPoliciesComplianceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinstanceospoliciescompliancerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinstanceospoliciescompliance), [protos.google.cloud.osconfig.v1alpha.IGetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinstanceospoliciescompliancerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInstanceOSPoliciesCompliance(request, callback)
    
    
    getInstanceOSPoliciesCompliance(request: protos.google.cloud.osconfig.v1alpha.IGetInstanceOSPoliciesComplianceRequest, callback: Callback<protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance, protos.google.cloud.osconfig.v1alpha.IGetInstanceOSPoliciesComplianceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinstanceospoliciescompliancerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinstanceospoliciescompliance), [protos.google.cloud.osconfig.v1alpha.IGetInstanceOSPoliciesComplianceRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinstanceospoliciescompliancerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInventory(request, options)
    
    
    getInventory(request?: protos.google.cloud.osconfig.v1alpha.IGetInventoryRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IInventory,
            protos.google.cloud.osconfig.v1alpha.IGetInventoryRequest | undefined,
            {} | undefined
        ]>;

Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinventoryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IInventory](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinventory), [protos.google.cloud.osconfig.v1alpha.IGetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinventoryrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. API resource name for inventory resource.
       *  Format:
       *  `projects/{project}/locations/{location}/instances/{instance}/inventory`
       *  For `{project}`, either `project-number` or `project-id` can be provided.
       *  For `{instance}`, either Compute Engine  `instance-id` or `instance-name`
       *  can be provided.
       */
      // const name = 'abc123'
      /**
       *  Inventory view indicating what information should be included in the
       *  inventory resource. If unspecified, the default view is BASIC.
       */
      // const view = {}
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callGetInventory() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.getInventory(request);
        console.log(response);
      }
    
      callGetInventory();
    
    

### getInventory(request, options, callback)
    
    
    getInventory(request: protos.google.cloud.osconfig.v1alpha.IGetInventoryRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1alpha.IInventory, protos.google.cloud.osconfig.v1alpha.IGetInventoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinventoryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1alpha.IInventory](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinventory), [protos.google.cloud.osconfig.v1alpha.IGetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinventoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getInventory(request, callback)
    
    
    getInventory(request: protos.google.cloud.osconfig.v1alpha.IGetInventoryRequest, callback: Callback<protos.google.cloud.osconfig.v1alpha.IInventory, protos.google.cloud.osconfig.v1alpha.IGetInventoryRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinventoryrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1alpha.IInventory](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinventory), [protos.google.cloud.osconfig.v1alpha.IGetInventoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetinventoryrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOSPolicyAssignment(request, options)
    
    
    getOSPolicyAssignment(request?: protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment,
            (protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentRequest | undefined),
            {} | undefined
        ]>;

Retrieve an existing OS policy assignment.

This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment), ([protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of OS policy assignment.
       *  Format:
       *  `projects/{project}/locations/{location}/osPolicyAssignments/{os_policy_assignment}@{revisionId}`
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callGetOSPolicyAssignment() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.getOSPolicyAssignment(request);
        console.log(response);
      }
    
      callGetOSPolicyAssignment();
    
    

### getOSPolicyAssignment(request, options, callback)
    
    
    getOSPolicyAssignment(request: protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment, protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment), [protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOSPolicyAssignment(request, callback)
    
    
    getOSPolicyAssignment(request: protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentRequest, callback: Callback<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment, protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment), [protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOSPolicyAssignmentReport(request, options)
    
    
    getOSPolicyAssignmentReport(request?: protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentReportRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport,
            (protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentReportRequest | undefined),
            {} | undefined
        ]>;

Get the OS policy asssignment report for the specified Compute Engine VM instance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentreportrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentreport), ([protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentreportrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. API resource name for OS policy assignment report.
       *  Format:
       *  `/projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/report`
       *  For `{project}`, either `project-number` or `project-id` can be provided.
       *  For `{instance_id}`, either Compute Engine `instance-id` or `instance-name`
       *  can be provided.
       *  For `{assignment_id}`, the OSPolicyAssignment id must be provided.
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callGetOSPolicyAssignmentReport() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.getOSPolicyAssignmentReport(request);
        console.log(response);
      }
    
      callGetOSPolicyAssignmentReport();
    
    

### getOSPolicyAssignmentReport(request, options, callback)
    
    
    getOSPolicyAssignmentReport(request: protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentReportRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport, protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentReportRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentreportrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentreport), [protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentreportrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getOSPolicyAssignmentReport(request, callback)
    
    
    getOSPolicyAssignmentReport(request: protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentReportRequest, callback: Callback<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport, protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentReportRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentreportrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentreport), [protos.google.cloud.osconfig.v1alpha.IGetOSPolicyAssignmentReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetospolicyassignmentreportrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getVulnerabilityReport(request, options)
    
    
    getVulnerabilityReport(request?: protos.google.cloud.osconfig.v1alpha.IGetVulnerabilityReportRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport,
            (protos.google.cloud.osconfig.v1alpha.IGetVulnerabilityReportRequest | undefined),
            {} | undefined
        ]>;

Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetVulnerabilityReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetvulnerabilityreportrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ivulnerabilityreport), ([protos.google.cloud.osconfig.v1alpha.IGetVulnerabilityReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetvulnerabilityreportrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. API resource name for vulnerability resource.
       *  Format:
       *  `projects/{project}/locations/{location}/instances/{instance}/vulnerabilityReport`
       *  For `{project}`, either `project-number` or `project-id` can be provided.
       *  For `{instance}`, either Compute Engine `instance-id` or `instance-name`
       *  can be provided.
       */
      // const name = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callGetVulnerabilityReport() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await osconfigClient.getVulnerabilityReport(request);
        console.log(response);
      }
    
      callGetVulnerabilityReport();
    
    

### getVulnerabilityReport(request, options, callback)
    
    
    getVulnerabilityReport(request: protos.google.cloud.osconfig.v1alpha.IGetVulnerabilityReportRequest, options: CallOptions, callback: Callback<protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport, protos.google.cloud.osconfig.v1alpha.IGetVulnerabilityReportRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetVulnerabilityReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetvulnerabilityreportrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ivulnerabilityreport), [protos.google.cloud.osconfig.v1alpha.IGetVulnerabilityReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetvulnerabilityreportrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getVulnerabilityReport(request, callback)
    
    
    getVulnerabilityReport(request: protos.google.cloud.osconfig.v1alpha.IGetVulnerabilityReportRequest, callback: Callback<protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport, protos.google.cloud.osconfig.v1alpha.IGetVulnerabilityReportRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetVulnerabilityReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetvulnerabilityreportrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ivulnerabilityreport), [protos.google.cloud.osconfig.v1alpha.IGetVulnerabilityReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.igetvulnerabilityreportrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### instanceOSPoliciesCompliancePath(project, location, instance)
    
    
    instanceOSPoliciesCompliancePath(project: string, location: string, instance: string): string;

Return a fully-qualified instanceOSPoliciesCompliance resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`instance` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### inventoryPath(project, location, instance)
    
    
    inventoryPath(project: string, location: string, instance: string): string;

Return a fully-qualified inventory resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`instance` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### listInstanceOSPoliciesCompliances(request, options)
    
    
    listInstanceOSPoliciesCompliances(request?: protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance[],
            protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest | null,
            protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesResponse
        ]>;

List OS policies compliance data for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinstanceospoliciescompliance)[], [protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesrequest) | null, [protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listInstanceOSPoliciesCompliancesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listInstanceOSPoliciesCompliances(request, options, callback)
    
    
    listInstanceOSPoliciesCompliances(request: protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest, protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesrequest), [protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinstanceospoliciescompliance)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstanceOSPoliciesCompliances(request, callback)
    
    
    listInstanceOSPoliciesCompliances(request: protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest, protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesrequest), [protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinstanceospoliciescompliance)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInstanceOSPoliciesCompliancesAsync(request, options)
    
    
    listInstanceOSPoliciesCompliancesAsync(request?: protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance>;

Equivalent to `listInstanceOSPoliciesCompliances`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.osconfig.v1alpha.IInstanceOSPoliciesCompliance](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinstanceospoliciescompliance)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name.
       *  Format: `projects/{project}/locations/{location}`
       *  For `{project}`, either Compute Engine project-number or project-id can be
       *  provided.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of results to return.
       */
      // const pageSize = 1234
      /**
       *  A pagination token returned from a previous call to
       *  `ListInstanceOSPoliciesCompliances` that indicates where this listing
       *  should continue from.
       */
      // const pageToken = 'abc123'
      /**
       *  If provided, this field specifies the criteria that must be met by a
       *  `InstanceOSPoliciesCompliance` API resource to be included in the response.
       */
      // const filter = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callListInstanceOSPoliciesCompliances() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = osconfigClient.[listInstanceOSPoliciesCompliancesAsync](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/v1alpha.osconfigzonalserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListInstanceOSPoliciesCompliances();
    
    

### listInstanceOSPoliciesCompliancesStream(request, options)
    
    
    listInstanceOSPoliciesCompliancesStream(request?: protos.google.cloud.osconfig.v1alpha.IListInstanceOSPoliciesCompliancesRequest, options?: CallOptions): Transform;

Equivalent to `listInstanceOSPoliciesCompliances`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInstanceOSPoliciesCompliancesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinstanceospoliciescompliancesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listInstanceOSPoliciesCompliancesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listInventories(request, options)
    
    
    listInventories(request?: protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IInventory[],
            protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest | null,
            protos.google.cloud.osconfig.v1alpha.IListInventoriesResponse
        ]>;

List inventory data for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IInventory](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinventory)[], [protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesrequest) | null, [protos.google.cloud.osconfig.v1alpha.IListInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listInventoriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listInventories(request, options, callback)
    
    
    listInventories(request: protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest, protos.google.cloud.osconfig.v1alpha.IListInventoriesResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IInventory>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesrequest), [protos.google.cloud.osconfig.v1alpha.IListInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IInventory](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinventory)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInventories(request, callback)
    
    
    listInventories(request: protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest, protos.google.cloud.osconfig.v1alpha.IListInventoriesResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IInventory>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesrequest), [protos.google.cloud.osconfig.v1alpha.IListInventoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IInventory](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinventory)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listInventoriesAsync(request, options)
    
    
    listInventoriesAsync(request?: protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.osconfig.v1alpha.IInventory>;

Equivalent to `listInventories`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.osconfig.v1alpha.IInventory](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iinventory)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name.
       *  Format: `projects/{project}/locations/{location}/instances/-`
       *  For `{project}`, either `project-number` or `project-id` can be provided.
       */
      // const parent = 'abc123'
      /**
       *  Inventory view indicating what information should be included in the
       *  inventory resource. If unspecified, the default view is BASIC.
       */
      // const view = {}
      /**
       *  The maximum number of results to return.
       */
      // const pageSize = 1234
      /**
       *  A pagination token returned from a previous call to
       *  `ListInventories` that indicates where this listing
       *  should continue from.
       */
      // const pageToken = 'abc123'
      /**
       *  If provided, this field specifies the criteria that must be met by a
       *  `Inventory` API resource to be included in the response.
       */
      // const filter = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callListInventories() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = osconfigClient.listInventoriesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListInventories();
    
    

### listInventoriesStream(request, options)
    
    
    listInventoriesStream(request?: protos.google.cloud.osconfig.v1alpha.IListInventoriesRequest, options?: CallOptions): Transform;

Equivalent to `listInventories`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListInventoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistinventoriesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listInventoriesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOSPolicyAssignmentReports(request, options)
    
    
    listOSPolicyAssignmentReports(request?: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport[],
            protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest | null,
            protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsResponse
        ]>;

List OS policy asssignment reports for all Compute Engine VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentreport)[], [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsrequest) | null, [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listOSPolicyAssignmentReportsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOSPolicyAssignmentReports(request, options, callback)
    
    
    listOSPolicyAssignmentReports(request: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest, protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsrequest), [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentreport)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOSPolicyAssignmentReports(request, callback)
    
    
    listOSPolicyAssignmentReports(request: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest, protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsrequest), [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentreport)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOSPolicyAssignmentReportsAsync(request, options)
    
    
    listOSPolicyAssignmentReportsAsync(request?: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport>;

Equivalent to `listOSPolicyAssignmentReports`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentreport)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name.
       *  Format:
       *  `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}/reports`
       *  For `{project}`, either `project-number` or `project-id` can be provided.
       *  For `{instance}`, either `instance-name`, `instance-id`, or `-` can be
       *  provided. If '-' is provided, the response will include
       *  OSPolicyAssignmentReports for all instances in the project/location.
       *  For `{assignment}`, either `assignment-id` or `-` can be provided. If '-'
       *  is provided, the response will include OSPolicyAssignmentReports for all
       *  OSPolicyAssignments in the project/location.
       *  Either {instance} or {assignment} must be `-`.
       *  For example:
       *  `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/-/reports`
       *   returns all reports for the instance
       *  `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/{assignment-id}/reports`
       *   returns all the reports for the given assignment across all instances.
       *  `projects/{project}/locations/{location}/instances/-/osPolicyAssignments/-/reports`
       *   returns all the reports for all assignments across all instances.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of results to return.
       */
      // const pageSize = 1234
      /**
       *  If provided, this field specifies the criteria that must be met by the
       *  `OSPolicyAssignmentReport` API resource that is included in the response.
       */
      // const filter = 'abc123'
      /**
       *  A pagination token returned from a previous call to the
       *  `ListOSPolicyAssignmentReports` method that indicates where this listing
       *  should continue from.
       */
      // const pageToken = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callListOSPolicyAssignmentReports() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = osconfigClient.listOSPolicyAssignmentReportsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListOSPolicyAssignmentReports();
    
    

### listOSPolicyAssignmentReportsStream(request, options)
    
    
    listOSPolicyAssignmentReportsStream(request?: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentReportsRequest, options?: CallOptions): Transform;

Equivalent to `listOSPolicyAssignmentReports`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentreportsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listOSPolicyAssignmentReportsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOSPolicyAssignmentRevisions(request, options)
    
    
    listOSPolicyAssignmentRevisions(request?: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment[],
            protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest | null,
            protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsResponse
        ]>;

List the OS policy assignment revisions for a given OS policy assignment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment)[], [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsrequest) | null, [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listOSPolicyAssignmentRevisionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOSPolicyAssignmentRevisions(request, options, callback)
    
    
    listOSPolicyAssignmentRevisions(request: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest, protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsrequest), [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOSPolicyAssignmentRevisions(request, callback)
    
    
    listOSPolicyAssignmentRevisions(request: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest, protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsrequest), [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOSPolicyAssignmentRevisionsAsync(request, options)
    
    
    listOSPolicyAssignmentRevisionsAsync(request?: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment>;

Equivalent to `listOSPolicyAssignmentRevisions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the OS policy assignment to list revisions for.
       */
      // const name = 'abc123'
      /**
       *  The maximum number of revisions to return.
       */
      // const pageSize = 1234
      /**
       *  A pagination token returned from a previous call to
       *  `ListOSPolicyAssignmentRevisions` that indicates where this listing should
       *  continue from.
       */
      // const pageToken = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callListOSPolicyAssignmentRevisions() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const iterable = osconfigClient.listOSPolicyAssignmentRevisionsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListOSPolicyAssignmentRevisions();
    
    

### listOSPolicyAssignmentRevisionsStream(request, options)
    
    
    listOSPolicyAssignmentRevisionsStream(request?: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentRevisionsRequest, options?: CallOptions): Transform;

Equivalent to `listOSPolicyAssignmentRevisions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentRevisionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentrevisionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listOSPolicyAssignmentRevisionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOSPolicyAssignments(request, options)
    
    
    listOSPolicyAssignments(request?: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment[],
            protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest | null,
            protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsResponse
        ]>;

List the OS policy assignments under the parent resource.

For each OS policy assignment, the latest revision is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment)[], [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsrequest) | null, [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listOSPolicyAssignmentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOSPolicyAssignments(request, options, callback)
    
    
    listOSPolicyAssignments(request: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest, protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsrequest), [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOSPolicyAssignments(request, callback)
    
    
    listOSPolicyAssignments(request: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest, protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsrequest), [protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOSPolicyAssignmentsAsync(request, options)
    
    
    listOSPolicyAssignmentsAsync(request?: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment>;

Equivalent to `listOSPolicyAssignments`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of assignments to return.
       */
      // const pageSize = 1234
      /**
       *  A pagination token returned from a previous call to
       *  `ListOSPolicyAssignments` that indicates where this listing should continue
       *  from.
       */
      // const pageToken = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callListOSPolicyAssignments() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = osconfigClient.listOSPolicyAssignmentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListOSPolicyAssignments();
    
    

### listOSPolicyAssignmentsStream(request, options)
    
    
    listOSPolicyAssignmentsStream(request?: protos.google.cloud.osconfig.v1alpha.IListOSPolicyAssignmentsRequest, options?: CallOptions): Transform;

Equivalent to `listOSPolicyAssignments`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOSPolicyAssignmentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistospolicyassignmentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listOSPolicyAssignmentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listVulnerabilityReports(request, options)
    
    
    listVulnerabilityReports(request?: protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport[],
            protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest | null,
            protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsResponse
        ]>;

List vulnerability reports for all VM instances in the specified zone.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVulnerabilityReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ivulnerabilityreport)[], [protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsrequest) | null, [protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listVulnerabilityReportsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listVulnerabilityReports(request, options, callback)
    
    
    listVulnerabilityReports(request: protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest, protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVulnerabilityReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsrequest), [protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ivulnerabilityreport)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listVulnerabilityReports(request, callback)
    
    
    listVulnerabilityReports(request: protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest, callback: PaginationCallback<protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest, protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsResponse | null | undefined, protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVulnerabilityReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsrequest), [protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsresponse) | null | undefined, [protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ivulnerabilityreport)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listVulnerabilityReportsAsync(request, options)
    
    
    listVulnerabilityReportsAsync(request?: protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport>;

Equivalent to `listVulnerabilityReports`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVulnerabilityReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.osconfig.v1alpha.IVulnerabilityReport](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ivulnerabilityreport)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name.
       *  Format: `projects/{project}/locations/{location}/instances/-`
       *  For `{project}`, either `project-number` or `project-id` can be provided.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of results to return.
       */
      // const pageSize = 1234
      /**
       *  A pagination token returned from a previous call to
       *  `ListVulnerabilityReports` that indicates where this listing
       *  should continue from.
       */
      // const pageToken = 'abc123'
      /**
       *  If provided, this field specifies the criteria that must be met by a
       *  `vulnerabilityReport` API resource to be included in the response.
       */
      // const filter = 'abc123'
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callListVulnerabilityReports() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = osconfigClient.listVulnerabilityReportsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListVulnerabilityReports();
    
    

### listVulnerabilityReportsStream(request, options)
    
    
    listVulnerabilityReportsStream(request?: protos.google.cloud.osconfig.v1alpha.IListVulnerabilityReportsRequest, options?: CallOptions): Transform;

Equivalent to `listVulnerabilityReports`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVulnerabilityReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.ilistvulnerabilityreportsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listVulnerabilityReportsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAssignmentFromOSPolicyAssignmentReportName(oSPolicyAssignmentReportName)
    
    
    matchAssignmentFromOSPolicyAssignmentReportName(oSPolicyAssignmentReportName: string): string | number;

Parse the assignment from OSPolicyAssignmentReport resource.

**Parameter**  
---  
**Name** | **Description**  
`oSPolicyAssignmentReportName` |  `string`   
A fully-qualified path representing OSPolicyAssignmentReport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the assignment.  
  
### matchInstanceFromInstanceOSPoliciesComplianceName(instanceOSPoliciesComplianceName)
    
    
    matchInstanceFromInstanceOSPoliciesComplianceName(instanceOSPoliciesComplianceName: string): string | number;

Parse the instance from InstanceOSPoliciesCompliance resource.

**Parameter**  
---  
**Name** | **Description**  
`instanceOSPoliciesComplianceName` |  `string`   
A fully-qualified path representing InstanceOSPoliciesCompliance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the instance.  
  
### matchInstanceFromInventoryName(inventoryName)
    
    
    matchInstanceFromInventoryName(inventoryName: string): string | number;

Parse the instance from Inventory resource.

**Parameter**  
---  
**Name** | **Description**  
`inventoryName` |  `string`   
A fully-qualified path representing Inventory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the instance.  
  
### matchInstanceFromOSPolicyAssignmentReportName(oSPolicyAssignmentReportName)
    
    
    matchInstanceFromOSPolicyAssignmentReportName(oSPolicyAssignmentReportName: string): string | number;

Parse the instance from OSPolicyAssignmentReport resource.

**Parameter**  
---  
**Name** | **Description**  
`oSPolicyAssignmentReportName` |  `string`   
A fully-qualified path representing OSPolicyAssignmentReport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the instance.  
  
### matchInstanceFromVulnerabilityReportName(vulnerabilityReportName)
    
    
    matchInstanceFromVulnerabilityReportName(vulnerabilityReportName: string): string | number;

Parse the instance from VulnerabilityReport resource.

**Parameter**  
---  
**Name** | **Description**  
`vulnerabilityReportName` |  `string`   
A fully-qualified path representing VulnerabilityReport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the instance.  
  
### matchLocationFromInstanceOSPoliciesComplianceName(instanceOSPoliciesComplianceName)
    
    
    matchLocationFromInstanceOSPoliciesComplianceName(instanceOSPoliciesComplianceName: string): string | number;

Parse the location from InstanceOSPoliciesCompliance resource.

**Parameter**  
---  
**Name** | **Description**  
`instanceOSPoliciesComplianceName` |  `string`   
A fully-qualified path representing InstanceOSPoliciesCompliance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromInventoryName(inventoryName)
    
    
    matchLocationFromInventoryName(inventoryName: string): string | number;

Parse the location from Inventory resource.

**Parameter**  
---  
**Name** | **Description**  
`inventoryName` |  `string`   
A fully-qualified path representing Inventory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromOSPolicyAssignmentName(oSPolicyAssignmentName)
    
    
    matchLocationFromOSPolicyAssignmentName(oSPolicyAssignmentName: string): string | number;

Parse the location from OSPolicyAssignment resource.

**Parameter**  
---  
**Name** | **Description**  
`oSPolicyAssignmentName` |  `string`   
A fully-qualified path representing OSPolicyAssignment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromOSPolicyAssignmentReportName(oSPolicyAssignmentReportName)
    
    
    matchLocationFromOSPolicyAssignmentReportName(oSPolicyAssignmentReportName: string): string | number;

Parse the location from OSPolicyAssignmentReport resource.

**Parameter**  
---  
**Name** | **Description**  
`oSPolicyAssignmentReportName` |  `string`   
A fully-qualified path representing OSPolicyAssignmentReport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromVulnerabilityReportName(vulnerabilityReportName)
    
    
    matchLocationFromVulnerabilityReportName(vulnerabilityReportName: string): string | number;

Parse the location from VulnerabilityReport resource.

**Parameter**  
---  
**Name** | **Description**  
`vulnerabilityReportName` |  `string`   
A fully-qualified path representing VulnerabilityReport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchOsPolicyAssignmentFromOSPolicyAssignmentName(oSPolicyAssignmentName)
    
    
    matchOsPolicyAssignmentFromOSPolicyAssignmentName(oSPolicyAssignmentName: string): string | number;

Parse the os_policy_assignment from OSPolicyAssignment resource.

**Parameter**  
---  
**Name** | **Description**  
`oSPolicyAssignmentName` |  `string`   
A fully-qualified path representing OSPolicyAssignment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the os_policy_assignment.  
  
### matchProjectFromInstanceOSPoliciesComplianceName(instanceOSPoliciesComplianceName)
    
    
    matchProjectFromInstanceOSPoliciesComplianceName(instanceOSPoliciesComplianceName: string): string | number;

Parse the project from InstanceOSPoliciesCompliance resource.

**Parameter**  
---  
**Name** | **Description**  
`instanceOSPoliciesComplianceName` |  `string`   
A fully-qualified path representing InstanceOSPoliciesCompliance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromInventoryName(inventoryName)
    
    
    matchProjectFromInventoryName(inventoryName: string): string | number;

Parse the project from Inventory resource.

**Parameter**  
---  
**Name** | **Description**  
`inventoryName` |  `string`   
A fully-qualified path representing Inventory resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromOSPolicyAssignmentName(oSPolicyAssignmentName)
    
    
    matchProjectFromOSPolicyAssignmentName(oSPolicyAssignmentName: string): string | number;

Parse the project from OSPolicyAssignment resource.

**Parameter**  
---  
**Name** | **Description**  
`oSPolicyAssignmentName` |  `string`   
A fully-qualified path representing OSPolicyAssignment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromOSPolicyAssignmentReportName(oSPolicyAssignmentReportName)
    
    
    matchProjectFromOSPolicyAssignmentReportName(oSPolicyAssignmentReportName: string): string | number;

Parse the project from OSPolicyAssignmentReport resource.

**Parameter**  
---  
**Name** | **Description**  
`oSPolicyAssignmentReportName` |  `string`   
A fully-qualified path representing OSPolicyAssignmentReport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromVulnerabilityReportName(vulnerabilityReportName)
    
    
    matchProjectFromVulnerabilityReportName(vulnerabilityReportName: string): string | number;

Parse the project from VulnerabilityReport resource.

**Parameter**  
---  
**Name** | **Description**  
`vulnerabilityReportName` |  `string`   
A fully-qualified path representing VulnerabilityReport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### oSPolicyAssignmentPath(project, location, osPolicyAssignment)
    
    
    oSPolicyAssignmentPath(project: string, location: string, osPolicyAssignment: string): string;

Return a fully-qualified oSPolicyAssignment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`osPolicyAssignment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### oSPolicyAssignmentReportPath(project, location, instance, assignment)
    
    
    oSPolicyAssignmentReportPath(project: string, location: string, instance: string, assignment: string): string;

Return a fully-qualified oSPolicyAssignmentReport resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`instance` |  `string`   
  
`assignment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateOSPolicyAssignment(request, options)
    
    
    updateOSPolicyAssignment(request?: protos.google.cloud.osconfig.v1alpha.IUpdateOSPolicyAssignmentRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Update an existing OS policy assignment.

This method creates a new revision of the OS policy assignment.

This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO.

For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](<https://cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel>).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iupdateospolicyassignmentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment), [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The updated OS policy assignment.
       */
      // const osPolicyAssignment = {}
      /**
       *  Optional. Field mask that controls which fields of the assignment should be updated.
       */
      // const updateMask = {}
    
      // Imports the Osconfig library
      const {OsConfigZonalServiceClient} = require('[@google-cloud/os-config](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const osconfigClient = new [OsConfigZonalServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/overview.html)();
    
      async function callUpdateOSPolicyAssignment() {
        // Construct request
        const request = {
          osPolicyAssignment,
        };
    
        // Run request
        const [operation] = await osconfigClient.updateOSPolicyAssignment(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateOSPolicyAssignment();
    
    

### updateOSPolicyAssignment(request, options, callback)
    
    
    updateOSPolicyAssignment(request: protos.google.cloud.osconfig.v1alpha.IUpdateOSPolicyAssignmentRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iupdateospolicyassignmentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment), [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateOSPolicyAssignment(request, callback)
    
    
    updateOSPolicyAssignment(request: protos.google.cloud.osconfig.v1alpha.IUpdateOSPolicyAssignmentRequest, callback: Callback<LROperation<protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment, protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateOSPolicyAssignmentRequest](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iupdateospolicyassignmentrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignment](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignment), [protos.google.cloud.osconfig.v1alpha.IOSPolicyAssignmentOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.cloud.osconfig.v1alpha.iospolicyassignmentoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/os-config/latest/os-config/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### vulnerabilityReportPath(project, location, instance)
    
    
    vulnerabilityReportPath(project: string, location: string, instance: string): string;

Return a fully-qualified vulnerabilityReport resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`instance` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
