---
url: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/v1beta.commercetransactionclient
title: Class v1beta.CommerceTransactionClient (0.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:57.204618+00:00
---

# Class v1beta.CommerceTransactionClient (0.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/v1beta.commercetransactionclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.CommerceTransactionClient (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

APIs related to managing resources that model commercial transactions. v1beta

## Package

[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of CommerceTransactionClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new CommerceTransactionClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### commerceTransactionStub
    
    
    commerceTransactionStub?: Promise<{
            [name: string]: Function;
        }>;

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

### cancelPrivateOffer(request, options)
    
    
    cancelPrivateOffer(request?: protos.google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IPrivateOffer,
            (protos.google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest | undefined),
            {} | undefined
        ]>;

Cancels the target PrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icancelprivateofferrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), ([protos.google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icancelprivateofferrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Optional. Internal note relating to the cancellation.
       *  Stored on the cancelled offer. Not visible to customers.
       */
      // const cancellationNote = 'abc123'
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callCancelPrivateOffer() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await commerceproducerClient.cancelPrivateOffer(request);
        console.log(response);
      }
    
      callCancelPrivateOffer();
    
    

### cancelPrivateOffer(request, options, callback)
    
    
    cancelPrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer, protos.google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icancelprivateofferrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), [protos.google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icancelprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelPrivateOffer(request, callback)
    
    
    cancelPrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer, protos.google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icancelprivateofferrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), [protos.google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icancelprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createPrivateOffer(request, options)
    
    
    createPrivateOffer(request?: protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IPrivateOffer,
            (protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest | undefined),
            {} | undefined
        ]>;

Creates a new PrivateOffer in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), ([protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Required. The resource being created
       */
      // const privateOffer = {}
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callCreatePrivateOffer() {
        // Construct request
        const request = {
          parent,
          privateOffer,
        };
    
        // Run request
        const response = await commerceproducerClient.createPrivateOffer(request);
        console.log(response);
      }
    
      callCreatePrivateOffer();
    
    

### createPrivateOffer(request, options, callback)
    
    
    createPrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer, protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), [protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPrivateOffer(request, callback)
    
    
    createPrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer, protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), [protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPrivateOfferDocument(request, options)
    
    
    createPrivateOfferDocument(request?: protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument,
            (protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest | undefined),
            {} | undefined
        ]>;

Creates a new PrivateOfferDocument in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferdocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument), ([protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferdocumentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Required. The resource being created.
       */
      // const privateOfferDocument = {}
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callCreatePrivateOfferDocument() {
        // Construct request
        const request = {
          parent,
          privateOfferDocument,
        };
    
        // Run request
        const response = await commerceproducerClient.createPrivateOfferDocument(request);
        console.log(response);
      }
    
      callCreatePrivateOfferDocument();
    
    

### createPrivateOfferDocument(request, options, callback)
    
    
    createPrivateOfferDocument(request: protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument, protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferdocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument), [protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferdocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPrivateOfferDocument(request, callback)
    
    
    createPrivateOfferDocument(request: protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument, protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferdocumentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument), [protos.google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferdocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePrivateOffer(request, options)
    
    
    deletePrivateOffer(request?: protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest | undefined),
            {} | undefined
        ]>;

Deletes the target PrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.protobuf.iempty), ([protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Optional. Indicates whether to cascade the delete to child resources.
       *  If false, the request fails if child resources exist.
       */
      // const force = true
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callDeletePrivateOffer() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await commerceproducerClient.deletePrivateOffer(request);
        console.log(response);
      }
    
      callDeletePrivateOffer();
    
    

### deletePrivateOffer(request, options, callback)
    
    
    deletePrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.protobuf.iempty), [protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePrivateOffer(request, callback)
    
    
    deletePrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.protobuf.iempty), [protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePrivateOfferDocument(request, options)
    
    
    deletePrivateOfferDocument(request?: protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest | undefined),
            {} | undefined
        ]>;

Deletes the target PrivateOfferDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferdocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.protobuf.iempty), ([protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferdocumentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       */
      // const name = 'abc123'
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callDeletePrivateOfferDocument() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await commerceproducerClient.deletePrivateOfferDocument(request);
        console.log(response);
      }
    
      callDeletePrivateOfferDocument();
    
    

### deletePrivateOfferDocument(request, options, callback)
    
    
    deletePrivateOfferDocument(request: protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferdocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.protobuf.iempty), [protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferdocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePrivateOfferDocument(request, callback)
    
    
    deletePrivateOfferDocument(request: protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferdocumentrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.protobuf.iempty), [protos.google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferdocumentrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getPrivateOffer(request, options)
    
    
    getPrivateOffer(request?: protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IPrivateOffer,
            (protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single PrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), ([protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Optional. The view of the PrivateOffer to return.
       *  If unspecified, the default view is BASIC.
       */
      // const view = {}
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callGetPrivateOffer() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await commerceproducerClient.getPrivateOffer(request);
        console.log(response);
      }
    
      callGetPrivateOffer();
    
    

### getPrivateOffer(request, options, callback)
    
    
    getPrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer, protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), [protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPrivateOffer(request, callback)
    
    
    getPrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer, protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), [protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPrivateOfferDocument(request, options)
    
    
    getPrivateOfferDocument(request?: protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument,
            (protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single PrivateOfferDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferdocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument), ([protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferdocumentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Name of the resource.
       */
      // const name = 'abc123'
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callGetPrivateOfferDocument() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await commerceproducerClient.getPrivateOfferDocument(request);
        console.log(response);
      }
    
      callGetPrivateOfferDocument();
    
    

### getPrivateOfferDocument(request, options, callback)
    
    
    getPrivateOfferDocument(request: protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument, protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferdocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument), [protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferdocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPrivateOfferDocument(request, callback)
    
    
    getPrivateOfferDocument(request: protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument, protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferdocumentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument), [protos.google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferdocumentrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getService(request, options)
    
    
    getService(request?: protos.google.cloud.commerceproducer.v1beta.IGetServiceRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IService,
            (protos.google.cloud.commerceproducer.v1beta.IGetServiceRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single Service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetservicerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IService](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iservice), ([protos.google.cloud.commerceproducer.v1beta.IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetservicerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Service](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.service). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Optional. The view of the Service to return.
       *  If unspecified, the default view is BASIC.
       */
      // const view = {}
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callGetService() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await commerceproducerClient.getService(request);
        console.log(response);
      }
    
      callGetService();
    
    

### getService(request, options, callback)
    
    
    getService(request: protos.google.cloud.commerceproducer.v1beta.IGetServiceRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IService, protos.google.cloud.commerceproducer.v1beta.IGetServiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetservicerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IService](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iservice), [protos.google.cloud.commerceproducer.v1beta.IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetservicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getService(request, callback)
    
    
    getService(request: protos.google.cloud.commerceproducer.v1beta.IGetServiceRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IService, protos.google.cloud.commerceproducer.v1beta.IGetServiceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetservicerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IService](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iservice), [protos.google.cloud.commerceproducer.v1beta.IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetservicerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSku(request, options)
    
    
    getSku(request?: protos.google.cloud.commerceproducer.v1beta.IGetSkuRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.ISku,
            protos.google.cloud.commerceproducer.v1beta.IGetSkuRequest | undefined,
            {} | undefined
        ]>;

Gets details of a single Sku.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskurequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.ISku](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.isku), [protos.google.cloud.commerceproducer.v1beta.IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskurequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callGetSku() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await commerceproducerClient.getSku(request);
        console.log(response);
      }
    
      callGetSku();
    
    

### getSku(request, options, callback)
    
    
    getSku(request: protos.google.cloud.commerceproducer.v1beta.IGetSkuRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.ISku, protos.google.cloud.commerceproducer.v1beta.IGetSkuRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskurequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.ISku](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.isku), [protos.google.cloud.commerceproducer.v1beta.IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskurequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSku(request, callback)
    
    
    getSku(request: protos.google.cloud.commerceproducer.v1beta.IGetSkuRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.ISku, protos.google.cloud.commerceproducer.v1beta.IGetSkuRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskurequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.ISku](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.isku), [protos.google.cloud.commerceproducer.v1beta.IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskurequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSkuGroup(request, options)
    
    
    getSkuGroup(request?: protos.google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.ISkuGroup,
            (protos.google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single SkuGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskugrouprequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.ISkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iskugroup), ([protos.google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskugrouprequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [SkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.skugroup). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callGetSkuGroup() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await commerceproducerClient.getSkuGroup(request);
        console.log(response);
      }
    
      callGetSkuGroup();
    
    

### getSkuGroup(request, options, callback)
    
    
    getSkuGroup(request: protos.google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.ISkuGroup, protos.google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskugrouprequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.ISkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iskugroup), [protos.google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskugrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSkuGroup(request, callback)
    
    
    getSkuGroup(request: protos.google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.ISkuGroup, protos.google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskugrouprequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.ISkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iskugroup), [protos.google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskugrouprequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStandardOffer(request, options)
    
    
    getStandardOffer(request?: protos.google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IStandardOffer,
            (protos.google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest | undefined),
            {} | undefined
        ]>;

Gets details of a single StandardOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStandardOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetstandardofferrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IStandardOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.istandardoffer), ([protos.google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetstandardofferrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Optional. The view of the StandardOffer to return.
       *  If unspecified, the default view is BASIC.
       */
      // const view = {}
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callGetStandardOffer() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await commerceproducerClient.getStandardOffer(request);
        console.log(response);
      }
    
      callGetStandardOffer();
    
    

### getStandardOffer(request, options, callback)
    
    
    getStandardOffer(request: protos.google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IStandardOffer, protos.google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStandardOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetstandardofferrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IStandardOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.istandardoffer), [protos.google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetstandardofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStandardOffer(request, callback)
    
    
    getStandardOffer(request: protos.google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IStandardOffer, protos.google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStandardOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetstandardofferrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IStandardOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.istandardoffer), [protos.google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetstandardofferrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### listPrivateOfferDocuments(request, options)
    
    
    listPrivateOfferDocuments(request?: protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument[],
            protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest | null,
            protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsResponse
        ]>;

Lists PrivateOfferDocuments for the given parent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument)[], [protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsrequest) | null, [protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listPrivateOfferDocumentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPrivateOfferDocuments(request, options, callback)
    
    
    listPrivateOfferDocuments(request: protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest, protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsrequest), [protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPrivateOfferDocuments(request, callback)
    
    
    listPrivateOfferDocuments(request: protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest, protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsrequest), [protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPrivateOfferDocumentsAsync(request, options)
    
    
    listPrivateOfferDocumentsAsync(request?: protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument>;

Equivalent to `listPrivateOfferDocuments`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListPrivateOfferDocumentsRequest.
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum results to return. The service may return fewer than this
       *  value. The maximum value is 500; values above 500 will be coerced to 500.
       *  If unspecified, the server will default to the maximum.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous list response message.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters of the list request must match the
       *  request that returned the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callListPrivateOfferDocuments() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = commerceproducerClient.[listPrivateOfferDocumentsAsync](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/v1beta.commercetransactionclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListPrivateOfferDocuments();
    
    

### listPrivateOfferDocumentsStream(request, options)
    
    
    listPrivateOfferDocumentsStream(request?: protos.google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest, options?: CallOptions): Transform;

Equivalent to `listPrivateOfferDocuments`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listPrivateOfferDocumentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPrivateOffers(request, options)
    
    
    listPrivateOffers(request?: protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IPrivateOffer[],
            protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest | null,
            protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersResponse
        ]>;

Lists PrivateOffers for the given parent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer)[], [protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersrequest) | null, [protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listPrivateOffersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listPrivateOffers(request, options, callback)
    
    
    listPrivateOffers(request: protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest, protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.IPrivateOffer>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersrequest), [protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPrivateOffers(request, callback)
    
    
    listPrivateOffers(request: protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest, protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.IPrivateOffer>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersrequest), [protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPrivateOffersAsync(request, options)
    
    
    listPrivateOffersAsync(request?: protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer>;

Equivalent to `listPrivateOffers`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListPrivateOffersRequest
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum results to return. The service may return fewer than this
       *  value. The maximum value is 500; values above 500 will be coerced to 500.
       *  If unspecified, the server will default to the maximum.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous list response message.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters of the list request must match the
       *  request that returned the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter expression that matches a subset of resources to show.
       *  See https://google.aip.dev/160 for more details.
       *  Only supports filtering by:
       *  * `update_time`. Example: `update_time > "2012-04-21T11:30:00-04:00"`.
       */
      // const filter = 'abc123'
      /**
       *  Optional. Ordering expression for sorting the results.
       *  See https://google.aip.dev/132#ordering for more details.
       *  If no value is present the default ordering is unspecified.
       *  Only supports ordering by:
       *  * `update_time`
       */
      // const orderBy = 'abc123'
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callListPrivateOffers() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = commerceproducerClient.[listPrivateOffersAsync](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/v1beta.commercetransactionclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListPrivateOffers();
    
    

### listPrivateOffersStream(request, options)
    
    
    listPrivateOffersStream(request?: protos.google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest, options?: CallOptions): Transform;

Equivalent to `listPrivateOffers`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listPrivateOffersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listServices(request, options)
    
    
    listServices(request?: protos.google.cloud.commerceproducer.v1beta.IListServicesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IService[],
            protos.google.cloud.commerceproducer.v1beta.IListServicesRequest | null,
            protos.google.cloud.commerceproducer.v1beta.IListServicesResponse
        ]>;

Lists Services in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IService](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iservice)[], [protos.google.cloud.commerceproducer.v1beta.IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesrequest) | null, [protos.google.cloud.commerceproducer.v1beta.IListServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Service](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.service). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listServicesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listServices(request, options, callback)
    
    
    listServices(request: protos.google.cloud.commerceproducer.v1beta.IListServicesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListServicesRequest, protos.google.cloud.commerceproducer.v1beta.IListServicesResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.IService>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesrequest), [protos.google.cloud.commerceproducer.v1beta.IListServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.IService](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iservice)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServices(request, callback)
    
    
    listServices(request: protos.google.cloud.commerceproducer.v1beta.IListServicesRequest, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListServicesRequest, protos.google.cloud.commerceproducer.v1beta.IListServicesResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.IService>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesrequest), [protos.google.cloud.commerceproducer.v1beta.IListServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.IService](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iservice)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServicesAsync(request, options)
    
    
    listServicesAsync(request?: protos.google.cloud.commerceproducer.v1beta.IListServicesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.commerceproducer.v1beta.IService>;

Equivalent to `listServices`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.commerceproducer.v1beta.IService](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iservice)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Service](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.service). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListServicesRequest
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum results to return. The service may return fewer than this
       *  value. The maximum value is 500; values above 500 will be coerced to 500.
       *  If unspecified, the server will default to the maximum.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callListServices() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = commerceproducerClient.[listServicesAsync](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/v1beta.commercetransactionclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListServices();
    
    

### listServicesStream(request, options)
    
    
    listServicesStream(request?: protos.google.cloud.commerceproducer.v1beta.IListServicesRequest, options?: CallOptions): Transform;

Equivalent to `listServices`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Service](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.service) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listServicesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSkuGroups(request, options)
    
    
    listSkuGroups(request?: protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.ISkuGroup[],
            protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest | null,
            protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsResponse
        ]>;

Lists SkuGroups for the given parent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.ISkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iskugroup)[], [protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsrequest) | null, [protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [SkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.skugroup). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listSkuGroupsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSkuGroups(request, options, callback)
    
    
    listSkuGroups(request: protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest, protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.ISkuGroup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsrequest), [protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.ISkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iskugroup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkuGroups(request, callback)
    
    
    listSkuGroups(request: protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest, protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.ISkuGroup>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsrequest), [protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.ISkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iskugroup)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkuGroupsAsync(request, options)
    
    
    listSkuGroupsAsync(request?: protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.commerceproducer.v1beta.ISkuGroup>;

Equivalent to `listSkuGroups`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.commerceproducer.v1beta.ISkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iskugroup)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [SkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.skugroup). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListSkuGroupsRequest
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum results to return. The service may return fewer than this
       *  value. The maximum value is 500; values above 500 will be coerced to 500.
       *  If unspecified, the server will default to the maximum.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous list response message.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters of the list request must match the
       *  request that returned the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callListSkuGroups() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = commerceproducerClient.[listSkuGroupsAsync](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/v1beta.commercetransactionclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListSkuGroups();
    
    

### listSkuGroupsStream(request, options)
    
    
    listSkuGroupsStream(request?: protos.google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest, options?: CallOptions): Transform;

Equivalent to `listSkuGroups`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [SkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.skugroup) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listSkuGroupsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSkus(request, options)
    
    
    listSkus(request?: protos.google.cloud.commerceproducer.v1beta.IListSkusRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.ISku[],
            protos.google.cloud.commerceproducer.v1beta.IListSkusRequest | null,
            protos.google.cloud.commerceproducer.v1beta.IListSkusResponse
        ]>;

Lists Skus for the given parent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.ISku](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.isku)[], [protos.google.cloud.commerceproducer.v1beta.IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusrequest) | null, [protos.google.cloud.commerceproducer.v1beta.IListSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listSkusAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listSkus(request, options, callback)
    
    
    listSkus(request: protos.google.cloud.commerceproducer.v1beta.IListSkusRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListSkusRequest, protos.google.cloud.commerceproducer.v1beta.IListSkusResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.ISku>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusrequest), [protos.google.cloud.commerceproducer.v1beta.IListSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.ISku](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.isku)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkus(request, callback)
    
    
    listSkus(request: protos.google.cloud.commerceproducer.v1beta.IListSkusRequest, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListSkusRequest, protos.google.cloud.commerceproducer.v1beta.IListSkusResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.ISku>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusrequest), [protos.google.cloud.commerceproducer.v1beta.IListSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.ISku](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.isku)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkusAsync(request, options)
    
    
    listSkusAsync(request?: protos.google.cloud.commerceproducer.v1beta.IListSkusRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.commerceproducer.v1beta.ISku>;

Equivalent to `listSkus`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.commerceproducer.v1beta.ISku](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.isku)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListSkusRequest
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum results to return. The service may return fewer than this
       *  value. The maximum value is 500; values above 500 will be coerced to 500.
       *  If unspecified, the server will default to the maximum.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous list response message.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters of the list request must match the
       *  request that returned the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callListSkus() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = commerceproducerClient.[listSkusAsync](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/v1beta.commercetransactionclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListSkus();
    
    

### listSkusStream(request, options)
    
    
    listSkusStream(request?: protos.google.cloud.commerceproducer.v1beta.IListSkusRequest, options?: CallOptions): Transform;

Equivalent to `listSkus`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listSkusAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listStandardOffers(request, options)
    
    
    listStandardOffers(request?: protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IStandardOffer[],
            protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest | null,
            protos.google.cloud.commerceproducer.v1beta.IListStandardOffersResponse
        ]>;

Lists StandardOffers for the given parent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStandardOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IStandardOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.istandardoffer)[], [protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersrequest) | null, [protos.google.cloud.commerceproducer.v1beta.IListStandardOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listStandardOffersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listStandardOffers(request, options, callback)
    
    
    listStandardOffers(request: protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest, protos.google.cloud.commerceproducer.v1beta.IListStandardOffersResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.IStandardOffer>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStandardOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersrequest), [protos.google.cloud.commerceproducer.v1beta.IListStandardOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.IStandardOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.istandardoffer)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStandardOffers(request, callback)
    
    
    listStandardOffers(request: protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest, callback: PaginationCallback<protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest, protos.google.cloud.commerceproducer.v1beta.IListStandardOffersResponse | null | undefined, protos.google.cloud.commerceproducer.v1beta.IStandardOffer>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStandardOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersrequest), [protos.google.cloud.commerceproducer.v1beta.IListStandardOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersresponse) | null | undefined, [protos.google.cloud.commerceproducer.v1beta.IStandardOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.istandardoffer)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStandardOffersAsync(request, options)
    
    
    listStandardOffersAsync(request?: protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.commerceproducer.v1beta.IStandardOffer>;

Equivalent to `listStandardOffers`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStandardOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.commerceproducer.v1beta.IStandardOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.istandardoffer)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListStandardOffersRequest
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum results to return. The service may return fewer than this
       *  value. The maximum value is 500; values above 500 will be coerced to 500.
       *  If unspecified, the server will default to the maximum.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous list response message.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters of the list request must match the
       *  request that returned the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter expression that matches a subset of resources to show.
       *  See https://google.aip.dev/160 for more details.
       *  Supports filtering by:
       *  * `effective_time`.
       *    Example: `effective_time > "2012-04-21T11:30:00-04:00"`.
       *  * `expire_time`. Example: `expire_time < "2026-05-06t00:00:00z"`.="" */="" const="" filter='abc123' *="" *="" optional.="" ordering="" expression="" for="" sorting="" the="" results.="" *="" see="" https://google.aip.dev/132#ordering="" for="" more="" details.="" *="" if="" no="" value="" is="" present="" the="" default="" ordering="" is="" unspecified.="" *="" supports="" ordering="" by:="" *="" *="" `effective_time`="" *="" *="" `expire_time`="" */="" const="" orderby='abc123' imports="" the="" commerceproducer="" library="" const="" {commercetransactionclient}="require('@google-cloud/commerceproducer').v1beta;" instantiates="" a="" client="" const="" commerceproducerclient="new" commercetransactionclient();="" async="" function="" callliststandardoffers()="" {="" construct="" request="" const="" request="{" parent,="" };="" run="" request="" const="" iterable="commerceproducerClient.listStandardOffersAsync(request);" for="" await="" (const="" response="" of="" iterable)="" {="" console.log(response);="" }="" }="" callliststandardoffers();="">

### listStandardOffersStream(request, options)
    
    
    listStandardOffersStream(request?: protos.google.cloud.commerceproducer.v1beta.IListStandardOffersRequest, options?: CallOptions): Transform;

Equivalent to `listStandardOffers`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStandardOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listStandardOffersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchDocumentFromPrivateOfferDocumentName(privateOfferDocumentName)
    
    
    matchDocumentFromPrivateOfferDocumentName(privateOfferDocumentName: string): string | number;

Parse the document from PrivateOfferDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`privateOfferDocumentName` |  `string`   
A fully-qualified path representing PrivateOfferDocument resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
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
  
### matchLocationFromPrivateOfferDocumentName(privateOfferDocumentName)
    
    
    matchLocationFromPrivateOfferDocumentName(privateOfferDocumentName: string): string | number;

Parse the location from PrivateOfferDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`privateOfferDocumentName` |  `string`   
A fully-qualified path representing PrivateOfferDocument resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromPrivateOfferName(privateOfferName)
    
    
    matchLocationFromPrivateOfferName(privateOfferName: string): string | number;

Parse the location from PrivateOffer resource.

**Parameter**  
---  
**Name** | **Description**  
`privateOfferName` |  `string`   
A fully-qualified path representing PrivateOffer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromServiceName(serviceName)
    
    
    matchLocationFromServiceName(serviceName: string): string | number;

Parse the location from Service resource.

**Parameter**  
---  
**Name** | **Description**  
`serviceName` |  `string`   
A fully-qualified path representing Service resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSkuGroupName(skuGroupName)
    
    
    matchLocationFromSkuGroupName(skuGroupName: string): string | number;

Parse the location from SkuGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`skuGroupName` |  `string`   
A fully-qualified path representing SkuGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSkuName(skuName)
    
    
    matchLocationFromSkuName(skuName: string): string | number;

Parse the location from Sku resource.

**Parameter**  
---  
**Name** | **Description**  
`skuName` |  `string`   
A fully-qualified path representing Sku resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromStandardOfferName(standardOfferName)
    
    
    matchLocationFromStandardOfferName(standardOfferName: string): string | number;

Parse the location from StandardOffer resource.

**Parameter**  
---  
**Name** | **Description**  
`standardOfferName` |  `string`   
A fully-qualified path representing StandardOffer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchPrivateOfferFromPrivateOfferDocumentName(privateOfferDocumentName)
    
    
    matchPrivateOfferFromPrivateOfferDocumentName(privateOfferDocumentName: string): string | number;

Parse the private_offer from PrivateOfferDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`privateOfferDocumentName` |  `string`   
A fully-qualified path representing PrivateOfferDocument resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the private_offer.  
  
### matchPrivateOfferFromPrivateOfferName(privateOfferName)
    
    
    matchPrivateOfferFromPrivateOfferName(privateOfferName: string): string | number;

Parse the private_offer from PrivateOffer resource.

**Parameter**  
---  
**Name** | **Description**  
`privateOfferName` |  `string`   
A fully-qualified path representing PrivateOffer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the private_offer.  
  
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
  
### matchProjectFromPrivateOfferDocumentName(privateOfferDocumentName)
    
    
    matchProjectFromPrivateOfferDocumentName(privateOfferDocumentName: string): string | number;

Parse the project from PrivateOfferDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`privateOfferDocumentName` |  `string`   
A fully-qualified path representing PrivateOfferDocument resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromPrivateOfferName(privateOfferName)
    
    
    matchProjectFromPrivateOfferName(privateOfferName: string): string | number;

Parse the project from PrivateOffer resource.

**Parameter**  
---  
**Name** | **Description**  
`privateOfferName` |  `string`   
A fully-qualified path representing PrivateOffer resource.  
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
  
### matchProjectFromServiceName(serviceName)
    
    
    matchProjectFromServiceName(serviceName: string): string | number;

Parse the project from Service resource.

**Parameter**  
---  
**Name** | **Description**  
`serviceName` |  `string`   
A fully-qualified path representing Service resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSkuGroupName(skuGroupName)
    
    
    matchProjectFromSkuGroupName(skuGroupName: string): string | number;

Parse the project from SkuGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`skuGroupName` |  `string`   
A fully-qualified path representing SkuGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSkuName(skuName)
    
    
    matchProjectFromSkuName(skuName: string): string | number;

Parse the project from Sku resource.

**Parameter**  
---  
**Name** | **Description**  
`skuName` |  `string`   
A fully-qualified path representing Sku resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromStandardOfferName(standardOfferName)
    
    
    matchProjectFromStandardOfferName(standardOfferName: string): string | number;

Parse the project from StandardOffer resource.

**Parameter**  
---  
**Name** | **Description**  
`standardOfferName` |  `string`   
A fully-qualified path representing StandardOffer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchServiceFromServiceName(serviceName)
    
    
    matchServiceFromServiceName(serviceName: string): string | number;

Parse the service from Service resource.

**Parameter**  
---  
**Name** | **Description**  
`serviceName` |  `string`   
A fully-qualified path representing Service resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the service.  
  
### matchServiceFromSkuName(skuName)
    
    
    matchServiceFromSkuName(skuName: string): string | number;

Parse the service from Sku resource.

**Parameter**  
---  
**Name** | **Description**  
`skuName` |  `string`   
A fully-qualified path representing Sku resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the service.  
  
### matchServiceFromStandardOfferName(standardOfferName)
    
    
    matchServiceFromStandardOfferName(standardOfferName: string): string | number;

Parse the service from StandardOffer resource.

**Parameter**  
---  
**Name** | **Description**  
`standardOfferName` |  `string`   
A fully-qualified path representing StandardOffer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the service.  
  
### matchSkuFromSkuName(skuName)
    
    
    matchSkuFromSkuName(skuName: string): string | number;

Parse the sku from Sku resource.

**Parameter**  
---  
**Name** | **Description**  
`skuName` |  `string`   
A fully-qualified path representing Sku resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sku.  
  
### matchSkuGroupFromSkuGroupName(skuGroupName)
    
    
    matchSkuGroupFromSkuGroupName(skuGroupName: string): string | number;

Parse the sku_group from SkuGroup resource.

**Parameter**  
---  
**Name** | **Description**  
`skuGroupName` |  `string`   
A fully-qualified path representing SkuGroup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sku_group.  
  
### matchStandardOfferFromStandardOfferName(standardOfferName)
    
    
    matchStandardOfferFromStandardOfferName(standardOfferName: string): string | number;

Parse the standard_offer from StandardOffer resource.

**Parameter**  
---  
**Name** | **Description**  
`standardOfferName` |  `string`   
A fully-qualified path representing StandardOffer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the standard_offer.  
  
### privateOfferDocumentPath(project, location, privateOffer, document)
    
    
    privateOfferDocumentPath(project: string, location: string, privateOffer: string, document: string): string;

Return a fully-qualified privateOfferDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`privateOffer` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### privateOfferPath(project, location, privateOffer)
    
    
    privateOfferPath(project: string, location: string, privateOffer: string): string;

Return a fully-qualified privateOffer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`privateOffer` |  `string`   
  
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
  
### publishPrivateOffer(request, options)
    
    
    publishPrivateOffer(request?: protos.google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IPrivateOffer,
            (protos.google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest | undefined),
            {} | undefined
        ]>;

Publishes the target PrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPublishPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ipublishprivateofferrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), ([protos.google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ipublishprivateofferrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
       *  Optional. If set to `true`, validates the request but does not execute it.
       */
      // const validateOnly = true
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callPublishPrivateOffer() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await commerceproducerClient.publishPrivateOffer(request);
        console.log(response);
      }
    
      callPublishPrivateOffer();
    
    

### publishPrivateOffer(request, options, callback)
    
    
    publishPrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer, protos.google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPublishPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ipublishprivateofferrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), [protos.google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ipublishprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### publishPrivateOffer(request, callback)
    
    
    publishPrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer, protos.google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPublishPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ipublishprivateofferrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), [protos.google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ipublishprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### servicePath(project, location, service)
    
    
    servicePath(project: string, location: string, service: string): string;

Return a fully-qualified service resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`service` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### skuGroupPath(project, location, skuGroup)
    
    
    skuGroupPath(project: string, location: string, skuGroup: string): string;

Return a fully-qualified skuGroup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`skuGroup` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### skuPath(project, location, service, sku)
    
    
    skuPath(project: string, location: string, service: string, sku: string): string;

Return a fully-qualified sku resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`service` |  `string`   
  
`sku` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### standardOfferPath(project, location, service, standardOffer)
    
    
    standardOfferPath(project: string, location: string, service: string, standardOffer: string): string;

Return a fully-qualified standardOffer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`service` |  `string`   
  
`standardOffer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updatePrivateOffer(request, options)
    
    
    updatePrivateOffer(request?: protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IPrivateOffer,
            (protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest | undefined),
            {} | undefined
        ]>;

Updates the target PrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), ([protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The list of fields to update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask.
       *  The special value "*" means full replacement.
       *  If unspecified, all fields present in the request will be overwritten.
       */
      // const updateMask = {}
      /**
       *  Required. The resource being updated
       */
      // const privateOffer = {}
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callUpdatePrivateOffer() {
        // Construct request
        const request = {
          privateOffer,
        };
    
        // Run request
        const response = await commerceproducerClient.updatePrivateOffer(request);
        console.log(response);
      }
    
      callUpdatePrivateOffer();
    
    

### updatePrivateOffer(request, options, callback)
    
    
    updatePrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer, protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), [protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePrivateOffer(request, callback)
    
    
    updatePrivateOffer(request: protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOffer, protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer), [protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePrivateOfferDocument(request, options)
    
    
    updatePrivateOfferDocument(request?: protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest, options?: CallOptions): Promise<[
            protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument,
            (protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest | undefined),
            {} | undefined
        ]>;

Updates the target PrivateOfferDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferdocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument), ([protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferdocumentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource being updated.
       */
      // const privateOfferDocument = {}
      /**
       *  Optional. The list of fields to update.
       *  The fields specified in the update_mask are relative to the resource, not
       *  the full request. A field will be overwritten if it is in the mask.
       *  The special value "*" means full replacement.
       *  If unspecified, all fields present in the request will be overwritten.
       */
      // const updateMask = {}
    
      // Imports the Commerceproducer library
      const {CommerceTransactionClient} = require('[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const commerceproducerClient = new [CommerceTransactionClient](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)();
    
      async function callUpdatePrivateOfferDocument() {
        // Construct request
        const request = {
          privateOfferDocument,
        };
    
        // Run request
        const response = await commerceproducerClient.updatePrivateOfferDocument(request);
        console.log(response);
      }
    
      callUpdatePrivateOfferDocument();
    
    

### updatePrivateOfferDocument(request, options, callback)
    
    
    updatePrivateOfferDocument(request: protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest, options: CallOptions, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument, protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferdocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument), [protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferdocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePrivateOfferDocument(request, callback)
    
    
    updatePrivateOfferDocument(request: protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest, callback: Callback<protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument, protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferdocumentrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.commerceproducer.v1beta.IPrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateofferdocument), [protos.google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferdocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
