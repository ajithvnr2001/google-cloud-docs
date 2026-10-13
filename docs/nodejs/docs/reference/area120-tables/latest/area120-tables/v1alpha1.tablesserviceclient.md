---
url: https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/v1alpha1.tablesserviceclient
title: Class v1alpha1.TablesServiceClient (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:26.253034+00:00
---

# Class v1alpha1.TablesServiceClient (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/v1alpha1.tablesserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1alpha1.TablesServiceClient (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  2.2.1  2.1.2  1.3.0  1.2.8 

The Tables Service provides an API for reading and updating tables. It defines the following resource model:

  * The API has a collection of [Table](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.table) resources, named `tables/*`

  * Each Table has a collection of [Row](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.row) resources, named `tables/* /rows/*`

  * The API has a collection of [Workspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.workspace) resources, named `workspaces/*`. v1alpha1




## Package

[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of TablesServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new TablesServiceClient({fallback: true}, gax); ```  
  
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

### scopes
    
    
    static get scopes(): string[];

The scopes needed to make gRPC calls for every method defined in this service.

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### tablesServiceStub
    
    
    tablesServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### batchCreateRows(request, options)
    
    
    batchCreateRows(request?: protos.google.area120.tables.v1alpha1.IBatchCreateRowsRequest, options?: CallOptions): Promise<[
            protos.google.area120.tables.v1alpha1.IBatchCreateRowsResponse,
            protos.google.area120.tables.v1alpha1.IBatchCreateRowsRequest | undefined,
            {} | undefined
        ]>;

Creates multiple rows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchcreaterowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.area120.tables.v1alpha1.IBatchCreateRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchcreaterowsresponse), [protos.google.area120.tables.v1alpha1.IBatchCreateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchcreaterowsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchCreateRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.batchcreaterowsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent table where the rows will be created.
       *  Format: tables/{table}
       */
      // const parent = 'abc123'
      /**
       *  Required. The request message specifying the rows to create.
       *  A maximum of 500 rows can be created in a single batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callBatchCreateRows() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const response = await tablesClient.batchCreateRows(request);
        console.log(response);
      }
    
      callBatchCreateRows();
    
    

### batchCreateRows(request, options, callback)
    
    
    batchCreateRows(request: protos.google.area120.tables.v1alpha1.IBatchCreateRowsRequest, options: CallOptions, callback: Callback<protos.google.area120.tables.v1alpha1.IBatchCreateRowsResponse, protos.google.area120.tables.v1alpha1.IBatchCreateRowsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchcreaterowsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IBatchCreateRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchcreaterowsresponse), [protos.google.area120.tables.v1alpha1.IBatchCreateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchcreaterowsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateRows(request, callback)
    
    
    batchCreateRows(request: protos.google.area120.tables.v1alpha1.IBatchCreateRowsRequest, callback: Callback<protos.google.area120.tables.v1alpha1.IBatchCreateRowsResponse, protos.google.area120.tables.v1alpha1.IBatchCreateRowsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchcreaterowsrequest)`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IBatchCreateRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchcreaterowsresponse), [protos.google.area120.tables.v1alpha1.IBatchCreateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchcreaterowsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteRows(request, options)
    
    
    batchDeleteRows(request?: protos.google.area120.tables.v1alpha1.IBatchDeleteRowsRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.area120.tables.v1alpha1.IBatchDeleteRowsRequest | undefined,
            {} | undefined
        ]>;

Deletes multiple rows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchdeleterowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.protobuf.iempty), [protos.google.area120.tables.v1alpha1.IBatchDeleteRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchdeleterowsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent table shared by all rows being deleted.
       *  Format: tables/{table}
       */
      // const parent = 'abc123'
      /**
       *  Required. The names of the rows to delete. All rows must belong to the parent table
       *  or else the entire batch will fail. A maximum of 500 rows can be deleted
       *  in a batch.
       *  Format: tables/{table}/rows/{row}
       */
      // const names = ['abc','def']
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callBatchDeleteRows() {
        // Construct request
        const request = {
          parent,
          names,
        };
    
        // Run request
        const response = await tablesClient.batchDeleteRows(request);
        console.log(response);
      }
    
      callBatchDeleteRows();
    
    

### batchDeleteRows(request, options, callback)
    
    
    batchDeleteRows(request: protos.google.area120.tables.v1alpha1.IBatchDeleteRowsRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.area120.tables.v1alpha1.IBatchDeleteRowsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchdeleterowsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.protobuf.iempty), [protos.google.area120.tables.v1alpha1.IBatchDeleteRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchdeleterowsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteRows(request, callback)
    
    
    batchDeleteRows(request: protos.google.area120.tables.v1alpha1.IBatchDeleteRowsRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.area120.tables.v1alpha1.IBatchDeleteRowsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchdeleterowsrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.protobuf.iempty), [protos.google.area120.tables.v1alpha1.IBatchDeleteRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchdeleterowsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateRows(request, options)
    
    
    batchUpdateRows(request?: protos.google.area120.tables.v1alpha1.IBatchUpdateRowsRequest, options?: CallOptions): Promise<[
            protos.google.area120.tables.v1alpha1.IBatchUpdateRowsResponse,
            protos.google.area120.tables.v1alpha1.IBatchUpdateRowsRequest | undefined,
            {} | undefined
        ]>;

Updates multiple rows.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchupdaterowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.area120.tables.v1alpha1.IBatchUpdateRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchupdaterowsresponse), [protos.google.area120.tables.v1alpha1.IBatchUpdateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchupdaterowsrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchUpdateRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.batchupdaterowsresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent table shared by all rows being updated.
       *  Format: tables/{table}
       */
      // const parent = 'abc123'
      /**
       *  Required. The request messages specifying the rows to update.
       *  A maximum of 500 rows can be modified in a single batch.
       */
      // const requests = [1,2,3,4]
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callBatchUpdateRows() {
        // Construct request
        const request = {
          parent,
          requests,
        };
    
        // Run request
        const response = await tablesClient.batchUpdateRows(request);
        console.log(response);
      }
    
      callBatchUpdateRows();
    
    

### batchUpdateRows(request, options, callback)
    
    
    batchUpdateRows(request: protos.google.area120.tables.v1alpha1.IBatchUpdateRowsRequest, options: CallOptions, callback: Callback<protos.google.area120.tables.v1alpha1.IBatchUpdateRowsResponse, protos.google.area120.tables.v1alpha1.IBatchUpdateRowsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchupdaterowsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IBatchUpdateRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchupdaterowsresponse), [protos.google.area120.tables.v1alpha1.IBatchUpdateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchupdaterowsrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateRows(request, callback)
    
    
    batchUpdateRows(request: protos.google.area120.tables.v1alpha1.IBatchUpdateRowsRequest, callback: Callback<protos.google.area120.tables.v1alpha1.IBatchUpdateRowsResponse, protos.google.area120.tables.v1alpha1.IBatchUpdateRowsRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchupdaterowsrequest)`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IBatchUpdateRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchupdaterowsresponse), [protos.google.area120.tables.v1alpha1.IBatchUpdateRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ibatchupdaterowsrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### createRow(request, options)
    
    
    createRow(request?: protos.google.area120.tables.v1alpha1.ICreateRowRequest, options?: CallOptions): Promise<[
            protos.google.area120.tables.v1alpha1.IRow,
            protos.google.area120.tables.v1alpha1.ICreateRowRequest | undefined,
            {} | undefined
        ]>;

Creates a row.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.icreaterowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow), [protos.google.area120.tables.v1alpha1.ICreateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.icreaterowrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Row](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.row). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent table where this row will be created.
       *  Format: tables/{table}
       */
      // const parent = 'abc123'
      /**
       *  Required. The row to create.
       */
      // const row = {}
      /**
       *  Optional. Column key to use for values in the row.
       *  Defaults to user entered name.
       */
      // const view = {}
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callCreateRow() {
        // Construct request
        const request = {
          parent,
          row,
        };
    
        // Run request
        const response = await tablesClient.createRow(request);
        console.log(response);
      }
    
      callCreateRow();
    
    

### createRow(request, options, callback)
    
    
    createRow(request: protos.google.area120.tables.v1alpha1.ICreateRowRequest, options: CallOptions, callback: Callback<protos.google.area120.tables.v1alpha1.IRow, protos.google.area120.tables.v1alpha1.ICreateRowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.icreaterowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow), [protos.google.area120.tables.v1alpha1.ICreateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.icreaterowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRow(request, callback)
    
    
    createRow(request: protos.google.area120.tables.v1alpha1.ICreateRowRequest, callback: Callback<protos.google.area120.tables.v1alpha1.IRow, protos.google.area120.tables.v1alpha1.ICreateRowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.icreaterowrequest)`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow), [protos.google.area120.tables.v1alpha1.ICreateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.icreaterowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRow(request, options)
    
    
    deleteRow(request?: protos.google.area120.tables.v1alpha1.IDeleteRowRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.area120.tables.v1alpha1.IDeleteRowRequest | undefined,
            {} | undefined
        ]>;

Deletes a row.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ideleterowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.protobuf.iempty), [protos.google.area120.tables.v1alpha1.IDeleteRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ideleterowrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the row to delete.
       *  Format: tables/{table}/rows/{row}
       */
      // const name = 'abc123'
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callDeleteRow() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await tablesClient.deleteRow(request);
        console.log(response);
      }
    
      callDeleteRow();
    
    

### deleteRow(request, options, callback)
    
    
    deleteRow(request: protos.google.area120.tables.v1alpha1.IDeleteRowRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.area120.tables.v1alpha1.IDeleteRowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ideleterowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.protobuf.iempty), [protos.google.area120.tables.v1alpha1.IDeleteRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ideleterowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRow(request, callback)
    
    
    deleteRow(request: protos.google.area120.tables.v1alpha1.IDeleteRowRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.area120.tables.v1alpha1.IDeleteRowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ideleterowrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.protobuf.iempty), [protos.google.area120.tables.v1alpha1.IDeleteRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ideleterowrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### getRow(request, options)
    
    
    getRow(request?: protos.google.area120.tables.v1alpha1.IGetRowRequest, options?: CallOptions): Promise<[
            protos.google.area120.tables.v1alpha1.IRow,
            protos.google.area120.tables.v1alpha1.IGetRowRequest | undefined,
            {} | undefined
        ]>;

Gets a row. Returns NOT_FOUND if the row does not exist in the table.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetrowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow), [protos.google.area120.tables.v1alpha1.IGetRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetrowrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Row](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.row). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the row to retrieve.
       *  Format: tables/{table}/rows/{row}
       */
      // const name = 'abc123'
      /**
       *  Optional. Column key to use for values in the row.
       *  Defaults to user entered name.
       */
      // const view = {}
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callGetRow() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await tablesClient.getRow(request);
        console.log(response);
      }
    
      callGetRow();
    
    

### getRow(request, options, callback)
    
    
    getRow(request: protos.google.area120.tables.v1alpha1.IGetRowRequest, options: CallOptions, callback: Callback<protos.google.area120.tables.v1alpha1.IRow, protos.google.area120.tables.v1alpha1.IGetRowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetrowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow), [protos.google.area120.tables.v1alpha1.IGetRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetrowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRow(request, callback)
    
    
    getRow(request: protos.google.area120.tables.v1alpha1.IGetRowRequest, callback: Callback<protos.google.area120.tables.v1alpha1.IRow, protos.google.area120.tables.v1alpha1.IGetRowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetrowrequest)`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow), [protos.google.area120.tables.v1alpha1.IGetRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetrowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTable(request, options)
    
    
    getTable(request?: protos.google.area120.tables.v1alpha1.IGetTableRequest, options?: CallOptions): Promise<[
            protos.google.area120.tables.v1alpha1.ITable,
            protos.google.area120.tables.v1alpha1.IGetTableRequest | undefined,
            {} | undefined
        ]>;

Gets a table. Returns NOT_FOUND if the table does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igettablerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.area120.tables.v1alpha1.ITable](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.itable), [protos.google.area120.tables.v1alpha1.IGetTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igettablerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Table](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.table). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the table to retrieve.
       *  Format: tables/{table}
       */
      // const name = 'abc123'
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callGetTable() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await tablesClient.getTable(request);
        console.log(response);
      }
    
      callGetTable();
    
    

### getTable(request, options, callback)
    
    
    getTable(request: protos.google.area120.tables.v1alpha1.IGetTableRequest, options: CallOptions, callback: Callback<protos.google.area120.tables.v1alpha1.ITable, protos.google.area120.tables.v1alpha1.IGetTableRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igettablerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.ITable](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.itable), [protos.google.area120.tables.v1alpha1.IGetTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igettablerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTable(request, callback)
    
    
    getTable(request: protos.google.area120.tables.v1alpha1.IGetTableRequest, callback: Callback<protos.google.area120.tables.v1alpha1.ITable, protos.google.area120.tables.v1alpha1.IGetTableRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igettablerequest)`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.ITable](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.itable), [protos.google.area120.tables.v1alpha1.IGetTableRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igettablerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkspace(request, options)
    
    
    getWorkspace(request?: protos.google.area120.tables.v1alpha1.IGetWorkspaceRequest, options?: CallOptions): Promise<[
            protos.google.area120.tables.v1alpha1.IWorkspace,
            protos.google.area120.tables.v1alpha1.IGetWorkspaceRequest | undefined,
            {} | undefined
        ]>;

Gets a workspace. Returns NOT_FOUND if the workspace does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetworkspacerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.area120.tables.v1alpha1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iworkspace), [protos.google.area120.tables.v1alpha1.IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetworkspacerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Workspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.workspace). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the workspace to retrieve.
       *  Format: workspaces/{workspace}
       */
      // const name = 'abc123'
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callGetWorkspace() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await tablesClient.getWorkspace(request);
        console.log(response);
      }
    
      callGetWorkspace();
    
    

### getWorkspace(request, options, callback)
    
    
    getWorkspace(request: protos.google.area120.tables.v1alpha1.IGetWorkspaceRequest, options: CallOptions, callback: Callback<protos.google.area120.tables.v1alpha1.IWorkspace, protos.google.area120.tables.v1alpha1.IGetWorkspaceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetworkspacerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iworkspace), [protos.google.area120.tables.v1alpha1.IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetworkspacerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkspace(request, callback)
    
    
    getWorkspace(request: protos.google.area120.tables.v1alpha1.IGetWorkspaceRequest, callback: Callback<protos.google.area120.tables.v1alpha1.IWorkspace, protos.google.area120.tables.v1alpha1.IGetWorkspaceRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetworkspacerequest)`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iworkspace), [protos.google.area120.tables.v1alpha1.IGetWorkspaceRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.igetworkspacerequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listRows(request, options)
    
    
    listRows(request?: protos.google.area120.tables.v1alpha1.IListRowsRequest, options?: CallOptions): Promise<[
            protos.google.area120.tables.v1alpha1.IRow[],
            protos.google.area120.tables.v1alpha1.IListRowsRequest | null,
            protos.google.area120.tables.v1alpha1.IListRowsResponse
        ]>;

Lists rows in a table. Returns NOT_FOUND if the table does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow)[], [protos.google.area120.tables.v1alpha1.IListRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsrequest) | null, [protos.google.area120.tables.v1alpha1.IListRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Row](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.row). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listRowsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listRows(request, options, callback)
    
    
    listRows(request: protos.google.area120.tables.v1alpha1.IListRowsRequest, options: CallOptions, callback: PaginationCallback<protos.google.area120.tables.v1alpha1.IListRowsRequest, protos.google.area120.tables.v1alpha1.IListRowsResponse | null | undefined, protos.google.area120.tables.v1alpha1.IRow>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.area120.tables.v1alpha1.IListRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsrequest), [protos.google.area120.tables.v1alpha1.IListRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsresponse) | null | undefined, [protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRows(request, callback)
    
    
    listRows(request: protos.google.area120.tables.v1alpha1.IListRowsRequest, callback: PaginationCallback<protos.google.area120.tables.v1alpha1.IListRowsRequest, protos.google.area120.tables.v1alpha1.IListRowsResponse | null | undefined, protos.google.area120.tables.v1alpha1.IRow>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.area120.tables.v1alpha1.IListRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsrequest), [protos.google.area120.tables.v1alpha1.IListRowsResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsresponse) | null | undefined, [protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRowsAsync(request, options)
    
    
    listRowsAsync(request?: protos.google.area120.tables.v1alpha1.IListRowsRequest, options?: CallOptions): AsyncIterable<protos.google.area120.tables.v1alpha1.IRow>;

Equivalent to `listRows`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Row](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.row). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent table.
       *  Format: tables/{table}
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of rows to return. The service may return fewer than
       *  this value.
       *  If unspecified, at most 50 rows are returned. The maximum value is 1,000;
       *  values above 1,000 are coerced to 1,000.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListRows` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListRows` must match
       *  the call that provided the page token.
       */
      // const pageToken = 'abc123'
      /**
       *  Optional. Column key to use for values in the row.
       *  Defaults to user entered name.
       */
      // const view = {}
      /**
       *  Optional. Raw text query to search for in rows of the table.
       *  Special characters must be escaped. Logical operators and field specific
       *  filtering not supported.
       */
      // const filter = 'abc123'
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callListRows() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = tablesClient.[listRowsAsync](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/v1alpha1.tablesserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListRows();
    
    

### listRowsStream(request, options)
    
    
    listRowsStream(request?: protos.google.area120.tables.v1alpha1.IListRowsRequest, options?: CallOptions): Transform;

Equivalent to `listRows`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRowsRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistrowsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Row](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.row) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listRowsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTables(request, options)
    
    
    listTables(request?: protos.google.area120.tables.v1alpha1.IListTablesRequest, options?: CallOptions): Promise<[
            protos.google.area120.tables.v1alpha1.ITable[],
            protos.google.area120.tables.v1alpha1.IListTablesRequest | null,
            protos.google.area120.tables.v1alpha1.IListTablesResponse
        ]>;

Lists tables for the user.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTablesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.area120.tables.v1alpha1.ITable](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.itable)[], [protos.google.area120.tables.v1alpha1.IListTablesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesrequest) | null, [protos.google.area120.tables.v1alpha1.IListTablesResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Table](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.table). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listTablesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listTables(request, options, callback)
    
    
    listTables(request: protos.google.area120.tables.v1alpha1.IListTablesRequest, options: CallOptions, callback: PaginationCallback<protos.google.area120.tables.v1alpha1.IListTablesRequest, protos.google.area120.tables.v1alpha1.IListTablesResponse | null | undefined, protos.google.area120.tables.v1alpha1.ITable>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTablesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.area120.tables.v1alpha1.IListTablesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesrequest), [protos.google.area120.tables.v1alpha1.IListTablesResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesresponse) | null | undefined, [protos.google.area120.tables.v1alpha1.ITable](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.itable)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTables(request, callback)
    
    
    listTables(request: protos.google.area120.tables.v1alpha1.IListTablesRequest, callback: PaginationCallback<protos.google.area120.tables.v1alpha1.IListTablesRequest, protos.google.area120.tables.v1alpha1.IListTablesResponse | null | undefined, protos.google.area120.tables.v1alpha1.ITable>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTablesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.area120.tables.v1alpha1.IListTablesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesrequest), [protos.google.area120.tables.v1alpha1.IListTablesResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesresponse) | null | undefined, [protos.google.area120.tables.v1alpha1.ITable](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.itable)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTablesAsync(request, options)
    
    
    listTablesAsync(request?: protos.google.area120.tables.v1alpha1.IListTablesRequest, options?: CallOptions): AsyncIterable<protos.google.area120.tables.v1alpha1.ITable>;

Equivalent to `listTables`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTablesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.area120.tables.v1alpha1.ITable](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.itable)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Table](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.table). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The maximum number of tables to return. The service may return fewer than
       *  this value.
       *  If unspecified, at most 20 tables are returned. The maximum value is 100;
       *  values above 100 are coerced to 100.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListTables` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListTables` must match
       *  the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callListTables() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = tablesClient.[listTablesAsync](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/v1alpha1.tablesserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListTables();
    
    

### listTablesStream(request, options)
    
    
    listTablesStream(request?: protos.google.area120.tables.v1alpha1.IListTablesRequest, options?: CallOptions): Transform;

Equivalent to `listTables`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTablesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilisttablesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Table](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.table) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listTablesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkspaces(request, options)
    
    
    listWorkspaces(request?: protos.google.area120.tables.v1alpha1.IListWorkspacesRequest, options?: CallOptions): Promise<[
            protos.google.area120.tables.v1alpha1.IWorkspace[],
            protos.google.area120.tables.v1alpha1.IListWorkspacesRequest | null,
            protos.google.area120.tables.v1alpha1.IListWorkspacesResponse
        ]>;

Lists workspaces for the user.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.area120.tables.v1alpha1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iworkspace)[], [protos.google.area120.tables.v1alpha1.IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesrequest) | null, [protos.google.area120.tables.v1alpha1.IListWorkspacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Workspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.workspace). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listWorkspacesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listWorkspaces(request, options, callback)
    
    
    listWorkspaces(request: protos.google.area120.tables.v1alpha1.IListWorkspacesRequest, options: CallOptions, callback: PaginationCallback<protos.google.area120.tables.v1alpha1.IListWorkspacesRequest, protos.google.area120.tables.v1alpha1.IListWorkspacesResponse | null | undefined, protos.google.area120.tables.v1alpha1.IWorkspace>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.area120.tables.v1alpha1.IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesrequest), [protos.google.area120.tables.v1alpha1.IListWorkspacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesresponse) | null | undefined, [protos.google.area120.tables.v1alpha1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iworkspace)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkspaces(request, callback)
    
    
    listWorkspaces(request: protos.google.area120.tables.v1alpha1.IListWorkspacesRequest, callback: PaginationCallback<protos.google.area120.tables.v1alpha1.IListWorkspacesRequest, protos.google.area120.tables.v1alpha1.IListWorkspacesResponse | null | undefined, protos.google.area120.tables.v1alpha1.IWorkspace>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.area120.tables.v1alpha1.IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesrequest), [protos.google.area120.tables.v1alpha1.IListWorkspacesResponse](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesresponse) | null | undefined, [protos.google.area120.tables.v1alpha1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iworkspace)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkspacesAsync(request, options)
    
    
    listWorkspacesAsync(request?: protos.google.area120.tables.v1alpha1.IListWorkspacesRequest, options?: CallOptions): AsyncIterable<protos.google.area120.tables.v1alpha1.IWorkspace>;

Equivalent to `listWorkspaces`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.area120.tables.v1alpha1.IWorkspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iworkspace)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Workspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.workspace). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  The maximum number of workspaces to return. The service may return fewer
       *  than this value.
       *  If unspecified, at most 10 workspaces are returned. The maximum value is
       *  25; values above 25 are coerced to 25.
       */
      // const pageSize = 1234
      /**
       *  A page token, received from a previous `ListWorkspaces` call.
       *  Provide this to retrieve the subsequent page.
       *  When paginating, all other parameters provided to `ListWorkspaces` must
       *  match the call that provided the page token.
       */
      // const pageToken = 'abc123'
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callListWorkspaces() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = tablesClient.[listWorkspacesAsync](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/v1alpha1.tablesserviceclient.html)(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListWorkspaces();
    
    

### listWorkspacesStream(request, options)
    
    
    listWorkspacesStream(request?: protos.google.area120.tables.v1alpha1.IListWorkspacesRequest, options?: CallOptions): Transform;

Equivalent to `listWorkspaces`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkspacesRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.ilistworkspacesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Workspace](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.workspace) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listWorkspacesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### matchRowFromRowName(rowName)
    
    
    matchRowFromRowName(rowName: string): string | number;

Parse the row from Row resource.

**Parameter**  
---  
**Name** | **Description**  
`rowName` |  `string`   
A fully-qualified path representing Row resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the row.  
  
### matchTableFromRowName(rowName)
    
    
    matchTableFromRowName(rowName: string): string | number;

Parse the table from Row resource.

**Parameter**  
---  
**Name** | **Description**  
`rowName` |  `string`   
A fully-qualified path representing Row resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the table.  
  
### matchTableFromTableName(tableName)
    
    
    matchTableFromTableName(tableName: string): string | number;

Parse the table from Table resource.

**Parameter**  
---  
**Name** | **Description**  
`tableName` |  `string`   
A fully-qualified path representing Table resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the table.  
  
### matchWorkspaceFromWorkspaceName(workspaceName)
    
    
    matchWorkspaceFromWorkspaceName(workspaceName: string): string | number;

Parse the workspace from Workspace resource.

**Parameter**  
---  
**Name** | **Description**  
`workspaceName` |  `string`   
A fully-qualified path representing Workspace resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the workspace.  
  
### rowPath(table, row)
    
    
    rowPath(table: string, row: string): string;

Return a fully-qualified row resource name string.

**Parameters**  
---  
**Name** | **Description**  
`table` |  `string`   
  
`row` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### tablePath(table)
    
    
    tablePath(table: string): string;

Return a fully-qualified table resource name string.

**Parameter**  
---  
**Name** | **Description**  
`table` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
### updateRow(request, options)
    
    
    updateRow(request?: protos.google.area120.tables.v1alpha1.IUpdateRowRequest, options?: CallOptions): Promise<[
            protos.google.area120.tables.v1alpha1.IRow,
            protos.google.area120.tables.v1alpha1.IUpdateRowRequest | undefined,
            {} | undefined
        ]>;

Updates a row.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iupdaterowrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow), [protos.google.area120.tables.v1alpha1.IUpdateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iupdaterowrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Row](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.row). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The row to update.
       */
      // const row = {}
      /**
       *  The list of fields to update.
       */
      // const updateMask = {}
      /**
       *  Optional. Column key to use for values in the row.
       *  Defaults to user entered name.
       */
      // const view = {}
    
      // Imports the Tables library
      const {TablesServiceClient} = require('[@google/area120-tables](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)').v1alpha1;
    
      // Instantiates a client
      const tablesClient = new [TablesServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/overview.html)();
    
      async function callUpdateRow() {
        // Construct request
        const request = {
          row,
        };
    
        // Run request
        const response = await tablesClient.updateRow(request);
        console.log(response);
      }
    
      callUpdateRow();
    
    

### updateRow(request, options, callback)
    
    
    updateRow(request: protos.google.area120.tables.v1alpha1.IUpdateRowRequest, options: CallOptions, callback: Callback<protos.google.area120.tables.v1alpha1.IRow, protos.google.area120.tables.v1alpha1.IUpdateRowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iupdaterowrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow), [protos.google.area120.tables.v1alpha1.IUpdateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iupdaterowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateRow(request, callback)
    
    
    updateRow(request: protos.google.area120.tables.v1alpha1.IUpdateRowRequest, callback: Callback<protos.google.area120.tables.v1alpha1.IRow, protos.google.area120.tables.v1alpha1.IUpdateRowRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iupdaterowrequest)`   
  
`callback` |  `Callback<[protos.google.area120.tables.v1alpha1.IRow](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.irow), [protos.google.area120.tables.v1alpha1.IUpdateRowRequest](https://docs.cloud.google.com/nodejs/docs/reference/area120-tables/latest/area120-tables/protos.google.area120.tables.v1alpha1.iupdaterowrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### workspacePath(workspace)
    
    
    workspacePath(workspace: string): string;

Return a fully-qualified workspace resource name string.

**Parameter**  
---  
**Name** | **Description**  
`workspace` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
