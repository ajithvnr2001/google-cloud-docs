---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.analyticshubservice-class
title: Class protos.google.cloud.bigquery.analyticshub.v1.AnalyticsHubService (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:28.928234+00:00
---

# Class protos.google.cloud.bigquery.analyticshub.v1.AnalyticsHubService (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.analyticshubservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.bigquery.analyticshub.v1.AnalyticsHubService (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  2.2.0  1.6.0  1.1.0  0.2.2  0.1.2 

Represents an AnalyticsHubService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.bigquery.analyticshub.v1.AnalyticsHubService

## Package

[@google-cloud/bigquery-analyticshub](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AnalyticsHubService service.

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

### approveQueryTemplate(request, callback)
    
    
    public approveQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.IApproveQueryTemplateRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.ApproveQueryTemplateCallback): void;

Calls ApproveQueryTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IApproveQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.iapprovequerytemplaterequest)`   
ApproveQueryTemplateRequest message or plain object  
`callback` |  `[ApproveQueryTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryTemplate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### approveQueryTemplate(request)
    
    
    public approveQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.IApproveQueryTemplateRequest): Promise<google.cloud.bigquery.analyticshub.v1.QueryTemplate>;

Calls ApproveQueryTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IApproveQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.iapprovequerytemplaterequest)`   
ApproveQueryTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.QueryTemplate](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.querytemplate-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AnalyticsHubService;

Creates new AnalyticsHubService service using the specified rpc implementation.

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
`[AnalyticsHubService](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.analyticshubservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataExchange(request, callback)
    
    
    public createDataExchange(request: google.cloud.bigquery.analyticshub.v1.ICreateDataExchangeRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.CreateDataExchangeCallback): void;

Calls CreateDataExchange.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataExchangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.icreatedataexchangerequest)`   
CreateDataExchangeRequest message or plain object  
`callback` |  `[CreateDataExchangeCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and DataExchange  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataExchange(request)
    
    
    public createDataExchange(request: google.cloud.bigquery.analyticshub.v1.ICreateDataExchangeRequest): Promise<google.cloud.bigquery.analyticshub.v1.DataExchange>;

Calls CreateDataExchange.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataExchangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.icreatedataexchangerequest)`   
CreateDataExchangeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.DataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.dataexchange)>` | Promise  
  
### createListing(request, callback)
    
    
    public createListing(request: google.cloud.bigquery.analyticshub.v1.ICreateListingRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.CreateListingCallback): void;

Calls CreateListing.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateListingRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.icreatelistingrequest)`   
CreateListingRequest message or plain object  
`callback` |  `[CreateListingCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Listing  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createListing(request)
    
    
    public createListing(request: google.cloud.bigquery.analyticshub.v1.ICreateListingRequest): Promise<google.cloud.bigquery.analyticshub.v1.Listing>;

Calls CreateListing.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateListingRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.icreatelistingrequest)`   
CreateListingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.Listing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listing-class)>` | Promise  
  
### createQueryTemplate(request, callback)
    
    
    public createQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.ICreateQueryTemplateRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.CreateQueryTemplateCallback): void;

Calls CreateQueryTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.icreatequerytemplaterequest)`   
CreateQueryTemplateRequest message or plain object  
`callback` |  `[CreateQueryTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryTemplate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createQueryTemplate(request)
    
    
    public createQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.ICreateQueryTemplateRequest): Promise<google.cloud.bigquery.analyticshub.v1.QueryTemplate>;

Calls CreateQueryTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.icreatequerytemplaterequest)`   
CreateQueryTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.QueryTemplate](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.querytemplate-class)>` | Promise  
  
### deleteDataExchange(request, callback)
    
    
    public deleteDataExchange(request: google.cloud.bigquery.analyticshub.v1.IDeleteDataExchangeRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.DeleteDataExchangeCallback): void;

Calls DeleteDataExchange.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataExchangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ideletedataexchangerequest)`   
DeleteDataExchangeRequest message or plain object  
`callback` |  `[DeleteDataExchangeCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataExchange(request)
    
    
    public deleteDataExchange(request: google.cloud.bigquery.analyticshub.v1.IDeleteDataExchangeRequest): Promise<google.protobuf.Empty>;

Calls DeleteDataExchange.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataExchangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ideletedataexchangerequest)`   
DeleteDataExchangeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.protobuf.empty)>` | Promise  
  
