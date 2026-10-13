---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/v2alpha.migrationserviceclient
title: Class v2alpha.MigrationServiceClient (3.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:12.594553+00:00
---

# Class v2alpha.MigrationServiceClient (3.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/v2alpha.migrationserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v2alpha.MigrationServiceClient (3.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.1 (latest)  2.2.0  1.0.1  0.2.0  0.1.0 

Service to handle EDW migrations. v2alpha

## Package

[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of MigrationServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new MigrationServiceClient({fallback: true}, gax); ```  
  
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

### migrationServiceStub
    
    
    migrationServiceStub?: Promise<{
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

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createMigrationWorkflow(request, options)
    
    
    createMigrationWorkflow(request?: protos.google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest, options?: CallOptions): Promise<[
            protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow,
            (protos.google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest | undefined),
            {} | undefined
        ]>;

Creates a migration workflow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.icreatemigrationworkflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationworkflow), ([protos.google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.icreatemigrationworkflowrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the project to which this migration workflow belongs.
       *  Example: `projects/foo/locations/bar`
       */
      // const parent = 'abc123'
      /**
       *  Required. The migration workflow to create.
       */
      // const migrationWorkflow = {}
    
      // Imports the Migration library
      const {MigrationServiceClient} = require('[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const migrationClient = new [MigrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)();
    
      async function callCreateMigrationWorkflow() {
        // Construct request
        const request = {
          parent,
          migrationWorkflow,
        };
    
        // Run request
        const response = await migrationClient.createMigrationWorkflow(request);
        console.log(response);
      }
    
      callCreateMigrationWorkflow();
    
    

### createMigrationWorkflow(request, options, callback)
    
    
    createMigrationWorkflow(request: protos.google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest, options: CallOptions, callback: Callback<protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow, protos.google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.icreatemigrationworkflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationworkflow), [protos.google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.icreatemigrationworkflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMigrationWorkflow(request, callback)
    
    
    createMigrationWorkflow(request: protos.google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest, callback: Callback<protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow, protos.google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.icreatemigrationworkflowrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationworkflow), [protos.google.cloud.bigquery.migration.v2alpha.ICreateMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.icreatemigrationworkflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMigrationWorkflow(request, options)
    
    
    deleteMigrationWorkflow(request?: protos.google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest | undefined),
            {} | undefined
        ]>;

Deletes a migration workflow by name.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ideletemigrationworkflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.protobuf.iempty), ([protos.google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ideletemigrationworkflowrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The unique identifier for the migration workflow.
       *  Example: `projects/123/locations/us/workflows/1234`
       */
      // const name = 'abc123'
    
      // Imports the Migration library
      const {MigrationServiceClient} = require('[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const migrationClient = new [MigrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)();
    
      async function callDeleteMigrationWorkflow() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await migrationClient.deleteMigrationWorkflow(request);
        console.log(response);
      }
    
      callDeleteMigrationWorkflow();
    
    

### deleteMigrationWorkflow(request, options, callback)
    
    
    deleteMigrationWorkflow(request: protos.google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ideletemigrationworkflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.protobuf.iempty), [protos.google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ideletemigrationworkflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMigrationWorkflow(request, callback)
    
    
    deleteMigrationWorkflow(request: protos.google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ideletemigrationworkflowrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.protobuf.iempty), [protos.google.cloud.bigquery.migration.v2alpha.IDeleteMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ideletemigrationworkflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMigrationSubtask(request, options)
    
    
    getMigrationSubtask(request?: protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest, options?: CallOptions): Promise<[
            protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask,
            (protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest | undefined),
            {} | undefined
        ]>;

Gets a previously created migration subtask.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMigrationSubtaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationsubtaskrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationsubtask), ([protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationsubtaskrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The unique identifier for the migration subtask.
       *  Example: `projects/123/locations/us/workflows/1234/subtasks/543`
       */
      // const name = 'abc123'
      /**
       *  Optional. The list of fields to be retrieved.
       */
      // const readMask = {}
    
      // Imports the Migration library
      const {MigrationServiceClient} = require('[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const migrationClient = new [MigrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)();
    
      async function callGetMigrationSubtask() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await migrationClient.getMigrationSubtask(request);
        console.log(response);
      }
    
      callGetMigrationSubtask();
    
    

### getMigrationSubtask(request, options, callback)
    
    
    getMigrationSubtask(request: protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest, options: CallOptions, callback: Callback<protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask, protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMigrationSubtaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationsubtaskrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationsubtask), [protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationsubtaskrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMigrationSubtask(request, callback)
    
    
    getMigrationSubtask(request: protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest, callback: Callback<protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask, protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMigrationSubtaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationsubtaskrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationsubtask), [protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationSubtaskRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationsubtaskrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMigrationWorkflow(request, options)
    
    
    getMigrationWorkflow(request?: protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest, options?: CallOptions): Promise<[
            protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow,
            (protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest | undefined),
            {} | undefined
        ]>;

Gets a previously created migration workflow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationworkflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationworkflow), ([protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationworkflowrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The unique identifier for the migration workflow.
       *  Example: `projects/123/locations/us/workflows/1234`
       */
      // const name = 'abc123'
      /**
       *  The list of fields to be retrieved.
       */
      // const readMask = {}
    
      // Imports the Migration library
      const {MigrationServiceClient} = require('[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const migrationClient = new [MigrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)();
    
      async function callGetMigrationWorkflow() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await migrationClient.getMigrationWorkflow(request);
        console.log(response);
      }
    
      callGetMigrationWorkflow();
    
    

### getMigrationWorkflow(request, options, callback)
    
    
    getMigrationWorkflow(request: protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest, options: CallOptions, callback: Callback<protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow, protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationworkflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationworkflow), [protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationworkflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMigrationWorkflow(request, callback)
    
    
    getMigrationWorkflow(request: protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest, callback: Callback<protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow, protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationworkflowrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationworkflow), [protos.google.cloud.bigquery.migration.v2alpha.IGetMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.igetmigrationworkflowrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listMigrationSubtasks(request, options)
    
    
    listMigrationSubtasks(request?: protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest, options?: CallOptions): Promise<[
            protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask[],
            protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest | null,
            protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksResponse
        ]>;

Lists previously created migration subtasks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationSubtasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationsubtask)[], [protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksrequest) | null, [protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMigrationSubtasksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMigrationSubtasks(request, options, callback)
    
    
    listMigrationSubtasks(request: protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest, protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksResponse | null | undefined, protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationSubtasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksrequest), [protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksresponse) | null | undefined, [protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationsubtask)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMigrationSubtasks(request, callback)
    
    
    listMigrationSubtasks(request: protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest, callback: PaginationCallback<protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest, protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksResponse | null | undefined, protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationSubtasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksrequest), [protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksresponse) | null | undefined, [protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationsubtask)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMigrationSubtasksAsync(request, options)
    
    
    listMigrationSubtasksAsync(request?: protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask>;

Equivalent to `listMigrationSubtasks`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationSubtasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.bigquery.migration.v2alpha.IMigrationSubtask](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationsubtask)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The migration task of the subtasks to list.
       *  Example: `projects/123/locations/us/workflows/1234`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The list of fields to be retrieved.
       */
      // const readMask = {}
      /**
       *  Optional. The maximum number of migration tasks to return. The service may return
       *  fewer than this number.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from previous `ListMigrationSubtasks` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListMigrationSubtasks`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. The filter to apply. This can be used to get the subtasks of a specific
       *  tasks in a workflow, e.g. `migration_task = "ab012"` where `"ab012"` is the
       *  task ID (not the name in the named map).
       */
      // const filter = 'abc123'
    
      // Imports the Migration library
      const {MigrationServiceClient} = require('[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const migrationClient = new [MigrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)();
    
      async function callListMigrationSubtasks() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = migrationClient.listMigrationSubtasksAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMigrationSubtasks();
    
    

### listMigrationSubtasksStream(request, options)
    
    
    listMigrationSubtasksStream(request?: protos.google.cloud.bigquery.migration.v2alpha.IListMigrationSubtasksRequest, options?: CallOptions): Transform;

Equivalent to `listMigrationSubtasks`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationSubtasksRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationsubtasksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMigrationSubtasksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMigrationWorkflows(request, options)
    
    
    listMigrationWorkflows(request?: protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow[],
            protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest | null,
            protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsResponse
        ]>;

Lists previously created migration workflow.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationWorkflowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationworkflow)[], [protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsrequest) | null, [protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMigrationWorkflowsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMigrationWorkflows(request, options, callback)
    
    
    listMigrationWorkflows(request: protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest, protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsResponse | null | undefined, protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationWorkflowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsrequest), [protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsresponse) | null | undefined, [protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationworkflow)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMigrationWorkflows(request, callback)
    
    
    listMigrationWorkflows(request: protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest, callback: PaginationCallback<protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest, protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsResponse | null | undefined, protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationWorkflowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsrequest), [protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsresponse) | null | undefined, [protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationworkflow)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMigrationWorkflowsAsync(request, options)
    
    
    listMigrationWorkflowsAsync(request?: protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow>;

Equivalent to `listMigrationWorkflows`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationWorkflowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.bigquery.migration.v2alpha.IMigrationWorkflow](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.imigrationworkflow)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location of the migration workflows to list.
       *  Example: `projects/123/locations/us`
       */
      // const parent = 'abc123'
      /**
       *  The list of fields to be retrieved.
       */
      // const readMask = {}
      /**
       *  The maximum number of migration workflows to return. The service may return
       *  fewer than this number.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from previous `ListMigrationWorkflows` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListMigrationWorkflows`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Migration library
      const {MigrationServiceClient} = require('[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const migrationClient = new [MigrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)();
    
      async function callListMigrationWorkflows() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = migrationClient.listMigrationWorkflowsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMigrationWorkflows();
    
    

### listMigrationWorkflowsStream(request, options)
    
    
    listMigrationWorkflowsStream(request?: protos.google.cloud.bigquery.migration.v2alpha.IListMigrationWorkflowsRequest, options?: CallOptions): Transform;

Equivalent to `listMigrationWorkflows`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMigrationWorkflowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.ilistmigrationworkflowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMigrationWorkflowsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchLocationFromMigrationSubtaskName(migrationSubtaskName)
    
    
    matchLocationFromMigrationSubtaskName(migrationSubtaskName: string): string | number;

Parse the location from MigrationSubtask resource.

**Parameter**  
---  
**Name** | **Description**  
`migrationSubtaskName` |  `string`   
A fully-qualified path representing MigrationSubtask resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMigrationWorkflowName(migrationWorkflowName)
    
    
    matchLocationFromMigrationWorkflowName(migrationWorkflowName: string): string | number;

Parse the location from MigrationWorkflow resource.

**Parameter**  
---  
**Name** | **Description**  
`migrationWorkflowName` |  `string`   
A fully-qualified path representing MigrationWorkflow resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
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
  
### matchProjectFromMigrationSubtaskName(migrationSubtaskName)
    
    
    matchProjectFromMigrationSubtaskName(migrationSubtaskName: string): string | number;

Parse the project from MigrationSubtask resource.

**Parameter**  
---  
**Name** | **Description**  
`migrationSubtaskName` |  `string`   
A fully-qualified path representing MigrationSubtask resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMigrationWorkflowName(migrationWorkflowName)
    
    
    matchProjectFromMigrationWorkflowName(migrationWorkflowName: string): string | number;

Parse the project from MigrationWorkflow resource.

**Parameter**  
---  
**Name** | **Description**  
`migrationWorkflowName` |  `string`   
A fully-qualified path representing MigrationWorkflow resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchSubtaskFromMigrationSubtaskName(migrationSubtaskName)
    
    
    matchSubtaskFromMigrationSubtaskName(migrationSubtaskName: string): string | number;

Parse the subtask from MigrationSubtask resource.

**Parameter**  
---  
**Name** | **Description**  
`migrationSubtaskName` |  `string`   
A fully-qualified path representing MigrationSubtask resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the subtask.  
  
### matchWorkflowFromMigrationSubtaskName(migrationSubtaskName)
    
    
    matchWorkflowFromMigrationSubtaskName(migrationSubtaskName: string): string | number;

Parse the workflow from MigrationSubtask resource.

**Parameter**  
---  
**Name** | **Description**  
`migrationSubtaskName` |  `string`   
A fully-qualified path representing MigrationSubtask resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the workflow.  
  
### matchWorkflowFromMigrationWorkflowName(migrationWorkflowName)
    
    
    matchWorkflowFromMigrationWorkflowName(migrationWorkflowName: string): string | number;

Parse the workflow from MigrationWorkflow resource.

**Parameter**  
---  
**Name** | **Description**  
`migrationWorkflowName` |  `string`   
A fully-qualified path representing MigrationWorkflow resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the workflow.  
  
### migrationSubtaskPath(project, location, workflow, subtask)
    
    
    migrationSubtaskPath(project: string, location: string, workflow: string, subtask: string): string;

Return a fully-qualified migrationSubtask resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`workflow` |  `string`   
  
`subtask` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### migrationWorkflowPath(project, location, workflow)
    
    
    migrationWorkflowPath(project: string, location: string, workflow: string): string;

Return a fully-qualified migrationWorkflow resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`workflow` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### startMigrationWorkflow(request, options)
    
    
    startMigrationWorkflow(request?: protos.google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest | undefined),
            {} | undefined
        ]>;

Starts a previously created migration workflow. I.e., the state transitions from DRAFT to RUNNING. This is a no-op if the state is already RUNNING. An error will be signaled if the state is anything other than DRAFT or RUNNING.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.istartmigrationworkflowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.protobuf.iempty), ([protos.google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.istartmigrationworkflowrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The unique identifier for the migration workflow.
       *  Example: `projects/123/locations/us/workflows/1234`
       */
      // const name = 'abc123'
    
      // Imports the Migration library
      const {MigrationServiceClient} = require('[@google-cloud/bigquery-migration](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const migrationClient = new [MigrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/overview.html)();
    
      async function callStartMigrationWorkflow() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await migrationClient.startMigrationWorkflow(request);
        console.log(response);
      }
    
      callStartMigrationWorkflow();
    
    

### startMigrationWorkflow(request, options, callback)
    
    
    startMigrationWorkflow(request: protos.google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.istartmigrationworkflowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.protobuf.iempty), [protos.google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.istartmigrationworkflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startMigrationWorkflow(request, callback)
    
    
    startMigrationWorkflow(request: protos.google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.istartmigrationworkflowrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.protobuf.iempty), [protos.google.cloud.bigquery.migration.v2alpha.IStartMigrationWorkflowRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-migration/latest/bigquery-migration/protos.google.cloud.bigquery.migration.v2alpha.istartmigrationworkflowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
