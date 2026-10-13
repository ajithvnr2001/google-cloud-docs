---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/v1alpha.searchserviceclient
title: Class v1alpha.SearchServiceClient (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:01:56.495846+00:00
---

# Class v1alpha.SearchServiceClient (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/v1alpha.searchserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha.SearchServiceClient (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Service for search. v1alpha

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of SearchServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new SearchServiceClient({fallback: true}, gax); ```  
  
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

### scopes
    
    
    static get scopes(): string[];

The scopes needed to make gRPC calls for every method defined in this service.

### searchServiceStub
    
    
    searchServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### aclConfigPath(project, location)
    
    
    aclConfigPath(project: string, location: string): string;

Return a fully-qualified aclConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
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
  
### enginePath(project, location, collection, engine)
    
    
    enginePath(project: string, location: string, collection: string, engine: string): string;

Return a fully-qualified engine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### evaluationPath(project, location, evaluation)
    
    
    evaluationPath(project: string, location: string, evaluation: string): string;

Return a fully-qualified evaluation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`evaluation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
    

### matchAnswerFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchAnswerFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchAnswerFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchAnswerFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchAnswerFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchAnswerFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the answer from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the answer.  
  
### matchBranchFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchBranchFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the branch from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchBranchFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the branch from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationCollectionDataStoreBranchName(projectLocationCollectionDataStoreBranchName)
    
    
    matchBranchFromProjectLocationCollectionDataStoreBranchName(projectLocationCollectionDataStoreBranchName: string): string | number;

Parse the branch from ProjectLocationCollectionDataStoreBranch resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchBranchFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the branch from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchBranchFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the branch from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProjectLocationDataStoreBranchName(projectLocationDataStoreBranchName)
    
    
    matchBranchFromProjectLocationDataStoreBranchName(projectLocationDataStoreBranchName: string): string | number;

Parse the branch from ProjectLocationDataStoreBranch resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchName` |  `string`   
A fully-qualified path representing project_location_data_store_branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchChunkFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchChunkFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the chunk from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchChunkFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchChunkFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the chunk from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the chunk.  
  
### matchCollectionFromEngineName(engineName)
    
    
    matchCollectionFromEngineName(engineName: string): string | number;

Parse the collection from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreBranchName(projectLocationCollectionDataStoreBranchName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreBranchName(projectLocationCollectionDataStoreBranchName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreBranch resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchCollectionFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchCollectionFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchCollectionFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchCollectionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchCollectionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchControlFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchControlFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the control from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchControlFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchControlFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the control from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchControlFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchControlFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the control from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchConversationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchConversationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the conversation from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchConversationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the conversation from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchConversationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchConversationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the conversation from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the conversation.  
  
### matchCustomTuningModelFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchCustomTuningModelFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the custom_tuning_model from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_tuning_model.  
  
### matchCustomTuningModelFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchCustomTuningModelFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the custom_tuning_model from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the custom_tuning_model.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreBranchName(projectLocationCollectionDataStoreBranchName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreBranchName(projectLocationCollectionDataStoreBranchName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreBranch resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchDataStoreFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the data_store from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchDataStoreFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the data_store from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreBranchName(projectLocationDataStoreBranchName)
    
    
    matchDataStoreFromProjectLocationDataStoreBranchName(projectLocationDataStoreBranchName: string): string | number;

Parse the data_store from ProjectLocationDataStoreBranch resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchName` |  `string`   
A fully-qualified path representing project_location_data_store_branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchDataStoreFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the data_store from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchDataStoreFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the data_store from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchDataStoreFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the data_store from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchDataStoreFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the data_store from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchDataStoreFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the data_store from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchDataStoreFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchDataStoreFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the data_store from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchDataStoreFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchDataStoreFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchDataStoreFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDataStoreFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchDataStoreFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the data_store.  
  
### matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the document from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchDocumentFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the document from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchDocumentFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the document from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchDocumentFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchDocumentFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the document from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the document.  
  
### matchEngineFromEngineName(engineName)
    
    
    matchEngineFromEngineName(engineName: string): string | number;

Parse the engine from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchEngineFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchEngineFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchEngineFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchEngineFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchEngineFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEvaluationFromEvaluationName(evaluationName)
    
    
    matchEvaluationFromEvaluationName(evaluationName: string): string | number;

Parse the evaluation from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the evaluation.  
  
### matchLocationFromAclConfigName(aclConfigName)
    
    
    matchLocationFromAclConfigName(aclConfigName: string): string | number;

Parse the location from AclConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`aclConfigName` |  `string`   
A fully-qualified path representing AclConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEngineName(engineName)
    
    
    matchLocationFromEngineName(engineName: string): string | number;

Parse the location from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromEvaluationName(evaluationName)
    
    
    matchLocationFromEvaluationName(evaluationName: string): string | number;

Parse the location from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreBranchName(projectLocationCollectionDataStoreBranchName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreBranchName(projectLocationCollectionDataStoreBranchName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreBranch resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the location from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchLocationFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the location from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchLocationFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the location from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchLocationFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the location from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchLocationFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the location from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchLocationFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the location from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchLocationFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the location from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchLocationFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the location from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreBranchName(projectLocationDataStoreBranchName)
    
    
    matchLocationFromProjectLocationDataStoreBranchName(projectLocationDataStoreBranchName: string): string | number;

Parse the location from ProjectLocationDataStoreBranch resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchName` |  `string`   
A fully-qualified path representing project_location_data_store_branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchLocationFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the location from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchLocationFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the location from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchLocationFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the location from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchLocationFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the location from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchLocationFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the location from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchLocationFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the location from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchLocationFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the location from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchLocationFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the location from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchLocationFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the location from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchLocationFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the location from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchLocationFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the location from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSampleQueryName(sampleQueryName)
    
    
    matchLocationFromSampleQueryName(sampleQueryName: string): string | number;

Parse the location from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchLocationFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the location from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchProjectFromAclConfigName(aclConfigName)
    
    
    matchProjectFromAclConfigName(aclConfigName: string): string | number;

Parse the project from AclConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`aclConfigName` |  `string`   
A fully-qualified path representing AclConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEngineName(engineName)
    
    
    matchProjectFromEngineName(engineName: string): string | number;

Parse the project from Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`engineName` |  `string`   
A fully-qualified path representing Engine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromEvaluationName(evaluationName)
    
    
    matchProjectFromEvaluationName(evaluationName: string): string | number;

Parse the project from Evaluation resource.

**Parameter**  
---  
**Name** | **Description**  
`evaluationName` |  `string`   
A fully-qualified path representing Evaluation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreBranchDocumentChunkName(projectLocationCollectionDataStoreBranchDocumentChunkName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreBranchDocumentName(projectLocationCollectionDataStoreBranchDocumentName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreBranchName(projectLocationCollectionDataStoreBranchName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreBranchName(projectLocationCollectionDataStoreBranchName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreBranch resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreBranchName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreControlName(projectLocationCollectionDataStoreControlName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreConversationName(projectLocationCollectionDataStoreConversationName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreCustomTuningModelName(projectLocationCollectionDataStoreCustomTuningModelName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreDocumentProcessingConfigName(projectLocationCollectionDataStoreDocumentProcessingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreName(projectLocationCollectionDataStoreName: string): string | number;

Parse the project from ProjectLocationCollectionDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreName` |  `string`   
A fully-qualified path representing project_location_collection_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineName(projectLocationCollectionDataStoreSiteSearchEngineName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName)
    
    
    matchProjectFromProjectLocationCollectionEngineControlName(projectLocationCollectionEngineControlName: string): string | number;

Parse the project from ProjectLocationCollectionEngineControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineControlName` |  `string`   
A fully-qualified path representing project_location_collection_engine_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName)
    
    
    matchProjectFromProjectLocationCollectionEngineConversationName(projectLocationCollectionEngineConversationName: string): string | number;

Parse the project from ProjectLocationCollectionEngineConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineConversationName` |  `string`   
A fully-qualified path representing project_location_collection_engine_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchProjectFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the project from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchProjectFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the project from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchProjectFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the project from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName)
    
    
    matchProjectFromProjectLocationDataStoreBranchDocumentChunkName(projectLocationDataStoreBranchDocumentChunkName: string): string | number;

Parse the project from ProjectLocationDataStoreBranchDocumentChunk resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentChunkName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document_chunk resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName)
    
    
    matchProjectFromProjectLocationDataStoreBranchDocumentName(projectLocationDataStoreBranchDocumentName: string): string | number;

Parse the project from ProjectLocationDataStoreBranchDocument resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchDocumentName` |  `string`   
A fully-qualified path representing project_location_data_store_branch_document resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreBranchName(projectLocationDataStoreBranchName)
    
    
    matchProjectFromProjectLocationDataStoreBranchName(projectLocationDataStoreBranchName: string): string | number;

Parse the project from ProjectLocationDataStoreBranch resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreBranchName` |  `string`   
A fully-qualified path representing project_location_data_store_branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName)
    
    
    matchProjectFromProjectLocationDataStoreControlName(projectLocationDataStoreControlName: string): string | number;