### deleteListing(request, callback)
    
    
    public deleteListing(request: google.cloud.bigquery.analyticshub.v1.IDeleteListingRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.DeleteListingCallback): void;

Calls DeleteListing.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteListingRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ideletelistingrequest)`   
DeleteListingRequest message or plain object  
`callback` |  `[DeleteListingCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteListing(request)
    
    
    public deleteListing(request: google.cloud.bigquery.analyticshub.v1.IDeleteListingRequest): Promise<google.protobuf.Empty>;

Calls DeleteListing.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteListingRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ideletelistingrequest)`   
DeleteListingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.protobuf.empty)>` | Promise  
  
### deleteQueryTemplate(request, callback)
    
    
    public deleteQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.IDeleteQueryTemplateRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.DeleteQueryTemplateCallback): void;

Calls DeleteQueryTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ideletequerytemplaterequest)`   
DeleteQueryTemplateRequest message or plain object  
`callback` |  `[DeleteQueryTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteQueryTemplate(request)
    
    
    public deleteQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.IDeleteQueryTemplateRequest): Promise<google.protobuf.Empty>;

Calls DeleteQueryTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ideletequerytemplaterequest)`   
DeleteQueryTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.protobuf.empty)>` | Promise  
  
### deleteSubscription(request, callback)
    
    
    public deleteSubscription(request: google.cloud.bigquery.analyticshub.v1.IDeleteSubscriptionRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.DeleteSubscriptionCallback): void;

Calls DeleteSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ideletesubscriptionrequest)`   
DeleteSubscriptionRequest message or plain object  
`callback` |  `[DeleteSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSubscription(request)
    
    
    public deleteSubscription(request: google.cloud.bigquery.analyticshub.v1.IDeleteSubscriptionRequest): Promise<google.longrunning.Operation>;

Calls DeleteSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ideletesubscriptionrequest)`   
DeleteSubscriptionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.longrunning.operation)>` | Promise  
  
### getDataExchange(request, callback)
    
    
    public getDataExchange(request: google.cloud.bigquery.analyticshub.v1.IGetDataExchangeRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.GetDataExchangeCallback): void;

Calls GetDataExchange.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataExchangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.igetdataexchangerequest)`   
GetDataExchangeRequest message or plain object  
`callback` |  `[GetDataExchangeCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and DataExchange  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataExchange(request)
    
    
    public getDataExchange(request: google.cloud.bigquery.analyticshub.v1.IGetDataExchangeRequest): Promise<google.cloud.bigquery.analyticshub.v1.DataExchange>;

Calls GetDataExchange.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataExchangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.igetdataexchangerequest)`   
GetDataExchangeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.DataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.dataexchange)>` | Promise  
  
### getIamPolicy(request, callback)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.GetIamPolicyCallback): void;

Calls GetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
`callback` |  `[GetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls GetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.iam.v1.policy)>` | Promise  
  
### getListing(request, callback)
    
    
    public getListing(request: google.cloud.bigquery.analyticshub.v1.IGetListingRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.GetListingCallback): void;

Calls GetListing.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetListingRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.igetlistingrequest)`   
GetListingRequest message or plain object  
`callback` |  `[GetListingCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Listing  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getListing(request)
    
    
    public getListing(request: google.cloud.bigquery.analyticshub.v1.IGetListingRequest): Promise<google.cloud.bigquery.analyticshub.v1.Listing>;

Calls GetListing.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetListingRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.igetlistingrequest)`   
GetListingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.Listing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listing-class)>` | Promise  
  
### getQueryTemplate(request, callback)
    
    
    public getQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.IGetQueryTemplateRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.GetQueryTemplateCallback): void;

Calls GetQueryTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.igetquerytemplaterequest)`   
GetQueryTemplateRequest message or plain object  
`callback` |  `[GetQueryTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryTemplate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getQueryTemplate(request)
    
    
    public getQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.IGetQueryTemplateRequest): Promise<google.cloud.bigquery.analyticshub.v1.QueryTemplate>;

