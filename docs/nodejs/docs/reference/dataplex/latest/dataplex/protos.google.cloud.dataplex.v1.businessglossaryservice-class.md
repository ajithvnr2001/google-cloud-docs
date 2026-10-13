---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.businessglossaryservice-class
title: Class protos.google.cloud.dataplex.v1.BusinessGlossaryService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:24.200984+00:00
---

# Class protos.google.cloud.dataplex.v1.BusinessGlossaryService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.businessglossaryservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.BusinessGlossaryService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a BusinessGlossaryService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataplex.v1.BusinessGlossaryService

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new BusinessGlossaryService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): BusinessGlossaryService;

Creates new BusinessGlossaryService service using the specified rpc implementation.

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
`[BusinessGlossaryService](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.businessglossaryservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createGlossary(request, callback)
    
    
    public createGlossary(request: google.cloud.dataplex.v1.ICreateGlossaryRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.CreateGlossaryCallback): void;

Calls CreateGlossary.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGlossaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateglossaryrequest)`   
CreateGlossaryRequest message or plain object  
`callback` |  `[CreateGlossaryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGlossary(request)
    
    
    public createGlossary(request: google.cloud.dataplex.v1.ICreateGlossaryRequest): Promise<google.longrunning.Operation>;

Calls CreateGlossary.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGlossaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateglossaryrequest)`   
CreateGlossaryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### createGlossaryCategory(request, callback)
    
    
    public createGlossaryCategory(request: google.cloud.dataplex.v1.ICreateGlossaryCategoryRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.CreateGlossaryCategoryCallback): void;

Calls CreateGlossaryCategory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGlossaryCategoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateglossarycategoryrequest)`   
CreateGlossaryCategoryRequest message or plain object  
`callback` |  `[CreateGlossaryCategoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and GlossaryCategory  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGlossaryCategory(request)
    
    
    public createGlossaryCategory(request: google.cloud.dataplex.v1.ICreateGlossaryCategoryRequest): Promise<google.cloud.dataplex.v1.GlossaryCategory>;

Calls CreateGlossaryCategory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGlossaryCategoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateglossarycategoryrequest)`   
CreateGlossaryCategoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.GlossaryCategory](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.glossarycategory)>` | Promise  
  
### createGlossaryTerm(request, callback)
    
    
    public createGlossaryTerm(request: google.cloud.dataplex.v1.ICreateGlossaryTermRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.CreateGlossaryTermCallback): void;

Calls CreateGlossaryTerm.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGlossaryTermRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateglossarytermrequest)`   
CreateGlossaryTermRequest message or plain object  
`callback` |  `[CreateGlossaryTermCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and GlossaryTerm  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGlossaryTerm(request)
    
    
    public createGlossaryTerm(request: google.cloud.dataplex.v1.ICreateGlossaryTermRequest): Promise<google.cloud.dataplex.v1.GlossaryTerm>;

Calls CreateGlossaryTerm.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGlossaryTermRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateglossarytermrequest)`   
CreateGlossaryTermRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.GlossaryTerm](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.glossaryterm)>` | Promise  
  
### deleteGlossary(request, callback)
    
    
    public deleteGlossary(request: google.cloud.dataplex.v1.IDeleteGlossaryRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.DeleteGlossaryCallback): void;

