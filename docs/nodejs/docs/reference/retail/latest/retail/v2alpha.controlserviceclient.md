---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/v2alpha.controlserviceclient
title: Class v2alpha.ControlServiceClient (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:02:36.415714+00:00
---

# Class v2alpha.ControlServiceClient (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/v2alpha.controlserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v2alpha.ControlServiceClient (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Service for modifying Control. v2alpha

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of ControlServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new ControlServiceClient({fallback: true}, gax); ```  
  
## Properties 

### apiEndpoint
    
    
    get apiEndpoint(): string;

The DNS address for this API service.

### apiEndpoint
    
    
    static get apiEndpoint(): string;

The DNS address for this API service - same as servicePath.

### auth
    
    
    auth: gax.GoogleAuth;

### controlServiceStub
    
    
    controlServiceStub?: Promise<{
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

### alertConfigPath(project)
    
    
    alertConfigPath(project: string): string;

Return a fully-qualified alertConfig resource name string.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### attributesConfigPath(project, location, catalog)
    
    
    attributesConfigPath(project: string, location: string, catalog: string): string;

Return a fully-qualified attributesConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### branchPath(project, location, catalog, branch)
    
    
    branchPath(project: string, location: string, catalog: string, branch: string): string;

Return a fully-qualified branch resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`branch` |  `string`   
  
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
`request` |  `[CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.canceloperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty), {} | undefined | null>`   
  
`callback` |  `Callback<[protos.google.longrunning.CancelOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.canceloperationrequest), [protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty), {} | undefined | null>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.cancelOperation({name: ''});
    

### catalogPath(project, location, catalog)
    
    
    catalogPath(project: string, location: string, catalog: string): string;

Return a fully-qualified catalog resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
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
  
### completionConfigPath(project, location, catalog)
    
    
    completionConfigPath(project: string, location: string, catalog: string): string;

Return a fully-qualified completionConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### controlPath(project, location, catalog, control)
    
    
    controlPath(project: string, location: string, catalog: string, control: string): string;

Return a fully-qualified control resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`control` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### createControl(request, options)
    
    
    createControl(request?: protos.google.cloud.retail.v2alpha.ICreateControlRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2alpha.IControl,
            protos.google.cloud.retail.v2alpha.ICreateControlRequest | undefined,
            {} | undefined
        ]>;

Creates a Control.

If the [Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control) to create already exists, an ALREADY_EXISTS error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreatecontrolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol), [protos.google.cloud.retail.v2alpha.ICreateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreatecontrolrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. Full resource name of parent catalog. Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The Control to create.
       */
      // const control = {}
      /**
       *  Required. The ID to use for the Control, which will become the final
       *  component of the Control's resource name.
       *  This value should be 4-63 characters, and valid characters
       *  are /[a-z][0-9]-_/.
       */
      // const controlId = 'abc123'
    
      // Imports the Retail library
      const {ControlServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ControlServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callCreateControl() {
        // Construct request
        const request = {
          parent,
          control,
          controlId,
        };
    
        // Run request
        const response = await retailClient.createControl(request);
        console.log(response);
      }
    
      callCreateControl();
    
    

### createControl(request, options, callback)
    
    
    createControl(request: protos.google.cloud.retail.v2alpha.ICreateControlRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2alpha.IControl, protos.google.cloud.retail.v2alpha.ICreateControlRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreatecontrolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol), [protos.google.cloud.retail.v2alpha.ICreateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreatecontrolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createControl(request, callback)
    
    
    createControl(request: protos.google.cloud.retail.v2alpha.ICreateControlRequest, callback: Callback<protos.google.cloud.retail.v2alpha.IControl, protos.google.cloud.retail.v2alpha.ICreateControlRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreatecontrolrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol), [protos.google.cloud.retail.v2alpha.ICreateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreatecontrolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteControl(request, options)
    
    
    deleteControl(request?: protos.google.cloud.retail.v2alpha.IDeleteControlRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.cloud.retail.v2alpha.IDeleteControlRequest | undefined,
            {} | undefined
        ]>;

Deletes a Control.

If the [Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control) to delete does not exist, a NOT_FOUND error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideletecontrolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.iempty), [protos.google.cloud.retail.v2alpha.IDeleteControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideletecontrolrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Control to delete. Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/controls/{control_id}`
       */
      // const name = 'abc123'
    
      // Imports the Retail library
      const {ControlServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ControlServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callDeleteControl() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await retailClient.deleteControl(request);
        console.log(response);
      }
    
      callDeleteControl();
    
    

### deleteControl(request, options, callback)
    
    
    deleteControl(request: protos.google.cloud.retail.v2alpha.IDeleteControlRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.retail.v2alpha.IDeleteControlRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideletecontrolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.iempty), [protos.google.cloud.retail.v2alpha.IDeleteControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideletecontrolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteControl(request, callback)
    
    
    deleteControl(request: protos.google.cloud.retail.v2alpha.IDeleteControlRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.cloud.retail.v2alpha.IDeleteControlRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideletecontrolrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.iempty), [protos.google.cloud.retail.v2alpha.IDeleteControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideletecontrolrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.deleteoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty), [protos.google.longrunning.DeleteOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.deleteoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. {Promise} - The promise which resolves when API call finishes. The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[protos.google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty)>` |   
**Example**
    
    
    const client = longrunning.operationsClient();
    await client.deleteOperation({name: ''});
    

### getControl(request, options)
    
    
    getControl(request?: protos.google.cloud.retail.v2alpha.IGetControlRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2alpha.IControl,
            protos.google.cloud.retail.v2alpha.IGetControlRequest | undefined,
            {} | undefined
        ]>;

Gets a Control.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetcontrolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol), [protos.google.cloud.retail.v2alpha.IGetControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetcontrolrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Control to get. Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/controls/{control_id}`
       */
      // const name = 'abc123'
    
      // Imports the Retail library
      const {ControlServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ControlServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callGetControl() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await retailClient.getControl(request);
        console.log(response);
      }
    
      callGetControl();
    
    

### getControl(request, options, callback)
    
    
    getControl(request: protos.google.cloud.retail.v2alpha.IGetControlRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2alpha.IControl, protos.google.cloud.retail.v2alpha.IGetControlRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetcontrolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol), [protos.google.cloud.retail.v2alpha.IGetControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetcontrolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getControl(request, callback)
    
    
    getControl(request: protos.google.cloud.retail.v2alpha.IGetControlRequest, callback: Callback<protos.google.cloud.retail.v2alpha.IControl, protos.google.cloud.retail.v2alpha.IGetControlRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetcontrolrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol), [protos.google.cloud.retail.v2alpha.IGetControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetcontrolrequest) | null | undefined, {} | null | undefined>`   
  
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
`request` |  `[GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.getoperationrequest)`   
The request object that will be sent.  
`optionsOrCallback` |  `CallOptions | Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
  
`callback` |  `Callback<[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation), [protos.google.longrunning.GetOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.getoperationrequest), {} | null | undefined>`   
The function which will be called with the result of the API call. The second parameter to the callback is an object representing . {Promise} - The promise which resolves to an array. The first element of the array is an object representing . The promise has a method named "cancel" which cancels the ongoing API call.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[[protos.google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.operation)]>` |   
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
  
### listControls(request, options)
    
    
    listControls(request?: protos.google.cloud.retail.v2alpha.IListControlsRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2alpha.IControl[],
            protos.google.cloud.retail.v2alpha.IListControlsRequest | null,
            protos.google.cloud.retail.v2alpha.IListControlsResponse
        ]>;

Lists all Controls by their parent [Catalog](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.catalog).

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol)[], [protos.google.cloud.retail.v2alpha.IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsrequest) | null, [protos.google.cloud.retail.v2alpha.IListControlsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listControlsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listControls(request, options, callback)
    
    
    listControls(request: protos.google.cloud.retail.v2alpha.IListControlsRequest, options: CallOptions, callback: PaginationCallback<protos.google.cloud.retail.v2alpha.IListControlsRequest, protos.google.cloud.retail.v2alpha.IListControlsResponse | null | undefined, protos.google.cloud.retail.v2alpha.IControl>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.retail.v2alpha.IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsrequest), [protos.google.cloud.retail.v2alpha.IListControlsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsresponse) | null | undefined, [protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listControls(request, callback)
    
    
    listControls(request: protos.google.cloud.retail.v2alpha.IListControlsRequest, callback: PaginationCallback<protos.google.cloud.retail.v2alpha.IListControlsRequest, protos.google.cloud.retail.v2alpha.IListControlsResponse | null | undefined, protos.google.cloud.retail.v2alpha.IControl>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.cloud.retail.v2alpha.IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsrequest), [protos.google.cloud.retail.v2alpha.IListControlsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsresponse) | null | undefined, [protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listControlsAsync(request, options)
    
    
    listControlsAsync(request?: protos.google.cloud.retail.v2alpha.IListControlsRequest, options?: CallOptions): AsyncIterable<protos.google.cloud.retail.v2alpha.IControl>;

Equivalent to `listControls`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The catalog resource name. Format:
       *  `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}`
       */
      // const parent = 'abc123'
      /**
       *  Optional. Maximum number of results to return. If unspecified, defaults
       *  to 50. Max allowed value is 1000.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token, received from a previous `ListControls` call.
       *  Provide this to retrieve the subsequent page.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. A filter to apply on the list results. Supported features:
       *  * List all the products under the parent branch if
       *  filter google.cloud.retail.v2alpha.ListControlsRequest.filter  is unset.
       *  * List controls that are used in a single ServingConfig:
       *      'serving_config = "boosted_home_page_cvr"'
       */
      // const filter = 'abc123'
    
      // Imports the Retail library
      const {ControlServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ControlServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callListControls() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = retailClient.listControlsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListControls();
    
    

### listControlsStream(request, options)
    
    
    listControlsStream(request?: protos.google.cloud.retail.v2alpha.IListControlsRequest, options?: CallOptions): Transform;

Equivalent to `listControls`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listControlsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
`request` |  `[ListOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.listoperationsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Optional parameters. You can override the default settings for this call, e.g, timeout, retries, paginations, etc. See [gax.CallOptions](https://googleapis.github.io/gax-nodejs/global.html#CallOptions) for the details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.longrunning.IOperation](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.longrunning.ioperation)>` | {Object} An iterable Object that conforms to [iteration protocols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols).  
**Example**
    
    
    const client = longrunning.operationsClient();
    for await (const response of client.listOperationsAsync(request));
    // doThingsWith(response)
    

### loggingConfigPath(project)
    
    
    loggingConfigPath(project: string): string;

Return a fully-qualified loggingConfig resource name string.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### matchBranchFromBranchName(branchName)
    
    
    matchBranchFromBranchName(branchName: string): string | number;

Parse the branch from Branch resource.

**Parameter**  
---  
**Name** | **Description**  
`branchName` |  `string`   
A fully-qualified path representing Branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchBranchFromProductName(productName)
    
    
    matchBranchFromProductName(productName: string): string | number;

Parse the branch from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the branch.  
  
### matchCatalogFromAttributesConfigName(attributesConfigName)
    
    
    matchCatalogFromAttributesConfigName(attributesConfigName: string): string | number;

Parse the catalog from AttributesConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`attributesConfigName` |  `string`   
A fully-qualified path representing AttributesConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromBranchName(branchName)
    
    
    matchCatalogFromBranchName(branchName: string): string | number;

Parse the catalog from Branch resource.

**Parameter**  
---  
**Name** | **Description**  
`branchName` |  `string`   
A fully-qualified path representing Branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromCatalogName(catalogName)
    
    
    matchCatalogFromCatalogName(catalogName: string): string | number;

Parse the catalog from Catalog resource.

**Parameter**  
---  
**Name** | **Description**  
`catalogName` |  `string`   
A fully-qualified path representing Catalog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromCompletionConfigName(completionConfigName)
    
    
    matchCatalogFromCompletionConfigName(completionConfigName: string): string | number;

Parse the catalog from CompletionConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`completionConfigName` |  `string`   
A fully-qualified path representing CompletionConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromControlName(controlName)
    
    
    matchCatalogFromControlName(controlName: string): string | number;

Parse the catalog from Control resource.

**Parameter**  
---  
**Name** | **Description**  
`controlName` |  `string`   
A fully-qualified path representing Control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName)
    
    
    matchCatalogFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName: string): string | number;

Parse the catalog from MerchantCenterAccountLink resource.

**Parameter**  
---  
**Name** | **Description**  
`merchantCenterAccountLinkName` |  `string`   
A fully-qualified path representing MerchantCenterAccountLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromModelName(modelName)
    
    
    matchCatalogFromModelName(modelName: string): string | number;

Parse the catalog from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromProductName(productName)
    
    
    matchCatalogFromProductName(productName: string): string | number;

Parse the catalog from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchCatalogFromServingConfigName(servingConfigName)
    
    
    matchCatalogFromServingConfigName(servingConfigName: string): string | number;

Parse the catalog from ServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`servingConfigName` |  `string`   
A fully-qualified path representing ServingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the catalog.  
  
### matchControlFromControlName(controlName)
    
    
    matchControlFromControlName(controlName: string): string | number;

Parse the control from Control resource.

**Parameter**  
---  
**Name** | **Description**  
`controlName` |  `string`   
A fully-qualified path representing Control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the control.  
  
### matchLocationFromAttributesConfigName(attributesConfigName)
    
    
    matchLocationFromAttributesConfigName(attributesConfigName: string): string | number;

Parse the location from AttributesConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`attributesConfigName` |  `string`   
A fully-qualified path representing AttributesConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromBranchName(branchName)
    
    
    matchLocationFromBranchName(branchName: string): string | number;

Parse the location from Branch resource.

**Parameter**  
---  
**Name** | **Description**  
`branchName` |  `string`   
A fully-qualified path representing Branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCatalogName(catalogName)
    
    
    matchLocationFromCatalogName(catalogName: string): string | number;

Parse the location from Catalog resource.

**Parameter**  
---  
**Name** | **Description**  
`catalogName` |  `string`   
A fully-qualified path representing Catalog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromCompletionConfigName(completionConfigName)
    
    
    matchLocationFromCompletionConfigName(completionConfigName: string): string | number;

Parse the location from CompletionConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`completionConfigName` |  `string`   
A fully-qualified path representing CompletionConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromControlName(controlName)
    
    
    matchLocationFromControlName(controlName: string): string | number;

Parse the location from Control resource.

**Parameter**  
---  
**Name** | **Description**  
`controlName` |  `string`   
A fully-qualified path representing Control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName)
    
    
    matchLocationFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName: string): string | number;

Parse the location from MerchantCenterAccountLink resource.

**Parameter**  
---  
**Name** | **Description**  
`merchantCenterAccountLinkName` |  `string`   
A fully-qualified path representing MerchantCenterAccountLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromModelName(modelName)
    
    
    matchLocationFromModelName(modelName: string): string | number;

Parse the location from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromProductName(productName)
    
    
    matchLocationFromProductName(productName: string): string | number;

Parse the location from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchLocationFromServingConfigName(servingConfigName)
    
    
    matchLocationFromServingConfigName(servingConfigName: string): string | number;

Parse the location from ServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`servingConfigName` |  `string`   
A fully-qualified path representing ServingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the location.  
  
### matchMerchantCenterAccountLinkFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName)
    
    
    matchMerchantCenterAccountLinkFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName: string): string | number;

Parse the merchant_center_account_link from MerchantCenterAccountLink resource.

**Parameter**  
---  
**Name** | **Description**  
`merchantCenterAccountLinkName` |  `string`   
A fully-qualified path representing MerchantCenterAccountLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the merchant_center_account_link.  
  
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
  
### matchProductFromProductName(productName)
    
    
    matchProductFromProductName(productName: string): string | number;

Parse the product from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the product.  
  
### matchProjectFromAlertConfigName(alertConfigName)
    
    
    matchProjectFromAlertConfigName(alertConfigName: string): string | number;

Parse the project from AlertConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`alertConfigName` |  `string`   
A fully-qualified path representing AlertConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromAttributesConfigName(attributesConfigName)
    
    
    matchProjectFromAttributesConfigName(attributesConfigName: string): string | number;

Parse the project from AttributesConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`attributesConfigName` |  `string`   
A fully-qualified path representing AttributesConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromBranchName(branchName)
    
    
    matchProjectFromBranchName(branchName: string): string | number;

Parse the project from Branch resource.

**Parameter**  
---  
**Name** | **Description**  
`branchName` |  `string`   
A fully-qualified path representing Branch resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCatalogName(catalogName)
    
    
    matchProjectFromCatalogName(catalogName: string): string | number;

Parse the project from Catalog resource.

**Parameter**  
---  
**Name** | **Description**  
`catalogName` |  `string`   
A fully-qualified path representing Catalog resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromCompletionConfigName(completionConfigName)
    
    
    matchProjectFromCompletionConfigName(completionConfigName: string): string | number;

Parse the project from CompletionConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`completionConfigName` |  `string`   
A fully-qualified path representing CompletionConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromControlName(controlName)
    
    
    matchProjectFromControlName(controlName: string): string | number;

Parse the project from Control resource.

**Parameter**  
---  
**Name** | **Description**  
`controlName` |  `string`   
A fully-qualified path representing Control resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromLoggingConfigName(loggingConfigName)
    
    
    matchProjectFromLoggingConfigName(loggingConfigName: string): string | number;

Parse the project from LoggingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`loggingConfigName` |  `string`   
A fully-qualified path representing LoggingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName)
    
    
    matchProjectFromMerchantCenterAccountLinkName(merchantCenterAccountLinkName: string): string | number;

Parse the project from MerchantCenterAccountLink resource.

**Parameter**  
---  
**Name** | **Description**  
`merchantCenterAccountLinkName` |  `string`   
A fully-qualified path representing MerchantCenterAccountLink resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromModelName(modelName)
    
    
    matchProjectFromModelName(modelName: string): string | number;

Parse the project from Model resource.

**Parameter**  
---  
**Name** | **Description**  
`modelName` |  `string`   
A fully-qualified path representing Model resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromProductName(productName)
    
    
    matchProjectFromProductName(productName: string): string | number;

Parse the project from Product resource.

**Parameter**  
---  
**Name** | **Description**  
`productName` |  `string`   
A fully-qualified path representing Product resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromRetailProjectName(retailProjectName)
    
    
    matchProjectFromRetailProjectName(retailProjectName: string): string | number;

Parse the project from RetailProject resource.

**Parameter**  
---  
**Name** | **Description**  
`retailProjectName` |  `string`   
A fully-qualified path representing RetailProject resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromServingConfigName(servingConfigName)
    
    
    matchProjectFromServingConfigName(servingConfigName: string): string | number;

Parse the project from ServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`servingConfigName` |  `string`   
A fully-qualified path representing ServingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchServingConfigFromServingConfigName(servingConfigName)
    
    
    matchServingConfigFromServingConfigName(servingConfigName: string): string | number;

Parse the serving_config from ServingConfig resource.

**Parameter**  
---  
**Name** | **Description**  
`servingConfigName` |  `string`   
A fully-qualified path representing ServingConfig resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the serving_config.  
  
### merchantCenterAccountLinkPath(project, location, catalog, merchantCenterAccountLink)
    
    
    merchantCenterAccountLinkPath(project: string, location: string, catalog: string, merchantCenterAccountLink: string): string;

Return a fully-qualified merchantCenterAccountLink resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`merchantCenterAccountLink` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### modelPath(project, location, catalog, model)
    
    
    modelPath(project: string, location: string, catalog: string, model: string): string;

Return a fully-qualified model resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`model` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### productPath(project, location, catalog, branch, product)
    
    
    productPath(project: string, location: string, catalog: string, branch: string, product: string): string;

Return a fully-qualified product resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`branch` |  `string`   
  
`product` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### retailProjectPath(project)
    
    
    retailProjectPath(project: string): string;

Return a fully-qualified retailProject resource name string.

**Parameter**  
---  
**Name** | **Description**  
`project` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### servingConfigPath(project, location, catalog, servingConfig)
    
    
    servingConfigPath(project: string, location: string, catalog: string, servingConfig: string): string;

Return a fully-qualified servingConfig resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`location` |  `string`   
  
`catalog` |  `string`   
  
`servingConfig` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateControl(request, options)
    
    
    updateControl(request?: protos.google.cloud.retail.v2alpha.IUpdateControlRequest, options?: CallOptions): Promise<[
            protos.google.cloud.retail.v2alpha.IControl,
            protos.google.cloud.retail.v2alpha.IUpdateControlRequest | undefined,
            {} | undefined
        ]>;

Updates a Control.

[Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control) cannot be set to a different oneof field, if so an INVALID_ARGUMENT is returned. If the [Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control) to update does not exist, a NOT_FOUND error is returned.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdatecontrolrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol), [protos.google.cloud.retail.v2alpha.IUpdateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdatecontrolrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The Control to update.
       */
      // const control = {}
      /**
       *  Indicates which fields in the provided
       *  Control google.cloud.retail.v2alpha.Control  to update. The following are
       *  NOT supported:
       *  * Control.name google.cloud.retail.v2alpha.Control.name 
       *  If not set or empty, all supported fields are updated.
       */
      // const updateMask = {}
    
      // Imports the Retail library
      const {ControlServiceClient} = require('[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)').v2alpha;
    
      // Instantiates a client
      const retailClient = new [ControlServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)();
    
      async function callUpdateControl() {
        // Construct request
        const request = {
          control,
        };
    
        // Run request
        const response = await retailClient.updateControl(request);
        console.log(response);
      }
    
      callUpdateControl();
    
    

### updateControl(request, options, callback)
    
    
    updateControl(request: protos.google.cloud.retail.v2alpha.IUpdateControlRequest, options: CallOptions, callback: Callback<protos.google.cloud.retail.v2alpha.IControl, protos.google.cloud.retail.v2alpha.IUpdateControlRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdatecontrolrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol), [protos.google.cloud.retail.v2alpha.IUpdateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdatecontrolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateControl(request, callback)
    
    
    updateControl(request: protos.google.cloud.retail.v2alpha.IUpdateControlRequest, callback: Callback<protos.google.cloud.retail.v2alpha.IControl, protos.google.cloud.retail.v2alpha.IUpdateControlRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdatecontrolrequest)`   
  
`callback` |  `Callback<[protos.google.cloud.retail.v2alpha.IControl](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icontrol), [protos.google.cloud.retail.v2alpha.IUpdateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdatecontrolrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
