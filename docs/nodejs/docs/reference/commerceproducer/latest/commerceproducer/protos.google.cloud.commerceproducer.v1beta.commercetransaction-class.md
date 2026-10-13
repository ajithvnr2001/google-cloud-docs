---
url: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.commercetransaction-class
title: Class protos.google.cloud.commerceproducer.v1beta.CommerceTransaction (0.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:58.643178+00:00
---

# Class protos.google.cloud.commerceproducer.v1beta.CommerceTransaction (0.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.commercetransaction-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.commerceproducer.v1beta.CommerceTransaction (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a CommerceTransaction

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.commerceproducer.v1beta.CommerceTransaction

## Package

[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CommerceTransaction service.

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

### cancelPrivateOffer(request, callback)
    
    
    public cancelPrivateOffer(request: google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.CancelPrivateOfferCallback): void;

Calls CancelPrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icancelprivateofferrequest)`   
CancelPrivateOfferRequest message or plain object  
`callback` |  `[CancelPrivateOfferCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and PrivateOffer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelPrivateOffer(request)
    
    
    public cancelPrivateOffer(request: google.cloud.commerceproducer.v1beta.ICancelPrivateOfferRequest): Promise<google.cloud.commerceproducer.v1beta.PrivateOffer>;

Calls CancelPrivateOffer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icancelprivateofferrequest)`   
CancelPrivateOfferRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.PrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CommerceTransaction;

Creates new CommerceTransaction service using the specified rpc implementation.

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
`[CommerceTransaction](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.commercetransaction-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createPrivateOffer(request, callback)
    
    
    public createPrivateOffer(request: google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.CreatePrivateOfferCallback): void;

Calls CreatePrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferrequest)`   
CreatePrivateOfferRequest message or plain object  
`callback` |  `[CreatePrivateOfferCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and PrivateOffer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPrivateOffer(request)
    
    
    public createPrivateOffer(request: google.cloud.commerceproducer.v1beta.ICreatePrivateOfferRequest): Promise<google.cloud.commerceproducer.v1beta.PrivateOffer>;

Calls CreatePrivateOffer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferrequest)`   
CreatePrivateOfferRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.PrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class)>` | Promise  
  
### createPrivateOfferDocument(request, callback)
    
    
    public createPrivateOfferDocument(request: google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.CreatePrivateOfferDocumentCallback): void;

Calls CreatePrivateOfferDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferdocumentrequest)`   
CreatePrivateOfferDocumentRequest message or plain object  
`callback` |  `[CreatePrivateOfferDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and PrivateOfferDocument  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPrivateOfferDocument(request)
    
    
    public createPrivateOfferDocument(request: google.cloud.commerceproducer.v1beta.ICreatePrivateOfferDocumentRequest): Promise<google.cloud.commerceproducer.v1beta.PrivateOfferDocument>;

Calls CreatePrivateOfferDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.icreateprivateofferdocumentrequest)`   
CreatePrivateOfferDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.PrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateofferdocument-class)>` | Promise  
  
### deletePrivateOffer(request, callback)
    
    
    public deletePrivateOffer(request: google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.DeletePrivateOfferCallback): void;

Calls DeletePrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferrequest)`   
DeletePrivateOfferRequest message or plain object  
`callback` |  `[DeletePrivateOfferCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePrivateOffer(request)
    
    
    public deletePrivateOffer(request: google.cloud.commerceproducer.v1beta.IDeletePrivateOfferRequest): Promise<google.protobuf.Empty>;

Calls DeletePrivateOffer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferrequest)`   
DeletePrivateOfferRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.protobuf.empty)>` | Promise  
  
### deletePrivateOfferDocument(request, callback)
    
    
    public deletePrivateOfferDocument(request: google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.DeletePrivateOfferDocumentCallback): void;

Calls DeletePrivateOfferDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferdocumentrequest)`   
DeletePrivateOfferDocumentRequest message or plain object  
`callback` |  `[DeletePrivateOfferDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePrivateOfferDocument(request)
    
    
    public deletePrivateOfferDocument(request: google.cloud.commerceproducer.v1beta.IDeletePrivateOfferDocumentRequest): Promise<google.protobuf.Empty>;

Calls DeletePrivateOfferDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ideleteprivateofferdocumentrequest)`   
DeletePrivateOfferDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.protobuf.empty)>` | Promise  
  
### getPrivateOffer(request, callback)
    
    
    public getPrivateOffer(request: google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.GetPrivateOfferCallback): void;

Calls GetPrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferrequest)`   
GetPrivateOfferRequest message or plain object  
`callback` |  `[GetPrivateOfferCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and PrivateOffer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPrivateOffer(request)
    
    
    public getPrivateOffer(request: google.cloud.commerceproducer.v1beta.IGetPrivateOfferRequest): Promise<google.cloud.commerceproducer.v1beta.PrivateOffer>;

Calls GetPrivateOffer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferrequest)`   
GetPrivateOfferRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.PrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class)>` | Promise  
  