Calls DeleteGlossary.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGlossaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteglossaryrequest)`   
DeleteGlossaryRequest message or plain object  
`callback` |  `[DeleteGlossaryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGlossary(request)
    
    
    public deleteGlossary(request: google.cloud.dataplex.v1.IDeleteGlossaryRequest): Promise<google.longrunning.Operation>;

Calls DeleteGlossary.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGlossaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteglossaryrequest)`   
DeleteGlossaryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteGlossaryCategory(request, callback)
    
    
    public deleteGlossaryCategory(request: google.cloud.dataplex.v1.IDeleteGlossaryCategoryRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.DeleteGlossaryCategoryCallback): void;

Calls DeleteGlossaryCategory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGlossaryCategoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteglossarycategoryrequest)`   
DeleteGlossaryCategoryRequest message or plain object  
`callback` |  `[DeleteGlossaryCategoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGlossaryCategory(request)
    
    
    public deleteGlossaryCategory(request: google.cloud.dataplex.v1.IDeleteGlossaryCategoryRequest): Promise<google.protobuf.Empty>;

Calls DeleteGlossaryCategory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGlossaryCategoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteglossarycategoryrequest)`   
DeleteGlossaryCategoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.protobuf.empty)>` | Promise  
  
### deleteGlossaryTerm(request, callback)
    
    
    public deleteGlossaryTerm(request: google.cloud.dataplex.v1.IDeleteGlossaryTermRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.DeleteGlossaryTermCallback): void;

Calls DeleteGlossaryTerm.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGlossaryTermRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteglossarytermrequest)`   
DeleteGlossaryTermRequest message or plain object  
`callback` |  `[DeleteGlossaryTermCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGlossaryTerm(request)
    
    
    public deleteGlossaryTerm(request: google.cloud.dataplex.v1.IDeleteGlossaryTermRequest): Promise<google.protobuf.Empty>;

Calls DeleteGlossaryTerm.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGlossaryTermRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteglossarytermrequest)`   
DeleteGlossaryTermRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.protobuf.empty)>` | Promise  
  
### getGlossary(request, callback)
    
    
    public getGlossary(request: google.cloud.dataplex.v1.IGetGlossaryRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.GetGlossaryCallback): void;

Calls GetGlossary.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGlossaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetglossaryrequest)`   
GetGlossaryRequest message or plain object  
`callback` |  `[GetGlossaryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Glossary  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGlossary(request)
    
    
    public getGlossary(request: google.cloud.dataplex.v1.IGetGlossaryRequest): Promise<google.cloud.dataplex.v1.Glossary>;

Calls GetGlossary.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGlossaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetglossaryrequest)`   
GetGlossaryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.Glossary](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.glossary)>` | Promise  
  
### getGlossaryCategory(request, callback)
    
    
    public getGlossaryCategory(request: google.cloud.dataplex.v1.IGetGlossaryCategoryRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.GetGlossaryCategoryCallback): void;

Calls GetGlossaryCategory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGlossaryCategoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetglossarycategoryrequest)`   
GetGlossaryCategoryRequest message or plain object  
`callback` |  `[GetGlossaryCategoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and GlossaryCategory  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGlossaryCategory(request)
    
    
    public getGlossaryCategory(request: google.cloud.dataplex.v1.IGetGlossaryCategoryRequest): Promise<google.cloud.dataplex.v1.GlossaryCategory>;

Calls GetGlossaryCategory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGlossaryCategoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetglossarycategoryrequest)`   
GetGlossaryCategoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.GlossaryCategory](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.glossarycategory)>` | Promise  
  
### getGlossaryTerm(request, callback)
    
    
    public getGlossaryTerm(request: google.cloud.dataplex.v1.IGetGlossaryTermRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.GetGlossaryTermCallback): void;

Calls GetGlossaryTerm.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGlossaryTermRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetglossarytermrequest)`   
GetGlossaryTermRequest message or plain object  
`callback` |  `[GetGlossaryTermCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and GlossaryTerm  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGlossaryTerm(request)
    
    
    public getGlossaryTerm(request: google.cloud.dataplex.v1.IGetGlossaryTermRequest): Promise<google.cloud.dataplex.v1.GlossaryTerm>;

Calls GetGlossaryTerm.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGlossaryTermRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetglossarytermrequest)`   
GetGlossaryTermRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.GlossaryTerm](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.glossaryterm)>` | Promise  
  
### listGlossaries(request, callback)
    
    
    public listGlossaries(request: google.cloud.dataplex.v1.IListGlossariesRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.ListGlossariesCallback): void;

Calls ListGlossaries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGlossariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistglossariesrequest)`   
ListGlossariesRequest message or plain object  
`callback` |  `[ListGlossariesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGlossariesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGlossaries(request)
    
    
    public listGlossaries(request: google.cloud.dataplex.v1.IListGlossariesRequest): Promise<google.cloud.dataplex.v1.ListGlossariesResponse>;

Calls ListGlossaries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGlossariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistglossariesrequest)`   
ListGlossariesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListGlossariesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listglossariesresponse)>` | Promise  
  
### listGlossaryCategories(request, callback)
    
    
    public listGlossaryCategories(request: google.cloud.dataplex.v1.IListGlossaryCategoriesRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.ListGlossaryCategoriesCallback): void;

Calls ListGlossaryCategories.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGlossaryCategoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistglossarycategoriesrequest)`   
ListGlossaryCategoriesRequest message or plain object  
`callback` |  `[ListGlossaryCategoriesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGlossaryCategoriesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGlossaryCategories(request)
    
    
    public listGlossaryCategories(request: google.cloud.dataplex.v1.IListGlossaryCategoriesRequest): Promise<google.cloud.dataplex.v1.ListGlossaryCategoriesResponse>;

Calls ListGlossaryCategories.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGlossaryCategoriesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistglossarycategoriesrequest)`   
ListGlossaryCategoriesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListGlossaryCategoriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listglossarycategoriesresponse)>` | Promise  
  
### listGlossaryTerms(request, callback)
    
    
    public listGlossaryTerms(request: google.cloud.dataplex.v1.IListGlossaryTermsRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.ListGlossaryTermsCallback): void;

Calls ListGlossaryTerms.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGlossaryTermsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistglossarytermsrequest)`   
ListGlossaryTermsRequest message or plain object  
`callback` |  `[ListGlossaryTermsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGlossaryTermsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGlossaryTerms(request)
    
    
    public listGlossaryTerms(request: google.cloud.dataplex.v1.IListGlossaryTermsRequest): Promise<google.cloud.dataplex.v1.ListGlossaryTermsResponse>;

Calls ListGlossaryTerms.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGlossaryTermsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistglossarytermsrequest)`   
ListGlossaryTermsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListGlossaryTermsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listglossarytermsresponse)>` | Promise  
  
### updateGlossary(request, callback)
    
    
    public updateGlossary(request: google.cloud.dataplex.v1.IUpdateGlossaryRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.UpdateGlossaryCallback): void;

Calls UpdateGlossary.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGlossaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateglossaryrequest)`   
UpdateGlossaryRequest message or plain object  
`callback` |  `[UpdateGlossaryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGlossary(request)
    
    
    public updateGlossary(request: google.cloud.dataplex.v1.IUpdateGlossaryRequest): Promise<google.longrunning.Operation>;

Calls UpdateGlossary.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGlossaryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateglossaryrequest)`   
UpdateGlossaryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### updateGlossaryCategory(request, callback)
    
    
    public updateGlossaryCategory(request: google.cloud.dataplex.v1.IUpdateGlossaryCategoryRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.UpdateGlossaryCategoryCallback): void;