Parse the project from ProjectLocationDataStoreControl resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreControlName` |  `string`   
A fully-qualified path representing project_location_data_store_control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName)
    
    
    matchProjectFromProjectLocationDataStoreConversationName(projectLocationDataStoreConversationName: string): string | number;

Parse the project from ProjectLocationDataStoreConversation resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreConversationName` |  `string`   
A fully-qualified path representing project_location_data_store_conversation resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName)
    
    
    matchProjectFromProjectLocationDataStoreCustomTuningModelName(projectLocationDataStoreCustomTuningModelName: string): string | number;

Parse the project from ProjectLocationDataStoreCustomTuningModel resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreCustomTuningModelName` |  `string`   
A fully-qualified path representing project_location_data_store_custom_tuning_model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName)
    
    
    matchProjectFromProjectLocationDataStoreDocumentProcessingConfigName(projectLocationDataStoreDocumentProcessingConfigName: string): string | number;

Parse the project from ProjectLocationDataStoreDocumentProcessingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreDocumentProcessingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_documentProcessingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreName(projectLocationDataStoreName)
    
    
    matchProjectFromProjectLocationDataStoreName(projectLocationDataStoreName: string): string | number;

Parse the project from ProjectLocationDataStore resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreName` |  `string`   
A fully-qualified path representing project_location_data_store resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchProjectFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the project from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchProjectFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the project from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchProjectFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the project from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchProjectFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the project from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName)
    
    
    matchProjectFromProjectLocationDataStoreSiteSearchEngineName(projectLocationDataStoreSiteSearchEngineName: string): string | number;