Calls GetQueryTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.igetquerytemplaterequest)`   
GetQueryTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.QueryTemplate](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.querytemplate-class)>` | Promise  
  
### getSubscription(request, callback)
    
    
    public getSubscription(request: google.cloud.bigquery.analyticshub.v1.IGetSubscriptionRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.GetSubscriptionCallback): void;

Calls GetSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.igetsubscriptionrequest)`   
GetSubscriptionRequest message or plain object  
`callback` |  `[GetSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Subscription  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSubscription(request)
    
    
    public getSubscription(request: google.cloud.bigquery.analyticshub.v1.IGetSubscriptionRequest): Promise<google.cloud.bigquery.analyticshub.v1.Subscription>;

Calls GetSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.igetsubscriptionrequest)`   
GetSubscriptionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.Subscription](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.subscription-class)>` | Promise  
  
### listDataExchanges(request, callback)
    
    
    public listDataExchanges(request: google.cloud.bigquery.analyticshub.v1.IListDataExchangesRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.ListDataExchangesCallback): void;

Calls ListDataExchanges.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataExchangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistdataexchangesrequest)`   
ListDataExchangesRequest message or plain object  
`callback` |  `[ListDataExchangesCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataExchangesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataExchanges(request)
    
    
    public listDataExchanges(request: google.cloud.bigquery.analyticshub.v1.IListDataExchangesRequest): Promise<google.cloud.bigquery.analyticshub.v1.ListDataExchangesResponse>;

Calls ListDataExchanges.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataExchangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistdataexchangesrequest)`   
ListDataExchangesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.ListDataExchangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listdataexchangesresponse)>` | Promise  
  
### listListings(request, callback)
    
    
    public listListings(request: google.cloud.bigquery.analyticshub.v1.IListListingsRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.ListListingsCallback): void;

Calls ListListings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListListingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistlistingsrequest)`   
ListListingsRequest message or plain object  
`callback` |  `[ListListingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListListingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listListings(request)
    
    
    public listListings(request: google.cloud.bigquery.analyticshub.v1.IListListingsRequest): Promise<google.cloud.bigquery.analyticshub.v1.ListListingsResponse>;

Calls ListListings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListListingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistlistingsrequest)`   
ListListingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.ListListingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listlistingsresponse)>` | Promise  
  
### listOrgDataExchanges(request, callback)
    
    
    public listOrgDataExchanges(request: google.cloud.bigquery.analyticshub.v1.IListOrgDataExchangesRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.ListOrgDataExchangesCallback): void;

Calls ListOrgDataExchanges.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListOrgDataExchangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistorgdataexchangesrequest)`   
ListOrgDataExchangesRequest message or plain object  
`callback` |  `[ListOrgDataExchangesCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListOrgDataExchangesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listOrgDataExchanges(request)
    
    
    public listOrgDataExchanges(request: google.cloud.bigquery.analyticshub.v1.IListOrgDataExchangesRequest): Promise<google.cloud.bigquery.analyticshub.v1.ListOrgDataExchangesResponse>;

Calls ListOrgDataExchanges.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListOrgDataExchangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistorgdataexchangesrequest)`   
ListOrgDataExchangesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.ListOrgDataExchangesResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listorgdataexchangesresponse)>` | Promise  
  
### listQueryTemplates(request, callback)
    
    
    public listQueryTemplates(request: google.cloud.bigquery.analyticshub.v1.IListQueryTemplatesRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.ListQueryTemplatesCallback): void;

Calls ListQueryTemplates.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListQueryTemplatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistquerytemplatesrequest)`   
ListQueryTemplatesRequest message or plain object  
`callback` |  `[ListQueryTemplatesCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListQueryTemplatesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listQueryTemplates(request)
    
    
    public listQueryTemplates(request: google.cloud.bigquery.analyticshub.v1.IListQueryTemplatesRequest): Promise<google.cloud.bigquery.analyticshub.v1.ListQueryTemplatesResponse>;

Calls ListQueryTemplates.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListQueryTemplatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistquerytemplatesrequest)`   
ListQueryTemplatesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.ListQueryTemplatesResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listquerytemplatesresponse)>` | Promise  
  
