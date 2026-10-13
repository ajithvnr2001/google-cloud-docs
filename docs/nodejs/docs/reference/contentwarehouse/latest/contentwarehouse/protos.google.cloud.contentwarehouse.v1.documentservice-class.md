---
url: https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.documentservice-class
title: Class protos.google.cloud.contentwarehouse.v1.DocumentService (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:35.271372+00:00
---

# Class protos.google.cloud.contentwarehouse.v1.DocumentService (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.documentservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.contentwarehouse.v1.DocumentService (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  1.10.0  1.9.0  1.7.0  1.5.0  1.4.0  1.3.0  0.5.1  0.4.0  0.3.1  0.1.2 

Represents a DocumentService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.contentwarehouse.v1.DocumentService

## Package

[@google-cloud/contentwarehouse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DocumentService service.

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

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DocumentService;

Creates new DocumentService service using the specified rpc implementation.

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
`[DocumentService](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.documentservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDocument(request, callback)
    
    
    public createDocument(request: google.cloud.contentwarehouse.v1.ICreateDocumentRequest, callback: google.cloud.contentwarehouse.v1.DocumentService.CreateDocumentCallback): void;

Calls CreateDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.icreatedocumentrequest)`   
CreateDocumentRequest message or plain object  
`callback` |  `[CreateDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)`   
Node-style callback called with the error, if any, and CreateDocumentResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDocument(request)
    
    
    public createDocument(request: google.cloud.contentwarehouse.v1.ICreateDocumentRequest): Promise<google.cloud.contentwarehouse.v1.CreateDocumentResponse>;

Calls CreateDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.icreatedocumentrequest)`   
CreateDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.contentwarehouse.v1.CreateDocumentResponse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.createdocumentresponse)>` | Promise  
  
### deleteDocument(request, callback)
    
    
    public deleteDocument(request: google.cloud.contentwarehouse.v1.IDeleteDocumentRequest, callback: google.cloud.contentwarehouse.v1.DocumentService.DeleteDocumentCallback): void;

Calls DeleteDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.ideletedocumentrequest)`   
DeleteDocumentRequest message or plain object  
`callback` |  `[DeleteDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDocument(request)
    
    
    public deleteDocument(request: google.cloud.contentwarehouse.v1.IDeleteDocumentRequest): Promise<google.protobuf.Empty>;

Calls DeleteDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.ideletedocumentrequest)`   
DeleteDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.protobuf.empty)>` | Promise  
  
### fetchAcl(request, callback)
    
    
    public fetchAcl(request: google.cloud.contentwarehouse.v1.IFetchAclRequest, callback: google.cloud.contentwarehouse.v1.DocumentService.FetchAclCallback): void;

Calls FetchAcl.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.ifetchaclrequest)`   
FetchAclRequest message or plain object  
`callback` |  `[FetchAclCallback](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchAclResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchAcl(request)
    
    
    public fetchAcl(request: google.cloud.contentwarehouse.v1.IFetchAclRequest): Promise<google.cloud.contentwarehouse.v1.FetchAclResponse>;

Calls FetchAcl.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.ifetchaclrequest)`   
FetchAclRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.contentwarehouse.v1.FetchAclResponse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.fetchaclresponse)>` | Promise  
  
### getDocument(request, callback)
    
    
    public getDocument(request: google.cloud.contentwarehouse.v1.IGetDocumentRequest, callback: google.cloud.contentwarehouse.v1.DocumentService.GetDocumentCallback): void;

Calls GetDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.igetdocumentrequest)`   
GetDocumentRequest message or plain object  
`callback` |  `[GetDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)`   
Node-style callback called with the error, if any, and Document  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDocument(request)
    
    
    public getDocument(request: google.cloud.contentwarehouse.v1.IGetDocumentRequest): Promise<google.cloud.contentwarehouse.v1.Document>;

Calls GetDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.igetdocumentrequest)`   
GetDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.contentwarehouse.v1.Document](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.document)>` | Promise  
  
### lockDocument(request, callback)
    
    
    public lockDocument(request: google.cloud.contentwarehouse.v1.ILockDocumentRequest, callback: google.cloud.contentwarehouse.v1.DocumentService.LockDocumentCallback): void;

Calls LockDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ILockDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.ilockdocumentrequest)`   
LockDocumentRequest message or plain object  
`callback` |  `[LockDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)`   
Node-style callback called with the error, if any, and Document  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### lockDocument(request)
    
    
    public lockDocument(request: google.cloud.contentwarehouse.v1.ILockDocumentRequest): Promise<google.cloud.contentwarehouse.v1.Document>;

Calls LockDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ILockDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.ilockdocumentrequest)`   
LockDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.contentwarehouse.v1.Document](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.document)>` | Promise  
  
### searchDocuments(request, callback)
    
    
    public searchDocuments(request: google.cloud.contentwarehouse.v1.ISearchDocumentsRequest, callback: google.cloud.contentwarehouse.v1.DocumentService.SearchDocumentsCallback): void;

Calls SearchDocuments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.isearchdocumentsrequest)`   
SearchDocumentsRequest message or plain object  
`callback` |  `[SearchDocumentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchDocumentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchDocuments(request)
    
    
    public searchDocuments(request: google.cloud.contentwarehouse.v1.ISearchDocumentsRequest): Promise<google.cloud.contentwarehouse.v1.SearchDocumentsResponse>;

Calls SearchDocuments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.isearchdocumentsrequest)`   
SearchDocumentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.contentwarehouse.v1.SearchDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.searchdocumentsresponse-class)>` | Promise  
  
### setAcl(request, callback)
    
    
    public setAcl(request: google.cloud.contentwarehouse.v1.ISetAclRequest, callback: google.cloud.contentwarehouse.v1.DocumentService.SetAclCallback): void;

Calls SetAcl.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.isetaclrequest)`   
SetAclRequest message or plain object  
`callback` |  `[SetAclCallback](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)`   
Node-style callback called with the error, if any, and SetAclResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setAcl(request)
    
    
    public setAcl(request: google.cloud.contentwarehouse.v1.ISetAclRequest): Promise<google.cloud.contentwarehouse.v1.SetAclResponse>;

Calls SetAcl.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetAclRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.isetaclrequest)`   
SetAclRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.contentwarehouse.v1.SetAclResponse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.setaclresponse)>` | Promise  
  
### updateDocument(request, callback)
    
    
    public updateDocument(request: google.cloud.contentwarehouse.v1.IUpdateDocumentRequest, callback: google.cloud.contentwarehouse.v1.DocumentService.UpdateDocumentCallback): void;

Calls UpdateDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.iupdatedocumentrequest)`   
UpdateDocumentRequest message or plain object  
`callback` |  `[UpdateDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)`   
Node-style callback called with the error, if any, and UpdateDocumentResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDocument(request)
    
    
    public updateDocument(request: google.cloud.contentwarehouse.v1.IUpdateDocumentRequest): Promise<google.cloud.contentwarehouse.v1.UpdateDocumentResponse>;

Calls UpdateDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.iupdatedocumentrequest)`   
UpdateDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.contentwarehouse.v1.UpdateDocumentResponse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.updatedocumentresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