Parse the project from ProjectLocationDataStoreSiteSearchEngine resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchProjectFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the project from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
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
  
### matchProjectFromSampleQueryName(sampleQueryName)
    
    
    matchProjectFromSampleQueryName(sampleQueryName: string): string | number;

Parse the project from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchProjectFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the project from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchSampleQueryFromSampleQueryName(sampleQueryName)
    
    
    matchSampleQueryFromSampleQueryName(sampleQueryName: string): string | number;

Parse the sample_query from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query.  
  
### matchSampleQuerySetFromSampleQueryName(sampleQueryName)
    
    
    matchSampleQuerySetFromSampleQueryName(sampleQueryName: string): string | number;

Parse the sample_query_set from SampleQuery resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQueryName` |  `string`   
A fully-qualified path representing SampleQuery resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query_set.  
  
### matchSampleQuerySetFromSampleQuerySetName(sampleQuerySetName)
    
    
    matchSampleQuerySetFromSampleQuerySetName(sampleQuerySetName: string): string | number;

Parse the sample_query_set from SampleQuerySet resource.

**Parameter**  
---  
**Name** | **Description**  
`sampleQuerySetName` |  `string`   
A fully-qualified path representing SampleQuerySet resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sample_query_set.  
  
### matchSchemaFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName)
    
    
    matchSchemaFromProjectLocationCollectionDataStoreSchemaName(projectLocationCollectionDataStoreSchemaName: string): string | number;

Parse the schema from ProjectLocationCollectionDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the schema.  
  
### matchSchemaFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName)
    
    
    matchSchemaFromProjectLocationDataStoreSchemaName(projectLocationDataStoreSchemaName: string): string | number;

Parse the schema from ProjectLocationDataStoreSchema resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSchemaName` |  `string`   
A fully-qualified path representing project_location_data_store_schema resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the schema.  
  
### matchServingConfigFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName)
    
    
    matchServingConfigFromProjectLocationCollectionDataStoreServingConfigName(projectLocationCollectionDataStoreServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationCollectionDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchServingConfigFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName)
    
    
    matchServingConfigFromProjectLocationCollectionEngineServingConfigName(projectLocationCollectionEngineServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationCollectionEngineServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineServingConfigName` |  `string`   
A fully-qualified path representing project_location_collection_engine_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchServingConfigFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName)
    
    
    matchServingConfigFromProjectLocationDataStoreServingConfigName(projectLocationDataStoreServingConfigName: string): string | number;

Parse the serving_config from ProjectLocationDataStoreServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreServingConfigName` |  `string`   
A fully-qualified path representing project_location_data_store_serving_config resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### matchSessionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName)
    
    
    matchSessionFromProjectLocationCollectionDataStoreSessionAnswerName(projectLocationCollectionDataStoreSessionAnswerName: string): string | number;

Parse the session from ProjectLocationCollectionDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName)
    
    
    matchSessionFromProjectLocationCollectionDataStoreSessionsName(projectLocationCollectionDataStoreSessionsName: string): string | number;

Parse the session from ProjectLocationCollectionDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName)
    
    
    matchSessionFromProjectLocationCollectionEngineSessionAnswerName(projectLocationCollectionEngineSessionAnswerName: string): string | number;

Parse the session from ProjectLocationCollectionEngineSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_collection_engine_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName)
    
    
    matchSessionFromProjectLocationCollectionEngineSessionsName(projectLocationCollectionEngineSessionsName: string): string | number;

Parse the session from ProjectLocationCollectionEngineSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName)
    
    
    matchSessionFromProjectLocationDataStoreSessionAnswerName(projectLocationDataStoreSessionAnswerName: string): string | number;

Parse the session from ProjectLocationDataStoreSessionAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionAnswerName` |  `string`   
A fully-qualified path representing project_location_data_store_session_answer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchSessionFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName)
    
    
    matchSessionFromProjectLocationDataStoreSessionsName(projectLocationDataStoreSessionsName: string): string | number;

Parse the session from ProjectLocationDataStoreSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSessionsName` |  `string`   
A fully-qualified path representing project_location_data_store_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
### matchTargetSiteFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchTargetSiteFromProjectLocationCollectionDataStoreSiteSearchEngineTargetSiteName(projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the target_site from ProjectLocationCollectionDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the target_site.  
  
### matchTargetSiteFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName)
    
    
    matchTargetSiteFromProjectLocationDataStoreSiteSearchEngineTargetSiteName(projectLocationDataStoreSiteSearchEngineTargetSiteName: string): string | number;

Parse the target_site from ProjectLocationDataStoreSiteSearchEngineTargetSite resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineTargetSiteName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_target_site resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the target_site.  
  
### projectLocationCollectionDataStoreBranchDocumentChunkPath(project, location, collection, dataStore, branch, document, chunk)
    
    
    projectLocationCollectionDataStoreBranchDocumentChunkPath(project: string, location: string, collection: string, dataStore: string, branch: string, document: string, chunk: string): string;

Return a fully-qualified projectLocationCollectionDataStoreBranchDocumentChunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreBranchDocumentPath(project, location, collection, dataStore, branch, document)
    
    
    projectLocationCollectionDataStoreBranchDocumentPath(project: string, location: string, collection: string, dataStore: string, branch: string, document: string): string;