### listSharedResourceSubscriptions(request, callback)
    
    
    public listSharedResourceSubscriptions(request: google.cloud.bigquery.analyticshub.v1.IListSharedResourceSubscriptionsRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.ListSharedResourceSubscriptionsCallback): void;

Calls ListSharedResourceSubscriptions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSharedResourceSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistsharedresourcesubscriptionsrequest)`   
ListSharedResourceSubscriptionsRequest message or plain object  
`callback` |  `[ListSharedResourceSubscriptionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSharedResourceSubscriptionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSharedResourceSubscriptions(request)
    
    
    public listSharedResourceSubscriptions(request: google.cloud.bigquery.analyticshub.v1.IListSharedResourceSubscriptionsRequest): Promise<google.cloud.bigquery.analyticshub.v1.ListSharedResourceSubscriptionsResponse>;

Calls ListSharedResourceSubscriptions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSharedResourceSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistsharedresourcesubscriptionsrequest)`   
ListSharedResourceSubscriptionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.ListSharedResourceSubscriptionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listsharedresourcesubscriptionsresponse)>` | Promise  
  
### listSubscriptions(request, callback)
    
    
    public listSubscriptions(request: google.cloud.bigquery.analyticshub.v1.IListSubscriptionsRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.ListSubscriptionsCallback): void;

Calls ListSubscriptions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistsubscriptionsrequest)`   
ListSubscriptionsRequest message or plain object  
`callback` |  `[ListSubscriptionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSubscriptionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSubscriptions(request)
    
    
    public listSubscriptions(request: google.cloud.bigquery.analyticshub.v1.IListSubscriptionsRequest): Promise<google.cloud.bigquery.analyticshub.v1.ListSubscriptionsResponse>;

Calls ListSubscriptions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.ilistsubscriptionsrequest)`   
ListSubscriptionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.ListSubscriptionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listsubscriptionsresponse)>` | Promise  
  
### refreshSubscription(request, callback)
    
    
    public refreshSubscription(request: google.cloud.bigquery.analyticshub.v1.IRefreshSubscriptionRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.RefreshSubscriptionCallback): void;

Calls RefreshSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRefreshSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.irefreshsubscriptionrequest)`   
RefreshSubscriptionRequest message or plain object  
`callback` |  `[RefreshSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### refreshSubscription(request)
    
    
    public refreshSubscription(request: google.cloud.bigquery.analyticshub.v1.IRefreshSubscriptionRequest): Promise<google.longrunning.Operation>;

Calls RefreshSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRefreshSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.irefreshsubscriptionrequest)`   
RefreshSubscriptionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.longrunning.operation)>` | Promise  
  
### revokeSubscription(request, callback)
    
    
    public revokeSubscription(request: google.cloud.bigquery.analyticshub.v1.IRevokeSubscriptionRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.RevokeSubscriptionCallback): void;

Calls RevokeSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRevokeSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.irevokesubscriptionrequest)`   
RevokeSubscriptionRequest message or plain object  
`callback` |  `[RevokeSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and RevokeSubscriptionResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### revokeSubscription(request)
    
    
    public revokeSubscription(request: google.cloud.bigquery.analyticshub.v1.IRevokeSubscriptionRequest): Promise<google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionResponse>;

Calls RevokeSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRevokeSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.irevokesubscriptionrequest)`   
RevokeSubscriptionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.revokesubscriptionresponse)>` | Promise  
  
### setIamPolicy(request, callback)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.SetIamPolicyCallback): void;

Calls SetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
`callback` |  `[SetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls SetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.iam.v1.policy)>` | Promise  
  
### submitQueryTemplate(request, callback)
    
    
    public submitQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.ISubmitQueryTemplateRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.SubmitQueryTemplateCallback): void;

Calls SubmitQueryTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubmitQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubmitquerytemplaterequest)`   
SubmitQueryTemplateRequest message or plain object  
`callback` |  `[SubmitQueryTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryTemplate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### submitQueryTemplate(request)
    
    
    public submitQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.ISubmitQueryTemplateRequest): Promise<google.cloud.bigquery.analyticshub.v1.QueryTemplate>;

Calls SubmitQueryTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISubmitQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubmitquerytemplaterequest)`   
SubmitQueryTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.QueryTemplate](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.querytemplate-class)>` | Promise  
  
