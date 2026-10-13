---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1beta.cacheserviceclient
title: Class v1beta.CacheServiceClient (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:48.050058+00:00
---

# Class v1beta.CacheServiceClient (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1beta.cacheserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.CacheServiceClient (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

API for managing cache of content (CachedContent resources) that can be used in GenerativeService requests. This way generate content requests can benefit from preprocessing work being done earlier, possibly lowering their computational cost. It is intended to be used with large contexts. v1beta

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of CacheServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new CacheServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### cacheServiceStub
    
    
    cacheServiceStub?: Promise<{
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
    
    
    static get scopes(): never[];

The scopes needed to make gRPC calls for every method defined in this service.

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### cachedContentPath(id)
    
    
    cachedContentPath(id: string): string;

Return a fully-qualified cachedContent resource name string.

**Parameter**  
---  
**Name** | **Description**  
`id` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### chunkPath(corpus, document, chunk)
    
    
    chunkPath(corpus: string, document: string, chunk: string): string;

Return a fully-qualified chunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
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
  
### corpusPath(corpus)
    
    
    corpusPath(corpus: string): string;

Return a fully-qualified corpus resource name string.

**Parameter**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### corpusPermissionsPath(corpus, permission)
    
    
    corpusPermissionsPath(corpus: string, permission: string): string;

Return a fully-qualified corpusPermissions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
`permission` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createCachedContent(request, options)
    
    
    createCachedContent(request?: protos.google.ai.generativelanguage.v1beta.ICreateCachedContentRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.ICachedContent,
            (protos.google.ai.generativelanguage.v1beta.ICreateCachedContentRequest | undefined),
            {} | undefined
        ]>;

Creates CachedContent resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatecachedcontentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent), ([protos.google.ai.generativelanguage.v1beta.ICreateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatecachedcontentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The cached content to create.
       */
      // const cachedContent = {}
    
      // Imports the Generativelanguage library
      const {CacheServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [CacheServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callCreateCachedContent() {
        // Construct request
        const request = {
          cachedContent,
        };
    
        // Run request
        const response = await generativelanguageClient.createCachedContent(request);
        console.log(response);
      }
    
      callCreateCachedContent();
    
    

### createCachedContent(request, options, callback)
    
    
    createCachedContent(request: protos.google.ai.generativelanguage.v1beta.ICreateCachedContentRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta.ICachedContent, protos.google.ai.generativelanguage.v1beta.ICreateCachedContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatecachedcontentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent), [protos.google.ai.generativelanguage.v1beta.ICreateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatecachedcontentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCachedContent(request, callback)
    
    
    createCachedContent(request: protos.google.ai.generativelanguage.v1beta.ICreateCachedContentRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta.ICachedContent, protos.google.ai.generativelanguage.v1beta.ICreateCachedContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatecachedcontentrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent), [protos.google.ai.generativelanguage.v1beta.ICreateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatecachedcontentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCachedContent(request, options)
    
    
    deleteCachedContent(request?: protos.google.ai.generativelanguage.v1beta.IDeleteCachedContentRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.ai.generativelanguage.v1beta.IDeleteCachedContentRequest | undefined),
            {} | undefined
        ]>;

Deletes CachedContent resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletecachedcontentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), ([protos.google.ai.generativelanguage.v1beta.IDeleteCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletecachedcontentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name referring to the content cache entry
       *  Format: `cachedContents/{id}`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {CacheServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [CacheServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callDeleteCachedContent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.deleteCachedContent(request);
        console.log(response);
      }
    
      callDeleteCachedContent();
    
    

### deleteCachedContent(request, options, callback)
    
    
    deleteCachedContent(request: protos.google.ai.generativelanguage.v1beta.IDeleteCachedContentRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1beta.IDeleteCachedContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletecachedcontentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1beta.IDeleteCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletecachedcontentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCachedContent(request, callback)
    
    
    deleteCachedContent(request: protos.google.ai.generativelanguage.v1beta.IDeleteCachedContentRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1beta.IDeleteCachedContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletecachedcontentrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1beta.IDeleteCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletecachedcontentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### documentPath(corpus, document)
    
    
    documentPath(corpus: string, document: string): string;

Return a fully-qualified document resource name string.

**Parameters**  
---  
**Name** | **Description**  
`corpus` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### filePath(file)
    
    
    filePath(file: string): string;

Return a fully-qualified file resource name string.

**Parameter**  
---  
**Name** | **Description**  
`file` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getCachedContent(request, options)
    
    
    getCachedContent(request?: protos.google.ai.generativelanguage.v1beta.IGetCachedContentRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.ICachedContent,
            (protos.google.ai.generativelanguage.v1beta.IGetCachedContentRequest | undefined),
            {} | undefined
        ]>;

Reads CachedContent resource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetcachedcontentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent), ([protos.google.ai.generativelanguage.v1beta.IGetCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetcachedcontentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name referring to the content cache entry.
       *  Format: `cachedContents/{id}`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {CacheServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [CacheServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGetCachedContent() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.getCachedContent(request);
        console.log(response);
      }
    
      callGetCachedContent();
    
    

### getCachedContent(request, options, callback)
    
    
    getCachedContent(request: protos.google.ai.generativelanguage.v1beta.IGetCachedContentRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta.ICachedContent, protos.google.ai.generativelanguage.v1beta.IGetCachedContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetcachedcontentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent), [protos.google.ai.generativelanguage.v1beta.IGetCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetcachedcontentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCachedContent(request, callback)
    
    
    getCachedContent(request: protos.google.ai.generativelanguage.v1beta.IGetCachedContentRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta.ICachedContent, protos.google.ai.generativelanguage.v1beta.IGetCachedContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetcachedcontentrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent), [protos.google.ai.generativelanguage.v1beta.IGetCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetcachedcontentrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listCachedContents(request, options)
    
    
    listCachedContents(request?: protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.ICachedContent[],
            protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest | null,
            protos.google.ai.generativelanguage.v1beta.IListCachedContentsResponse
        ]>;

Lists CachedContents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCachedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent)[], [protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsrequest) | null, [protos.google.ai.generativelanguage.v1beta.IListCachedContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listCachedContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listCachedContents(request, options, callback)
    
    
    listCachedContents(request: protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest, protos.google.ai.generativelanguage.v1beta.IListCachedContentsResponse | null | undefined, protos.google.ai.generativelanguage.v1beta.ICachedContent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCachedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsrequest), [protos.google.ai.generativelanguage.v1beta.IListCachedContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsresponse) | null | undefined, [protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCachedContents(request, callback)
    
    
    listCachedContents(request: protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest, callback: PaginationCallback<protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest, protos.google.ai.generativelanguage.v1beta.IListCachedContentsResponse | null | undefined, protos.google.ai.generativelanguage.v1beta.ICachedContent>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCachedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsrequest), [protos.google.ai.generativelanguage.v1beta.IListCachedContentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsresponse) | null | undefined, [protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCachedContentsAsync(request, options)
    
    
    listCachedContentsAsync(request?: protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest, options?: CallOptions): AsyncIterable<protos.google.ai.generativelanguage.v1beta.ICachedContent>;

Equivalent to `listCachedContents`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCachedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The maximum number of cached contents to return. The service may
       *  return fewer than this value. If unspecified, some default (under maximum)
       *  number of items will be returned. The maximum value is 1000; values above
       *  1000 will be coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListCachedContents` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListCachedContents` must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Generativelanguage library
      const {CacheServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [CacheServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callListCachedContents() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = generativelanguageClient.listCachedContentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListCachedContents();
    
    

### listCachedContentsStream(request, options)
    
    
    listCachedContentsStream(request?: protos.google.ai.generativelanguage.v1beta.IListCachedContentsRequest, options?: CallOptions): Transform;

Equivalent to `listCachedContents`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCachedContentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistcachedcontentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listCachedContentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchChunkFromChunkName(chunkName)
    
    
    matchChunkFromChunkName(chunkName: string): string | number;

Parse the chunk from Chunk resource.

**Parameter**  
---  
**Name** | **Description**  
`chunkName` |  `string`   
A fully-qualified path representing Chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchCorpusFromChunkName(chunkName)
    
    
    matchCorpusFromChunkName(chunkName: string): string | number;

Parse the corpus from Chunk resource.

**Parameter**  
---  
**Name** | **Description**  
`chunkName` |  `string`   
A fully-qualified path representing Chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchCorpusFromCorpusName(corpusName)
    
    
    matchCorpusFromCorpusName(corpusName: string): string | number;

Parse the corpus from Corpus resource.

**Parameter**  
---  
**Name** | **Description**  
`corpusName` |  `string`   
A fully-qualified path representing Corpus resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchCorpusFromCorpusPermissionsName(corpusPermissionsName)
    
    
    matchCorpusFromCorpusPermissionsName(corpusPermissionsName: string): string | number;

Parse the corpus from CorpusPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`corpusPermissionsName` |  `string`   
A fully-qualified path representing corpus_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchCorpusFromDocumentName(documentName)
    
    
    matchCorpusFromDocumentName(documentName: string): string | number;

Parse the corpus from Document resource.

**Parameter**  
---  
**Name** | **Description**  
`documentName` |  `string`   
A fully-qualified path representing Document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the corpus.  
  
### matchDocumentFromChunkName(chunkName)
    
    
    matchDocumentFromChunkName(chunkName: string): string | number;

Parse the document from Chunk resource.

**Parameter**  
---  
**Name** | **Description**  
`chunkName` |  `string`   
A fully-qualified path representing Chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromDocumentName(documentName)
    
    
    matchDocumentFromDocumentName(documentName: string): string | number;

Parse the document from Document resource.

**Parameter**  
---  
**Name** | **Description**  
`documentName` |  `string`   
A fully-qualified path representing Document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchFileFromFileName(fileName)
    
    
    matchFileFromFileName(fileName: string): string | number;

Parse the file from File resource.

**Parameter**  
---  
**Name** | **Description**  
`fileName` |  `string`   
A fully-qualified path representing File resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the file.  
  
### matchIdFromCachedContentName(cachedContentName)
    
    
    matchIdFromCachedContentName(cachedContentName: string): string | number;

Parse the id from CachedContent resource.

**Parameter**  
---  
**Name** | **Description**  
`cachedContentName` |  `string`   
A fully-qualified path representing CachedContent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the id.  
  
### matchModelFromModelName(modelName)
    
    
    matchModelFromModelName(modelName: string): string | number;

Parse the model from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the model.  
  
### matchPermissionFromCorpusPermissionsName(corpusPermissionsName)
    
    
    matchPermissionFromCorpusPermissionsName(corpusPermissionsName: string): string | number;

Parse the permission from CorpusPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`corpusPermissionsName` |  `string`   
A fully-qualified path representing corpus_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the permission.  
  
### matchPermissionFromTunedModelPermissionsName(tunedModelPermissionsName)
    
    
    matchPermissionFromTunedModelPermissionsName(tunedModelPermissionsName: string): string | number;

Parse the permission from TunedModelPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`tunedModelPermissionsName` |  `string`   
A fully-qualified path representing tuned_model_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the permission.  
  
### matchTunedModelFromTunedModelName(tunedModelName)
    
    
    matchTunedModelFromTunedModelName(tunedModelName: string): string | number;

Parse the tuned_model from TunedModel resource.

**Parameter**  
---  
**Name** | **Description**  
`tunedModelName` |  `string`   
A fully-qualified path representing TunedModel resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tuned_model.  
  
### matchTunedModelFromTunedModelPermissionsName(tunedModelPermissionsName)
    
    
    matchTunedModelFromTunedModelPermissionsName(tunedModelPermissionsName: string): string | number;

Parse the tuned_model from TunedModelPermissions resource.

**Parameter**  
---  
**Name** | **Description**  
`tunedModelPermissionsName` |  `string`   
A fully-qualified path representing tuned_model_permissions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tuned_model.  
  
### modelPath(model)
    
    
    modelPath(model: string): string;

Return a fully-qualified model resource name string.

**Parameter**  
---  
**Name** | **Description**  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tunedModelPath(tunedModel)
    
    
    tunedModelPath(tunedModel: string): string;

Return a fully-qualified tunedModel resource name string.

**Parameter**  
---  
**Name** | **Description**  
`tunedModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tunedModelPermissionsPath(tunedModel, permission)
    
    
    tunedModelPermissionsPath(tunedModel: string, permission: string): string;

Return a fully-qualified tunedModelPermissions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`tunedModel` |  `string`   
  
`permission` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateCachedContent(request, options)
    
    
    updateCachedContent(request?: protos.google.ai.generativelanguage.v1beta.IUpdateCachedContentRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.ICachedContent,
            (protos.google.ai.generativelanguage.v1beta.IUpdateCachedContentRequest | undefined),
            {} | undefined
        ]>;

Updates CachedContent resource (only expiration is updatable).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iupdatecachedcontentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent), ([protos.google.ai.generativelanguage.v1beta.IUpdateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iupdatecachedcontentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The content cache entry to update
       */
      // const cachedContent = {}
      /**
       *  The list of fields to update.
       */
      // const updateMask = {}
    
      // Imports the Generativelanguage library
      const {CacheServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [CacheServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callUpdateCachedContent() {
        // Construct request
        const request = {
          cachedContent,
        };
    
        // Run request
        const response = await generativelanguageClient.updateCachedContent(request);
        console.log(response);
      }
    
      callUpdateCachedContent();
    
    

### updateCachedContent(request, options, callback)
    
    
    updateCachedContent(request: protos.google.ai.generativelanguage.v1beta.IUpdateCachedContentRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta.ICachedContent, protos.google.ai.generativelanguage.v1beta.IUpdateCachedContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iupdatecachedcontentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent), [protos.google.ai.generativelanguage.v1beta.IUpdateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iupdatecachedcontentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCachedContent(request, callback)
    
    
    updateCachedContent(request: protos.google.ai.generativelanguage.v1beta.IUpdateCachedContentRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta.ICachedContent, protos.google.ai.generativelanguage.v1beta.IUpdateCachedContentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iupdatecachedcontentrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.ICachedContent](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icachedcontent), [protos.google.ai.generativelanguage.v1beta.IUpdateCachedContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.iupdatecachedcontentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