### getPrivateOfferDocument(request, callback)
    
    
    public getPrivateOfferDocument(request: google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.GetPrivateOfferDocumentCallback): void;

Calls GetPrivateOfferDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferdocumentrequest)`   
GetPrivateOfferDocumentRequest message or plain object  
`callback` |  `[GetPrivateOfferDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and PrivateOfferDocument  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPrivateOfferDocument(request)
    
    
    public getPrivateOfferDocument(request: google.cloud.commerceproducer.v1beta.IGetPrivateOfferDocumentRequest): Promise<google.cloud.commerceproducer.v1beta.PrivateOfferDocument>;

Calls GetPrivateOfferDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetprivateofferdocumentrequest)`   
GetPrivateOfferDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.PrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateofferdocument-class)>` | Promise  
  
### getService(request, callback)
    
    
    public getService(request: google.cloud.commerceproducer.v1beta.IGetServiceRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.GetServiceCallback): void;

Calls GetService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetservicerequest)`   
GetServiceRequest message or plain object  
`callback` |  `[GetServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and Service  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getService(request)
    
    
    public getService(request: google.cloud.commerceproducer.v1beta.IGetServiceRequest): Promise<google.cloud.commerceproducer.v1beta.Service>;

Calls GetService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetservicerequest)`   
GetServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.Service](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.service)>` | Promise  
  
### getSku(request, callback)
    
    
    public getSku(request: google.cloud.commerceproducer.v1beta.IGetSkuRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.GetSkuCallback): void;

Calls GetSku.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskurequest)`   
GetSkuRequest message or plain object  
`callback` |  `[GetSkuCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and Sku  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSku(request)
    
    
    public getSku(request: google.cloud.commerceproducer.v1beta.IGetSkuRequest): Promise<google.cloud.commerceproducer.v1beta.Sku>;

Calls GetSku.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskurequest)`   
GetSkuRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.Sku](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.sku-class)>` | Promise  
  
### getSkuGroup(request, callback)
    
    
    public getSkuGroup(request: google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.GetSkuGroupCallback): void;

Calls GetSkuGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskugrouprequest)`   
GetSkuGroupRequest message or plain object  
`callback` |  `[GetSkuGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and SkuGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSkuGroup(request)
    
    
    public getSkuGroup(request: google.cloud.commerceproducer.v1beta.IGetSkuGroupRequest): Promise<google.cloud.commerceproducer.v1beta.SkuGroup>;

Calls GetSkuGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSkuGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetskugrouprequest)`   
GetSkuGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.SkuGroup](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.skugroup)>` | Promise  
  
### getStandardOffer(request, callback)
    
    
    public getStandardOffer(request: google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.GetStandardOfferCallback): void;

Calls GetStandardOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStandardOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetstandardofferrequest)`   
GetStandardOfferRequest message or plain object  
`callback` |  `[GetStandardOfferCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and StandardOffer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStandardOffer(request)
    
    
    public getStandardOffer(request: google.cloud.commerceproducer.v1beta.IGetStandardOfferRequest): Promise<google.cloud.commerceproducer.v1beta.StandardOffer>;

Calls GetStandardOffer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetStandardOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.igetstandardofferrequest)`   
GetStandardOfferRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.StandardOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer-class)>` | Promise  
  
### listPrivateOfferDocuments(request, callback)
    
    
    public listPrivateOfferDocuments(request: google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.ListPrivateOfferDocumentsCallback): void;

Calls ListPrivateOfferDocuments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsrequest)`   
ListPrivateOfferDocumentsRequest message or plain object  
`callback` |  `[ListPrivateOfferDocumentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPrivateOfferDocumentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPrivateOfferDocuments(request)
    
    
    public listPrivateOfferDocuments(request: google.cloud.commerceproducer.v1beta.IListPrivateOfferDocumentsRequest): Promise<google.cloud.commerceproducer.v1beta.ListPrivateOfferDocumentsResponse>;

Calls ListPrivateOfferDocuments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOfferDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateofferdocumentsrequest)`   
ListPrivateOfferDocumentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.ListPrivateOfferDocumentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.listprivateofferdocumentsresponse)>` | Promise  
  
### listPrivateOffers(request, callback)
    
    
    public listPrivateOffers(request: google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.ListPrivateOffersCallback): void;

Calls ListPrivateOffers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersrequest)`   
ListPrivateOffersRequest message or plain object  
`callback` |  `[ListPrivateOffersCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPrivateOffersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPrivateOffers(request)
    
    
    public listPrivateOffers(request: google.cloud.commerceproducer.v1beta.IListPrivateOffersRequest): Promise<google.cloud.commerceproducer.v1beta.ListPrivateOffersResponse>;

Calls ListPrivateOffers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPrivateOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistprivateoffersrequest)`   
ListPrivateOffersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.ListPrivateOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.listprivateoffersresponse)>` | Promise  
  
### listServices(request, callback)
    
    
    public listServices(request: google.cloud.commerceproducer.v1beta.IListServicesRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.ListServicesCallback): void;

