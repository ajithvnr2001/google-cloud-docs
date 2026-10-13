---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1beta1.dnsthreatdetectorserviceclient
title: Class v1beta1.DnsThreatDetectorServiceClient (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:21.232698+00:00
---

# Class v1beta1.DnsThreatDetectorServiceClient (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/v1beta1.dnsthreatdetectorserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.DnsThreatDetectorServiceClient (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.6.0  3.1.0  1.1.2  1.0.2  0.5.0  0.3.0  0.2.0 

The Network Security API for DNS Threat Detectors. v1beta1

## Package

[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of DnsThreatDetectorServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new DnsThreatDetectorServiceClient({fallback: true}, gax); ```  
  
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

### dnsThreatDetectorServiceStub
    
    
    dnsThreatDetectorServiceStub?: Promise<{
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
  
### createDnsThreatDetector(request, options)
    
    
    createDnsThreatDetector(request?: protos.google.cloud.networksecurity.v1beta1.ICreateDnsThreatDetectorRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector,
            (protos.google.cloud.networksecurity.v1beta1.ICreateDnsThreatDetectorRequest | undefined),
            {} | undefined
        ]>;

Creates a new DnsThreatDetector in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreatednsthreatdetectorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector), ([protos.google.cloud.networksecurity.v1beta1.ICreateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreatednsthreatdetectorrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The value for the parent of the DnsThreatDetector resource.
       */
      // const parent = 'abc123'
      /**
       *  Optional. The ID of the requesting DnsThreatDetector object.
       *  If this field is not supplied, the service generates an identifier.
       */
      // const dnsThreatDetectorId = 'abc123'
      /**
       *  Required. The `DnsThreatDetector` resource to create.
       */
      // const dnsThreatDetector = {}
    
      // Imports the Networksecurity library
      const {DnsThreatDetectorServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [DnsThreatDetectorServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callCreateDnsThreatDetector() {
        // Construct request
        const request = {
          parent,
          dnsThreatDetector,
        };
    
        // Run request
        const response = await networksecurityClient.createDnsThreatDetector(request);
        console.log(response);
      }
    
      callCreateDnsThreatDetector();
    
    

### createDnsThreatDetector(request, options, callback)
    
    
    createDnsThreatDetector(request: protos.google.cloud.networksecurity.v1beta1.ICreateDnsThreatDetectorRequest, options: CallOptions, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector, protos.google.cloud.networksecurity.v1beta1.ICreateDnsThreatDetectorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreatednsthreatdetectorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector), [protos.google.cloud.networksecurity.v1beta1.ICreateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreatednsthreatdetectorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDnsThreatDetector(request, callback)
    
    
    createDnsThreatDetector(request: protos.google.cloud.networksecurity.v1beta1.ICreateDnsThreatDetectorRequest, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector, protos.google.cloud.networksecurity.v1beta1.ICreateDnsThreatDetectorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreatednsthreatdetectorrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector), [protos.google.cloud.networksecurity.v1beta1.ICreateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.icreatednsthreatdetectorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDnsThreatDetector(request, options)
    
    
    deleteDnsThreatDetector(request?: protos.google.cloud.networksecurity.v1beta1.IDeleteDnsThreatDetectorRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.networksecurity.v1beta1.IDeleteDnsThreatDetectorRequest | undefined),
            {} | undefined
        ]>;

Deletes a single DnsThreatDetector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideletednsthreatdetectorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), ([protos.google.cloud.networksecurity.v1beta1.IDeleteDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideletednsthreatdetectorrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the DnsThreatDetector resource.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {DnsThreatDetectorServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [DnsThreatDetectorServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callDeleteDnsThreatDetector() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networksecurityClient.deleteDnsThreatDetector(request);
        console.log(response);
      }
    
      callDeleteDnsThreatDetector();
    
    

### deleteDnsThreatDetector(request, options, callback)
    
    
    deleteDnsThreatDetector(request: protos.google.cloud.networksecurity.v1beta1.IDeleteDnsThreatDetectorRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IDeleteDnsThreatDetectorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideletednsthreatdetectorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IDeleteDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideletednsthreatdetectorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDnsThreatDetector(request, callback)
    
    
    deleteDnsThreatDetector(request: protos.google.cloud.networksecurity.v1beta1.IDeleteDnsThreatDetectorRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.networksecurity.v1beta1.IDeleteDnsThreatDetectorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideletednsthreatdetectorrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.protobuf.iempty), [protos.google.cloud.networksecurity.v1beta1.IDeleteDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ideletednsthreatdetectorrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getDnsThreatDetector(request, options)
    
    
    getDnsThreatDetector(request?: protos.google.cloud.networksecurity.v1beta1.IGetDnsThreatDetectorRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector,
            (protos.google.cloud.networksecurity.v1beta1.IGetDnsThreatDetectorRequest | undefined),
            {} | undefined
        ]>;

Gets the details of a single DnsThreatDetector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetdnsthreatdetectorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector), ([protos.google.cloud.networksecurity.v1beta1.IGetDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetdnsthreatdetectorrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the DnsThreatDetector resource.
       */
      // const name = 'abc123'
    
      // Imports the Networksecurity library
      const {DnsThreatDetectorServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [DnsThreatDetectorServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callGetDnsThreatDetector() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await networksecurityClient.getDnsThreatDetector(request);
        console.log(response);
      }
    
      callGetDnsThreatDetector();
    
    

### getDnsThreatDetector(request, options, callback)
    
    
    getDnsThreatDetector(request: protos.google.cloud.networksecurity.v1beta1.IGetDnsThreatDetectorRequest, options: CallOptions, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector, protos.google.cloud.networksecurity.v1beta1.IGetDnsThreatDetectorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetdnsthreatdetectorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector), [protos.google.cloud.networksecurity.v1beta1.IGetDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetdnsthreatdetectorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDnsThreatDetector(request, callback)
    
    
    getDnsThreatDetector(request: protos.google.cloud.networksecurity.v1beta1.IGetDnsThreatDetectorRequest, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector, protos.google.cloud.networksecurity.v1beta1.IGetDnsThreatDetectorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetdnsthreatdetectorrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector), [protos.google.cloud.networksecurity.v1beta1.IGetDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.igetdnsthreatdetectorrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listDnsThreatDetectors(request, options)
    
    
    listDnsThreatDetectors(request?: protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector[],
            protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest | null,
            protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsResponse
        ]>;

Lists DnsThreatDetectors in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDnsThreatDetectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector)[], [protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsrequest) | null, [protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDnsThreatDetectorsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDnsThreatDetectors(request, options, callback)
    
    
    listDnsThreatDetectors(request: protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest, protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsResponse | null | undefined, protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDnsThreatDetectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsrequest), [protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsresponse) | null | undefined, [protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDnsThreatDetectors(request, callback)
    
    
    listDnsThreatDetectors(request: protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest, callback: PaginationCallback<protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest, protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsResponse | null | undefined, protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDnsThreatDetectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsrequest), [protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsresponse) | null | undefined, [protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDnsThreatDetectorsAsync(request, options)
    
    
    listDnsThreatDetectorsAsync(request?: protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector>;

Equivalent to `listDnsThreatDetectors`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDnsThreatDetectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent value for `ListDnsThreatDetectorsRequest`.
       */
      // const parent = 'abc123'
      /**
       *  Optional. The requested page size. The server may return fewer items than
       *  requested. If unspecified, the server picks an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token received from a previous
       *  `ListDnsThreatDetectorsRequest` call. Provide this to retrieve the
       *  subsequent page.
       */
      // const pageToken = 'abc123'
    
      // Imports the Networksecurity library
      const {DnsThreatDetectorServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [DnsThreatDetectorServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callListDnsThreatDetectors() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = networksecurityClient.listDnsThreatDetectorsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDnsThreatDetectors();
    
    

### listDnsThreatDetectorsStream(request, options)
    
    
    listDnsThreatDetectorsStream(request?: protos.google.cloud.networksecurity.v1beta1.IListDnsThreatDetectorsRequest, options?: CallOptions): Transform;

Equivalent to `listDnsThreatDetectors`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDnsThreatDetectorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.ilistdnsthreatdetectorsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDnsThreatDetectorsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchNetworkFromNetworkName(networkName)
    
    
    matchNetworkFromNetworkName(networkName: string): string | number;

Parse the network from Network resource.

**Parameter**  
---  
**Name** | **Description**  
`networkName` |  `string`   
A fully-qualified path representing Network resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the network.  
  
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
  
### networkPath(project, network)
    
    
    networkPath(project: string, network: string): string;

Return a fully-qualified network resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`network` |  `string`   
  
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
  
### updateDnsThreatDetector(request, options)
    
    
    updateDnsThreatDetector(request?: protos.google.cloud.networksecurity.v1beta1.IUpdateDnsThreatDetectorRequest, options?: CallOptions): Promise<[
            protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector,
            (protos.google.cloud.networksecurity.v1beta1.IUpdateDnsThreatDetectorRequest | undefined),
            {} | undefined
        ]>;

Updates a single DnsThreatDetector.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdatednsthreatdetectorrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector), ([protos.google.cloud.networksecurity.v1beta1.IUpdateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdatednsthreatdetectorrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The field mask is used to specify the fields to be overwritten in
       *  the DnsThreatDetector resource by the update. The fields specified in the
       *  update_mask are relative to the resource, not the full request. A field
       *  will be overwritten if it is in the mask. If the mask is not provided then
       *  all fields present in the request will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The DnsThreatDetector resource being updated.
       */
      // const dnsThreatDetector = {}
    
      // Imports the Networksecurity library
      const {DnsThreatDetectorServiceClient} = require('[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const networksecurityClient = new [DnsThreatDetectorServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)();
    
      async function callUpdateDnsThreatDetector() {
        // Construct request
        const request = {
          dnsThreatDetector,
        };
    
        // Run request
        const response = await networksecurityClient.updateDnsThreatDetector(request);
        console.log(response);
      }
    
      callUpdateDnsThreatDetector();
    
    

### updateDnsThreatDetector(request, options, callback)
    
    
    updateDnsThreatDetector(request: protos.google.cloud.networksecurity.v1beta1.IUpdateDnsThreatDetectorRequest, options: CallOptions, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector, protos.google.cloud.networksecurity.v1beta1.IUpdateDnsThreatDetectorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdatednsthreatdetectorrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector), [protos.google.cloud.networksecurity.v1beta1.IUpdateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdatednsthreatdetectorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDnsThreatDetector(request, callback)
    
    
    updateDnsThreatDetector(request: protos.google.cloud.networksecurity.v1beta1.IUpdateDnsThreatDetectorRequest, callback: Callback<protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector, protos.google.cloud.networksecurity.v1beta1.IUpdateDnsThreatDetectorRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdatednsthreatdetectorrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.networksecurity.v1beta1.IDnsThreatDetector](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.idnsthreatdetector), [protos.google.cloud.networksecurity.v1beta1.IUpdateDnsThreatDetectorRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1beta1.iupdatednsthreatdetectorrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
