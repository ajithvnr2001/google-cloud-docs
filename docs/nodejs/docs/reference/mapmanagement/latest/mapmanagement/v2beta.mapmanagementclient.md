---
url: https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/v2beta.mapmanagementclient
title: Class v2beta.MapManagementClient (0.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:15.628806+00:00
---

# Class v2beta.MapManagementClient (0.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/v2beta.mapmanagementclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v2beta.MapManagementClient (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

The Map Management API uses your inputs to create and manage Google Cloud based styling resources for Google Maps.

Using this API, you can can create and manage MapConfigs (Map IDs), StyleConfigs (JSON-based styling), and MapContextConfigs (associations between styles, datasets, and map variants).

This API offers features through three channels: * `v2alpha`: Experimental features. * `v2beta`: Preview features, recommended for early adoption. * `v2`: General Availability (GA) features.

Capabilities described here are generally available across both the v2alpha and v2beta endpoints. v2beta

## Package

[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of MapManagementClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new MapManagementClient({fallback: true}, gax); ```  
  
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

### mapManagementStub
    
    
    mapManagementStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### createMapConfig(request, options)
    
    
    createMapConfig(request?: protos.google.maps.mapmanagement.v2beta.ICreateMapConfigRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IMapConfig,
            (protos.google.maps.mapmanagement.v2beta.ICreateMapConfigRequest | undefined),
            {} | undefined
        ]>;

Creates a MapConfig in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig), ([protos.google.maps.mapmanagement.v2beta.ICreateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapconfig). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent project that will own the MapConfig.
       *  Format: `projects/{$my-project-id}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The MapConfig to create.
       */
      // const mapConfig = {}
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callCreateMapConfig() {
        // Construct request
        const request = {
          parent,
          mapConfig,
        };
    
        // Run request
        const response = await mapmanagementClient.createMapConfig(request);
        console.log(response);
      }
    
      callCreateMapConfig();
    
    

### createMapConfig(request, options, callback)
    
    
    createMapConfig(request: protos.google.maps.mapmanagement.v2beta.ICreateMapConfigRequest, options: CallOptions, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapConfig, protos.google.maps.mapmanagement.v2beta.ICreateMapConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig), [protos.google.maps.mapmanagement.v2beta.ICreateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMapConfig(request, callback)
    
    
    createMapConfig(request: protos.google.maps.mapmanagement.v2beta.ICreateMapConfigRequest, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapConfig, protos.google.maps.mapmanagement.v2beta.ICreateMapConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapconfigrequest)`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig), [protos.google.maps.mapmanagement.v2beta.ICreateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMapContextConfig(request, options)
    
    
    createMapContextConfig(request?: protos.google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IMapContextConfig,
            (protos.google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest | undefined),
            {} | undefined
        ]>;

Creates a MapContextConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapcontextconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig), ([protos.google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapcontextconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent MapConfig that will own the MapContextConfig.
       *  Format: `projects/{project}/mapConfigs/{map_config}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The MapContextConfig to create.
       */
      // const mapContextConfig = {}
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callCreateMapContextConfig() {
        // Construct request
        const request = {
          parent,
          mapContextConfig,
        };
    
        // Run request
        const response = await mapmanagementClient.createMapContextConfig(request);
        console.log(response);
      }
    
      callCreateMapContextConfig();
    
    

### createMapContextConfig(request, options, callback)
    
    
    createMapContextConfig(request: protos.google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest, options: CallOptions, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapContextConfig, protos.google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapcontextconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig), [protos.google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapcontextconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMapContextConfig(request, callback)
    
    
    createMapContextConfig(request: protos.google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapContextConfig, protos.google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapcontextconfigrequest)`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig), [protos.google.maps.mapmanagement.v2beta.ICreateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatemapcontextconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createStyleConfig(request, options)
    
    
    createStyleConfig(request?: protos.google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IStyleConfig,
            (protos.google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest | undefined),
            {} | undefined
        ]>;

Creates a StyleConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatestyleconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig), ([protos.google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatestyleconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [StyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.styleconfig). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent project that will own the StyleConfig.
       *  Format: `projects/{project}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The StyleConfig to create.
       */
      // const styleConfig = {}
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callCreateStyleConfig() {
        // Construct request
        const request = {
          parent,
          styleConfig,
        };
    
        // Run request
        const response = await mapmanagementClient.createStyleConfig(request);
        console.log(response);
      }
    
      callCreateStyleConfig();
    
    

### createStyleConfig(request, options, callback)
    
    
    createStyleConfig(request: protos.google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest, options: CallOptions, callback: Callback<protos.google.maps.mapmanagement.v2beta.IStyleConfig, protos.google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatestyleconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig), [protos.google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatestyleconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createStyleConfig(request, callback)
    
    
    createStyleConfig(request: protos.google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest, callback: Callback<protos.google.maps.mapmanagement.v2beta.IStyleConfig, protos.google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatestyleconfigrequest)`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig), [protos.google.maps.mapmanagement.v2beta.ICreateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.icreatestyleconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### datasetPath(project, dataset)
    
    
    datasetPath(project: string, dataset: string): string;

Return a fully-qualified dataset resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`dataset` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### deleteMapConfig(request, options)
    
    
    deleteMapConfig(request?: protos.google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest | undefined),
            {} | undefined
        ]>;

Deletes a MapConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.iempty), ([protos.google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the MapConfig to delete.
       *  Format: `projects/{project}/mapConfigs/{map_config}`
       */
      // const name = 'abc123'
      /**
       *  Optional. If set to true, any MapContextConfigs from this MapConfig will
       *  also be deleted. (Otherwise, the request will only work if the MapConfig
       *  has no MapContextConfigs.)
       */
      // const force = true
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callDeleteMapConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await mapmanagementClient.deleteMapConfig(request);
        console.log(response);
      }
    
      callDeleteMapConfig();
    
    

### deleteMapConfig(request, options, callback)
    
    
    deleteMapConfig(request: protos.google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.iempty), [protos.google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMapConfig(request, callback)
    
    
    deleteMapConfig(request: protos.google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.iempty), [protos.google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMapContextConfig(request, options)
    
    
    deleteMapContextConfig(request?: protos.google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest | undefined),
            {} | undefined
        ]>;

Deletes a MapContextConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapcontextconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.iempty), ([protos.google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapcontextconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the MapContextConfig to delete.
       *  Format:
       *  `projects/{project}/mapConfigs/{map_config}/mapContextConfigs/{map_context_config}`
       */
      // const name = 'abc123'
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callDeleteMapContextConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await mapmanagementClient.deleteMapContextConfig(request);
        console.log(response);
      }
    
      callDeleteMapContextConfig();
    
    

### deleteMapContextConfig(request, options, callback)
    
    
    deleteMapContextConfig(request: protos.google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapcontextconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.iempty), [protos.google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapcontextconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMapContextConfig(request, callback)
    
    
    deleteMapContextConfig(request: protos.google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapcontextconfigrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.iempty), [protos.google.maps.mapmanagement.v2beta.IDeleteMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapcontextconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteStyleConfig(request, options)
    
    
    deleteStyleConfig(request?: protos.google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            (protos.google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest | undefined),
            {} | undefined
        ]>;

Deletes a StyleConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletestyleconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.iempty), ([protos.google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletestyleconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the StyleConfig to delete.
       *  Format: `projects/{project}/styleConfigs/{style_config}`
       */
      // const name = 'abc123'
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callDeleteStyleConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await mapmanagementClient.deleteStyleConfig(request);
        console.log(response);
      }
    
      callDeleteStyleConfig();
    
    

### deleteStyleConfig(request, options, callback)
    
    
    deleteStyleConfig(request: protos.google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletestyleconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.iempty), [protos.google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletestyleconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteStyleConfig(request, callback)
    
    
    deleteStyleConfig(request: protos.google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletestyleconfigrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.protobuf.iempty), [protos.google.maps.mapmanagement.v2beta.IDeleteStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletestyleconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMapConfig(request, options)
    
    
    getMapConfig(request?: protos.google.maps.mapmanagement.v2beta.IGetMapConfigRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IMapConfig,
            protos.google.maps.mapmanagement.v2beta.IGetMapConfigRequest | undefined,
            {} | undefined
        ]>;

Gets a MapConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig), [protos.google.maps.mapmanagement.v2beta.IGetMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapconfigrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapconfig). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the MapConfig.
       *  Format: `projects/{project}/mapConfigs/{map_config}`
       */
      // const name = 'abc123'
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callGetMapConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await mapmanagementClient.getMapConfig(request);
        console.log(response);
      }
    
      callGetMapConfig();
    
    

### getMapConfig(request, options, callback)
    
    
    getMapConfig(request: protos.google.maps.mapmanagement.v2beta.IGetMapConfigRequest, options: CallOptions, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapConfig, protos.google.maps.mapmanagement.v2beta.IGetMapConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig), [protos.google.maps.mapmanagement.v2beta.IGetMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMapConfig(request, callback)
    
    
    getMapConfig(request: protos.google.maps.mapmanagement.v2beta.IGetMapConfigRequest, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapConfig, protos.google.maps.mapmanagement.v2beta.IGetMapConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapconfigrequest)`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig), [protos.google.maps.mapmanagement.v2beta.IGetMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMapContextConfig(request, options)
    
    
    getMapContextConfig(request?: protos.google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IMapContextConfig,
            (protos.google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest | undefined),
            {} | undefined
        ]>;

Gets a MapContextConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapcontextconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig), ([protos.google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapcontextconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the MapContextConfig.
       *  Format:
       *  `projects/{project}/mapConfigs/{map_config}/mapContextConfigs/{map_context_config}`
       */
      // const name = 'abc123'
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callGetMapContextConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await mapmanagementClient.getMapContextConfig(request);
        console.log(response);
      }
    
      callGetMapContextConfig();
    
    

### getMapContextConfig(request, options, callback)
    
    
    getMapContextConfig(request: protos.google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest, options: CallOptions, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapContextConfig, protos.google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapcontextconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig), [protos.google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapcontextconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMapContextConfig(request, callback)
    
    
    getMapContextConfig(request: protos.google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapContextConfig, protos.google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapcontextconfigrequest)`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig), [protos.google.maps.mapmanagement.v2beta.IGetMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetmapcontextconfigrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getStyleConfig(request, options)
    
    
    getStyleConfig(request?: protos.google.maps.mapmanagement.v2beta.IGetStyleConfigRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IStyleConfig,
            (protos.google.maps.mapmanagement.v2beta.IGetStyleConfigRequest | undefined),
            {} | undefined
        ]>;

Gets a StyleConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetstyleconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig), ([protos.google.maps.mapmanagement.v2beta.IGetStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetstyleconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [StyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.styleconfig). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Resource name of the StyleConfig.
       *  Format: `projects/{project}/styleConfigs/{style_config}`
       */
      // const name = 'abc123'
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callGetStyleConfig() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await mapmanagementClient.getStyleConfig(request);
        console.log(response);
      }
    
      callGetStyleConfig();
    
    

### getStyleConfig(request, options, callback)
    
    
    getStyleConfig(request: protos.google.maps.mapmanagement.v2beta.IGetStyleConfigRequest, options: CallOptions, callback: Callback<protos.google.maps.mapmanagement.v2beta.IStyleConfig, protos.google.maps.mapmanagement.v2beta.IGetStyleConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetstyleconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig), [protos.google.maps.mapmanagement.v2beta.IGetStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetstyleconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStyleConfig(request, callback)
    
    
    getStyleConfig(request: protos.google.maps.mapmanagement.v2beta.IGetStyleConfigRequest, callback: Callback<protos.google.maps.mapmanagement.v2beta.IStyleConfig, protos.google.maps.mapmanagement.v2beta.IGetStyleConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetstyleconfigrequest)`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig), [protos.google.maps.mapmanagement.v2beta.IGetStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.igetstyleconfigrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listMapConfigs(request, options)
    
    
    listMapConfigs(request?: protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IMapConfig[],
            protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest | null,
            protos.google.maps.mapmanagement.v2beta.IListMapConfigsResponse
        ]>;

Lists MapConfigs for a project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig)[], [protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsrequest) | null, [protos.google.maps.mapmanagement.v2beta.IListMapConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [MapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapconfig). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMapConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMapConfigs(request, options, callback)
    
    
    listMapConfigs(request: protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest, options: CallOptions, callback: PaginationCallback<protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest, protos.google.maps.mapmanagement.v2beta.IListMapConfigsResponse | null | undefined, protos.google.maps.mapmanagement.v2beta.IMapConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsrequest), [protos.google.maps.mapmanagement.v2beta.IListMapConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsresponse) | null | undefined, [protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMapConfigs(request, callback)
    
    
    listMapConfigs(request: protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest, callback: PaginationCallback<protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest, protos.google.maps.mapmanagement.v2beta.IListMapConfigsResponse | null | undefined, protos.google.maps.mapmanagement.v2beta.IMapConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsrequest), [protos.google.maps.mapmanagement.v2beta.IListMapConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsresponse) | null | undefined, [protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMapConfigsAsync(request, options)
    
    
    listMapConfigsAsync(request?: protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest, options?: CallOptions): AsyncIterable<protos.google.maps.mapmanagement.v2beta.IMapConfig>;

Equivalent to `listMapConfigs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [MapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapconfig). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent project that owns the MapConfigs.
       *  Format: `projects/{project}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of MapConfigs to return. The service may
       *  return fewer than this value. If unspecified, at most 50 MapConfigs will be
       *  returned. The maximum value is 1000; values above 1000 will be coerced to
       *  1000. CURRENTLY UNSUPPORTED.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListMapConfigs` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListMapConfigs` must
       *  match the call that provided the page token.
       *  CURRENTLY UNSUPPORTED.
       */
      // const pageToken = 'abc123'
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callListMapConfigs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = mapmanagementClient.[listMapConfigsAsync](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/v2beta.mapmanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMapConfigs();
    
    

### listMapConfigsStream(request, options)
    
    
    listMapConfigsStream(request?: protos.google.maps.mapmanagement.v2beta.IListMapConfigsRequest, options?: CallOptions): Transform;

Equivalent to `listMapConfigs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [MapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapconfig) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMapConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMapContextConfigs(request, options)
    
    
    listMapContextConfigs(request?: protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IMapContextConfig[],
            protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest | null,
            protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsResponse
        ]>;

Lists MapContextConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapContextConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig)[], [protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsrequest) | null, [protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listMapContextConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listMapContextConfigs(request, options, callback)
    
    
    listMapContextConfigs(request: protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest, options: CallOptions, callback: PaginationCallback<protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest, protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsResponse | null | undefined, protos.google.maps.mapmanagement.v2beta.IMapContextConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapContextConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsrequest), [protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsresponse) | null | undefined, [protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMapContextConfigs(request, callback)
    
    
    listMapContextConfigs(request: protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest, callback: PaginationCallback<protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest, protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsResponse | null | undefined, protos.google.maps.mapmanagement.v2beta.IMapContextConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapContextConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsrequest), [protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsresponse) | null | undefined, [protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMapContextConfigsAsync(request, options)
    
    
    listMapContextConfigsAsync(request?: protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest, options?: CallOptions): AsyncIterable<protos.google.maps.mapmanagement.v2beta.IMapContextConfig>;

Equivalent to `listMapContextConfigs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapContextConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent MapConfig that owns the MapContextConfigs.
       *  Format: `projects/{project}/mapConfigs/{map_config}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of MapContextConfigs to return. The service
       *  may return fewer than this value. If unspecified, at most 50
       *  MapContextConfigs will be returned. The maximum value is 1000; values above
       *  1000 will be coerced to 1000. CURRENTLY UNSUPPORTED.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListMapContextConfigs`
       *  call. Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListMapContextConfigs`
       *  must match the call that provided the page token. CURRENTLY UNSUPPORTED.
       */
      // const pageToken = 'abc123'
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callListMapContextConfigs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = mapmanagementClient.[listMapContextConfigsAsync](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/v2beta.mapmanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListMapContextConfigs();
    
    

### listMapContextConfigsStream(request, options)
    
    
    listMapContextConfigsStream(request?: protos.google.maps.mapmanagement.v2beta.IListMapContextConfigsRequest, options?: CallOptions): Transform;

Equivalent to `listMapContextConfigs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMapContextConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ilistmapcontextconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listMapContextConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listStyleConfigs(request, options)
    
    
    listStyleConfigs(request?: protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IStyleConfig[],
            protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest | null,
            protos.google.maps.mapmanagement.v2beta.IListStyleConfigsResponse
        ]>;

Lists StyleConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStyleConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig)[], [protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsrequest) | null, [protos.google.maps.mapmanagement.v2beta.IListStyleConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [StyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.styleconfig). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listStyleConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listStyleConfigs(request, options, callback)
    
    
    listStyleConfigs(request: protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest, options: CallOptions, callback: PaginationCallback<protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest, protos.google.maps.mapmanagement.v2beta.IListStyleConfigsResponse | null | undefined, protos.google.maps.mapmanagement.v2beta.IStyleConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStyleConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsrequest), [protos.google.maps.mapmanagement.v2beta.IListStyleConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsresponse) | null | undefined, [protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStyleConfigs(request, callback)
    
    
    listStyleConfigs(request: protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest, callback: PaginationCallback<protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest, protos.google.maps.mapmanagement.v2beta.IListStyleConfigsResponse | null | undefined, protos.google.maps.mapmanagement.v2beta.IStyleConfig>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStyleConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsrequest), [protos.google.maps.mapmanagement.v2beta.IListStyleConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsresponse) | null | undefined, [protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStyleConfigsAsync(request, options)
    
    
    listStyleConfigsAsync(request?: protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest, options?: CallOptions): AsyncIterable<protos.google.maps.mapmanagement.v2beta.IStyleConfig>;

Equivalent to `listStyleConfigs`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStyleConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [StyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.styleconfig). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Parent project that owns the StyleConfigs.
       *  Format: `projects/{project}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. The maximum number of StyleConfigs to return. The service may
       *  return fewer than this value. If unspecified, at most 50 StyleConfigs will
       *  be returned. The maximum value is 1000; values above 1000 will be coerced
       *  to 1000. CURRENTLY UNSUPPORTED.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListStyleConfigs` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListStyleConfigs` must
       *  match the call that provided the page token.
       *  CURRENTLY UNSUPPORTED.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Filter expression for the ListStyleConfigs call.
       *  Currently only supports filtering by display_name.
       *  For example: `display_name="My StyleConfig"` will return all StyleConfigs
       *  with the display name "My StyleConfig".
       */
      // const filter = 'abc123'
      /**
       *  Optional. The subset of the StyleConfig to return. If this is unset, the
       *  default behavior is to return the FULL view.
       */
      // const view = {}
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callListStyleConfigs() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = mapmanagementClient.[listStyleConfigsAsync](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/v2beta.mapmanagementclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListStyleConfigs();
    
    

### listStyleConfigsStream(request, options)
    
    
    listStyleConfigsStream(request?: protos.google.maps.mapmanagement.v2beta.IListStyleConfigsRequest, options?: CallOptions): Transform;

Equivalent to `listStyleConfigs`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStyleConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iliststyleconfigsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [StyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.styleconfig) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listStyleConfigsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### mapConfigPath(project, mapConfig)
    
    
    mapConfigPath(project: string, mapConfig: string): string;

Return a fully-qualified mapConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`mapConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### mapContextConfigPath(project, mapConfig, mapContextConfig)
    
    
    mapContextConfigPath(project: string, mapConfig: string, mapContextConfig: string): string;

Return a fully-qualified mapContextConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`mapConfig` |  `string`   
  
`mapContextConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### matchDatasetFromDatasetName(datasetName)
    
    
    matchDatasetFromDatasetName(datasetName: string): string | number;

Parse the dataset from Dataset resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetName` |  `string`   
A fully-qualified path representing Dataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the dataset.  
  
### matchMapConfigFromMapConfigName(mapConfigName)
    
    
    matchMapConfigFromMapConfigName(mapConfigName: string): string | number;

Parse the map_config from MapConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`mapConfigName` |  `string`   
A fully-qualified path representing MapConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the map_config.  
  
### matchMapConfigFromMapContextConfigName(mapContextConfigName)
    
    
    matchMapConfigFromMapContextConfigName(mapContextConfigName: string): string | number;

Parse the map_config from MapContextConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`mapContextConfigName` |  `string`   
A fully-qualified path representing MapContextConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the map_config.  
  
### matchMapContextConfigFromMapContextConfigName(mapContextConfigName)
    
    
    matchMapContextConfigFromMapContextConfigName(mapContextConfigName: string): string | number;

Parse the map_context_config from MapContextConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`mapContextConfigName` |  `string`   
A fully-qualified path representing MapContextConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the map_context_config.  
  
### matchProjectFromDatasetName(datasetName)
    
    
    matchProjectFromDatasetName(datasetName: string): string | number;

Parse the project from Dataset resource.

**Parameter**  
---  
**Name** | **Description**  
`datasetName` |  `string`   
A fully-qualified path representing Dataset resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMapConfigName(mapConfigName)
    
    
    matchProjectFromMapConfigName(mapConfigName: string): string | number;

Parse the project from MapConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`mapConfigName` |  `string`   
A fully-qualified path representing MapConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMapContextConfigName(mapContextConfigName)
    
    
    matchProjectFromMapContextConfigName(mapContextConfigName: string): string | number;

Parse the project from MapContextConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`mapContextConfigName` |  `string`   
A fully-qualified path representing MapContextConfig resource.  
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
  
### matchProjectFromStyleConfigName(styleConfigName)
    
    
    matchProjectFromStyleConfigName(styleConfigName: string): string | number;

Parse the project from StyleConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`styleConfigName` |  `string`   
A fully-qualified path representing StyleConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchStyleConfigFromStyleConfigName(styleConfigName)
    
    
    matchStyleConfigFromStyleConfigName(styleConfigName: string): string | number;

Parse the style_config from StyleConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`styleConfigName` |  `string`   
A fully-qualified path representing StyleConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the style_config.  
  
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
  
### styleConfigPath(project, styleConfig)
    
    
    styleConfigPath(project: string, styleConfig: string): string;

Return a fully-qualified styleConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`styleConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateMapConfig(request, options)
    
    
    updateMapConfig(request?: protos.google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IMapConfig,
            (protos.google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest | undefined),
            {} | undefined
        ]>;

Updates a MapConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig), ([protos.google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [MapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.mapconfig). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The MapConfig to update.
       *  The MapConfig's `name` field is used to identify the MapConfig to update.
       *  Format: `projects/{project}/mapConfigs/{map_config}`
       */
      // const mapConfig = {}
      /**
       *  Optional. The specific field to update for the MapConfig. If not specified,
       *  the MapConfig will be updated in its entirety. Valid fields are:
       *  * `display_name`
       *  * `description`
       *  * `map_features`
       */
      // const updateMask = {}
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callUpdateMapConfig() {
        // Construct request
        const request = {
          mapConfig,
        };
    
        // Run request
        const response = await mapmanagementClient.updateMapConfig(request);
        console.log(response);
      }
    
      callUpdateMapConfig();
    
    

### updateMapConfig(request, options, callback)
    
    
    updateMapConfig(request: protos.google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest, options: CallOptions, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapConfig, protos.google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig), [protos.google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMapConfig(request, callback)
    
    
    updateMapConfig(request: protos.google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapConfig, protos.google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest)`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapconfig), [protos.google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMapContextConfig(request, options)
    
    
    updateMapContextConfig(request?: protos.google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IMapContextConfig,
            (protos.google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest | undefined),
            {} | undefined
        ]>;

Updates a MapContextConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig), ([protos.google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The MapContextConfig to update.
       *  The MapContextConfig's `name` field is used to identify the
       *  MapContextConfig to update. Format:
       *  `projects/{project}/mapConfigs/{map_config}/mapContextConfigs/{map_context_config}`
       */
      // const mapContextConfig = {}
      /**
       *  Optional. The list of fields to update. If not specified, the
       *  MapContextConfig will be updated in its entirety. Valid fields are:
       *  * `display_name`
       *  * `alias`
       *  * `map_variants`
       *  * `style_config`
       *  * `dataset`
       */
      // const updateMask = {}
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callUpdateMapContextConfig() {
        // Construct request
        const request = {
          mapContextConfig,
        };
    
        // Run request
        const response = await mapmanagementClient.updateMapContextConfig(request);
        console.log(response);
      }
    
      callUpdateMapContextConfig();
    
    

### updateMapContextConfig(request, options, callback)
    
    
    updateMapContextConfig(request: protos.google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest, options: CallOptions, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapContextConfig, protos.google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig), [protos.google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMapContextConfig(request, callback)
    
    
    updateMapContextConfig(request: protos.google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest, callback: Callback<protos.google.maps.mapmanagement.v2beta.IMapContextConfig, protos.google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest)`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IMapContextConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.imapcontextconfig), [protos.google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateStyleConfig(request, options)
    
    
    updateStyleConfig(request?: protos.google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest, options?: CallOptions): Promise<[
            protos.google.maps.mapmanagement.v2beta.IStyleConfig,
            (protos.google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest | undefined),
            {} | undefined
        ]>;

Updates a StyleConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatestyleconfigrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig), ([protos.google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatestyleconfigrequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [StyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.styleconfig). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The StyleConfig to update.
       *  The StyleConfig's `name` field is used to identify the StyleConfig to
       *  update. Format: `projects/{project}/styleConfigs/{style_config}`
       */
      // const styleConfig = {}
      /**
       *  Optional. The list of fields to update. If not specified, the StyleConfig
       *  will be updated in its entirety. Valid fields are:
       *  * `display_name`
       *  * `description`
       *  * `json_style_sheet`
       */
      // const updateMask = {}
    
      // Imports the Mapmanagement library
      const {MapManagementClient} = require('[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)').v2beta;
    
      // Instantiates a client
      const mapmanagementClient = new [MapManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)();
    
      async function callUpdateStyleConfig() {
        // Construct request
        const request = {
          styleConfig,
        };
    
        // Run request
        const response = await mapmanagementClient.updateStyleConfig(request);
        console.log(response);
      }
    
      callUpdateStyleConfig();
    
    

### updateStyleConfig(request, options, callback)
    
    
    updateStyleConfig(request: protos.google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest, options: CallOptions, callback: Callback<protos.google.maps.mapmanagement.v2beta.IStyleConfig, protos.google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatestyleconfigrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig), [protos.google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatestyleconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateStyleConfig(request, callback)
    
    
    updateStyleConfig(request: protos.google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest, callback: Callback<protos.google.maps.mapmanagement.v2beta.IStyleConfig, protos.google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatestyleconfigrequest)`   
  
`callback` |  `Callback<[protos.google.maps.mapmanagement.v2beta.IStyleConfig](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.istyleconfig), [protos.google.maps.mapmanagement.v2beta.IUpdateStyleConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatestyleconfigrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-25 UTC."],[],[]] 