### subscribeDataExchange(request, callback)
    
    
    public subscribeDataExchange(request: google.cloud.bigquery.analyticshub.v1.ISubscribeDataExchangeRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.SubscribeDataExchangeCallback): void;

Calls SubscribeDataExchange.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubscribeDataExchangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubscribedataexchangerequest)`   
SubscribeDataExchangeRequest message or plain object  
`callback` |  `[SubscribeDataExchangeCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### subscribeDataExchange(request)
    
    
    public subscribeDataExchange(request: google.cloud.bigquery.analyticshub.v1.ISubscribeDataExchangeRequest): Promise<google.longrunning.Operation>;

Calls SubscribeDataExchange.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISubscribeDataExchangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubscribedataexchangerequest)`   
SubscribeDataExchangeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.longrunning.operation)>` | Promise  
  
### subscribeListing(request, callback)
    
    
    public subscribeListing(request: google.cloud.bigquery.analyticshub.v1.ISubscribeListingRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.SubscribeListingCallback): void;

Calls SubscribeListing.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubscribeListingRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubscribelistingrequest)`   
SubscribeListingRequest message or plain object  
`callback` |  `[SubscribeListingCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and SubscribeListingResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### subscribeListing(request)
    
    
    public subscribeListing(request: google.cloud.bigquery.analyticshub.v1.ISubscribeListingRequest): Promise<google.cloud.bigquery.analyticshub.v1.SubscribeListingResponse>;

Calls SubscribeListing.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISubscribeListingRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.isubscribelistingrequest)`   
SubscribeListingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.SubscribeListingResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.subscribelistingresponse)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and TestIamPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest): Promise<google.iam.v1.TestIamPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.TestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.iam.v1.testiampermissionsresponse)>` | Promise  
  
### updateDataExchange(request, callback)
    
    
    public updateDataExchange(request: google.cloud.bigquery.analyticshub.v1.IUpdateDataExchangeRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.UpdateDataExchangeCallback): void;

Calls UpdateDataExchange.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataExchangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.iupdatedataexchangerequest)`   
UpdateDataExchangeRequest message or plain object  
`callback` |  `[UpdateDataExchangeCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and DataExchange  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataExchange(request)
    
    
    public updateDataExchange(request: google.cloud.bigquery.analyticshub.v1.IUpdateDataExchangeRequest): Promise<google.cloud.bigquery.analyticshub.v1.DataExchange>;

Calls UpdateDataExchange.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataExchangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.iupdatedataexchangerequest)`   
UpdateDataExchangeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.DataExchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.dataexchange)>` | Promise  
  
### updateListing(request, callback)
    
    
    public updateListing(request: google.cloud.bigquery.analyticshub.v1.IUpdateListingRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.UpdateListingCallback): void;

Calls UpdateListing.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateListingRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.iupdatelistingrequest)`   
UpdateListingRequest message or plain object  
`callback` |  `[UpdateListingCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and Listing  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateListing(request)
    
    
    public updateListing(request: google.cloud.bigquery.analyticshub.v1.IUpdateListingRequest): Promise<google.cloud.bigquery.analyticshub.v1.Listing>;

Calls UpdateListing.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateListingRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.iupdatelistingrequest)`   
UpdateListingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.Listing](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.listing-class)>` | Promise  
  
### updateQueryTemplate(request, callback)
    
    
    public updateQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.IUpdateQueryTemplateRequest, callback: google.cloud.bigquery.analyticshub.v1.AnalyticsHubService.UpdateQueryTemplateCallback): void;

Calls UpdateQueryTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.iupdatequerytemplaterequest)`   
UpdateQueryTemplateRequest message or plain object  
`callback` |  `[UpdateQueryTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryTemplate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateQueryTemplate(request)
    
    
    public updateQueryTemplate(request: google.cloud.bigquery.analyticshub.v1.IUpdateQueryTemplateRequest): Promise<google.cloud.bigquery.analyticshub.v1.QueryTemplate>;

Calls UpdateQueryTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateQueryTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.iupdatequerytemplaterequest)`   
UpdateQueryTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.bigquery.analyticshub.v1.QueryTemplate](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-analyticshub/latest/bigquery-analyticshub/protos.google.cloud.bigquery.analyticshub.v1.querytemplate-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
