---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.retrieverservice-class
title: Class protos.google.ai.generativelanguage.v1alpha.RetrieverService (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:08.352687+00:00
---

# Class protos.google.ai.generativelanguage.v1alpha.RetrieverService (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.retrieverservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ai.generativelanguage.v1alpha.RetrieverService (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

Represents a RetrieverService

## Inheritance

$protobuf.rpc.Service > protos.google.ai.generativelanguage.v1alpha.RetrieverService

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new RetrieverService service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### batchCreateChunks(request, callback)
    
    
    public batchCreateChunks(request: google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.BatchCreateChunksCallback): void;

Calls BatchCreateChunks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksrequest)`   
BatchCreateChunksRequest message or plain object  
`callback` |  `[BatchCreateChunksCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateChunksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateChunks(request)
    
    
    public batchCreateChunks(request: google.ai.generativelanguage.v1alpha.IBatchCreateChunksRequest): Promise<google.ai.generativelanguage.v1alpha.BatchCreateChunksResponse>;

Calls BatchCreateChunks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchcreatechunksrequest)`   
BatchCreateChunksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.BatchCreateChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.batchcreatechunksresponse)>` | Promise  
  
### batchDeleteChunks(request, callback)
    
    
    public batchDeleteChunks(request: google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.BatchDeleteChunksCallback): void;

Calls BatchDeleteChunks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchdeletechunksrequest)`   
BatchDeleteChunksRequest message or plain object  
`callback` |  `[BatchDeleteChunksCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteChunks(request)
    
    
    public batchDeleteChunks(request: google.ai.generativelanguage.v1alpha.IBatchDeleteChunksRequest): Promise<google.protobuf.Empty>;

Calls BatchDeleteChunks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchdeletechunksrequest)`   
BatchDeleteChunksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty)>` | Promise  
  
### batchUpdateChunks(request, callback)
    
    
    public batchUpdateChunks(request: google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.BatchUpdateChunksCallback): void;

