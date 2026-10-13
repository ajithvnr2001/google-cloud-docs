---
url: https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/v2beta.supporteventsubscriptionserviceclient
title: Class v2beta.SupportEventSubscriptionServiceClient (3.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:44.921044+00:00
---

# Class v2beta.SupportEventSubscriptionServiceClient (3.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/v2beta.supporteventsubscriptionserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v2beta.SupportEventSubscriptionServiceClient (3.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.1 (latest)  2.5.0  2.4.0  1.0.2 

Service for managing customer support event subscriptions. v2beta

## Package

[@google-cloud/support](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of SupportEventSubscriptionServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new SupportEventSubscriptionServiceClient({fallback: true}, gax); ```  
  
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

### supportEventSubscriptionServiceStub
    
    
    supportEventSubscriptionServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### createSupportEventSubscription(request, options)
    
    
    createSupportEventSubscription(request?: protos.google.cloud.support.v2beta.ICreateSupportEventSubscriptionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.support.v2beta.ISupportEventSubscription,
            (protos.google.cloud.support.v2beta.ICreateSupportEventSubscriptionRequest | undefined),
            {} | undefined
        ]>;

Creates a support event subscription for an organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.icreatesupporteventsubscriptionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), ([protos.google.cloud.support.v2beta.ICreateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.icreatesupporteventsubscriptionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name where the support event subscription
       *  will be created. Format: organizations/{organization_id}
       */
      // const parent = 'abc123'
      /**
       *  Required. The Pub/Sub configuration to create.
       */
      // const supportEventSubscription = {}
    
      // Imports the Support library
      const {SupportEventSubscriptionServiceClient} = require('[@google-cloud/support](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const supportClient = new [SupportEventSubscriptionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)();
    
      async function callCreateSupportEventSubscription() {
        // Construct request
        const request = {
          parent,
          supportEventSubscription,
        };
    
        // Run request
        const response = await supportClient.createSupportEventSubscription(request);
        console.log(response);
      }
    
      callCreateSupportEventSubscription();
    
    

### createSupportEventSubscription(request, options, callback)
    
    
    createSupportEventSubscription(request: protos.google.cloud.support.v2beta.ICreateSupportEventSubscriptionRequest, options: CallOptions, callback: Callback<protos.google.cloud.support.v2beta.ISupportEventSubscription, protos.google.cloud.support.v2beta.ICreateSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.icreatesupporteventsubscriptionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), [protos.google.cloud.support.v2beta.ICreateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.icreatesupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSupportEventSubscription(request, callback)
    
    
    createSupportEventSubscription(request: protos.google.cloud.support.v2beta.ICreateSupportEventSubscriptionRequest, callback: Callback<protos.google.cloud.support.v2beta.ISupportEventSubscription, protos.google.cloud.support.v2beta.ICreateSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.icreatesupporteventsubscriptionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), [protos.google.cloud.support.v2beta.ICreateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.icreatesupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSupportEventSubscription(request, options)
    
    
    deleteSupportEventSubscription(request?: protos.google.cloud.support.v2beta.IDeleteSupportEventSubscriptionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.support.v2beta.ISupportEventSubscription,
            (protos.google.cloud.support.v2beta.IDeleteSupportEventSubscriptionRequest | undefined),
            {} | undefined
        ]>;

Soft deletes a support event subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ideletesupporteventsubscriptionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), ([protos.google.cloud.support.v2beta.IDeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ideletesupporteventsubscriptionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the support event subscription to delete.
       *  Format:
       *  organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
       */
      // const name = 'abc123'
    
      // Imports the Support library
      const {SupportEventSubscriptionServiceClient} = require('[@google-cloud/support](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const supportClient = new [SupportEventSubscriptionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)();
    
      async function callDeleteSupportEventSubscription() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await supportClient.deleteSupportEventSubscription(request);
        console.log(response);
      }
    
      callDeleteSupportEventSubscription();
    
    

### deleteSupportEventSubscription(request, options, callback)
    
    
    deleteSupportEventSubscription(request: protos.google.cloud.support.v2beta.IDeleteSupportEventSubscriptionRequest, options: CallOptions, callback: Callback<protos.google.cloud.support.v2beta.ISupportEventSubscription, protos.google.cloud.support.v2beta.IDeleteSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ideletesupporteventsubscriptionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), [protos.google.cloud.support.v2beta.IDeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ideletesupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSupportEventSubscription(request, callback)
    
    
    deleteSupportEventSubscription(request: protos.google.cloud.support.v2beta.IDeleteSupportEventSubscriptionRequest, callback: Callback<protos.google.cloud.support.v2beta.ISupportEventSubscription, protos.google.cloud.support.v2beta.IDeleteSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ideletesupporteventsubscriptionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), [protos.google.cloud.support.v2beta.IDeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ideletesupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### expungeSupportEventSubscription(request, options)
    
    
    expungeSupportEventSubscription(request?: protos.google.cloud.support.v2beta.IExpungeSupportEventSubscriptionRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.support.v2beta.IExpungeSupportEventSubscriptionRequest | undefined),
            {} | undefined
        ]>;

Expunges a support event subscription.

EXAMPLES:

cURL:
    
    
    support_event_subscription="organizations/123456789/supportEventSubscriptions/abcdef123456"
    curl \
      --request POST \
      --header "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://cloudsupport.googleapis.com/v2beta/$support_event_subscription:expunge"
    

Python:
    
    
    import googleapiclient.discovery
    
    api_version = "v2beta"
    supportApiService = googleapiclient.discovery.build(
        serviceName="cloudsupport",
        version=api_version,
        discoveryServiceUrl=f"https://cloudsupport.googleapis.com/$discovery/rest?version={api_version}",
    )
    
    request = supportApiService.supportEventSubscriptions().expunge(
        name="organizations/123456789/supportEventSubscriptions/abcdef123456"
    )
    print(request.execute())
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExpungeSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iexpungesupporteventsubscriptionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.protobuf.iempty), ([protos.google.cloud.support.v2beta.IExpungeSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iexpungesupporteventsubscriptionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the support event subscription to expunge.
       *  Format:
       *  organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
       */
      // const name = 'abc123'
    
      // Imports the Support library
      const {SupportEventSubscriptionServiceClient} = require('[@google-cloud/support](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const supportClient = new [SupportEventSubscriptionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)();
    
      async function callExpungeSupportEventSubscription() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await supportClient.expungeSupportEventSubscription(request);
        console.log(response);
      }
    
      callExpungeSupportEventSubscription();
    
    

### expungeSupportEventSubscription(request, options, callback)
    
    
    expungeSupportEventSubscription(request: protos.google.cloud.support.v2beta.IExpungeSupportEventSubscriptionRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.support.v2beta.IExpungeSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExpungeSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iexpungesupporteventsubscriptionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.protobuf.iempty), [protos.google.cloud.support.v2beta.IExpungeSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iexpungesupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### expungeSupportEventSubscription(request, callback)
    
    
    expungeSupportEventSubscription(request: protos.google.cloud.support.v2beta.IExpungeSupportEventSubscriptionRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.support.v2beta.IExpungeSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IExpungeSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iexpungesupporteventsubscriptionrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.protobuf.iempty), [protos.google.cloud.support.v2beta.IExpungeSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iexpungesupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getSupportEventSubscription(request, options)
    
    
    getSupportEventSubscription(request?: protos.google.cloud.support.v2beta.IGetSupportEventSubscriptionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.support.v2beta.ISupportEventSubscription,
            (protos.google.cloud.support.v2beta.IGetSupportEventSubscriptionRequest | undefined),
            {} | undefined
        ]>;

Gets a support event subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.igetsupporteventsubscriptionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), ([protos.google.cloud.support.v2beta.IGetSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.igetsupporteventsubscriptionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the support event subscription to retrieve.
       *  Format:
       *  organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
       */
      // const name = 'abc123'
    
      // Imports the Support library
      const {SupportEventSubscriptionServiceClient} = require('[@google-cloud/support](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const supportClient = new [SupportEventSubscriptionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)();
    
      async function callGetSupportEventSubscription() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await supportClient.getSupportEventSubscription(request);
        console.log(response);
      }
    
      callGetSupportEventSubscription();
    
    

### getSupportEventSubscription(request, options, callback)
    
    
    getSupportEventSubscription(request: protos.google.cloud.support.v2beta.IGetSupportEventSubscriptionRequest, options: CallOptions, callback: Callback<protos.google.cloud.support.v2beta.ISupportEventSubscription, protos.google.cloud.support.v2beta.IGetSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.igetsupporteventsubscriptionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), [protos.google.cloud.support.v2beta.IGetSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.igetsupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSupportEventSubscription(request, callback)
    
    
    getSupportEventSubscription(request: protos.google.cloud.support.v2beta.IGetSupportEventSubscriptionRequest, callback: Callback<protos.google.cloud.support.v2beta.ISupportEventSubscription, protos.google.cloud.support.v2beta.IGetSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.igetsupporteventsubscriptionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), [protos.google.cloud.support.v2beta.IGetSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.igetsupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listSupportEventSubscriptions(request, options)
    
    
    listSupportEventSubscriptions(request?: protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.support.v2beta.ISupportEventSubscription[],
            protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest | null,
            protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsResponse
        ]>;

Lists support event subscriptions for an organization.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription)[], [protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsrequest) | null, [protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listSupportEventSubscriptionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSupportEventSubscriptions(request, options, callback)
    
    
    listSupportEventSubscriptions(request: protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest, protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsResponse | null | undefined, protos.google.cloud.support.v2beta.ISupportEventSubscription>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsrequest), [protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsresponse) | null | undefined, [protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSupportEventSubscriptions(request, callback)
    
    
    listSupportEventSubscriptions(request: protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest, callback: PaginationCallback<protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest, protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsResponse | null | undefined, protos.google.cloud.support.v2beta.ISupportEventSubscription>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsrequest), [protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsresponse) | null | undefined, [protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSupportEventSubscriptionsAsync(request, options)
    
    
    listSupportEventSubscriptionsAsync(request?: protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.support.v2beta.ISupportEventSubscription>;

Equivalent to `listSupportEventSubscriptions`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The fully qualified name of the Cloud resource to list support
       *  event subscriptions under. Format: organizations/{organization_id}
       */
      // const parent = 'abc123'
      /**
       *  Optional. Filter expression based on AIP-160.
       *  Supported fields:
       *  - pub_sub_topic
       *  - state
       *  Examples:
       *  - `pub_sub_topic="projects/example-project/topics/example-topic"`
       *  - `state=WORKING`
       *  - `pub_sub_topic="projects/example-project/topics/example-topic" AND
       *  state=WORKING`
       */
      // const filter = 'abc123'
      /**
       *  Optional. Whether to show deleted subscriptions. By default, deleted
       *  subscriptions are not returned.
       */
      // const showDeleted = true
      /**
       *  Optional. The maximum number of support event subscriptions to return.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying the page of results to return. If
       *  unspecified, the first page is retrieved.
       *  When paginating, all other parameters provided to
       *  `ListSupportEventSubscriptions` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Support library
      const {SupportEventSubscriptionServiceClient} = require('[@google-cloud/support](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const supportClient = new [SupportEventSubscriptionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)();
    
      async function callListSupportEventSubscriptions() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = supportClient.listSupportEventSubscriptionsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListSupportEventSubscriptions();
    
    

### listSupportEventSubscriptionsStream(request, options)
    
    
    listSupportEventSubscriptionsStream(request?: protos.google.cloud.support.v2beta.IListSupportEventSubscriptionsRequest, options?: CallOptions): Transform;

Equivalent to `listSupportEventSubscriptions`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistsupporteventsubscriptionsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listSupportEventSubscriptionsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAttachmentIdFromOrganizationCaseAttachmentIdName(organizationCaseAttachmentIdName)
    
    
    matchAttachmentIdFromOrganizationCaseAttachmentIdName(organizationCaseAttachmentIdName: string): string | number;

Parse the attachment_id from OrganizationCaseAttachmentId resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseAttachmentIdName` |  `string`   
A fully-qualified path representing organization_case_attachment_id resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the attachment_id.  
  
### matchAttachmentIdFromProjectCaseAttachmentIdName(projectCaseAttachmentIdName)
    
    
    matchAttachmentIdFromProjectCaseAttachmentIdName(projectCaseAttachmentIdName: string): string | number;

Parse the attachment_id from ProjectCaseAttachmentId resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseAttachmentIdName` |  `string`   
A fully-qualified path representing project_case_attachment_id resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the attachment_id.  
  
### matchCaseFromOrganizationCaseAttachmentIdName(organizationCaseAttachmentIdName)
    
    
    matchCaseFromOrganizationCaseAttachmentIdName(organizationCaseAttachmentIdName: string): string | number;

Parse the case from OrganizationCaseAttachmentId resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseAttachmentIdName` |  `string`   
A fully-qualified path representing organization_case_attachment_id resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the case.  
  
### matchCaseFromOrganizationCaseCommentName(organizationCaseCommentName)
    
    
    matchCaseFromOrganizationCaseCommentName(organizationCaseCommentName: string): string | number;

Parse the case from OrganizationCaseComment resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseCommentName` |  `string`   
A fully-qualified path representing organization_case_comment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the case.  
  
### matchCaseFromOrganizationCaseEmailMessagesName(organizationCaseEmailMessagesName)
    
    
    matchCaseFromOrganizationCaseEmailMessagesName(organizationCaseEmailMessagesName: string): string | number;

Parse the case from OrganizationCaseEmailMessages resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseEmailMessagesName` |  `string`   
A fully-qualified path representing organization_case_emailMessages resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the case.  
  
### matchCaseFromOrganizationCaseName(organizationCaseName)
    
    
    matchCaseFromOrganizationCaseName(organizationCaseName: string): string | number;

Parse the case from OrganizationCase resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseName` |  `string`   
A fully-qualified path representing organization_case resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the case.  
  
### matchCaseFromProjectCaseAttachmentIdName(projectCaseAttachmentIdName)
    
    
    matchCaseFromProjectCaseAttachmentIdName(projectCaseAttachmentIdName: string): string | number;

Parse the case from ProjectCaseAttachmentId resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseAttachmentIdName` |  `string`   
A fully-qualified path representing project_case_attachment_id resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the case.  
  
### matchCaseFromProjectCaseCommentName(projectCaseCommentName)
    
    
    matchCaseFromProjectCaseCommentName(projectCaseCommentName: string): string | number;

Parse the case from ProjectCaseComment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseCommentName` |  `string`   
A fully-qualified path representing project_case_comment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the case.  
  
### matchCaseFromProjectCaseEmailMessagesName(projectCaseEmailMessagesName)
    
    
    matchCaseFromProjectCaseEmailMessagesName(projectCaseEmailMessagesName: string): string | number;

Parse the case from ProjectCaseEmailMessages resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseEmailMessagesName` |  `string`   
A fully-qualified path representing project_case_emailMessages resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the case.  
  
### matchCaseFromProjectCaseName(projectCaseName)
    
    
    matchCaseFromProjectCaseName(projectCaseName: string): string | number;

Parse the case from ProjectCase resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseName` |  `string`   
A fully-qualified path representing project_case resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the case.  
  
### matchCommentFromOrganizationCaseCommentName(organizationCaseCommentName)
    
    
    matchCommentFromOrganizationCaseCommentName(organizationCaseCommentName: string): string | number;

Parse the comment from OrganizationCaseComment resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseCommentName` |  `string`   
A fully-qualified path representing organization_case_comment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the comment.  
  
### matchCommentFromProjectCaseCommentName(projectCaseCommentName)
    
    
    matchCommentFromProjectCaseCommentName(projectCaseCommentName: string): string | number;

Parse the comment from ProjectCaseComment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseCommentName` |  `string`   
A fully-qualified path representing project_case_comment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the comment.  
  
### matchEmailMessageFromOrganizationCaseEmailMessagesName(organizationCaseEmailMessagesName)
    
    
    matchEmailMessageFromOrganizationCaseEmailMessagesName(organizationCaseEmailMessagesName: string): string | number;

Parse the email_message from OrganizationCaseEmailMessages resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseEmailMessagesName` |  `string`   
A fully-qualified path representing organization_case_emailMessages resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the email_message.  
  
### matchEmailMessageFromProjectCaseEmailMessagesName(projectCaseEmailMessagesName)
    
    
    matchEmailMessageFromProjectCaseEmailMessagesName(projectCaseEmailMessagesName: string): string | number;

Parse the email_message from ProjectCaseEmailMessages resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseEmailMessagesName` |  `string`   
A fully-qualified path representing project_case_emailMessages resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the email_message.  
  
### matchOrganizationFromOrganizationCaseAttachmentIdName(organizationCaseAttachmentIdName)
    
    
    matchOrganizationFromOrganizationCaseAttachmentIdName(organizationCaseAttachmentIdName: string): string | number;

Parse the organization from OrganizationCaseAttachmentId resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseAttachmentIdName` |  `string`   
A fully-qualified path representing organization_case_attachment_id resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromOrganizationCaseCommentName(organizationCaseCommentName)
    
    
    matchOrganizationFromOrganizationCaseCommentName(organizationCaseCommentName: string): string | number;

Parse the organization from OrganizationCaseComment resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseCommentName` |  `string`   
A fully-qualified path representing organization_case_comment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromOrganizationCaseEmailMessagesName(organizationCaseEmailMessagesName)
    
    
    matchOrganizationFromOrganizationCaseEmailMessagesName(organizationCaseEmailMessagesName: string): string | number;

Parse the organization from OrganizationCaseEmailMessages resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseEmailMessagesName` |  `string`   
A fully-qualified path representing organization_case_emailMessages resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromOrganizationCaseName(organizationCaseName)
    
    
    matchOrganizationFromOrganizationCaseName(organizationCaseName: string): string | number;

Parse the organization from OrganizationCase resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationCaseName` |  `string`   
A fully-qualified path representing organization_case resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromOrganizationName(organizationName)
    
    
    matchOrganizationFromOrganizationName(organizationName: string): string | number;

Parse the organization from Organization resource.

**Parameter**  
---  
**Name** | **Description**  
`organizationName` |  `string`   
A fully-qualified path representing Organization resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchOrganizationFromSupportEventSubscriptionName(supportEventSubscriptionName)
    
    
    matchOrganizationFromSupportEventSubscriptionName(supportEventSubscriptionName: string): string | number;

Parse the organization from SupportEventSubscription resource.

**Parameter**  
---  
**Name** | **Description**  
`supportEventSubscriptionName` |  `string`   
A fully-qualified path representing SupportEventSubscription resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the organization.  
  
### matchProjectFromProjectCaseAttachmentIdName(projectCaseAttachmentIdName)
    
    
    matchProjectFromProjectCaseAttachmentIdName(projectCaseAttachmentIdName: string): string | number;

Parse the project from ProjectCaseAttachmentId resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseAttachmentIdName` |  `string`   
A fully-qualified path representing project_case_attachment_id resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectCaseCommentName(projectCaseCommentName)
    
    
    matchProjectFromProjectCaseCommentName(projectCaseCommentName: string): string | number;

Parse the project from ProjectCaseComment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseCommentName` |  `string`   
A fully-qualified path representing project_case_comment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectCaseEmailMessagesName(projectCaseEmailMessagesName)
    
    
    matchProjectFromProjectCaseEmailMessagesName(projectCaseEmailMessagesName: string): string | number;

Parse the project from ProjectCaseEmailMessages resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseEmailMessagesName` |  `string`   
A fully-qualified path representing project_case_emailMessages resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectCaseName(projectCaseName)
    
    
    matchProjectFromProjectCaseName(projectCaseName: string): string | number;

Parse the project from ProjectCase resource.

**Parameter**  
---  
**Name** | **Description**  
`projectCaseName` |  `string`   
A fully-qualified path representing project_case resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchSupportEventSubscriptionFromSupportEventSubscriptionName(supportEventSubscriptionName)
    
    
    matchSupportEventSubscriptionFromSupportEventSubscriptionName(supportEventSubscriptionName: string): string | number;

Parse the support_event_subscription from SupportEventSubscription resource.

**Parameter**  
---  
**Name** | **Description**  
`supportEventSubscriptionName` |  `string`   
A fully-qualified path representing SupportEventSubscription resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the support_event_subscription.  
  
### organizationCaseAttachmentIdPath(organization, caseParam, attachmentId)
    
    
    organizationCaseAttachmentIdPath(organization: string, caseParam: string, attachmentId: string): string;

Return a fully-qualified organizationCaseAttachmentId resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`caseParam` |  `string`   
  
`attachmentId` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### organizationCaseCommentPath(organization, caseParam, comment)
    
    
    organizationCaseCommentPath(organization: string, caseParam: string, comment: string): string;

Return a fully-qualified organizationCaseComment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`caseParam` |  `string`   
  
`comment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### organizationCaseEmailMessagesPath(organization, caseParam, emailMessage)
    
    
    organizationCaseEmailMessagesPath(organization: string, caseParam: string, emailMessage: string): string;

Return a fully-qualified organizationCaseEmailMessages resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`caseParam` |  `string`   
  
`emailMessage` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### organizationCasePath(organization, caseParam)
    
    
    organizationCasePath(organization: string, caseParam: string): string;

Return a fully-qualified organizationCase resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`caseParam` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### organizationPath(organization)
    
    
    organizationPath(organization: string): string;

Return a fully-qualified organization resource name string.

**Parameter**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectCaseAttachmentIdPath(project, caseParam, attachmentId)
    
    
    projectCaseAttachmentIdPath(project: string, caseParam: string, attachmentId: string): string;

Return a fully-qualified projectCaseAttachmentId resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`caseParam` |  `string`   
  
`attachmentId` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectCaseCommentPath(project, caseParam, comment)
    
    
    projectCaseCommentPath(project: string, caseParam: string, comment: string): string;

Return a fully-qualified projectCaseComment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`caseParam` |  `string`   
  
`comment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectCaseEmailMessagesPath(project, caseParam, emailMessage)
    
    
    projectCaseEmailMessagesPath(project: string, caseParam: string, emailMessage: string): string;

Return a fully-qualified projectCaseEmailMessages resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`caseParam` |  `string`   
  
`emailMessage` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectCasePath(project, caseParam)
    
    
    projectCasePath(project: string, caseParam: string): string;

Return a fully-qualified projectCase resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`caseParam` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### supportEventSubscriptionPath(organization, supportEventSubscription)
    
    
    supportEventSubscriptionPath(organization: string, supportEventSubscription: string): string;

Return a fully-qualified supportEventSubscription resource name string.

**Parameters**  
---  
**Name** | **Description**  
`organization` |  `string`   
  
`supportEventSubscription` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### undeleteSupportEventSubscription(request, options)
    
    
    undeleteSupportEventSubscription(request?: protos.google.cloud.support.v2beta.IUndeleteSupportEventSubscriptionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.support.v2beta.ISupportEventSubscription,
            (protos.google.cloud.support.v2beta.IUndeleteSupportEventSubscriptionRequest | undefined),
            {} | undefined
        ]>;

Undeletes a support event subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iundeletesupporteventsubscriptionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), ([protos.google.cloud.support.v2beta.IUndeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iundeletesupporteventsubscriptionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the support event subscription to undelete.
       *  Format:
       *  organizations/{organization_id}/supportEventSubscriptions/{subscription_id}
       */
      // const name = 'abc123'
    
      // Imports the Support library
      const {SupportEventSubscriptionServiceClient} = require('[@google-cloud/support](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const supportClient = new [SupportEventSubscriptionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)();
    
      async function callUndeleteSupportEventSubscription() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await supportClient.undeleteSupportEventSubscription(request);
        console.log(response);
      }
    
      callUndeleteSupportEventSubscription();
    
    

### undeleteSupportEventSubscription(request, options, callback)
    
    
    undeleteSupportEventSubscription(request: protos.google.cloud.support.v2beta.IUndeleteSupportEventSubscriptionRequest, options: CallOptions, callback: Callback<protos.google.cloud.support.v2beta.ISupportEventSubscription, protos.google.cloud.support.v2beta.IUndeleteSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iundeletesupporteventsubscriptionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), [protos.google.cloud.support.v2beta.IUndeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iundeletesupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeleteSupportEventSubscription(request, callback)
    
    
    undeleteSupportEventSubscription(request: protos.google.cloud.support.v2beta.IUndeleteSupportEventSubscriptionRequest, callback: Callback<protos.google.cloud.support.v2beta.ISupportEventSubscription, protos.google.cloud.support.v2beta.IUndeleteSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iundeletesupporteventsubscriptionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), [protos.google.cloud.support.v2beta.IUndeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iundeletesupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSupportEventSubscription(request, options)
    
    
    updateSupportEventSubscription(request?: protos.google.cloud.support.v2beta.IUpdateSupportEventSubscriptionRequest, options?: CallOptions): Promise<[
            protos.google.cloud.support.v2beta.ISupportEventSubscription,
            (protos.google.cloud.support.v2beta.IUpdateSupportEventSubscriptionRequest | undefined),
            {} | undefined
        ]>;

Updates a support event subscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iupdatesupporteventsubscriptionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), ([protos.google.cloud.support.v2beta.IUpdateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iupdatesupporteventsubscriptionrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The support event subscription to update.
       *  The `name` field is used to identify the configuration to update.
       */
      // const supportEventSubscription = {}
      /**
       *  Optional. The list of fields to update. The only supported value is
       *  pub_sub_topic.
       */
      // const updateMask = {}
    
      // Imports the Support library
      const {SupportEventSubscriptionServiceClient} = require('[@google-cloud/support](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const supportClient = new [SupportEventSubscriptionServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)();
    
      async function callUpdateSupportEventSubscription() {
        // Construct request
        const request = {
          supportEventSubscription,
        };
    
        // Run request
        const response = await supportClient.updateSupportEventSubscription(request);
        console.log(response);
      }
    
      callUpdateSupportEventSubscription();
    
    

### updateSupportEventSubscription(request, options, callback)
    
    
    updateSupportEventSubscription(request: protos.google.cloud.support.v2beta.IUpdateSupportEventSubscriptionRequest, options: CallOptions, callback: Callback<protos.google.cloud.support.v2beta.ISupportEventSubscription, protos.google.cloud.support.v2beta.IUpdateSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iupdatesupporteventsubscriptionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), [protos.google.cloud.support.v2beta.IUpdateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iupdatesupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSupportEventSubscription(request, callback)
    
    
    updateSupportEventSubscription(request: protos.google.cloud.support.v2beta.IUpdateSupportEventSubscriptionRequest, callback: Callback<protos.google.cloud.support.v2beta.ISupportEventSubscription, protos.google.cloud.support.v2beta.IUpdateSupportEventSubscriptionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iupdatesupporteventsubscriptionrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.support.v2beta.ISupportEventSubscription](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isupporteventsubscription), [protos.google.cloud.support.v2beta.IUpdateSupportEventSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iupdatesupporteventsubscriptionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
