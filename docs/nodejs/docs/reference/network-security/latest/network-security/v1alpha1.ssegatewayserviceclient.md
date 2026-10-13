---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient
title: Class v1alpha1.SSEGatewayServiceClient (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:43.963183+00:00
---

# Class v1alpha1.SSEGatewayServiceClient (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha1.SSEGatewayServiceClient (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.6.0  3.1.0  1.1.2  1.0.2  0.5.0  0.3.0  0.2.0 

Service describing handlers for resources v1alpha1

## Package

[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of SSEGatewayServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new SSEGatewayServiceClient({fallback: true}, gax); ```  
  
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

### sSEGatewayServiceStub
    
    
    sSEGatewayServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### authzPolicyPath(project, location, authzPolicy)
    
    
    authzPolicyPath(project: string, location: string, authzPolicy: string): string;

Return a fully-qualified authzPolicy resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`authzPolicy` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### backendAuthenticationConfigPath(project, location, backendAuthenticationConfig)
    
    
    backendAuthenticationConfigPath(project: string, location: string, backendAuthenticationConfig: string): string;

Return a fully-qualified backendAuthenticationConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`backendAuthenticationConfig` |  `string`   
  
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
    

### checkCreatePartnerSSEGatewayProgress(name)
    
    
    checkCreatePartnerSSEGatewayProgress(name: string): Promise<LROperation<protos.google.cloud.networksecurity.v1alpha1.PartnerSSEGateway, protos.google.cloud.networksecurity.v1alpha1.OperationMetadata>>;

Check the status of the long running operation returned by `createPartnerSSEGateway()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networksecurity.v1alpha1.PartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.partnerssegateway-class), [protos.google.cloud.networksecurity.v1alpha1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
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
       *  Required. Id of the requesting object
       *  If auto-generating Id server-side, remove this field and
       *  partner_sse_gateway_id from the method_signature of Create RPC
       */
      // const partnerSseGatewayId = 'abc123'
      /**
       *  Required. The resource being created
       */
      // const partnerSseGateway = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networksecurity library
      const {SSEGatewayServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networksecurityClient = new [SSEGatewayServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)();
    
      async function callCreatePartnerSSEGateway() {
        // Construct request
        const request = {
          parent,
          partnerSseGatewayId,
          partnerSseGateway,
        };
    
        // Run request
        const [operation] = await networksecurityClient.createPartnerSSEGateway(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreatePartnerSSEGateway();
    
    

### checkDeletePartnerSSEGatewayProgress(name)
    
    
    checkDeletePartnerSSEGatewayProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.networksecurity.v1alpha1.OperationMetadata>>;

Check the status of the long running operation returned by `deletePartnerSSEGateway()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty), [protos.google.cloud.networksecurity.v1alpha1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
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
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networksecurity library
      const {SSEGatewayServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networksecurityClient = new [SSEGatewayServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)();
    
      async function callDeletePartnerSSEGateway() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networksecurityClient.deletePartnerSSEGateway(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeletePartnerSSEGateway();
    
    

### checkUpdatePartnerSSEGatewayProgress(name)
    
    
    checkUpdatePartnerSSEGatewayProgress(name: string): Promise<LROperation<protos.google.cloud.networksecurity.v1alpha1.PartnerSSEGateway, protos.google.cloud.networksecurity.v1alpha1.OperationMetadata>>;

Check the status of the long running operation returned by `updatePartnerSSEGateway()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networksecurity.v1alpha1.PartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.partnerssegateway-class), [protos.google.cloud.networksecurity.v1alpha1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource being created
       */
      // const partnerSseGateway = {}
      /**
       *  The list of fields to update
       */
      // const updateMask = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networksecurity library
      const {SSEGatewayServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networksecurityClient = new [SSEGatewayServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)();
    
      async function callUpdatePartnerSSEGateway() {
        // Construct request
        const request = {
          partnerSseGateway,
        };
    
        // Run request
        const [operation] = await networksecurityClient.updatePartnerSSEGateway(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdatePartnerSSEGateway();
    
    

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
  
### createPartnerSSEGateway(request, options)
    
    
    createPartnerSSEGateway(request?: protos.google.cloud.networksecurity.v1alpha1.ICreatePartnerSSEGatewayRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway, protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new PartnerSSEGateway in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.icreatepartnerssegatewayrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway), [protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
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
       *  Required. Id of the requesting object
       *  If auto-generating Id server-side, remove this field and
       *  partner_sse_gateway_id from the method_signature of Create RPC
       */
      // const partnerSseGatewayId = 'abc123'
      /**
       *  Required. The resource being created
       */
      // const partnerSseGateway = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networksecurity library
      const {SSEGatewayServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networksecurityClient = new [SSEGatewayServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)();
    
      async function callCreatePartnerSSEGateway() {
        // Construct request
        const request = {
          parent,
          partnerSseGatewayId,
          partnerSseGateway,
        };
    
        // Run request
        const [operation] = await networksecurityClient.createPartnerSSEGateway(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreatePartnerSSEGateway();
    
    

### createPartnerSSEGateway(request, options, callback)
    
    
    createPartnerSSEGateway(request: protos.google.cloud.networksecurity.v1alpha1.ICreatePartnerSSEGatewayRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway, protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.icreatepartnerssegatewayrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway), [protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPartnerSSEGateway(request, callback)
    
    
    createPartnerSSEGateway(request: protos.google.cloud.networksecurity.v1alpha1.ICreatePartnerSSEGatewayRequest, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway, protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.icreatepartnerssegatewayrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway), [protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
    

### deletePartnerSSEGateway(request, options)
    
    
    deletePartnerSSEGateway(request?: protos.google.cloud.networksecurity.v1alpha1.IDeletePartnerSSEGatewayRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single PartnerSSEGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ideletepartnerssegatewayrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
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
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networksecurity library
      const {SSEGatewayServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networksecurityClient = new [SSEGatewayServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)();
    
      async function callDeletePartnerSSEGateway() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networksecurityClient.deletePartnerSSEGateway(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeletePartnerSSEGateway();
    
    

### deletePartnerSSEGateway(request, options, callback)
    
    
    deletePartnerSSEGateway(request: protos.google.cloud.networksecurity.v1alpha1.IDeletePartnerSSEGatewayRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ideletepartnerssegatewayrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePartnerSSEGateway(request, callback)
    
    
    deletePartnerSSEGateway(request: protos.google.cloud.networksecurity.v1alpha1.IDeletePartnerSSEGatewayRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ideletepartnerssegatewayrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
  
### firewallEndpointAssociationPath(project, location, firewallEndpointAssociation)
    
    
    firewallEndpointAssociationPath(project: string, location: string, firewallEndpointAssociation: string): string;

Return a fully-qualified firewallEndpointAssociation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`firewallEndpointAssociation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### gatewaySecurityPolicyPath(project, location, gatewaySecurityPolicy)
    
    
    gatewaySecurityPolicyPath(project: string, location: string, gatewaySecurityPolicy: string): string;

Return a fully-qualified gatewaySecurityPolicy resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`gatewaySecurityPolicy` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### gatewaySecurityPolicyRulePath(project, location, gatewaySecurityPolicy, rule)
    
    
    gatewaySecurityPolicyRulePath(project: string, location: string, gatewaySecurityPolicy: string, rule: string): string;

Return a fully-qualified gatewaySecurityPolicyRule resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`gatewaySecurityPolicy` |  `string`   
  
`rule` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
    

### getPartnerSSEGateway(request, options)
    
    
    getPartnerSSEGateway(request?: protos.google.cloud.networksecurity.v1alpha1.IGetPartnerSSEGatewayRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway,
            (protos.google.cloud.networksecurity.v1alpha1.IGetPartnerSSEGatewayRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single PartnerSSEGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetpartnerssegatewayrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway), ([protos.google.cloud.networksecurity.v1alpha1.IGetPartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetpartnerssegatewayrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Networksecurity library
      const {SSEGatewayServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networksecurityClient = new [SSEGatewayServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)();
    
      async function callGetPartnerSSEGateway() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networksecurityClient.getPartnerSSEGateway(request);
        console.log(response);
      }
    
      callGetPartnerSSEGateway();
    
    

### getPartnerSSEGateway(request, options, callback)
    
    
    getPartnerSSEGateway(request: protos.google.cloud.networksecurity.v1alpha1.IGetPartnerSSEGatewayRequest, options: CallOptions, callback: Callback<protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway, protos.google.cloud.networksecurity.v1alpha1.IGetPartnerSSEGatewayRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetpartnerssegatewayrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway), [protos.google.cloud.networksecurity.v1alpha1.IGetPartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetpartnerssegatewayrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPartnerSSEGateway(request, callback)
    
    
    getPartnerSSEGateway(request: protos.google.cloud.networksecurity.v1alpha1.IGetPartnerSSEGatewayRequest, callback: Callback<protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway, protos.google.cloud.networksecurity.v1alpha1.IGetPartnerSSEGatewayRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetpartnerssegatewayrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway), [protos.google.cloud.networksecurity.v1alpha1.IGetPartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetpartnerssegatewayrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getSSEGatewayReference(request, options)
    
    
    getSSEGatewayReference(request?: protos.google.cloud.networksecurity.v1alpha1.IGetSSEGatewayReferenceRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference,
            (protos.google.cloud.networksecurity.v1alpha1.IGetSSEGatewayReferenceRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single SSEGatewayReference.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSSEGatewayReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetssegatewayreferencerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.issegatewayreference), ([protos.google.cloud.networksecurity.v1alpha1.IGetSSEGatewayReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetssegatewayreferencerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [SSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ssegatewayreference). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Networksecurity library
      const {SSEGatewayServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networksecurityClient = new [SSEGatewayServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)();
    
      async function callGetSSEGatewayReference() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networksecurityClient.getSSEGatewayReference(request);
        console.log(response);
      }
    
      callGetSSEGatewayReference();
    
    

### getSSEGatewayReference(request, options, callback)
    
    
    getSSEGatewayReference(request: protos.google.cloud.networksecurity.v1alpha1.IGetSSEGatewayReferenceRequest, options: CallOptions, callback: Callback<protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference, protos.google.cloud.networksecurity.v1alpha1.IGetSSEGatewayReferenceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSSEGatewayReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetssegatewayreferencerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.issegatewayreference), [protos.google.cloud.networksecurity.v1alpha1.IGetSSEGatewayReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetssegatewayreferencerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSSEGatewayReference(request, callback)
    
    
    getSSEGatewayReference(request: protos.google.cloud.networksecurity.v1alpha1.IGetSSEGatewayReferenceRequest, callback: Callback<protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference, protos.google.cloud.networksecurity.v1alpha1.IGetSSEGatewayReferenceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSSEGatewayReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetssegatewayreferencerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.issegatewayreference), [protos.google.cloud.networksecurity.v1alpha1.IGetSSEGatewayReferenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.igetssegatewayreferencerequest) | null | undefined, {} | null | undefined>`   
  
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
  
### interceptDeploymentGroupPath(project, location, interceptDeploymentGroup)
    
    
    interceptDeploymentGroupPath(project: string, location: string, interceptDeploymentGroup: string): string;

Return a fully-qualified interceptDeploymentGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`interceptDeploymentGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### interceptDeploymentPath(project, location, interceptDeployment)
    
    
    interceptDeploymentPath(project: string, location: string, interceptDeployment: string): string;

Return a fully-qualified interceptDeployment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`interceptDeployment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### interceptEndpointGroupAssociationPath(project, location, interceptEndpointGroupAssociation)
    
    
    interceptEndpointGroupAssociationPath(project: string, location: string, interceptEndpointGroupAssociation: string): string;

Return a fully-qualified interceptEndpointGroupAssociation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`interceptEndpointGroupAssociation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### interceptEndpointGroupPath(project, location, interceptEndpointGroup)
    
    
    interceptEndpointGroupPath(project: string, location: string, interceptEndpointGroup: string): string;

Return a fully-qualified interceptEndpointGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`interceptEndpointGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
    

### listPartnerSSEGateways(request, options)
    
    
    listPartnerSSEGateways(request?: protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway[],
            protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest | null,
            protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysResponse
        ]>;

Lists PartnerSSEGateways in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPartnerSSEGatewaysRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway)[], [protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysrequest) | null, [protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listPartnerSSEGatewaysAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPartnerSSEGateways(request, options, callback)
    
    
    listPartnerSSEGateways(request: protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest, protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysResponse | null | undefined, protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPartnerSSEGatewaysRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysrequest), [protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysresponse) | null | undefined, [protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPartnerSSEGateways(request, callback)
    
    
    listPartnerSSEGateways(request: protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest, callback: PaginationCallback<protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest, protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysResponse | null | undefined, protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPartnerSSEGatewaysRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysrequest), [protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysresponse) | null | undefined, [protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPartnerSSEGatewaysAsync(request, options)
    
    
    listPartnerSSEGatewaysAsync(request?: protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway>;

Equivalent to `listPartnerSSEGateways`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPartnerSSEGatewaysRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListPartnerSSEGatewaysRequest
       */
      // const parent = 'abc123'
      /**
       *  Requested page size. Server may return fewer items than requested.
       *  If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Filtering results
       */
      // const filter = 'abc123'
      /**
       *  Hint for how to order the results
       */
      // const orderBy = 'abc123'
    
      // Imports the Networksecurity library
      const {SSEGatewayServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networksecurityClient = new [SSEGatewayServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)();
    
      async function callListPartnerSSEGateways() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networksecurityClient.[listPartnerSSEGatewaysAsync](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListPartnerSSEGateways();
    
    

### listPartnerSSEGatewaysStream(request, options)
    
    
    listPartnerSSEGatewaysStream(request?: protos.google.cloud.networksecurity.v1alpha1.IListPartnerSSEGatewaysRequest, options?: CallOptions): Transform;

Equivalent to `listPartnerSSEGateways`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPartnerSSEGatewaysRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistpartnerssegatewaysrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listPartnerSSEGatewaysAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSSEGatewayReferences(request, options)
    
    
    listSSEGatewayReferences(request?: protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference[],
            protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest | null,
            protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesResponse
        ]>;

Lists SSEGatewayReferences in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSSEGatewayReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.issegatewayreference)[], [protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesrequest) | null, [protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [SSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ssegatewayreference). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listSSEGatewayReferencesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSSEGatewayReferences(request, options, callback)
    
    
    listSSEGatewayReferences(request: protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest, protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesResponse | null | undefined, protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSSEGatewayReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesrequest), [protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesresponse) | null | undefined, [protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.issegatewayreference)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSSEGatewayReferences(request, callback)
    
    
    listSSEGatewayReferences(request: protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest, callback: PaginationCallback<protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest, protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesResponse | null | undefined, protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSSEGatewayReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesrequest), [protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesresponse) | null | undefined, [protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.issegatewayreference)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSSEGatewayReferencesAsync(request, options)
    
    
    listSSEGatewayReferencesAsync(request?: protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference>;

Equivalent to `listSSEGatewayReferences`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSSEGatewayReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networksecurity.v1alpha1.ISSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.issegatewayreference)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [SSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ssegatewayreference). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListSSEGatewayReferencesRequest
       */
      // const parent = 'abc123'
      /**
       *  Requested page size. Server may return fewer items than requested.
       *  If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Filtering results
       */
      // const filter = 'abc123'
      /**
       *  Hint for how to order the results
       */
      // const orderBy = 'abc123'
    
      // Imports the Networksecurity library
      const {SSEGatewayServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networksecurityClient = new [SSEGatewayServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)();
    
      async function callListSSEGatewayReferences() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networksecurityClient.[listSSEGatewayReferencesAsync](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListSSEGatewayReferences();
    
    

### listSSEGatewayReferencesStream(request, options)
    
    
    listSSEGatewayReferencesStream(request?: protos.google.cloud.networksecurity.v1alpha1.IListSSEGatewayReferencesRequest, options?: CallOptions): Transform;

Equivalent to `listSSEGatewayReferences`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSSEGatewayReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ilistssegatewayreferencesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [SSEGatewayReference](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ssegatewayreference) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listSSEGatewayReferencesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchAuthzPolicyFromAuthzPolicyName(authzPolicyName)
    
    
    matchAuthzPolicyFromAuthzPolicyName(authzPolicyName: string): string | number;

Parse the authz_policy from AuthzPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`authzPolicyName` |  `string`   
A fully-qualified path representing AuthzPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the authz_policy.  
  
### matchBackendAuthenticationConfigFromBackendAuthenticationConfigName(backendAuthenticationConfigName)
    
    
    matchBackendAuthenticationConfigFromBackendAuthenticationConfigName(backendAuthenticationConfigName: string): string | number;

Parse the backend_authentication_config from BackendAuthenticationConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`backendAuthenticationConfigName` |  `string`   
A fully-qualified path representing BackendAuthenticationConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the backend_authentication_config.  
  
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
  
### matchFirewallEndpointAssociationFromFirewallEndpointAssociationName(firewallEndpointAssociationName)
    
    
    matchFirewallEndpointAssociationFromFirewallEndpointAssociationName(firewallEndpointAssociationName: string): string | number;

Parse the firewall_endpoint_association from FirewallEndpointAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`firewallEndpointAssociationName` |  `string`   
A fully-qualified path representing FirewallEndpointAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the firewall_endpoint_association.  
  
### matchFirewallEndpointFromOrganizationLocationFirewallEndpointsName(organizationLocationFirewallEndpointsName)
    
    
    matchFirewallEndpointFromOrganizationLocationFirewallEndpointsName(organizationLocationFirewallEndpointsName: string): string | number;

Parse the firewall_endpoint from OrganizationLocationFirewallEndpoints resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationFirewallEndpointsName` |  `string`   
A fully-qualified path representing organization_location_firewallEndpoints resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the firewall_endpoint.  
  
### matchFirewallEndpointFromProjectLocationFirewallEndpointsName(projectLocationFirewallEndpointsName)
    
    
    matchFirewallEndpointFromProjectLocationFirewallEndpointsName(projectLocationFirewallEndpointsName: string): string | number;

Parse the firewall_endpoint from ProjectLocationFirewallEndpoints resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFirewallEndpointsName` |  `string`   
A fully-qualified path representing project_location_firewallEndpoints resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the firewall_endpoint.  
  
### matchGatewaySecurityPolicyFromGatewaySecurityPolicyName(gatewaySecurityPolicyName)
    
    
    matchGatewaySecurityPolicyFromGatewaySecurityPolicyName(gatewaySecurityPolicyName: string): string | number;

Parse the gateway_security_policy from GatewaySecurityPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewaySecurityPolicyName` |  `string`   
A fully-qualified path representing GatewaySecurityPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the gateway_security_policy.  
  
### matchGatewaySecurityPolicyFromGatewaySecurityPolicyRuleName(gatewaySecurityPolicyRuleName)
    
    
    matchGatewaySecurityPolicyFromGatewaySecurityPolicyRuleName(gatewaySecurityPolicyRuleName: string): string | number;

Parse the gateway_security_policy from GatewaySecurityPolicyRule resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewaySecurityPolicyRuleName` |  `string`   
A fully-qualified path representing GatewaySecurityPolicyRule resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the gateway_security_policy.  
  
### matchInterceptDeploymentFromInterceptDeploymentName(interceptDeploymentName)
    
    
    matchInterceptDeploymentFromInterceptDeploymentName(interceptDeploymentName: string): string | number;

Parse the intercept_deployment from InterceptDeployment resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptDeploymentName` |  `string`   
A fully-qualified path representing InterceptDeployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the intercept_deployment.  
  
### matchInterceptDeploymentGroupFromInterceptDeploymentGroupName(interceptDeploymentGroupName)
    
    
    matchInterceptDeploymentGroupFromInterceptDeploymentGroupName(interceptDeploymentGroupName: string): string | number;

Parse the intercept_deployment_group from InterceptDeploymentGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptDeploymentGroupName` |  `string`   
A fully-qualified path representing InterceptDeploymentGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the intercept_deployment_group.  
  
### matchInterceptEndpointGroupAssociationFromInterceptEndpointGroupAssociationName(interceptEndpointGroupAssociationName)
    
    
    matchInterceptEndpointGroupAssociationFromInterceptEndpointGroupAssociationName(interceptEndpointGroupAssociationName: string): string | number;

Parse the intercept_endpoint_group_association from InterceptEndpointGroupAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptEndpointGroupAssociationName` |  `string`   
A fully-qualified path representing InterceptEndpointGroupAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the intercept_endpoint_group_association.  
  
### matchInterceptEndpointGroupFromInterceptEndpointGroupName(interceptEndpointGroupName)
    
    
    matchInterceptEndpointGroupFromInterceptEndpointGroupName(interceptEndpointGroupName: string): string | number;

Parse the intercept_endpoint_group from InterceptEndpointGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptEndpointGroupName` |  `string`   
A fully-qualified path representing InterceptEndpointGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the intercept_endpoint_group.  
  
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
  
### matchLocationFromAuthzPolicyName(authzPolicyName)
    
    
    matchLocationFromAuthzPolicyName(authzPolicyName: string): string | number;

Parse the location from AuthzPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`authzPolicyName` |  `string`   
A fully-qualified path representing AuthzPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBackendAuthenticationConfigName(backendAuthenticationConfigName)
    
    
    matchLocationFromBackendAuthenticationConfigName(backendAuthenticationConfigName: string): string | number;

Parse the location from BackendAuthenticationConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`backendAuthenticationConfigName` |  `string`   
A fully-qualified path representing BackendAuthenticationConfig resource.  
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
  
### matchLocationFromFirewallEndpointAssociationName(firewallEndpointAssociationName)
    
    
    matchLocationFromFirewallEndpointAssociationName(firewallEndpointAssociationName: string): string | number;

Parse the location from FirewallEndpointAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`firewallEndpointAssociationName` |  `string`   
A fully-qualified path representing FirewallEndpointAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromGatewaySecurityPolicyName(gatewaySecurityPolicyName)
    
    
    matchLocationFromGatewaySecurityPolicyName(gatewaySecurityPolicyName: string): string | number;

Parse the location from GatewaySecurityPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewaySecurityPolicyName` |  `string`   
A fully-qualified path representing GatewaySecurityPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromGatewaySecurityPolicyRuleName(gatewaySecurityPolicyRuleName)
    
    
    matchLocationFromGatewaySecurityPolicyRuleName(gatewaySecurityPolicyRuleName: string): string | number;

Parse the location from GatewaySecurityPolicyRule resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewaySecurityPolicyRuleName` |  `string`   
A fully-qualified path representing GatewaySecurityPolicyRule resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromInterceptDeploymentGroupName(interceptDeploymentGroupName)
    
    
    matchLocationFromInterceptDeploymentGroupName(interceptDeploymentGroupName: string): string | number;

Parse the location from InterceptDeploymentGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptDeploymentGroupName` |  `string`   
A fully-qualified path representing InterceptDeploymentGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromInterceptDeploymentName(interceptDeploymentName)
    
    
    matchLocationFromInterceptDeploymentName(interceptDeploymentName: string): string | number;

Parse the location from InterceptDeployment resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptDeploymentName` |  `string`   
A fully-qualified path representing InterceptDeployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromInterceptEndpointGroupAssociationName(interceptEndpointGroupAssociationName)
    
    
    matchLocationFromInterceptEndpointGroupAssociationName(interceptEndpointGroupAssociationName: string): string | number;

Parse the location from InterceptEndpointGroupAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptEndpointGroupAssociationName` |  `string`   
A fully-qualified path representing InterceptEndpointGroupAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromInterceptEndpointGroupName(interceptEndpointGroupName)
    
    
    matchLocationFromInterceptEndpointGroupName(interceptEndpointGroupName: string): string | number;

Parse the location from InterceptEndpointGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptEndpointGroupName` |  `string`   
A fully-qualified path representing InterceptEndpointGroup resource.  
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
  
### matchLocationFromMirroringDeploymentGroupName(mirroringDeploymentGroupName)
    
    
    matchLocationFromMirroringDeploymentGroupName(mirroringDeploymentGroupName: string): string | number;

Parse the location from MirroringDeploymentGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringDeploymentGroupName` |  `string`   
A fully-qualified path representing MirroringDeploymentGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMirroringDeploymentName(mirroringDeploymentName)
    
    
    matchLocationFromMirroringDeploymentName(mirroringDeploymentName: string): string | number;

Parse the location from MirroringDeployment resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringDeploymentName` |  `string`   
A fully-qualified path representing MirroringDeployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMirroringEndpointGroupAssociationName(mirroringEndpointGroupAssociationName)
    
    
    matchLocationFromMirroringEndpointGroupAssociationName(mirroringEndpointGroupAssociationName: string): string | number;

Parse the location from MirroringEndpointGroupAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringEndpointGroupAssociationName` |  `string`   
A fully-qualified path representing MirroringEndpointGroupAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMirroringEndpointGroupName(mirroringEndpointGroupName)
    
    
    matchLocationFromMirroringEndpointGroupName(mirroringEndpointGroupName: string): string | number;

Parse the location from MirroringEndpointGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringEndpointGroupName` |  `string`   
A fully-qualified path representing MirroringEndpointGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromOrganizationLocationFirewallEndpointsName(organizationLocationFirewallEndpointsName)
    
    
    matchLocationFromOrganizationLocationFirewallEndpointsName(organizationLocationFirewallEndpointsName: string): string | number;

Parse the location from OrganizationLocationFirewallEndpoints resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationFirewallEndpointsName` |  `string`   
A fully-qualified path representing organization_location_firewallEndpoints resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromOrganizationLocationSecurityProfileGroupName(organizationLocationSecurityProfileGroupName)
    
    
    matchLocationFromOrganizationLocationSecurityProfileGroupName(organizationLocationSecurityProfileGroupName: string): string | number;

Parse the location from OrganizationLocationSecurityProfileGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationSecurityProfileGroupName` |  `string`   
A fully-qualified path representing organization_location_security_profile_group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromOrganizationLocationSecurityProfileName(organizationLocationSecurityProfileName)
    
    
    matchLocationFromOrganizationLocationSecurityProfileName(organizationLocationSecurityProfileName: string): string | number;

Parse the location from OrganizationLocationSecurityProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationSecurityProfileName` |  `string`   
A fully-qualified path representing organization_location_security_profile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPartnerSSEGatewayName(partnerSSEGatewayName)
    
    
    matchLocationFromPartnerSSEGatewayName(partnerSSEGatewayName: string): string | number;

Parse the location from PartnerSSEGateway resource.

**Parameter**  
---  
**Name** | **Description**  
`partnerSSEGatewayName` |  `string`   
A fully-qualified path representing PartnerSSEGateway resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPartnerSSERealmName(partnerSSERealmName)
    
    
    matchLocationFromPartnerSSERealmName(partnerSSERealmName: string): string | number;

Parse the location from PartnerSSERealm resource.

**Parameter**  
---  
**Name** | **Description**  
`partnerSSERealmName` |  `string`   
A fully-qualified path representing PartnerSSERealm resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationFirewallEndpointsName(projectLocationFirewallEndpointsName)
    
    
    matchLocationFromProjectLocationFirewallEndpointsName(projectLocationFirewallEndpointsName: string): string | number;

Parse the location from ProjectLocationFirewallEndpoints resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFirewallEndpointsName` |  `string`   
A fully-qualified path representing project_location_firewallEndpoints resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationSecurityProfileGroupName(projectLocationSecurityProfileGroupName)
    
    
    matchLocationFromProjectLocationSecurityProfileGroupName(projectLocationSecurityProfileGroupName: string): string | number;

Parse the location from ProjectLocationSecurityProfileGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationSecurityProfileGroupName` |  `string`   
A fully-qualified path representing project_location_security_profile_group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationSecurityProfileName(projectLocationSecurityProfileName)
    
    
    matchLocationFromProjectLocationSecurityProfileName(projectLocationSecurityProfileName: string): string | number;

Parse the location from ProjectLocationSecurityProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationSecurityProfileName` |  `string`   
A fully-qualified path representing project_location_security_profile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSACAttachmentName(sACAttachmentName)
    
    
    matchLocationFromSACAttachmentName(sACAttachmentName: string): string | number;

Parse the location from SACAttachment resource.

**Parameter**  
---  
**Name** | **Description**  
`sACAttachmentName` |  `string`   
A fully-qualified path representing SACAttachment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSACRealmName(sACRealmName)
    
    
    matchLocationFromSACRealmName(sACRealmName: string): string | number;

Parse the location from SACRealm resource.

**Parameter**  
---  
**Name** | **Description**  
`sACRealmName` |  `string`   
A fully-qualified path representing SACRealm resource.  
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
  
### matchLocationFromSSEGatewayReferenceName(sSEGatewayReferenceName)
    
    
    matchLocationFromSSEGatewayReferenceName(sSEGatewayReferenceName: string): string | number;

Parse the location from SSEGatewayReference resource.

**Parameter**  
---  
**Name** | **Description**  
`sSEGatewayReferenceName` |  `string`   
A fully-qualified path representing SSEGatewayReference resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTlsInspectionPolicyName(tlsInspectionPolicyName)
    
    
    matchLocationFromTlsInspectionPolicyName(tlsInspectionPolicyName: string): string | number;

Parse the location from TlsInspectionPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`tlsInspectionPolicyName` |  `string`   
A fully-qualified path representing TlsInspectionPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromUrlListName(urlListName)
    
    
    matchLocationFromUrlListName(urlListName: string): string | number;

Parse the location from UrlList resource.

**Parameter**  
---  
**Name** | **Description**  
`urlListName` |  `string`   
A fully-qualified path representing UrlList resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMirroringDeploymentFromMirroringDeploymentName(mirroringDeploymentName)
    
    
    matchMirroringDeploymentFromMirroringDeploymentName(mirroringDeploymentName: string): string | number;

Parse the mirroring_deployment from MirroringDeployment resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringDeploymentName` |  `string`   
A fully-qualified path representing MirroringDeployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the mirroring_deployment.  
  
### matchMirroringDeploymentGroupFromMirroringDeploymentGroupName(mirroringDeploymentGroupName)
    
    
    matchMirroringDeploymentGroupFromMirroringDeploymentGroupName(mirroringDeploymentGroupName: string): string | number;

Parse the mirroring_deployment_group from MirroringDeploymentGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringDeploymentGroupName` |  `string`   
A fully-qualified path representing MirroringDeploymentGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the mirroring_deployment_group.  
  
### matchMirroringEndpointGroupAssociationFromMirroringEndpointGroupAssociationName(mirroringEndpointGroupAssociationName)
    
    
    matchMirroringEndpointGroupAssociationFromMirroringEndpointGroupAssociationName(mirroringEndpointGroupAssociationName: string): string | number;

Parse the mirroring_endpoint_group_association from MirroringEndpointGroupAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringEndpointGroupAssociationName` |  `string`   
A fully-qualified path representing MirroringEndpointGroupAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the mirroring_endpoint_group_association.  
  
### matchMirroringEndpointGroupFromMirroringEndpointGroupName(mirroringEndpointGroupName)
    
    
    matchMirroringEndpointGroupFromMirroringEndpointGroupName(mirroringEndpointGroupName: string): string | number;

Parse the mirroring_endpoint_group from MirroringEndpointGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringEndpointGroupName` |  `string`   
A fully-qualified path representing MirroringEndpointGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the mirroring_endpoint_group.  
  
### matchOrganizationFromOrganizationLocationFirewallEndpointsName(organizationLocationFirewallEndpointsName)
    
    
    matchOrganizationFromOrganizationLocationFirewallEndpointsName(organizationLocationFirewallEndpointsName: string): string | number;

Parse the organization from OrganizationLocationFirewallEndpoints resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationFirewallEndpointsName` |  `string`   
A fully-qualified path representing organization_location_firewallEndpoints resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromOrganizationLocationSecurityProfileGroupName(organizationLocationSecurityProfileGroupName)
    
    
    matchOrganizationFromOrganizationLocationSecurityProfileGroupName(organizationLocationSecurityProfileGroupName: string): string | number;

Parse the organization from OrganizationLocationSecurityProfileGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationSecurityProfileGroupName` |  `string`   
A fully-qualified path representing organization_location_security_profile_group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromOrganizationLocationSecurityProfileName(organizationLocationSecurityProfileName)
    
    
    matchOrganizationFromOrganizationLocationSecurityProfileName(organizationLocationSecurityProfileName: string): string | number;

Parse the organization from OrganizationLocationSecurityProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationSecurityProfileName` |  `string`   
A fully-qualified path representing organization_location_security_profile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchPartnerSseGatewayFromPartnerSSEGatewayName(partnerSSEGatewayName)
    
    
    matchPartnerSseGatewayFromPartnerSSEGatewayName(partnerSSEGatewayName: string): string | number;

Parse the partner_sse_gateway from PartnerSSEGateway resource.

**Parameter**  
---  
**Name** | **Description**  
`partnerSSEGatewayName` |  `string`   
A fully-qualified path representing PartnerSSEGateway resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the partner_sse_gateway.  
  
### matchPartnerSseRealmFromPartnerSSERealmName(partnerSSERealmName)
    
    
    matchPartnerSseRealmFromPartnerSSERealmName(partnerSSERealmName: string): string | number;

Parse the partner_sse_realm from PartnerSSERealm resource.

**Parameter**  
---  
**Name** | **Description**  
`partnerSSERealmName` |  `string`   
A fully-qualified path representing PartnerSSERealm resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the partner_sse_realm.  
  
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
  
### matchProjectFromAuthzPolicyName(authzPolicyName)
    
    
    matchProjectFromAuthzPolicyName(authzPolicyName: string): string | number;

Parse the project from AuthzPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`authzPolicyName` |  `string`   
A fully-qualified path representing AuthzPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBackendAuthenticationConfigName(backendAuthenticationConfigName)
    
    
    matchProjectFromBackendAuthenticationConfigName(backendAuthenticationConfigName: string): string | number;

Parse the project from BackendAuthenticationConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`backendAuthenticationConfigName` |  `string`   
A fully-qualified path representing BackendAuthenticationConfig resource.  
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
  
### matchProjectFromFirewallEndpointAssociationName(firewallEndpointAssociationName)
    
    
    matchProjectFromFirewallEndpointAssociationName(firewallEndpointAssociationName: string): string | number;

Parse the project from FirewallEndpointAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`firewallEndpointAssociationName` |  `string`   
A fully-qualified path representing FirewallEndpointAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromGatewaySecurityPolicyName(gatewaySecurityPolicyName)
    
    
    matchProjectFromGatewaySecurityPolicyName(gatewaySecurityPolicyName: string): string | number;

Parse the project from GatewaySecurityPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewaySecurityPolicyName` |  `string`   
A fully-qualified path representing GatewaySecurityPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromGatewaySecurityPolicyRuleName(gatewaySecurityPolicyRuleName)
    
    
    matchProjectFromGatewaySecurityPolicyRuleName(gatewaySecurityPolicyRuleName: string): string | number;

Parse the project from GatewaySecurityPolicyRule resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewaySecurityPolicyRuleName` |  `string`   
A fully-qualified path representing GatewaySecurityPolicyRule resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromInterceptDeploymentGroupName(interceptDeploymentGroupName)
    
    
    matchProjectFromInterceptDeploymentGroupName(interceptDeploymentGroupName: string): string | number;

Parse the project from InterceptDeploymentGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptDeploymentGroupName` |  `string`   
A fully-qualified path representing InterceptDeploymentGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromInterceptDeploymentName(interceptDeploymentName)
    
    
    matchProjectFromInterceptDeploymentName(interceptDeploymentName: string): string | number;

Parse the project from InterceptDeployment resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptDeploymentName` |  `string`   
A fully-qualified path representing InterceptDeployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromInterceptEndpointGroupAssociationName(interceptEndpointGroupAssociationName)
    
    
    matchProjectFromInterceptEndpointGroupAssociationName(interceptEndpointGroupAssociationName: string): string | number;

Parse the project from InterceptEndpointGroupAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptEndpointGroupAssociationName` |  `string`   
A fully-qualified path representing InterceptEndpointGroupAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromInterceptEndpointGroupName(interceptEndpointGroupName)
    
    
    matchProjectFromInterceptEndpointGroupName(interceptEndpointGroupName: string): string | number;

Parse the project from InterceptEndpointGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`interceptEndpointGroupName` |  `string`   
A fully-qualified path representing InterceptEndpointGroup resource.  
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
  
### matchProjectFromMirroringDeploymentGroupName(mirroringDeploymentGroupName)
    
    
    matchProjectFromMirroringDeploymentGroupName(mirroringDeploymentGroupName: string): string | number;

Parse the project from MirroringDeploymentGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringDeploymentGroupName` |  `string`   
A fully-qualified path representing MirroringDeploymentGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMirroringDeploymentName(mirroringDeploymentName)
    
    
    matchProjectFromMirroringDeploymentName(mirroringDeploymentName: string): string | number;

Parse the project from MirroringDeployment resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringDeploymentName` |  `string`   
A fully-qualified path representing MirroringDeployment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMirroringEndpointGroupAssociationName(mirroringEndpointGroupAssociationName)
    
    
    matchProjectFromMirroringEndpointGroupAssociationName(mirroringEndpointGroupAssociationName: string): string | number;

Parse the project from MirroringEndpointGroupAssociation resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringEndpointGroupAssociationName` |  `string`   
A fully-qualified path representing MirroringEndpointGroupAssociation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMirroringEndpointGroupName(mirroringEndpointGroupName)
    
    
    matchProjectFromMirroringEndpointGroupName(mirroringEndpointGroupName: string): string | number;

Parse the project from MirroringEndpointGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`mirroringEndpointGroupName` |  `string`   
A fully-qualified path representing MirroringEndpointGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPartnerSSEGatewayName(partnerSSEGatewayName)
    
    
    matchProjectFromPartnerSSEGatewayName(partnerSSEGatewayName: string): string | number;

Parse the project from PartnerSSEGateway resource.

**Parameter**  
---  
**Name** | **Description**  
`partnerSSEGatewayName` |  `string`   
A fully-qualified path representing PartnerSSEGateway resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPartnerSSERealmName(partnerSSERealmName)
    
    
    matchProjectFromPartnerSSERealmName(partnerSSERealmName: string): string | number;

Parse the project from PartnerSSERealm resource.

**Parameter**  
---  
**Name** | **Description**  
`partnerSSERealmName` |  `string`   
A fully-qualified path representing PartnerSSERealm resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationFirewallEndpointsName(projectLocationFirewallEndpointsName)
    
    
    matchProjectFromProjectLocationFirewallEndpointsName(projectLocationFirewallEndpointsName: string): string | number;

Parse the project from ProjectLocationFirewallEndpoints resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationFirewallEndpointsName` |  `string`   
A fully-qualified path representing project_location_firewallEndpoints resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationSecurityProfileGroupName(projectLocationSecurityProfileGroupName)
    
    
    matchProjectFromProjectLocationSecurityProfileGroupName(projectLocationSecurityProfileGroupName: string): string | number;

Parse the project from ProjectLocationSecurityProfileGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationSecurityProfileGroupName` |  `string`   
A fully-qualified path representing project_location_security_profile_group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationSecurityProfileName(projectLocationSecurityProfileName)
    
    
    matchProjectFromProjectLocationSecurityProfileName(projectLocationSecurityProfileName: string): string | number;

Parse the project from ProjectLocationSecurityProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationSecurityProfileName` |  `string`   
A fully-qualified path representing project_location_security_profile resource.  
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
  
### matchProjectFromSACAttachmentName(sACAttachmentName)
    
    
    matchProjectFromSACAttachmentName(sACAttachmentName: string): string | number;

Parse the project from SACAttachment resource.

**Parameter**  
---  
**Name** | **Description**  
`sACAttachmentName` |  `string`   
A fully-qualified path representing SACAttachment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSACRealmName(sACRealmName)
    
    
    matchProjectFromSACRealmName(sACRealmName: string): string | number;

Parse the project from SACRealm resource.

**Parameter**  
---  
**Name** | **Description**  
`sACRealmName` |  `string`   
A fully-qualified path representing SACRealm resource.  
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
  
### matchProjectFromSSEGatewayReferenceName(sSEGatewayReferenceName)
    
    
    matchProjectFromSSEGatewayReferenceName(sSEGatewayReferenceName: string): string | number;

Parse the project from SSEGatewayReference resource.

**Parameter**  
---  
**Name** | **Description**  
`sSEGatewayReferenceName` |  `string`   
A fully-qualified path representing SSEGatewayReference resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTlsInspectionPolicyName(tlsInspectionPolicyName)
    
    
    matchProjectFromTlsInspectionPolicyName(tlsInspectionPolicyName: string): string | number;

Parse the project from TlsInspectionPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`tlsInspectionPolicyName` |  `string`   
A fully-qualified path representing TlsInspectionPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromUrlListName(urlListName)
    
    
    matchProjectFromUrlListName(urlListName: string): string | number;

Parse the project from UrlList resource.

**Parameter**  
---  
**Name** | **Description**  
`urlListName` |  `string`   
A fully-qualified path representing UrlList resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchRuleFromGatewaySecurityPolicyRuleName(gatewaySecurityPolicyRuleName)
    
    
    matchRuleFromGatewaySecurityPolicyRuleName(gatewaySecurityPolicyRuleName: string): string | number;

Parse the rule from GatewaySecurityPolicyRule resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewaySecurityPolicyRuleName` |  `string`   
A fully-qualified path representing GatewaySecurityPolicyRule resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rule.  
  
### matchSacAttachmentFromSACAttachmentName(sACAttachmentName)
    
    
    matchSacAttachmentFromSACAttachmentName(sACAttachmentName: string): string | number;

Parse the sac_attachment from SACAttachment resource.

**Parameter**  
---  
**Name** | **Description**  
`sACAttachmentName` |  `string`   
A fully-qualified path representing SACAttachment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sac_attachment.  
  
### matchSacRealmFromSACRealmName(sACRealmName)
    
    
    matchSacRealmFromSACRealmName(sACRealmName: string): string | number;

Parse the sac_realm from SACRealm resource.

**Parameter**  
---  
**Name** | **Description**  
`sACRealmName` |  `string`   
A fully-qualified path representing SACRealm resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sac_realm.  
  
### matchSecurityProfileFromOrganizationLocationSecurityProfileName(organizationLocationSecurityProfileName)
    
    
    matchSecurityProfileFromOrganizationLocationSecurityProfileName(organizationLocationSecurityProfileName: string): string | number;

Parse the security_profile from OrganizationLocationSecurityProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationSecurityProfileName` |  `string`   
A fully-qualified path representing organization_location_security_profile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the security_profile.  
  
### matchSecurityProfileFromProjectLocationSecurityProfileName(projectLocationSecurityProfileName)
    
    
    matchSecurityProfileFromProjectLocationSecurityProfileName(projectLocationSecurityProfileName: string): string | number;

Parse the security_profile from ProjectLocationSecurityProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationSecurityProfileName` |  `string`   
A fully-qualified path representing project_location_security_profile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the security_profile.  
  
### matchSecurityProfileGroupFromOrganizationLocationSecurityProfileGroupName(organizationLocationSecurityProfileGroupName)
    
    
    matchSecurityProfileGroupFromOrganizationLocationSecurityProfileGroupName(organizationLocationSecurityProfileGroupName: string): string | number;

Parse the security_profile_group from OrganizationLocationSecurityProfileGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationLocationSecurityProfileGroupName` |  `string`   
A fully-qualified path representing organization_location_security_profile_group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the security_profile_group.  
  
### matchSecurityProfileGroupFromProjectLocationSecurityProfileGroupName(projectLocationSecurityProfileGroupName)
    
    
    matchSecurityProfileGroupFromProjectLocationSecurityProfileGroupName(projectLocationSecurityProfileGroupName: string): string | number;

Parse the security_profile_group from ProjectLocationSecurityProfileGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationSecurityProfileGroupName` |  `string`   
A fully-qualified path representing project_location_security_profile_group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the security_profile_group.  
  
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
  
### matchSseGatewayReferenceFromSSEGatewayReferenceName(sSEGatewayReferenceName)
    
    
    matchSseGatewayReferenceFromSSEGatewayReferenceName(sSEGatewayReferenceName: string): string | number;

Parse the sse_gateway_reference from SSEGatewayReference resource.

**Parameter**  
---  
**Name** | **Description**  
`sSEGatewayReferenceName` |  `string`   
A fully-qualified path representing SSEGatewayReference resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sse_gateway_reference.  
  
### matchTlsInspectionPolicyFromTlsInspectionPolicyName(tlsInspectionPolicyName)
    
    
    matchTlsInspectionPolicyFromTlsInspectionPolicyName(tlsInspectionPolicyName: string): string | number;

Parse the tls_inspection_policy from TlsInspectionPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`tlsInspectionPolicyName` |  `string`   
A fully-qualified path representing TlsInspectionPolicy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tls_inspection_policy.  
  
### matchUrlListFromUrlListName(urlListName)
    
    
    matchUrlListFromUrlListName(urlListName: string): string | number;

Parse the url_list from UrlList resource.

**Parameter**  
---  
**Name** | **Description**  
`urlListName` |  `string`   
A fully-qualified path representing UrlList resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the url_list.  
  
### mirroringDeploymentGroupPath(project, location, mirroringDeploymentGroup)
    
    
    mirroringDeploymentGroupPath(project: string, location: string, mirroringDeploymentGroup: string): string;

Return a fully-qualified mirroringDeploymentGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`mirroringDeploymentGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### mirroringDeploymentPath(project, location, mirroringDeployment)
    
    
    mirroringDeploymentPath(project: string, location: string, mirroringDeployment: string): string;

Return a fully-qualified mirroringDeployment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`mirroringDeployment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### mirroringEndpointGroupAssociationPath(project, location, mirroringEndpointGroupAssociation)
    
    
    mirroringEndpointGroupAssociationPath(project: string, location: string, mirroringEndpointGroupAssociation: string): string;

Return a fully-qualified mirroringEndpointGroupAssociation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`mirroringEndpointGroupAssociation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### mirroringEndpointGroupPath(project, location, mirroringEndpointGroup)
    
    
    mirroringEndpointGroupPath(project: string, location: string, mirroringEndpointGroup: string): string;

Return a fully-qualified mirroringEndpointGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`mirroringEndpointGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### organizationLocationFirewallEndpointsPath(organization, location, firewallEndpoint)
    
    
    organizationLocationFirewallEndpointsPath(organization: string, location: string, firewallEndpoint: string): string;

Return a fully-qualified organizationLocationFirewallEndpoints resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`location` |  `string`   
  
`firewallEndpoint` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### organizationLocationSecurityProfileGroupPath(organization, location, securityProfileGroup)
    
    
    organizationLocationSecurityProfileGroupPath(organization: string, location: string, securityProfileGroup: string): string;

Return a fully-qualified organizationLocationSecurityProfileGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`location` |  `string`   
  
`securityProfileGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### organizationLocationSecurityProfilePath(organization, location, securityProfile)
    
    
    organizationLocationSecurityProfilePath(organization: string, location: string, securityProfile: string): string;

Return a fully-qualified organizationLocationSecurityProfile resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`location` |  `string`   
  
`securityProfile` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### partnerSSEGatewayPath(project, location, partnerSseGateway)
    
    
    partnerSSEGatewayPath(project: string, location: string, partnerSseGateway: string): string;

Return a fully-qualified partnerSSEGateway resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`partnerSseGateway` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### partnerSSERealmPath(project, location, partnerSseRealm)
    
    
    partnerSSERealmPath(project: string, location: string, partnerSseRealm: string): string;

Return a fully-qualified partnerSSERealm resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`partnerSseRealm` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationFirewallEndpointsPath(project, location, firewallEndpoint)
    
    
    projectLocationFirewallEndpointsPath(project: string, location: string, firewallEndpoint: string): string;

Return a fully-qualified projectLocationFirewallEndpoints resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`firewallEndpoint` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationSecurityProfileGroupPath(project, location, securityProfileGroup)
    
    
    projectLocationSecurityProfileGroupPath(project: string, location: string, securityProfileGroup: string): string;

Return a fully-qualified projectLocationSecurityProfileGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`securityProfileGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationSecurityProfilePath(project, location, securityProfile)
    
    
    projectLocationSecurityProfilePath(project: string, location: string, securityProfile: string): string;

Return a fully-qualified projectLocationSecurityProfile resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`securityProfile` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
  
### sACAttachmentPath(project, location, sacAttachment)
    
    
    sACAttachmentPath(project: string, location: string, sacAttachment: string): string;

Return a fully-qualified sACAttachment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sacAttachment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### sACRealmPath(project, location, sacRealm)
    
    
    sACRealmPath(project: string, location: string, sacRealm: string): string;

Return a fully-qualified sACRealm resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sacRealm` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
  
### sSEGatewayReferencePath(project, location, sseGatewayReference)
    
    
    sSEGatewayReferencePath(project: string, location: string, sseGatewayReference: string): string;

Return a fully-qualified sSEGatewayReference resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sseGatewayReference` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
  
### tlsInspectionPolicyPath(project, location, tlsInspectionPolicy)
    
    
    tlsInspectionPolicyPath(project: string, location: string, tlsInspectionPolicy: string): string;

Return a fully-qualified tlsInspectionPolicy resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tlsInspectionPolicy` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updatePartnerSSEGateway(request, options)
    
    
    updatePartnerSSEGateway(request?: protos.google.cloud.networksecurity.v1alpha1.IUpdatePartnerSSEGatewayRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway, protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates a single PartnerSSEGateway.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.iupdatepartnerssegatewayrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway), [protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource being created
       */
      // const partnerSseGateway = {}
      /**
       *  The list of fields to update
       */
      // const updateMask = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server will know to
       *  ignore the request if it has already been completed. The server will
       *  guarantee that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networksecurity library
      const {SSEGatewayServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const networksecurityClient = new [SSEGatewayServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1alpha1.ssegatewayserviceclient.html)();
    
      async function callUpdatePartnerSSEGateway() {
        // Construct request
        const request = {
          partnerSseGateway,
        };
    
        // Run request
        const [operation] = await networksecurityClient.updatePartnerSSEGateway(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdatePartnerSSEGateway();
    
    

### updatePartnerSSEGateway(request, options, callback)
    
    
    updatePartnerSSEGateway(request: protos.google.cloud.networksecurity.v1alpha1.IUpdatePartnerSSEGatewayRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway, protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.iupdatepartnerssegatewayrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway), [protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePartnerSSEGateway(request, callback)
    
    
    updatePartnerSSEGateway(request: protos.google.cloud.networksecurity.v1alpha1.IUpdatePartnerSSEGatewayRequest, callback: Callback<LROperation<protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway, protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePartnerSSEGatewayRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.iupdatepartnerssegatewayrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networksecurity.v1alpha1.IPartnerSSEGateway](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ipartnerssegateway), [protos.google.cloud.networksecurity.v1alpha1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1alpha1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### urlListPath(project, location, urlList)
    
    
    urlListPath(project: string, location: string, urlList: string): string;

Return a fully-qualified urlList resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`urlList` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