Calls BatchUpdateChunks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksrequest)`   
BatchUpdateChunksRequest message or plain object  
`callback` |  `[BatchUpdateChunksCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateChunksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateChunks(request)
    
    
    public batchUpdateChunks(request: google.ai.generativelanguage.v1alpha.IBatchUpdateChunksRequest): Promise<google.ai.generativelanguage.v1alpha.BatchUpdateChunksResponse>;

Calls BatchUpdateChunks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ibatchupdatechunksrequest)`   
BatchUpdateChunksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.BatchUpdateChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.batchupdatechunksresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): RetrieverService;

Creates new RetrieverService service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[RetrieverService](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.retrieverservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createChunk(request, callback)
    
    
    public createChunk(request: google.ai.generativelanguage.v1alpha.ICreateChunkRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.CreateChunkCallback): void;

Calls CreateChunk.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatechunkrequest)`   
CreateChunkRequest message or plain object  
`callback` |  `[CreateChunkCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Chunk  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createChunk(request)
    
    
    public createChunk(request: google.ai.generativelanguage.v1alpha.ICreateChunkRequest): Promise<google.ai.generativelanguage.v1alpha.Chunk>;

Calls CreateChunk.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatechunkrequest)`   
CreateChunkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.Chunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.chunk-class)>` | Promise  
  
### createCorpus(request, callback)
    
    
    public createCorpus(request: google.ai.generativelanguage.v1alpha.ICreateCorpusRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.CreateCorpusCallback): void;

Calls CreateCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatecorpusrequest)`   
CreateCorpusRequest message or plain object  
`callback` |  `[CreateCorpusCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Corpus  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCorpus(request)
    
    
    public createCorpus(request: google.ai.generativelanguage.v1alpha.ICreateCorpusRequest): Promise<google.ai.generativelanguage.v1alpha.Corpus>;

Calls CreateCorpus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatecorpusrequest)`   
CreateCorpusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.Corpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.corpus)>` | Promise  
  
### createDocument(request, callback)
    
    
    public createDocument(request: google.ai.generativelanguage.v1alpha.ICreateDocumentRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.CreateDocumentCallback): void;

Calls CreateDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatedocumentrequest)`   
CreateDocumentRequest message or plain object  
`callback` |  `[CreateDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Document  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDocument(request)
    
    
    public createDocument(request: google.ai.generativelanguage.v1alpha.ICreateDocumentRequest): Promise<google.ai.generativelanguage.v1alpha.Document>;

Calls CreateDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.icreatedocumentrequest)`   
CreateDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.Document](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.document)>` | Promise  
  
### deleteChunk(request, callback)
    
    
    public deleteChunk(request: google.ai.generativelanguage.v1alpha.IDeleteChunkRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.DeleteChunkCallback): void;

Calls DeleteChunk.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletechunkrequest)`   
DeleteChunkRequest message or plain object  
`callback` |  `[DeleteChunkCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteChunk(request)
    
    
    public deleteChunk(request: google.ai.generativelanguage.v1alpha.IDeleteChunkRequest): Promise<google.protobuf.Empty>;

Calls DeleteChunk.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletechunkrequest)`   
DeleteChunkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty)>` | Promise  
  
### deleteCorpus(request, callback)
    
    
    public deleteCorpus(request: google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.DeleteCorpusCallback): void;

Calls DeleteCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletecorpusrequest)`   
DeleteCorpusRequest message or plain object  
`callback` |  `[DeleteCorpusCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCorpus(request)
    
    
    public deleteCorpus(request: google.ai.generativelanguage.v1alpha.IDeleteCorpusRequest): Promise<google.protobuf.Empty>;

Calls DeleteCorpus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletecorpusrequest)`   
DeleteCorpusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty)>` | Promise  
  
### deleteDocument(request, callback)
    
    
    public deleteDocument(request: google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.DeleteDocumentCallback): void;

Calls DeleteDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletedocumentrequest)`   
DeleteDocumentRequest message or plain object  
`callback` |  `[DeleteDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDocument(request)
    
    
    public deleteDocument(request: google.ai.generativelanguage.v1alpha.IDeleteDocumentRequest): Promise<google.protobuf.Empty>;

Calls DeleteDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ideletedocumentrequest)`   
DeleteDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.protobuf.empty)>` | Promise  
  
### getChunk(request, callback)
    
    
    public getChunk(request: google.ai.generativelanguage.v1alpha.IGetChunkRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.GetChunkCallback): void;

Calls GetChunk.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetchunkrequest)`   
GetChunkRequest message or plain object  
`callback` |  `[GetChunkCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Chunk  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChunk(request)
    
    
    public getChunk(request: google.ai.generativelanguage.v1alpha.IGetChunkRequest): Promise<google.ai.generativelanguage.v1alpha.Chunk>;

Calls GetChunk.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetchunkrequest)`   
GetChunkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.Chunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.chunk-class)>` | Promise  
  
### getCorpus(request, callback)
    
    
    public getCorpus(request: google.ai.generativelanguage.v1alpha.IGetCorpusRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.GetCorpusCallback): void;

Calls GetCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetcorpusrequest)`   
GetCorpusRequest message or plain object  
`callback` |  `[GetCorpusCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Corpus  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCorpus(request)
    
    
    public getCorpus(request: google.ai.generativelanguage.v1alpha.IGetCorpusRequest): Promise<google.ai.generativelanguage.v1alpha.Corpus>;

Calls GetCorpus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetcorpusrequest)`   
GetCorpusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.Corpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.corpus)>` | Promise  
  
### getDocument(request, callback)
    
    
    public getDocument(request: google.ai.generativelanguage.v1alpha.IGetDocumentRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.GetDocumentCallback): void;

Calls GetDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetdocumentrequest)`   
GetDocumentRequest message or plain object  
`callback` |  `[GetDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Document  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDocument(request)
    
    
    public getDocument(request: google.ai.generativelanguage.v1alpha.IGetDocumentRequest): Promise<google.ai.generativelanguage.v1alpha.Document>;

Calls GetDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.igetdocumentrequest)`   
GetDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.Document](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.document)>` | Promise  
  
### listChunks(request, callback)
    
    
    public listChunks(request: google.ai.generativelanguage.v1alpha.IListChunksRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.ListChunksCallback): void;

Calls ListChunks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksrequest)`   
ListChunksRequest message or plain object  
`callback` |  `[ListChunksCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and ListChunksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChunks(request)
    
    
    public listChunks(request: google.ai.generativelanguage.v1alpha.IListChunksRequest): Promise<google.ai.generativelanguage.v1alpha.ListChunksResponse>;

Calls ListChunks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListChunksRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistchunksrequest)`   
ListChunksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.ListChunksResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.listchunksresponse)>` | Promise  
  
### listCorpora(request, callback)
    
    
    public listCorpora(request: google.ai.generativelanguage.v1alpha.IListCorporaRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.ListCorporaCallback): void;

Calls ListCorpora.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCorporaRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporarequest)`   
ListCorporaRequest message or plain object  
`callback` |  `[ListCorporaCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCorporaResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCorpora(request)
    
    
    public listCorpora(request: google.ai.generativelanguage.v1alpha.IListCorporaRequest): Promise<google.ai.generativelanguage.v1alpha.ListCorporaResponse>;

Calls ListCorpora.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCorporaRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistcorporarequest)`   
ListCorporaRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.ListCorporaResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.listcorporaresponse)>` | Promise  
  
### listDocuments(request, callback)
    
    
    public listDocuments(request: google.ai.generativelanguage.v1alpha.IListDocumentsRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.ListDocumentsCallback): void;

Calls ListDocuments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsrequest)`   
ListDocumentsRequest message or plain object  
`callback` |  `[ListDocumentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDocumentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDocuments(request)
    
    
    public listDocuments(request: google.ai.generativelanguage.v1alpha.IListDocumentsRequest): Promise<google.ai.generativelanguage.v1alpha.ListDocumentsResponse>;

Calls ListDocuments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ilistdocumentsrequest)`   
ListDocumentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.ListDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.listdocumentsresponse)>` | Promise  
  
### queryCorpus(request, callback)
    
    
    public queryCorpus(request: google.ai.generativelanguage.v1alpha.IQueryCorpusRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.QueryCorpusCallback): void;

Calls QueryCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusrequest)`   
QueryCorpusRequest message or plain object  
`callback` |  `[QueryCorpusCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryCorpusResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryCorpus(request)
    
    
    public queryCorpus(request: google.ai.generativelanguage.v1alpha.IQueryCorpusRequest): Promise<google.ai.generativelanguage.v1alpha.QueryCorpusResponse>;

Calls QueryCorpus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerycorpusrequest)`   
QueryCorpusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.QueryCorpusResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.querycorpusresponse)>` | Promise  
  
### queryDocument(request, callback)
    
    
    public queryDocument(request: google.ai.generativelanguage.v1alpha.IQueryDocumentRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.QueryDocumentCallback): void;

Calls QueryDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentrequest)`   
QueryDocumentRequest message or plain object  
`callback` |  `[QueryDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryDocumentResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryDocument(request)
    
    
    public queryDocument(request: google.ai.generativelanguage.v1alpha.IQueryDocumentRequest): Promise<google.ai.generativelanguage.v1alpha.QueryDocumentResponse>;

Calls QueryDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iquerydocumentrequest)`   
QueryDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.QueryDocumentResponse](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.querydocumentresponse)>` | Promise  
  
### updateChunk(request, callback)
    
    
    public updateChunk(request: google.ai.generativelanguage.v1alpha.IUpdateChunkRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.UpdateChunkCallback): void;

Calls UpdateChunk.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatechunkrequest)`   
UpdateChunkRequest message or plain object  
`callback` |  `[UpdateChunkCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Chunk  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateChunk(request)
    
    
    public updateChunk(request: google.ai.generativelanguage.v1alpha.IUpdateChunkRequest): Promise<google.ai.generativelanguage.v1alpha.Chunk>;

Calls UpdateChunk.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatechunkrequest)`   
UpdateChunkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.Chunk](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.chunk-class)>` | Promise  
  
### updateCorpus(request, callback)
    
    
    public updateCorpus(request: google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.UpdateCorpusCallback): void;

Calls UpdateCorpus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatecorpusrequest)`   
UpdateCorpusRequest message or plain object  
`callback` |  `[UpdateCorpusCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Corpus  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCorpus(request)
    
    
    public updateCorpus(request: google.ai.generativelanguage.v1alpha.IUpdateCorpusRequest): Promise<google.ai.generativelanguage.v1alpha.Corpus>;

Calls UpdateCorpus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCorpusRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatecorpusrequest)`   
UpdateCorpusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.Corpus](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.corpus)>` | Promise  
  
### updateDocument(request, callback)
    
    
    public updateDocument(request: google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest, callback: google.ai.generativelanguage.v1alpha.RetrieverService.UpdateDocumentCallback): void;

Calls UpdateDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatedocumentrequest)`   
UpdateDocumentRequest message or plain object  
`callback` |  `[UpdateDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)`   
Node-style callback called with the error, if any, and Document  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDocument(request)
    
    
    public updateDocument(request: google.ai.generativelanguage.v1alpha.IUpdateDocumentRequest): Promise<google.ai.generativelanguage.v1alpha.Document>;

Calls UpdateDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.iupdatedocumentrequest)`   
UpdateDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ai.generativelanguage.v1alpha.Document](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.document)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
