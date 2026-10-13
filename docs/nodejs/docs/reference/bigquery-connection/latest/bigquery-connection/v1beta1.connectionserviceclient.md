---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/v1beta1.connectionserviceclient
title: Class v1beta1.ConnectionServiceClient (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:01.248484+00:00
---

# Class v1beta1.ConnectionServiceClient (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/v1beta1.connectionserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.ConnectionServiceClient (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  2.2.1  2.1.1  2.0.2  1.5.1  1.4.2  1.3.5 

Manages external data source connections and credentials. v1beta1

## Package

[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of ConnectionServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new ConnectionServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### connectionServiceStub
    
    
    connectionServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### descriptors
    
    
    descriptors: Descriptors;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

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
  
### connectionPath(project, location, connection)
    
    
    connectionPath(project: string, location: string, connection: string): string;

Return a fully-qualified connection resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`connection` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createConnection(request, options)
    
    
    createConnection(request?: protos.google.cloud.bigquery.connection.v1beta1.ICreateConnectionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.bigquery.connection.v1beta1.IConnection,
            (protos.google.cloud.bigquery.connection.v1beta1.ICreateConnectionRequest | undefined),
            {} | undefined
        ]>;

Creates a new connection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.icreateconnectionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.bigquery.connection.v1beta1.IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iconnection), ([protos.google.cloud.bigquery.connection.v1beta1.ICreateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.icreateconnectionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.connection). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent resource name.
       *  Must be in the format `projects/{project_id}/locations/{location_id}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Connection id that should be assigned to the created connection.
       */
      // const connectionId = 'abc123'
      /**
       *  Required. Connection to create.
       */
      // const connection = {}
    
      // Imports the Connection library
      const {ConnectionServiceClient} = require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const connectionClient = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
      async function callCreateConnection() {
        // Construct request
        const request = {
          parent,
          connection,
        };
    
        // Run request
        const response = await connectionClient.createConnection(request);
        console.log(response);
      }
    
      callCreateConnection();
    
    

### createConnection(request, options, callback)
    
    
    createConnection(request: protos.google.cloud.bigquery.connection.v1beta1.ICreateConnectionRequest, options: CallOptions, callback: Callback<protos.google.cloud.bigquery.connection.v1beta1.IConnection, protos.google.cloud.bigquery.connection.v1beta1.ICreateConnectionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.icreateconnectionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.connection.v1beta1.IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iconnection), [protos.google.cloud.bigquery.connection.v1beta1.ICreateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.icreateconnectionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConnection(request, callback)
    
    
    createConnection(request: protos.google.cloud.bigquery.connection.v1beta1.ICreateConnectionRequest, callback: Callback<protos.google.cloud.bigquery.connection.v1beta1.IConnection, protos.google.cloud.bigquery.connection.v1beta1.ICreateConnectionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.icreateconnectionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.connection.v1beta1.IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iconnection), [protos.google.cloud.bigquery.connection.v1beta1.ICreateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.icreateconnectionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConnection(request, options)
    
    
    deleteConnection(request?: protos.google.cloud.bigquery.connection.v1beta1.IDeleteConnectionRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.bigquery.connection.v1beta1.IDeleteConnectionRequest | undefined),
            {} | undefined
        ]>;

Deletes connection and associated credential.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ideleteconnectionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.protobuf.iempty), ([protos.google.cloud.bigquery.connection.v1beta1.IDeleteConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ideleteconnectionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the deleted connection, for example:
       *  `projects/{project_id}/locations/{location_id}/connections/{connection_id}`
       */
      // const name = 'abc123'
    
      // Imports the Connection library
      const {ConnectionServiceClient} = require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const connectionClient = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
      async function callDeleteConnection() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await connectionClient.deleteConnection(request);
        console.log(response);
      }
    
      callDeleteConnection();
    
    

### deleteConnection(request, options, callback)
    
    
    deleteConnection(request: protos.google.cloud.bigquery.connection.v1beta1.IDeleteConnectionRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.bigquery.connection.v1beta1.IDeleteConnectionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ideleteconnectionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.protobuf.iempty), [protos.google.cloud.bigquery.connection.v1beta1.IDeleteConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ideleteconnectionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConnection(request, callback)
    
    
    deleteConnection(request: protos.google.cloud.bigquery.connection.v1beta1.IDeleteConnectionRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.bigquery.connection.v1beta1.IDeleteConnectionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ideleteconnectionrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.protobuf.iempty), [protos.google.cloud.bigquery.connection.v1beta1.IDeleteConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ideleteconnectionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnection(request, options)
    
    
    getConnection(request?: protos.google.cloud.bigquery.connection.v1beta1.IGetConnectionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.bigquery.connection.v1beta1.IConnection,
            (protos.google.cloud.bigquery.connection.v1beta1.IGetConnectionRequest | undefined),
            {} | undefined
        ]>;

Returns specified connection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.igetconnectionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.bigquery.connection.v1beta1.IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iconnection), ([protos.google.cloud.bigquery.connection.v1beta1.IGetConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.igetconnectionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.connection). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the requested connection, for example:
       *  `projects/{project_id}/locations/{location_id}/connections/{connection_id}`
       */
      // const name = 'abc123'
    
      // Imports the Connection library
      const {ConnectionServiceClient} = require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const connectionClient = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
      async function callGetConnection() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await connectionClient.getConnection(request);
        console.log(response);
      }
    
      callGetConnection();
    
    

### getConnection(request, options, callback)
    
    
    getConnection(request: protos.google.cloud.bigquery.connection.v1beta1.IGetConnectionRequest, options: CallOptions, callback: Callback<protos.google.cloud.bigquery.connection.v1beta1.IConnection, protos.google.cloud.bigquery.connection.v1beta1.IGetConnectionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.igetconnectionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.connection.v1beta1.IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iconnection), [protos.google.cloud.bigquery.connection.v1beta1.IGetConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.igetconnectionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConnection(request, callback)
    
    
    getConnection(request: protos.google.cloud.bigquery.connection.v1beta1.IGetConnectionRequest, callback: Callback<protos.google.cloud.bigquery.connection.v1beta1.IConnection, protos.google.cloud.bigquery.connection.v1beta1.IGetConnectionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.igetconnectionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.connection.v1beta1.IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iconnection), [protos.google.cloud.bigquery.connection.v1beta1.IGetConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.igetconnectionrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.igetiampolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.igetiampolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Connection library
      const {ConnectionServiceClient} = require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const connectionClient = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
      async function callGetIamPolicy() {
        // Construct request
        const request = {
          resource,
        };
    
        // Run request
        const response = await connectionClient.getIamPolicy(request);
        console.log(response);
      }
    
      callGetIamPolicy();
    
    

### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: protos.google.iam.v1.IGetIamPolicyRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.IGetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.igetiampolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.igetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, callback)
    
    
    getIamPolicy(request: protos.google.iam.v1.IGetIamPolicyRequest, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.IGetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.igetiampolicyrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.igetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listConnections(request, options)
    
    
    listConnections(request?: protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsResponse,
            (protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsRequest | undefined),
            {} | undefined
        ]>;

Returns a list of connections in the given project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ilistconnectionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ilistconnectionsresponse), ([protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ilistconnectionsrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ListConnectionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.listconnectionsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent resource name.
       *  Must be in the form: `projects/{project_id}/locations/{location_id}`
       */
      // const parent = 'abc123'
      /**
       *  Required. Maximum number of results per page.
       */
      // const maxResults = {}
      /**
       *  Page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Connection library
      const {ConnectionServiceClient} = require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const connectionClient = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
      async function callListConnections() {
        // Construct request
        const request = {
          parent,
          maxResults,
        };
    
        // Run request
        const response = await connectionClient.listConnections(request);
        console.log(response);
      }
    
      callListConnections();
    
    

### listConnections(request, options, callback)
    
    
    listConnections(request: protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsRequest, options: CallOptions, callback: Callback<protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsResponse, protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ilistconnectionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ilistconnectionsresponse), [protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ilistconnectionsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConnections(request, callback)
    
    
    listConnections(request: protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsRequest, callback: Callback<protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsResponse, protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ilistconnectionsrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ilistconnectionsresponse), [protos.google.cloud.bigquery.connection.v1beta1.IListConnectionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.ilistconnectionsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### matchConnectionFromConnectionName(connectionName)
    
    
    matchConnectionFromConnectionName(connectionName: string): string | number;

Parse the connection from Connection resource.

**Parameter**  
---  
**Name** | **Description**  
`connectionName` |  `string`   
A fully-qualified path representing Connection resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the connection.  
  
### matchLocationFromConnectionName(connectionName)
    
    
    matchLocationFromConnectionName(connectionName: string): string | number;

Parse the location from Connection resource.

**Parameter**  
---  
**Name** | **Description**  
`connectionName` |  `string`   
A fully-qualified path representing Connection resource.  
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
  
### matchProjectFromConnectionName(connectionName)
    
    
    matchProjectFromConnectionName(connectionName: string): string | number;

Parse the project from Connection resource.

**Parameter**  
---  
**Name** | **Description**  
`connectionName` |  `string`   
A fully-qualified path representing Connection resource.  
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
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.isetiampolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.isetiampolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Connection library
      const {ConnectionServiceClient} = require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const connectionClient = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
      async function callSetIamPolicy() {
        // Construct request
        const request = {
          resource,
          policy,
        };
    
        // Run request
        const response = await connectionClient.setIamPolicy(request);
        console.log(response);
      }
    
      callSetIamPolicy();
    
    

### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: protos.google.iam.v1.ISetIamPolicyRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.ISetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.isetiampolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.isetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, callback)
    
    
    setIamPolicy(request: protos.google.iam.v1.ISetIamPolicyRequest, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.ISetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.isetiampolicyrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.isetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.ITestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsresponse), [protos.google.iam.v1.ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.testiampermissionsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Connection library
      const {ConnectionServiceClient} = require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const connectionClient = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
      async function callTestIamPermissions() {
        // Construct request
        const request = {
          resource,
          permissions,
        };
    
        // Run request
        const response = await connectionClient.testIamPermissions(request);
        console.log(response);
      }
    
      callTestIamPermissions();
    
    

### testIamPermissions(request, options, callback)
    
    
    testIamPermissions(request: protos.google.iam.v1.ITestIamPermissionsRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.ITestIamPermissionsResponse, protos.google.iam.v1.ITestIamPermissionsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.ITestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsresponse), [protos.google.iam.v1.ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, callback)
    
    
    testIamPermissions(request: protos.google.iam.v1.ITestIamPermissionsRequest, callback: Callback<protos.google.iam.v1.ITestIamPermissionsResponse, protos.google.iam.v1.ITestIamPermissionsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.ITestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsresponse), [protos.google.iam.v1.ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.iam.v1.itestiampermissionsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConnection(request, options)
    
    
    updateConnection(request?: protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.bigquery.connection.v1beta1.IConnection,
            (protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionRequest | undefined),
            {} | undefined
        ]>;

Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.bigquery.connection.v1beta1.IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iconnection), ([protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.connection). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the connection to update, for example:
       *  `projects/{project_id}/locations/{location_id}/connections/{connection_id}`
       */
      // const name = 'abc123'
      /**
       *  Required. Connection containing the updated fields.
       */
      // const connection = {}
      /**
       *  Required. Update mask for the connection fields to be updated.
       */
      // const updateMask = {}
    
      // Imports the Connection library
      const {ConnectionServiceClient} = require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const connectionClient = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
      async function callUpdateConnection() {
        // Construct request
        const request = {
          name,
          connection,
          updateMask,
        };
    
        // Run request
        const response = await connectionClient.updateConnection(request);
        console.log(response);
      }
    
      callUpdateConnection();
    
    

### updateConnection(request, options, callback)
    
    
    updateConnection(request: protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionRequest, options: CallOptions, callback: Callback<protos.google.cloud.bigquery.connection.v1beta1.IConnection, protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.connection.v1beta1.IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iconnection), [protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConnection(request, callback)
    
    
    updateConnection(request: protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionRequest, callback: Callback<protos.google.cloud.bigquery.connection.v1beta1.IConnection, protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.bigquery.connection.v1beta1.IConnection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iconnection), [protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConnectionCredential(request, options)
    
    
    updateConnectionCredential(request?: protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionCredentialRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionCredentialRequest | undefined),
            {} | undefined
        ]>;

Sets the credential for the specified connection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectioncredentialrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.protobuf.iempty), ([protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectioncredentialrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the connection, for example:
       *  `projects/{project_id}/locations/{location_id}/connections/{connection_id}/credential`
       */
      // const name = 'abc123'
      /**
       *  Required. Credential to use with the connection.
       */
      // const credential = {}
    
      // Imports the Connection library
      const {ConnectionServiceClient} = require('[@google-cloud/bigquery-connection](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const connectionClient = new [ConnectionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/overview.html)();
    
      async function callUpdateConnectionCredential() {
        // Construct request
        const request = {
          name,
          credential,
        };
    
        // Run request
        const response = await connectionClient.updateConnectionCredential(request);
        console.log(response);
      }
    
      callUpdateConnectionCredential();
    
    

### updateConnectionCredential(request, options, callback)
    
    
    updateConnectionCredential(request: protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionCredentialRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionCredentialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectioncredentialrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.protobuf.iempty), [protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectioncredentialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConnectionCredential(request, callback)
    
    
    updateConnectionCredential(request: protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionCredentialRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionCredentialRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConnectionCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectioncredentialrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.protobuf.iempty), [protos.google.cloud.bigquery.connection.v1beta1.IUpdateConnectionCredentialRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-connection/latest/bigquery-connection/protos.google.cloud.bigquery.connection.v1beta1.iupdateconnectioncredentialrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
