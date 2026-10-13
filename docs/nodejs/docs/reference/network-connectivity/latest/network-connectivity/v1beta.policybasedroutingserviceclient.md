---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/v1beta.policybasedroutingserviceclient
title: Class v1beta.PolicyBasedRoutingServiceClient (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:03.785738+00:00
---

# Class v1beta.PolicyBasedRoutingServiceClient (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/v1beta.policybasedroutingserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.PolicyBasedRoutingServiceClient (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.6.0  4.2.0  3.6.0  3.2.0  2.3.3  2.2.0  2.1.2  1.5.0  1.4.2  1.3.0  1.2.1  1.1.6 

Policy-Based Routing allows GCP customers to specify flexibile routing policies for Layer 4 traffic traversing through the connected service. v1beta

## Package

[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of PolicyBasedRoutingServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new PolicyBasedRoutingServiceClient({fallback: true}, gax); ```  
  
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

### policyBasedRoutingServiceStub
    
    
    policyBasedRoutingServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreatePolicyBasedRouteProgress(name)
    
    
    checkCreatePolicyBasedRouteProgress(name: string): Promise<LROperation<protos.google.cloud.networkconnectivity.v1beta.PolicyBasedRoute, protos.google.cloud.networkconnectivity.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `createPolicyBasedRoute()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.networkconnectivity.v1beta.PolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.policybasedroute-class), [protos.google.cloud.networkconnectivity.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource's name of the PolicyBasedRoute.
       */
      // const parent = 'abc123'
      /**
       *  Required. Unique id for the policy-based route to create. Provided by the
       *  client when the resource is created. The name must comply with
       *  https://google.aip.dev/122#resource-id-segments. Specifically, the name
       *  must be 1-63 characters long and match the regular expression
       *  a-z(a-z0-9-*a-z0-9)?. The first character must be a lowercase letter,
       *  and all following characters (except for the last character) must be a
       *  dash, lowercase letter, or digit. The last character must be a lowercase
       *  letter or digit.
       */
      // const policyBasedRouteId = 'abc123'
      /**
       *  Required. Initial values for a new policy-based route.
       */
      // const policyBasedRoute = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server knows to
       *  ignore the request if it has already been completed. The server guarantees
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, ignores the second request. This prevents clients
       *  from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {PolicyBasedRoutingServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callCreatePolicyBasedRoute() {
        // Construct request
        const request = {
          parent,
          policyBasedRouteId,
          policyBasedRoute,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.createPolicyBasedRoute(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreatePolicyBasedRoute();
    
    

### checkDeletePolicyBasedRouteProgress(name)
    
    
    checkDeletePolicyBasedRouteProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.networkconnectivity.v1beta.OperationMetadata>>;

Check the status of the long running operation returned by `deletePolicyBasedRoute()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), [protos.google.cloud.networkconnectivity.v1beta.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the policy-based route resource to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server knows to
       *  ignore the request if it has already been completed. The server guarantees
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, ignores the second request. This prevents clients
       *  from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {PolicyBasedRoutingServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callDeletePolicyBasedRoute() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.deletePolicyBasedRoute(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeletePolicyBasedRoute();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createPolicyBasedRoute(request, options)
    
    
    createPolicyBasedRoute(request?: protos.google.cloud.networkconnectivity.v1beta.ICreatePolicyBasedRouteRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new policy-based route in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatepolicybasedrouterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ipolicybasedroute), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource's name of the PolicyBasedRoute.
       */
      // const parent = 'abc123'
      /**
       *  Required. Unique id for the policy-based route to create. Provided by the
       *  client when the resource is created. The name must comply with
       *  https://google.aip.dev/122#resource-id-segments. Specifically, the name
       *  must be 1-63 characters long and match the regular expression
       *  a-z(a-z0-9-*a-z0-9)?. The first character must be a lowercase letter,
       *  and all following characters (except for the last character) must be a
       *  dash, lowercase letter, or digit. The last character must be a lowercase
       *  letter or digit.
       */
      // const policyBasedRouteId = 'abc123'
      /**
       *  Required. Initial values for a new policy-based route.
       */
      // const policyBasedRoute = {}
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server knows to
       *  ignore the request if it has already been completed. The server guarantees
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, ignores the second request. This prevents clients
       *  from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {PolicyBasedRoutingServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callCreatePolicyBasedRoute() {
        // Construct request
        const request = {
          parent,
          policyBasedRouteId,
          policyBasedRoute,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.createPolicyBasedRoute(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreatePolicyBasedRoute();
    
    

### createPolicyBasedRoute(request, options, callback)
    
    
    createPolicyBasedRoute(request: protos.google.cloud.networkconnectivity.v1beta.ICreatePolicyBasedRouteRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatepolicybasedrouterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ipolicybasedroute), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPolicyBasedRoute(request, callback)
    
    
    createPolicyBasedRoute(request: protos.google.cloud.networkconnectivity.v1beta.ICreatePolicyBasedRouteRequest, callback: Callback<LROperation<protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatepolicybasedrouterequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ipolicybasedroute), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### deletePolicyBasedRoute(request, options)
    
    
    deletePolicyBasedRoute(request?: protos.google.cloud.networkconnectivity.v1beta.IDeletePolicyBasedRouteRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes a single policy-based route.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletepolicybasedrouterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the policy-based route resource to delete.
       */
      // const name = 'abc123'
      /**
       *  Optional. An optional request ID to identify requests. Specify a unique
       *  request ID so that if you must retry your request, the server knows to
       *  ignore the request if it has already been completed. The server guarantees
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, ignores the second request. This prevents clients
       *  from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Networkconnectivity library
      const {PolicyBasedRoutingServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callDeletePolicyBasedRoute() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await networkconnectivityClient.deletePolicyBasedRoute(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeletePolicyBasedRoute();
    
    

### deletePolicyBasedRoute(request, options, callback)
    
    
    deletePolicyBasedRoute(request: protos.google.cloud.networkconnectivity.v1beta.IDeletePolicyBasedRouteRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletepolicybasedrouterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePolicyBasedRoute(request, callback)
    
    
    deletePolicyBasedRoute(request: protos.google.cloud.networkconnectivity.v1beta.IDeletePolicyBasedRouteRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletepolicybasedrouterequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.protobuf.iempty), [protos.google.cloud.networkconnectivity.v1beta.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### destinationPath(project, location, multicloudDataTransferConfig, destination)
    
    
    destinationPath(project: string, location: string, multicloudDataTransferConfig: string, destination: string): string;

Return a fully-qualified destination resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`multicloudDataTransferConfig` |  `string`   
  
`destination` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### gatewayAdvertisedRoutePath(project, location, spoke, gatewayAdvertisedRoute)
    
    
    gatewayAdvertisedRoutePath(project: string, location: string, spoke: string, gatewayAdvertisedRoute: string): string;

Return a fully-qualified gatewayAdvertisedRoute resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`spoke` |  `string`   
  
`gatewayAdvertisedRoute` |  `string`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)]>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    const name = '';
    const [response] = await client.getOperation({name});
    // doThingsWith(response)
    

### getPolicyBasedRoute(request, options)
    
    
    getPolicyBasedRoute(request?: protos.google.cloud.networkconnectivity.v1beta.IGetPolicyBasedRouteRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute,
            (protos.google.cloud.networkconnectivity.v1beta.IGetPolicyBasedRouteRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single policy-based route.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetpolicybasedrouterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ipolicybasedroute), ([protos.google.cloud.networkconnectivity.v1beta.IGetPolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetpolicybasedrouterequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the PolicyBasedRoute resource to get.
       */
      // const name = 'abc123'
    
      // Imports the Networkconnectivity library
      const {PolicyBasedRoutingServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callGetPolicyBasedRoute() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networkconnectivityClient.getPolicyBasedRoute(request);
        console.log(response);
      }
    
      callGetPolicyBasedRoute();
    
    

### getPolicyBasedRoute(request, options, callback)
    
    
    getPolicyBasedRoute(request: protos.google.cloud.networkconnectivity.v1beta.IGetPolicyBasedRouteRequest, options: CallOptions, callback: Callback<protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute, protos.google.cloud.networkconnectivity.v1beta.IGetPolicyBasedRouteRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetpolicybasedrouterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ipolicybasedroute), [protos.google.cloud.networkconnectivity.v1beta.IGetPolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetpolicybasedrouterequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPolicyBasedRoute(request, callback)
    
    
    getPolicyBasedRoute(request: protos.google.cloud.networkconnectivity.v1beta.IGetPolicyBasedRouteRequest, callback: Callback<protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute, protos.google.cloud.networkconnectivity.v1beta.IGetPolicyBasedRouteRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetpolicybasedrouterequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ipolicybasedroute), [protos.google.cloud.networkconnectivity.v1beta.IGetPolicyBasedRouteRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetpolicybasedrouterequest) | null | undefined, {} | null | undefined>`   
  
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
  
### groupPath(project, hub, group)
    
    
    groupPath(project: string, hub: string, group: string): string;

Return a fully-qualified group resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`hub` |  `string`   
  
`group` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### hubPath(project, hub)
    
    
    hubPath(project: string, hub: string): string;

Return a fully-qualified hub resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`hub` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### hubRoutePath(project, hub, routeTable, route)
    
    
    hubRoutePath(project: string, hub: string, routeTable: string, route: string): string;

Return a fully-qualified hubRoute resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`hub` |  `string`   
  
`routeTable` |  `string`   
  
`route` |  `string`   
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### listPolicyBasedRoutes(request, options)
    
    
    listPolicyBasedRoutes(request?: protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute[],
            protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest | null,
            protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesResponse
        ]>;

Lists policy-based routes in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPolicyBasedRoutesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ipolicybasedroute)[], [protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesrequest) | null, [protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listPolicyBasedRoutesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPolicyBasedRoutes(request, options, callback)
    
    
    listPolicyBasedRoutes(request: protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest, protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesResponse | null | undefined, protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPolicyBasedRoutesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesrequest), [protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ipolicybasedroute)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPolicyBasedRoutes(request, callback)
    
    
    listPolicyBasedRoutes(request: protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest, callback: PaginationCallback<protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest, protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesResponse | null | undefined, protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPolicyBasedRoutesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesrequest), [protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesresponse) | null | undefined, [protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ipolicybasedroute)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPolicyBasedRoutesAsync(request, options)
    
    
    listPolicyBasedRoutesAsync(request?: protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute>;

Equivalent to `listPolicyBasedRoutes`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPolicyBasedRoutesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networkconnectivity.v1beta.IPolicyBasedRoute](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ipolicybasedroute)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource's name.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of results per page that should be returned.
       */
      // const pageSize = 1234
      /**
       *  The page token.
       */
      // const pageToken = 'abc123'
      /**
       *  A filter expression that filters the results listed in the response.
       */
      // const filter = 'abc123'
      /**
       *  Sort the results by a certain order.
       */
      // const orderBy = 'abc123'
    
      // Imports the Networkconnectivity library
      const {PolicyBasedRoutingServiceClient} = require('[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const networkconnectivityClient = new [PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)();
    
      async function callListPolicyBasedRoutes() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networkconnectivityClient.listPolicyBasedRoutesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListPolicyBasedRoutes();
    
    

### listPolicyBasedRoutesStream(request, options)
    
    
    listPolicyBasedRoutesStream(request?: protos.google.cloud.networkconnectivity.v1beta.IListPolicyBasedRoutesRequest, options?: CallOptions): Transform;

Equivalent to `listPolicyBasedRoutes`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPolicyBasedRoutesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistpolicybasedroutesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listPolicyBasedRoutesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchDestinationFromDestinationName(destinationName)
    
    
    matchDestinationFromDestinationName(destinationName: string): string | number;

Parse the destination from Destination resource.

**Parameter**  
---  
**Name** | **Description**  
`destinationName` |  `string`   
A fully-qualified path representing Destination resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the destination.  
  
### matchGatewayAdvertisedRouteFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName)
    
    
    matchGatewayAdvertisedRouteFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName: string): string | number;

Parse the gateway_advertised_route from GatewayAdvertisedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewayAdvertisedRouteName` |  `string`   
A fully-qualified path representing GatewayAdvertisedRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the gateway_advertised_route.  
  
### matchGroupFromGroupName(groupName)
    
    
    matchGroupFromGroupName(groupName: string): string | number;

Parse the group from Group resource.

**Parameter**  
---  
**Name** | **Description**  
`groupName` |  `string`   
A fully-qualified path representing Group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the group.  
  
### matchHubFromGroupName(groupName)
    
    
    matchHubFromGroupName(groupName: string): string | number;

Parse the hub from Group resource.

**Parameter**  
---  
**Name** | **Description**  
`groupName` |  `string`   
A fully-qualified path representing Group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hub.  
  
### matchHubFromHubName(hubName)
    
    
    matchHubFromHubName(hubName: string): string | number;

Parse the hub from Hub resource.

**Parameter**  
---  
**Name** | **Description**  
`hubName` |  `string`   
A fully-qualified path representing Hub resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hub.  
  
### matchHubFromHubRouteName(hubRouteName)
    
    
    matchHubFromHubRouteName(hubRouteName: string): string | number;

Parse the hub from HubRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`hubRouteName` |  `string`   
A fully-qualified path representing HubRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hub.  
  
### matchHubFromRouteTableName(routeTableName)
    
    
    matchHubFromRouteTableName(routeTableName: string): string | number;

Parse the hub from RouteTable resource.

**Parameter**  
---  
**Name** | **Description**  
`routeTableName` |  `string`   
A fully-qualified path representing RouteTable resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the hub.  
  
### matchLocationFromDestinationName(destinationName)
    
    
    matchLocationFromDestinationName(destinationName: string): string | number;

Parse the location from Destination resource.

**Parameter**  
---  
**Name** | **Description**  
`destinationName` |  `string`   
A fully-qualified path representing Destination resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName)
    
    
    matchLocationFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName: string): string | number;

Parse the location from GatewayAdvertisedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewayAdvertisedRouteName` |  `string`   
A fully-qualified path representing GatewayAdvertisedRoute resource.  
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
  
### matchLocationFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName)
    
    
    matchLocationFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName: string): string | number;

Parse the location from MulticloudDataTransferConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferConfigName` |  `string`   
A fully-qualified path representing MulticloudDataTransferConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName)
    
    
    matchLocationFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName: string): string | number;

Parse the location from MulticloudDataTransferSupportedService resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferSupportedServiceName` |  `string`   
A fully-qualified path representing MulticloudDataTransferSupportedService resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRemoteTransportProfileName(remoteTransportProfileName)
    
    
    matchLocationFromRemoteTransportProfileName(remoteTransportProfileName: string): string | number;

Parse the location from RemoteTransportProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`remoteTransportProfileName` |  `string`   
A fully-qualified path representing RemoteTransportProfile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSpokeName(spokeName)
    
    
    matchLocationFromSpokeName(spokeName: string): string | number;

Parse the location from Spoke resource.

**Parameter**  
---  
**Name** | **Description**  
`spokeName` |  `string`   
A fully-qualified path representing Spoke resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTransportName(transportName)
    
    
    matchLocationFromTransportName(transportName: string): string | number;

Parse the location from Transport resource.

**Parameter**  
---  
**Name** | **Description**  
`transportName` |  `string`   
A fully-qualified path representing Transport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMulticloudDataTransferConfigFromDestinationName(destinationName)
    
    
    matchMulticloudDataTransferConfigFromDestinationName(destinationName: string): string | number;

Parse the multicloud_data_transfer_config from Destination resource.

**Parameter**  
---  
**Name** | **Description**  
`destinationName` |  `string`   
A fully-qualified path representing Destination resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the multicloud_data_transfer_config.  
  
### matchMulticloudDataTransferConfigFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName)
    
    
    matchMulticloudDataTransferConfigFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName: string): string | number;

Parse the multicloud_data_transfer_config from MulticloudDataTransferConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferConfigName` |  `string`   
A fully-qualified path representing MulticloudDataTransferConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the multicloud_data_transfer_config.  
  
### matchMulticloudDataTransferSupportedServiceFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName)
    
    
    matchMulticloudDataTransferSupportedServiceFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName: string): string | number;

Parse the multicloud_data_transfer_supported_service from MulticloudDataTransferSupportedService resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferSupportedServiceName` |  `string`   
A fully-qualified path representing MulticloudDataTransferSupportedService resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the multicloud_data_transfer_supported_service.  
  
### matchPolicyBasedRouteFromPolicyBasedRouteName(policyBasedRouteName)
    
    
    matchPolicyBasedRouteFromPolicyBasedRouteName(policyBasedRouteName: string): string | number;

Parse the policy_based_route from PolicyBasedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`policyBasedRouteName` |  `string`   
A fully-qualified path representing PolicyBasedRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the policy_based_route.  
  
### matchProjectFromDestinationName(destinationName)
    
    
    matchProjectFromDestinationName(destinationName: string): string | number;

Parse the project from Destination resource.

**Parameter**  
---  
**Name** | **Description**  
`destinationName` |  `string`   
A fully-qualified path representing Destination resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName)
    
    
    matchProjectFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName: string): string | number;

Parse the project from GatewayAdvertisedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewayAdvertisedRouteName` |  `string`   
A fully-qualified path representing GatewayAdvertisedRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromGroupName(groupName)
    
    
    matchProjectFromGroupName(groupName: string): string | number;

Parse the project from Group resource.

**Parameter**  
---  
**Name** | **Description**  
`groupName` |  `string`   
A fully-qualified path representing Group resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromHubName(hubName)
    
    
    matchProjectFromHubName(hubName: string): string | number;

Parse the project from Hub resource.

**Parameter**  
---  
**Name** | **Description**  
`hubName` |  `string`   
A fully-qualified path representing Hub resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromHubRouteName(hubRouteName)
    
    
    matchProjectFromHubRouteName(hubRouteName: string): string | number;

Parse the project from HubRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`hubRouteName` |  `string`   
A fully-qualified path representing HubRoute resource.  
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
  
### matchProjectFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName)
    
    
    matchProjectFromMulticloudDataTransferConfigName(multicloudDataTransferConfigName: string): string | number;

Parse the project from MulticloudDataTransferConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferConfigName` |  `string`   
A fully-qualified path representing MulticloudDataTransferConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName)
    
    
    matchProjectFromMulticloudDataTransferSupportedServiceName(multicloudDataTransferSupportedServiceName: string): string | number;

Parse the project from MulticloudDataTransferSupportedService resource.

**Parameter**  
---  
**Name** | **Description**  
`multicloudDataTransferSupportedServiceName` |  `string`   
A fully-qualified path representing MulticloudDataTransferSupportedService resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromNetworkName(networkName)
    
    
    matchProjectFromNetworkName(networkName: string): string | number;

Parse the project from Network resource.

**Parameter**  
---  
**Name** | **Description**  
`networkName` |  `string`   
A fully-qualified path representing Network resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPolicyBasedRouteName(policyBasedRouteName)
    
    
    matchProjectFromPolicyBasedRouteName(policyBasedRouteName: string): string | number;

Parse the project from PolicyBasedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`policyBasedRouteName` |  `string`   
A fully-qualified path representing PolicyBasedRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRemoteTransportProfileName(remoteTransportProfileName)
    
    
    matchProjectFromRemoteTransportProfileName(remoteTransportProfileName: string): string | number;

Parse the project from RemoteTransportProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`remoteTransportProfileName` |  `string`   
A fully-qualified path representing RemoteTransportProfile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRouteTableName(routeTableName)
    
    
    matchProjectFromRouteTableName(routeTableName: string): string | number;

Parse the project from RouteTable resource.

**Parameter**  
---  
**Name** | **Description**  
`routeTableName` |  `string`   
A fully-qualified path representing RouteTable resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSpokeName(spokeName)
    
    
    matchProjectFromSpokeName(spokeName: string): string | number;

Parse the project from Spoke resource.

**Parameter**  
---  
**Name** | **Description**  
`spokeName` |  `string`   
A fully-qualified path representing Spoke resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTransportName(transportName)
    
    
    matchProjectFromTransportName(transportName: string): string | number;

Parse the project from Transport resource.

**Parameter**  
---  
**Name** | **Description**  
`transportName` |  `string`   
A fully-qualified path representing Transport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchRemoteTransportProfileFromRemoteTransportProfileName(remoteTransportProfileName)
    
    
    matchRemoteTransportProfileFromRemoteTransportProfileName(remoteTransportProfileName: string): string | number;

Parse the remote_transport_profile from RemoteTransportProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`remoteTransportProfileName` |  `string`   
A fully-qualified path representing RemoteTransportProfile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the remote_transport_profile.  
  
### matchResourceIdFromNetworkName(networkName)
    
    
    matchResourceIdFromNetworkName(networkName: string): string | number;

Parse the resource_id from Network resource.

**Parameter**  
---  
**Name** | **Description**  
`networkName` |  `string`   
A fully-qualified path representing Network resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the resource_id.  
  
### matchRouteFromHubRouteName(hubRouteName)
    
    
    matchRouteFromHubRouteName(hubRouteName: string): string | number;

Parse the route from HubRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`hubRouteName` |  `string`   
A fully-qualified path representing HubRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the route.  
  
### matchRouteTableFromHubRouteName(hubRouteName)
    
    
    matchRouteTableFromHubRouteName(hubRouteName: string): string | number;

Parse the route_table from HubRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`hubRouteName` |  `string`   
A fully-qualified path representing HubRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the route_table.  
  
### matchRouteTableFromRouteTableName(routeTableName)
    
    
    matchRouteTableFromRouteTableName(routeTableName: string): string | number;

Parse the route_table from RouteTable resource.

**Parameter**  
---  
**Name** | **Description**  
`routeTableName` |  `string`   
A fully-qualified path representing RouteTable resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the route_table.  
  
### matchSpokeFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName)
    
    
    matchSpokeFromGatewayAdvertisedRouteName(gatewayAdvertisedRouteName: string): string | number;

Parse the spoke from GatewayAdvertisedRoute resource.

**Parameter**  
---  
**Name** | **Description**  
`gatewayAdvertisedRouteName` |  `string`   
A fully-qualified path representing GatewayAdvertisedRoute resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the spoke.  
  
### matchSpokeFromSpokeName(spokeName)
    
    
    matchSpokeFromSpokeName(spokeName: string): string | number;

Parse the spoke from Spoke resource.

**Parameter**  
---  
**Name** | **Description**  
`spokeName` |  `string`   
A fully-qualified path representing Spoke resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the spoke.  
  
### matchTransportFromTransportName(transportName)
    
    
    matchTransportFromTransportName(transportName: string): string | number;

Parse the transport from Transport resource.

**Parameter**  
---  
**Name** | **Description**  
`transportName` |  `string`   
A fully-qualified path representing Transport resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the transport.  
  
### multicloudDataTransferConfigPath(project, location, multicloudDataTransferConfig)
    
    
    multicloudDataTransferConfigPath(project: string, location: string, multicloudDataTransferConfig: string): string;

Return a fully-qualified multicloudDataTransferConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`multicloudDataTransferConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### multicloudDataTransferSupportedServicePath(project, location, multicloudDataTransferSupportedService)
    
    
    multicloudDataTransferSupportedServicePath(project: string, location: string, multicloudDataTransferSupportedService: string): string;

Return a fully-qualified multicloudDataTransferSupportedService resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`multicloudDataTransferSupportedService` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### networkPath(project, resourceId)
    
    
    networkPath(project: string, resourceId: string): string;

Return a fully-qualified network resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`resourceId` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### policyBasedRoutePath(project, policyBasedRoute)
    
    
    policyBasedRoutePath(project: string, policyBasedRoute: string): string;

Return a fully-qualified policyBasedRoute resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`policyBasedRoute` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### remoteTransportProfilePath(project, location, remoteTransportProfile)
    
    
    remoteTransportProfilePath(project: string, location: string, remoteTransportProfile: string): string;

Return a fully-qualified remoteTransportProfile resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`remoteTransportProfile` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### routeTablePath(project, hub, routeTable)
    
    
    routeTablePath(project: string, hub: string, routeTable: string): string;

Return a fully-qualified routeTable resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`hub` |  `string`   
  
`routeTable` |  `string`   
  
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
  
### spokePath(project, location, spoke)
    
    
    spokePath(project: string, location: string, spoke: string): string;

Return a fully-qualified spoke resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`spoke` |  `string`   
  
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
  
### transportPath(project, location, transport)
    
    
    transportPath(project: string, location: string, transport: string): string;

Return a fully-qualified transport resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`transport` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
