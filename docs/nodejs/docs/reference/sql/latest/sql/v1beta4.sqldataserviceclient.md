---
url: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/v1beta4.sqldataserviceclient
title: Class v1beta4.SqlDataServiceClient (0.29.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:34.531471+00:00
---

# Class v1beta4.SqlDataServiceClient (0.29.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/v1beta4.sqldataserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta4.SqlDataServiceClient (0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.25.0  0.23.0  0.19.1  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.4.0 

Service for streaming data to and from Cloud SQL instances. v1beta4

## Package

[@google-cloud/sql](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of SqlDataServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new SqlDataServiceClient({fallback: true}, gax); ```  
  
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

### servicePath
    
    
    static get servicePath(): string;

The DNS address for this API service.

### sqlDataServiceStub
    
    
    sqlDataServiceStub?: Promise<{
            [name: string]: Function;
        }>;

### universeDomain
    
    
    get universeDomain(): string;

### warn
    
    
    warn: (code: string, message: string, warnType?: string) => void;

## Methods 

### backupPath(project, backup)
    
    
    backupPath(project: string, backup: string): string;

Return a fully-qualified backup resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`backup` |  `string`   
  
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
  
### instancePath(project, instance)
    
    
    instancePath(project: string, instance: string): string;

Return a fully-qualified instance resource name string.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `string`   
  
`instance` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`string` | {string} Resource name string.  
  
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
    

### matchBackupFromBackupName(backupName)
    
    
    matchBackupFromBackupName(backupName: string): string | number;

Parse the backup from Backup resource.

**Parameter**  
---  
**Name** | **Description**  
`backupName` |  `string`   
A fully-qualified path representing Backup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the backup.  
  
### matchInstanceFromInstanceName(instanceName)
    
    
    matchInstanceFromInstanceName(instanceName: string): string | number;

Parse the instance from Instance resource.

**Parameter**  
---  
**Name** | **Description**  
`instanceName` |  `string`   
A fully-qualified path representing Instance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the instance.  
  
### matchProjectFromBackupName(backupName)
    
    
    matchProjectFromBackupName(backupName: string): string | number;

Parse the project from Backup resource.

**Parameter**  
---  
**Name** | **Description**  
`backupName` |  `string`   
A fully-qualified path representing Backup resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### matchProjectFromInstanceName(instanceName)
    
    
    matchProjectFromInstanceName(instanceName: string): string | number;

Parse the project from Instance resource.

**Parameter**  
---  
**Name** | **Description**  
`instanceName` |  `string`   
A fully-qualified path representing Instance resource.  
**Returns**  
---  
**Type** | **Description**  
`string | number` | {string} A string representing the project.  
  
### streamSqlData(options)
    
    
    streamSqlData(options?: CallOptions): gax.CancellableStream;

`StreamSqlData` establishes a bidirectional stream to a Cloud SQL instance, and then streams data to and from the instance.

The first message from the client MUST be a `StreamSqlDataRequest` request with configuration settings, including required values for the `connection_settings` field. Subsequent messages from the client may contain the `payload` field.

Messages from the server may contain the `payload` field.

The `payload` fields of the request and response streams contain the raw data of the database's native wire protocol (e.g., PostgreSQL wire protocol). The database client is responsible for generating and parsing this data.

Any errors on initial connection (e.g., connection failure, authorization issues, network problems) will result in the stream being terminated with an appropriate RPC status exception.

After a successful connection is made, if an error occurs, then the server terminates connection and returns the appropriate RPC status exception.

Add the request params headers to the request to ensure that the streaming request is routed to the correct service for your database.

Use this format for the request params header:

`x-goog-request-params`: location_id={location_path}&instance_id={instance_path}`

`location_path` is `locations/{location_name}` `instance_path` is `projects/{project_name}/instances/{instance_name}`

for example: `x-goog-request-params`: `location_id=locations/us-central1&instance_id=projects/myproject/instances/instancename`

**Parameter**  
---  
**Name** | **Description**  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which is both readable and writable. It accepts objects representing [StreamSqlDataRequest](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.streamsqldatarequest) for write() method, and will emit objects representing [StreamSqlDataResponse](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.streamsqldataresponse) on 'data' event asynchronously. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#bi-directional-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Acknowledges data received by the client.
       */
      // const ack = {}
      /**
       *  Starts a new session. When starting a new session, this is the first
       *  message the client sends.
       */
      // const startSession = {}
      /**
       *  Continues an existing session. When continuing an existing session, this
       *  is the first message the client sends.
       */
      // const continueSession = {}
      /**
       *  Database data.
       */
      // const data = {}
      /**
       *  Terminates the session. This closes the connection to the database.
       */
      // const terminateSession = {}
    
      // Imports the Sql library
      const {SqlDataServiceClient} = require('[@google-cloud/sql](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)').v1beta4;
    
      // Instantiates a client
      const sqlClient = new [SqlDataServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/v1beta4.sqldataserviceclient.html)();
    
      async function callStreamSqlData() {
        // Construct request
        const request = {
        };
    
        // Run request
        const stream = await sqlClient.streamSqlData();
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
        stream.write(request);
        stream.end();
      }
    
      callStreamSqlData();
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
