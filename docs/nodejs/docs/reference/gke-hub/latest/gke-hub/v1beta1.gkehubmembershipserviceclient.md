---
url: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient
title: Class v1beta1.GkeHubMembershipServiceClient (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:01.629444+00:00
---

# Class v1beta1.GkeHubMembershipServiceClient (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.GkeHubMembershipServiceClient (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.4.0  6.1.0  6.0.1  5.0.0  4.5.0  4.4.0  4.2.0  3.4.0  3.3.1  3.2.2  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.1  1.1.4 

The GKE Hub MembershipService handles the registration of many Kubernetes clusters to Google Cloud, represented with the resource.

GKE Hub is currently available in the global region and all regions in <https://cloud.google.com/compute/docs/regions-zones>.

**Membership management may be non-trivial:** it is recommended to use one of the Google-provided client libraries or tools where possible when working with Membership resources. v1beta1

## Package

[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of GkeHubMembershipServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new GkeHubMembershipServiceClient({fallback: true}, gax); ```  
  
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

### gkeHubMembershipServiceStub
    
    
    gkeHubMembershipServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkCreateMembershipProgress(name)
    
    
    checkCreateMembershipProgress(name: string): Promise<LROperation<protos.google.cloud.gkehub.v1beta1.Membership, protos.google.cloud.gkehub.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `createMembership()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gkehub.v1beta1.Membership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.membership-class), [protos.google.cloud.gkehub.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent (project and location) where the Memberships will be
       *  created. Specified in the format `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Client chosen ID for the membership. `membership_id` must be a
       *  valid RFC 1123 compliant DNS label:
       *    1. At most 63 characters in length
       *    2. It must consist of lower case alphanumeric characters or `-`
       *    3. It must start and end with an alphanumeric character
       *  Which can be expressed as the regex: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`,
       *  with a maximum length of 63 characters.
       */
      // const membershipId = 'abc123'
      /**
       *  Required. The membership to create.
       */
      // const resource = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callCreateMembership() {
        // Construct request
        const request = {
          parent,
          membershipId,
          resource,
        };
    
        // Run request
        const [operation] = await gkehubClient.createMembership(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateMembership();
    
    

### checkDeleteMembershipProgress(name)
    
    
    checkDeleteMembershipProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.gkehub.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `deleteMembership()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.empty), [protos.google.cloud.gkehub.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Membership resource name in the format
       *  `projects/* /locations/* /memberships/*`.
       */
      // const name = 'abc123'
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
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
       *  Optional. If set to true, any subresource from this Membership will also be
       *  deleted. Otherwise, the request will only work if the Membership has no
       *  subresource.
       */
      // const force = true
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callDeleteMembership() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gkehubClient.deleteMembership(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteMembership();
    
    

### checkUpdateMembershipProgress(name)
    
    
    checkUpdateMembershipProgress(name: string): Promise<LROperation<protos.google.cloud.gkehub.v1beta1.Membership, protos.google.cloud.gkehub.v1beta1.OperationMetadata>>;

Check the status of the long running operation returned by `updateMembership()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.gkehub.v1beta1.Membership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.membership-class), [protos.google.cloud.gkehub.v1beta1.OperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.operationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The membership resource name in the format:
       *  `projects/[project_id]/locations/global/memberships/[membership_id]`
       */
      // const name = 'abc123'
      /**
       *  Required. Mask of fields to update. At least one field path must be
       *  specified in this mask.
       */
      // const updateMask = {}
      /**
       *  Required. Only fields specified in update_mask are updated.
       *  If you specify a field in the update_mask but don't specify its value here
       *  that field will be deleted.
       *  If you are updating a map field, set the value of a key to null or empty
       *  string to delete the key from the map. It's not possible to update a key's
       *  value to the empty string.
       *  If you specify the update_mask to be a special path "*", fully replaces all
       *  user-modifiable fields to match `resource`.
       */
      // const resource = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callUpdateMembership() {
        // Construct request
        const request = {
          name,
          updateMask,
          resource,
        };
    
        // Run request
        const [operation] = await gkehubClient.updateMembership(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateMembership();
    
    

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createMembership(request, options)
    
    
    createMembership(request?: protos.google.cloud.gkehub.v1beta1.ICreateMembershipRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gkehub.v1beta1.IMembership, protos.google.cloud.gkehub.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Creates a new Membership.

**This is currently only supported for GKE clusters on Google Cloud**. To register other clusters, follow the instructions at <https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster>.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.icreatemembershiprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership), [protos.google.cloud.gkehub.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent (project and location) where the Memberships will be
       *  created. Specified in the format `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  Required. Client chosen ID for the membership. `membership_id` must be a
       *  valid RFC 1123 compliant DNS label:
       *    1. At most 63 characters in length
       *    2. It must consist of lower case alphanumeric characters or `-`
       *    3. It must start and end with an alphanumeric character
       *  Which can be expressed as the regex: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`,
       *  with a maximum length of 63 characters.
       */
      // const membershipId = 'abc123'
      /**
       *  Required. The membership to create.
       */
      // const resource = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callCreateMembership() {
        // Construct request
        const request = {
          parent,
          membershipId,
          resource,
        };
    
        // Run request
        const [operation] = await gkehubClient.createMembership(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callCreateMembership();
    
    

### createMembership(request, options, callback)
    
    
    createMembership(request: protos.google.cloud.gkehub.v1beta1.ICreateMembershipRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gkehub.v1beta1.IMembership, protos.google.cloud.gkehub.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.icreatemembershiprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership), [protos.google.cloud.gkehub.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMembership(request, callback)
    
    
    createMembership(request: protos.google.cloud.gkehub.v1beta1.ICreateMembershipRequest, callback: Callback<LROperation<protos.google.cloud.gkehub.v1beta1.IMembership, protos.google.cloud.gkehub.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.icreatemembershiprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership), [protos.google.cloud.gkehub.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMembership(request, options)
    
    
    deleteMembership(request?: protos.google.cloud.gkehub.v1beta1.IDeleteMembershipRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gkehub.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Removes a Membership.

**This is currently only supported for GKE clusters on Google Cloud**. To unregister other clusters, follow the instructions at <https://cloud.google.com/anthos/multicluster-management/connect/unregistering-a-cluster>.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ideletemembershiprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.iempty), [protos.google.cloud.gkehub.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Membership resource name in the format
       *  `projects/* /locations/* /memberships/*`.
       */
      // const name = 'abc123'
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
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
       *  Optional. If set to true, any subresource from this Membership will also be
       *  deleted. Otherwise, the request will only work if the Membership has no
       *  subresource.
       */
      // const force = true
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callDeleteMembership() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await gkehubClient.deleteMembership(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteMembership();
    
    

### deleteMembership(request, options, callback)
    
    
    deleteMembership(request: protos.google.cloud.gkehub.v1beta1.IDeleteMembershipRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gkehub.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ideletemembershiprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.iempty), [protos.google.cloud.gkehub.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMembership(request, callback)
    
    
    deleteMembership(request: protos.google.cloud.gkehub.v1beta1.IDeleteMembershipRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.gkehub.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ideletemembershiprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.iempty), [protos.google.cloud.gkehub.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### generateConnectManifest(request, options)
    
    
    generateConnectManifest(request?: protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestResponse,
            (protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestRequest | undefined),
            {} | undefined
        ]>;

Generates the manifest for deployment of the GKE connect agent.

**This method is used internally by Google-provided libraries.** Most clients should not need to call this method directly.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateConnectManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateconnectmanifestrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateconnectmanifestresponse), ([protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateconnectmanifestrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GenerateConnectManifestResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.generateconnectmanifestresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Membership resource name the Agent will associate with, in
       *  the format `projects/* /locations/* /memberships/*`.
       */
      // const name = 'abc123'
      /**
       *  Optional. The connect agent to generate manifest for.
       */
      // const connectAgent = {}
      /**
       *  Optional. The Connect agent version to use. Defaults to the most current
       *  version.
       */
      // const version = 'abc123'
      /**
       *  Optional. If true, generate the resources for upgrade only. Some resources
       *  generated only for installation (e.g. secrets) will be excluded.
       */
      // const isUpgrade = true
      /**
       *  Optional. The registry to fetch the connect agent image from. Defaults to
       *  gcr.io/gkeconnect.
       */
      // const registry = 'abc123'
      /**
       *  Optional. The image pull secret content for the registry, if not public.
       */
      // const imagePullSecretContent = Buffer.from('string')
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callGenerateConnectManifest() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gkehubClient.generateConnectManifest(request);
        console.log(response);
      }
    
      callGenerateConnectManifest();
    
    

### generateConnectManifest(request, options, callback)
    
    
    generateConnectManifest(request: protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestRequest, options: CallOptions, callback: Callback<protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestResponse, protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateConnectManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateconnectmanifestrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateconnectmanifestresponse), [protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateconnectmanifestrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateConnectManifest(request, callback)
    
    
    generateConnectManifest(request: protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestRequest, callback: Callback<protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestResponse, protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateConnectManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateconnectmanifestrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateconnectmanifestresponse), [protos.google.cloud.gkehub.v1beta1.IGenerateConnectManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateconnectmanifestrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateExclusivityManifest(request, options)
    
    
    generateExclusivityManifest(request?: protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestResponse,
            (protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestRequest | undefined),
            {} | undefined
        ]>;

GenerateExclusivityManifest generates the manifests to update the exclusivity artifacts in the cluster if needed.

Exclusivity artifacts include the Membership custom resource definition (CRD) and the singleton Membership custom resource (CR). Combined with ValidateExclusivity, exclusivity artifacts guarantee that a Kubernetes cluster is only registered to a single GKE Hub.

The Membership CRD is versioned, and may require conversion when the GKE Hub API server begins serving a newer version of the CRD and corresponding CR. The response will be the converted CRD and CR if there are any differences between the versions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateExclusivityManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateexclusivitymanifestrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateexclusivitymanifestresponse), ([protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateexclusivitymanifestrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [GenerateExclusivityManifestResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.generateexclusivitymanifestresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Membership resource name in the format
       *  `projects/* /locations/* /memberships/*`.
       */
      // const name = 'abc123'
      /**
       *  Optional. The YAML manifest of the membership CRD retrieved by
       *  `kubectl get customresourcedefinitions membership`.
       *  Leave empty if the resource does not exist.
       */
      // const crdManifest = 'abc123'
      /**
       *  Optional. The YAML manifest of the membership CR retrieved by
       *  `kubectl get memberships membership`.
       *  Leave empty if the resource does not exist.
       */
      // const crManifest = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callGenerateExclusivityManifest() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gkehubClient.generateExclusivityManifest(request);
        console.log(response);
      }
    
      callGenerateExclusivityManifest();
    
    

### generateExclusivityManifest(request, options, callback)
    
    
    generateExclusivityManifest(request: protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestRequest, options: CallOptions, callback: Callback<protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestResponse, protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateExclusivityManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateexclusivitymanifestrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateexclusivitymanifestresponse), [protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateexclusivitymanifestrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateExclusivityManifest(request, callback)
    
    
    generateExclusivityManifest(request: protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestRequest, callback: Callback<protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestResponse, protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateExclusivityManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateexclusivitymanifestrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateexclusivitymanifestresponse), [protos.google.cloud.gkehub.v1beta1.IGenerateExclusivityManifestRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igenerateexclusivitymanifestrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getMembership(request, options)
    
    
    getMembership(request?: protos.google.cloud.gkehub.v1beta1.IGetMembershipRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gkehub.v1beta1.IMembership,
            protos.google.cloud.gkehub.v1beta1.IGetMembershipRequest | undefined,
            {} | undefined
        ]>;

Gets the details of a Membership.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igetmembershiprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership), [protos.google.cloud.gkehub.v1beta1.IGetMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igetmembershiprequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Membership resource name in the format
       *  `projects/* /locations/* /memberships/*`.
       */
      // const name = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callGetMembership() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await gkehubClient.getMembership(request);
        console.log(response);
      }
    
      callGetMembership();
    
    

### getMembership(request, options, callback)
    
    
    getMembership(request: protos.google.cloud.gkehub.v1beta1.IGetMembershipRequest, options: CallOptions, callback: Callback<protos.google.cloud.gkehub.v1beta1.IMembership, protos.google.cloud.gkehub.v1beta1.IGetMembershipRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igetmembershiprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership), [protos.google.cloud.gkehub.v1beta1.IGetMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igetmembershiprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMembership(request, callback)
    
    
    getMembership(request: protos.google.cloud.gkehub.v1beta1.IGetMembershipRequest, callback: Callback<protos.google.cloud.gkehub.v1beta1.IMembership, protos.google.cloud.gkehub.v1beta1.IGetMembershipRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igetmembershiprequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership), [protos.google.cloud.gkehub.v1beta1.IGetMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.igetmembershiprequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.operation)]>` |   
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
    

### listMemberships(request, options)
    
    
    listMemberships(request?: protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gkehub.v1beta1.IMembership[],
            protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest | null,
            protos.google.cloud.gkehub.v1beta1.IListMembershipsResponse
        ]>;

Lists Memberships in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMembershipsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership)[], [protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsrequest) | null, [protos.google.cloud.gkehub.v1beta1.IListMembershipsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMembershipsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMemberships(request, options, callback)
    
    
    listMemberships(request: protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest, protos.google.cloud.gkehub.v1beta1.IListMembershipsResponse | null | undefined, protos.google.cloud.gkehub.v1beta1.IMembership>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMembershipsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsrequest), [protos.google.cloud.gkehub.v1beta1.IListMembershipsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsresponse) | null | undefined, [protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMemberships(request, callback)
    
    
    listMemberships(request: protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest, callback: PaginationCallback<protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest, protos.google.cloud.gkehub.v1beta1.IListMembershipsResponse | null | undefined, protos.google.cloud.gkehub.v1beta1.IMembership>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMembershipsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsrequest), [protos.google.cloud.gkehub.v1beta1.IListMembershipsResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsresponse) | null | undefined, [protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMembershipsAsync(request, options)
    
    
    listMembershipsAsync(request?: protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.gkehub.v1beta1.IMembership>;

Equivalent to `listMemberships`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMembershipsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent (project and location) where the Memberships will be
       *  listed. Specified in the format `projects/* /locations/*`.
       *  `projects/* /locations/-` list memberships in all the regions.
       */
      // const parent = 'abc123'
      /**
       *  Optional. When requesting a 'page' of resources, `page_size` specifies
       *  number of resources to return. If unspecified or set to 0, all resources
       *  will be returned.
       */
      // const pageSize = 1234
      /**
       *  Optional. Token returned by previous call to `ListMemberships` which
       *  specifies the position in the list from where to continue listing the
       *  resources.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Lists Memberships that match the filter expression, following the
       *  syntax outlined in https://google.aip.dev/160.
       *  Examples:
       *    - Name is `bar` in project `foo-proj` and location `global`:
       *        name = "projects/foo-proj/locations/global/membership/bar"
       *    - Memberships that have a label called `foo`:
       *        labels.foo:*
       *    - Memberships that have a label called `foo` whose value is `bar`:
       *        labels.foo = bar
       *    - Memberships in the CREATING state:
       *        state = CREATING
       */
      // const filter = 'abc123'
      /**
       *  Optional. One or more fields to compare and use to sort the output.
       *  See https://google.aip.dev/132#ordering.
       */
      // const orderBy = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callListMemberships() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = gkehubClient.listMembershipsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMemberships();
    
    

### listMembershipsStream(request, options)
    
    
    listMembershipsStream(request?: protos.google.cloud.gkehub.v1beta1.IListMembershipsRequest, options?: CallOptions): Transform;

Equivalent to `listMemberships`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMembershipsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ilistmembershipsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMembershipsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
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
  
### matchLocationFromMembershipName(membershipName)
    
    
    matchLocationFromMembershipName(membershipName: string): string | number;

Parse the location from Membership resource.

**Parameter**  
---  
**Name** | **Description**  
`membershipName` |  `string`   
A fully-qualified path representing Membership resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMembershipFromMembershipName(membershipName)
    
    
    matchMembershipFromMembershipName(membershipName: string): string | number;

Parse the membership from Membership resource.

**Parameter**  
---  
**Name** | **Description**  
`membershipName` |  `string`   
A fully-qualified path representing Membership resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the membership.  
  
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
  
### matchProjectFromMembershipName(membershipName)
    
    
    matchProjectFromMembershipName(membershipName: string): string | number;

Parse the project from Membership resource.

**Parameter**  
---  
**Name** | **Description**  
`membershipName` |  `string`   
A fully-qualified path representing Membership resource.  
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
  
### membershipPath(project, location, membership)
    
    
    membershipPath(project: string, location: string, membership: string): string;

Return a fully-qualified membership resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`membership` |  `string`   
  
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
  
### updateMembership(request, options)
    
    
    updateMembership(request?: protos.google.cloud.gkehub.v1beta1.IUpdateMembershipRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.gkehub.v1beta1.IMembership, protos.google.cloud.gkehub.v1beta1.IOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Updates an existing Membership.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.iupdatemembershiprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership), [protos.google.cloud.gkehub.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The membership resource name in the format:
       *  `projects/[project_id]/locations/global/memberships/[membership_id]`
       */
      // const name = 'abc123'
      /**
       *  Required. Mask of fields to update. At least one field path must be
       *  specified in this mask.
       */
      // const updateMask = {}
      /**
       *  Required. Only fields specified in update_mask are updated.
       *  If you specify a field in the update_mask but don't specify its value here
       *  that field will be deleted.
       *  If you are updating a map field, set the value of a key to null or empty
       *  string to delete the key from the map. It's not possible to update a key's
       *  value to the empty string.
       *  If you specify the update_mask to be a special path "*", fully replaces all
       *  user-modifiable fields to match `resource`.
       */
      // const resource = {}
      /**
       *  Optional. A request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes after the first request.
       *  For example, consider a situation where you make an initial request and
       *  the request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callUpdateMembership() {
        // Construct request
        const request = {
          name,
          updateMask,
          resource,
        };
    
        // Run request
        const [operation] = await gkehubClient.updateMembership(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callUpdateMembership();
    
    

### updateMembership(request, options, callback)
    
    
    updateMembership(request: protos.google.cloud.gkehub.v1beta1.IUpdateMembershipRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.gkehub.v1beta1.IMembership, protos.google.cloud.gkehub.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.iupdatemembershiprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership), [protos.google.cloud.gkehub.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMembership(request, callback)
    
    
    updateMembership(request: protos.google.cloud.gkehub.v1beta1.IUpdateMembershipRequest, callback: Callback<LROperation<protos.google.cloud.gkehub.v1beta1.IMembership, protos.google.cloud.gkehub.v1beta1.IOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMembershipRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.iupdatemembershiprequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.gkehub.v1beta1.IMembership](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.imembership), [protos.google.cloud.gkehub.v1beta1.IOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ioperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### validateExclusivity(request, options)
    
    
    validateExclusivity(request?: protos.google.cloud.gkehub.v1beta1.IValidateExclusivityRequest, options?: CallOptions): Promise<[
            protos.google.cloud.gkehub.v1beta1.IValidateExclusivityResponse,
            (protos.google.cloud.gkehub.v1beta1.IValidateExclusivityRequest | undefined),
            {} | undefined
        ]>;

ValidateExclusivity validates the state of exclusivity in the cluster. The validation does not depend on an existing Hub membership resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IValidateExclusivityRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ivalidateexclusivityrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.gkehub.v1beta1.IValidateExclusivityResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ivalidateexclusivityresponse), ([protos.google.cloud.gkehub.v1beta1.IValidateExclusivityRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ivalidateexclusivityrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [ValidateExclusivityResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.validateexclusivityresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent (project and location) where the Memberships will be
       *  created. Specified in the format `projects/* /locations/*`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. The YAML of the membership CR in the cluster. Empty if the
       *  membership CR does not exist.
       */
      // const crManifest = 'abc123'
      /**
       *  Required. The intended membership name under the `parent`. This method only
       *  does validation in anticipation of a CreateMembership call with the same
       *  name.
       */
      // const intendedMembership = 'abc123'
    
      // Imports the Gkehub library
      const {GkeHubMembershipServiceClient} = require('[@google-cloud/gke-hub](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const gkehubClient = new [GkeHubMembershipServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/v1beta1.gkehubmembershipserviceclient.html)();
    
      async function callValidateExclusivity() {
        // Construct request
        const request = {
          parent,
          intendedMembership,
        };
    
        // Run request
        const response = await gkehubClient.validateExclusivity(request);
        console.log(response);
      }
    
      callValidateExclusivity();
    
    

### validateExclusivity(request, options, callback)
    
    
    validateExclusivity(request: protos.google.cloud.gkehub.v1beta1.IValidateExclusivityRequest, options: CallOptions, callback: Callback<protos.google.cloud.gkehub.v1beta1.IValidateExclusivityResponse, protos.google.cloud.gkehub.v1beta1.IValidateExclusivityRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IValidateExclusivityRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ivalidateexclusivityrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.gkehub.v1beta1.IValidateExclusivityResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ivalidateexclusivityresponse), [protos.google.cloud.gkehub.v1beta1.IValidateExclusivityRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ivalidateexclusivityrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### validateExclusivity(request, callback)
    
    
    validateExclusivity(request: protos.google.cloud.gkehub.v1beta1.IValidateExclusivityRequest, callback: Callback<protos.google.cloud.gkehub.v1beta1.IValidateExclusivityResponse, protos.google.cloud.gkehub.v1beta1.IValidateExclusivityRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IValidateExclusivityRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ivalidateexclusivityrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.gkehub.v1beta1.IValidateExclusivityResponse](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ivalidateexclusivityresponse), [protos.google.cloud.gkehub.v1beta1.IValidateExclusivityRequest](https://docs.cloud.google.com/nodejs/docs/reference/gke-hub/latest/gke-hub/protos.google.cloud.gkehub.v1beta1.ivalidateexclusivityrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
