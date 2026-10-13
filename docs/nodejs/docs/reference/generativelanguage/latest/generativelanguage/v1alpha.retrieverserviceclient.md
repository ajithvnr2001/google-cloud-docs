---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1alpha.retrieverserviceclient
title: Class v1alpha.RetrieverServiceClient (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:58.139377+00:00
---

# Class v1alpha.RetrieverServiceClient (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1alpha.retrieverserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.RetrieverServiceClient (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

An API for semantic search over a corpus of user uploaded content. v1alpha

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of RetrieverServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new RetrieverServiceClient({fallback: true}, gax); ```  
  
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

### retrieverServiceStub
    
    
    retrieverServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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

### batchCreateChunks(request, options)
    
    
    batchCreateChunks(request?: protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksResponse,
            (protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest | undefined),
            {} | undefined
        ]>;

Batch create `Chunk`s.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksresponse), ([protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchCreateChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.batchcreatechunksresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The name of the `Document` where this batch of `Chunk`s will be
       *  created. The parent field in every `CreateChunkRequest` must match this
       *  value. Example: `corpora/my-corpus-123/documents/the-doc-abc`
       */
      // const parent = 'abc123'
      /**
       *  Required. The request messages specifying the `Chunk`s to create.
       *  A maximum of 100 `Chunk`s can be created in a batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callBatchCreateChunks() {
        // Construct request
        const request = {
          requests,
        };
    
        // Run request
        const response = await generativelanguageClient.batchCreateChunks(request);
        console.log(response);
      }
    
      callBatchCreateChunks();
    
    

### batchCreateChunks(request, options, callback)
    
    
    batchCreateChunks(request: protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksResponse, protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksresponse), [protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateChunks(request, callback)
    
    
    batchCreateChunks(request: protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksResponse, protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksresponse), [protos.google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteChunks(request, options)
    
    
    batchDeleteChunks(request?: protos.google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest | undefined),
            {} | undefined
        ]>;

Batch delete `Chunk`s.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchdeletechunksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), ([protos.google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchdeletechunksrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The name of the `Document` containing the `Chunk`s to delete.
       *  The parent field in every `DeleteChunkRequest` must match this value.
       *  Example: `corpora/my-corpus-123/documents/the-doc-abc`
       */
      // const parent = 'abc123'
      /**
       *  Required. The request messages specifying the `Chunk`s to delete.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callBatchDeleteChunks() {
        // Construct request
        const request = {
          requests,
        };
    
        // Run request
        const response = await generativelanguageClient.batchDeleteChunks(request);
        console.log(response);
      }
    
      callBatchDeleteChunks();
    
    

### batchDeleteChunks(request, options, callback)
    
    
    batchDeleteChunks(request: protos.google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchdeletechunksrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchdeletechunksrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteChunks(request, callback)
    
    
    batchDeleteChunks(request: protos.google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchdeletechunksrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchdeletechunksrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateChunks(request, options)
    
    
    batchUpdateChunks(request?: protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksResponse,
            (protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest | undefined),
            {} | undefined
        ]>;

Batch update `Chunk`s.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksresponse), ([protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchUpdateChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.batchupdatechunksresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The name of the `Document` containing the `Chunk`s to update.
       *  The parent field in every `UpdateChunkRequest` must match this value.
       *  Example: `corpora/my-corpus-123/documents/the-doc-abc`
       */
      // const parent = 'abc123'
      /**
       *  Required. The request messages specifying the `Chunk`s to update.
       *  A maximum of 100 `Chunk`s can be updated in a batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callBatchUpdateChunks() {
        // Construct request
        const request = {
          requests,
        };
    
        // Run request
        const response = await generativelanguageClient.batchUpdateChunks(request);
        console.log(response);
      }
    
      callBatchUpdateChunks();
    
    

### batchUpdateChunks(request, options, callback)
    
    
    batchUpdateChunks(request: protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksResponse, protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksresponse), [protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateChunks(request, callback)
    
    
    batchUpdateChunks(request: protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksResponse, protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksresponse), [protos.google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### createChunk(request, options)
    
    
    createChunk(request?: protos.google.ai.generativelanguage.v1alpha.ICreateChunkRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IChunk,
            (protos.google.ai.generativelanguage.v1alpha.ICreateChunkRequest | undefined),
            {} | undefined
        ]>;

Creates a `Chunk`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatechunkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk), ([protos.google.ai.generativelanguage.v1alpha.ICreateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatechunkrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Document` where this `Chunk` will be created.
       *  Example: `corpora/my-corpus-123/documents/the-doc-abc`
       */
      // const parent = 'abc123'
      /**
       *  Required. The `Chunk` to create.
       */
      // const chunk = {}
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callCreateChunk() {
        // Construct request
        const request = {
          parent,
          chunk,
        };
    
        // Run request
        const response = await generativelanguageClient.createChunk(request);
        console.log(response);
      }
    
      callCreateChunk();
    
    

### createChunk(request, options, callback)
    
    
    createChunk(request: protos.google.ai.generativelanguage.v1alpha.ICreateChunkRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IChunk, protos.google.ai.generativelanguage.v1alpha.ICreateChunkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatechunkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk), [protos.google.ai.generativelanguage.v1alpha.ICreateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatechunkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createChunk(request, callback)
    
    
    createChunk(request: protos.google.ai.generativelanguage.v1alpha.ICreateChunkRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IChunk, protos.google.ai.generativelanguage.v1alpha.ICreateChunkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatechunkrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk), [protos.google.ai.generativelanguage.v1alpha.ICreateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatechunkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCorpus(request, options)
    
    
    createCorpus(request?: protos.google.ai.generativelanguage.v1alpha.ICreateCorpusRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.ICorpus,
            (protos.google.ai.generativelanguage.v1alpha.ICreateCorpusRequest | undefined),
            {} | undefined
        ]>;

Creates an empty `Corpus`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatecorpusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus), ([protos.google.ai.generativelanguage.v1alpha.ICreateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatecorpusrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Corpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.corpus). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The `Corpus` to create.
       */
      // const corpus = {}
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callCreateCorpus() {
        // Construct request
        const request = {
          corpus,
        };
    
        // Run request
        const response = await generativelanguageClient.createCorpus(request);
        console.log(response);
      }
    
      callCreateCorpus();
    
    

### createCorpus(request, options, callback)
    
    
    createCorpus(request: protos.google.ai.generativelanguage.v1alpha.ICreateCorpusRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ICorpus, protos.google.ai.generativelanguage.v1alpha.ICreateCorpusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatecorpusrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus), [protos.google.ai.generativelanguage.v1alpha.ICreateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatecorpusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCorpus(request, callback)
    
    
    createCorpus(request: protos.google.ai.generativelanguage.v1alpha.ICreateCorpusRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ICorpus, protos.google.ai.generativelanguage.v1alpha.ICreateCorpusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatecorpusrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus), [protos.google.ai.generativelanguage.v1alpha.ICreateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatecorpusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDocument(request, options)
    
    
    createDocument(request?: protos.google.ai.generativelanguage.v1alpha.ICreateDocumentRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IDocument,
            (protos.google.ai.generativelanguage.v1alpha.ICreateDocumentRequest | undefined),
            {} | undefined
        ]>;

Creates an empty `Document`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatedocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument), ([protos.google.ai.generativelanguage.v1alpha.ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatedocumentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Document](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.document). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Corpus` where this `Document` will be created.
       *  Example: `corpora/my-corpus-123`
       */
      // const parent = 'abc123'
      /**
       *  Required. The `Document` to create.
       */
      // const document = {}
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callCreateDocument() {
        // Construct request
        const request = {
          parent,
          document,
        };
    
        // Run request
        const response = await generativelanguageClient.createDocument(request);
        console.log(response);
      }
    
      callCreateDocument();
    
    

### createDocument(request, options, callback)
    
    
    createDocument(request: protos.google.ai.generativelanguage.v1alpha.ICreateDocumentRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IDocument, protos.google.ai.generativelanguage.v1alpha.ICreateDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatedocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument), [protos.google.ai.generativelanguage.v1alpha.ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDocument(request, callback)
    
    
    createDocument(request: protos.google.ai.generativelanguage.v1alpha.ICreateDocumentRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IDocument, protos.google.ai.generativelanguage.v1alpha.ICreateDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatedocumentrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument), [protos.google.ai.generativelanguage.v1alpha.ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteChunk(request, options)
    
    
    deleteChunk(request?: protos.google.ai.generativelanguage.v1alpha.IDeleteChunkRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.ai.generativelanguage.v1alpha.IDeleteChunkRequest | undefined),
            {} | undefined
        ]>;

Deletes a `Chunk`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletechunkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), ([protos.google.ai.generativelanguage.v1alpha.IDeleteChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletechunkrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the `Chunk` to delete.
       *  Example: `corpora/my-corpus-123/documents/the-doc-abc/chunks/some-chunk`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callDeleteChunk() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.deleteChunk(request);
        console.log(response);
      }
    
      callDeleteChunk();
    
    

### deleteChunk(request, options, callback)
    
    
    deleteChunk(request: protos.google.ai.generativelanguage.v1alpha.IDeleteChunkRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1alpha.IDeleteChunkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletechunkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1alpha.IDeleteChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletechunkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteChunk(request, callback)
    
    
    deleteChunk(request: protos.google.ai.generativelanguage.v1alpha.IDeleteChunkRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1alpha.IDeleteChunkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletechunkrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1alpha.IDeleteChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletechunkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCorpus(request, options)
    
    
    deleteCorpus(request?: protos.google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest | undefined),
            {} | undefined
        ]>;

Deletes a `Corpus`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletecorpusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), ([protos.google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletecorpusrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the `Corpus`.
       *  Example: `corpora/my-corpus-123`
       */
      // const name = 'abc123'
      /**
       *  Optional. If set to true, any `Document`s and objects related to this
       *  `Corpus` will also be deleted.
       *  If false (the default), a `FAILED_PRECONDITION` error will be returned if
       *  `Corpus` contains any `Document`s.
       */
      // const force = true
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callDeleteCorpus() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.deleteCorpus(request);
        console.log(response);
      }
    
      callDeleteCorpus();
    
    

### deleteCorpus(request, options, callback)
    
    
    deleteCorpus(request: protos.google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletecorpusrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletecorpusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCorpus(request, callback)
    
    
    deleteCorpus(request: protos.google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletecorpusrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletecorpusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDocument(request, options)
    
    
    deleteDocument(request?: protos.google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest | undefined),
            {} | undefined
        ]>;

Deletes a `Document`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletedocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), ([protos.google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletedocumentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the `Document` to delete.
       *  Example: `corpora/my-corpus-123/documents/the-doc-abc`
       */
      // const name = 'abc123'
      /**
       *  Optional. If set to true, any `Chunk`s and objects related to this
       *  `Document` will also be deleted.
       *  If false (the default), a `FAILED_PRECONDITION` error will be returned if
       *  `Document` contains any `Chunk`s.
       */
      // const force = true
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callDeleteDocument() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.deleteDocument(request);
        console.log(response);
      }
    
      callDeleteDocument();
    
    

### deleteDocument(request, options, callback)
    
    
    deleteDocument(request: protos.google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletedocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDocument(request, callback)
    
    
    deleteDocument(request: protos.google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletedocumentrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletedocumentrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getChunk(request, options)
    
    
    getChunk(request?: protos.google.ai.generativelanguage.v1alpha.IGetChunkRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IChunk,
            protos.google.ai.generativelanguage.v1alpha.IGetChunkRequest | undefined,
            {} | undefined
        ]>;

Gets information about a specific `Chunk`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetchunkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk), [protos.google.ai.generativelanguage.v1alpha.IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetchunkrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Chunk` to retrieve.
       *  Example: `corpora/my-corpus-123/documents/the-doc-abc/chunks/some-chunk`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGetChunk() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.getChunk(request);
        console.log(response);
      }
    
      callGetChunk();
    
    

### getChunk(request, options, callback)
    
    
    getChunk(request: protos.google.ai.generativelanguage.v1alpha.IGetChunkRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IChunk, protos.google.ai.generativelanguage.v1alpha.IGetChunkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetchunkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk), [protos.google.ai.generativelanguage.v1alpha.IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetchunkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChunk(request, callback)
    
    
    getChunk(request: protos.google.ai.generativelanguage.v1alpha.IGetChunkRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IChunk, protos.google.ai.generativelanguage.v1alpha.IGetChunkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetchunkrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk), [protos.google.ai.generativelanguage.v1alpha.IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetchunkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCorpus(request, options)
    
    
    getCorpus(request?: protos.google.ai.generativelanguage.v1alpha.IGetCorpusRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.ICorpus,
            protos.google.ai.generativelanguage.v1alpha.IGetCorpusRequest | undefined,
            {} | undefined
        ]>;

Gets information about a specific `Corpus`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetcorpusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus), [protos.google.ai.generativelanguage.v1alpha.IGetCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetcorpusrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Corpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.corpus). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Corpus`.
       *  Example: `corpora/my-corpus-123`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGetCorpus() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.getCorpus(request);
        console.log(response);
      }
    
      callGetCorpus();
    
    

### getCorpus(request, options, callback)
    
    
    getCorpus(request: protos.google.ai.generativelanguage.v1alpha.IGetCorpusRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ICorpus, protos.google.ai.generativelanguage.v1alpha.IGetCorpusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetcorpusrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus), [protos.google.ai.generativelanguage.v1alpha.IGetCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetcorpusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCorpus(request, callback)
    
    
    getCorpus(request: protos.google.ai.generativelanguage.v1alpha.IGetCorpusRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ICorpus, protos.google.ai.generativelanguage.v1alpha.IGetCorpusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetcorpusrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus), [protos.google.ai.generativelanguage.v1alpha.IGetCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetcorpusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDocument(request, options)
    
    
    getDocument(request?: protos.google.ai.generativelanguage.v1alpha.IGetDocumentRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IDocument,
            (protos.google.ai.generativelanguage.v1alpha.IGetDocumentRequest | undefined),
            {} | undefined
        ]>;

Gets information about a specific `Document`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetdocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument), ([protos.google.ai.generativelanguage.v1alpha.IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetdocumentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Document](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.document). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Document` to retrieve.
       *  Example: `corpora/my-corpus-123/documents/the-doc-abc`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGetDocument() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.getDocument(request);
        console.log(response);
      }
    
      callGetDocument();
    
    

### getDocument(request, options, callback)
    
    
    getDocument(request: protos.google.ai.generativelanguage.v1alpha.IGetDocumentRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IDocument, protos.google.ai.generativelanguage.v1alpha.IGetDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetdocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument), [protos.google.ai.generativelanguage.v1alpha.IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetdocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDocument(request, callback)
    
    
    getDocument(request: protos.google.ai.generativelanguage.v1alpha.IGetDocumentRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IDocument, protos.google.ai.generativelanguage.v1alpha.IGetDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetdocumentrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument), [protos.google.ai.generativelanguage.v1alpha.IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetdocumentrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listChunks(request, options)
    
    
    listChunks(request?: protos.google.ai.generativelanguage.v1alpha.IListChunksRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IChunk[],
            protos.google.ai.generativelanguage.v1alpha.IListChunksRequest | null,
            protos.google.ai.generativelanguage.v1alpha.IListChunksResponse
        ]>;

Lists all `Chunk`s in a `Document`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk)[], [protos.google.ai.generativelanguage.v1alpha.IListChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksrequest) | null, [protos.google.ai.generativelanguage.v1alpha.IListChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listChunksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listChunks(request, options, callback)
    
    
    listChunks(request: protos.google.ai.generativelanguage.v1alpha.IListChunksRequest, options: CallOptions, callback: PaginationCallback<protos.google.ai.generativelanguage.v1alpha.IListChunksRequest, protos.google.ai.generativelanguage.v1alpha.IListChunksResponse | null | undefined, protos.google.ai.generativelanguage.v1alpha.IChunk>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1alpha.IListChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksrequest), [protos.google.ai.generativelanguage.v1alpha.IListChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksresponse) | null | undefined, [protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChunks(request, callback)
    
    
    listChunks(request: protos.google.ai.generativelanguage.v1alpha.IListChunksRequest, callback: PaginationCallback<protos.google.ai.generativelanguage.v1alpha.IListChunksRequest, protos.google.ai.generativelanguage.v1alpha.IListChunksResponse | null | undefined, protos.google.ai.generativelanguage.v1alpha.IChunk>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1alpha.IListChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksrequest), [protos.google.ai.generativelanguage.v1alpha.IListChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksresponse) | null | undefined, [protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChunksAsync(request, options)
    
    
    listChunksAsync(request?: protos.google.ai.generativelanguage.v1alpha.IListChunksRequest, options?: CallOptions): AsyncIterable<protos.google.ai.generativelanguage.v1alpha.IChunk>;

Equivalent to `listChunks`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Document` containing `Chunk`s.
       *  Example: `corpora/my-corpus-123/documents/the-doc-abc`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of `Chunk`s to return (per page).
       *  The service may return fewer `Chunk`s.
       *  If unspecified, at most 10 `Chunk`s will be returned.
       *  The maximum size limit is 100 `Chunk`s per page.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListChunks` call.
       *  Provide the `next_page_token` returned in the response as an argument to
       *  the next request to retrieve the next page.
       *  When paginating, all other parameters provided to `ListChunks`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callListChunks() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = generativelanguageClient.listChunksAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListChunks();
    
    

### listChunksStream(request, options)
    
    
    listChunksStream(request?: protos.google.ai.generativelanguage.v1alpha.IListChunksRequest, options?: CallOptions): Transform;

Equivalent to `listChunks`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listChunksAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listCorpora(request, options)
    
    
    listCorpora(request?: protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.ICorpus[],
            protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest | null,
            protos.google.ai.generativelanguage.v1alpha.IListCorporaResponse
        ]>;

Lists all `Corpora` owned by the user.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCorporaRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus)[], [protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporarequest) | null, [protos.google.ai.generativelanguage.v1alpha.IListCorporaResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporaresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Corpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.corpus). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listCorporaAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listCorpora(request, options, callback)
    
    
    listCorpora(request: protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest, options: CallOptions, callback: PaginationCallback<protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest, protos.google.ai.generativelanguage.v1alpha.IListCorporaResponse | null | undefined, protos.google.ai.generativelanguage.v1alpha.ICorpus>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCorporaRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporarequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporarequest), [protos.google.ai.generativelanguage.v1alpha.IListCorporaResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporaresponse) | null | undefined, [protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCorpora(request, callback)
    
    
    listCorpora(request: protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest, callback: PaginationCallback<protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest, protos.google.ai.generativelanguage.v1alpha.IListCorporaResponse | null | undefined, protos.google.ai.generativelanguage.v1alpha.ICorpus>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCorporaRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporarequest)`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporarequest), [protos.google.ai.generativelanguage.v1alpha.IListCorporaResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporaresponse) | null | undefined, [protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCorporaAsync(request, options)
    
    
    listCorporaAsync(request?: protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest, options?: CallOptions): AsyncIterable<protos.google.ai.generativelanguage.v1alpha.ICorpus>;

Equivalent to `listCorpora`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCorporaRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Corpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.corpus). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. The maximum number of `Corpora` to return (per page).
       *  The service may return fewer `Corpora`.
       *  If unspecified, at most 10 `Corpora` will be returned.
       *  The maximum size limit is 20 `Corpora` per page.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListCorpora` call.
       *  Provide the `next_page_token` returned in the response as an argument to
       *  the next request to retrieve the next page.
       *  When paginating, all other parameters provided to `ListCorpora`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callListCorpora() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = generativelanguageClient.listCorporaAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListCorpora();
    
    

### listCorporaStream(request, options)
    
    
    listCorporaStream(request?: protos.google.ai.generativelanguage.v1alpha.IListCorporaRequest, options?: CallOptions): Transform;

Equivalent to `listCorpora`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCorporaRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporarequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Corpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.corpus) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listCorporaAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDocuments(request, options)
    
    
    listDocuments(request?: protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IDocument[],
            protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest | null,
            protos.google.ai.generativelanguage.v1alpha.IListDocumentsResponse
        ]>;

Lists all `Document`s in a `Corpus`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument)[], [protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsrequest) | null, [protos.google.ai.generativelanguage.v1alpha.IListDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Document](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.document). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDocumentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDocuments(request, options, callback)
    
    
    listDocuments(request: protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest, protos.google.ai.generativelanguage.v1alpha.IListDocumentsResponse | null | undefined, protos.google.ai.generativelanguage.v1alpha.IDocument>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsrequest), [protos.google.ai.generativelanguage.v1alpha.IListDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsresponse) | null | undefined, [protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDocuments(request, callback)
    
    
    listDocuments(request: protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest, callback: PaginationCallback<protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest, protos.google.ai.generativelanguage.v1alpha.IListDocumentsResponse | null | undefined, protos.google.ai.generativelanguage.v1alpha.IDocument>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsrequest), [protos.google.ai.generativelanguage.v1alpha.IListDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsresponse) | null | undefined, [protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDocumentsAsync(request, options)
    
    
    listDocumentsAsync(request?: protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest, options?: CallOptions): AsyncIterable<protos.google.ai.generativelanguage.v1alpha.IDocument>;

Equivalent to `listDocuments`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Document](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.document). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Corpus` containing `Document`s.
       *  Example: `corpora/my-corpus-123`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of `Document`s to return (per page).
       *  The service may return fewer `Document`s.
       *  If unspecified, at most 10 `Document`s will be returned.
       *  The maximum size limit is 20 `Document`s per page.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListDocuments` call.
       *  Provide the `next_page_token` returned in the response as an argument to
       *  the next request to retrieve the next page.
       *  When paginating, all other parameters provided to `ListDocuments`
       *  must match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callListDocuments() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = generativelanguageClient.listDocumentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDocuments();
    
    

### listDocumentsStream(request, options)
    
    
    listDocumentsStream(request?: protos.google.ai.generativelanguage.v1alpha.IListDocumentsRequest, options?: CallOptions): Transform;

Equivalent to `listDocuments`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Document](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.document) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDocumentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### queryCorpus(request, options)
    
    
    queryCorpus(request?: protos.google.ai.generativelanguage.v1alpha.IQueryCorpusRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IQueryCorpusResponse,
            (protos.google.ai.generativelanguage.v1alpha.IQueryCorpusRequest | undefined),
            {} | undefined
        ]>;

Performs semantic search over a `Corpus`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IQueryCorpusResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusresponse), ([protos.google.ai.generativelanguage.v1alpha.IQueryCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [QueryCorpusResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.querycorpusresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Corpus` to query.
       *  Example: `corpora/my-corpus-123`
       */
      // const name = 'abc123'
      /**
       *  Required. Query string to perform semantic search.
       */
      // const query = 'abc123'
      /**
       *  Optional. Filter for `Chunk` and `Document` metadata. Each `MetadataFilter`
       *  object should correspond to a unique key. Multiple `MetadataFilter` objects
       *  are joined by logical "AND"s.
       *  Example query at document level:
       *  (year >= 2020 OR year < 2010)="" and="" (genre="drama" or="" genre="action)" *="" `metadatafilter`="" object="" list:="" *="" metadata_filters="*" {key="document.custom_metadata.year" *="" conditions="{int_value" =="" 2020,="" operation="GREATER_EQUAL}," *="" {int_value="2010," operation="LESS}" },="" *="" {key="document.custom_metadata.year" *="" conditions="{int_value" =="" 2020,="" operation="GREATER_EQUAL}," *="" {int_value="2010," operation="LESS}" },="" *="" {key="document.custom_metadata.genre" *="" conditions="{string_value" =="" "drama",="" operation="EQUAL}," *="" {string_value="action" ,="" operation="EQUAL}" }="" *="" example="" query="" at="" chunk="" level="" for="" a="" numeric="" range="" of="" values:="" *="" (year=""> 2015 AND year <= 2020)="" *="" `metadatafilter`="" object="" list:="" *="" metadata_filters="*" {key="chunk.custom_metadata.year" *="" conditions="{int_value" =="" 2015,="" operation="GREATER}" },="" *="" {key="chunk.custom_metadata.year" *="" conditions="{int_value" =="" 2020,="" operation="LESS_EQUAL}" }="" *="" note:="" "and"s="" for="" the="" same="" key="" are="" only="" supported="" for="" numeric="" values.="" string="" *="" values="" only="" support="" "or"s="" for="" the="" same="" key.="" */="" const="" metadatafilters="[1,2,3,4]" *="" *="" optional.="" the="" maximum="" number="" of="" `chunk`s="" to="" return.="" *="" the="" service="" may="" return="" fewer="" `chunk`s.="" *="" if="" unspecified,="" at="" most="" 10="" `chunk`s="" will="" be="" returned.="" *="" the="" maximum="" specified="" result="" count="" is="" 100.="" */="" const="" resultscount="1234" imports="" the="" generativelanguage="" library="" const="" {retrieverserviceclient}="require('@google-ai/generativelanguage').v1alpha;" instantiates="" a="" client="" const="" generativelanguageclient="new" retrieverserviceclient();="" async="" function="" callquerycorpus()="" {="" construct="" request="" const="" request="{" name,="" query,="" };="" run="" request="" const="" response="await" generativelanguageclient.querycorpus(request);="" console.log(response);="" }="" callquerycorpus();="">

### queryCorpus(request, options, callback)
    
    
    queryCorpus(request: protos.google.ai.generativelanguage.v1alpha.IQueryCorpusRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IQueryCorpusResponse, protos.google.ai.generativelanguage.v1alpha.IQueryCorpusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IQueryCorpusResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusresponse), [protos.google.ai.generativelanguage.v1alpha.IQueryCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryCorpus(request, callback)
    
    
    queryCorpus(request: protos.google.ai.generativelanguage.v1alpha.IQueryCorpusRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IQueryCorpusResponse, protos.google.ai.generativelanguage.v1alpha.IQueryCorpusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IQueryCorpusResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusresponse), [protos.google.ai.generativelanguage.v1alpha.IQueryCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryDocument(request, options)
    
    
    queryDocument(request?: protos.google.ai.generativelanguage.v1alpha.IQueryDocumentRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IQueryDocumentResponse,
            (protos.google.ai.generativelanguage.v1alpha.IQueryDocumentRequest | undefined),
            {} | undefined
        ]>;

Performs semantic search over a `Document`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IQueryDocumentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentresponse), ([protos.google.ai.generativelanguage.v1alpha.IQueryDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [QueryDocumentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.querydocumentresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `Document` to query.
       *  Example: `corpora/my-corpus-123/documents/the-doc-abc`
       */
      // const name = 'abc123'
      /**
       *  Required. Query string to perform semantic search.
       */
      // const query = 'abc123'
      /**
       *  Optional. The maximum number of `Chunk`s to return.
       *  The service may return fewer `Chunk`s.
       *  If unspecified, at most 10 `Chunk`s will be returned.
       *  The maximum specified result count is 100.
       */
      // const resultsCount = 1234
      /**
       *  Optional. Filter for `Chunk` metadata. Each `MetadataFilter` object should
       *  correspond to a unique key. Multiple `MetadataFilter` objects are joined by
       *  logical "AND"s.
       *  Note: `Document`-level filtering is not supported for this request because
       *  a `Document` name is already specified.
       *  Example query:
       *  (year >= 2020 OR year < 2010)="" and="" (genre="drama" or="" genre="action)" *="" `metadatafilter`="" object="" list:="" *="" metadata_filters="*" {key="chunk.custom_metadata.year" *="" conditions="{int_value" =="" 2020,="" operation="GREATER_EQUAL}," *="" {int_value="2010," operation="LESS}}," *="" {key="chunk.custom_metadata.genre" *="" conditions="{string_value" =="" "drama",="" operation="EQUAL}," *="" {string_value="action" ,="" operation="EQUAL}}" *="" example="" query="" for="" a="" numeric="" range="" of="" values:="" *="" (year=""> 2015 AND year <= 2020)="" *="" `metadatafilter`="" object="" list:="" *="" metadata_filters="*" {key="chunk.custom_metadata.year" *="" conditions="{int_value" =="" 2015,="" operation="GREATER}" },="" *="" {key="chunk.custom_metadata.year" *="" conditions="{int_value" =="" 2020,="" operation="LESS_EQUAL}" }="" *="" note:="" "and"s="" for="" the="" same="" key="" are="" only="" supported="" for="" numeric="" values.="" string="" *="" values="" only="" support="" "or"s="" for="" the="" same="" key.="" */="" const="" metadatafilters="[1,2,3,4]" imports="" the="" generativelanguage="" library="" const="" {retrieverserviceclient}="require('@google-ai/generativelanguage').v1alpha;" instantiates="" a="" client="" const="" generativelanguageclient="new" retrieverserviceclient();="" async="" function="" callquerydocument()="" {="" construct="" request="" const="" request="{" name,="" query,="" };="" run="" request="" const="" response="await" generativelanguageclient.querydocument(request);="" console.log(response);="" }="" callquerydocument();="">

### queryDocument(request, options, callback)
    
    
    queryDocument(request: protos.google.ai.generativelanguage.v1alpha.IQueryDocumentRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IQueryDocumentResponse, protos.google.ai.generativelanguage.v1alpha.IQueryDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IQueryDocumentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentresponse), [protos.google.ai.generativelanguage.v1alpha.IQueryDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryDocument(request, callback)
    
    
    queryDocument(request: protos.google.ai.generativelanguage.v1alpha.IQueryDocumentRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IQueryDocumentResponse, protos.google.ai.generativelanguage.v1alpha.IQueryDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IQueryDocumentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentresponse), [protos.google.ai.generativelanguage.v1alpha.IQueryDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### updateChunk(request, options)
    
    
    updateChunk(request?: protos.google.ai.generativelanguage.v1alpha.IUpdateChunkRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IChunk,
            (protos.google.ai.generativelanguage.v1alpha.IUpdateChunkRequest | undefined),
            {} | undefined
        ]>;

Updates a `Chunk`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatechunkrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk), ([protos.google.ai.generativelanguage.v1alpha.IUpdateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatechunkrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The `Chunk` to update.
       */
      // const chunk = {}
      /**
       *  Required. The list of fields to update.
       *  Currently, this only supports updating `custom_metadata` and `data`.
       */
      // const updateMask = {}
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callUpdateChunk() {
        // Construct request
        const request = {
          chunk,
          updateMask,
        };
    
        // Run request
        const response = await generativelanguageClient.updateChunk(request);
        console.log(response);
      }
    
      callUpdateChunk();
    
    

### updateChunk(request, options, callback)
    
    
    updateChunk(request: protos.google.ai.generativelanguage.v1alpha.IUpdateChunkRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IChunk, protos.google.ai.generativelanguage.v1alpha.IUpdateChunkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatechunkrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk), [protos.google.ai.generativelanguage.v1alpha.IUpdateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatechunkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateChunk(request, callback)
    
    
    updateChunk(request: protos.google.ai.generativelanguage.v1alpha.IUpdateChunkRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IChunk, protos.google.ai.generativelanguage.v1alpha.IUpdateChunkRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatechunkrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IChunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ichunk), [protos.google.ai.generativelanguage.v1alpha.IUpdateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatechunkrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCorpus(request, options)
    
    
    updateCorpus(request?: protos.google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.ICorpus,
            (protos.google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest | undefined),
            {} | undefined
        ]>;

Updates a `Corpus`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatecorpusrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus), ([protos.google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatecorpusrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Corpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.corpus). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The `Corpus` to update.
       */
      // const corpus = {}
      /**
       *  Required. The list of fields to update.
       *  Currently, this only supports updating `display_name`.
       */
      // const updateMask = {}
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callUpdateCorpus() {
        // Construct request
        const request = {
          corpus,
          updateMask,
        };
    
        // Run request
        const response = await generativelanguageClient.updateCorpus(request);
        console.log(response);
      }
    
      callUpdateCorpus();
    
    

### updateCorpus(request, options, callback)
    
    
    updateCorpus(request: protos.google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ICorpus, protos.google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatecorpusrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus), [protos.google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatecorpusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCorpus(request, callback)
    
    
    updateCorpus(request: protos.google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.ICorpus, protos.google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatecorpusrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.ICorpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icorpus), [protos.google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatecorpusrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDocument(request, options)
    
    
    updateDocument(request?: protos.google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1alpha.IDocument,
            (protos.google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest | undefined),
            {} | undefined
        ]>;

Updates a `Document`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatedocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument), ([protos.google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatedocumentrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Document](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.document). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The `Document` to update.
       */
      // const document = {}
      /**
       *  Required. The list of fields to update.
       *  Currently, this only supports updating `display_name` and
       *  `custom_metadata`.
       */
      // const updateMask = {}
    
      // Imports the Generativelanguage library
      const {RetrieverServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const generativelanguageClient = new [RetrieverServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callUpdateDocument() {
        // Construct request
        const request = {
          document,
          updateMask,
        };
    
        // Run request
        const response = await generativelanguageClient.updateDocument(request);
        console.log(response);
      }
    
      callUpdateDocument();
    
    

### updateDocument(request, options, callback)
    
    
    updateDocument(request: protos.google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IDocument, protos.google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatedocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument), [protos.google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDocument(request, callback)
    
    
    updateDocument(request: protos.google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest, callback: Callback<protos.google.ai.generativelanguage.v1alpha.IDocument, protos.google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatedocumentrequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1alpha.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.idocument), [protos.google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