Calls ListServices.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesrequest)`   
ListServicesRequest message or plain object  
`callback` |  `[ListServicesCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and ListServicesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServices(request)
    
    
    public listServices(request: google.cloud.commerceproducer.v1beta.IListServicesRequest): Promise<google.cloud.commerceproducer.v1beta.ListServicesResponse>;

Calls ListServices.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistservicesrequest)`   
ListServicesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.ListServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.listservicesresponse)>` | Promise  
  
### listSkuGroups(request, callback)
    
    
    public listSkuGroups(request: google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.ListSkuGroupsCallback): void;

Calls ListSkuGroups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsrequest)`   
ListSkuGroupsRequest message or plain object  
`callback` |  `[ListSkuGroupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSkuGroupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkuGroups(request)
    
    
    public listSkuGroups(request: google.cloud.commerceproducer.v1beta.IListSkuGroupsRequest): Promise<google.cloud.commerceproducer.v1beta.ListSkuGroupsResponse>;

Calls ListSkuGroups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSkuGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskugroupsrequest)`   
ListSkuGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.ListSkuGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.listskugroupsresponse)>` | Promise  
  
### listSkus(request, callback)
    
    
    public listSkus(request: google.cloud.commerceproducer.v1beta.IListSkusRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.ListSkusCallback): void;

Calls ListSkus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusrequest)`   
ListSkusRequest message or plain object  
`callback` |  `[ListSkusCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSkusResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSkus(request)
    
    
    public listSkus(request: google.cloud.commerceproducer.v1beta.IListSkusRequest): Promise<google.cloud.commerceproducer.v1beta.ListSkusResponse>;

Calls ListSkus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSkusRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ilistskusrequest)`   
ListSkusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.ListSkusResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.listskusresponse)>` | Promise  
  
### listStandardOffers(request, callback)
    
    
    public listStandardOffers(request: google.cloud.commerceproducer.v1beta.IListStandardOffersRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.ListStandardOffersCallback): void;

Calls ListStandardOffers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListStandardOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersrequest)`   
ListStandardOffersRequest message or plain object  
`callback` |  `[ListStandardOffersCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and ListStandardOffersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listStandardOffers(request)
    
    
    public listStandardOffers(request: google.cloud.commerceproducer.v1beta.IListStandardOffersRequest): Promise<google.cloud.commerceproducer.v1beta.ListStandardOffersResponse>;

Calls ListStandardOffers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListStandardOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iliststandardoffersrequest)`   
ListStandardOffersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.ListStandardOffersResponse](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.liststandardoffersresponse)>` | Promise  
  
### publishPrivateOffer(request, callback)
    
    
    public publishPrivateOffer(request: google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.PublishPrivateOfferCallback): void;

Calls PublishPrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPublishPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ipublishprivateofferrequest)`   
PublishPrivateOfferRequest message or plain object  
`callback` |  `[PublishPrivateOfferCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and PrivateOffer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### publishPrivateOffer(request)
    
    
    public publishPrivateOffer(request: google.cloud.commerceproducer.v1beta.IPublishPrivateOfferRequest): Promise<google.cloud.commerceproducer.v1beta.PrivateOffer>;

Calls PublishPrivateOffer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPublishPrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.ipublishprivateofferrequest)`   
PublishPrivateOfferRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.PrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class)>` | Promise  
  
### updatePrivateOffer(request, callback)
    
    
    public updatePrivateOffer(request: google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.UpdatePrivateOfferCallback): void;

Calls UpdatePrivateOffer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferrequest)`   
UpdatePrivateOfferRequest message or plain object  
`callback` |  `[UpdatePrivateOfferCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and PrivateOffer  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePrivateOffer(request)
    
    
    public updatePrivateOffer(request: google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferRequest): Promise<google.cloud.commerceproducer.v1beta.PrivateOffer>;

Calls UpdatePrivateOffer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrivateOfferRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferrequest)`   
UpdatePrivateOfferRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.PrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class)>` | Promise  
  
### updatePrivateOfferDocument(request, callback)
    
    
    public updatePrivateOfferDocument(request: google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest, callback: google.cloud.commerceproducer.v1beta.CommerceTransaction.UpdatePrivateOfferDocumentCallback): void;

Calls UpdatePrivateOfferDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferdocumentrequest)`   
UpdatePrivateOfferDocumentRequest message or plain object  
`callback` |  `[UpdatePrivateOfferDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)`   
Node-style callback called with the error, if any, and PrivateOfferDocument  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePrivateOfferDocument(request)
    
    
    public updatePrivateOfferDocument(request: google.cloud.commerceproducer.v1beta.IUpdatePrivateOfferDocumentRequest): Promise<google.cloud.commerceproducer.v1beta.PrivateOfferDocument>;

Calls UpdatePrivateOfferDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePrivateOfferDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iupdateprivateofferdocumentrequest)`   
UpdatePrivateOfferDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.commerceproducer.v1beta.PrivateOfferDocument](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateofferdocument-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
