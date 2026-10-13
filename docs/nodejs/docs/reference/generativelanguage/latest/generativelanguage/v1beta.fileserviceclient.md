---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1beta.fileserviceclient
title: Class v1beta.FileServiceClient (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:50.560575+00:00
---

# Class v1beta.FileServiceClient (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/v1beta.fileserviceclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta.FileServiceClient (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

An API for uploading and managing files. v1beta

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of FileServiceClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new FileServiceClient({fallback: true}, gax); ```  
  
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

### fileServiceStub
    
    
    fileServiceStub?: Promise<{
            [name: string]: Function;
        }>;

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
  
### createFile(request, options)
    
    
    createFile(request?: protos.google.ai.generativelanguage.v1beta.ICreateFileRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.ICreateFileResponse,
            protos.google.ai.generativelanguage.v1beta.ICreateFileRequest | undefined,
            {} | undefined
        ]>;

Creates a `File`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatefilerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.ICreateFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatefileresponse), [protos.google.ai.generativelanguage.v1beta.ICreateFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatefilerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [CreateFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.createfileresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Metadata for the file to create.
       */
      // const file = {}
    
      // Imports the Generativelanguage library
      const {FileServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [FileServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callCreateFile() {
        // Construct request
        const request = {
        };
    
        // Run request
        const response = await generativelanguageClient.createFile(request);
        console.log(response);
      }
    
      callCreateFile();
    
    

### createFile(request, options, callback)
    
    
    createFile(request: protos.google.ai.generativelanguage.v1beta.ICreateFileRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta.ICreateFileResponse, protos.google.ai.generativelanguage.v1beta.ICreateFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatefilerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.ICreateFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatefileresponse), [protos.google.ai.generativelanguage.v1beta.ICreateFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatefilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFile(request, callback)
    
    
    createFile(request: protos.google.ai.generativelanguage.v1beta.ICreateFileRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta.ICreateFileResponse, protos.google.ai.generativelanguage.v1beta.ICreateFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatefilerequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.ICreateFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatefileresponse), [protos.google.ai.generativelanguage.v1beta.ICreateFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.icreatefilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFile(request, options)
    
    
    deleteFile(request?: protos.google.ai.generativelanguage.v1beta.IDeleteFileRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.ai.generativelanguage.v1beta.IDeleteFileRequest | undefined,
            {} | undefined
        ]>;

Deletes the `File`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletefilerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1beta.IDeleteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletefilerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `File` to delete.
       *  Example: `files/abc-123`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {FileServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [FileServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callDeleteFile() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.deleteFile(request);
        console.log(response);
      }
    
      callDeleteFile();
    
    

### deleteFile(request, options, callback)
    
    
    deleteFile(request: protos.google.ai.generativelanguage.v1beta.IDeleteFileRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1beta.IDeleteFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletefilerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1beta.IDeleteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletefilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFile(request, callback)
    
    
    deleteFile(request: protos.google.ai.generativelanguage.v1beta.IDeleteFileRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.ai.generativelanguage.v1beta.IDeleteFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletefilerequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.iempty), [protos.google.ai.generativelanguage.v1beta.IDeleteFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ideletefilerequest) | null | undefined, {} | null | undefined>`   
  
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
  
### downloadFile(request, options)
    
    
    downloadFile(request?: protos.google.ai.generativelanguage.v1beta.IDownloadFileRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.IDownloadFileResponse,
            (protos.google.ai.generativelanguage.v1beta.IDownloadFileRequest | undefined),
            {} | undefined
        ]>;

Download the `File`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDownloadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.idownloadfilerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.IDownloadFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.idownloadfileresponse), ([protos.google.ai.generativelanguage.v1beta.IDownloadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.idownloadfilerequest) | undefined), {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [DownloadFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.downloadfileresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `File` to download.
       *  Example: `files/abc-123`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {FileServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [FileServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callDownloadFile() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.downloadFile(request);
        console.log(response);
      }
    
      callDownloadFile();
    
    

### downloadFile(request, options, callback)
    
    
    downloadFile(request: protos.google.ai.generativelanguage.v1beta.IDownloadFileRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta.IDownloadFileResponse, protos.google.ai.generativelanguage.v1beta.IDownloadFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDownloadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.idownloadfilerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.IDownloadFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.idownloadfileresponse), [protos.google.ai.generativelanguage.v1beta.IDownloadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.idownloadfilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### downloadFile(request, callback)
    
    
    downloadFile(request: protos.google.ai.generativelanguage.v1beta.IDownloadFileRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta.IDownloadFileResponse, protos.google.ai.generativelanguage.v1beta.IDownloadFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDownloadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.idownloadfilerequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.IDownloadFileResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.idownloadfileresponse), [protos.google.ai.generativelanguage.v1beta.IDownloadFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.idownloadfilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
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
  
### getFile(request, options)
    
    
    getFile(request?: protos.google.ai.generativelanguage.v1beta.IGetFileRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.IFile,
            protos.google.ai.generativelanguage.v1beta.IGetFileRequest | undefined,
            {} | undefined
        ]>;

Gets the metadata for the given `File`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetfilerequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.IFile](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ifile), [protos.google.ai.generativelanguage.v1beta.IGetFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetfilerequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing . Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the `File` to get.
       *  Example: `files/abc-123`
       */
      // const name = 'abc123'
    
      // Imports the Generativelanguage library
      const {FileServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [FileServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callGetFile() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await generativelanguageClient.getFile(request);
        console.log(response);
      }
    
      callGetFile();
    
    

### getFile(request, options, callback)
    
    
    getFile(request: protos.google.ai.generativelanguage.v1beta.IGetFileRequest, options: CallOptions, callback: Callback<protos.google.ai.generativelanguage.v1beta.IFile, protos.google.ai.generativelanguage.v1beta.IGetFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetfilerequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.IFile](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ifile), [protos.google.ai.generativelanguage.v1beta.IGetFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetfilerequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFile(request, callback)
    
    
    getFile(request: protos.google.ai.generativelanguage.v1beta.IGetFileRequest, callback: Callback<protos.google.ai.generativelanguage.v1beta.IFile, protos.google.ai.generativelanguage.v1beta.IGetFileRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetfilerequest)`   
  
`callback` |  `Callback<[protos.google.ai.generativelanguage.v1beta.IFile](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ifile), [protos.google.ai.generativelanguage.v1beta.IGetFileRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.igetfilerequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listFiles(request, options)
    
    
    listFiles(request?: protos.google.ai.generativelanguage.v1beta.IListFilesRequest, options?: CallOptions): Promise<[
            protos.google.ai.generativelanguage.v1beta.IFile[],
            protos.google.ai.generativelanguage.v1beta.IListFilesRequest | null,
            protos.google.ai.generativelanguage.v1beta.IListFilesResponse
        ]>;

Lists the metadata for `File`s owned by the requesting project.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.ai.generativelanguage.v1beta.IFile](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ifile)[], [protos.google.ai.generativelanguage.v1beta.IListFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesrequest) | null, [protos.google.ai.generativelanguage.v1beta.IListFilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of . The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listFilesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listFiles(request, options, callback)
    
    
    listFiles(request: protos.google.ai.generativelanguage.v1beta.IListFilesRequest, options: CallOptions, callback: PaginationCallback<protos.google.ai.generativelanguage.v1beta.IListFilesRequest, protos.google.ai.generativelanguage.v1beta.IListFilesResponse | null | undefined, protos.google.ai.generativelanguage.v1beta.IFile>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1beta.IListFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesrequest), [protos.google.ai.generativelanguage.v1beta.IListFilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesresponse) | null | undefined, [protos.google.ai.generativelanguage.v1beta.IFile](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ifile)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFiles(request, callback)
    
    
    listFiles(request: protos.google.ai.generativelanguage.v1beta.IListFilesRequest, callback: PaginationCallback<protos.google.ai.generativelanguage.v1beta.IListFilesRequest, protos.google.ai.generativelanguage.v1beta.IListFilesResponse | null | undefined, protos.google.ai.generativelanguage.v1beta.IFile>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.ai.generativelanguage.v1beta.IListFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesrequest), [protos.google.ai.generativelanguage.v1beta.IListFilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesresponse) | null | undefined, [protos.google.ai.generativelanguage.v1beta.IFile](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ifile)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFilesAsync(request, options)
    
    
    listFilesAsync(request?: protos.google.ai.generativelanguage.v1beta.IListFilesRequest, options?: CallOptions): AsyncIterable<protos.google.ai.generativelanguage.v1beta.IFile>;

Equivalent to `listFiles`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.ai.generativelanguage.v1beta.IFile](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ifile)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing . The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Optional. Maximum number of `File`s to return per page.
       *  If unspecified, defaults to 10. Maximum `page_size` is 100.
       */
      // const pageSize = 1234
      /**
       *  Optional. A page token from a previous `ListFiles` call.
       */
      // const pageToken = 'abc123'
    
      // Imports the Generativelanguage library
      const {FileServiceClient} = require('[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)').v1beta;
    
      // Instantiates a client
      const generativelanguageClient = new [FileServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)();
    
      async function callListFiles() {
        // Construct request
        const request = {
        };
    
        // Run request
        const iterable = generativelanguageClient.listFilesAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListFiles();
    
    

### listFilesStream(request, options)
    
    
    listFilesStream(request?: protos.google.ai.generativelanguage.v1beta.IListFilesRequest, options?: CallOptions): Transform;

Equivalent to `listFiles`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1beta.ilistfilesrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listFilesAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
