---
url: https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/v1beta.cloudapiregistryclient
title: Class v1beta.CloudApiRegistryClient (0.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:09.360822+00:00
---

# Class v1beta.CloudApiRegistryClient (0.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/v1beta.cloudapiregistryclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.CloudApiRegistryClient (0.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.2.0  0.1.0 

The Cloud API Registry service provides a central registry for managing API Data. v1beta

## Package

[@google-cloud/apiregistry](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of CloudApiRegistryClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new CloudApiRegistryClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### cloudApiRegistryStub
    
    
    cloudApiRegistryStub?: Promise<{
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

### apiNamespacePath(project, location, apiNamespace)
    
    
    apiNamespacePath(project: string, location: string, apiNamespace: string): string;

Return a fully-qualified apiNamespace resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`apiNamespace` |  `string`   
  
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
    

### getMcpServer(request, options)
    
    
    getMcpServer(request?: protos.google.cloud.apiregistry.v1beta.IGetMcpServerRequest, options?: CallOptions): Promise<[
            protos.google.cloud.apiregistry.v1beta.IMcpServer,
            protos.google.cloud.apiregistry.v1beta.IGetMcpServerRequest | undefined,
            {} | undefined
        ]>;

Gets a single McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMcpServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcpserverrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.apiregistry.v1beta.IMcpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcpserver), [protos.google.cloud.apiregistry.v1beta.IGetMcpServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcpserverrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [McpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.mcpserver). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Apiregistry library
      const {CloudApiRegistryClient} = require('[@google-cloud/apiregistry](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const apiregistryClient = new [CloudApiRegistryClient](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)();
    
      async function callGetMcpServer() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await apiregistryClient.getMcpServer(request);
        console.log(response);
      }
    
      callGetMcpServer();
    
    

### getMcpServer(request, options, callback)
    
    
    getMcpServer(request: protos.google.cloud.apiregistry.v1beta.IGetMcpServerRequest, options: CallOptions, callback: Callback<protos.google.cloud.apiregistry.v1beta.IMcpServer, protos.google.cloud.apiregistry.v1beta.IGetMcpServerRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMcpServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcpserverrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.apiregistry.v1beta.IMcpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcpserver), [protos.google.cloud.apiregistry.v1beta.IGetMcpServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcpserverrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMcpServer(request, callback)
    
    
    getMcpServer(request: protos.google.cloud.apiregistry.v1beta.IGetMcpServerRequest, callback: Callback<protos.google.cloud.apiregistry.v1beta.IMcpServer, protos.google.cloud.apiregistry.v1beta.IGetMcpServerRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMcpServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcpserverrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.apiregistry.v1beta.IMcpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcpserver), [protos.google.cloud.apiregistry.v1beta.IGetMcpServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcpserverrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMcpTool(request, options)
    
    
    getMcpTool(request?: protos.google.cloud.apiregistry.v1beta.IGetMcpToolRequest, options?: CallOptions): Promise<[
            protos.google.cloud.apiregistry.v1beta.IMcpTool,
            protos.google.cloud.apiregistry.v1beta.IGetMcpToolRequest | undefined,
            {} | undefined
        ]>;

Gets a single McpTool.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMcpToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcptoolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.apiregistry.v1beta.IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcptool), [protos.google.cloud.apiregistry.v1beta.IGetMcpToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcptoolrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [McpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.mcptool). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
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
    
      // Imports the Apiregistry library
      const {CloudApiRegistryClient} = require('[@google-cloud/apiregistry](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const apiregistryClient = new [CloudApiRegistryClient](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)();
    
      async function callGetMcpTool() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await apiregistryClient.getMcpTool(request);
        console.log(response);
      }
    
      callGetMcpTool();
    
    

### getMcpTool(request, options, callback)
    
    
    getMcpTool(request: protos.google.cloud.apiregistry.v1beta.IGetMcpToolRequest, options: CallOptions, callback: Callback<protos.google.cloud.apiregistry.v1beta.IMcpTool, protos.google.cloud.apiregistry.v1beta.IGetMcpToolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMcpToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcptoolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.apiregistry.v1beta.IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcptool), [protos.google.cloud.apiregistry.v1beta.IGetMcpToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcptoolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMcpTool(request, callback)
    
    
    getMcpTool(request: protos.google.cloud.apiregistry.v1beta.IGetMcpToolRequest, callback: Callback<protos.google.cloud.apiregistry.v1beta.IMcpTool, protos.google.cloud.apiregistry.v1beta.IGetMcpToolRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMcpToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcptoolrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.apiregistry.v1beta.IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcptool), [protos.google.cloud.apiregistry.v1beta.IGetMcpToolRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.igetmcptoolrequest) | null | undefined, {} | null | undefined>`   
  
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
    

### listMcpServers(request, options)
    
    
    listMcpServers(request?: protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest, options?: CallOptions): Promise<[
            protos.google.cloud.apiregistry.v1beta.IMcpServer[],
            protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest | null,
            protos.google.cloud.apiregistry.v1beta.IListMcpServersResponse
        ]>;

Lists McpServers in a given Project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.apiregistry.v1beta.IMcpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcpserver)[], [protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversrequest) | null, [protos.google.cloud.apiregistry.v1beta.IListMcpServersResponse](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [McpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.mcpserver). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMcpServersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMcpServers(request, options, callback)
    
    
    listMcpServers(request: protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest, protos.google.cloud.apiregistry.v1beta.IListMcpServersResponse | null | undefined, protos.google.cloud.apiregistry.v1beta.IMcpServer>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversrequest), [protos.google.cloud.apiregistry.v1beta.IListMcpServersResponse](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversresponse) | null | undefined, [protos.google.cloud.apiregistry.v1beta.IMcpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcpserver)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMcpServers(request, callback)
    
    
    listMcpServers(request: protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest, callback: PaginationCallback<protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest, protos.google.cloud.apiregistry.v1beta.IListMcpServersResponse | null | undefined, protos.google.cloud.apiregistry.v1beta.IMcpServer>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversrequest), [protos.google.cloud.apiregistry.v1beta.IListMcpServersResponse](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversresponse) | null | undefined, [protos.google.cloud.apiregistry.v1beta.IMcpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcpserver)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMcpServersAsync(request, options)
    
    
    listMcpServersAsync(request?: protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.apiregistry.v1beta.IMcpServer>;

Equivalent to `listMcpServers`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.apiregistry.v1beta.IMcpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcpserver)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [McpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.mcpserver). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListMcpServersRequest
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results
       */
      // const orderBy = 'abc123'
    
      // Imports the Apiregistry library
      const {CloudApiRegistryClient} = require('[@google-cloud/apiregistry](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const apiregistryClient = new [CloudApiRegistryClient](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)();
    
      async function callListMcpServers() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = apiregistryClient.listMcpServersAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMcpServers();
    
    

### listMcpServersStream(request, options)
    
    
    listMcpServersStream(request?: protos.google.cloud.apiregistry.v1beta.IListMcpServersRequest, options?: CallOptions): Transform;

Equivalent to `listMcpServers`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpServersRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcpserversrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [McpServer](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.mcpserver) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMcpServersAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMcpTools(request, options)
    
    
    listMcpTools(request?: protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.apiregistry.v1beta.IMcpTool[],
            protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest | null,
            protos.google.cloud.apiregistry.v1beta.IListMcpToolsResponse
        ]>;

Lists McpTools in a given McpServer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.apiregistry.v1beta.IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcptool)[], [protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsrequest) | null, [protos.google.cloud.apiregistry.v1beta.IListMcpToolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [McpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.mcptool). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMcpToolsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMcpTools(request, options, callback)
    
    
    listMcpTools(request: protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest, protos.google.cloud.apiregistry.v1beta.IListMcpToolsResponse | null | undefined, protos.google.cloud.apiregistry.v1beta.IMcpTool>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsrequest), [protos.google.cloud.apiregistry.v1beta.IListMcpToolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsresponse) | null | undefined, [protos.google.cloud.apiregistry.v1beta.IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcptool)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMcpTools(request, callback)
    
    
    listMcpTools(request: protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest, callback: PaginationCallback<protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest, protos.google.cloud.apiregistry.v1beta.IListMcpToolsResponse | null | undefined, protos.google.cloud.apiregistry.v1beta.IMcpTool>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsrequest), [protos.google.cloud.apiregistry.v1beta.IListMcpToolsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsresponse) | null | undefined, [protos.google.cloud.apiregistry.v1beta.IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcptool)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMcpToolsAsync(request, options)
    
    
    listMcpToolsAsync(request?: protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.apiregistry.v1beta.IMcpTool>;

Equivalent to `listMcpTools`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.apiregistry.v1beta.IMcpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.imcptool)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [McpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.mcptool). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent value for ListMcpToolsRequest
       */
      // const parent = 'abc123'
      /**
       *  Optional. Requested page size. Server may return fewer items than
       *  requested. If unspecified, server will pick an appropriate default.
       */
      // const pageSize = 1234
      /**
       *  Optional. A token identifying a page of results the server should return.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filtering results
       */
      // const filter = 'abc123'
      /**
       *  Optional. Hint for how to order the results
       */
      // const orderBy = 'abc123'
    
      // Imports the Apiregistry library
      const {CloudApiRegistryClient} = require('[@google-cloud/apiregistry](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const apiregistryClient = new [CloudApiRegistryClient](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)();
    
      async function callListMcpTools() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = apiregistryClient.listMcpToolsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMcpTools();
    
    

### listMcpToolsStream(request, options)
    
    
    listMcpToolsStream(request?: protos.google.cloud.apiregistry.v1beta.IListMcpToolsRequest, options?: CallOptions): Transform;

Equivalent to `listMcpTools`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMcpToolsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.ilistmcptoolsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [McpTool](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.cloud.apiregistry.v1beta.mcptool) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMcpToolsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
### matchApiNamespaceFromApiNamespaceName(apiNamespaceName)
    
    
    matchApiNamespaceFromApiNamespaceName(apiNamespaceName: string): string | number;

Parse the api_namespace from ApiNamespace resource.

**Parameter**  
---  
**Name** | **Description**  
`apiNamespaceName` |  `string`   
A fully-qualified path representing ApiNamespace resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the api_namespace.  
  
### matchApiNamespaceFromProjectLocationApiNamespaceMcpServerMcpToolsName(projectLocationApiNamespaceMcpServerMcpToolsName)
    
    
    matchApiNamespaceFromProjectLocationApiNamespaceMcpServerMcpToolsName(projectLocationApiNamespaceMcpServerMcpToolsName: string): string | number;

Parse the api_namespace from ProjectLocationApiNamespaceMcpServerMcpTools resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationApiNamespaceMcpServerMcpToolsName` |  `string`   
A fully-qualified path representing project_location_api_namespace_mcp_server_mcpTools resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the api_namespace.  
  
### matchApiNamespaceFromProjectLocationApiNamespaceMcpServersName(projectLocationApiNamespaceMcpServersName)
    
    
    matchApiNamespaceFromProjectLocationApiNamespaceMcpServersName(projectLocationApiNamespaceMcpServersName: string): string | number;

Parse the api_namespace from ProjectLocationApiNamespaceMcpServers resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationApiNamespaceMcpServersName` |  `string`   
A fully-qualified path representing project_location_api_namespace_mcpServers resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the api_namespace.  
  
### matchLocationFromApiNamespaceName(apiNamespaceName)
    
    
    matchLocationFromApiNamespaceName(apiNamespaceName: string): string | number;

Parse the location from ApiNamespace resource.

**Parameter**  
---  
**Name** | **Description**  
`apiNamespaceName` |  `string`   
A fully-qualified path representing ApiNamespace resource.  
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
  
### matchLocationFromProjectLocationApiNamespaceMcpServerMcpToolsName(projectLocationApiNamespaceMcpServerMcpToolsName)
    
    
    matchLocationFromProjectLocationApiNamespaceMcpServerMcpToolsName(projectLocationApiNamespaceMcpServerMcpToolsName: string): string | number;

Parse the location from ProjectLocationApiNamespaceMcpServerMcpTools resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationApiNamespaceMcpServerMcpToolsName` |  `string`   
A fully-qualified path representing project_location_api_namespace_mcp_server_mcpTools resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationApiNamespaceMcpServersName(projectLocationApiNamespaceMcpServersName)
    
    
    matchLocationFromProjectLocationApiNamespaceMcpServersName(projectLocationApiNamespaceMcpServersName: string): string | number;

Parse the location from ProjectLocationApiNamespaceMcpServers resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationApiNamespaceMcpServersName` |  `string`   
A fully-qualified path representing project_location_api_namespace_mcpServers resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationMcpServerMcpToolsName(projectLocationMcpServerMcpToolsName)
    
    
    matchLocationFromProjectLocationMcpServerMcpToolsName(projectLocationMcpServerMcpToolsName: string): string | number;

Parse the location from ProjectLocationMcpServerMcpTools resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationMcpServerMcpToolsName` |  `string`   
A fully-qualified path representing project_location_mcp_server_mcpTools resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationMcpServersName(projectLocationMcpServersName)
    
    
    matchLocationFromProjectLocationMcpServersName(projectLocationMcpServersName: string): string | number;

Parse the location from ProjectLocationMcpServers resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationMcpServersName` |  `string`   
A fully-qualified path representing project_location_mcpServers resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMcpServerFromProjectLocationApiNamespaceMcpServerMcpToolsName(projectLocationApiNamespaceMcpServerMcpToolsName)
    
    
    matchMcpServerFromProjectLocationApiNamespaceMcpServerMcpToolsName(projectLocationApiNamespaceMcpServerMcpToolsName: string): string | number;

Parse the mcp_server from ProjectLocationApiNamespaceMcpServerMcpTools resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationApiNamespaceMcpServerMcpToolsName` |  `string`   
A fully-qualified path representing project_location_api_namespace_mcp_server_mcpTools resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the mcp_server.  
  
### matchMcpServerFromProjectLocationApiNamespaceMcpServersName(projectLocationApiNamespaceMcpServersName)
    
    
    matchMcpServerFromProjectLocationApiNamespaceMcpServersName(projectLocationApiNamespaceMcpServersName: string): string | number;

Parse the mcp_server from ProjectLocationApiNamespaceMcpServers resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationApiNamespaceMcpServersName` |  `string`   
A fully-qualified path representing project_location_api_namespace_mcpServers resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the mcp_server.  
  
### matchMcpServerFromProjectLocationMcpServerMcpToolsName(projectLocationMcpServerMcpToolsName)
    
    
    matchMcpServerFromProjectLocationMcpServerMcpToolsName(projectLocationMcpServerMcpToolsName: string): string | number;

Parse the mcp_server from ProjectLocationMcpServerMcpTools resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationMcpServerMcpToolsName` |  `string`   
A fully-qualified path representing project_location_mcp_server_mcpTools resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the mcp_server.  
  
### matchMcpServerFromProjectLocationMcpServersName(projectLocationMcpServersName)
    
    
    matchMcpServerFromProjectLocationMcpServersName(projectLocationMcpServersName: string): string | number;

Parse the mcp_server from ProjectLocationMcpServers resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationMcpServersName` |  `string`   
A fully-qualified path representing project_location_mcpServers resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the mcp_server.  
  
### matchMcpToolFromProjectLocationApiNamespaceMcpServerMcpToolsName(projectLocationApiNamespaceMcpServerMcpToolsName)
    
    
    matchMcpToolFromProjectLocationApiNamespaceMcpServerMcpToolsName(projectLocationApiNamespaceMcpServerMcpToolsName: string): string | number;

Parse the mcp_tool from ProjectLocationApiNamespaceMcpServerMcpTools resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationApiNamespaceMcpServerMcpToolsName` |  `string`   
A fully-qualified path representing project_location_api_namespace_mcp_server_mcpTools resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the mcp_tool.  
  
### matchMcpToolFromProjectLocationMcpServerMcpToolsName(projectLocationMcpServerMcpToolsName)
    
    
    matchMcpToolFromProjectLocationMcpServerMcpToolsName(projectLocationMcpServerMcpToolsName: string): string | number;

Parse the mcp_tool from ProjectLocationMcpServerMcpTools resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationMcpServerMcpToolsName` |  `string`   
A fully-qualified path representing project_location_mcp_server_mcpTools resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the mcp_tool.  
  
### matchProjectFromApiNamespaceName(apiNamespaceName)
    
    
    matchProjectFromApiNamespaceName(apiNamespaceName: string): string | number;

Parse the project from ApiNamespace resource.

**Parameter**  
---  
**Name** | **Description**  
`apiNamespaceName` |  `string`   
A fully-qualified path representing ApiNamespace resource.  
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
  
### matchProjectFromProjectLocationApiNamespaceMcpServerMcpToolsName(projectLocationApiNamespaceMcpServerMcpToolsName)
    
    
    matchProjectFromProjectLocationApiNamespaceMcpServerMcpToolsName(projectLocationApiNamespaceMcpServerMcpToolsName: string): string | number;

Parse the project from ProjectLocationApiNamespaceMcpServerMcpTools resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationApiNamespaceMcpServerMcpToolsName` |  `string`   
A fully-qualified path representing project_location_api_namespace_mcp_server_mcpTools resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationApiNamespaceMcpServersName(projectLocationApiNamespaceMcpServersName)
    
    
    matchProjectFromProjectLocationApiNamespaceMcpServersName(projectLocationApiNamespaceMcpServersName: string): string | number;

Parse the project from ProjectLocationApiNamespaceMcpServers resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationApiNamespaceMcpServersName` |  `string`   
A fully-qualified path representing project_location_api_namespace_mcpServers resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationMcpServerMcpToolsName(projectLocationMcpServerMcpToolsName)
    
    
    matchProjectFromProjectLocationMcpServerMcpToolsName(projectLocationMcpServerMcpToolsName: string): string | number;

Parse the project from ProjectLocationMcpServerMcpTools resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationMcpServerMcpToolsName` |  `string`   
A fully-qualified path representing project_location_mcp_server_mcpTools resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationMcpServersName(projectLocationMcpServersName)
    
    
    matchProjectFromProjectLocationMcpServersName(projectLocationMcpServersName: string): string | number;

Parse the project from ProjectLocationMcpServers resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationMcpServersName` |  `string`   
A fully-qualified path representing project_location_mcpServers resource.  
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
  
### projectLocationApiNamespaceMcpServerMcpToolsPath(project, location, apiNamespace, mcpServer, mcpTool)
    
    
    projectLocationApiNamespaceMcpServerMcpToolsPath(project: string, location: string, apiNamespace: string, mcpServer: string, mcpTool: string): string;

Return a fully-qualified projectLocationApiNamespaceMcpServerMcpTools resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`apiNamespace` |  `string`   
  
`mcpServer` |  `string`   
  
`mcpTool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationApiNamespaceMcpServersPath(project, location, apiNamespace, mcpServer)
    
    
    projectLocationApiNamespaceMcpServersPath(project: string, location: string, apiNamespace: string, mcpServer: string): string;

Return a fully-qualified projectLocationApiNamespaceMcpServers resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`apiNamespace` |  `string`   
  
`mcpServer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationMcpServerMcpToolsPath(project, location, mcpServer, mcpTool)
    
    
    projectLocationMcpServerMcpToolsPath(project: string, location: string, mcpServer: string, mcpTool: string): string;

Return a fully-qualified projectLocationMcpServerMcpTools resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`mcpServer` |  `string`   
  
`mcpTool` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationMcpServersPath(project, location, mcpServer)
    
    
    projectLocationMcpServersPath(project: string, location: string, mcpServer: string): string;

Return a fully-qualified projectLocationMcpServers resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`mcpServer` |  `string`   
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
