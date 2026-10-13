---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/v1beta1.firestoreclient
title: Class v1beta1.FirestoreClient (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:11.647732+00:00
---

# Class v1beta1.FirestoreClient (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/v1beta1.firestoreclient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class v1beta1.FirestoreClient (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Firestore service.

Cloud Firestore is a fast, fully managed, serverless, cloud-native NoSQL document database that simplifies storing, syncing, and querying data for your mobile, web, and IoT apps at global scale. Its client libraries provide live synchronization and offline support, while its security features and integrations with Firebase and Google Cloud Platform (GCP) accelerate building truly serverless apps. v1beta1

## Package

[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)

## Constructors 

### (constructor)(opts, gaxInstance)
    
    
    constructor(opts?: ClientOptions, gaxInstance?: typeof gax | typeof gax.fallback);

Construct an instance of FirestoreClient.

**Parameters**  
---  
**Name** | **Description**  
`opts` |  `ClientOptions`   
  
`gaxInstance` |  `typeof gax | typeof fallback`   
: loaded instance of `google-gax`. Useful if you need to avoid loading the default gRPC version and want to use the fallback HTTP implementation. Load only fallback version and pass it to the constructor: ``` const gax = require('google-gax/build/src/fallback'); // avoids loading google-gax with gRPC const client = new FirestoreClient({fallback: true}, gax); ```  
  
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

### firestoreStub
    
    
    firestoreStub?: Promise<{
            [name: string]: Function;
        }>;

### innerApiCalls
    
    
    innerApiCalls: {
            [name: string]: Function;
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

### batchGetDocuments(request, options)
    
    
    batchGetDocuments(request?: protos.google.firestore.v1beta1.IBatchGetDocumentsRequest, options?: CallOptions): gax.CancellableStream;

Gets multiple documents.

Documents returned by this method are not guaranteed to be returned in the same order that they were requested.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibatchgetdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which emits [BatchGetDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.batchgetdocumentsresponse) on 'data' event. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#server-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The database name. In the format:
       *  `projects/{project_id}/databases/{database_id}`.
       */
      // const database = 'abc123'
      /**
       *  The names of the documents to retrieve. In the format:
       *  `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
       *  The request will fail if any of the document is not a child resource of the
       *  given `database`. Duplicate names will be elided.
       */
      // const documents = ['abc','def']
      /**
       *  The fields to return. If not set, returns all fields.
       *  If a document has a field that is not present in this mask, that field will
       *  not be returned in the response.
       */
      // const mask = {}
      /**
       *  Reads documents in a transaction.
       */
      // const transaction = Buffer.from('string')
      /**
       *  Starts a new transaction and reads the documents.
       *  Defaults to a read-only transaction.
       *  The new transaction ID will be returned as the first response in the
       *  stream.
       */
      // const newTransaction = {}
      /**
       *  Reads documents as they were at the given time.
       *  This may not be older than 270 seconds.
       */
      // const readTime = {}
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callBatchGetDocuments() {
        // Construct request
        const request = {
          database,
        };
    
        // Run request
        const stream = await firestoreClient.batchGetDocuments(request);
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
      }
    
      callBatchGetDocuments();
    
    

### batchWrite(request, options)
    
    
    batchWrite(request?: protos.google.firestore.v1beta1.IBatchWriteRequest, options?: CallOptions): Promise<[
            protos.google.firestore.v1beta1.IBatchWriteResponse,
            protos.google.firestore.v1beta1.IBatchWriteRequest | undefined,
            {} | undefined
        ]>;

Applies a batch of write operations.

The BatchWrite method does not apply the write operations atomically and can apply them out of order. Method does not allow more than one write per document. Each write succeeds or fails independently. See the [BatchWriteResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.batchwriteresponse) for the success status of each write.

If you require an atomically applied set of writes, use instead.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchWriteRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibatchwriterequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.firestore.v1beta1.IBatchWriteResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibatchwriteresponse), [protos.google.firestore.v1beta1.IBatchWriteRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibatchwriterequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BatchWriteResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.batchwriteresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The database name. In the format:
       *  `projects/{project_id}/databases/{database_id}`.
       */
      // const database = 'abc123'
      /**
       *  The writes to apply.
       *  Method does not apply writes atomically and does not guarantee ordering.
       *  Each write succeeds or fails independently. You cannot write to the same
       *  document more than once per request.
       */
      // const writes = [1,2,3,4]
      /**
       *  Labels associated with this batch write.
       */
      // const labels = [1,2,3,4]
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callBatchWrite() {
        // Construct request
        const request = {
          database,
        };
    
        // Run request
        const response = await firestoreClient.batchWrite(request);
        console.log(response);
      }
    
      callBatchWrite();
    
    

### batchWrite(request, options, callback)
    
    
    batchWrite(request: protos.google.firestore.v1beta1.IBatchWriteRequest, options: CallOptions, callback: Callback<protos.google.firestore.v1beta1.IBatchWriteResponse, protos.google.firestore.v1beta1.IBatchWriteRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchWriteRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibatchwriterequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.IBatchWriteResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibatchwriteresponse), [protos.google.firestore.v1beta1.IBatchWriteRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibatchwriterequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchWrite(request, callback)
    
    
    batchWrite(request: protos.google.firestore.v1beta1.IBatchWriteRequest, callback: Callback<protos.google.firestore.v1beta1.IBatchWriteResponse, protos.google.firestore.v1beta1.IBatchWriteRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchWriteRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibatchwriterequest)`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.IBatchWriteResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibatchwriteresponse), [protos.google.firestore.v1beta1.IBatchWriteRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibatchwriterequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### beginTransaction(request, options)
    
    
    beginTransaction(request?: protos.google.firestore.v1beta1.IBeginTransactionRequest, options?: CallOptions): Promise<[
            protos.google.firestore.v1beta1.IBeginTransactionResponse,
            protos.google.firestore.v1beta1.IBeginTransactionRequest | undefined,
            {} | undefined
        ]>;

Starts a new transaction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBeginTransactionRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibegintransactionrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.firestore.v1beta1.IBeginTransactionResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibegintransactionresponse), [protos.google.firestore.v1beta1.IBeginTransactionRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibegintransactionrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [BeginTransactionResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.begintransactionresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The database name. In the format:
       *  `projects/{project_id}/databases/{database_id}`.
       */
      // const database = 'abc123'
      /**
       *  The options for the transaction.
       *  Defaults to a read-write transaction.
       */
      // const options = {}
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callBeginTransaction() {
        // Construct request
        const request = {
          database,
        };
    
        // Run request
        const response = await firestoreClient.beginTransaction(request);
        console.log(response);
      }
    
      callBeginTransaction();
    
    

### beginTransaction(request, options, callback)
    
    
    beginTransaction(request: protos.google.firestore.v1beta1.IBeginTransactionRequest, options: CallOptions, callback: Callback<protos.google.firestore.v1beta1.IBeginTransactionResponse, protos.google.firestore.v1beta1.IBeginTransactionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBeginTransactionRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibegintransactionrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.IBeginTransactionResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibegintransactionresponse), [protos.google.firestore.v1beta1.IBeginTransactionRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibegintransactionrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### beginTransaction(request, callback)
    
    
    beginTransaction(request: protos.google.firestore.v1beta1.IBeginTransactionRequest, callback: Callback<protos.google.firestore.v1beta1.IBeginTransactionResponse, protos.google.firestore.v1beta1.IBeginTransactionRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBeginTransactionRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibegintransactionrequest)`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.IBeginTransactionResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibegintransactionresponse), [protos.google.firestore.v1beta1.IBeginTransactionRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ibegintransactionrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### commit(request, options)
    
    
    commit(request?: protos.google.firestore.v1beta1.ICommitRequest, options?: CallOptions): Promise<[
            protos.google.firestore.v1beta1.ICommitResponse,
            protos.google.firestore.v1beta1.ICommitRequest | undefined,
            {} | undefined
        ]>;

Commits a transaction, while optionally updating documents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icommitrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.firestore.v1beta1.ICommitResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icommitresponse), [protos.google.firestore.v1beta1.ICommitRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icommitrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [CommitResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.commitresponse). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The database name. In the format:
       *  `projects/{project_id}/databases/{database_id}`.
       */
      // const database = 'abc123'
      /**
       *  The writes to apply.
       *  Always executed atomically and in order.
       */
      // const writes = [1,2,3,4]
      /**
       *  If set, applies all writes in this transaction, and commits it.
       */
      // const transaction = Buffer.from('string')
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callCommit() {
        // Construct request
        const request = {
          database,
        };
    
        // Run request
        const response = await firestoreClient.commit(request);
        console.log(response);
      }
    
      callCommit();
    
    

### commit(request, options, callback)
    
    
    commit(request: protos.google.firestore.v1beta1.ICommitRequest, options: CallOptions, callback: Callback<protos.google.firestore.v1beta1.ICommitResponse, protos.google.firestore.v1beta1.ICommitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icommitrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.ICommitResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icommitresponse), [protos.google.firestore.v1beta1.ICommitRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icommitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### commit(request, callback)
    
    
    commit(request: protos.google.firestore.v1beta1.ICommitRequest, callback: Callback<protos.google.firestore.v1beta1.ICommitResponse, protos.google.firestore.v1beta1.ICommitRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICommitRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icommitrequest)`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.ICommitResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icommitresponse), [protos.google.firestore.v1beta1.ICommitRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icommitrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDocument(request, options)
    
    
    createDocument(request?: protos.google.firestore.v1beta1.ICreateDocumentRequest, options?: CallOptions): Promise<[
            protos.google.firestore.v1beta1.IDocument,
            protos.google.firestore.v1beta1.ICreateDocumentRequest | undefined,
            {} | undefined
        ]>;

Creates a new document.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icreatedocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument), [protos.google.firestore.v1beta1.ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icreatedocumentrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Document](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.document). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource. For example:
       *  `projects/{project_id}/databases/{database_id}/documents` or
       *  `projects/{project_id}/databases/{database_id}/documents/chatrooms/{chatroom_id}`
       */
      // const parent = 'abc123'
      /**
       *  Required. The collection ID, relative to `parent`, to list. For example: `chatrooms`.
       */
      // const collectionId = 'abc123'
      /**
       *  The client-assigned document ID to use for this document.
       *  Optional. If not specified, an ID will be assigned by the service.
       */
      // const documentId = 'abc123'
      /**
       *  Required. The document to create. `name` must not be set.
       */
      // const document = {}
      /**
       *  The fields to return. If not set, returns all fields.
       *  If the document has a field that is not present in this mask, that field
       *  will not be returned in the response.
       */
      // const mask = {}
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callCreateDocument() {
        // Construct request
        const request = {
          parent,
          collectionId,
          document,
        };
    
        // Run request
        const response = await firestoreClient.createDocument(request);
        console.log(response);
      }
    
      callCreateDocument();
    
    

### createDocument(request, options, callback)
    
    
    createDocument(request: protos.google.firestore.v1beta1.ICreateDocumentRequest, options: CallOptions, callback: Callback<protos.google.firestore.v1beta1.IDocument, protos.google.firestore.v1beta1.ICreateDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icreatedocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument), [protos.google.firestore.v1beta1.ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icreatedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDocument(request, callback)
    
    
    createDocument(request: protos.google.firestore.v1beta1.ICreateDocumentRequest, callback: Callback<protos.google.firestore.v1beta1.IDocument, protos.google.firestore.v1beta1.ICreateDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icreatedocumentrequest)`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument), [protos.google.firestore.v1beta1.ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icreatedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDocument(request, options)
    
    
    deleteDocument(request?: protos.google.firestore.v1beta1.IDeleteDocumentRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.firestore.v1beta1.IDeleteDocumentRequest | undefined,
            {} | undefined
        ]>;

Deletes a document.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ideletedocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.iempty), [protos.google.firestore.v1beta1.IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ideletedocumentrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Document to delete. In the format:
       *  `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
       */
      // const name = 'abc123'
      /**
       *  An optional precondition on the document.
       *  The request will fail if this is set and not met by the target document.
       */
      // const currentDocument = {}
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callDeleteDocument() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await firestoreClient.deleteDocument(request);
        console.log(response);
      }
    
      callDeleteDocument();
    
    

### deleteDocument(request, options, callback)
    
    
    deleteDocument(request: protos.google.firestore.v1beta1.IDeleteDocumentRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.firestore.v1beta1.IDeleteDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ideletedocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.iempty), [protos.google.firestore.v1beta1.IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ideletedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDocument(request, callback)
    
    
    deleteDocument(request: protos.google.firestore.v1beta1.IDeleteDocumentRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.firestore.v1beta1.IDeleteDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ideletedocumentrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.iempty), [protos.google.firestore.v1beta1.IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ideletedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDocument(request, options)
    
    
    getDocument(request?: protos.google.firestore.v1beta1.IGetDocumentRequest, options?: CallOptions): Promise<[
            protos.google.firestore.v1beta1.IDocument,
            protos.google.firestore.v1beta1.IGetDocumentRequest | undefined,
            {} | undefined
        ]>;

Gets a single document.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.igetdocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument), [protos.google.firestore.v1beta1.IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.igetdocumentrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Document](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.document). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The resource name of the Document to get. In the format:
       *  `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
       */
      // const name = 'abc123'
      /**
       *  The fields to return. If not set, returns all fields.
       *  If the document has a field that is not present in this mask, that field
       *  will not be returned in the response.
       */
      // const mask = {}
      /**
       *  Reads the document in a transaction.
       */
      // const transaction = Buffer.from('string')
      /**
       *  Reads the version of the document at the given time.
       *  This may not be older than 270 seconds.
       */
      // const readTime = {}
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callGetDocument() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const response = await firestoreClient.getDocument(request);
        console.log(response);
      }
    
      callGetDocument();
    
    

### getDocument(request, options, callback)
    
    
    getDocument(request: protos.google.firestore.v1beta1.IGetDocumentRequest, options: CallOptions, callback: Callback<protos.google.firestore.v1beta1.IDocument, protos.google.firestore.v1beta1.IGetDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.igetdocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument), [protos.google.firestore.v1beta1.IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.igetdocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDocument(request, callback)
    
    
    getDocument(request: protos.google.firestore.v1beta1.IGetDocumentRequest, callback: Callback<protos.google.firestore.v1beta1.IDocument, protos.google.firestore.v1beta1.IGetDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.igetdocumentrequest)`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument), [protos.google.firestore.v1beta1.IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.igetdocumentrequest) | null | undefined, {} | null | undefined>`   
  
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
  
### listCollectionIds(request, options)
    
    
    listCollectionIds(request?: protos.google.firestore.v1beta1.IListCollectionIdsRequest, options?: CallOptions): Promise<[
            string[],
            protos.google.firestore.v1beta1.IListCollectionIdsRequest | null,
            protos.google.firestore.v1beta1.IListCollectionIdsResponse
        ]>;

Lists all the collection IDs underneath a document.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCollectionIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ string[], [protos.google.firestore.v1beta1.IListCollectionIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsrequest) | null, [protos.google.firestore.v1beta1.IListCollectionIdsResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of string. The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listCollectionIdsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listCollectionIds(request, options, callback)
    
    
    listCollectionIds(request: protos.google.firestore.v1beta1.IListCollectionIdsRequest, options: CallOptions, callback: PaginationCallback<protos.google.firestore.v1beta1.IListCollectionIdsRequest, protos.google.firestore.v1beta1.IListCollectionIdsResponse | null | undefined, string>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCollectionIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.firestore.v1beta1.IListCollectionIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsrequest), [protos.google.firestore.v1beta1.IListCollectionIdsResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsresponse) | null | undefined, string>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCollectionIds(request, callback)
    
    
    listCollectionIds(request: protos.google.firestore.v1beta1.IListCollectionIdsRequest, callback: PaginationCallback<protos.google.firestore.v1beta1.IListCollectionIdsRequest, protos.google.firestore.v1beta1.IListCollectionIdsResponse | null | undefined, string>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCollectionIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.firestore.v1beta1.IListCollectionIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsrequest), [protos.google.firestore.v1beta1.IListCollectionIdsResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsresponse) | null | undefined, string>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCollectionIdsAsync(request, options)
    
    
    listCollectionIdsAsync(request?: protos.google.firestore.v1beta1.IListCollectionIdsRequest, options?: CallOptions): AsyncIterable<string>;

Equivalent to `listCollectionIds`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCollectionIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<string>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing string. The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent document. In the format:
       *  `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
       *  For example:
       *  `projects/my-project/databases/my-database/documents/chatrooms/my-chatroom`
       */
      // const parent = 'abc123'
      /**
       *  The maximum number of results to return.
       */
      // const pageSize = 1234
      /**
       *  A page token. Must be a value from
       *  ListCollectionIdsResponse google.firestore.v1beta1.ListCollectionIdsResponse.
       */
      // const pageToken = 'abc123'
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callListCollectionIds() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = firestoreClient.listCollectionIdsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListCollectionIds();
    
    

### listCollectionIdsStream(request, options)
    
    
    listCollectionIdsStream(request?: protos.google.firestore.v1beta1.IListCollectionIdsRequest, options?: CallOptions): Transform;

Equivalent to `listCollectionIds`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCollectionIdsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistcollectionidsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing string on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listCollectionIdsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDocuments(request, options)
    
    
    listDocuments(request?: protos.google.firestore.v1beta1.IListDocumentsRequest, options?: CallOptions): Promise<[
            protos.google.firestore.v1beta1.IDocument[],
            protos.google.firestore.v1beta1.IListDocumentsRequest | null,
            protos.google.firestore.v1beta1.IListDocumentsResponse
        ]>;

Lists documents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument)[], [protos.google.firestore.v1beta1.IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsrequest) | null, [protos.google.firestore.v1beta1.IListDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Document](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.document). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `listDocumentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listDocuments(request, options, callback)
    
    
    listDocuments(request: protos.google.firestore.v1beta1.IListDocumentsRequest, options: CallOptions, callback: PaginationCallback<protos.google.firestore.v1beta1.IListDocumentsRequest, protos.google.firestore.v1beta1.IListDocumentsResponse | null | undefined, protos.google.firestore.v1beta1.IDocument>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.firestore.v1beta1.IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsrequest), [protos.google.firestore.v1beta1.IListDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsresponse) | null | undefined, [protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDocuments(request, callback)
    
    
    listDocuments(request: protos.google.firestore.v1beta1.IListDocumentsRequest, callback: PaginationCallback<protos.google.firestore.v1beta1.IListDocumentsRequest, protos.google.firestore.v1beta1.IListDocumentsResponse | null | undefined, protos.google.firestore.v1beta1.IDocument>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.firestore.v1beta1.IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsrequest), [protos.google.firestore.v1beta1.IListDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsresponse) | null | undefined, [protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDocumentsAsync(request, options)
    
    
    listDocumentsAsync(request?: protos.google.firestore.v1beta1.IListDocumentsRequest, options?: CallOptions): AsyncIterable<protos.google.firestore.v1beta1.IDocument>;

Equivalent to `listDocuments`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Document](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.document). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name. In the format:
       *  `projects/{project_id}/databases/{database_id}/documents` or
       *  `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
       *  For example:
       *  `projects/my-project/databases/my-database/documents` or
       *  `projects/my-project/databases/my-database/documents/chatrooms/my-chatroom`
       */
      // const parent = 'abc123'
      /**
       *  Required. The collection ID, relative to `parent`, to list. For example: `chatrooms`
       *  or `messages`.
       */
      // const collectionId = 'abc123'
      /**
       *  The maximum number of documents to return.
       */
      // const pageSize = 1234
      /**
       *  The `next_page_token` value returned from a previous List request, if any.
       */
      // const pageToken = 'abc123'
      /**
       *  The order to sort results by. For example: `priority desc, name`.
       */
      // const orderBy = 'abc123'
      /**
       *  The fields to return. If not set, returns all fields.
       *  If a document has a field that is not present in this mask, that field
       *  will not be returned in the response.
       */
      // const mask = {}
      /**
       *  Reads documents in a transaction.
       */
      // const transaction = Buffer.from('string')
      /**
       *  Reads documents as they were at the given time.
       *  This may not be older than 270 seconds.
       */
      // const readTime = {}
      /**
       *  If the list should show missing documents. A missing document is a
       *  document that does not exist but has sub-documents. These documents will
       *  be returned with a key but will not have fields, Document.create_time google.firestore.v1beta1.Document.create_time,
       *  or Document.update_time google.firestore.v1beta1.Document.update_time  set.
       *  Requests with `show_missing` may not specify `where` or
       *  `order_by`.
       */
      // const showMissing = true
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callListDocuments() {
        // Construct request
        const request = {
          parent,
          collectionId,
        };
    
        // Run request
        const iterable = firestoreClient.listDocumentsAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callListDocuments();
    
    

### listDocumentsStream(request, options)
    
    
    listDocumentsStream(request?: protos.google.firestore.v1beta1.IListDocumentsRequest, options?: CallOptions): Transform;

Equivalent to `listDocuments`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ilistdocumentsrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Document](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.document) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `listDocumentsAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### listen(options)
    
    
    listen(options?: CallOptions): gax.CancellableStream;

Listens to changes.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which is both readable and writable. It accepts objects representing [ListenRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.listenrequest) for write() method, and will emit objects representing [ListenResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.listenresponse) on 'data' event asynchronously. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#bi-directional-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The database name. In the format:
       *  `projects/{project_id}/databases/{database_id}`.
       */
      // const database = 'abc123'
      /**
       *  A target to add to this stream.
       */
      // const addTarget = {}
      /**
       *  The ID of a target to remove from this stream.
       */
      // const removeTarget = 1234
      /**
       *  Labels associated with this target change.
       */
      // const labels = [1,2,3,4]
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callListen() {
        // Construct request
        const request = {
          database,
        };
    
        // Run request
        const stream = await firestoreClient.listen();
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
        stream.write(request);
        stream.end();
      }
    
      callListen();
    
    

### partitionQuery(request, options)
    
    
    partitionQuery(request?: protos.google.firestore.v1beta1.IPartitionQueryRequest, options?: CallOptions): Promise<[
            protos.google.firestore.v1beta1.ICursor[],
            protos.google.firestore.v1beta1.IPartitionQueryRequest | null,
            protos.google.firestore.v1beta1.IPartitionQueryResponse
        ]>;

Partitions a query by returning partition cursors that can be used to run the query in parallel. The returned partition cursors are split points that can be used by RunQuery as starting/end points for the query results.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPartitionQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.firestore.v1beta1.ICursor](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icursor)[], [protos.google.firestore.v1beta1.IPartitionQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryrequest) | null, [protos.google.firestore.v1beta1.IPartitionQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryresponse) ]>` | {Promise} - The promise which resolves to an array. The first element of the array is Array of [Cursor](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.cursor). The client library will perform auto-pagination by default: it will call the API as many times as needed and will merge results from all the pages into this array. Note that it can affect your quota. We recommend using `partitionQueryAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### partitionQuery(request, options, callback)
    
    
    partitionQuery(request: protos.google.firestore.v1beta1.IPartitionQueryRequest, options: CallOptions, callback: PaginationCallback<protos.google.firestore.v1beta1.IPartitionQueryRequest, protos.google.firestore.v1beta1.IPartitionQueryResponse | null | undefined, protos.google.firestore.v1beta1.ICursor>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPartitionQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `PaginationCallback<[protos.google.firestore.v1beta1.IPartitionQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryrequest), [protos.google.firestore.v1beta1.IPartitionQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryresponse) | null | undefined, [protos.google.firestore.v1beta1.ICursor](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icursor)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### partitionQuery(request, callback)
    
    
    partitionQuery(request: protos.google.firestore.v1beta1.IPartitionQueryRequest, callback: PaginationCallback<protos.google.firestore.v1beta1.IPartitionQueryRequest, protos.google.firestore.v1beta1.IPartitionQueryResponse | null | undefined, protos.google.firestore.v1beta1.ICursor>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPartitionQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryrequest)`   
  
`callback` |  `PaginationCallback<[protos.google.firestore.v1beta1.IPartitionQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryrequest), [protos.google.firestore.v1beta1.IPartitionQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryresponse) | null | undefined, [protos.google.firestore.v1beta1.ICursor](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icursor)>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### partitionQueryAsync(request, options)
    
    
    partitionQueryAsync(request?: protos.google.firestore.v1beta1.IPartitionQueryRequest, options?: CallOptions): AsyncIterable<protos.google.firestore.v1beta1.ICursor>;

Equivalent to `partitionQuery`, but returns an iterable object.

`for`-`await`-`of` syntax is used with the iterable to get response elements on-demand.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPartitionQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`AsyncIterable<[protos.google.firestore.v1beta1.ICursor](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.icursor)>` | {Object} An iterable Object that allows [async iteration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols). When you iterate the returned iterable, each element will be an object representing [Cursor](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.cursor). The API will be called under the hood as needed, once per the page, so you can stop the iteration when you don't need more results. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name. In the format:
       *  `projects/{project_id}/databases/{database_id}/documents`.
       *  Document resource names are not supported; only database resource names
       *  can be specified.
       */
      // const parent = 'abc123'
      /**
       *  A structured query.
       *  Query must specify collection with all descendants and be ordered by name
       *  ascending. Other filters, order bys, limits, offsets, and start/end
       *  cursors are not supported.
       */
      // const structuredQuery = {}
      /**
       *  The desired maximum number of partition points.
       *  The partitions may be returned across multiple pages of results.
       *  The number must be positive. The actual number of partitions
       *  returned may be fewer.
       *  For example, this may be set to one fewer than the number of parallel
       *  queries to be run, or in running a data pipeline job, one fewer than the
       *  number of workers or compute instances available.
       */
      // const partitionCount = 1234
      /**
       *  The `next_page_token` value returned from a previous call to
       *  PartitionQuery that may be used to get an additional set of results.
       *  There are no ordering guarantees between sets of results. Thus, using
       *  multiple sets of results will require merging the different result sets.
       *  For example, two subsequent calls using a page_token may return:
       *   * cursor B, cursor M, cursor Q
       *   * cursor A, cursor U, cursor W
       *  To obtain a complete result set ordered with respect to the results of the
       *  query supplied to PartitionQuery, the results sets should be merged:
       *  cursor A, cursor B, cursor M, cursor Q, cursor U, cursor W
       */
      // const pageToken = 'abc123'
      /**
       *  The maximum number of partitions to return in this call, subject to
       *  `partition_count`.
       *  For example, if `partition_count` = 10 and `page_size` = 8, the first call
       *  to PartitionQuery will return up to 8 partitions and a `next_page_token`
       *  if more results exist. A second call to PartitionQuery will return up to
       *  2 partitions, to complete the total of 10 specified in `partition_count`.
       */
      // const pageSize = 1234
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callPartitionQuery() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const iterable = firestoreClient.partitionQueryAsync(request);
        for await (const response of iterable) {
            console.log(response);
        }
      }
    
      callPartitionQuery();
    
    

### partitionQueryStream(request, options)
    
    
    partitionQueryStream(request?: protos.google.firestore.v1beta1.IPartitionQueryRequest, options?: CallOptions): Transform;

Equivalent to `partitionQuery`, but returns a NodeJS Stream object.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPartitionQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.ipartitionqueryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Transform` | {Stream} An object stream which emits an object representing [Cursor](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.cursor) on 'data' event. The client library will perform auto-pagination by default: it will call the API as many times as needed. Note that it can affect your quota. We recommend using `partitionQueryAsync()` method described below for async iteration which you can stop as needed. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#auto-pagination) for more details and examples.  
  
### rollback(request, options)
    
    
    rollback(request?: protos.google.firestore.v1beta1.IRollbackRequest, options?: CallOptions): Promise<[
            protos.google.protobuf.IEmpty,
            protos.google.firestore.v1beta1.IRollbackRequest | undefined,
            {} | undefined
        ]>;

Rolls back a transaction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.irollbackrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.iempty), [protos.google.firestore.v1beta1.IRollbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.irollbackrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Empty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.empty). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The database name. In the format:
       *  `projects/{project_id}/databases/{database_id}`.
       */
      // const database = 'abc123'
      /**
       *  Required. The transaction to roll back.
       */
      // const transaction = Buffer.from('string')
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callRollback() {
        // Construct request
        const request = {
          database,
          transaction,
        };
    
        // Run request
        const response = await firestoreClient.rollback(request);
        console.log(response);
      }
    
      callRollback();
    
    

### rollback(request, options, callback)
    
    
    rollback(request: protos.google.firestore.v1beta1.IRollbackRequest, options: CallOptions, callback: Callback<protos.google.protobuf.IEmpty, protos.google.firestore.v1beta1.IRollbackRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.irollbackrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.iempty), [protos.google.firestore.v1beta1.IRollbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.irollbackrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### rollback(request, callback)
    
    
    rollback(request: protos.google.firestore.v1beta1.IRollbackRequest, callback: Callback<protos.google.protobuf.IEmpty, protos.google.firestore.v1beta1.IRollbackRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRollbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.irollbackrequest)`   
  
`callback` |  `Callback<[protos.google.protobuf.IEmpty](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.protobuf.iempty), [protos.google.firestore.v1beta1.IRollbackRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.irollbackrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runQuery(request, options)
    
    
    runQuery(request?: protos.google.firestore.v1beta1.IRunQueryRequest, options?: CallOptions): gax.CancellableStream;

Runs a query.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.irunqueryrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which emits [RunQueryResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.runqueryresponse) on 'data' event. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#server-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The parent resource name. In the format:
       *  `projects/{project_id}/databases/{database_id}/documents` or
       *  `projects/{project_id}/databases/{database_id}/documents/{document_path}`.
       *  For example:
       *  `projects/my-project/databases/my-database/documents` or
       *  `projects/my-project/databases/my-database/documents/chatrooms/my-chatroom`
       */
      // const parent = 'abc123'
      /**
       *  A structured query.
       */
      // const structuredQuery = {}
      /**
       *  Reads documents in a transaction.
       */
      // const transaction = Buffer.from('string')
      /**
       *  Starts a new transaction and reads the documents.
       *  Defaults to a read-only transaction.
       *  The new transaction ID will be returned as the first response in the
       *  stream.
       */
      // const newTransaction = {}
      /**
       *  Reads documents as they were at the given time.
       *  This may not be older than 270 seconds.
       */
      // const readTime = {}
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callRunQuery() {
        // Construct request
        const request = {
          parent,
        };
    
        // Run request
        const stream = await firestoreClient.runQuery(request);
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
      }
    
      callRunQuery();
    
    

### updateDocument(request, options)
    
    
    updateDocument(request?: protos.google.firestore.v1beta1.IUpdateDocumentRequest, options?: CallOptions): Promise<[
            protos.google.firestore.v1beta1.IDocument,
            protos.google.firestore.v1beta1.IUpdateDocumentRequest | undefined,
            {} | undefined
        ]>;

Updates or inserts a document.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.iupdatedocumentrequest)`   
The request object that will be sent.  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[ [protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument), [protos.google.firestore.v1beta1.IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.iupdatedocumentrequest) | undefined, {} | undefined ]>` | {Promise} - The promise which resolves to an array. The first element of the array is an object representing [Document](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.document). Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#regular-methods) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The updated document.
       *  Creates the document if it does not already exist.
       */
      // const document = {}
      /**
       *  The fields to update.
       *  None of the field paths in the mask may contain a reserved name.
       *  If the document exists on the server and has fields not referenced in the
       *  mask, they are left unchanged.
       *  Fields referenced in the mask, but not present in the input document, are
       *  deleted from the document on the server.
       */
      // const updateMask = {}
      /**
       *  The fields to return. If not set, returns all fields.
       *  If the document has a field that is not present in this mask, that field
       *  will not be returned in the response.
       */
      // const mask = {}
      /**
       *  An optional precondition on the document.
       *  The request will fail if this is set and not met by the target document.
       */
      // const currentDocument = {}
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callUpdateDocument() {
        // Construct request
        const request = {
          document,
        };
    
        // Run request
        const response = await firestoreClient.updateDocument(request);
        console.log(response);
      }
    
      callUpdateDocument();
    
    

### updateDocument(request, options, callback)
    
    
    updateDocument(request: protos.google.firestore.v1beta1.IUpdateDocumentRequest, options: CallOptions, callback: Callback<protos.google.firestore.v1beta1.IDocument, protos.google.firestore.v1beta1.IUpdateDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.iupdatedocumentrequest)`   
  
`options` |  `CallOptions`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument), [protos.google.firestore.v1beta1.IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.iupdatedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDocument(request, callback)
    
    
    updateDocument(request: protos.google.firestore.v1beta1.IUpdateDocumentRequest, callback: Callback<protos.google.firestore.v1beta1.IDocument, protos.google.firestore.v1beta1.IUpdateDocumentRequest | null | undefined, {} | null | undefined>): void;

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.iupdatedocumentrequest)`   
  
`callback` |  `Callback<[protos.google.firestore.v1beta1.IDocument](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocument), [protos.google.firestore.v1beta1.IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.iupdatedocumentrequest) | null | undefined, {} | null | undefined>`   
  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### write(options)
    
    
    write(options?: CallOptions): gax.CancellableStream;

Streams batches of document updates and deletes, in order.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `CallOptions`   
Call options. See [CallOptions](https://googleapis.dev/nodejs/google-gax/latest/interfaces/CallOptions.html) for more details.  
**Returns**  
---  
**Type** | **Description**  
`gax.CancellableStream` | {Stream} An object stream which is both readable and writable. It accepts objects representing [WriteRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.writerequest) for write() method, and will emit objects representing [WriteResponse](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.writeresponse) on 'data' event asynchronously. Please see the [documentation](https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#bi-directional-streaming) for more details and examples.  
**Example**
    
    
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The database name. In the format:
       *  `projects/{project_id}/databases/{database_id}`.
       *  This is only required in the first message.
       */
      // const database = 'abc123'
      /**
       *  The ID of the write stream to resume.
       *  This may only be set in the first message. When left empty, a new write
       *  stream will be created.
       */
      // const streamId = 'abc123'
      /**
       *  The writes to apply.
       *  Always executed atomically and in order.
       *  This must be empty on the first request.
       *  This may be empty on the last request.
       *  This must not be empty on all other requests.
       */
      // const writes = [1,2,3,4]
      /**
       *  A stream token that was previously sent by the server.
       *  The client should set this field to the token from the most recent
       *  WriteResponse google.firestore.v1beta1.WriteResponse  it has received. This acknowledges that the client has
       *  received responses up to this token. After sending this token, earlier
       *  tokens may not be used anymore.
       *  The server may close the stream if there are too many unacknowledged
       *  responses.
       *  Leave this field unset when creating a new stream. To resume a stream at
       *  a specific point, set this field and the `stream_id` field.
       *  Leave this field unset when creating a new stream.
       */
      // const streamToken = Buffer.from('string')
      /**
       *  Labels associated with this write request.
       */
      // const labels = [1,2,3,4]
    
      // Imports the Firestore library
      const {FirestoreClient} = require('[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)').v1beta1;
    
      // Instantiates a client
      const firestoreClient = new [FirestoreClient](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)();
    
      async function callWrite() {
        // Construct request
        const request = {
          database,
        };
    
        // Run request
        const stream = await firestoreClient.write();
        stream.on('data', (response) => { console.log(response) });
        stream.on('error', (err) => { throw(err) });
        stream.on('end', () => { /* API call completed */ });
        stream.write(request);
        stream.end();
      }
    
      callWrite();
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