Return a fully-qualified projectLocationCollectionDataStoreBranchDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreBranchPath(project, location, collection, dataStore, branch)
    
    
    projectLocationCollectionDataStoreBranchPath(project: string, location: string, collection: string, dataStore: string, branch: string): string;

Return a fully-qualified projectLocationCollectionDataStoreBranch resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreControlPath(project, location, collection, dataStore, control)
    
    
    projectLocationCollectionDataStoreControlPath(project: string, location: string, collection: string, dataStore: string, control: string): string;

Return a fully-qualified projectLocationCollectionDataStoreControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreConversationPath(project, location, collection, dataStore, conversation)
    
    
    projectLocationCollectionDataStoreConversationPath(project: string, location: string, collection: string, dataStore: string, conversation: string): string;

Return a fully-qualified projectLocationCollectionDataStoreConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreCustomTuningModelPath(project, location, collection, dataStore, customTuningModel)
    
    
    projectLocationCollectionDataStoreCustomTuningModelPath(project: string, location: string, collection: string, dataStore: string, customTuningModel: string): string;

Return a fully-qualified projectLocationCollectionDataStoreCustomTuningModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`customTuningModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreDocumentProcessingConfigPath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStoreDocumentProcessingConfigPath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStoreDocumentProcessingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStorePath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStorePath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSchemaPath(project, location, collection, dataStore, schema)
    
    
    projectLocationCollectionDataStoreSchemaPath(project: string, location: string, collection: string, dataStore: string, schema: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`schema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreServingConfigPath(project, location, collection, dataStore, servingConfig)
    
    
    projectLocationCollectionDataStoreServingConfigPath(project: string, location: string, collection: string, dataStore: string, servingConfig: string): string;

