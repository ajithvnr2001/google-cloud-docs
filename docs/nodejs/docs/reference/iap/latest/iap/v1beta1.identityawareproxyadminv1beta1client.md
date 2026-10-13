---
url: https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/v1beta1.identityawareproxyadminv1beta1client
title: Class v1beta1.IdentityAwareProxyAdminV1Beta1Client (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:55.701041+00:00
---

# Class v1beta1.IdentityAwareProxyAdminV1Beta1Client (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/v1beta1.identityawareproxyadminv1beta1client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.IdentityAwareProxyAdminV1Beta1Client (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.4.0  4.2.0  2.3.1  2.2.1  2.0.3  1.1.1  1.0.1 

APIs for Identity-Aware Proxy Admin configurations. v1beta1

## Package

[@google-cloud/iap](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of IdentityAwareProxyAdminV1Beta1Client.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new IdentityAwareProxyAdminV1Beta1Client({fallback: true}, gax); ```  
  
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

### identityAwareProxyAdminV1Beta1Stub
    
    
    identityAwareProxyAdminV1Beta1Stub?: Promise<{
            [name: string]: Function;
        }>;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
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
  
### getIamPolicy(request, options)
    
    
    getIamPolicy(request?: protos.google.iam.v1.IGetIamPolicyRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1.IPolicy,
            protos.google.iam.v1.IGetIamPolicyRequest | undefined,
            {} | undefined
        ]>;

Gets the access control policy for an Identity-Aware Proxy protected resource. More information about managing access via IAP can be found at: https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.igetiampolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.igetiampolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Iap library
      const {IdentityAwareProxyAdminV1Beta1Client} = require('[@google-cloud/iap](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const iapClient = new [IdentityAwareProxyAdminV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/v1beta1.identityawareproxyadminv1beta1client.html)();
    
      async function callGetIamPolicy() {
        // Construct request
        const request = {
          resource,
        };
    
        // Run request
        const response = await iapClient.getIamPolicy(request);
        console.log(response);
      }
    
      callGetIamPolicy();
    
    

### getIamPolicy(request, options, callback)
    
    
    getIamPolicy(request: protos.google.iam.v1.IGetIamPolicyRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.IGetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.igetiampolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.igetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request, callback)
    
    
    getIamPolicy(request: protos.google.iam.v1.IGetIamPolicyRequest, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.IGetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.igetiampolicyrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.igetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### setIamPolicy(request, options)
    
    
    setIamPolicy(request?: protos.google.iam.v1.ISetIamPolicyRequest, options?: CallOptions): Promise<[
            protos.google.iam.v1.IPolicy,
            protos.google.iam.v1.ISetIamPolicyRequest | undefined,
            {} | undefined
        ]>;

Sets the access control policy for an Identity-Aware Proxy protected resource. Replaces any existing policy. More information about managing access via IAP can be found at: https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.isetiampolicyrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.isetiampolicyrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Policy](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.policy). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Iap library
      const {IdentityAwareProxyAdminV1Beta1Client} = require('[@google-cloud/iap](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const iapClient = new [IdentityAwareProxyAdminV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/v1beta1.identityawareproxyadminv1beta1client.html)();
    
      async function callSetIamPolicy() {
        // Construct request
        const request = {
          resource,
          policy,
        };
    
        // Run request
        const response = await iapClient.setIamPolicy(request);
        console.log(response);
      }
    
      callSetIamPolicy();
    
    

### setIamPolicy(request, options, callback)
    
    
    setIamPolicy(request: protos.google.iam.v1.ISetIamPolicyRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.ISetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.isetiampolicyrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.isetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request, callback)
    
    
    setIamPolicy(request: protos.google.iam.v1.ISetIamPolicyRequest, callback: Callback<protos.google.iam.v1.IPolicy, protos.google.iam.v1.ISetIamPolicyRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.isetiampolicyrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.ipolicy), [protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.isetiampolicyrequest) | null | undefined, {} | null | undefined>`   
  
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

Returns permissions that a caller has on the Identity-Aware Proxy protected resource. If the resource does not exist or the caller does not have Identity-Aware Proxy permissions a [google.rpc.Code.PERMISSION_DENIED] will be returned. More information about managing access via IAP can be found at: https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.itestiampermissionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.iam.v1.ITestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.itestiampermissionsresponse), [protos.google.iam.v1.ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.itestiampermissionsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [TestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.testiampermissionsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Iap library
      const {IdentityAwareProxyAdminV1Beta1Client} = require('[@google-cloud/iap](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const iapClient = new [IdentityAwareProxyAdminV1Beta1Client](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/v1beta1.identityawareproxyadminv1beta1client.html)();
    
      async function callTestIamPermissions() {
        // Construct request
        const request = {
          resource,
          permissions,
        };
    
        // Run request
        const response = await iapClient.testIamPermissions(request);
        console.log(response);
      }
    
      callTestIamPermissions();
    
    

### testIamPermissions(request, options, callback)
    
    
    testIamPermissions(request: protos.google.iam.v1.ITestIamPermissionsRequest, options: CallOptions, callback: Callback<protos.google.iam.v1.ITestIamPermissionsResponse, protos.google.iam.v1.ITestIamPermissionsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.itestiampermissionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.iam.v1.ITestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.itestiampermissionsresponse), [protos.google.iam.v1.ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.itestiampermissionsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request, callback)
    
    
    testIamPermissions(request: protos.google.iam.v1.ITestIamPermissionsRequest, callback: Callback<protos.google.iam.v1.ITestIamPermissionsResponse, protos.google.iam.v1.ITestIamPermissionsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.itestiampermissionsrequest)`   
  
`callback` |  `Callback<[protos.google.iam.v1.ITestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.itestiampermissionsresponse), [protos.google.iam.v1.ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/iap/latest/iap/protos.google.iam.v1.itestiampermissionsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
