---
url: https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasrolloutsclient
title: Class v1beta1.SaasRolloutsClient (0.6.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:40.723235+00:00
---

# Class v1beta1.SaasRolloutsClient (0.6.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasrolloutsclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.SaasRolloutsClient (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.4.0 

Manages the rollout of SaaS services. v1beta1

## Package

[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of SaasRolloutsClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new SaasRolloutsClient({fallback: true}, gax); ```  
  
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

### locationsClient
    
    
    locationsClient: LocationsClient;

### pathTemplates
    
    
    pathTemplates: {
            [name: string]: gax.PathTemplate;
        };

### port
    
    
    static get port(): number;

The port for this API service.

### saasRolloutsStub
    
    
    saasRolloutsStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### createRollout(request, options)
    
    
    createRollout(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutRequest | undefined),
            {} | undefined
        ]>;

Create a new rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the rollout.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID value for the new rollout.
       */
      // const rolloutId = 'abc123'
      /**
       *  Required. The desired state for the rollout.
       */
      // const rollout = {}
      /**
       *  If "validate_only" is set to true, the service will try to validate
       *  that this request would succeed, but will not actually make changes.
       */
      // const validateOnly = true
      /**
       *  An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Saasservicemgmt library
      const {SaasRolloutsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasRolloutsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callCreateRollout() {
        // Construct request
        const request = {
          parent,
          rolloutId,
          rollout,
        };
    
        // Run request
        const response = await saasservicemgmtClient.createRollout(request);
        console.log(response);
      }
    
      callCreateRollout();
    
    

### createRollout(request, options, callback)
    
    
    createRollout(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRollout(request, callback)
    
    
    createRollout(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRolloutKind(request, options)
    
    
    createRolloutKind(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutKindRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutKindRequest | undefined),
            {} | undefined
        ]>;

Create a new rollout kind.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutkindrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutkindrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the rollout kind.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID value for the new rollout kind.
       */
      // const rolloutKindId = 'abc123'
      /**
       *  Required. The desired state for the rollout kind.
       */
      // const rolloutKind = {}
      /**
       *  If "validate_only" is set to true, the service will try to validate
       *  that this request would succeed, but will not actually make changes.
       */
      // const validateOnly = true
      /**
       *  An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Saasservicemgmt library
      const {SaasRolloutsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasRolloutsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callCreateRolloutKind() {
        // Construct request
        const request = {
          parent,
          rolloutKindId,
          rolloutKind,
        };
    
        // Run request
        const response = await saasservicemgmtClient.createRolloutKind(request);
        console.log(response);
      }
    
      callCreateRolloutKind();
    
    

### createRolloutKind(request, options, callback)
    
    
    createRolloutKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutKindRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutkindrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRolloutKind(request, callback)
    
    
    createRolloutKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutKindRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutkindrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreaterolloutkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRollout(request, options)
    
    
    deleteRollout(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutRequest | undefined),
            {} | undefined
        ]>;

Delete a single rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the resource within a service.
       */
      // const name = 'abc123'
      /**
       *  The etag known to the client for the expected state of the rollout. This is
       *  used with state-changing methods to prevent accidental overwrites when
       *  multiple user agents might be acting in parallel on the same resource.
       *  An etag wildcard provide optimistic concurrency based on the expected
       *  existence of the rollout. The Any wildcard (`*`) requires that the resource
       *  must already exists, and the Not Any wildcard (`!*`) requires that it must
       *  not.
       */
      // const etag = 'abc123'
      /**
       *  If "validate_only" is set to true, the service will try to validate
       *  that this request would succeed, but will not actually make changes.
       */
      // const validateOnly = true
      /**
       *  An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Saasservicemgmt library
      const {SaasRolloutsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasRolloutsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callDeleteRollout() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.deleteRollout(request);
        console.log(response);
      }
    
      callDeleteRollout();
    
    

### deleteRollout(request, options, callback)
    
    
    deleteRollout(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRollout(request, callback)
    
    
    deleteRollout(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRolloutKind(request, options)
    
    
    deleteRolloutKind(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutKindRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutKindRequest | undefined),
            {} | undefined
        ]>;

Delete a single rollout kind.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutkindrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutkindrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the resource within a service.
       */
      // const name = 'abc123'
      /**
       *  The etag known to the client for the expected state of the rollout kind.
       *  This is used with state-changing methods to prevent accidental overwrites
       *  when multiple user agents might be acting in parallel on the same resource.
       *  An etag wildcard provide optimistic concurrency based on the expected
       *  existence of the rollout kind. The Any wildcard (`*`) requires that the
       *  resource must already exists, and the Not Any wildcard (`!*`) requires that
       *  it must not.
       */
      // const etag = 'abc123'
      /**
       *  If "validate_only" is set to true, the service will try to validate
       *  that this request would succeed, but will not actually make changes.
       */
      // const validateOnly = true
      /**
       *  An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
    
      // Imports the Saasservicemgmt library
      const {SaasRolloutsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasRolloutsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callDeleteRolloutKind() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.deleteRolloutKind(request);
        console.log(response);
      }
    
      callDeleteRolloutKind();
    
    

### deleteRolloutKind(request, options, callback)
    
    
    deleteRolloutKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutKindRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutkindrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRolloutKind(request, callback)
    
    
    deleteRolloutKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutKindRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutkindrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleterolloutkindrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getRollout(request, options)
    
    
    getRollout(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutRequest | undefined),
            {} | undefined
        ]>;

Retrieve a single rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the resource within a service.
       */
      // const name = 'abc123'
    
      // Imports the Saasservicemgmt library
      const {SaasRolloutsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasRolloutsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callGetRollout() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.getRollout(request);
        console.log(response);
      }
    
      callGetRollout();
    
    

### getRollout(request, options, callback)
    
    
    getRollout(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRollout(request, callback)
    
    
    getRollout(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRolloutKind(request, options)
    
    
    getRolloutKind(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutKindRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutKindRequest | undefined),
            {} | undefined
        ]>;

Retrieve a single rollout kind.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutkindrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutkindrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the resource within a service.
       */
      // const name = 'abc123'
    
      // Imports the Saasservicemgmt library
      const {SaasRolloutsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasRolloutsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callGetRolloutKind() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.getRolloutKind(request);
        console.log(response);
      }
    
      callGetRolloutKind();
    
    

### getRolloutKind(request, options, callback)
    
    
    getRolloutKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutKindRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutkindrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRolloutKind(request, callback)
    
    
    getRolloutKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutKindRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutkindrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetrolloutkindrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### listRolloutKinds(request, options)
    
    
    listRolloutKinds(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind[],
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest | null,
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsResponse
        ]>;

Retrieve a collection of rollout kinds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind)[], [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsrequest) | null, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listRolloutKindsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listRolloutKinds(request, options, callback)
    
    
    listRolloutKinds(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRolloutKinds(request, callback)
    
    
    listRolloutKinds(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRolloutKindsAsync(request, options)
    
    
    listRolloutKindsAsync(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind>;

Equivalent to `listRolloutKinds`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the rollout kind.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of rollout kinds to send per page.
       */
      // const pageSize = 1234
      /**
       *  The page token: If the next_page_token from a previous response
       *  is provided, this request will send the subsequent page.
       */
      // const pageToken = 'abc123'
      /**
       *  Filter the list as specified in https://google.aip.dev/160.
       */
      // const filter = 'abc123'
      /**
       *  Order results as specified in https://google.aip.dev/132.
       */
      // const orderBy = 'abc123'
    
      // Imports the Saasservicemgmt library
      const {SaasRolloutsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasRolloutsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callListRolloutKinds() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = saasservicemgmtClient.[listRolloutKindsAsync](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasrolloutsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListRolloutKinds();
    
    

### listRolloutKindsStream(request, options)
    
    
    listRolloutKindsStream(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutKindsRequest, options?: CallOptions): Transform;

Equivalent to `listRolloutKinds`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutkindsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listRolloutKindsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listRollouts(request, options)
    
    
    listRollouts(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout[],
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest | null,
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsResponse
        ]>;

Retrieve a collection of rollouts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout)[], [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsrequest) | null, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listRolloutsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listRollouts(request, options, callback)
    
    
    listRollouts(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRollouts(request, callback)
    
    
    listRollouts(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRolloutsAsync(request, options)
    
    
    listRolloutsAsync(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout>;

Equivalent to `listRollouts`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the rollout.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of rollouts to send per page.
       */
      // const pageSize = 1234
      /**
       *  The page token: If the next_page_token from a previous response
       *  is provided, this request will send the subsequent page.
       */
      // const pageToken = 'abc123'
      /**
       *  Filter the list as specified in https://google.aip.dev/160.
       */
      // const filter = 'abc123'
      /**
       *  Order results as specified in https://google.aip.dev/132.
       */
      // const orderBy = 'abc123'
    
      // Imports the Saasservicemgmt library
      const {SaasRolloutsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasRolloutsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callListRollouts() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = saasservicemgmtClient.[listRolloutsAsync](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasrolloutsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListRollouts();
    
    

### listRolloutsStream(request, options)
    
    
    listRolloutsStream(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListRolloutsRequest, options?: CallOptions): Transform;

Equivalent to `listRollouts`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRolloutsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistrolloutsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listRolloutsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchLocationFromReleaseName(releaseName)
    
    
    matchLocationFromReleaseName(releaseName: string): string | number;

Parse the location from Release resource.

**Parameter**  
---  
**Name** | **Description**  
`releaseName` |  `string`   
A fully-qualified path representing Release resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRolloutKindName(rolloutKindName)
    
    
    matchLocationFromRolloutKindName(rolloutKindName: string): string | number;

Parse the location from RolloutKind resource.

**Parameter**  
---  
**Name** | **Description**  
`rolloutKindName` |  `string`   
A fully-qualified path representing RolloutKind resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromRolloutName(rolloutName)
    
    
    matchLocationFromRolloutName(rolloutName: string): string | number;

Parse the location from Rollout resource.

**Parameter**  
---  
**Name** | **Description**  
`rolloutName` |  `string`   
A fully-qualified path representing Rollout resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSaasName(saasName)
    
    
    matchLocationFromSaasName(saasName: string): string | number;

Parse the location from Saas resource.

**Parameter**  
---  
**Name** | **Description**  
`saasName` |  `string`   
A fully-qualified path representing Saas resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromTenantName(tenantName)
    
    
    matchLocationFromTenantName(tenantName: string): string | number;

Parse the location from Tenant resource.

**Parameter**  
---  
**Name** | **Description**  
`tenantName` |  `string`   
A fully-qualified path representing Tenant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromUnitKindName(unitKindName)
    
    
    matchLocationFromUnitKindName(unitKindName: string): string | number;

Parse the location from UnitKind resource.

**Parameter**  
---  
**Name** | **Description**  
`unitKindName` |  `string`   
A fully-qualified path representing UnitKind resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromUnitName(unitName)
    
    
    matchLocationFromUnitName(unitName: string): string | number;

Parse the location from Unit resource.

**Parameter**  
---  
**Name** | **Description**  
`unitName` |  `string`   
A fully-qualified path representing Unit resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromUnitOperationName(unitOperationName)
    
    
    matchLocationFromUnitOperationName(unitOperationName: string): string | number;

Parse the location from UnitOperation resource.

**Parameter**  
---  
**Name** | **Description**  
`unitOperationName` |  `string`   
A fully-qualified path representing UnitOperation resource.  
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
  
### matchProjectFromReleaseName(releaseName)
    
    
    matchProjectFromReleaseName(releaseName: string): string | number;

Parse the project from Release resource.

**Parameter**  
---  
**Name** | **Description**  
`releaseName` |  `string`   
A fully-qualified path representing Release resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRolloutKindName(rolloutKindName)
    
    
    matchProjectFromRolloutKindName(rolloutKindName: string): string | number;

Parse the project from RolloutKind resource.

**Parameter**  
---  
**Name** | **Description**  
`rolloutKindName` |  `string`   
A fully-qualified path representing RolloutKind resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRolloutName(rolloutName)
    
    
    matchProjectFromRolloutName(rolloutName: string): string | number;

Parse the project from Rollout resource.

**Parameter**  
---  
**Name** | **Description**  
`rolloutName` |  `string`   
A fully-qualified path representing Rollout resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSaasName(saasName)
    
    
    matchProjectFromSaasName(saasName: string): string | number;

Parse the project from Saas resource.

**Parameter**  
---  
**Name** | **Description**  
`saasName` |  `string`   
A fully-qualified path representing Saas resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromTenantName(tenantName)
    
    
    matchProjectFromTenantName(tenantName: string): string | number;

Parse the project from Tenant resource.

**Parameter**  
---  
**Name** | **Description**  
`tenantName` |  `string`   
A fully-qualified path representing Tenant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromUnitKindName(unitKindName)
    
    
    matchProjectFromUnitKindName(unitKindName: string): string | number;

Parse the project from UnitKind resource.

**Parameter**  
---  
**Name** | **Description**  
`unitKindName` |  `string`   
A fully-qualified path representing UnitKind resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromUnitName(unitName)
    
    
    matchProjectFromUnitName(unitName: string): string | number;

Parse the project from Unit resource.

**Parameter**  
---  
**Name** | **Description**  
`unitName` |  `string`   
A fully-qualified path representing Unit resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromUnitOperationName(unitOperationName)
    
    
    matchProjectFromUnitOperationName(unitOperationName: string): string | number;

Parse the project from UnitOperation resource.

**Parameter**  
---  
**Name** | **Description**  
`unitOperationName` |  `string`   
A fully-qualified path representing UnitOperation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchReleaseFromReleaseName(releaseName)
    
    
    matchReleaseFromReleaseName(releaseName: string): string | number;

Parse the release from Release resource.

**Parameter**  
---  
**Name** | **Description**  
`releaseName` |  `string`   
A fully-qualified path representing Release resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the release.  
  
### matchRolloutIdFromRolloutName(rolloutName)
    
    
    matchRolloutIdFromRolloutName(rolloutName: string): string | number;

Parse the rollout_id from Rollout resource.

**Parameter**  
---  
**Name** | **Description**  
`rolloutName` |  `string`   
A fully-qualified path representing Rollout resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rollout_id.  
  
### matchRolloutKindIdFromRolloutKindName(rolloutKindName)
    
    
    matchRolloutKindIdFromRolloutKindName(rolloutKindName: string): string | number;

Parse the rollout_kind_id from RolloutKind resource.

**Parameter**  
---  
**Name** | **Description**  
`rolloutKindName` |  `string`   
A fully-qualified path representing RolloutKind resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the rollout_kind_id.  
  
### matchSaasFromSaasName(saasName)
    
    
    matchSaasFromSaasName(saasName: string): string | number;

Parse the saas from Saas resource.

**Parameter**  
---  
**Name** | **Description**  
`saasName` |  `string`   
A fully-qualified path representing Saas resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the saas.  
  
### matchTenantFromTenantName(tenantName)
    
    
    matchTenantFromTenantName(tenantName: string): string | number;

Parse the tenant from Tenant resource.

**Parameter**  
---  
**Name** | **Description**  
`tenantName` |  `string`   
A fully-qualified path representing Tenant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tenant.  
  
### matchUnitFromUnitName(unitName)
    
    
    matchUnitFromUnitName(unitName: string): string | number;

Parse the unit from Unit resource.

**Parameter**  
---  
**Name** | **Description**  
`unitName` |  `string`   
A fully-qualified path representing Unit resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the unit.  
  
### matchUnitKindFromUnitKindName(unitKindName)
    
    
    matchUnitKindFromUnitKindName(unitKindName: string): string | number;

Parse the unitKind from UnitKind resource.

**Parameter**  
---  
**Name** | **Description**  
`unitKindName` |  `string`   
A fully-qualified path representing UnitKind resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the unitKind.  
  
### matchUnitOperationFromUnitOperationName(unitOperationName)
    
    
    matchUnitOperationFromUnitOperationName(unitOperationName: string): string | number;

Parse the unitOperation from UnitOperation resource.

**Parameter**  
---  
**Name** | **Description**  
`unitOperationName` |  `string`   
A fully-qualified path representing UnitOperation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the unitOperation.  
  
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
  
### releasePath(project, location, release)
    
    
    releasePath(project: string, location: string, release: string): string;

Return a fully-qualified release resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`release` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### rolloutKindPath(project, location, rolloutKindId)
    
    
    rolloutKindPath(project: string, location: string, rolloutKindId: string): string;

Return a fully-qualified rolloutKind resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`rolloutKindId` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### rolloutPath(project, location, rolloutId)
    
    
    rolloutPath(project: string, location: string, rolloutId: string): string;

Return a fully-qualified rollout resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`rolloutId` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### saasPath(project, location, saas)
    
    
    saasPath(project: string, location: string, saas: string): string;

Return a fully-qualified saas resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`saas` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tenantPath(project, location, tenant)
    
    
    tenantPath(project: string, location: string, tenant: string): string;

Return a fully-qualified tenant resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tenant` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### unitKindPath(project, location, unitKind)
    
    
    unitKindPath(project: string, location: string, unitKind: string): string;

Return a fully-qualified unitKind resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`unitKind` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### unitOperationPath(project, location, unitOperation)
    
    
    unitOperationPath(project: string, location: string, unitOperation: string): string;

Return a fully-qualified unitOperation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`unitOperation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### unitPath(project, location, unit)
    
    
    unitPath(project: string, location: string, unit: string): string;

Return a fully-qualified unit resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`unit` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateRollout(request, options)
    
    
    updateRollout(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutRequest | undefined),
            {} | undefined
        ]>;

Update a single rollout.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired state for the rollout.
       */
      // const rollout = {}
      /**
       *  If "validate_only" is set to true, the service will try to validate
       *  that this request would succeed, but will not actually make changes.
       */
      // const validateOnly = true
      /**
       *  An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Field mask is used to specify the fields to be overwritten in the
       *  Rollout resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask.
       *  If the user does not provide a mask then all fields in the
       *  Rollout will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Saasservicemgmt library
      const {SaasRolloutsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasRolloutsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callUpdateRollout() {
        // Construct request
        const request = {
          rollout,
        };
    
        // Run request
        const response = await saasservicemgmtClient.updateRollout(request);
        console.log(response);
      }
    
      callUpdateRollout();
    
    

### updateRollout(request, options, callback)
    
    
    updateRollout(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRollout(request, callback)
    
    
    updateRollout(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRollout](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irollout), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRolloutKind(request, options)
    
    
    updateRolloutKind(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutKindRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutKindRequest | undefined),
            {} | undefined
        ]>;

Update a single rollout kind.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutkindrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutkindrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired state for the rollout kind.
       */
      // const rolloutKind = {}
      /**
       *  If "validate_only" is set to true, the service will try to validate
       *  that this request would succeed, but will not actually make changes.
       */
      // const validateOnly = true
      /**
       *  An optional request ID to identify requests. Specify a unique request ID
       *  so that if you must retry your request, the server will know to ignore
       *  the request if it has already been completed. The server will guarantee
       *  that for at least 60 minutes since the first request.
       *  For example, consider a situation where you make an initial request and the
       *  request times out. If you make the request again with the same request
       *  ID, the server can check if original operation with the same request ID
       *  was received, and if so, will ignore the second request. This prevents
       *  clients from accidentally creating duplicate commitments.
       *  The request ID must be a valid UUID with the exception that zero UUID is
       *  not supported (00000000-0000-0000-0000-000000000000).
       */
      // const requestId = 'abc123'
      /**
       *  Field mask is used to specify the fields to be overwritten in the
       *  RolloutKind resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask.
       *  If the user does not provide a mask then all fields in the
       *  RolloutKind will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Saasservicemgmt library
      const {SaasRolloutsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasRolloutsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callUpdateRolloutKind() {
        // Construct request
        const request = {
          rolloutKind,
        };
    
        // Run request
        const response = await saasservicemgmtClient.updateRolloutKind(request);
        console.log(response);
      }
    
      callUpdateRolloutKind();
    
    

### updateRolloutKind(request, options, callback)
    
    
    updateRolloutKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutKindRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutkindrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRolloutKind(request, callback)
    
    
    updateRolloutKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutKindRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutkindrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRolloutKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irolloutkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateRolloutKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdaterolloutkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