Return a fully-qualified projectLocationCollectionDataStoreServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSessionAnswerPath(project, location, collection, dataStore, session, answer)
    
    
    projectLocationCollectionDataStoreSessionAnswerPath(project: string, location: string, collection: string, dataStore: string, session: string, answer: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSessionsPath(project, location, collection, dataStore, session)
    
    
    projectLocationCollectionDataStoreSessionsPath(project: string, location: string, collection: string, dataStore: string, session: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSiteSearchEnginePath(project, location, collection, dataStore)
    
    
    projectLocationCollectionDataStoreSiteSearchEnginePath(project: string, location: string, collection: string, dataStore: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSiteSearchEngine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionDataStoreSiteSearchEngineTargetSitePath(project, location, collection, dataStore, targetSite)
    
    
    projectLocationCollectionDataStoreSiteSearchEngineTargetSitePath(project: string, location: string, collection: string, dataStore: string, targetSite: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSiteSearchEngineTargetSite resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`targetSite` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineControlPath(project, location, collection, engine, control)
    
    
    projectLocationCollectionEngineControlPath(project: string, location: string, collection: string, engine: string, control: string): string;

Return a fully-qualified projectLocationCollectionEngineControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineConversationPath(project, location, collection, engine, conversation)
    
    
    projectLocationCollectionEngineConversationPath(project: string, location: string, collection: string, engine: string, conversation: string): string;

Return a fully-qualified projectLocationCollectionEngineConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineServingConfigPath(project, location, collection, engine, servingConfig)
    
    
    projectLocationCollectionEngineServingConfigPath(project: string, location: string, collection: string, engine: string, servingConfig: string): string;

Return a fully-qualified projectLocationCollectionEngineServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineSessionAnswerPath(project, location, collection, engine, session, answer)
    
    
    projectLocationCollectionEngineSessionAnswerPath(project: string, location: string, collection: string, engine: string, session: string, answer: string): string;

Return a fully-qualified projectLocationCollectionEngineSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCollectionEngineSessionsPath(project, location, collection, engine, session)
    
    
    projectLocationCollectionEngineSessionsPath(project: string, location: string, collection: string, engine: string, session: string): string;

Return a fully-qualified projectLocationCollectionEngineSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreBranchDocumentChunkPath(project, location, dataStore, branch, document, chunk)
    
    
    projectLocationDataStoreBranchDocumentChunkPath(project: string, location: string, dataStore: string, branch: string, document: string, chunk: string): string;

Return a fully-qualified projectLocationDataStoreBranchDocumentChunk resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
`chunk` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreBranchDocumentPath(project, location, dataStore, branch, document)
    
    
    projectLocationDataStoreBranchDocumentPath(project: string, location: string, dataStore: string, branch: string, document: string): string;

Return a fully-qualified projectLocationDataStoreBranchDocument resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
`document` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreBranchPath(project, location, dataStore, branch)
    
    
    projectLocationDataStoreBranchPath(project: string, location: string, dataStore: string, branch: string): string;

Return a fully-qualified projectLocationDataStoreBranch resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`branch` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreControlPath(project, location, dataStore, control)
    
    
    projectLocationDataStoreControlPath(project: string, location: string, dataStore: string, control: string): string;

Return a fully-qualified projectLocationDataStoreControl resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreConversationPath(project, location, dataStore, conversation)
    
    
    projectLocationDataStoreConversationPath(project: string, location: string, dataStore: string, conversation: string): string;

Return a fully-qualified projectLocationDataStoreConversation resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`conversation` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreCustomTuningModelPath(project, location, dataStore, customTuningModel)
    
    
    projectLocationDataStoreCustomTuningModelPath(project: string, location: string, dataStore: string, customTuningModel: string): string;

Return a fully-qualified projectLocationDataStoreCustomTuningModel resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`customTuningModel` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreDocumentProcessingConfigPath(project, location, dataStore)
    
    
    projectLocationDataStoreDocumentProcessingConfigPath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStoreDocumentProcessingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStorePath(project, location, dataStore)
    
    
    projectLocationDataStorePath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSchemaPath(project, location, dataStore, schema)
    
    
    projectLocationDataStoreSchemaPath(project: string, location: string, dataStore: string, schema: string): string;

Return a fully-qualified projectLocationDataStoreSchema resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`schema` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreServingConfigPath(project, location, dataStore, servingConfig)
    
    
    projectLocationDataStoreServingConfigPath(project: string, location: string, dataStore: string, servingConfig: string): string;

Return a fully-qualified projectLocationDataStoreServingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSessionAnswerPath(project, location, dataStore, session, answer)
    
    
    projectLocationDataStoreSessionAnswerPath(project: string, location: string, dataStore: string, session: string, answer: string): string;

Return a fully-qualified projectLocationDataStoreSessionAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
`answer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSessionsPath(project, location, dataStore, session)
    
    
    projectLocationDataStoreSessionsPath(project: string, location: string, dataStore: string, session: string): string;

Return a fully-qualified projectLocationDataStoreSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`session` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSiteSearchEnginePath(project, location, dataStore)
    
    
    projectLocationDataStoreSiteSearchEnginePath(project: string, location: string, dataStore: string): string;

Return a fully-qualified projectLocationDataStoreSiteSearchEngine resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationDataStoreSiteSearchEngineTargetSitePath(project, location, dataStore, targetSite)
    
    
    projectLocationDataStoreSiteSearchEngineTargetSitePath(project: string, location: string, dataStore: string, targetSite: string): string;

Return a fully-qualified projectLocationDataStoreSiteSearchEngineTargetSite resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`targetSite` |  `string`   
  
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
  
### sampleQueryPath(project, location, sampleQuerySet, sampleQuery)
    
    
    sampleQueryPath(project: string, location: string, sampleQuerySet: string, sampleQuery: string): string;

Return a fully-qualified sampleQuery resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sampleQuerySet` |  `string`   
  
`sampleQuery` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### sampleQuerySetPath(project, location, sampleQuerySet)
    
    
    sampleQuerySetPath(project: string, location: string, sampleQuerySet: string): string;

Return a fully-qualified sampleQuerySet resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`sampleQuerySet` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### search(request, options)
    
    
    search(request?: protos.google.cloud.discoveryengine.v1alpha.ISearchRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1alpha.SearchResponse.ISearchResult[],
            protos.google.cloud.discoveryengine.v1alpha.ISearchRequest | null,
            protos.google.cloud.discoveryengine.v1alpha.ISearchResponse
        ]>;

Performs a search.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1alpha.SearchResponse.ISearchResult](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.searchresponse.isearchresult)[], [protos.google.cloud.discoveryengine.v1alpha.ISearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchrequest) | null, [protos.google.cloud.discoveryengine.v1alpha.ISearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `searchAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### search(request, options, callback)
    
    
    search(request: protos.google.cloud.discoveryengine.v1alpha.ISearchRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1alpha.ISearchRequest, protos.google.cloud.discoveryengine.v1alpha.ISearchResponse | null | undefined, protos.google.cloud.discoveryengine.v1alpha.SearchResponse.ISearchResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1alpha.ISearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchrequest), [protos.google.cloud.discoveryengine.v1alpha.ISearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1alpha.SearchResponse.ISearchResult](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.searchresponse.isearchresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### search(request, callback)
    
    
    search(request: protos.google.cloud.discoveryengine.v1alpha.ISearchRequest, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1alpha.ISearchRequest, protos.google.cloud.discoveryengine.v1alpha.ISearchResponse | null | undefined, protos.google.cloud.discoveryengine.v1alpha.SearchResponse.ISearchResult>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1alpha.ISearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchrequest), [protos.google.cloud.discoveryengine.v1alpha.ISearchResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1alpha.SearchResponse.ISearchResult](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.searchresponse.isearchresult)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchAsync(request, options)
    
    
    searchAsync(request?: protos.google.cloud.discoveryengine.v1alpha.ISearchRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.discoveryengine.v1alpha.SearchResponse.ISearchResult>;

Equivalent to `search`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.discoveryengine.v1alpha.SearchResponse.ISearchResult](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.searchresponse.isearchresult)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Search serving config, such as
       *  `projects/* /locations/global/collections/default_collection/engines/* /servingConfigs/default_serving_config`,
       *  or
       *  `projects/* /locations/global/collections/default_collection/dataStores/default_data_store/servingConfigs/default_serving_config`.
       *  This field is used to identify the serving configuration name, set
       *  of models used to make the search.
       */
      // const servingConfig = 'abc123'
      /**
       *  The branch resource name, such as
       *  `projects/* /locations/global/collections/default_collection/dataStores/default_data_store/branches/0`.
       *  Use `default_branch` as the branch ID or leave this field empty, to search
       *  documents under the default branch.
       */
      // const branch = 'abc123'
      /**
       *  Raw search query.
       */
      // const query = 'abc123'
      /**
       *  Raw image query.
       */
      // const imageQuery = {}
      /**
       *  Maximum number of
       *  Document google.cloud.discoveryengine.v1alpha.Document s to return. The
       *  maximum allowed value depends on the data type. Values above the maximum
       *  value are coerced to the maximum value.
       *  * Websites with basic indexing: Default `10`, Maximum `25`.
       *  * Websites with advanced indexing: Default `25`, Maximum `50`.
       *  * Other: Default `50`, Maximum `100`.
       *  If this field is negative, an  `INVALID_ARGUMENT` is returned.
       */
      // const pageSize = 1234
      /**
       *  A page token received from a previous
       *  SearchService.Search google.cloud.discoveryengine.v1alpha.SearchService.Search 
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  SearchService.Search google.cloud.discoveryengine.v1alpha.SearchService.Search 
       *  must match the call that provided the page token. Otherwise, an
       *   `INVALID_ARGUMENT`  error is returned.
       */
      // const pageToken = 'abc123'
      /**
       *  A 0-indexed integer that specifies the current offset (that is, starting
       *  result location, amongst the
       *  Document google.cloud.discoveryengine.v1alpha.Document s deemed by the
       *  API as relevant) in search results. This field is only considered if
       *  page_token google.cloud.discoveryengine.v1alpha.SearchRequest.page_token 
       *  is unset.
       *  If this field is negative, an  `INVALID_ARGUMENT`  is returned.
       */
      // const offset = 1234
      /**
       *  Specs defining dataStores to filter on in a search call and configurations
       *  for those dataStores. This is only considered for engines with multiple
       *  dataStores use case. For single dataStore within an engine, they should
       *  use the specs at the top level.
       */
      // const dataStoreSpecs = [1,2,3,4]
      /**
       *  The filter syntax consists of an expression language for constructing a
       *  predicate from one or more fields of the documents being filtered. Filter
       *  expression is case-sensitive.
       *  If this field is unrecognizable, an  `INVALID_ARGUMENT`  is returned.
       *  Filtering in Vertex AI Search is done by mapping the LHS filter key to a
       *  key property defined in the Vertex AI Search backend -- this mapping is
       *  defined by the customer in their schema. For example a media customer might
       *  have a field 'name' in their schema. In this case the filter would look
       *  like this: filter --> name:'ANY("king kong")'
       *  For more information about filtering including syntax and filter
       *  operators, see
       *  Filter (https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)
       */
      // const filter = 'abc123'
      /**
       *  The default filter that is applied when a user performs a search without
       *  checking any filters on the search page.
       *  The filter applied to every search request when quality improvement such as
       *  query expansion is needed. In the case a query does not have a sufficient
       *  amount of results this filter will be used to determine whether or not to
       *  enable the query expansion flow. The original filter will still be used for
       *  the query expanded search.
       *  This field is strongly recommended to achieve high search quality.
       *  For more information about filter syntax, see
       *  SearchRequest.filter google.cloud.discoveryengine.v1alpha.SearchRequest.filter.
       */
      // const canonicalFilter = 'abc123'
      /**
       *  The order in which documents are returned. Documents can be ordered by
       *  a field in an Document google.cloud.discoveryengine.v1alpha.Document 
       *  object. Leave it unset if ordered by relevance. `order_by` expression is
       *  case-sensitive.
       *  For more information on ordering the website search results, see
       *  Order web search
       *  results (https://cloud.google.com/generative-ai-app-builder/docs/order-web-search-results).
       *  For more information on ordering the healthcare search results, see
       *  Order healthcare search
       *  results (https://cloud.google.com/generative-ai-app-builder/docs/order-hc-results).
       *  If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.
       */
      // const orderBy = 'abc123'
      /**
       *  Information about the end user.
       *  Highly recommended for analytics.
       *  UserInfo.user_agent google.cloud.discoveryengine.v1alpha.UserInfo.user_agent 
       *  is used to deduce `device_type` for analytics.
       */
      // const userInfo = {}
      /**
       *  The BCP-47 language code, such as "en-US" or "sr-Latn". For more
       *  information, see Standard
       *  fields (https://cloud.google.com/apis/design/standard_fields). This field
       *  helps to better interpret the query. If a value isn't specified, the query
       *  language code is automatically detected, which may not be accurate.
       */
      // const languageCode = 'abc123'
      /**
       *  The Unicode country/region code (CLDR) of a location, such as "US" and
       *  "419". For more information, see Standard
       *  fields (https://cloud.google.com/apis/design/standard_fields). If set,
       *  then results will be boosted based on the region_code provided.
       */
      // const regionCode = 'abc123'
      /**
       *  Facet specifications for faceted search. If empty, no facets are returned.
       *  A maximum of 100 values are allowed. Otherwise, an  `INVALID_ARGUMENT`
       *  error is returned.
       */
      // const facetSpecs = [1,2,3,4]
      /**
       *  Boost specification to boost certain documents.
       *  For more information on boosting, see
       *  Boosting (https://cloud.google.com/generative-ai-app-builder/docs/boost-search-results)
       */
      // const boostSpec = {}
      /**
       *  Additional search parameters.
       *  For public website search only, supported values are:
       *  * `user_country_code`: string. Default empty. If set to non-empty, results
       *     are restricted or boosted based on the location provided.
       *     For example, `user_country_code: "au"`
       *     For available codes see Country
       *     Codes (https://developers.google.com/custom-search/docs/json_api_reference#countryCodes)
       *  * `search_type`: double. Default empty. Enables non-webpage searching
       *     depending on the value. The only valid non-default value is 1,
       *     which enables image searching.
       *     For example, `search_type: 1`
       */
      // const params = [1,2,3,4]
      /**
       *  The query expansion specification that specifies the conditions under which
       *  query expansion occurs.
       */
      // const queryExpansionSpec = {}
      /**
       *  The spell correction specification that specifies the mode under
       *  which spell correction takes effect.
       */
      // const spellCorrectionSpec = {}
      /**
       *  A unique identifier for tracking visitors. For example, this could be
       *  implemented with an HTTP cookie, which should be able to uniquely identify
       *  a visitor on a single device. This unique identifier should not change if
       *  the visitor logs in or out of the website.
       *  This field should NOT have a fixed value such as `unknown_visitor`.
       *  This should be the same identifier as
       *  UserEvent.user_pseudo_id google.cloud.discoveryengine.v1alpha.UserEvent.user_pseudo_id 
       *  and
       *  CompleteQueryRequest.user_pseudo_id google.cloud.discoveryengine.v1alpha.CompleteQueryRequest.user_pseudo_id 
       *  The field must be a UTF-8 encoded string with a length limit of 128
       *  characters. Otherwise, an  `INVALID_ARGUMENT`  error is returned.
       */
      // const userPseudoId = 'abc123'
      /**
       *  A specification for configuring the behavior of content search.
       */
      // const contentSearchSpec = {}
      /**
       *  Uses the provided embedding to do additional semantic document retrieval.
       *  The retrieval is based on the dot product of
       *  SearchRequest.EmbeddingSpec.EmbeddingVector.vector google.cloud.discoveryengine.v1alpha.SearchRequest.EmbeddingSpec.EmbeddingVector.vector 
       *  and the document embedding that is provided in
       *  SearchRequest.EmbeddingSpec.EmbeddingVector.field_path google.cloud.discoveryengine.v1alpha.SearchRequest.EmbeddingSpec.EmbeddingVector.field_path.
       *  If
       *  SearchRequest.EmbeddingSpec.EmbeddingVector.field_path google.cloud.discoveryengine.v1alpha.SearchRequest.EmbeddingSpec.EmbeddingVector.field_path 
       *  is not provided, it will use
       *  ServingConfig.EmbeddingConfig.field_path google.cloud.discoveryengine.v1alpha.ServingConfig.embedding_config.
       */
      // const embeddingSpec = {}
      /**
       *  The ranking expression controls the customized ranking on retrieval
       *  documents. This overrides
       *  ServingConfig.ranking_expression google.cloud.discoveryengine.v1alpha.ServingConfig.ranking_expression.
       *  The syntax and supported features depend on the
       *  `ranking_expression_backend` value. If `ranking_expression_backend` is not
       *  provided, it defaults to `RANK_BY_EMBEDDING`.
       *  If
       *  ranking_expression_backend google.cloud.discoveryengine.v1alpha.SearchRequest.ranking_expression_backend 
       *  is not provided or set to `RANK_BY_EMBEDDING`, it should be a single
       *  function or multiple functions that are joined by "+".
       *    * ranking_expression = function, { " + ", function };
       *  Supported functions:
       *    * double * relevance_score
       *    * double * dotProduct(embedding_field_path)
       *  Function variables:
       *    * `relevance_score`: pre-defined keywords, used for measure relevance
       *    between query and document.
       *    * `embedding_field_path`: the document embedding field
       *    used with query embedding vector.
       *    * `dotProduct`: embedding function between `embedding_field_path` and
       *    query embedding vector.
       *   Example ranking expression:
       *     If document has an embedding field doc_embedding, the ranking expression
       *     could be `0.5 * relevance_score + 0.3 * dotProduct(doc_embedding)`.
       *  If
       *  ranking_expression_backend google.cloud.discoveryengine.v1alpha.SearchRequest.ranking_expression_backend 
       *  is set to `RANK_BY_FORMULA`, the following expression types (and
       *  combinations of those chained using + or
       *  * operators) are supported:
       *    * `double`
       *    * `signal`
       *    * `log(signal)`
       *    * `exp(signal)`
       *    * `rr(signal, double > 0)`  -- reciprocal rank transformation with second
       *    argument being a denominator constant.
       *    * `is_nan(signal)` -- returns 0 if signal is NaN, 1 otherwise.
       *    * `fill_nan(signal1, signal2 | double)` -- if signal1 is NaN, returns
       *    signal2 | double, else returns signal1.
       *    Here are a few examples of ranking formulas that use the supported
       *    ranking expression types:
       *    - `0.2 * semantic_similarity_score + 0.8 * log(keyword_similarity_score)`
       *    -- mostly rank by the logarithm of `keyword_similarity_score` with slight
       *    `semantic_smilarity_score` adjustment.
       *    - `0.2 * exp(fill_nan(semantic_similarity_score, 0)) + 0.3 *
       *    is_nan(keyword_similarity_score)` -- rank by the exponent of
       *    `semantic_similarity_score` filling the value with 0 if it's NaN, also
       *    add constant 0.3 adjustment to the final score if
       *    `semantic_similarity_score` is NaN.
       *    - `0.2 * rr(semantic_similarity_score, 16) + 0.8 *
       *    rr(keyword_similarity_score, 16)` -- mostly rank by the reciprocal rank
       *    of `keyword_similarity_score` with slight adjustment of reciprocal rank
       *    of `semantic_smilarity_score`.
       *  The following signals are supported:
       *    * `semantic_similarity_score`: semantic similarity adjustment that is
       *    calculated using the embeddings generated by a proprietary Google model.
       *    This score determines how semantically similar a search query is to a
       *    document.
       *    * `keyword_similarity_score`: keyword match adjustment uses the Best
       *    Match 25 (BM25) ranking function. This score is calculated using a
       *    probabilistic model to estimate the probability that a document is
       *    relevant to a given query.
       *    * `relevance_score`: semantic relevance adjustment that uses a
       *    proprietary Google model to determine the meaning and intent behind a
       *    user's query in context with the content in the documents.
       *    * `pctr_rank`: predicted conversion rate adjustment as a rank use
       *    predicted Click-through rate (pCTR) to gauge the relevance and
       *    attractiveness of a search result from a user's perspective. A higher
       *    pCTR suggests that the result is more likely to satisfy the user's query
       *    and intent, making it a valuable signal for ranking.
       *    * `freshness_rank`: freshness adjustment as a rank
       *    * `document_age`: The time in hours elapsed since the document was last
       *    updated, a floating-point number (e.g., 0.25 means 15 minutes).
       *    * `topicality_rank`: topicality adjustment as a rank. Uses proprietary
       *    Google model to determine the keyword-based overlap between the query and
       *    the document.
       *    * `base_rank`: the default rank of the result
       */
      // const rankingExpression = 'abc123'
      /**
       *  The backend to use for the ranking expression evaluation.
       */
      // const rankingExpressionBackend = {}
      /**
       *  Whether to turn on safe search. This is only supported for
       *  website search.
       */
      // const safeSearch = true
      /**
       *  The user labels applied to a resource must meet the following requirements:
       *  * Each resource can have multiple labels, up to a maximum of 64.
       *  * Each label must be a key-value pair.
       *  * Keys have a minimum length of 1 character and a maximum length of 63
       *    characters and cannot be empty. Values can be empty and have a maximum
       *    length of 63 characters.
       *  * Keys and values can contain only lowercase letters, numeric characters,
       *    underscores, and dashes. All characters must use UTF-8 encoding, and
       *    international characters are allowed.
       *  * The key portion of a label must be unique. However, you can use the same
       *    key with multiple resources.
       *  * Keys must start with a lowercase letter or international character.
       *  See Google Cloud
       *  Document (https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements)
       *  for more details.
       */
      // const userLabels = [1,2,3,4]
      /**
       *  If `naturalLanguageQueryUnderstandingSpec` is not specified, no additional
       *  natural language query understanding will be done.
       */
      // const naturalLanguageQueryUnderstandingSpec = {}
      /**
       *  Search as you type configuration. Only supported for the
       *  IndustryVertical.MEDIA google.cloud.discoveryengine.v1alpha.IndustryVertical.MEDIA 
       *  vertical.
       */
      // const searchAsYouTypeSpec = {}
      /**
       *  Custom fine tuning configs.
       *  If set, it has higher priority than the configs set in
       *  ServingConfig.custom_fine_tuning_spec google.cloud.discoveryengine.v1alpha.ServingConfig.custom_fine_tuning_spec.
       */
      // const customFineTuningSpec = {}
      /**
       *  The session resource name. Optional.
       *  Session allows users to do multi-turn /search API calls or coordination
       *  between /search API calls and /answer API calls.
       *  Example #1 (multi-turn /search API calls):
       *    Call /search API with the session ID generated in the first call.
       *    Here, the previous search query gets considered in query
       *    standing. I.e., if the first query is "How did Alphabet do in 2022?"
       *    and the current query is "How about 2023?", the current query will
       *    be interpreted as "How did Alphabet do in 2023?".
       *  Example #2 (coordination between /search API calls and /answer API calls):
       *    Call /answer API with the session ID generated in the first call.
       *    Here, the answer generation happens in the context of the search
       *    results from the first search call.
       *  Multi-turn Search feature is currently at private GA stage. Please use
       *  v1alpha or v1beta version instead before we launch this feature to public
       *  GA. Or ask for allowlisting through Google Support team.
       */
      // const session = 'abc123'
      /**
       *  Session specification.
       *  Can be used only when `session` is set.
       */
      // const sessionSpec = {}
      /**
       *  The relevance threshold of the search results.
       *  Default to Google defined threshold, leveraging a balance of
       *  precision and recall to deliver both highly accurate results and
       *  comprehensive coverage of relevant information.
       */
      // const relevanceThreshold = {}
    
      // Imports the Discoveryengine library
      const {SearchServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1alpha;
    
      // Instantiates a client
      const discoveryengineClient = new [SearchServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callSearch() {
        // Construct request
        const request = {
          servingConfig,
        };
    
        // Run request
        const iterable = discoveryengineClient.searchAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callSearch();
    
    

### searchStream(request, options)
    
    
    searchStream(request?: protos.google.cloud.discoveryengine.v1alpha.ISearchRequest, options?: CallOptions): Transform;

Equivalent to `search`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.isearchrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `searchAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
