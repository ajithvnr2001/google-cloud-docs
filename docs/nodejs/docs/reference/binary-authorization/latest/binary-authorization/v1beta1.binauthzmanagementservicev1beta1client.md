---
url: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/v1beta1.binauthzmanagementservicev1beta1client
title: Class v1beta1.BinauthzManagementServiceV1Beta1Client (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:00.489293+00:00
---

# Class v1beta1.BinauthzManagementServiceV1Beta1Client (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/v1beta1.binauthzmanagementservicev1beta1client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.BinauthzManagementServiceV1Beta1Client (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.5.0  4.4.0  4.2.0  3.7.0  2.5.0  2.2.1  2.1.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.6 

Google Cloud Management Service for Binary Authorization admission policies and attestation authorities.

This API implements a REST model with the following objects:

* * [Attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor) v1beta1

## Package

[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of BinauthzManagementServiceV1Beta1Client.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new BinauthzManagementServiceV1Beta1Client({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### binauthzManagementServiceV1Beta1Stub
    
    
    binauthzManagementServiceV1Beta1Stub?: Promise<{
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

### attestorPath(project, attestor)
    
    
    attestorPath(project: string, attestor: string): string;

Return a fully-qualified attestor resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`attestor` |  `string`   
  
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
  
### createAttestor(request, options)
    
    
    createAttestor(request?: protos.google.cloud.binaryauthorization.v1beta1.ICreateAttestorRequest, options?: CallOptions): Promise<[
            protos.google.cloud.binaryauthorization.v1beta1.IAttestor,
            (protos.google.cloud.binaryauthorization.v1beta1.ICreateAttestorRequest | undefined),
            {} | undefined
        ]>;

Creates an [attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor), and returns a copy of the new [attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor). Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed, ALREADY_EXISTS if the [attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor) already exists.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.icreateattestorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor), ([protos.google.cloud.binaryauthorization.v1beta1.ICreateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.icreateattestorrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of this
       *  attestor google.cloud.binaryauthorization.v1beta1.Attestor.
       */
      // const parent = 'abc123'
      /**
       *  Required. The
       *  attestors google.cloud.binaryauthorization.v1beta1.Attestor  ID.
       */
      // const attestorId = 'abc123'
      /**
       *  Required. The initial
       *  attestor google.cloud.binaryauthorization.v1beta1.Attestor  value. The
       *  service will overwrite the attestor
       *  name google.cloud.binaryauthorization.v1beta1.Attestor.name  field with
       *  the resource name, in the format `projects/* /attestors/*`.
       */
      // const attestor = {}
    
      // Imports the Binaryauthorization library
      const {BinauthzManagementServiceV1Beta1Client} = require('[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const binaryauthorizationClient = new [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/v1beta1.binauthzmanagementservicev1beta1client.html)();
    
      async function callCreateAttestor() {
        // Construct request
        const request = {
          parent,
          attestorId,
          attestor,
        };
    
        // Run request
        const response = await binaryauthorizationClient.createAttestor(request);
        console.log(response);
      }
    
      callCreateAttestor();
    
    

### createAttestor(request, options, callback)
    
    
    createAttestor(request: protos.google.cloud.binaryauthorization.v1beta1.ICreateAttestorRequest, options: CallOptions, callback: Callback<protos.google.cloud.binaryauthorization.v1beta1.IAttestor, protos.google.cloud.binaryauthorization.v1beta1.ICreateAttestorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.icreateattestorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor), [protos.google.cloud.binaryauthorization.v1beta1.ICreateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.icreateattestorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAttestor(request, callback)
    
    
    createAttestor(request: protos.google.cloud.binaryauthorization.v1beta1.ICreateAttestorRequest, callback: Callback<protos.google.cloud.binaryauthorization.v1beta1.IAttestor, protos.google.cloud.binaryauthorization.v1beta1.ICreateAttestorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.icreateattestorrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor), [protos.google.cloud.binaryauthorization.v1beta1.ICreateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.icreateattestorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAttestor(request, options)
    
    
    deleteAttestor(request?: protos.google.cloud.binaryauthorization.v1beta1.IDeleteAttestorRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.binaryauthorization.v1beta1.IDeleteAttestorRequest | undefined),
            {} | undefined
        ]>;

Deletes an [attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor). Returns NOT_FOUND if the [attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor) does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ideleteattestorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.protobuf.iempty), ([protos.google.cloud.binaryauthorization.v1beta1.IDeleteAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ideleteattestorrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the
       *  attestors google.cloud.binaryauthorization.v1beta1.Attestor  to delete,
       *  in the format `projects/* /attestors/*`.
       */
      // const name = 'abc123'
    
      // Imports the Binaryauthorization library
      const {BinauthzManagementServiceV1Beta1Client} = require('[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const binaryauthorizationClient = new [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/v1beta1.binauthzmanagementservicev1beta1client.html)();
    
      async function callDeleteAttestor() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await binaryauthorizationClient.deleteAttestor(request);
        console.log(response);
      }
    
      callDeleteAttestor();
    
    

### deleteAttestor(request, options, callback)
    
    
    deleteAttestor(request: protos.google.cloud.binaryauthorization.v1beta1.IDeleteAttestorRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.binaryauthorization.v1beta1.IDeleteAttestorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ideleteattestorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.protobuf.iempty), [protos.google.cloud.binaryauthorization.v1beta1.IDeleteAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ideleteattestorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAttestor(request, callback)
    
    
    deleteAttestor(request: protos.google.cloud.binaryauthorization.v1beta1.IDeleteAttestorRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.binaryauthorization.v1beta1.IDeleteAttestorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ideleteattestorrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.protobuf.iempty), [protos.google.cloud.binaryauthorization.v1beta1.IDeleteAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ideleteattestorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAttestor(request, options)
    
    
    getAttestor(request?: protos.google.cloud.binaryauthorization.v1beta1.IGetAttestorRequest, options?: CallOptions): Promise<[
            protos.google.cloud.binaryauthorization.v1beta1.IAttestor,
            (protos.google.cloud.binaryauthorization.v1beta1.IGetAttestorRequest | undefined),
            {} | undefined
        ]>;

Gets an [attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor). Returns NOT_FOUND if the [attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor) does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetattestorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor), ([protos.google.cloud.binaryauthorization.v1beta1.IGetAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetattestorrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the
       *  attestor google.cloud.binaryauthorization.v1beta1.Attestor  to retrieve,
       *  in the format `projects/* /attestors/*`.
       */
      // const name = 'abc123'
    
      // Imports the Binaryauthorization library
      const {BinauthzManagementServiceV1Beta1Client} = require('[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const binaryauthorizationClient = new [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/v1beta1.binauthzmanagementservicev1beta1client.html)();
    
      async function callGetAttestor() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await binaryauthorizationClient.getAttestor(request);
        console.log(response);
      }
    
      callGetAttestor();
    
    

### getAttestor(request, options, callback)
    
    
    getAttestor(request: protos.google.cloud.binaryauthorization.v1beta1.IGetAttestorRequest, options: CallOptions, callback: Callback<protos.google.cloud.binaryauthorization.v1beta1.IAttestor, protos.google.cloud.binaryauthorization.v1beta1.IGetAttestorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetattestorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor), [protos.google.cloud.binaryauthorization.v1beta1.IGetAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetattestorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAttestor(request, callback)
    
    
    getAttestor(request: protos.google.cloud.binaryauthorization.v1beta1.IGetAttestorRequest, callback: Callback<protos.google.cloud.binaryauthorization.v1beta1.IAttestor, protos.google.cloud.binaryauthorization.v1beta1.IGetAttestorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetattestorrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor), [protos.google.cloud.binaryauthorization.v1beta1.IGetAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetattestorrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getPolicy(request, options)
    
    
    getPolicy(request?: protos.google.cloud.binaryauthorization.v1beta1.IGetPolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.binaryauthorization.v1beta1.IPolicy,
            (protos.google.cloud.binaryauthorization.v1beta1.IGetPolicyRequest | undefined),
            {} | undefined
        ]>;

A specifies the [attestors](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor) that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy.

Gets the for this project. Returns a default if the project does not have one.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetpolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.binaryauthorization.v1beta1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ipolicy), ([protos.google.cloud.binaryauthorization.v1beta1.IGetPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetpolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the
       *  policy google.cloud.binaryauthorization.v1beta1.Policy  to retrieve, in
       *  the format `projects/* /policy`.
       */
      // const name = 'abc123'
    
      // Imports the Binaryauthorization library
      const {BinauthzManagementServiceV1Beta1Client} = require('[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const binaryauthorizationClient = new [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/v1beta1.binauthzmanagementservicev1beta1client.html)();
    
      async function callGetPolicy() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await binaryauthorizationClient.getPolicy(request);
        console.log(response);
      }
    
      callGetPolicy();
    
    

### getPolicy(request, options, callback)
    
    
    getPolicy(request: protos.google.cloud.binaryauthorization.v1beta1.IGetPolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.binaryauthorization.v1beta1.IPolicy, protos.google.cloud.binaryauthorization.v1beta1.IGetPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetpolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.binaryauthorization.v1beta1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ipolicy), [protos.google.cloud.binaryauthorization.v1beta1.IGetPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetpolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPolicy(request, callback)
    
    
    getPolicy(request: protos.google.cloud.binaryauthorization.v1beta1.IGetPolicyRequest, callback: Callback<protos.google.cloud.binaryauthorization.v1beta1.IPolicy, protos.google.cloud.binaryauthorization.v1beta1.IGetPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetpolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.binaryauthorization.v1beta1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ipolicy), [protos.google.cloud.binaryauthorization.v1beta1.IGetPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.igetpolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listAttestors(request, options)
    
    
    listAttestors(request?: protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.binaryauthorization.v1beta1.IAttestor[],
            protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest | null,
            protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsResponse
        ]>;

Lists [attestors](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor). Returns INVALID_ARGUMENT if the project does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAttestorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor)[], [protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsrequest) | null, [protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listAttestorsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listAttestors(request, options, callback)
    
    
    listAttestors(request: protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest, protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsResponse | null | undefined, protos.google.cloud.binaryauthorization.v1beta1.IAttestor>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAttestorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsrequest), [protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsresponse) | null | undefined, [protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAttestors(request, callback)
    
    
    listAttestors(request: protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest, callback: PaginationCallback<protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest, protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsResponse | null | undefined, protos.google.cloud.binaryauthorization.v1beta1.IAttestor>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAttestorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsrequest), [protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsresponse) | null | undefined, [protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAttestorsAsync(request, options)
    
    
    listAttestorsAsync(request?: protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.binaryauthorization.v1beta1.IAttestor>;

Equivalent to `listAttestors`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAttestorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the project associated with the
       *  attestors google.cloud.binaryauthorization.v1beta1.Attestor, in the
       *  format `projects/*`.
       */
      // const parent = 'abc123'
      /**
       *  Requested page size. The server may return fewer results than requested. If
       *  unspecified, the server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  A token identifying a page of results the server should return. Typically,
       *  this is the value of
       *  ListAttestorsResponse.next_page_token google.cloud.binaryauthorization.v1beta1.ListAttestorsResponse.next_page_token 
       *  returned from the previous call to the `ListAttestors` method.
       */
      // const pageToken = 'abc123'
    
      // Imports the Binaryauthorization library
      const {BinauthzManagementServiceV1Beta1Client} = require('[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const binaryauthorizationClient = new [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/v1beta1.binauthzmanagementservicev1beta1client.html)();
    
      async function callListAttestors() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = binaryauthorizationClient.listAttestorsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListAttestors();
    
    

### listAttestorsStream(request, options)
    
    
    listAttestorsStream(request?: protos.google.cloud.binaryauthorization.v1beta1.IListAttestorsRequest, options?: CallOptions): Transform;

Equivalent to `listAttestors`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAttestorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ilistattestorsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listAttestorsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### locationPolicyPath(location)
    
    
    locationPolicyPath(location: string): string;

Return a fully-qualified locationPolicy resource name string.

**Parameter**  
---  
**Name** | **Description**  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### matchAttestorFromAttestorName(attestorName)
    
    
    matchAttestorFromAttestorName(attestorName: string): string | number;

Parse the attestor from Attestor resource.

**Parameter**  
---  
**Name** | **Description**  
`attestorName` |  `string`   
A fully-qualified path representing Attestor resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the attestor.  
  
### matchLocationFromLocationPolicyName(locationPolicyName)
    
    
    matchLocationFromLocationPolicyName(locationPolicyName: string): string | number;

Parse the location from LocationPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`locationPolicyName` |  `string`   
A fully-qualified path representing location_policy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchProjectFromAttestorName(attestorName)
    
    
    matchProjectFromAttestorName(attestorName: string): string | number;

Parse the project from Attestor resource.

**Parameter**  
---  
**Name** | **Description**  
`attestorName` |  `string`   
A fully-qualified path representing Attestor resource.  
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
  
### matchProjectFromProjectPolicyName(projectPolicyName)
    
    
    matchProjectFromProjectPolicyName(projectPolicyName: string): string | number;

Parse the project from ProjectPolicy resource.

**Parameter**  
---  
**Name** | **Description**  
`projectPolicyName` |  `string`   
A fully-qualified path representing project_policy resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
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
  
### projectPolicyPath(project)
    
    
    projectPolicyPath(project: string): string;

Return a fully-qualified projectPolicy resource name string.

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
  
### updateAttestor(request, options)
    
    
    updateAttestor(request?: protos.google.cloud.binaryauthorization.v1beta1.IUpdateAttestorRequest, options?: CallOptions): Promise<[
            protos.google.cloud.binaryauthorization.v1beta1.IAttestor,
            (protos.google.cloud.binaryauthorization.v1beta1.IUpdateAttestorRequest | undefined),
            {} | undefined
        ]>;

Updates an [attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor). Returns NOT_FOUND if the [attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor) does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdateattestorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor), ([protos.google.cloud.binaryauthorization.v1beta1.IUpdateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdateattestorrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Attestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.attestor). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The updated
       *  attestor google.cloud.binaryauthorization.v1beta1.Attestor  value. The
       *  service will overwrite the attestor
       *  name google.cloud.binaryauthorization.v1beta1.Attestor.name  field with
       *  the resource name in the request URL, in the format
       *  `projects/* /attestors/*`.
       */
      // const attestor = {}
    
      // Imports the Binaryauthorization library
      const {BinauthzManagementServiceV1Beta1Client} = require('[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const binaryauthorizationClient = new [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/v1beta1.binauthzmanagementservicev1beta1client.html)();
    
      async function callUpdateAttestor() {
        // Construct request
        const request = {
          attestor,
        };
    
        // Run request
        const response = await binaryauthorizationClient.updateAttestor(request);
        console.log(response);
      }
    
      callUpdateAttestor();
    
    

### updateAttestor(request, options, callback)
    
    
    updateAttestor(request: protos.google.cloud.binaryauthorization.v1beta1.IUpdateAttestorRequest, options: CallOptions, callback: Callback<protos.google.cloud.binaryauthorization.v1beta1.IAttestor, protos.google.cloud.binaryauthorization.v1beta1.IUpdateAttestorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdateattestorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor), [protos.google.cloud.binaryauthorization.v1beta1.IUpdateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdateattestorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAttestor(request, callback)
    
    
    updateAttestor(request: protos.google.cloud.binaryauthorization.v1beta1.IUpdateAttestorRequest, callback: Callback<protos.google.cloud.binaryauthorization.v1beta1.IAttestor, protos.google.cloud.binaryauthorization.v1beta1.IUpdateAttestorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdateattestorrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.binaryauthorization.v1beta1.IAttestor](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iattestor), [protos.google.cloud.binaryauthorization.v1beta1.IUpdateAttestorRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdateattestorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePolicy(request, options)
    
    
    updatePolicy(request?: protos.google.cloud.binaryauthorization.v1beta1.IUpdatePolicyRequest, options?: CallOptions): Promise<[
            protos.google.cloud.binaryauthorization.v1beta1.IPolicy,
            (protos.google.cloud.binaryauthorization.v1beta1.IUpdatePolicyRequest | undefined),
            {} | undefined
        ]>;

Creates or updates a project's , and returns a copy of the new . A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns NOT_FOUND if the project does not exist, INVALID_ARGUMENT if the request is malformed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdatepolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.binaryauthorization.v1beta1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ipolicy), ([protos.google.cloud.binaryauthorization.v1beta1.IUpdatePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdatepolicyrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. A new or updated
       *  policy google.cloud.binaryauthorization.v1beta1.Policy  value. The
       *  service will overwrite the policy
       *  name google.cloud.binaryauthorization.v1beta1.Policy.name  field with the
       *  resource name in the request URL, in the format `projects/* /policy`.
       */
      // const policy = {}
    
      // Imports the Binaryauthorization library
      const {BinauthzManagementServiceV1Beta1Client} = require('[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const binaryauthorizationClient = new [BinauthzManagementServiceV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/v1beta1.binauthzmanagementservicev1beta1client.html)();
    
      async function callUpdatePolicy() {
        // Construct request
        const request = {
          policy,
        };
    
        // Run request
        const response = await binaryauthorizationClient.updatePolicy(request);
        console.log(response);
      }
    
      callUpdatePolicy();
    
    

### updatePolicy(request, options, callback)
    
    
    updatePolicy(request: protos.google.cloud.binaryauthorization.v1beta1.IUpdatePolicyRequest, options: CallOptions, callback: Callback<protos.google.cloud.binaryauthorization.v1beta1.IPolicy, protos.google.cloud.binaryauthorization.v1beta1.IUpdatePolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdatepolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.binaryauthorization.v1beta1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ipolicy), [protos.google.cloud.binaryauthorization.v1beta1.IUpdatePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdatepolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePolicy(request, callback)
    
    
    updatePolicy(request: protos.google.cloud.binaryauthorization.v1beta1.IUpdatePolicyRequest, callback: Callback<protos.google.cloud.binaryauthorization.v1beta1.IPolicy, protos.google.cloud.binaryauthorization.v1beta1.IUpdatePolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdatepolicyrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.binaryauthorization.v1beta1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.ipolicy), [protos.google.cloud.binaryauthorization.v1beta1.IUpdatePolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1beta1.iupdatepolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
