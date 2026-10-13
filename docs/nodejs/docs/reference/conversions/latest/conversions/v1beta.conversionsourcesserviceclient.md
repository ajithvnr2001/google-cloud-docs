---
url: https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/v1beta.conversionsourcesserviceclient
title: Class v1beta.ConversionSourcesServiceClient (0.8.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:38.240019+00:00
---

# Class v1beta.ConversionSourcesServiceClient (0.8.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/v1beta.conversionsourcesserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.ConversionSourcesServiceClient (0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.1.0 

Service for managing conversion sources for a merchant account. v1beta

## Package

[@google-shopping/conversions](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of ConversionSourcesServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new ConversionSourcesServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### conversionSourcesServiceStub
    
    
    conversionSourcesServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### accountPath(account)
    
    
    accountPath(account: string): string;

Return a fully-qualified account resource name string.

**Parameter**  
---  
**Name** | **Description**  
`account` |  `string`   
  
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
  
### conversionSourcePath(account, conversionSource)
    
    
    conversionSourcePath(account: string, conversionSource: string): string;

Return a fully-qualified conversionSource resource name string.

**Parameters**  
---  
**Name** | **Description**  
`account` |  `string`   
  
`conversionSource` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createConversionSource(request, options)
    
    
    createConversionSource(request?: protos.google.shopping.merchant.conversions.v1beta.ICreateConversionSourceRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.conversions.v1beta.IConversionSource,
            (protos.google.shopping.merchant.conversions.v1beta.ICreateConversionSourceRequest | undefined),
            {} | undefined
        ]>;

Creates a new conversion source.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.icreateconversionsourcerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), ([protos.google.shopping.merchant.conversions.v1beta.ICreateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.icreateconversionsourcerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The merchant account that will own the new conversion source.
       *  Format: accounts/{account}
       */
      // const parent = 'abc123'
      /**
       *  Required. The conversion source description. A new ID will be automatically
       *  assigned to it upon creation.
       */
      // const conversionSource = {}
    
      // Imports the Conversions library
      const {ConversionSourcesServiceClient} = require('[@google-shopping/conversions](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const conversionsClient = new [ConversionSourcesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)();
    
      async function callCreateConversionSource() {
        // Construct request
        const request = {
          parent,
          conversionSource,
        };
    
        // Run request
        const response = await conversionsClient.createConversionSource(request);
        console.log(response);
      }
    
      callCreateConversionSource();
    
    

### createConversionSource(request, options, callback)
    
    
    createConversionSource(request: protos.google.shopping.merchant.conversions.v1beta.ICreateConversionSourceRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.conversions.v1beta.IConversionSource, protos.google.shopping.merchant.conversions.v1beta.ICreateConversionSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.icreateconversionsourcerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), [protos.google.shopping.merchant.conversions.v1beta.ICreateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.icreateconversionsourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversionSource(request, callback)
    
    
    createConversionSource(request: protos.google.shopping.merchant.conversions.v1beta.ICreateConversionSourceRequest, callback: Callback<protos.google.shopping.merchant.conversions.v1beta.IConversionSource, protos.google.shopping.merchant.conversions.v1beta.ICreateConversionSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.icreateconversionsourcerequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), [protos.google.shopping.merchant.conversions.v1beta.ICreateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.icreateconversionsourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversionSource(request, options)
    
    
    deleteConversionSource(request?: protos.google.shopping.merchant.conversions.v1beta.IDeleteConversionSourceRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.shopping.merchant.conversions.v1beta.IDeleteConversionSourceRequest | undefined),
            {} | undefined
        ]>;

Archives an existing conversion source. If the conversion source is a Merchant Center Destination, it will be recoverable for 30 days. If the conversion source is a Google Analytics Link, it will be deleted immediately and can be restored by creating a new one.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ideleteconversionsourcerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.protobuf.iempty), ([protos.google.shopping.merchant.conversions.v1beta.IDeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ideleteconversionsourcerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the conversion source to be deleted.
       *  Format: accounts/{account}/conversionSources/{conversion_source}
       */
      // const name = 'abc123'
    
      // Imports the Conversions library
      const {ConversionSourcesServiceClient} = require('[@google-shopping/conversions](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const conversionsClient = new [ConversionSourcesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)();
    
      async function callDeleteConversionSource() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await conversionsClient.deleteConversionSource(request);
        console.log(response);
      }
    
      callDeleteConversionSource();
    
    

### deleteConversionSource(request, options, callback)
    
    
    deleteConversionSource(request: protos.google.shopping.merchant.conversions.v1beta.IDeleteConversionSourceRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.shopping.merchant.conversions.v1beta.IDeleteConversionSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ideleteconversionsourcerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.protobuf.iempty), [protos.google.shopping.merchant.conversions.v1beta.IDeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ideleteconversionsourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversionSource(request, callback)
    
    
    deleteConversionSource(request: protos.google.shopping.merchant.conversions.v1beta.IDeleteConversionSourceRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.shopping.merchant.conversions.v1beta.IDeleteConversionSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ideleteconversionsourcerequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.protobuf.iempty), [protos.google.shopping.merchant.conversions.v1beta.IDeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ideleteconversionsourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversionSource(request, options)
    
    
    getConversionSource(request?: protos.google.shopping.merchant.conversions.v1beta.IGetConversionSourceRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.conversions.v1beta.IConversionSource,
            (protos.google.shopping.merchant.conversions.v1beta.IGetConversionSourceRequest | undefined),
            {} | undefined
        ]>;

Fetches a conversion source.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.igetconversionsourcerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), ([protos.google.shopping.merchant.conversions.v1beta.IGetConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.igetconversionsourcerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the conversion source to be fetched.
       *  Format: accounts/{account}/conversionsources/{conversion_source}
       */
      // const name = 'abc123'
    
      // Imports the Conversions library
      const {ConversionSourcesServiceClient} = require('[@google-shopping/conversions](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const conversionsClient = new [ConversionSourcesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)();
    
      async function callGetConversionSource() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await conversionsClient.getConversionSource(request);
        console.log(response);
      }
    
      callGetConversionSource();
    
    

### getConversionSource(request, options, callback)
    
    
    getConversionSource(request: protos.google.shopping.merchant.conversions.v1beta.IGetConversionSourceRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.conversions.v1beta.IConversionSource, protos.google.shopping.merchant.conversions.v1beta.IGetConversionSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.igetconversionsourcerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), [protos.google.shopping.merchant.conversions.v1beta.IGetConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.igetconversionsourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversionSource(request, callback)
    
    
    getConversionSource(request: protos.google.shopping.merchant.conversions.v1beta.IGetConversionSourceRequest, callback: Callback<protos.google.shopping.merchant.conversions.v1beta.IConversionSource, protos.google.shopping.merchant.conversions.v1beta.IGetConversionSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.igetconversionsourcerequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), [protos.google.shopping.merchant.conversions.v1beta.IGetConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.igetconversionsourcerequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listConversionSources(request, options)
    
    
    listConversionSources(request?: protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.conversions.v1beta.IConversionSource[],
            protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest | null,
            protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesResponse
        ]>;

Retrieves the list of conversion sources the caller has access to.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource)[], [protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesrequest) | null, [protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listConversionSourcesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listConversionSources(request, options, callback)
    
    
    listConversionSources(request: protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest, options: CallOptions, callback: PaginationCallback<protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest, protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesResponse | null | undefined, protos.google.shopping.merchant.conversions.v1beta.IConversionSource>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesrequest), [protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesresponse) | null | undefined, [protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversionSources(request, callback)
    
    
    listConversionSources(request: protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest, callback: PaginationCallback<protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest, protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesResponse | null | undefined, protos.google.shopping.merchant.conversions.v1beta.IConversionSource>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesrequest), [protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesresponse) | null | undefined, [protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversionSourcesAsync(request, options)
    
    
    listConversionSourcesAsync(request?: protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest, options?: CallOptions): AsyncIterable<protos.google.shopping.merchant.conversions.v1beta.IConversionSource>;

Equivalent to `listConversionSources`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The merchant account who owns the collection of conversion
       *  sources. Format: accounts/{account}
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of conversion sources to return in a page.
       *  If no `page_size` is specified, `100` is used as the default value. The
       *  maximum value is `200`. Values above `200` will be coerced to `200`.
       *  Regardless of pagination, at most `200` conversion sources are returned
       *  in total.
       */
      // const pageSize = 1234
      /**
       *  Optional. Page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Show deleted (archived) option.
       */
      // const showDeleted = true
    
      // Imports the Conversions library
      const {ConversionSourcesServiceClient} = require('[@google-shopping/conversions](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const conversionsClient = new [ConversionSourcesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)();
    
      async function callListConversionSources() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = conversionsClient.listConversionSourcesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListConversionSources();
    
    

### listConversionSourcesStream(request, options)
    
    
    listConversionSourcesStream(request?: protos.google.shopping.merchant.conversions.v1beta.IListConversionSourcesRequest, options?: CallOptions): Transform;

Equivalent to `listConversionSources`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionSourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.ilistconversionsourcesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listConversionSourcesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchAccountFromAccountName(accountName)
    
    
    matchAccountFromAccountName(accountName: string): string | number;

Parse the account from Account resource.

**Parameter**  
---  
**Name** | **Description**  
`accountName` |  `string`   
A fully-qualified path representing Account resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchAccountFromConversionSourceName(conversionSourceName)
    
    
    matchAccountFromConversionSourceName(conversionSourceName: string): string | number;

Parse the account from ConversionSource resource.

**Parameter**  
---  
**Name** | **Description**  
`conversionSourceName` |  `string`   
A fully-qualified path representing ConversionSource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the account.  
  
### matchConversionSourceFromConversionSourceName(conversionSourceName)
    
    
    matchConversionSourceFromConversionSourceName(conversionSourceName: string): string | number;

Parse the conversion_source from ConversionSource resource.

**Parameter**  
---  
**Name** | **Description**  
`conversionSourceName` |  `string`   
A fully-qualified path representing ConversionSource resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversion_source.  
  
### undeleteConversionSource(request, options)
    
    
    undeleteConversionSource(request?: protos.google.shopping.merchant.conversions.v1beta.IUndeleteConversionSourceRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.conversions.v1beta.IConversionSource,
            (protos.google.shopping.merchant.conversions.v1beta.IUndeleteConversionSourceRequest | undefined),
            {} | undefined
        ]>;

Re-enables an archived conversion source. Only Available for Merchant Center Destination conversion sources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iundeleteconversionsourcerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), ([protos.google.shopping.merchant.conversions.v1beta.IUndeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iundeleteconversionsourcerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the conversion source to be undeleted.
       *  Format: accounts/{account}/conversionSources/{conversion_source}
       */
      // const name = 'abc123'
    
      // Imports the Conversions library
      const {ConversionSourcesServiceClient} = require('[@google-shopping/conversions](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const conversionsClient = new [ConversionSourcesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)();
    
      async function callUndeleteConversionSource() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await conversionsClient.undeleteConversionSource(request);
        console.log(response);
      }
    
      callUndeleteConversionSource();
    
    

### undeleteConversionSource(request, options, callback)
    
    
    undeleteConversionSource(request: protos.google.shopping.merchant.conversions.v1beta.IUndeleteConversionSourceRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.conversions.v1beta.IConversionSource, protos.google.shopping.merchant.conversions.v1beta.IUndeleteConversionSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iundeleteconversionsourcerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), [protos.google.shopping.merchant.conversions.v1beta.IUndeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iundeleteconversionsourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeleteConversionSource(request, callback)
    
    
    undeleteConversionSource(request: protos.google.shopping.merchant.conversions.v1beta.IUndeleteConversionSourceRequest, callback: Callback<protos.google.shopping.merchant.conversions.v1beta.IConversionSource, protos.google.shopping.merchant.conversions.v1beta.IUndeleteConversionSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iundeleteconversionsourcerequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), [protos.google.shopping.merchant.conversions.v1beta.IUndeleteConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iundeleteconversionsourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversionSource(request, options)
    
    
    updateConversionSource(request?: protos.google.shopping.merchant.conversions.v1beta.IUpdateConversionSourceRequest, options?: CallOptions): Promise<[
            protos.google.shopping.merchant.conversions.v1beta.IConversionSource,
            (protos.google.shopping.merchant.conversions.v1beta.IUpdateConversionSourceRequest | undefined),
            {} | undefined
        ]>;

Updates information of an existing conversion source. Available only for Merchant Center Destination conversion sources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iupdateconversionsourcerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), ([protos.google.shopping.merchant.conversions.v1beta.IUpdateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iupdateconversionsourcerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The new version of the conversion source data.
       *  Format: accounts/{account}/conversionSources/{conversion_source}
       */
      // const conversionSource = {}
      /**
       *  Required. List of fields being updated.
       */
      // const updateMask = {}
    
      // Imports the Conversions library
      const {ConversionSourcesServiceClient} = require('[@google-shopping/conversions](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const conversionsClient = new [ConversionSourcesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/overview.html)();
    
      async function callUpdateConversionSource() {
        // Construct request
        const request = {
          conversionSource,
          updateMask,
        };
    
        // Run request
        const response = await conversionsClient.updateConversionSource(request);
        console.log(response);
      }
    
      callUpdateConversionSource();
    
    

### updateConversionSource(request, options, callback)
    
    
    updateConversionSource(request: protos.google.shopping.merchant.conversions.v1beta.IUpdateConversionSourceRequest, options: CallOptions, callback: Callback<protos.google.shopping.merchant.conversions.v1beta.IConversionSource, protos.google.shopping.merchant.conversions.v1beta.IUpdateConversionSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iupdateconversionsourcerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), [protos.google.shopping.merchant.conversions.v1beta.IUpdateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iupdateconversionsourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversionSource(request, callback)
    
    
    updateConversionSource(request: protos.google.shopping.merchant.conversions.v1beta.IUpdateConversionSourceRequest, callback: Callback<protos.google.shopping.merchant.conversions.v1beta.IConversionSource, protos.google.shopping.merchant.conversions.v1beta.IUpdateConversionSourceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iupdateconversionsourcerequest)`   
  
`callback` |  `Callback<[protos.google.shopping.merchant.conversions.v1beta.IConversionSource](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iconversionsource), [protos.google.shopping.merchant.conversions.v1beta.IUpdateConversionSourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/conversions/latest/conversions/protos.google.shopping.merchant.conversions.v1beta.iupdateconversionsourcerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