Calls UpdateGlossaryCategory.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGlossaryCategoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateglossarycategoryrequest)`   
UpdateGlossaryCategoryRequest message or plain object  
`callback` |  `[UpdateGlossaryCategoryCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and GlossaryCategory  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGlossaryCategory(request)
    
    
    public updateGlossaryCategory(request: google.cloud.dataplex.v1.IUpdateGlossaryCategoryRequest): Promise<google.cloud.dataplex.v1.GlossaryCategory>;

Calls UpdateGlossaryCategory.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGlossaryCategoryRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateglossarycategoryrequest)`   
UpdateGlossaryCategoryRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.GlossaryCategory](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.glossarycategory)>` | Promise  
  
### updateGlossaryTerm(request, callback)
    
    
    public updateGlossaryTerm(request: google.cloud.dataplex.v1.IUpdateGlossaryTermRequest, callback: google.cloud.dataplex.v1.BusinessGlossaryService.UpdateGlossaryTermCallback): void;

Calls UpdateGlossaryTerm.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGlossaryTermRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateglossarytermrequest)`   
UpdateGlossaryTermRequest message or plain object  
`callback` |  `[UpdateGlossaryTermCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and GlossaryTerm  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGlossaryTerm(request)
    
    
    public updateGlossaryTerm(request: google.cloud.dataplex.v1.IUpdateGlossaryTermRequest): Promise<google.cloud.dataplex.v1.GlossaryTerm>;

Calls UpdateGlossaryTerm.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGlossaryTermRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateglossarytermrequest)`   
UpdateGlossaryTermRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.GlossaryTerm](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.glossaryterm)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
