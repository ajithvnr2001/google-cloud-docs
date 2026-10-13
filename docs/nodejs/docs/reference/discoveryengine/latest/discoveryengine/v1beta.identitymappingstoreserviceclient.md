---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/v1beta.identitymappingstoreserviceclient
title: Class v1beta.IdentityMappingStoreServiceClient (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:01:27.359159+00:00
---

# Class v1beta.IdentityMappingStoreServiceClient (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/v1beta.identitymappingstoreserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.IdentityMappingStoreServiceClient (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Service for managing Identity Mapping Stores. v1beta

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of IdentityMappingStoreServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new IdentityMappingStoreServiceClient({fallback: true}, gax); ```  
  
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

### identityMappingStoreServiceStub
    
    
    identityMappingStoreServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
        };

### locationsClient
    
    
    locationsClient: LocationsClient;

### operationsClient
    
    
    operationsClient: gax.OperationsClient;

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
  
### assistAnswerPath(project, location, collection, engine, session, assistAnswer)
    
    
    assistAnswerPath(project: string, location: string, collection: string, engine: string, session: string, assistAnswer: string): string;

Return a fully-qualified assistAnswer resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`session` |  `string`   
  
`assistAnswer` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### assistantPath(project, location, collection, engine, assistant)
    
    
    assistantPath(project: string, location: string, collection: string, engine: string, assistant: string): string;

Return a fully-qualified assistant resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`assistant` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### cancelOperation(request, optionsOrCallback, callback)
    
    
    cancelOperation(request: protos.google.longrunning.CancelOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>, callback?: Callback<protos.google.longrunning.CancelOperationRequest, protos.google.protobuf.Empty, {} | undefined | null>): Promise<protos.google.protobuf.Empty>;

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an value with a of 1, corresponding to `Code.CANCELLED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### checkDeleteIdentityMappingStoreProgress(name)
    
    
    checkDeleteIdentityMappingStoreProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.discoveryengine.v1beta.DeleteIdentityMappingStoreMetadata>>;

Check the status of the long running operation returned by `deleteIdentityMappingStore()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), [protos.google.cloud.discoveryengine.v1beta.DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.deleteidentitymappingstoremetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Identity Mapping Store to delete.
       *  Format:
       *  `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {IdentityMappingStoreServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callDeleteIdentityMappingStore() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.deleteIdentityMappingStore(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteIdentityMappingStore();
    
    

### checkImportIdentityMappingsProgress(name)
    
    
    checkImportIdentityMappingsProgress(name: string): Promise<LROperation<protos.google.cloud.discoveryengine.v1beta.ImportIdentityMappingsResponse, protos.google.cloud.discoveryengine.v1beta.IdentityMappingEntryOperationMetadata>>;

Check the status of the long running operation returned by `importIdentityMappings()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.cloud.discoveryengine.v1beta.ImportIdentityMappingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.importidentitymappingsresponse), [protos.google.cloud.discoveryengine.v1beta.IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.identitymappingentryoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The inline source to import identity mapping entries from.
       */
      // const inlineSource = {}
      /**
       *  Required. The name of the Identity Mapping Store to import Identity Mapping
       *  Entries to. Format:
       *  `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`
       */
      // const identityMappingStore = 'abc123'
    
      // Imports the Discoveryengine library
      const {IdentityMappingStoreServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callImportIdentityMappings() {
        // Construct request
        const request = {
          identityMappingStore,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.importIdentityMappings(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportIdentityMappings();
    
    

### checkPurgeIdentityMappingsProgress(name)
    
    
    checkPurgeIdentityMappingsProgress(name: string): Promise<LROperation<protos.google.protobuf.Empty, protos.google.cloud.discoveryengine.v1beta.IdentityMappingEntryOperationMetadata>>;

Check the status of the long running operation returned by `purgeIdentityMappings()`.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
The operation name that will be passed.  
**Returns**  
---  
**Type** | **Description**  
`Promise<LROperation<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), [protos.google.cloud.discoveryengine.v1beta.IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.identitymappingentryoperationmetadata)>>` | {Promise} - The promise which resolves to an object. The decoded operation object has result and metadata field to get information from. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The inline source to purge identity mapping entries from.
       */
      // const inlineSource = {}
      /**
       *  Required. The name of the Identity Mapping Store to purge Identity Mapping
       *  Entries from. Format:
       *  `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`
       */
      // const identityMappingStore = 'abc123'
      /**
       *  Filter matching identity mappings to purge.
       *  The eligible field for filtering is:
       *  * `update_time`: in ISO 8601 "zulu" format.
       *  * `external_id`
       *  Examples:
       *  * Deleting all identity mappings updated in a time range:
       *    `update_time > "2012-04-23T18:25:43.511Z" AND update_time < *="" "2012-04-23t18:30:43.511z"`="" *="" *="" deleting="" all="" identity="" mappings="" for="" a="" given="" external_id:="" *="" `external_id="id1" `="" *="" *="" deleting="" all="" identity="" mappings="" inside="" an="" identity="" mapping="" store:="" *="" `*`="" *="" the="" filtering="" fields="" are="" assumed="" to="" have="" an="" implicit="" and.="" *="" should="" not="" be="" used="" with="" source.="" an="" error="" will="" be="" thrown,="" if="" both="" are="" *="" provided.="" */="" const="" filter='abc123' *="" *="" actually="" performs="" the="" purge.="" if="" `force`="" is="" set="" to="" false,="" return="" the="" *="" expected="" purge="" count="" without="" deleting="" any="" identity="" mappings.="" this="" field="" is="" *="" only="" supported="" for="" purge="" with="" filter.="" for="" input="" source="" this="" field="" is="" *="" ignored="" and="" data="" will="" be="" purged="" regardless="" of="" the="" value="" of="" this="" field.="" */="" const="" force="true" imports="" the="" discoveryengine="" library="" const="" {identitymappingstoreserviceclient}="require('@google-cloud/discoveryengine').v1beta;" instantiates="" a="" client="" const="" discoveryengineclient="new" identitymappingstoreserviceclient();="" async="" function="" callpurgeidentitymappings()="" {="" construct="" request="" const="" request="{" identitymappingstore,="" };="" run="" request="" const="" [operation]="await" discoveryengineclient.purgeidentitymappings(request);="" const="" [response]="await" operation.promise();="" console.log(response);="" }="" callpurgeidentitymappings();="">

### close()
    
    
    close(): Promise<void>;

Terminate the gRPC channel and close the client.

The client will no longer be usable and all future behavior is undefined.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise} A promise that resolves when the client is closed.  
  
### createIdentityMappingStore(request, options)
    
    
    createIdentityMappingStore(request?: protos.google.cloud.discoveryengine.v1beta.ICreateIdentityMappingStoreRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore,
            (protos.google.cloud.discoveryengine.v1beta.ICreateIdentityMappingStoreRequest | undefined),
            {} | undefined
        ]>;

Creates a new Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateidentitymappingstorerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingstore), ([protos.google.cloud.discoveryengine.v1beta.ICreateIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateidentitymappingstorerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [IdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.identitymappingstore). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Resource name of the CmekConfig to use for protecting this Identity
       *  Mapping Store.
       */
      // const cmekConfigName = 'abc123'
      /**
       *  Identity Mapping Store without CMEK protections. If a default CmekConfig
       *  is set for the project, setting this field will override the default
       *  CmekConfig as well.
       */
      // const disableCmek = true
      /**
       *  Required. The parent collection resource name, such as
       *  `projects/{project}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Required. The ID of the Identity Mapping Store to create.
       *  The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores
       *  (_), and hyphens (-). The maximum length is 63 characters.
       */
      // const identityMappingStoreId = 'abc123'
      /**
       *  Required. The Identity Mapping Store to create.
       */
      // const identityMappingStore = {}
    
      // Imports the Discoveryengine library
      const {IdentityMappingStoreServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callCreateIdentityMappingStore() {
        // Construct request
        const request = {
          parent,
          identityMappingStoreId,
          identityMappingStore,
        };
    
        // Run request
        const response = await discoveryengineClient.createIdentityMappingStore(request);
        console.log(response);
      }
    
      callCreateIdentityMappingStore();
    
    

### createIdentityMappingStore(request, options, callback)
    
    
    createIdentityMappingStore(request: protos.google.cloud.discoveryengine.v1beta.ICreateIdentityMappingStoreRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore, protos.google.cloud.discoveryengine.v1beta.ICreateIdentityMappingStoreRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateidentitymappingstorerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingstore), [protos.google.cloud.discoveryengine.v1beta.ICreateIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateidentitymappingstorerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createIdentityMappingStore(request, callback)
    
    
    createIdentityMappingStore(request: protos.google.cloud.discoveryengine.v1beta.ICreateIdentityMappingStoreRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore, protos.google.cloud.discoveryengine.v1beta.ICreateIdentityMappingStoreRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateidentitymappingstorerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingstore), [protos.google.cloud.discoveryengine.v1beta.ICreateIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateidentitymappingstorerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteIdentityMappingStore(request, options)
    
    
    deleteIdentityMappingStore(request?: protos.google.cloud.discoveryengine.v1beta.IDeleteIdentityMappingStoreRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1beta.IDeleteIdentityMappingStoreMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Deletes the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteidentitymappingstorerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1beta.IDeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteidentitymappingstoremetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Identity Mapping Store to delete.
       *  Format:
       *  `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {IdentityMappingStoreServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callDeleteIdentityMappingStore() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.deleteIdentityMappingStore(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteIdentityMappingStore();
    
    

### deleteIdentityMappingStore(request, options, callback)
    
    
    deleteIdentityMappingStore(request: protos.google.cloud.discoveryengine.v1beta.IDeleteIdentityMappingStoreRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1beta.IDeleteIdentityMappingStoreMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteidentitymappingstorerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1beta.IDeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteidentitymappingstoremetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteIdentityMappingStore(request, callback)
    
    
    deleteIdentityMappingStore(request: protos.google.cloud.discoveryengine.v1beta.IDeleteIdentityMappingStoreRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1beta.IDeleteIdentityMappingStoreMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteidentitymappingstorerequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1beta.IDeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ideleteidentitymappingstoremetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteOperation(request, optionsOrCallback, callback)
    
    
    deleteOperation(request: protos.google.longrunning.DeleteOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.protobuf.Empty, protos.google.longrunning.DeleteOperationRequest, {} | null | undefined>): Promise<protos.google.protobuf.Empty>;

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

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
  
### getIdentityMappingStore(request, options)
    
    
    getIdentityMappingStore(request?: protos.google.cloud.discoveryengine.v1beta.IGetIdentityMappingStoreRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore,
            (protos.google.cloud.discoveryengine.v1beta.IGetIdentityMappingStoreRequest | undefined),
            {} | undefined
        ]>;

Gets the Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetidentitymappingstorerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingstore), ([protos.google.cloud.discoveryengine.v1beta.IGetIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetidentitymappingstorerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [IdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.identitymappingstore). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Identity Mapping Store to get.
       *  Format:
       *  `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`
       */
      // const name = 'abc123'
    
      // Imports the Discoveryengine library
      const {IdentityMappingStoreServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callGetIdentityMappingStore() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await discoveryengineClient.getIdentityMappingStore(request);
        console.log(response);
      }
    
      callGetIdentityMappingStore();
    
    

### getIdentityMappingStore(request, options, callback)
    
    
    getIdentityMappingStore(request: protos.google.cloud.discoveryengine.v1beta.IGetIdentityMappingStoreRequest, options: CallOptions, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore, protos.google.cloud.discoveryengine.v1beta.IGetIdentityMappingStoreRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetidentitymappingstorerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingstore), [protos.google.cloud.discoveryengine.v1beta.IGetIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetidentitymappingstorerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIdentityMappingStore(request, callback)
    
    
    getIdentityMappingStore(request: protos.google.cloud.discoveryengine.v1beta.IGetIdentityMappingStoreRequest, callback: Callback<protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore, protos.google.cloud.discoveryengine.v1beta.IGetIdentityMappingStoreRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetidentitymappingstorerequest)`   
  
`callback` |  `Callback<[protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingstore), [protos.google.cloud.discoveryengine.v1beta.IGetIdentityMappingStoreRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetidentitymappingstorerequest) | null | undefined, {} | null | undefined>`   
  
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
    

### getOperation(request, optionsOrCallback, callback)
    
    
    getOperation(request: protos.google.longrunning.GetOperationRequest, optionsOrCallback?: gax.CallOptions | Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>, callback?: Callback<protos.google.longrunning.Operation, protos.google.longrunning.GetOperationRequest, {} | null | undefined>): Promise<[protos.google.longrunning.Operation]>;

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)]>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    const name = '';
    const [response] = await client.getOperation({name});
    // doThingsWith(response)
    

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
  
### groundingConfigPath(project, location, groundingConfig)
    
    
    groundingConfigPath(project: string, location: string, groundingConfig: string): string;

Return a fully-qualified groundingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`groundingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### identityMappingStorePath(project, location, identityMappingStore)
    
    
    identityMappingStorePath(project: string, location: string, identityMappingStore: string): string;

Return a fully-qualified identityMappingStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`identityMappingStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### importIdentityMappings(request, options)
    
    
    importIdentityMappings(request?: protos.google.cloud.discoveryengine.v1beta.IImportIdentityMappingsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.cloud.discoveryengine.v1beta.IImportIdentityMappingsResponse, protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Imports a list of Identity Mapping Entries to an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iimportidentitymappingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.cloud.discoveryengine.v1beta.IImportIdentityMappingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iimportidentitymappingsresponse), [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingentryoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The inline source to import identity mapping entries from.
       */
      // const inlineSource = {}
      /**
       *  Required. The name of the Identity Mapping Store to import Identity Mapping
       *  Entries to. Format:
       *  `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`
       */
      // const identityMappingStore = 'abc123'
    
      // Imports the Discoveryengine library
      const {IdentityMappingStoreServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callImportIdentityMappings() {
        // Construct request
        const request = {
          identityMappingStore,
        };
    
        // Run request
        const [operation] = await discoveryengineClient.importIdentityMappings(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callImportIdentityMappings();
    
    

### importIdentityMappings(request, options, callback)
    
    
    importIdentityMappings(request: protos.google.cloud.discoveryengine.v1beta.IImportIdentityMappingsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1beta.IImportIdentityMappingsResponse, protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iimportidentitymappingsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1beta.IImportIdentityMappingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iimportidentitymappingsresponse), [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingentryoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importIdentityMappings(request, callback)
    
    
    importIdentityMappings(request: protos.google.cloud.discoveryengine.v1beta.IImportIdentityMappingsRequest, callback: Callback<LROperation<protos.google.cloud.discoveryengine.v1beta.IImportIdentityMappingsResponse, protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iimportidentitymappingsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.cloud.discoveryengine.v1beta.IImportIdentityMappingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iimportidentitymappingsresponse), [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingentryoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
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
  
### licenseConfigPath(project, location, licenseConfig)
    
    
    licenseConfigPath(project: string, location: string, licenseConfig: string): string;

Return a fully-qualified licenseConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`licenseConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### listIdentityMappings(request, options)
    
    
    listIdentityMappings(request?: protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntry[],
            protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest | null,
            protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsResponse
        ]>;

Lists Identity Mappings in an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntry](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingentry)[], [protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsrequest) | null, [protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [IdentityMappingEntry](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.identitymappingentry). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listIdentityMappingsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listIdentityMappings(request, options, callback)
    
    
    listIdentityMappings(request: protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest, protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsResponse | null | undefined, protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsrequest), [protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntry](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listIdentityMappings(request, callback)
    
    
    listIdentityMappings(request: protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest, protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsResponse | null | undefined, protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntry>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsrequest), [protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntry](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingentry)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listIdentityMappingsAsync(request, options)
    
    
    listIdentityMappingsAsync(request?: protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntry>;

Equivalent to `listIdentityMappings`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntry](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingentry)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [IdentityMappingEntry](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.identitymappingentry). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the Identity Mapping Store to list Identity Mapping
       *  Entries in. Format:
       *  `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`
       */
      // const identityMappingStore = 'abc123'
      /**
       *  Maximum number of IdentityMappings to return. If unspecified, defaults
       *  to 2000. The maximum allowed value is 10000. Values above 10000 will be
       *  coerced to 10000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListIdentityMappings` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `ListIdentityMappings` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Discoveryengine library
      const {IdentityMappingStoreServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callListIdentityMappings() {
        // Construct request
        const request = {
          identityMappingStore,
        };
    
        // Run request
        const iterable = discoveryengineClient.listIdentityMappingsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListIdentityMappings();
    
    

### listIdentityMappingsStream(request, options)
    
    
    listIdentityMappingsStream(request?: protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingsRequest, options?: CallOptions): Transform;

Equivalent to `listIdentityMappings`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [IdentityMappingEntry](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.identitymappingentry) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listIdentityMappingsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listIdentityMappingStores(request, options)
    
    
    listIdentityMappingStores(request?: protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest, options?: CallOptions): Promise<[
            protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore[],
            protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest | null,
            protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresResponse
        ]>;

Lists all Identity Mapping Stores.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIdentityMappingStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingstore)[], [protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresrequest) | null, [protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [IdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.identitymappingstore). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listIdentityMappingStoresAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listIdentityMappingStores(request, options, callback)
    
    
    listIdentityMappingStores(request: protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest, protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresResponse | null | undefined, protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIdentityMappingStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresrequest), [protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingstore)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listIdentityMappingStores(request, callback)
    
    
    listIdentityMappingStores(request: protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest, callback: PaginationCallback<protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest, protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresResponse | null | undefined, protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIdentityMappingStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresrequest), [protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresresponse) | null | undefined, [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingstore)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listIdentityMappingStoresAsync(request, options)
    
    
    listIdentityMappingStoresAsync(request?: protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore>;

Equivalent to `listIdentityMappingStores`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIdentityMappingStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.discoveryengine.v1beta.IIdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingstore)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [IdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.identitymappingstore). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent of the Identity Mapping Stores to list.
       *  Format:
       *  `projects/{project}/locations/{location}`.
       */
      // const parent = 'abc123'
      /**
       *  Maximum number of IdentityMappingStores to return. If unspecified, defaults
       *  to 100. The maximum allowed value is 1000. Values above 1000 will be
       *  coerced to 1000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListIdentityMappingStores` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to
       *  `ListIdentityMappingStores` must match the call that provided the page
       *  token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Discoveryengine library
      const {IdentityMappingStoreServiceClient} = require('[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const discoveryengineClient = new [IdentityMappingStoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)();
    
      async function callListIdentityMappingStores() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = discoveryengineClient.listIdentityMappingStoresAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListIdentityMappingStores();
    
    

### listIdentityMappingStoresStream(request, options)
    
    
    listIdentityMappingStoresStream(request?: protos.google.cloud.discoveryengine.v1beta.IListIdentityMappingStoresRequest, options?: CallOptions): Transform;

Equivalent to `listIdentityMappingStores`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIdentityMappingStoresRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistidentitymappingstoresrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [IdentityMappingStore](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.identitymappingstore) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listIdentityMappingStoresAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
    

### listOperationsAsync(request, options)
    
    
    listOperationsAsync(request: protos.google.longrunning.ListOperationsRequest, options?: gax.CallOptions): AsyncIterable<protos.google.longrunning.IOperation>;

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. Returns an iterable object.

For-await-of syntax is used with the iterable to recursively get response element on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

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
  
### matchAssistAnswerFromAssistAnswerName(assistAnswerName)
    
    
    matchAssistAnswerFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the assist_answer from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the assist_answer.  
  
### matchAssistantFromAssistantName(assistantName)
    
    
    matchAssistantFromAssistantName(assistantName: string): string | number;

Parse the assistant from Assistant resource.

**Parameter**  
---  
**Name** | **Description**  
`assistantName` |  `string`   
A fully-qualified path representing Assistant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the assistant.  
  
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
  
### matchCmekConfigFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName)
    
    
    matchCmekConfigFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName: string): string | number;

Parse the cmek_config from ProjectLocationCmekConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCmekConfigsName` |  `string`   
A fully-qualified path representing project_location_cmekConfigs resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the cmek_config.  
  
### matchCollaborativeProjectFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchCollaborativeProjectFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the collaborative_project from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collaborative_project.  
  
### matchCollectionFromAssistAnswerName(assistAnswerName)
    
    
    matchCollectionFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the collection from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
### matchCollectionFromAssistantName(assistantName)
    
    
    matchCollectionFromAssistantName(assistantName: string): string | number;

Parse the collection from Assistant resource.

**Parameter**  
---  
**Name** | **Description**  
`assistantName` |  `string`   
A fully-qualified path representing Assistant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the collection.  
  
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
  
### matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName)
    
    
    matchCollectionFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the collection from ProjectLocationCollectionDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_sitemap resource.  
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
  
### matchCollectionFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchCollectionFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the collection from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
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
  
### matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName)
    
    
    matchDataStoreFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the data_store from ProjectLocationCollectionDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_sitemap resource.  
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
  
### matchDataStoreFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName)
    
    
    matchDataStoreFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the data_store from ProjectLocationDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_sitemap resource.  
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
  
### matchEngineFromAssistAnswerName(assistAnswerName)
    
    
    matchEngineFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the engine from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
### matchEngineFromAssistantName(assistantName)
    
    
    matchEngineFromAssistantName(assistantName: string): string | number;

Parse the engine from Assistant resource.

**Parameter**  
---  
**Name** | **Description**  
`assistantName` |  `string`   
A fully-qualified path representing Assistant resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the engine.  
  
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
  
### matchEngineFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchEngineFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the engine from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
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
  
### matchGroundingConfigFromGroundingConfigName(groundingConfigName)
    
    
    matchGroundingConfigFromGroundingConfigName(groundingConfigName: string): string | number;

Parse the grounding_config from GroundingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`groundingConfigName` |  `string`   
A fully-qualified path representing GroundingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the grounding_config.  
  
### matchIdentityMappingStoreFromIdentityMappingStoreName(identityMappingStoreName)
    
    
    matchIdentityMappingStoreFromIdentityMappingStoreName(identityMappingStoreName: string): string | number;

Parse the identity_mapping_store from IdentityMappingStore resource.

**Parameter**  
---  
**Name** | **Description**  
`identityMappingStoreName` |  `string`   
A fully-qualified path representing IdentityMappingStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the identity_mapping_store.  
  
### matchLicenseConfigFromLicenseConfigName(licenseConfigName)
    
    
    matchLicenseConfigFromLicenseConfigName(licenseConfigName: string): string | number;

Parse the license_config from LicenseConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`licenseConfigName` |  `string`   
A fully-qualified path representing LicenseConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the license_config.  
  
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
  
### matchLocationFromAssistAnswerName(assistAnswerName)
    
    
    matchLocationFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the location from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromAssistantName(assistantName)
    
    
    matchLocationFromAssistantName(assistantName: string): string | number;

Parse the location from Assistant resource.

**Parameter**  
---  
**Name** | **Description**  
`assistantName` |  `string`   
A fully-qualified path representing Assistant resource.  
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
  
### matchLocationFromGroundingConfigName(groundingConfigName)
    
    
    matchLocationFromGroundingConfigName(groundingConfigName: string): string | number;

Parse the location from GroundingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`groundingConfigName` |  `string`   
A fully-qualified path representing GroundingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromIdentityMappingStoreName(identityMappingStoreName)
    
    
    matchLocationFromIdentityMappingStoreName(identityMappingStoreName: string): string | number;

Parse the location from IdentityMappingStore resource.

**Parameter**  
---  
**Name** | **Description**  
`identityMappingStoreName` |  `string`   
A fully-qualified path representing IdentityMappingStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromLicenseConfigName(licenseConfigName)
    
    
    matchLocationFromLicenseConfigName(licenseConfigName: string): string | number;

Parse the location from LicenseConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`licenseConfigName` |  `string`   
A fully-qualified path representing LicenseConfig resource.  
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
  
### matchLocationFromProjectLocationCmekConfigName(projectLocationCmekConfigName)
    
    
    matchLocationFromProjectLocationCmekConfigName(projectLocationCmekConfigName: string): string | number;

Parse the location from ProjectLocationCmekConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCmekConfigName` |  `string`   
A fully-qualified path representing project_location_cmekConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName)
    
    
    matchLocationFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName: string): string | number;

Parse the location from ProjectLocationCmekConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCmekConfigsName` |  `string`   
A fully-qualified path representing project_location_cmekConfigs resource.  
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
  
### matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName)
    
    
    matchLocationFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the location from ProjectLocationCollectionDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_sitemap resource.  
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
  
### matchLocationFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchLocationFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the location from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
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
  
### matchLocationFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName)
    
    
    matchLocationFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the location from ProjectLocationDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_sitemap resource.  
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
  
### matchLocationFromUserStoreName(userStoreName)
    
    
    matchLocationFromUserStoreName(userStoreName: string): string | number;

Parse the location from UserStore resource.

**Parameter**  
---  
**Name** | **Description**  
`userStoreName` |  `string`   
A fully-qualified path representing UserStore resource.  
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
  
### matchProjectFromAssistAnswerName(assistAnswerName)
    
    
    matchProjectFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the project from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAssistantName(assistantName)
    
    
    matchProjectFromAssistantName(assistantName: string): string | number;

Parse the project from Assistant resource.

**Parameter**  
---  
**Name** | **Description**  
`assistantName` |  `string`   
A fully-qualified path representing Assistant resource.  
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
  
### matchProjectFromGroundingConfigName(groundingConfigName)
    
    
    matchProjectFromGroundingConfigName(groundingConfigName: string): string | number;

Parse the project from GroundingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`groundingConfigName` |  `string`   
A fully-qualified path representing GroundingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromIdentityMappingStoreName(identityMappingStoreName)
    
    
    matchProjectFromIdentityMappingStoreName(identityMappingStoreName: string): string | number;

Parse the project from IdentityMappingStore resource.

**Parameter**  
---  
**Name** | **Description**  
`identityMappingStoreName` |  `string`   
A fully-qualified path representing IdentityMappingStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromLicenseConfigName(licenseConfigName)
    
    
    matchProjectFromLicenseConfigName(licenseConfigName: string): string | number;

Parse the project from LicenseConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`licenseConfigName` |  `string`   
A fully-qualified path representing LicenseConfig resource.  
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
  
### matchProjectFromProjectLocationCmekConfigName(projectLocationCmekConfigName)
    
    
    matchProjectFromProjectLocationCmekConfigName(projectLocationCmekConfigName: string): string | number;

Parse the project from ProjectLocationCmekConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCmekConfigName` |  `string`   
A fully-qualified path representing project_location_cmekConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName)
    
    
    matchProjectFromProjectLocationCmekConfigsName(projectLocationCmekConfigsName: string): string | number;

Parse the project from ProjectLocationCmekConfigs resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCmekConfigsName` |  `string`   
A fully-qualified path representing project_location_cmekConfigs resource.  
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
  
### matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName)
    
    
    matchProjectFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the project from ProjectLocationCollectionDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_sitemap resource.  
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
  
### matchProjectFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchProjectFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the project from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
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
  
### matchProjectFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName)
    
    
    matchProjectFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the project from ProjectLocationDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_sitemap resource.  
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
  
### matchProjectFromUserStoreName(userStoreName)
    
    
    matchProjectFromUserStoreName(userStoreName: string): string | number;

Parse the project from UserStore resource.

**Parameter**  
---  
**Name** | **Description**  
`userStoreName` |  `string`   
A fully-qualified path representing UserStore resource.  
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
  
### matchSessionFromAssistAnswerName(assistAnswerName)
    
    
    matchSessionFromAssistAnswerName(assistAnswerName: string): string | number;

Parse the session from AssistAnswer resource.

**Parameter**  
---  
**Name** | **Description**  
`assistAnswerName` |  `string`   
A fully-qualified path representing AssistAnswer resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the session.  
  
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
  
### matchSessionFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName)
    
    
    matchSessionFromProjectLocationCollectionEngineCollaborativeProjectSessionsName(projectLocationCollectionEngineCollaborativeProjectSessionsName: string): string | number;

Parse the session from ProjectLocationCollectionEngineCollaborativeProjectSessions resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionEngineCollaborativeProjectSessionsName` |  `string`   
A fully-qualified path representing project_location_collection_engine_collaborative_project_sessions resource.  
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
  
### matchSitemapFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName)
    
    
    matchSitemapFromProjectLocationCollectionDataStoreSiteSearchEngineSitemapName(projectLocationCollectionDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the sitemap from ProjectLocationCollectionDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationCollectionDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_collection_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sitemap.  
  
### matchSitemapFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName)
    
    
    matchSitemapFromProjectLocationDataStoreSiteSearchEngineSitemapName(projectLocationDataStoreSiteSearchEngineSitemapName: string): string | number;

Parse the sitemap from ProjectLocationDataStoreSiteSearchEngineSitemap resource.

**Parameter**  
---  
**Name** | **Description**  
`projectLocationDataStoreSiteSearchEngineSitemapName` |  `string`   
A fully-qualified path representing project_location_data_store_siteSearchEngine_sitemap resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the sitemap.  
  
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
  
### matchUserStoreFromUserStoreName(userStoreName)
    
    
    matchUserStoreFromUserStoreName(userStoreName: string): string | number;

Parse the user_store from UserStore resource.

**Parameter**  
---  
**Name** | **Description**  
`userStoreName` |  `string`   
A fully-qualified path representing UserStore resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the user_store.  
  
### projectLocationCmekConfigPath(project, location)
    
    
    projectLocationCmekConfigPath(project: string, location: string): string;

Return a fully-qualified projectLocationCmekConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### projectLocationCmekConfigsPath(project, location, cmekConfig)
    
    
    projectLocationCmekConfigsPath(project: string, location: string, cmekConfig: string): string;

Return a fully-qualified projectLocationCmekConfigs resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`cmekConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
  
### projectLocationCollectionDataStoreSiteSearchEngineSitemapPath(project, location, collection, dataStore, sitemap)
    
    
    projectLocationCollectionDataStoreSiteSearchEngineSitemapPath(project: string, location: string, collection: string, dataStore: string, sitemap: string): string;

Return a fully-qualified projectLocationCollectionDataStoreSiteSearchEngineSitemap resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`dataStore` |  `string`   
  
`sitemap` |  `string`   
  
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
  
### projectLocationCollectionEngineCollaborativeProjectSessionsPath(project, location, collection, engine, collaborativeProject, session)
    
    
    projectLocationCollectionEngineCollaborativeProjectSessionsPath(project: string, location: string, collection: string, engine: string, collaborativeProject: string, session: string): string;

Return a fully-qualified projectLocationCollectionEngineCollaborativeProjectSessions resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`collection` |  `string`   
  
`engine` |  `string`   
  
`collaborativeProject` |  `string`   
  
`session` |  `string`   
  
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
  
### projectLocationDataStoreSiteSearchEngineSitemapPath(project, location, dataStore, sitemap)
    
    
    projectLocationDataStoreSiteSearchEngineSitemapPath(project: string, location: string, dataStore: string, sitemap: string): string;

Return a fully-qualified projectLocationDataStoreSiteSearchEngineSitemap resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`dataStore` |  `string`   
  
`sitemap` |  `string`   
  
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
  
### purgeIdentityMappings(request, options)
    
    
    purgeIdentityMappings(request?: protos.google.cloud.discoveryengine.v1beta.IPurgeIdentityMappingsRequest, options?: CallOptions): Promise<[
            LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata>,
            protos.google.longrunning.IOperation | undefined,
            {} | undefined
        ]>;

Purges specified or all Identity Mapping Entries from an Identity Mapping Store.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ipurgeidentitymappingsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingentryoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing a long running operation. Its `promise()` method returns a promise you can `await` for. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The inline source to purge identity mapping entries from.
       */
      // const inlineSource = {}
      /**
       *  Required. The name of the Identity Mapping Store to purge Identity Mapping
       *  Entries from. Format:
       *  `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`
       */
      // const identityMappingStore = 'abc123'
      /**
       *  Filter matching identity mappings to purge.
       *  The eligible field for filtering is:
       *  * `update_time`: in ISO 8601 "zulu" format.
       *  * `external_id`
       *  Examples:
       *  * Deleting all identity mappings updated in a time range:
       *    `update_time > "2012-04-23T18:25:43.511Z" AND update_time < *="" "2012-04-23t18:30:43.511z"`="" *="" *="" deleting="" all="" identity="" mappings="" for="" a="" given="" external_id:="" *="" `external_id="id1" `="" *="" *="" deleting="" all="" identity="" mappings="" inside="" an="" identity="" mapping="" store:="" *="" `*`="" *="" the="" filtering="" fields="" are="" assumed="" to="" have="" an="" implicit="" and.="" *="" should="" not="" be="" used="" with="" source.="" an="" error="" will="" be="" thrown,="" if="" both="" are="" *="" provided.="" */="" const="" filter='abc123' *="" *="" actually="" performs="" the="" purge.="" if="" `force`="" is="" set="" to="" false,="" return="" the="" *="" expected="" purge="" count="" without="" deleting="" any="" identity="" mappings.="" this="" field="" is="" *="" only="" supported="" for="" purge="" with="" filter.="" for="" input="" source="" this="" field="" is="" *="" ignored="" and="" data="" will="" be="" purged="" regardless="" of="" the="" value="" of="" this="" field.="" */="" const="" force="true" imports="" the="" discoveryengine="" library="" const="" {identitymappingstoreserviceclient}="require('@google-cloud/discoveryengine').v1beta;" instantiates="" a="" client="" const="" discoveryengineclient="new" identitymappingstoreserviceclient();="" async="" function="" callpurgeidentitymappings()="" {="" construct="" request="" const="" request="{" identitymappingstore,="" };="" run="" request="" const="" [operation]="await" discoveryengineclient.purgeidentitymappings(request);="" const="" [response]="await" operation.promise();="" console.log(response);="" }="" callpurgeidentitymappings();="">

### purgeIdentityMappings(request, options, callback)
    
    
    purgeIdentityMappings(request: protos.google.cloud.discoveryengine.v1beta.IPurgeIdentityMappingsRequest, options: CallOptions, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ipurgeidentitymappingsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingentryoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### purgeIdentityMappings(request, callback)
    
    
    purgeIdentityMappings(request: protos.google.cloud.discoveryengine.v1beta.IPurgeIdentityMappingsRequest, callback: Callback<LROperation<protos.google.protobuf.IEmpty, protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata>, protos.google.longrunning.IOperation | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPurgeIdentityMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ipurgeidentitymappingsrequest)`   
  
`callback` |  `Callback<LROperation<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.protobuf.iempty), [protos.google.cloud.discoveryengine.v1beta.IIdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.iidentitymappingentryoperationmetadata)>, [protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.ioperation) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### userStorePath(project, location, userStore)
    
    
    userStorePath(project: string, location: string, userStore: string): string;

Return a fully-qualified userStore resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`userStore` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
