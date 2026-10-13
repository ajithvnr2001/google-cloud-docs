---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/v2beta1.knowledgebasesclient
title: Class v2beta1.KnowledgeBasesClient (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:58:45.799016+00:00
---

# Class v2beta1.KnowledgeBasesClient (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/v2beta1.knowledgebasesclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v2beta1.KnowledgeBasesClient (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Service for managing [KnowledgeBases](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.knowledgebase). v2beta1

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of KnowledgeBasesClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new KnowledgeBasesClient({fallback: true}, gax); ```  
  
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

### knowledgeBasesStub
    
    
    knowledgeBasesStub?: Promise<{
            [name: string]: Function;
        }>;

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

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createKnowledgeBase(request, options)
    
    
    createKnowledgeBase(request?: protos.google.cloud.dialogflow.v2beta1.ICreateKnowledgeBaseRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase,
            (protos.google.cloud.dialogflow.v2beta1.ICreateKnowledgeBaseRequest | undefined),
            {} | undefined
        ]>;

Creates a knowledge base.

Note: The `projects.agent.knowledgeBases` resource is deprecated; only use `projects.knowledgeBases`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.icreateknowledgebaserequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase), ([protos.google.cloud.dialogflow.v2beta1.ICreateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.icreateknowledgebaserequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [KnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.knowledgebase). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project to create a knowledge base for.
       *  Format: `projects/

### createKnowledgeBase(request, options, callback)
    
    
    createKnowledgeBase(request: protos.google.cloud.dialogflow.v2beta1.ICreateKnowledgeBaseRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase, protos.google.cloud.dialogflow.v2beta1.ICreateKnowledgeBaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.icreateknowledgebaserequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase), [protos.google.cloud.dialogflow.v2beta1.ICreateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.icreateknowledgebaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createKnowledgeBase(request, callback)
    
    
    createKnowledgeBase(request: protos.google.cloud.dialogflow.v2beta1.ICreateKnowledgeBaseRequest, callback: Callback<protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase, protos.google.cloud.dialogflow.v2beta1.ICreateKnowledgeBaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.icreateknowledgebaserequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase), [protos.google.cloud.dialogflow.v2beta1.ICreateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.icreateknowledgebaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteKnowledgeBase(request, options)
    
    
    deleteKnowledgeBase(request?: protos.google.cloud.dialogflow.v2beta1.IDeleteKnowledgeBaseRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.cloud.dialogflow.v2beta1.IDeleteKnowledgeBaseRequest | undefined),
            {} | undefined
        ]>;

Deletes the specified knowledge base.

Note: The `projects.agent.knowledgeBases` resource is deprecated; only use `projects.knowledgeBases`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ideleteknowledgebaserequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.iempty), ([protos.google.cloud.dialogflow.v2beta1.IDeleteKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ideleteknowledgebaserequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the knowledge base to delete.
       *  Format: `projects/

### deleteKnowledgeBase(request, options, callback)
    
    
    deleteKnowledgeBase(request: protos.google.cloud.dialogflow.v2beta1.IDeleteKnowledgeBaseRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dialogflow.v2beta1.IDeleteKnowledgeBaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ideleteknowledgebaserequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.iempty), [protos.google.cloud.dialogflow.v2beta1.IDeleteKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ideleteknowledgebaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteKnowledgeBase(request, callback)
    
    
    deleteKnowledgeBase(request: protos.google.cloud.dialogflow.v2beta1.IDeleteKnowledgeBaseRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.dialogflow.v2beta1.IDeleteKnowledgeBaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ideleteknowledgebaserequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.iempty), [protos.google.cloud.dialogflow.v2beta1.IDeleteKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ideleteknowledgebaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### encryptionSpecPath(project, location)
    
    
    encryptionSpecPath(project: string, location: string): string;

Return a fully-qualified encryptionSpec resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### generatorEvaluationPath(project, location, generator, evaluation)
    
    
    generatorEvaluationPath(project: string, location: string, generator: string, evaluation: string): string;

Return a fully-qualified generatorEvaluation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`generator` |  `string`   
  
`evaluation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### generatorPath(project, location, generator)
    
    
    generatorPath(project: string, location: string, generator: string): string;

Return a fully-qualified generator resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`generator` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### getKnowledgeBase(request, options)
    
    
    getKnowledgeBase(request?: protos.google.cloud.dialogflow.v2beta1.IGetKnowledgeBaseRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase,
            (protos.google.cloud.dialogflow.v2beta1.IGetKnowledgeBaseRequest | undefined),
            {} | undefined
        ]>;

Retrieves the specified knowledge base.

Note: The `projects.agent.knowledgeBases` resource is deprecated; only use `projects.knowledgeBases`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.igetknowledgebaserequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase), ([protos.google.cloud.dialogflow.v2beta1.IGetKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.igetknowledgebaserequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [KnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.knowledgebase). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the knowledge base to retrieve.
       *  Format `projects/

### getKnowledgeBase(request, options, callback)
    
    
    getKnowledgeBase(request: protos.google.cloud.dialogflow.v2beta1.IGetKnowledgeBaseRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase, protos.google.cloud.dialogflow.v2beta1.IGetKnowledgeBaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.igetknowledgebaserequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase), [protos.google.cloud.dialogflow.v2beta1.IGetKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.igetknowledgebaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getKnowledgeBase(request, callback)
    
    
    getKnowledgeBase(request: protos.google.cloud.dialogflow.v2beta1.IGetKnowledgeBaseRequest, callback: Callback<protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase, protos.google.cloud.dialogflow.v2beta1.IGetKnowledgeBaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.igetknowledgebaserequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase), [protos.google.cloud.dialogflow.v2beta1.IGetKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.igetknowledgebaserequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listKnowledgeBases(request, options)
    
    
    listKnowledgeBases(request?: protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase[],
            protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest | null,
            protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesResponse
        ]>;

Returns the list of all knowledge bases of the specified agent.

Note: The `projects.agent.knowledgeBases` resource is deprecated; only use `projects.knowledgeBases`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKnowledgeBasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase)[], [protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesrequest) | null, [protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [KnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.knowledgebase). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listKnowledgeBasesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listKnowledgeBases(request, options, callback)
    
    
    listKnowledgeBases(request: protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest, protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesResponse | null | undefined, protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKnowledgeBasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesrequest), [protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesresponse) | null | undefined, [protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listKnowledgeBases(request, callback)
    
    
    listKnowledgeBases(request: protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest, callback: PaginationCallback<protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest, protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesResponse | null | undefined, protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKnowledgeBasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesrequest), [protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesresponse) | null | undefined, [protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listKnowledgeBasesAsync(request, options)
    
    
    listKnowledgeBasesAsync(request?: protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase>;

Equivalent to `listKnowledgeBases`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKnowledgeBasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [KnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.knowledgebase). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The project to list of knowledge bases for.
       *  Format: `projects/

### listKnowledgeBasesStream(request, options)
    
    
    listKnowledgeBasesStream(request?: protos.google.cloud.dialogflow.v2beta1.IListKnowledgeBasesRequest, options?: CallOptions): Transform;

Equivalent to `listKnowledgeBases`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKnowledgeBasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.ilistknowledgebasesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [KnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.knowledgebase) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listKnowledgeBasesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
    

### matchAnswerRecordFromProjectAnswerRecordName(projectAnswerRecordName)
    
    
    matchAnswerRecordFromProjectAnswerRecordName(projectAnswerRecordName: string): string | number;

Parse the answer_record from ProjectAnswerRecord resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAnswerRecordName` |  `string`   
A fully-qualified path representing project_answer_record resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer_record.  
  
### matchAnswerRecordFromProjectLocationAnswerRecordName(projectLocationAnswerRecordName)
    
    
    matchAnswerRecordFromProjectLocationAnswerRecordName(projectLocationAnswerRecordName: string): string | number;

Parse the answer_record from ProjectLocationAnswerRecord resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAnswerRecordName` |  `string`   
A fully-qualified path representing project_location_answer_record resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer_record.  
  
### matchContextFromProjectAgentEnvironmentUserSessionContextName(projectAgentEnvironmentUserSessionContextName)
    
    
    matchContextFromProjectAgentEnvironmentUserSessionContextName(projectAgentEnvironmentUserSessionContextName: string): string | number;

Parse the context from ProjectAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the context.  
  
### matchContextFromProjectAgentSessionContextName(projectAgentSessionContextName)
    
    
    matchContextFromProjectAgentSessionContextName(projectAgentSessionContextName: string): string | number;

Parse the context from ProjectAgentSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentSessionContextName` |  `string`   
A fully-qualified path representing project_agent_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the context.  
  
### matchContextFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName)
    
    
    matchContextFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName: string): string | number;

Parse the context from ProjectLocationAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the context.  
  
### matchContextFromProjectLocationAgentSessionContextName(projectLocationAgentSessionContextName)
    
    
    matchContextFromProjectLocationAgentSessionContextName(projectLocationAgentSessionContextName: string): string | number;

Parse the context from ProjectLocationAgentSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionContextName` |  `string`   
A fully-qualified path representing project_location_agent_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the context.  
  
### matchConversationFromProjectConversationMessageName(projectConversationMessageName)
    
    
    matchConversationFromProjectConversationMessageName(projectConversationMessageName: string): string | number;

Parse the conversation from ProjectConversationMessage resource.

**Parameter**  
---  
**Name** | **Description**  
`projectConversationMessageName` |  `string`   
A fully-qualified path representing project_conversation_message resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectConversationParticipantName(projectConversationParticipantName)
    
    
    matchConversationFromProjectConversationParticipantName(projectConversationParticipantName: string): string | number;

Parse the conversation from ProjectConversationParticipant resource.

**Parameter**  
---  
**Name** | **Description**  
`projectConversationParticipantName` |  `string`   
A fully-qualified path representing project_conversation_participant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectConversationsName(projectConversationsName)
    
    
    matchConversationFromProjectConversationsName(projectConversationsName: string): string | number;

Parse the conversation from ProjectConversations resource.

**Parameter**  
---  
**Name** | **Description**  
`projectConversationsName` |  `string`   
A fully-qualified path representing project_conversations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationConversationMessageName(projectLocationConversationMessageName)
    
    
    matchConversationFromProjectLocationConversationMessageName(projectLocationConversationMessageName: string): string | number;

Parse the conversation from ProjectLocationConversationMessage resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationMessageName` |  `string`   
A fully-qualified path representing project_location_conversation_message resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationConversationParticipantName(projectLocationConversationParticipantName)
    
    
    matchConversationFromProjectLocationConversationParticipantName(projectLocationConversationParticipantName: string): string | number;

Parse the conversation from ProjectLocationConversationParticipant resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationParticipantName` |  `string`   
A fully-qualified path representing project_location_conversation_participant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationConversationsName(projectLocationConversationsName)
    
    
    matchConversationFromProjectLocationConversationsName(projectLocationConversationsName: string): string | number;

Parse the conversation from ProjectLocationConversations resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationsName` |  `string`   
A fully-qualified path representing project_location_conversations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationProfileFromProjectConversationProfileName(projectConversationProfileName)
    
    
    matchConversationProfileFromProjectConversationProfileName(projectConversationProfileName: string): string | number;

Parse the conversation_profile from ProjectConversationProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`projectConversationProfileName` |  `string`   
A fully-qualified path representing project_conversation_profile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation_profile.  
  
### matchConversationProfileFromProjectLocationConversationProfileName(projectLocationConversationProfileName)
    
    
    matchConversationProfileFromProjectLocationConversationProfileName(projectLocationConversationProfileName: string): string | number;

Parse the conversation_profile from ProjectLocationConversationProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationProfileName` |  `string`   
A fully-qualified path representing project_location_conversation_profile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation_profile.  
  
### matchDocumentFromProjectKnowledgeBaseDocumentName(projectKnowledgeBaseDocumentName)
    
    
    matchDocumentFromProjectKnowledgeBaseDocumentName(projectKnowledgeBaseDocumentName: string): string | number;

Parse the document from ProjectKnowledgeBaseDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectKnowledgeBaseDocumentName` |  `string`   
A fully-qualified path representing project_knowledge_base_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationKnowledgeBaseDocumentName(projectLocationKnowledgeBaseDocumentName)
    
    
    matchDocumentFromProjectLocationKnowledgeBaseDocumentName(projectLocationKnowledgeBaseDocumentName: string): string | number;

Parse the document from ProjectLocationKnowledgeBaseDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationKnowledgeBaseDocumentName` |  `string`   
A fully-qualified path representing project_location_knowledge_base_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchEntityTypeFromProjectAgentEntityTypeName(projectAgentEntityTypeName)
    
    
    matchEntityTypeFromProjectAgentEntityTypeName(projectAgentEntityTypeName: string): string | number;

Parse the entity_type from ProjectAgentEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEntityTypeName` |  `string`   
A fully-qualified path representing project_agent_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEntityTypeFromProjectAgentEnvironmentUserSessionEntityTypeName(projectAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchEntityTypeFromProjectAgentEnvironmentUserSessionEntityTypeName(projectAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the entity_type from ProjectAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEntityTypeFromProjectAgentSessionEntityTypeName(projectAgentSessionEntityTypeName)
    
    
    matchEntityTypeFromProjectAgentSessionEntityTypeName(projectAgentSessionEntityTypeName: string): string | number;

Parse the entity_type from ProjectAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEntityTypeFromProjectLocationAgentEntityTypeName(projectLocationAgentEntityTypeName)
    
    
    matchEntityTypeFromProjectLocationAgentEntityTypeName(projectLocationAgentEntityTypeName: string): string | number;

Parse the entity_type from ProjectLocationAgentEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEntityTypeFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchEntityTypeFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the entity_type from ProjectLocationAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEntityTypeFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName)
    
    
    matchEntityTypeFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName: string): string | number;

Parse the entity_type from ProjectLocationAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the entity_type.  
  
### matchEnvironmentFromProjectAgentEnvironmentName(projectAgentEnvironmentName)
    
    
    matchEnvironmentFromProjectAgentEnvironmentName(projectAgentEnvironmentName: string): string | number;

Parse the environment from ProjectAgentEnvironment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentName` |  `string`   
A fully-qualified path representing project_agent_environment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchEnvironmentFromProjectAgentEnvironmentUserSessionContextName(projectAgentEnvironmentUserSessionContextName)
    
    
    matchEnvironmentFromProjectAgentEnvironmentUserSessionContextName(projectAgentEnvironmentUserSessionContextName: string): string | number;

Parse the environment from ProjectAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchEnvironmentFromProjectAgentEnvironmentUserSessionEntityTypeName(projectAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchEnvironmentFromProjectAgentEnvironmentUserSessionEntityTypeName(projectAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the environment from ProjectAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchEnvironmentFromProjectLocationAgentEnvironmentName(projectLocationAgentEnvironmentName)
    
    
    matchEnvironmentFromProjectLocationAgentEnvironmentName(projectLocationAgentEnvironmentName: string): string | number;

Parse the environment from ProjectLocationAgentEnvironment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentName` |  `string`   
A fully-qualified path representing project_location_agent_environment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchEnvironmentFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName)
    
    
    matchEnvironmentFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName: string): string | number;

Parse the environment from ProjectLocationAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchEnvironmentFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchEnvironmentFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the environment from ProjectLocationAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the environment.  
  
### matchEvaluationFromGeneratorEvaluationName(generatorEvaluationName)
    
    
    matchEvaluationFromGeneratorEvaluationName(generatorEvaluationName: string): string | number;

Parse the evaluation from GeneratorEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorEvaluationName` |  `string`   
A fully-qualified path representing GeneratorEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation.  
  
### matchGeneratorFromGeneratorEvaluationName(generatorEvaluationName)
    
    
    matchGeneratorFromGeneratorEvaluationName(generatorEvaluationName: string): string | number;

Parse the generator from GeneratorEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorEvaluationName` |  `string`   
A fully-qualified path representing GeneratorEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the generator.  
  
### matchGeneratorFromGeneratorName(generatorName)
    
    
    matchGeneratorFromGeneratorName(generatorName: string): string | number;

Parse the generator from Generator resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorName` |  `string`   
A fully-qualified path representing Generator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the generator.  
  
### matchIntentFromProjectAgentIntentName(projectAgentIntentName)
    
    
    matchIntentFromProjectAgentIntentName(projectAgentIntentName: string): string | number;

Parse the intent from ProjectAgentIntent resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentIntentName` |  `string`   
A fully-qualified path representing project_agent_intent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the intent.  
  
### matchIntentFromProjectLocationAgentIntentName(projectLocationAgentIntentName)
    
    
    matchIntentFromProjectLocationAgentIntentName(projectLocationAgentIntentName: string): string | number;

Parse the intent from ProjectLocationAgentIntent resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentIntentName` |  `string`   
A fully-qualified path representing project_location_agent_intent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the intent.  
  
### matchKnowledgeBaseFromProjectKnowledgeBaseDocumentName(projectKnowledgeBaseDocumentName)
    
    
    matchKnowledgeBaseFromProjectKnowledgeBaseDocumentName(projectKnowledgeBaseDocumentName: string): string | number;

Parse the knowledge_base from ProjectKnowledgeBaseDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectKnowledgeBaseDocumentName` |  `string`   
A fully-qualified path representing project_knowledge_base_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the knowledge_base.  
  
### matchKnowledgeBaseFromProjectKnowledgeBaseName(projectKnowledgeBaseName)
    
    
    matchKnowledgeBaseFromProjectKnowledgeBaseName(projectKnowledgeBaseName: string): string | number;

Parse the knowledge_base from ProjectKnowledgeBase resource.

**Parameter**  
---  
**Name** | **Description**  
`projectKnowledgeBaseName` |  `string`   
A fully-qualified path representing project_knowledge_base resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the knowledge_base.  
  
### matchKnowledgeBaseFromProjectLocationKnowledgeBaseDocumentName(projectLocationKnowledgeBaseDocumentName)
    
    
    matchKnowledgeBaseFromProjectLocationKnowledgeBaseDocumentName(projectLocationKnowledgeBaseDocumentName: string): string | number;

Parse the knowledge_base from ProjectLocationKnowledgeBaseDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationKnowledgeBaseDocumentName` |  `string`   
A fully-qualified path representing project_location_knowledge_base_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the knowledge_base.  
  
### matchKnowledgeBaseFromProjectLocationKnowledgeBaseName(projectLocationKnowledgeBaseName)
    
    
    matchKnowledgeBaseFromProjectLocationKnowledgeBaseName(projectLocationKnowledgeBaseName: string): string | number;

Parse the knowledge_base from ProjectLocationKnowledgeBase resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationKnowledgeBaseName` |  `string`   
A fully-qualified path representing project_location_knowledge_base resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the knowledge_base.  
  
### matchLocationFromEncryptionSpecName(encryptionSpecName)
    
    
    matchLocationFromEncryptionSpecName(encryptionSpecName: string): string | number;

Parse the location from EncryptionSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`encryptionSpecName` |  `string`   
A fully-qualified path representing EncryptionSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromGeneratorEvaluationName(generatorEvaluationName)
    
    
    matchLocationFromGeneratorEvaluationName(generatorEvaluationName: string): string | number;

Parse the location from GeneratorEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorEvaluationName` |  `string`   
A fully-qualified path representing GeneratorEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromGeneratorName(generatorName)
    
    
    matchLocationFromGeneratorName(generatorName: string): string | number;

Parse the location from Generator resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorName` |  `string`   
A fully-qualified path representing Generator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentEntityTypeName(projectLocationAgentEntityTypeName)
    
    
    matchLocationFromProjectLocationAgentEntityTypeName(projectLocationAgentEntityTypeName: string): string | number;

Parse the location from ProjectLocationAgentEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentEnvironmentName(projectLocationAgentEnvironmentName)
    
    
    matchLocationFromProjectLocationAgentEnvironmentName(projectLocationAgentEnvironmentName: string): string | number;

Parse the location from ProjectLocationAgentEnvironment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentName` |  `string`   
A fully-qualified path representing project_location_agent_environment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName)
    
    
    matchLocationFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName: string): string | number;

Parse the location from ProjectLocationAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchLocationFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the location from ProjectLocationAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentFulfillmentName(projectLocationAgentFulfillmentName)
    
    
    matchLocationFromProjectLocationAgentFulfillmentName(projectLocationAgentFulfillmentName: string): string | number;

Parse the location from ProjectLocationAgentFulfillment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentFulfillmentName` |  `string`   
A fully-qualified path representing project_location_agent_fulfillment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentIntentName(projectLocationAgentIntentName)
    
    
    matchLocationFromProjectLocationAgentIntentName(projectLocationAgentIntentName: string): string | number;

Parse the location from ProjectLocationAgentIntent resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentIntentName` |  `string`   
A fully-qualified path representing project_location_agent_intent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentName(projectLocationAgentName)
    
    
    matchLocationFromProjectLocationAgentName(projectLocationAgentName: string): string | number;

Parse the location from ProjectLocationAgent resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentName` |  `string`   
A fully-qualified path representing project_location_agent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentSessionContextName(projectLocationAgentSessionContextName)
    
    
    matchLocationFromProjectLocationAgentSessionContextName(projectLocationAgentSessionContextName: string): string | number;

Parse the location from ProjectLocationAgentSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionContextName` |  `string`   
A fully-qualified path representing project_location_agent_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName)
    
    
    matchLocationFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName: string): string | number;

Parse the location from ProjectLocationAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAgentVersionName(projectLocationAgentVersionName)
    
    
    matchLocationFromProjectLocationAgentVersionName(projectLocationAgentVersionName: string): string | number;

Parse the location from ProjectLocationAgentVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentVersionName` |  `string`   
A fully-qualified path representing project_location_agent_version resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationAnswerRecordName(projectLocationAnswerRecordName)
    
    
    matchLocationFromProjectLocationAnswerRecordName(projectLocationAnswerRecordName: string): string | number;

Parse the location from ProjectLocationAnswerRecord resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAnswerRecordName` |  `string`   
A fully-qualified path representing project_location_answer_record resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationConversationMessageName(projectLocationConversationMessageName)
    
    
    matchLocationFromProjectLocationConversationMessageName(projectLocationConversationMessageName: string): string | number;

Parse the location from ProjectLocationConversationMessage resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationMessageName` |  `string`   
A fully-qualified path representing project_location_conversation_message resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationConversationParticipantName(projectLocationConversationParticipantName)
    
    
    matchLocationFromProjectLocationConversationParticipantName(projectLocationConversationParticipantName: string): string | number;

Parse the location from ProjectLocationConversationParticipant resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationParticipantName` |  `string`   
A fully-qualified path representing project_location_conversation_participant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationConversationProfileName(projectLocationConversationProfileName)
    
    
    matchLocationFromProjectLocationConversationProfileName(projectLocationConversationProfileName: string): string | number;

Parse the location from ProjectLocationConversationProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationProfileName` |  `string`   
A fully-qualified path representing project_location_conversation_profile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationConversationsName(projectLocationConversationsName)
    
    
    matchLocationFromProjectLocationConversationsName(projectLocationConversationsName: string): string | number;

Parse the location from ProjectLocationConversations resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationsName` |  `string`   
A fully-qualified path representing project_location_conversations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationKnowledgeBaseDocumentName(projectLocationKnowledgeBaseDocumentName)
    
    
    matchLocationFromProjectLocationKnowledgeBaseDocumentName(projectLocationKnowledgeBaseDocumentName: string): string | number;

Parse the location from ProjectLocationKnowledgeBaseDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationKnowledgeBaseDocumentName` |  `string`   
A fully-qualified path representing project_location_knowledge_base_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationKnowledgeBaseName(projectLocationKnowledgeBaseName)
    
    
    matchLocationFromProjectLocationKnowledgeBaseName(projectLocationKnowledgeBaseName: string): string | number;

Parse the location from ProjectLocationKnowledgeBase resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationKnowledgeBaseName` |  `string`   
A fully-qualified path representing project_location_knowledge_base resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationPhoneNumberName(projectLocationPhoneNumberName)
    
    
    matchLocationFromProjectLocationPhoneNumberName(projectLocationPhoneNumberName: string): string | number;

Parse the location from ProjectLocationPhoneNumber resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPhoneNumberName` |  `string`   
A fully-qualified path representing project_location_phone_number resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSipTrunkName(sipTrunkName)
    
    
    matchLocationFromSipTrunkName(sipTrunkName: string): string | number;

Parse the location from SipTrunk resource.

**Parameter**  
---  
**Name** | **Description**  
`sipTrunkName` |  `string`   
A fully-qualified path representing SipTrunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromToolName(toolName)
    
    
    matchLocationFromToolName(toolName: string): string | number;

Parse the location from Tool resource.

**Parameter**  
---  
**Name** | **Description**  
`toolName` |  `string`   
A fully-qualified path representing Tool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMessageFromProjectConversationMessageName(projectConversationMessageName)
    
    
    matchMessageFromProjectConversationMessageName(projectConversationMessageName: string): string | number;

Parse the message from ProjectConversationMessage resource.

**Parameter**  
---  
**Name** | **Description**  
`projectConversationMessageName` |  `string`   
A fully-qualified path representing project_conversation_message resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the message.  
  
### matchMessageFromProjectLocationConversationMessageName(projectLocationConversationMessageName)
    
    
    matchMessageFromProjectLocationConversationMessageName(projectLocationConversationMessageName: string): string | number;

Parse the message from ProjectLocationConversationMessage resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationMessageName` |  `string`   
A fully-qualified path representing project_location_conversation_message resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the message.  
  
### matchParticipantFromProjectConversationParticipantName(projectConversationParticipantName)
    
    
    matchParticipantFromProjectConversationParticipantName(projectConversationParticipantName: string): string | number;

Parse the participant from ProjectConversationParticipant resource.

**Parameter**  
---  
**Name** | **Description**  
`projectConversationParticipantName` |  `string`   
A fully-qualified path representing project_conversation_participant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the participant.  
  
### matchParticipantFromProjectLocationConversationParticipantName(projectLocationConversationParticipantName)
    
    
    matchParticipantFromProjectLocationConversationParticipantName(projectLocationConversationParticipantName: string): string | number;

Parse the participant from ProjectLocationConversationParticipant resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationParticipantName` |  `string`   
A fully-qualified path representing project_location_conversation_participant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the participant.  
  
### matchPhoneNumberFromProjectLocationPhoneNumberName(projectLocationPhoneNumberName)
    
    
    matchPhoneNumberFromProjectLocationPhoneNumberName(projectLocationPhoneNumberName: string): string | number;

Parse the phone_number from ProjectLocationPhoneNumber resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPhoneNumberName` |  `string`   
A fully-qualified path representing project_location_phone_number resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the phone_number.  
  
### matchPhoneNumberFromProjectPhoneNumberName(projectPhoneNumberName)
    
    
    matchPhoneNumberFromProjectPhoneNumberName(projectPhoneNumberName: string): string | number;

Parse the phone_number from ProjectPhoneNumber resource.

**Parameter**  
---  
**Name** | **Description**  
`projectPhoneNumberName` |  `string`   
A fully-qualified path representing project_phone_number resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the phone_number.  
  
### matchProjectFromEncryptionSpecName(encryptionSpecName)
    
    
    matchProjectFromEncryptionSpecName(encryptionSpecName: string): string | number;

Parse the project from EncryptionSpec resource.

**Parameter**  
---  
**Name** | **Description**  
`encryptionSpecName` |  `string`   
A fully-qualified path representing EncryptionSpec resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromGeneratorEvaluationName(generatorEvaluationName)
    
    
    matchProjectFromGeneratorEvaluationName(generatorEvaluationName: string): string | number;

Parse the project from GeneratorEvaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorEvaluationName` |  `string`   
A fully-qualified path representing GeneratorEvaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromGeneratorName(generatorName)
    
    
    matchProjectFromGeneratorName(generatorName: string): string | number;

Parse the project from Generator resource.

**Parameter**  
---  
**Name** | **Description**  
`generatorName` |  `string`   
A fully-qualified path representing Generator resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAgentEntityTypeName(projectAgentEntityTypeName)
    
    
    matchProjectFromProjectAgentEntityTypeName(projectAgentEntityTypeName: string): string | number;

Parse the project from ProjectAgentEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEntityTypeName` |  `string`   
A fully-qualified path representing project_agent_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAgentEnvironmentName(projectAgentEnvironmentName)
    
    
    matchProjectFromProjectAgentEnvironmentName(projectAgentEnvironmentName: string): string | number;

Parse the project from ProjectAgentEnvironment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentName` |  `string`   
A fully-qualified path representing project_agent_environment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAgentEnvironmentUserSessionContextName(projectAgentEnvironmentUserSessionContextName)
    
    
    matchProjectFromProjectAgentEnvironmentUserSessionContextName(projectAgentEnvironmentUserSessionContextName: string): string | number;

Parse the project from ProjectAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAgentEnvironmentUserSessionEntityTypeName(projectAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchProjectFromProjectAgentEnvironmentUserSessionEntityTypeName(projectAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the project from ProjectAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAgentFulfillmentName(projectAgentFulfillmentName)
    
    
    matchProjectFromProjectAgentFulfillmentName(projectAgentFulfillmentName: string): string | number;

Parse the project from ProjectAgentFulfillment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentFulfillmentName` |  `string`   
A fully-qualified path representing project_agent_fulfillment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAgentIntentName(projectAgentIntentName)
    
    
    matchProjectFromProjectAgentIntentName(projectAgentIntentName: string): string | number;

Parse the project from ProjectAgentIntent resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentIntentName` |  `string`   
A fully-qualified path representing project_agent_intent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAgentName(projectAgentName)
    
    
    matchProjectFromProjectAgentName(projectAgentName: string): string | number;

Parse the project from ProjectAgent resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentName` |  `string`   
A fully-qualified path representing project_agent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAgentSessionContextName(projectAgentSessionContextName)
    
    
    matchProjectFromProjectAgentSessionContextName(projectAgentSessionContextName: string): string | number;

Parse the project from ProjectAgentSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentSessionContextName` |  `string`   
A fully-qualified path representing project_agent_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAgentSessionEntityTypeName(projectAgentSessionEntityTypeName)
    
    
    matchProjectFromProjectAgentSessionEntityTypeName(projectAgentSessionEntityTypeName: string): string | number;

Parse the project from ProjectAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAgentVersionName(projectAgentVersionName)
    
    
    matchProjectFromProjectAgentVersionName(projectAgentVersionName: string): string | number;

Parse the project from ProjectAgentVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentVersionName` |  `string`   
A fully-qualified path representing project_agent_version resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectAnswerRecordName(projectAnswerRecordName)
    
    
    matchProjectFromProjectAnswerRecordName(projectAnswerRecordName: string): string | number;

Parse the project from ProjectAnswerRecord resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAnswerRecordName` |  `string`   
A fully-qualified path representing project_answer_record resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectConversationMessageName(projectConversationMessageName)
    
    
    matchProjectFromProjectConversationMessageName(projectConversationMessageName: string): string | number;

Parse the project from ProjectConversationMessage resource.

**Parameter**  
---  
**Name** | **Description**  
`projectConversationMessageName` |  `string`   
A fully-qualified path representing project_conversation_message resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectConversationParticipantName(projectConversationParticipantName)
    
    
    matchProjectFromProjectConversationParticipantName(projectConversationParticipantName: string): string | number;

Parse the project from ProjectConversationParticipant resource.

**Parameter**  
---  
**Name** | **Description**  
`projectConversationParticipantName` |  `string`   
A fully-qualified path representing project_conversation_participant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectConversationProfileName(projectConversationProfileName)
    
    
    matchProjectFromProjectConversationProfileName(projectConversationProfileName: string): string | number;

Parse the project from ProjectConversationProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`projectConversationProfileName` |  `string`   
A fully-qualified path representing project_conversation_profile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectConversationsName(projectConversationsName)
    
    
    matchProjectFromProjectConversationsName(projectConversationsName: string): string | number;

Parse the project from ProjectConversations resource.

**Parameter**  
---  
**Name** | **Description**  
`projectConversationsName` |  `string`   
A fully-qualified path representing project_conversations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectKnowledgeBaseDocumentName(projectKnowledgeBaseDocumentName)
    
    
    matchProjectFromProjectKnowledgeBaseDocumentName(projectKnowledgeBaseDocumentName: string): string | number;

Parse the project from ProjectKnowledgeBaseDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectKnowledgeBaseDocumentName` |  `string`   
A fully-qualified path representing project_knowledge_base_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectKnowledgeBaseName(projectKnowledgeBaseName)
    
    
    matchProjectFromProjectKnowledgeBaseName(projectKnowledgeBaseName: string): string | number;

Parse the project from ProjectKnowledgeBase resource.

**Parameter**  
---  
**Name** | **Description**  
`projectKnowledgeBaseName` |  `string`   
A fully-qualified path representing project_knowledge_base resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentEntityTypeName(projectLocationAgentEntityTypeName)
    
    
    matchProjectFromProjectLocationAgentEntityTypeName(projectLocationAgentEntityTypeName: string): string | number;

Parse the project from ProjectLocationAgentEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentEnvironmentName(projectLocationAgentEnvironmentName)
    
    
    matchProjectFromProjectLocationAgentEnvironmentName(projectLocationAgentEnvironmentName: string): string | number;

Parse the project from ProjectLocationAgentEnvironment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentName` |  `string`   
A fully-qualified path representing project_location_agent_environment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName)
    
    
    matchProjectFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName: string): string | number;

Parse the project from ProjectLocationAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchProjectFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the project from ProjectLocationAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentFulfillmentName(projectLocationAgentFulfillmentName)
    
    
    matchProjectFromProjectLocationAgentFulfillmentName(projectLocationAgentFulfillmentName: string): string | number;

Parse the project from ProjectLocationAgentFulfillment resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentFulfillmentName` |  `string`   
A fully-qualified path representing project_location_agent_fulfillment resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentIntentName(projectLocationAgentIntentName)
    
    
    matchProjectFromProjectLocationAgentIntentName(projectLocationAgentIntentName: string): string | number;

Parse the project from ProjectLocationAgentIntent resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentIntentName` |  `string`   
A fully-qualified path representing project_location_agent_intent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentName(projectLocationAgentName)
    
    
    matchProjectFromProjectLocationAgentName(projectLocationAgentName: string): string | number;

Parse the project from ProjectLocationAgent resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentName` |  `string`   
A fully-qualified path representing project_location_agent resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentSessionContextName(projectLocationAgentSessionContextName)
    
    
    matchProjectFromProjectLocationAgentSessionContextName(projectLocationAgentSessionContextName: string): string | number;

Parse the project from ProjectLocationAgentSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionContextName` |  `string`   
A fully-qualified path representing project_location_agent_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName)
    
    
    matchProjectFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName: string): string | number;

Parse the project from ProjectLocationAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAgentVersionName(projectLocationAgentVersionName)
    
    
    matchProjectFromProjectLocationAgentVersionName(projectLocationAgentVersionName: string): string | number;

Parse the project from ProjectLocationAgentVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentVersionName` |  `string`   
A fully-qualified path representing project_location_agent_version resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationAnswerRecordName(projectLocationAnswerRecordName)
    
    
    matchProjectFromProjectLocationAnswerRecordName(projectLocationAnswerRecordName: string): string | number;

Parse the project from ProjectLocationAnswerRecord resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAnswerRecordName` |  `string`   
A fully-qualified path representing project_location_answer_record resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationConversationMessageName(projectLocationConversationMessageName)
    
    
    matchProjectFromProjectLocationConversationMessageName(projectLocationConversationMessageName: string): string | number;

Parse the project from ProjectLocationConversationMessage resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationMessageName` |  `string`   
A fully-qualified path representing project_location_conversation_message resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationConversationParticipantName(projectLocationConversationParticipantName)
    
    
    matchProjectFromProjectLocationConversationParticipantName(projectLocationConversationParticipantName: string): string | number;

Parse the project from ProjectLocationConversationParticipant resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationParticipantName` |  `string`   
A fully-qualified path representing project_location_conversation_participant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationConversationProfileName(projectLocationConversationProfileName)
    
    
    matchProjectFromProjectLocationConversationProfileName(projectLocationConversationProfileName: string): string | number;

Parse the project from ProjectLocationConversationProfile resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationProfileName` |  `string`   
A fully-qualified path representing project_location_conversation_profile resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationConversationsName(projectLocationConversationsName)
    
    
    matchProjectFromProjectLocationConversationsName(projectLocationConversationsName: string): string | number;

Parse the project from ProjectLocationConversations resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationConversationsName` |  `string`   
A fully-qualified path representing project_location_conversations resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationKnowledgeBaseDocumentName(projectLocationKnowledgeBaseDocumentName)
    
    
    matchProjectFromProjectLocationKnowledgeBaseDocumentName(projectLocationKnowledgeBaseDocumentName: string): string | number;

Parse the project from ProjectLocationKnowledgeBaseDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationKnowledgeBaseDocumentName` |  `string`   
A fully-qualified path representing project_location_knowledge_base_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationKnowledgeBaseName(projectLocationKnowledgeBaseName)
    
    
    matchProjectFromProjectLocationKnowledgeBaseName(projectLocationKnowledgeBaseName: string): string | number;

Parse the project from ProjectLocationKnowledgeBase resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationKnowledgeBaseName` |  `string`   
A fully-qualified path representing project_location_knowledge_base resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationPhoneNumberName(projectLocationPhoneNumberName)
    
    
    matchProjectFromProjectLocationPhoneNumberName(projectLocationPhoneNumberName: string): string | number;

Parse the project from ProjectLocationPhoneNumber resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationPhoneNumberName` |  `string`   
A fully-qualified path representing project_location_phone_number resource.  
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
  
### matchProjectFromProjectPhoneNumberName(projectPhoneNumberName)
    
    
    matchProjectFromProjectPhoneNumberName(projectPhoneNumberName: string): string | number;

Parse the project from ProjectPhoneNumber resource.

**Parameter**  
---  
**Name** | **Description**  
`projectPhoneNumberName` |  `string`   
A fully-qualified path representing project_phone_number resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSipTrunkName(sipTrunkName)
    
    
    matchProjectFromSipTrunkName(sipTrunkName: string): string | number;

Parse the project from SipTrunk resource.

**Parameter**  
---  
**Name** | **Description**  
`sipTrunkName` |  `string`   
A fully-qualified path representing SipTrunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromToolName(toolName)
    
    
    matchProjectFromToolName(toolName: string): string | number;

Parse the project from Tool resource.

**Parameter**  
---  
**Name** | **Description**  
`toolName` |  `string`   
A fully-qualified path representing Tool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchSessionFromProjectAgentEnvironmentUserSessionContextName(projectAgentEnvironmentUserSessionContextName)
    
    
    matchSessionFromProjectAgentEnvironmentUserSessionContextName(projectAgentEnvironmentUserSessionContextName: string): string | number;

Parse the session from ProjectAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectAgentEnvironmentUserSessionEntityTypeName(projectAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchSessionFromProjectAgentEnvironmentUserSessionEntityTypeName(projectAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the session from ProjectAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectAgentSessionContextName(projectAgentSessionContextName)
    
    
    matchSessionFromProjectAgentSessionContextName(projectAgentSessionContextName: string): string | number;

Parse the session from ProjectAgentSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentSessionContextName` |  `string`   
A fully-qualified path representing project_agent_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectAgentSessionEntityTypeName(projectAgentSessionEntityTypeName)
    
    
    matchSessionFromProjectAgentSessionEntityTypeName(projectAgentSessionEntityTypeName: string): string | number;

Parse the session from ProjectAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName)
    
    
    matchSessionFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName: string): string | number;

Parse the session from ProjectLocationAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchSessionFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the session from ProjectLocationAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationAgentSessionContextName(projectLocationAgentSessionContextName)
    
    
    matchSessionFromProjectLocationAgentSessionContextName(projectLocationAgentSessionContextName: string): string | number;

Parse the session from ProjectLocationAgentSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionContextName` |  `string`   
A fully-qualified path representing project_location_agent_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName)
    
    
    matchSessionFromProjectLocationAgentSessionEntityTypeName(projectLocationAgentSessionEntityTypeName: string): string | number;

Parse the session from ProjectLocationAgentSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSiptrunkFromSipTrunkName(sipTrunkName)
    
    
    matchSiptrunkFromSipTrunkName(sipTrunkName: string): string | number;

Parse the siptrunk from SipTrunk resource.

**Parameter**  
---  
**Name** | **Description**  
`sipTrunkName` |  `string`   
A fully-qualified path representing SipTrunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the siptrunk.  
  
### matchToolFromToolName(toolName)
    
    
    matchToolFromToolName(toolName: string): string | number;

Parse the tool from Tool resource.

**Parameter**  
---  
**Name** | **Description**  
`toolName` |  `string`   
A fully-qualified path representing Tool resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the tool.  
  
### matchUserFromProjectAgentEnvironmentUserSessionContextName(projectAgentEnvironmentUserSessionContextName)
    
    
    matchUserFromProjectAgentEnvironmentUserSessionContextName(projectAgentEnvironmentUserSessionContextName: string): string | number;

Parse the user from ProjectAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the user.  
  
### matchUserFromProjectAgentEnvironmentUserSessionEntityTypeName(projectAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchUserFromProjectAgentEnvironmentUserSessionEntityTypeName(projectAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the user from ProjectAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the user.  
  
### matchUserFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName)
    
    
    matchUserFromProjectLocationAgentEnvironmentUserSessionContextName(projectLocationAgentEnvironmentUserSessionContextName: string): string | number;

Parse the user from ProjectLocationAgentEnvironmentUserSessionContext resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionContextName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_context resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the user.  
  
### matchUserFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName)
    
    
    matchUserFromProjectLocationAgentEnvironmentUserSessionEntityTypeName(projectLocationAgentEnvironmentUserSessionEntityTypeName: string): string | number;

Parse the user from ProjectLocationAgentEnvironmentUserSessionEntityType resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentEnvironmentUserSessionEntityTypeName` |  `string`   
A fully-qualified path representing project_location_agent_environment_user_session_entity_type resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the user.  
  
### matchVersionFromProjectAgentVersionName(projectAgentVersionName)
    
    
    matchVersionFromProjectAgentVersionName(projectAgentVersionName: string): string | number;

Parse the version from ProjectAgentVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`projectAgentVersionName` |  `string`   
A fully-qualified path representing project_agent_version resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the version.  
  
### matchVersionFromProjectLocationAgentVersionName(projectLocationAgentVersionName)
    
    
    matchVersionFromProjectLocationAgentVersionName(projectLocationAgentVersionName: string): string | number;

Parse the version from ProjectLocationAgentVersion resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationAgentVersionName` |  `string`   
A fully-qualified path representing project_location_agent_version resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the version.  
  
### projectAgentEntityTypePath(project, entityType)
    
    
    projectAgentEntityTypePath(project: string, entityType: string): string;

Return a fully-qualified projectAgentEntityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectAgentEnvironmentPath(project, environment)
    
    
    projectAgentEnvironmentPath(project: string, environment: string): string;

Return a fully-qualified projectAgentEnvironment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`environment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectAgentEnvironmentUserSessionContextPath(project, environment, user, session, context)
    
    
    projectAgentEnvironmentUserSessionContextPath(project: string, environment: string, user: string, session: string, context: string): string;

Return a fully-qualified projectAgentEnvironmentUserSessionContext resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`environment` |  `string`   
  
`user` |  `string`   
  
`session` |  `string`   
  
`context` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectAgentEnvironmentUserSessionEntityTypePath(project, environment, user, session, entityType)
    
    
    projectAgentEnvironmentUserSessionEntityTypePath(project: string, environment: string, user: string, session: string, entityType: string): string;

Return a fully-qualified projectAgentEnvironmentUserSessionEntityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`environment` |  `string`   
  
`user` |  `string`   
  
`session` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectAgentFulfillmentPath(project)
    
    
    projectAgentFulfillmentPath(project: string): string;

Return a fully-qualified projectAgentFulfillment resource name string.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectAgentIntentPath(project, intent)
    
    
    projectAgentIntentPath(project: string, intent: string): string;

Return a fully-qualified projectAgentIntent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`intent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectAgentPath(project)
    
    
    projectAgentPath(project: string): string;

Return a fully-qualified projectAgent resource name string.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectAgentSessionContextPath(project, session, context)
    
    
    projectAgentSessionContextPath(project: string, session: string, context: string): string;

Return a fully-qualified projectAgentSessionContext resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`session` |  `string`   
  
`context` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectAgentSessionEntityTypePath(project, session, entityType)
    
    
    projectAgentSessionEntityTypePath(project: string, session: string, entityType: string): string;

Return a fully-qualified projectAgentSessionEntityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`session` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectAgentVersionPath(project, version)
    
    
    projectAgentVersionPath(project: string, version: string): string;

Return a fully-qualified projectAgentVersion resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`version` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectAnswerRecordPath(project, answerRecord)
    
    
    projectAnswerRecordPath(project: string, answerRecord: string): string;

Return a fully-qualified projectAnswerRecord resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`answerRecord` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectConversationMessagePath(project, conversation, message)
    
    
    projectConversationMessagePath(project: string, conversation: string, message: string): string;

Return a fully-qualified projectConversationMessage resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`conversation` |  `string`   
  
`message` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectConversationParticipantPath(project, conversation, participant)
    
    
    projectConversationParticipantPath(project: string, conversation: string, participant: string): string;

Return a fully-qualified projectConversationParticipant resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`conversation` |  `string`   
  
`participant` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectConversationProfilePath(project, conversationProfile)
    
    
    projectConversationProfilePath(project: string, conversationProfile: string): string;

Return a fully-qualified projectConversationProfile resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`conversationProfile` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectConversationsPath(project, conversation)
    
    
    projectConversationsPath(project: string, conversation: string): string;

Return a fully-qualified projectConversations resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectKnowledgeBaseDocumentPath(project, knowledgeBase, document)
    
    
    projectKnowledgeBaseDocumentPath(project: string, knowledgeBase: string, document: string): string;

Return a fully-qualified projectKnowledgeBaseDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`knowledgeBase` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectKnowledgeBasePath(project, knowledgeBase)
    
    
    projectKnowledgeBasePath(project: string, knowledgeBase: string): string;

Return a fully-qualified projectKnowledgeBase resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`knowledgeBase` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentEntityTypePath(project, location, entityType)
    
    
    projectLocationAgentEntityTypePath(project: string, location: string, entityType: string): string;

Return a fully-qualified projectLocationAgentEntityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentEnvironmentPath(project, location, environment)
    
    
    projectLocationAgentEnvironmentPath(project: string, location: string, environment: string): string;

Return a fully-qualified projectLocationAgentEnvironment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`environment` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentEnvironmentUserSessionContextPath(project, location, environment, user, session, context)
    
    
    projectLocationAgentEnvironmentUserSessionContextPath(project: string, location: string, environment: string, user: string, session: string, context: string): string;

Return a fully-qualified projectLocationAgentEnvironmentUserSessionContext resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`environment` |  `string`   
  
`user` |  `string`   
  
`session` |  `string`   
  
`context` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentEnvironmentUserSessionEntityTypePath(project, location, environment, user, session, entityType)
    
    
    projectLocationAgentEnvironmentUserSessionEntityTypePath(project: string, location: string, environment: string, user: string, session: string, entityType: string): string;

Return a fully-qualified projectLocationAgentEnvironmentUserSessionEntityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`environment` |  `string`   
  
`user` |  `string`   
  
`session` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentFulfillmentPath(project, location)
    
    
    projectLocationAgentFulfillmentPath(project: string, location: string): string;

Return a fully-qualified projectLocationAgentFulfillment resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentIntentPath(project, location, intent)
    
    
    projectLocationAgentIntentPath(project: string, location: string, intent: string): string;

Return a fully-qualified projectLocationAgentIntent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`intent` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentPath(project, location)
    
    
    projectLocationAgentPath(project: string, location: string): string;

Return a fully-qualified projectLocationAgent resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentSessionContextPath(project, location, session, context)
    
    
    projectLocationAgentSessionContextPath(project: string, location: string, session: string, context: string): string;

Return a fully-qualified projectLocationAgentSessionContext resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`session` |  `string`   
  
`context` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentSessionEntityTypePath(project, location, session, entityType)
    
    
    projectLocationAgentSessionEntityTypePath(project: string, location: string, session: string, entityType: string): string;

Return a fully-qualified projectLocationAgentSessionEntityType resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`session` |  `string`   
  
`entityType` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAgentVersionPath(project, location, version)
    
    
    projectLocationAgentVersionPath(project: string, location: string, version: string): string;

Return a fully-qualified projectLocationAgentVersion resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`version` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationAnswerRecordPath(project, location, answerRecord)
    
    
    projectLocationAnswerRecordPath(project: string, location: string, answerRecord: string): string;

Return a fully-qualified projectLocationAnswerRecord resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`answerRecord` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationConversationMessagePath(project, location, conversation, message)
    
    
    projectLocationConversationMessagePath(project: string, location: string, conversation: string, message: string): string;

Return a fully-qualified projectLocationConversationMessage resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`conversation` |  `string`   
  
`message` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationConversationParticipantPath(project, location, conversation, participant)
    
    
    projectLocationConversationParticipantPath(project: string, location: string, conversation: string, participant: string): string;

Return a fully-qualified projectLocationConversationParticipant resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`conversation` |  `string`   
  
`participant` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationConversationProfilePath(project, location, conversationProfile)
    
    
    projectLocationConversationProfilePath(project: string, location: string, conversationProfile: string): string;

Return a fully-qualified projectLocationConversationProfile resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`conversationProfile` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationConversationsPath(project, location, conversation)
    
    
    projectLocationConversationsPath(project: string, location: string, conversation: string): string;

Return a fully-qualified projectLocationConversations resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationKnowledgeBaseDocumentPath(project, location, knowledgeBase, document)
    
    
    projectLocationKnowledgeBaseDocumentPath(project: string, location: string, knowledgeBase: string, document: string): string;

Return a fully-qualified projectLocationKnowledgeBaseDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`knowledgeBase` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationKnowledgeBasePath(project, location, knowledgeBase)
    
    
    projectLocationKnowledgeBasePath(project: string, location: string, knowledgeBase: string): string;

Return a fully-qualified projectLocationKnowledgeBase resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`knowledgeBase` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationPhoneNumberPath(project, location, phoneNumber)
    
    
    projectLocationPhoneNumberPath(project: string, location: string, phoneNumber: string): string;

Return a fully-qualified projectLocationPhoneNumber resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`phoneNumber` |  `string`   
  
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
  
### projectPhoneNumberPath(project, phoneNumber)
    
    
    projectPhoneNumberPath(project: string, phoneNumber: string): string;

Return a fully-qualified projectPhoneNumber resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`phoneNumber` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### sipTrunkPath(project, location, siptrunk)
    
    
    sipTrunkPath(project: string, location: string, siptrunk: string): string;

Return a fully-qualified sipTrunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`siptrunk` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### toolPath(project, location, tool)
    
    
    toolPath(project: string, location: string, tool: string): string;

Return a fully-qualified tool resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`tool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateKnowledgeBase(request, options)
    
    
    updateKnowledgeBase(request?: protos.google.cloud.dialogflow.v2beta1.IUpdateKnowledgeBaseRequest, options?: CallOptions): Promise<[
            protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase,
            (protos.google.cloud.dialogflow.v2beta1.IUpdateKnowledgeBaseRequest | undefined),
            {} | undefined
        ]>;

Updates the specified knowledge base.

Note: The `projects.agent.knowledgeBases` resource is deprecated; only use `projects.knowledgeBases`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iupdateknowledgebaserequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase), ([protos.google.cloud.dialogflow.v2beta1.IUpdateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iupdateknowledgebaserequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [KnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.knowledgebase). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The knowledge base to update.
       */
      // const knowledgeBase = {}
      /**
       *  Optional. Not specified means `update all`.
       *  Currently, only `display_name` can be updated, an InvalidArgument will be
       *  returned for attempting to update other fields.
       */
      // const updateMask = {}
    
      // Imports the Dialogflow library
      const {KnowledgeBasesClient} = require('[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)').v2beta1;
    
      // Instantiates a client
      const dialogflowClient = new [KnowledgeBasesClient](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)();
    
      async function callUpdateKnowledgeBase() {
        // Construct request
        const request = {
          knowledgeBase,
        };
    
        // Run request
        const response = await dialogflowClient.updateKnowledgeBase(request);
        console.log(response);
      }
    
      callUpdateKnowledgeBase();
    
    

### updateKnowledgeBase(request, options, callback)
    
    
    updateKnowledgeBase(request: protos.google.cloud.dialogflow.v2beta1.IUpdateKnowledgeBaseRequest, options: CallOptions, callback: Callback<protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase, protos.google.cloud.dialogflow.v2beta1.IUpdateKnowledgeBaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iupdateknowledgebaserequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase), [protos.google.cloud.dialogflow.v2beta1.IUpdateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iupdateknowledgebaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateKnowledgeBase(request, callback)
    
    
    updateKnowledgeBase(request: protos.google.cloud.dialogflow.v2beta1.IUpdateKnowledgeBaseRequest, callback: Callback<protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase, protos.google.cloud.dialogflow.v2beta1.IUpdateKnowledgeBaseRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iupdateknowledgebaserequest)`   
  
`callback` |  `Callback<[protos.google.cloud.dialogflow.v2beta1.IKnowledgeBase](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iknowledgebase), [protos.google.cloud.dialogflow.v2beta1.IUpdateKnowledgeBaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iupdateknowledgebaserequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
