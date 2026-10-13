---
url: https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasdeploymentsclient
title: Class v1beta1.SaasDeploymentsClient (0.6.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:18:13.108227+00:00
---

# Class v1beta1.SaasDeploymentsClient (0.6.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasdeploymentsclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.SaasDeploymentsClient (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.4.0 

Manages the deployment of SaaS services. v1beta1

## Package

[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of SaasDeploymentsClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new SaasDeploymentsClient({fallback: true}, gax); ```  
  
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

### saasDeploymentsStub
    
    
    saasDeploymentsStub?: Promise<{
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
  
### createRelease(request, options)
    
    
    createRelease(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateReleaseRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateReleaseRequest | undefined),
            {} | undefined
        ]>;

Create a new release.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatereleaserequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatereleaserequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the release.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID value for the new release.
       */
      // const releaseId = 'abc123'
      /**
       *  Required. The desired state for the release.
       */
      // const release = {}
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callCreateRelease() {
        // Construct request
        const request = {
          parent,
          releaseId,
          release,
        };
    
        // Run request
        const response = await saasservicemgmtClient.createRelease(request);
        console.log(response);
      }
    
      callCreateRelease();
    
    

### createRelease(request, options, callback)
    
    
    createRelease(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateReleaseRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateReleaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatereleaserequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatereleaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRelease(request, callback)
    
    
    createRelease(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateReleaseRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateReleaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatereleaserequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatereleaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSaas(request, options)
    
    
    createSaas(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateSaasRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateSaasRequest | undefined),
            {} | undefined
        ]>;

Create a new saas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatesaasrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatesaasrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the saas.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID value for the new saas.
       */
      // const saasId = 'abc123'
      /**
       *  Required. The desired state for the saas.
       */
      // const saas = {}
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callCreateSaas() {
        // Construct request
        const request = {
          parent,
          saasId,
          saas,
        };
    
        // Run request
        const response = await saasservicemgmtClient.createSaas(request);
        console.log(response);
      }
    
      callCreateSaas();
    
    

### createSaas(request, options, callback)
    
    
    createSaas(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateSaasRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateSaasRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatesaasrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatesaasrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSaas(request, callback)
    
    
    createSaas(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateSaasRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateSaasRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatesaasrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatesaasrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTenant(request, options)
    
    
    createTenant(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateTenantRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateTenantRequest | undefined),
            {} | undefined
        ]>;

Create a new tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatetenantrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatetenantrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Tenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.tenant). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the tenant.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID value for the new tenant.
       */
      // const tenantId = 'abc123'
      /**
       *  Required. The desired state for the tenant.
       */
      // const tenant = {}
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callCreateTenant() {
        // Construct request
        const request = {
          parent,
          tenantId,
          tenant,
        };
    
        // Run request
        const response = await saasservicemgmtClient.createTenant(request);
        console.log(response);
      }
    
      callCreateTenant();
    
    

### createTenant(request, options, callback)
    
    
    createTenant(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateTenantRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateTenantRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatetenantrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatetenantrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTenant(request, callback)
    
    
    createTenant(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateTenantRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateTenantRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatetenantrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreatetenantrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUnit(request, options)
    
    
    createUnit(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitRequest | undefined),
            {} | undefined
        ]>;

Create a new unit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the unit.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID value for the new unit.
       */
      // const unitId = 'abc123'
      /**
       *  Required. The desired state for the unit.
       */
      // const unit = {}
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callCreateUnit() {
        // Construct request
        const request = {
          parent,
          unitId,
          unit,
        };
    
        // Run request
        const response = await saasservicemgmtClient.createUnit(request);
        console.log(response);
      }
    
      callCreateUnit();
    
    

### createUnit(request, options, callback)
    
    
    createUnit(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUnit(request, callback)
    
    
    createUnit(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUnitKind(request, options)
    
    
    createUnitKind(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest | undefined),
            {} | undefined
        ]>;

Create a new unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [UnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.unitkind). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the unit kind.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID value for the new unit kind.
       */
      // const unitKindId = 'abc123'
      /**
       *  Required. The desired state for the unit kind.
       */
      // const unitKind = {}
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callCreateUnitKind() {
        // Construct request
        const request = {
          parent,
          unitKindId,
          unitKind,
        };
    
        // Run request
        const response = await saasservicemgmtClient.createUnitKind(request);
        console.log(response);
      }
    
      callCreateUnitKind();
    
    

### createUnitKind(request, options, callback)
    
    
    createUnitKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUnitKind(request, callback)
    
    
    createUnitKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUnitOperation(request, options)
    
    
    createUnitOperation(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitOperationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitOperationRequest | undefined),
            {} | undefined
        ]>;

Create a new unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitoperationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitoperationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the unit operation.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID value for the new unit operation.
       */
      // const unitOperationId = 'abc123'
      /**
       *  Required. The desired state for the unit operation.
       */
      // const unitOperation = {}
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callCreateUnitOperation() {
        // Construct request
        const request = {
          parent,
          unitOperationId,
          unitOperation,
        };
    
        // Run request
        const response = await saasservicemgmtClient.createUnitOperation(request);
        console.log(response);
      }
    
      callCreateUnitOperation();
    
    

### createUnitOperation(request, options, callback)
    
    
    createUnitOperation(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitOperationRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitoperationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitoperationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createUnitOperation(request, callback)
    
    
    createUnitOperation(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitOperationRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitoperationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ICreateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.icreateunitoperationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRelease(request, options)
    
    
    deleteRelease(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteReleaseRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteReleaseRequest | undefined),
            {} | undefined
        ]>;

Delete a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletereleaserequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletereleaserequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  The etag known to the client for the expected state of the release. This is
       *  used with state-changing methods to prevent accidental overwrites when
       *  multiple user agents might be acting in parallel on the same resource.
       *  An etag wildcard provide optimistic concurrency based on the expected
       *  existence of the release. The Any wildcard (`*`) requires that the resource
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callDeleteRelease() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.deleteRelease(request);
        console.log(response);
      }
    
      callDeleteRelease();
    
    

### deleteRelease(request, options, callback)
    
    
    deleteRelease(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteReleaseRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteReleaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletereleaserequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletereleaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRelease(request, callback)
    
    
    deleteRelease(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteReleaseRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteReleaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletereleaserequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletereleaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSaas(request, options)
    
    
    deleteSaas(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteSaasRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteSaasRequest | undefined),
            {} | undefined
        ]>;

Delete a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletesaasrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletesaasrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  The etag known to the client for the expected state of the saas. This is
       *  used with state-changing methods to prevent accidental overwrites when
       *  multiple user agents might be acting in parallel on the same resource.
       *  An etag wildcard provide optimistic concurrency based on the expected
       *  existence of the saas. The Any wildcard (`*`) requires that the resource
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callDeleteSaas() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.deleteSaas(request);
        console.log(response);
      }
    
      callDeleteSaas();
    
    

### deleteSaas(request, options, callback)
    
    
    deleteSaas(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteSaasRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteSaasRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletesaasrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletesaasrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSaas(request, callback)
    
    
    deleteSaas(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteSaasRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteSaasRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletesaasrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletesaasrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTenant(request, options)
    
    
    deleteTenant(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteTenantRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteTenantRequest | undefined),
            {} | undefined
        ]>;

Delete a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletetenantrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletetenantrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  The etag known to the client for the expected state of the tenant. This is
       *  used with state-changing methods to prevent accidental overwrites when
       *  multiple user agents might be acting in parallel on the same resource.
       *  An etag wildcard provide optimistic concurrency based on the expected
       *  existence of the tenant. The Any wildcard (`*`) requires that the resource
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callDeleteTenant() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.deleteTenant(request);
        console.log(response);
      }
    
      callDeleteTenant();
    
    

### deleteTenant(request, options, callback)
    
    
    deleteTenant(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteTenantRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteTenantRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletetenantrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletetenantrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTenant(request, callback)
    
    
    deleteTenant(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteTenantRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteTenantRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletetenantrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideletetenantrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUnit(request, options)
    
    
    deleteUnit(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitRequest | undefined),
            {} | undefined
        ]>;

Delete a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  The etag known to the client for the expected state of the unit. This is
       *  used with state-changing methods to prevent accidental overwrites when
       *  multiple user agents might be acting in parallel on the same resource.
       *  An etag wildcard provide optimistic concurrency based on the expected
       *  existence of the unit. The Any wildcard (`*`) requires that the resource
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callDeleteUnit() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.deleteUnit(request);
        console.log(response);
      }
    
      callDeleteUnit();
    
    

### deleteUnit(request, options, callback)
    
    
    deleteUnit(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUnit(request, callback)
    
    
    deleteUnit(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUnitKind(request, options)
    
    
    deleteUnitKind(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitKindRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitKindRequest | undefined),
            {} | undefined
        ]>;

Delete a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitkindrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitkindrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  The etag known to the client for the expected state of the unit kind. This
       *  is used with state-changing methods to prevent accidental overwrites when
       *  multiple user agents might be acting in parallel on the same resource.
       *  An etag wildcard provide optimistic concurrency based on the expected
       *  existence of the unit kind. The Any wildcard (`*`) requires that the
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callDeleteUnitKind() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.deleteUnitKind(request);
        console.log(response);
      }
    
      callDeleteUnitKind();
    
    

### deleteUnitKind(request, options, callback)
    
    
    deleteUnitKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitKindRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitkindrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUnitKind(request, callback)
    
    
    deleteUnitKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitKindRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitkindrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUnitOperation(request, options)
    
    
    deleteUnitOperation(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitOperationRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitOperationRequest | undefined),
            {} | undefined
        ]>;

Delete a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitoperationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitoperationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  The etag known to the client for the expected state of the unit operation.
       *  This is used with state-changing methods to prevent accidental overwrites
       *  when multiple user agents might be acting in parallel on the same resource.
       *  An etag wildcard provide optimistic concurrency based on the expected
       *  existence of the unit operation. The Any wildcard (`*`) requires that the
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callDeleteUnitOperation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.deleteUnitOperation(request);
        console.log(response);
      }
    
      callDeleteUnitOperation();
    
    

### deleteUnitOperation(request, options, callback)
    
    
    deleteUnitOperation(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitOperationRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitoperationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitoperationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteUnitOperation(request, callback)
    
    
    deleteUnitOperation(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitOperationRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitoperationrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.protobuf.iempty), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IDeleteUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ideleteunitoperationrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getRelease(request, options)
    
    
    getRelease(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetReleaseRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetReleaseRequest | undefined),
            {} | undefined
        ]>;

Retrieve a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetreleaserequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetreleaserequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callGetRelease() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.getRelease(request);
        console.log(response);
      }
    
      callGetRelease();
    
    

### getRelease(request, options, callback)
    
    
    getRelease(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetReleaseRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetReleaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetreleaserequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetreleaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRelease(request, callback)
    
    
    getRelease(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetReleaseRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetReleaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetreleaserequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetreleaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSaas(request, options)
    
    
    getSaas(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetSaasRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetSaasRequest | undefined),
            {} | undefined
        ]>;

Retrieve a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetsaasrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetsaasrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callGetSaas() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.getSaas(request);
        console.log(response);
      }
    
      callGetSaas();
    
    

### getSaas(request, options, callback)
    
    
    getSaas(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetSaasRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetSaasRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetsaasrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetsaasrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSaas(request, callback)
    
    
    getSaas(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetSaasRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetSaasRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetsaasrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetsaasrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTenant(request, options)
    
    
    getTenant(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetTenantRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetTenantRequest | undefined),
            {} | undefined
        ]>;

Retrieve a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igettenantrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igettenantrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Tenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.tenant). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callGetTenant() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.getTenant(request);
        console.log(response);
      }
    
      callGetTenant();
    
    

### getTenant(request, options, callback)
    
    
    getTenant(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetTenantRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetTenantRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igettenantrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igettenantrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTenant(request, callback)
    
    
    getTenant(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetTenantRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetTenantRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igettenantrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igettenantrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUnit(request, options)
    
    
    getUnit(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitRequest | undefined),
            {} | undefined
        ]>;

Retrieve a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callGetUnit() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.getUnit(request);
        console.log(response);
      }
    
      callGetUnit();
    
    

### getUnit(request, options, callback)
    
    
    getUnit(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUnit(request, callback)
    
    
    getUnit(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUnitKind(request, options)
    
    
    getUnitKind(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitKindRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitKindRequest | undefined),
            {} | undefined
        ]>;

Retrieve a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitkindrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitkindrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [UnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.unitkind). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callGetUnitKind() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.getUnitKind(request);
        console.log(response);
      }
    
      callGetUnitKind();
    
    

### getUnitKind(request, options, callback)
    
    
    getUnitKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitKindRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitkindrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUnitKind(request, callback)
    
    
    getUnitKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitKindRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitkindrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUnitOperation(request, options)
    
    
    getUnitOperation(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitOperationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitOperationRequest | undefined),
            {} | undefined
        ]>;

Retrieve a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitoperationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitoperationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callGetUnitOperation() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await saasservicemgmtClient.getUnitOperation(request);
        console.log(response);
      }
    
      callGetUnitOperation();
    
    

### getUnitOperation(request, options, callback)
    
    
    getUnitOperation(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitOperationRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitoperationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitoperationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUnitOperation(request, callback)
    
    
    getUnitOperation(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitOperationRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitoperationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IGetUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.igetunitoperationrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### listReleases(request, options)
    
    
    listReleases(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease[],
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest | null,
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesResponse
        ]>;

Retrieve a collection of releases.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease)[], [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesrequest) | null, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listReleasesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listReleases(request, options, callback)
    
    
    listReleases(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReleases(request, callback)
    
    
    listReleases(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReleasesAsync(request, options)
    
    
    listReleasesAsync(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease>;

Equivalent to `listReleases`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the release.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of releases to send per page.
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callListReleases() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = saasservicemgmtClient.[listReleasesAsync](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasdeploymentsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListReleases();
    
    

### listReleasesStream(request, options)
    
    
    listReleasesStream(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListReleasesRequest, options?: CallOptions): Transform;

Equivalent to `listReleases`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReleasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistreleasesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listReleasesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSaas(request, options)
    
    
    listSaas(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas[],
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest | null,
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasResponse
        ]>;

Retrieve a collection of saas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas)[], [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasrequest) | null, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listSaasAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSaas(request, options, callback)
    
    
    listSaas(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSaas(request, callback)
    
    
    listSaas(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSaasAsync(request, options)
    
    
    listSaasAsync(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas>;

Equivalent to `listSaas`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the saas.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of saas to send per page.
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callListSaas() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = saasservicemgmtClient.[listSaasAsync](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasdeploymentsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListSaas();
    
    

### listSaasStream(request, options)
    
    
    listSaasStream(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListSaasRequest, options?: CallOptions): Transform;

Equivalent to `listSaas`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistsaasrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listSaasAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTenants(request, options)
    
    
    listTenants(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant[],
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest | null,
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsResponse
        ]>;

Retrieve a collection of tenants.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTenantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant)[], [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsrequest) | null, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Tenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.tenant). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listTenantsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTenants(request, options, callback)
    
    
    listTenants(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTenantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTenants(request, callback)
    
    
    listTenants(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTenantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTenantsAsync(request, options)
    
    
    listTenantsAsync(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant>;

Equivalent to `listTenants`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTenantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Tenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.tenant). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the tenant.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of tenants to send per page.
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callListTenants() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = saasservicemgmtClient.[listTenantsAsync](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasdeploymentsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListTenants();
    
    

### listTenantsStream(request, options)
    
    
    listTenantsStream(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListTenantsRequest, options?: CallOptions): Transform;

Equivalent to `listTenants`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTenantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilisttenantsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Tenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.tenant) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listTenantsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUnitKinds(request, options)
    
    
    listUnitKinds(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind[],
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest | null,
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsResponse
        ]>;

Retrieve a collection of unit kinds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind)[], [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsrequest) | null, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [UnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.unitkind). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listUnitKindsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUnitKinds(request, options, callback)
    
    
    listUnitKinds(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUnitKinds(request, callback)
    
    
    listUnitKinds(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUnitKindsAsync(request, options)
    
    
    listUnitKindsAsync(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind>;

Equivalent to `listUnitKinds`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [UnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.unitkind). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the unit kind.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of unit kinds to send per page.
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callListUnitKinds() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = saasservicemgmtClient.[listUnitKindsAsync](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasdeploymentsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListUnitKinds();
    
    

### listUnitKindsStream(request, options)
    
    
    listUnitKindsStream(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitKindsRequest, options?: CallOptions): Transform;

Equivalent to `listUnitKinds`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitKindsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitkindsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [UnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.unitkind) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listUnitKindsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUnitOperations(request, options)
    
    
    listUnitOperations(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation[],
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest | null,
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsResponse
        ]>;

Retrieve a collection of unit operations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation)[], [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsrequest) | null, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listUnitOperationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUnitOperations(request, options, callback)
    
    
    listUnitOperations(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUnitOperations(request, callback)
    
    
    listUnitOperations(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUnitOperationsAsync(request, options)
    
    
    listUnitOperationsAsync(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation>;

Equivalent to `listUnitOperations`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the unit operation.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of unit operations to send per page.
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callListUnitOperations() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = saasservicemgmtClient.[listUnitOperationsAsync](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasdeploymentsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListUnitOperations();
    
    

### listUnitOperationsStream(request, options)
    
    
    listUnitOperationsStream(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitOperationsRequest, options?: CallOptions): Transform;

Equivalent to `listUnitOperations`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listUnitOperationsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUnits(request, options)
    
    
    listUnits(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit[],
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest | null,
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsResponse
        ]>;

Retrieve a collection of units.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit)[], [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsrequest) | null, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listUnitsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listUnits(request, options, callback)
    
    
    listUnits(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUnits(request, callback)
    
    
    listUnits(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest, callback: PaginationCallback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsResponse | null | undefined, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsrequest), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsResponse](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsresponse) | null | undefined, [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listUnitsAsync(request, options)
    
    
    listUnitsAsync(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit>;

Equivalent to `listUnits`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the unit.
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of units to send per page.
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
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callListUnits() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = saasservicemgmtClient.[listUnitsAsync](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/v1beta1.saasdeploymentsclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListUnits();
    
    

### listUnitsStream(request, options)
    
    
    listUnitsStream(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IListUnitsRequest, options?: CallOptions): Transform;

Equivalent to `listUnits`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListUnitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ilistunitsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listUnitsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### updateRelease(request, options)
    
    
    updateRelease(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateReleaseRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateReleaseRequest | undefined),
            {} | undefined
        ]>;

Update a single release.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatereleaserequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatereleaserequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired state for the release.
       */
      // const release = {}
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
       *  Release resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask.
       *  If the user does not provide a mask then all fields in the
       *  Release will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Saasservicemgmt library
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callUpdateRelease() {
        // Construct request
        const request = {
          release,
        };
    
        // Run request
        const response = await saasservicemgmtClient.updateRelease(request);
        console.log(response);
      }
    
      callUpdateRelease();
    
    

### updateRelease(request, options, callback)
    
    
    updateRelease(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateReleaseRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateReleaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatereleaserequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatereleaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRelease(request, callback)
    
    
    updateRelease(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateReleaseRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateReleaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatereleaserequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IRelease](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.irelease), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateReleaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatereleaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSaas(request, options)
    
    
    updateSaas(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateSaasRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateSaasRequest | undefined),
            {} | undefined
        ]>;

Update a single saas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatesaasrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatesaasrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired state for the saas.
       */
      // const saas = {}
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
       *  Saas resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask.
       *  If the user does not provide a mask then all fields in the
       *  Saas will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Saasservicemgmt library
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callUpdateSaas() {
        // Construct request
        const request = {
          saas,
        };
    
        // Run request
        const response = await saasservicemgmtClient.updateSaas(request);
        console.log(response);
      }
    
      callUpdateSaas();
    
    

### updateSaas(request, options, callback)
    
    
    updateSaas(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateSaasRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateSaasRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatesaasrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatesaasrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSaas(request, callback)
    
    
    updateSaas(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateSaasRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateSaasRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatesaasrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ISaas](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.isaas), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateSaasRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatesaasrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTenant(request, options)
    
    
    updateTenant(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateTenantRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateTenantRequest | undefined),
            {} | undefined
        ]>;

Update a single tenant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatetenantrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatetenantrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Tenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.tenant). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired state for the tenant.
       */
      // const tenant = {}
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
       *  Tenant resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask.
       *  If the user does not provide a mask then all fields in the
       *  Tenant will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Saasservicemgmt library
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callUpdateTenant() {
        // Construct request
        const request = {
          tenant,
        };
    
        // Run request
        const response = await saasservicemgmtClient.updateTenant(request);
        console.log(response);
      }
    
      callUpdateTenant();
    
    

### updateTenant(request, options, callback)
    
    
    updateTenant(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateTenantRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateTenantRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatetenantrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatetenantrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTenant(request, callback)
    
    
    updateTenant(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateTenantRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateTenantRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatetenantrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.ITenant](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.itenant), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateTenantRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdatetenantrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUnit(request, options)
    
    
    updateUnit(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitRequest | undefined),
            {} | undefined
        ]>;

Update a single unit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired state for the unit.
       */
      // const unit = {}
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
       *  Unit resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask.
       *  If the user does not provide a mask then all fields in the
       *  Unit will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Saasservicemgmt library
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callUpdateUnit() {
        // Construct request
        const request = {
          unit,
        };
    
        // Run request
        const response = await saasservicemgmtClient.updateUnit(request);
        console.log(response);
      }
    
      callUpdateUnit();
    
    

### updateUnit(request, options, callback)
    
    
    updateUnit(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUnit(request, callback)
    
    
    updateUnit(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnit](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunit), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUnitKind(request, options)
    
    
    updateUnitKind(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitKindRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitKindRequest | undefined),
            {} | undefined
        ]>;

Update a single unit kind.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitkindrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitkindrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [UnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.unitkind). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired state for the unit kind.
       */
      // const unitKind = {}
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
       *  UnitKind resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask.
       *  If the user does not provide a mask then all fields in the
       *  UnitKind will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Saasservicemgmt library
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callUpdateUnitKind() {
        // Construct request
        const request = {
          unitKind,
        };
    
        // Run request
        const response = await saasservicemgmtClient.updateUnitKind(request);
        console.log(response);
      }
    
      callUpdateUnitKind();
    
    

### updateUnitKind(request, options, callback)
    
    
    updateUnitKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitKindRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitkindrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUnitKind(request, callback)
    
    
    updateUnitKind(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitKindRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitKindRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitkindrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitKind](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitkind), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitKindRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitkindrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUnitOperation(request, options)
    
    
    updateUnitOperation(request?: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitOperationRequest, options?: CallOptions): Promise<[
            protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation,
            (protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitOperationRequest | undefined),
            {} | undefined
        ]>;

Update a single unit operation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitoperationrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation), ([protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitoperationrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The desired state for the unit operation.
       */
      // const unitOperation = {}
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
       *  UnitOperation resource by the update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask.
       *  If the user does not provide a mask then all fields in the
       *  UnitOperation will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Saasservicemgmt library
      const {SaasDeploymentsClient} = require('[@google-cloud/saasservicemgmt](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const saasservicemgmtClient = new [SaasDeploymentsClient](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/overview.html)();
    
      async function callUpdateUnitOperation() {
        // Construct request
        const request = {
          unitOperation,
        };
    
        // Run request
        const response = await saasservicemgmtClient.updateUnitOperation(request);
        console.log(response);
      }
    
      callUpdateUnitOperation();
    
    

### updateUnitOperation(request, options, callback)
    
    
    updateUnitOperation(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitOperationRequest, options: CallOptions, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitoperationrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitoperationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateUnitOperation(request, callback)
    
    
    updateUnitOperation(request: protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitOperationRequest, callback: Callback<protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation, protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitOperationRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitoperationrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUnitOperation](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iunitoperation), [protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.IUpdateUnitOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/saasservicemgmt/latest/saasservicemgmt/protos.google.cloud.saasplatform.saasservicemgmt.v1beta1.iupdateunitoperationrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
