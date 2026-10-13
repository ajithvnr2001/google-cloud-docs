---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1beta1.networksecurityclient
title: Class v1beta1.NetworkSecurityClient (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:33.566222+00:00
---

# Class v1beta1.NetworkSecurityClient (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1beta1.networksecurityclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.NetworkSecurityClient (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.6.0  3.1.0  1.1.2  1.0.2  0.5.0  0.3.0  0.2.0 

Network Security API provides resources to configure authentication and authorization policies. Refer to per API resource documentation for more information. v1beta1

## Package

[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of NetworkSecurityClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new NetworkSecurityClient({fallback: true}, gax); ```  
  
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

### iamClient
    
    
    iamClient: IamClient;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### locationsClient
    
    
    locationsClient: LocationsClient;

### networkSecurityStub
    
    
    networkSecurityStub?: Promise<{
            [name: string]: Function;
        }>;

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

### authorizationPolicyPath(project, location, authorizationPolicy)
    
    
    authorizationPolicyPath(project: string, location: string, authorizationPolicy: string): string;

Return a fully-qualified authorizationPolicy resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`authorizationPolicy` |  `string`   
  
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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreateAuthorizationPolicyProgress(name)
    
    
    checkCreateAuthorizationPolicyProgress(name: string): Promise<LROperation<protos.google.cloud.networksecurity.v1beta1.AuthorizationPolicy, protos.google.cloud.networksecurity.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `createAuthorizationPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networksecurity.v1beta1.AuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.authorizationpolicy-class), [protos.google.cloud.networksecurity.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource of the AuthorizationPolicy. Must be in the
       *  format `projects/{project}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Short name of the AuthorizationPolicy resource to be created.
       *  This value should be 1-63 characters long, containing only
       *  letters, numbers, hyphens, and underscores, and should not start
       *  with a number. E.g. "authz_policy".
       */
      // const authorizationPolicyId = 'abc123'
      /**
       *  Required. AuthorizationPolicy resource to be created.
       */
      // const authorizationPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callCreateAuthorizationPolicy() {
        // Construct request
        const request = {
          parent,
          authorizationPolicyId,
          authorizationPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.createAuthorizationPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateAuthorizationPolicy();
    
    

### checkCreateClientTlsPolicyProgress(name)
    
    
    checkCreateClientTlsPolicyProgress(name: string): Promise<LROperation<protos.google.cloud.networksecurity.v1beta1.ClientTlsPolicy, protos.google.cloud.networksecurity.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `createClientTlsPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networksecurity.v1beta1.ClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.clienttlspolicy), [protos.google.cloud.networksecurity.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource of the ClientTlsPolicy. Must be in
       *  the format `projects/* /locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Short name of the ClientTlsPolicy resource to be created. This
       *  value should be 1-63 characters long, containing only letters, numbers,
       *  hyphens, and underscores, and should not start with a number. E.g.
       *  "client_mtls_policy".
       */
      // const clientTlsPolicyId = 'abc123'
      /**
       *  Required. ClientTlsPolicy resource to be created.
       */
      // const clientTlsPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callCreateClientTlsPolicy() {
        // Construct request
        const request = {
          parent,
          clientTlsPolicyId,
          clientTlsPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.createClientTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateClientTlsPolicy();
    
    

### checkCreateServerTlsPolicyProgress(name)
    
    
    checkCreateServerTlsPolicyProgress(name: string): Promise<LROperation<protos.google.cloud.networksecurity.v1beta1.ServerTlsPolicy, protos.google.cloud.networksecurity.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `createServerTlsPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networksecurity.v1beta1.ServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.servertlspolicy-class), [protos.google.cloud.networksecurity.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource of the ServerTlsPolicy. Must be in
       *  the format `projects/* /locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Short name of the ServerTlsPolicy resource to be created. This
       *  value should be 1-63 characters long, containing only letters, numbers,
       *  hyphens, and underscores, and should not start with a number. E.g.
       *  "server_mtls_policy".
       */
      // const serverTlsPolicyId = 'abc123'
      /**
       *  Required. ServerTlsPolicy resource to be created.
       */
      // const serverTlsPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callCreateServerTlsPolicy() {
        // Construct request
        const request = {
          parent,
          serverTlsPolicyId,
          serverTlsPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.createServerTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateServerTlsPolicy();
    
    

### checkDeleteAuthorizationPolicyProgress(name)
    
    
    checkDeleteAuthorizationPolicyProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.networksecurity.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteAuthorizationPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty), [protos.google.cloud.networksecurity.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A name of the AuthorizationPolicy to delete. Must be in the
       *  format `projects/{project}/locations/{location}/authorizationPolicies/*`.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callDeleteAuthorizationPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networksecurityClient.deleteAuthorizationPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteAuthorizationPolicy();
    
    

### checkDeleteClientTlsPolicyProgress(name)
    
    
    checkDeleteClientTlsPolicyProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.networksecurity.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteClientTlsPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty), [protos.google.cloud.networksecurity.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A name of the ClientTlsPolicy to delete. Must be in
       *  the format `projects/* /locations/{location}/clientTlsPolicies/*`.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callDeleteClientTlsPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networksecurityClient.deleteClientTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteClientTlsPolicy();
    
    

### checkDeleteServerTlsPolicyProgress(name)
    
    
    checkDeleteServerTlsPolicyProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.networksecurity.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteServerTlsPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty), [protos.google.cloud.networksecurity.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A name of the ServerTlsPolicy to delete. Must be in
       *  the format `projects/* /locations/{location}/serverTlsPolicies/*`.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callDeleteServerTlsPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networksecurityClient.deleteServerTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteServerTlsPolicy();
    
    

### checkUpdateAuthorizationPolicyProgress(name)
    
    
    checkUpdateAuthorizationPolicyProgress(name: string): Promise<LROperation<protos.google.cloud.networksecurity.v1beta1.AuthorizationPolicy, protos.google.cloud.networksecurity.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `updateAuthorizationPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networksecurity.v1beta1.AuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.authorizationpolicy-class), [protos.google.cloud.networksecurity.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  AuthorizationPolicy resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. Updated AuthorizationPolicy resource.
       */
      // const authorizationPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callUpdateAuthorizationPolicy() {
        // Construct request
        const request = {
          authorizationPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.updateAuthorizationPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateAuthorizationPolicy();
    
    

### checkUpdateClientTlsPolicyProgress(name)
    
    
    checkUpdateClientTlsPolicyProgress(name: string): Promise<LROperation<protos.google.cloud.networksecurity.v1beta1.ClientTlsPolicy, protos.google.cloud.networksecurity.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `updateClientTlsPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networksecurity.v1beta1.ClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.clienttlspolicy), [protos.google.cloud.networksecurity.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  ClientTlsPolicy resource by the update.  The fields
       *  specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the
       *  mask. If the user does not provide a mask then all fields will be
       *  overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. Updated ClientTlsPolicy resource.
       */
      // const clientTlsPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callUpdateClientTlsPolicy() {
        // Construct request
        const request = {
          clientTlsPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.updateClientTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateClientTlsPolicy();
    
    

### checkUpdateServerTlsPolicyProgress(name)
    
    
    checkUpdateServerTlsPolicyProgress(name: string): Promise<LROperation<protos.google.cloud.networksecurity.v1beta1.ServerTlsPolicy, protos.google.cloud.networksecurity.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `updateServerTlsPolicy()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networksecurity.v1beta1.ServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.servertlspolicy-class), [protos.google.cloud.networksecurity.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  ServerTlsPolicy resource by the update.  The fields
       *  specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the
       *  mask. If the user does not provide a mask then all fields will be
       *  overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. Updated ServerTlsPolicy resource.
       */
      // const serverTlsPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callUpdateServerTlsPolicy() {
        // Construct request
        const request = {
          serverTlsPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.updateServerTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateServerTlsPolicy();
    
    

### clientTlsPolicyPath(project, location, clientTlsPolicy)
    
    
    clientTlsPolicyPath(project: string, location: string, clientTlsPolicy: string): string;

Return a fully-qualified clientTlsPolicy resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`clientTlsPolicy` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createAuthorizationPolicy(request, options)
    
    
    createAuthorizationPolicy(request?: protos.google.cloud.networksecurity.v1beta1.ICreateAuthorizationPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new AuthorizationPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreateauthorizationpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource of the AuthorizationPolicy. Must be in the
       *  format `projects/{project}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Short name of the AuthorizationPolicy resource to be created.
       *  This value should be 1-63 characters long, containing only
       *  letters, numbers, hyphens, and underscores, and should not start
       *  with a number. E.g. "authz_policy".
       */
      // const authorizationPolicyId = 'abc123'
      /**
       *  Required. AuthorizationPolicy resource to be created.
       */
      // const authorizationPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callCreateAuthorizationPolicy() {
        // Construct request
        const request = {
          parent,
          authorizationPolicyId,
          authorizationPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.createAuthorizationPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateAuthorizationPolicy();
    
    

### createAuthorizationPolicy(request, options, callback)
    
    
    createAuthorizationPolicy(request: protos.google.cloud.networksecurity.v1beta1.ICreateAuthorizationPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreateauthorizationpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAuthorizationPolicy(request, callback)
    
    
    createAuthorizationPolicy(request: protos.google.cloud.networksecurity.v1beta1.ICreateAuthorizationPolicyRequest, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreateauthorizationpolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createClientTlsPolicy(request, options)
    
    
    createClientTlsPolicy(request?: protos.google.cloud.networksecurity.v1beta1.ICreateClientTlsPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new ClientTlsPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreateclienttlspolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource of the ClientTlsPolicy. Must be in
       *  the format `projects/* /locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Short name of the ClientTlsPolicy resource to be created. This
       *  value should be 1-63 characters long, containing only letters, numbers,
       *  hyphens, and underscores, and should not start with a number. E.g.
       *  "client_mtls_policy".
       */
      // const clientTlsPolicyId = 'abc123'
      /**
       *  Required. ClientTlsPolicy resource to be created.
       */
      // const clientTlsPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callCreateClientTlsPolicy() {
        // Construct request
        const request = {
          parent,
          clientTlsPolicyId,
          clientTlsPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.createClientTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateClientTlsPolicy();
    
    

### createClientTlsPolicy(request, options, callback)
    
    
    createClientTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.ICreateClientTlsPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreateclienttlspolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createClientTlsPolicy(request, callback)
    
    
    createClientTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.ICreateClientTlsPolicyRequest, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreateclienttlspolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createServerTlsPolicy(request, options)
    
    
    createServerTlsPolicy(request?: protos.google.cloud.networksecurity.v1beta1.ICreateServerTlsPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new ServerTlsPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreateservertlspolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource of the ServerTlsPolicy. Must be in
       *  the format `projects/* /locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Short name of the ServerTlsPolicy resource to be created. This
       *  value should be 1-63 characters long, containing only letters, numbers,
       *  hyphens, and underscores, and should not start with a number. E.g.
       *  "server_mtls_policy".
       */
      // const serverTlsPolicyId = 'abc123'
      /**
       *  Required. ServerTlsPolicy resource to be created.
       */
      // const serverTlsPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callCreateServerTlsPolicy() {
        // Construct request
        const request = {
          parent,
          serverTlsPolicyId,
          serverTlsPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.createServerTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateServerTlsPolicy();
    
    

### createServerTlsPolicy(request, options, callback)
    
    
    createServerTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.ICreateServerTlsPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreateservertlspolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createServerTlsPolicy(request, callback)
    
    
    createServerTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.ICreateServerTlsPolicyRequest, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreateservertlspolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAuthorizationPolicy(request, options)
    
    
    deleteAuthorizationPolicy(request?: protos.google.cloud.networksecurity.v1beta1.IDeleteAuthorizationPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideleteauthorizationpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A name of the AuthorizationPolicy to delete. Must be in the
       *  format `projects/{project}/locations/{location}/authorizationPolicies/*`.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callDeleteAuthorizationPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networksecurityClient.deleteAuthorizationPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteAuthorizationPolicy();
    
    

### deleteAuthorizationPolicy(request, options, callback)
    
    
    deleteAuthorizationPolicy(request: protos.google.cloud.networksecurity.v1beta1.IDeleteAuthorizationPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideleteauthorizationpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAuthorizationPolicy(request, callback)
    
    
    deleteAuthorizationPolicy(request: protos.google.cloud.networksecurity.v1beta1.IDeleteAuthorizationPolicyRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideleteauthorizationpolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteClientTlsPolicy(request, options)
    
    
    deleteClientTlsPolicy(request?: protos.google.cloud.networksecurity.v1beta1.IDeleteClientTlsPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideleteclienttlspolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A name of the ClientTlsPolicy to delete. Must be in
       *  the format `projects/* /locations/{location}/clientTlsPolicies/*`.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callDeleteClientTlsPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networksecurityClient.deleteClientTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteClientTlsPolicy();
    
    

### deleteClientTlsPolicy(request, options, callback)
    
    
    deleteClientTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IDeleteClientTlsPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideleteclienttlspolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteClientTlsPolicy(request, callback)
    
    
    deleteClientTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IDeleteClientTlsPolicyRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideleteclienttlspolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deleteServerTlsPolicy(request, options)
    
    
    deleteServerTlsPolicy(request?: protos.google.cloud.networksecurity.v1beta1.IDeleteServerTlsPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideleteservertlspolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A name of the ServerTlsPolicy to delete. Must be in
       *  the format `projects/* /locations/{location}/serverTlsPolicies/*`.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callDeleteServerTlsPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networksecurityClient.deleteServerTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteServerTlsPolicy();
    
    

### deleteServerTlsPolicy(request, options, callback)
    
    
    deleteServerTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IDeleteServerTlsPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideleteservertlspolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteServerTlsPolicy(request, callback)
    
    
    deleteServerTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IDeleteServerTlsPolicyRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideleteservertlspolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### dnsThreatDetectorPath(project, location, dnsThreatDetector)
    
    
    dnsThreatDetectorPath(project: string, location: string, dnsThreatDetector: string): string;

Return a fully-qualified dnsThreatDetector resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dnsThreatDetector` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getAuthorizationPolicy(request, options)
    
    
    getAuthorizationPolicy(request?: protos.google.cloud.networksecurity.v1beta1.IGetAuthorizationPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy,
            (protos.google.cloud.networksecurity.v1beta1.IGetAuthorizationPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetauthorizationpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy), ([protos.google.cloud.networksecurity.v1beta1.IGetAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetauthorizationpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A name of the AuthorizationPolicy to get. Must be in the format
       *  `projects/{project}/locations/{location}/authorizationPolicies/*`.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callGetAuthorizationPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networksecurityClient.getAuthorizationPolicy(request);
        console.log(response);
      }
    
      callGetAuthorizationPolicy();
    
    

### getAuthorizationPolicy(request, options, callback)
    
    
    getAuthorizationPolicy(request: protos.google.cloud.networksecurity.v1beta1.IGetAuthorizationPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy, protos.google.cloud.networksecurity.v1beta1.IGetAuthorizationPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetauthorizationpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy), [protos.google.cloud.networksecurity.v1beta1.IGetAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetauthorizationpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAuthorizationPolicy(request, callback)
    
    
    getAuthorizationPolicy(request: protos.google.cloud.networksecurity.v1beta1.IGetAuthorizationPolicyRequest, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy, protos.google.cloud.networksecurity.v1beta1.IGetAuthorizationPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetauthorizationpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy), [protos.google.cloud.networksecurity.v1beta1.IGetAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetauthorizationpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getClientTlsPolicy(request, options)
    
    
    getClientTlsPolicy(request?: protos.google.cloud.networksecurity.v1beta1.IGetClientTlsPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy,
            (protos.google.cloud.networksecurity.v1beta1.IGetClientTlsPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetclienttlspolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy), ([protos.google.cloud.networksecurity.v1beta1.IGetClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetclienttlspolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.clienttlspolicy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A name of the ClientTlsPolicy to get. Must be in the format
       *  `projects/* /locations/{location}/clientTlsPolicies/*`.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callGetClientTlsPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networksecurityClient.getClientTlsPolicy(request);
        console.log(response);
      }
    
      callGetClientTlsPolicy();
    
    

### getClientTlsPolicy(request, options, callback)
    
    
    getClientTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IGetClientTlsPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IGetClientTlsPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetclienttlspolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy), [protos.google.cloud.networksecurity.v1beta1.IGetClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetclienttlspolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getClientTlsPolicy(request, callback)
    
    
    getClientTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IGetClientTlsPolicyRequest, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IGetClientTlsPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetclienttlspolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy), [protos.google.cloud.networksecurity.v1beta1.IGetClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetclienttlspolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.operation)]>` |   
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
  
### getServerTlsPolicy(request, options)
    
    
    getServerTlsPolicy(request?: protos.google.cloud.networksecurity.v1beta1.IGetServerTlsPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy,
            (protos.google.cloud.networksecurity.v1beta1.IGetServerTlsPolicyRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetservertlspolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy), ([protos.google.cloud.networksecurity.v1beta1.IGetServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetservertlspolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A name of the ServerTlsPolicy to get. Must be in the format
       *  `projects/* /locations/{location}/serverTlsPolicies/*`.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callGetServerTlsPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networksecurityClient.getServerTlsPolicy(request);
        console.log(response);
      }
    
      callGetServerTlsPolicy();
    
    

### getServerTlsPolicy(request, options, callback)
    
    
    getServerTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IGetServerTlsPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IGetServerTlsPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetservertlspolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy), [protos.google.cloud.networksecurity.v1beta1.IGetServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetservertlspolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getServerTlsPolicy(request, callback)
    
    
    getServerTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IGetServerTlsPolicyRequest, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IGetServerTlsPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetservertlspolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy), [protos.google.cloud.networksecurity.v1beta1.IGetServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetservertlspolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listAuthorizationPolicies(request, options)
    
    
    listAuthorizationPolicies(request?: protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy[],
            protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest | null,
            protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesResponse
        ]>;

Lists AuthorizationPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuthorizationPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy)[], [protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesrequest) | null, [protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAuthorizationPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAuthorizationPolicies(request, options, callback)
    
    
    listAuthorizationPolicies(request: protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest, protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesResponse | null | undefined, protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuthorizationPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesrequest), [protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesresponse) | null | undefined, [protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAuthorizationPolicies(request, callback)
    
    
    listAuthorizationPolicies(request: protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest, callback: PaginationCallback<protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest, protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesResponse | null | undefined, protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuthorizationPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesrequest), [protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesresponse) | null | undefined, [protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAuthorizationPoliciesAsync(request, options)
    
    
    listAuthorizationPoliciesAsync(request?: protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy>;

Equivalent to `listAuthorizationPolicies`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuthorizationPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location from which the AuthorizationPolicies
       *  should be listed, specified in the format
       *  `projects/{project}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Maximum number of AuthorizationPolicies to return per call.
       */
      // const pageSize = 1234
      /**
       *  The value returned by the last
       *  `ListAuthorizationPoliciesResponse` Indicates that this is a
       *  continuation of a prior `ListAuthorizationPolicies` call, and
       *  that the system should return the next page of data.
       */
      // const pageToken = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callListAuthorizationPolicies() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networksecurityClient.listAuthorizationPoliciesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAuthorizationPolicies();
    
    

### listAuthorizationPoliciesStream(request, options)
    
    
    listAuthorizationPoliciesStream(request?: protos.google.cloud.networksecurity.v1beta1.IListAuthorizationPoliciesRequest, options?: CallOptions): Transform;

Equivalent to `listAuthorizationPolicies`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuthorizationPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistauthorizationpoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAuthorizationPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listClientTlsPolicies(request, options)
    
    
    listClientTlsPolicies(request?: protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy[],
            protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest | null,
            protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesResponse
        ]>;

Lists ClientTlsPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClientTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy)[], [protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesrequest) | null, [protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [ClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.clienttlspolicy). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listClientTlsPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listClientTlsPolicies(request, options, callback)
    
    
    listClientTlsPolicies(request: protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest, protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesResponse | null | undefined, protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClientTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesrequest), [protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesresponse) | null | undefined, [protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClientTlsPolicies(request, callback)
    
    
    listClientTlsPolicies(request: protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest, callback: PaginationCallback<protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest, protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesResponse | null | undefined, protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClientTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesrequest), [protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesresponse) | null | undefined, [protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listClientTlsPoliciesAsync(request, options)
    
    
    listClientTlsPoliciesAsync(request?: protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy>;

Equivalent to `listClientTlsPolicies`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClientTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [ClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.clienttlspolicy). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location from which the ClientTlsPolicies should
       *  be listed, specified in the format `projects/* /locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Maximum number of ClientTlsPolicies to return per call.
       */
      // const pageSize = 1234
      /**
       *  The value returned by the last `ListClientTlsPoliciesResponse`
       *  Indicates that this is a continuation of a prior
       *  `ListClientTlsPolicies` call, and that the system
       *  should return the next page of data.
       */
      // const pageToken = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} =
        require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function listClientTlsPolicies() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable =
          await networksecurityClient.listClientTlsPoliciesAsync(request);
        for await (const response of iterable) {
          console.log(response);
        }
      }
    
      listClientTlsPolicies();
    
    

### listClientTlsPoliciesStream(request, options)
    
    
    listClientTlsPoliciesStream(request?: protos.google.cloud.networksecurity.v1beta1.IListClientTlsPoliciesRequest, options?: CallOptions): Transform;

Equivalent to `listClientTlsPolicies`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListClientTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistclienttlspoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [ClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.clienttlspolicy) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listClientTlsPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listServerTlsPolicies(request, options)
    
    
    listServerTlsPolicies(request?: protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy[],
            protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest | null,
            protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesResponse
        ]>;

Lists ServerTlsPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServerTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy)[], [protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesrequest) | null, [protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listServerTlsPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listServerTlsPolicies(request, options, callback)
    
    
    listServerTlsPolicies(request: protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest, protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesResponse | null | undefined, protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServerTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesrequest), [protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesresponse) | null | undefined, [protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServerTlsPolicies(request, callback)
    
    
    listServerTlsPolicies(request: protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest, callback: PaginationCallback<protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest, protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesResponse | null | undefined, protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServerTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesrequest), [protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesresponse) | null | undefined, [protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServerTlsPoliciesAsync(request, options)
    
    
    listServerTlsPoliciesAsync(request?: protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy>;

Equivalent to `listServerTlsPolicies`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServerTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project and location from which the ServerTlsPolicies should
       *  be listed, specified in the format `projects/* /locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Maximum number of ServerTlsPolicies to return per call.
       */
      // const pageSize = 1234
      /**
       *  The value returned by the last `ListServerTlsPoliciesResponse`
       *  Indicates that this is a continuation of a prior
       *  `ListServerTlsPolicies` call, and that the system
       *  should return the next page of data.
       */
      // const pageToken = 'abc123'
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callListServerTlsPolicies() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networksecurityClient.listServerTlsPoliciesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListServerTlsPolicies();
    
    

### listServerTlsPoliciesStream(request, options)
    
    
    listServerTlsPoliciesStream(request?: protos.google.cloud.networksecurity.v1beta1.IListServerTlsPoliciesRequest, options?: CallOptions): Transform;

Equivalent to `listServerTlsPolicies`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServerTlsPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistservertlspoliciesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listServerTlsPoliciesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAuthorizationPolicyFromAuthorizationPolicyName(authorizationPolicyName)
    
    
    matchAuthorizationPolicyFromAuthorizationPolicyName(authorizationPolicyName: string): string | number;

Parse the authorization_policy from AuthorizationPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`authorizationPolicyName` |  `string`   
A fully-qualified path representing AuthorizationPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the authorization_policy.  
  
### matchClientTlsPolicyFromClientTlsPolicyName(clientTlsPolicyName)
    
    
    matchClientTlsPolicyFromClientTlsPolicyName(clientTlsPolicyName: string): string | number;

Parse the client_tls_policy from ClientTlsPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`clientTlsPolicyName` |  `string`   
A fully-qualified path representing ClientTlsPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the client_tls_policy.  
  
### matchDnsThreatDetectorFromDnsThreatDetectorName(dnsThreatDetectorName)
    
    
    matchDnsThreatDetectorFromDnsThreatDetectorName(dnsThreatDetectorName: string): string | number;

Parse the dns_threat_detector from DnsThreatDetector resource.

**Parameter**  
---  
**Name** | **Description**  
`dnsThreatDetectorName` |  `string`   
A fully-qualified path representing DnsThreatDetector resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dns_threat_detector.  
  
### matchLocationFromAuthorizationPolicyName(authorizationPolicyName)
    
    
    matchLocationFromAuthorizationPolicyName(authorizationPolicyName: string): string | number;

Parse the location from AuthorizationPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`authorizationPolicyName` |  `string`   
A fully-qualified path representing AuthorizationPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromClientTlsPolicyName(clientTlsPolicyName)
    
    
    matchLocationFromClientTlsPolicyName(clientTlsPolicyName: string): string | number;

Parse the location from ClientTlsPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`clientTlsPolicyName` |  `string`   
A fully-qualified path representing ClientTlsPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromDnsThreatDetectorName(dnsThreatDetectorName)
    
    
    matchLocationFromDnsThreatDetectorName(dnsThreatDetectorName: string): string | number;

Parse the location from DnsThreatDetector resource.

**Parameter**  
---  
**Name** | **Description**  
`dnsThreatDetectorName` |  `string`   
A fully-qualified path representing DnsThreatDetector resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromServerTlsPolicyName(serverTlsPolicyName)
    
    
    matchLocationFromServerTlsPolicyName(serverTlsPolicyName: string): string | number;

Parse the location from ServerTlsPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`serverTlsPolicyName` |  `string`   
A fully-qualified path representing ServerTlsPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchProjectFromAuthorizationPolicyName(authorizationPolicyName)
    
    
    matchProjectFromAuthorizationPolicyName(authorizationPolicyName: string): string | number;

Parse the project from AuthorizationPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`authorizationPolicyName` |  `string`   
A fully-qualified path representing AuthorizationPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromClientTlsPolicyName(clientTlsPolicyName)
    
    
    matchProjectFromClientTlsPolicyName(clientTlsPolicyName: string): string | number;

Parse the project from ClientTlsPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`clientTlsPolicyName` |  `string`   
A fully-qualified path representing ClientTlsPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromDnsThreatDetectorName(dnsThreatDetectorName)
    
    
    matchProjectFromDnsThreatDetectorName(dnsThreatDetectorName: string): string | number;

Parse the project from DnsThreatDetector resource.

**Parameter**  
---  
**Name** | **Description**  
`dnsThreatDetectorName` |  `string`   
A fully-qualified path representing DnsThreatDetector resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromServerTlsPolicyName(serverTlsPolicyName)
    
    
    matchProjectFromServerTlsPolicyName(serverTlsPolicyName: string): string | number;

Parse the project from ServerTlsPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`serverTlsPolicyName` |  `string`   
A fully-qualified path representing ServerTlsPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchServerTlsPolicyFromServerTlsPolicyName(serverTlsPolicyName)
    
    
    matchServerTlsPolicyFromServerTlsPolicyName(serverTlsPolicyName: string): string | number;

Parse the server_tls_policy from ServerTlsPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`serverTlsPolicyName` |  `string`   
A fully-qualified path representing ServerTlsPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the server_tls_policy.  
  
### serverTlsPolicyPath(project, location, serverTlsPolicy)
    
    
    serverTlsPolicyPath(project: string, location: string, serverTlsPolicy: string): string;

Return a fully-qualified serverTlsPolicy resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`serverTlsPolicy` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
  
### updateAuthorizationPolicy(request, options)
    
    
    updateAuthorizationPolicy(request?: protos.google.cloud.networksecurity.v1beta1.IUpdateAuthorizationPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single AuthorizationPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdateauthorizationpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  AuthorizationPolicy resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask. If the
       *  user does not provide a mask then all fields will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. Updated AuthorizationPolicy resource.
       */
      // const authorizationPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callUpdateAuthorizationPolicy() {
        // Construct request
        const request = {
          authorizationPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.updateAuthorizationPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateAuthorizationPolicy();
    
    

### updateAuthorizationPolicy(request, options, callback)
    
    
    updateAuthorizationPolicy(request: protos.google.cloud.networksecurity.v1beta1.IUpdateAuthorizationPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdateauthorizationpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAuthorizationPolicy(request, callback)
    
    
    updateAuthorizationPolicy(request: protos.google.cloud.networksecurity.v1beta1.IUpdateAuthorizationPolicyRequest, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdateauthorizationpolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IAuthorizationPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iauthorizationpolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateClientTlsPolicy(request, options)
    
    
    updateClientTlsPolicy(request?: protos.google.cloud.networksecurity.v1beta1.IUpdateClientTlsPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single ClientTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdateclienttlspolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  ClientTlsPolicy resource by the update.  The fields
       *  specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the
       *  mask. If the user does not provide a mask then all fields will be
       *  overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. Updated ClientTlsPolicy resource.
       */
      // const clientTlsPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callUpdateClientTlsPolicy() {
        // Construct request
        const request = {
          clientTlsPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.updateClientTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateClientTlsPolicy();
    
    

### updateClientTlsPolicy(request, options, callback)
    
    
    updateClientTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IUpdateClientTlsPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdateclienttlspolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateClientTlsPolicy(request, callback)
    
    
    updateClientTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IUpdateClientTlsPolicyRequest, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateClientTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdateclienttlspolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IClientTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iclienttlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateServerTlsPolicy(request, options)
    
    
    updateServerTlsPolicy(request?: protos.google.cloud.networksecurity.v1beta1.IUpdateServerTlsPolicyRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates the parameters of a single ServerTlsPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdateservertlspolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Field mask is used to specify the fields to be overwritten in the
       *  ServerTlsPolicy resource by the update.  The fields
       *  specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the
       *  mask. If the user does not provide a mask then all fields will be
       *  overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. Updated ServerTlsPolicy resource.
       */
      // const serverTlsPolicy = {}
    
      // Imports the Networksecurity library
      const {NetworkSecurityClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [NetworkSecurityClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callUpdateServerTlsPolicy() {
        // Construct request
        const request = {
          serverTlsPolicy,
        };
    
        // Run request
        const [operation] = await networksecurityClient.updateServerTlsPolicy(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateServerTlsPolicy();
    
    

### updateServerTlsPolicy(request, options, callback)
    
    
    updateServerTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IUpdateServerTlsPolicyRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdateservertlspolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateServerTlsPolicy(request, callback)
    
    
    updateServerTlsPolicy(request: protos.google.cloud.networksecurity.v1beta1.IUpdateServerTlsPolicyRequest, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy, protos.google.cloud.networksecurity.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServerTlsPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdateservertlspolicyrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1beta1.IServerTlsPolicy](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iservertlspolicy), [protos.google.cloud.networksecurity.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
