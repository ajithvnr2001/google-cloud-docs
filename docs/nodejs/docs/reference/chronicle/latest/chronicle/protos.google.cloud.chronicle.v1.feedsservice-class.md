---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feedsservice-class
title: Class protos.google.cloud.chronicle.v1.FeedsService (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:36.990630+00:00
---

# Class protos.google.cloud.chronicle.v1.FeedsService (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feedsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.FeedsService (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a FeedsService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.chronicle.v1.FeedsService

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new FeedsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): FeedsService;

Creates new FeedsService service using the specified rpc implementation.

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
`[FeedsService](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feedsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createFeed(request, callback)
    
    
    public createFeed(request: google.cloud.chronicle.v1.ICreateFeedRequest, callback: google.cloud.chronicle.v1.FeedsService.CreateFeedCallback): void;

Calls CreateFeed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatefeedrequest)`   
CreateFeedRequest message or plain object  
`callback` |  `[CreateFeedCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Feed  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFeed(request)
    
    
    public createFeed(request: google.cloud.chronicle.v1.ICreateFeedRequest): Promise<google.cloud.chronicle.v1.Feed>;

Calls CreateFeed.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatefeedrequest)`   
CreateFeedRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.Feed](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feed-class)>` | Promise  
  
### deleteFeed(request, callback)
    
    
    public deleteFeed(request: google.cloud.chronicle.v1.IDeleteFeedRequest, callback: google.cloud.chronicle.v1.FeedsService.DeleteFeedCallback): void;

Calls DeleteFeed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletefeedrequest)`   
DeleteFeedRequest message or plain object  
`callback` |  `[DeleteFeedCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFeed(request)
    
    
    public deleteFeed(request: google.cloud.chronicle.v1.IDeleteFeedRequest): Promise<google.protobuf.Empty>;

Calls DeleteFeed.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletefeedrequest)`   
DeleteFeedRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.protobuf.empty)>` | Promise  
  
### disableFeed(request, callback)
    
    
    public disableFeed(request: google.cloud.chronicle.v1.IDisableFeedRequest, callback: google.cloud.chronicle.v1.FeedsService.DisableFeedCallback): void;

Calls DisableFeed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.idisablefeedrequest)`   
DisableFeedRequest message or plain object  
`callback` |  `[DisableFeedCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Feed  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disableFeed(request)
    
    
    public disableFeed(request: google.cloud.chronicle.v1.IDisableFeedRequest): Promise<google.cloud.chronicle.v1.Feed>;

Calls DisableFeed.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDisableFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.idisablefeedrequest)`   
DisableFeedRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.Feed](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feed-class)>` | Promise  
  
### enableFeed(request, callback)
    
    
    public enableFeed(request: google.cloud.chronicle.v1.IEnableFeedRequest, callback: google.cloud.chronicle.v1.FeedsService.EnableFeedCallback): void;

Calls EnableFeed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ienablefeedrequest)`   
EnableFeedRequest message or plain object  
`callback` |  `[EnableFeedCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Feed  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enableFeed(request)
    
    
    public enableFeed(request: google.cloud.chronicle.v1.IEnableFeedRequest): Promise<google.cloud.chronicle.v1.Feed>;

Calls EnableFeed.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEnableFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ienablefeedrequest)`   
EnableFeedRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.Feed](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feed-class)>` | Promise  
  
### fetchServiceAccountForCustomer(request, callback)
    
    
    public fetchServiceAccountForCustomer(request: google.cloud.chronicle.v1.IFetchServiceAccountForCustomerRequest, callback: google.cloud.chronicle.v1.FeedsService.FetchServiceAccountForCustomerCallback): void;

Calls FetchServiceAccountForCustomer.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchServiceAccountForCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifetchserviceaccountforcustomerrequest)`   
FetchServiceAccountForCustomerRequest message or plain object  
`callback` |  `[FetchServiceAccountForCustomerCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and FeedServiceAccount  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchServiceAccountForCustomer(request)
    
    
    public fetchServiceAccountForCustomer(request: google.cloud.chronicle.v1.IFetchServiceAccountForCustomerRequest): Promise<google.cloud.chronicle.v1.FeedServiceAccount>;

Calls FetchServiceAccountForCustomer.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchServiceAccountForCustomerRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ifetchserviceaccountforcustomerrequest)`   
FetchServiceAccountForCustomerRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.FeedServiceAccount](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feedserviceaccount)>` | Promise  
  
### generateSecret(request, callback)
    
    
    public generateSecret(request: google.cloud.chronicle.v1.IGenerateSecretRequest, callback: google.cloud.chronicle.v1.FeedsService.GenerateSecretCallback): void;

Calls GenerateSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igeneratesecretrequest)`   
GenerateSecretRequest message or plain object  
`callback` |  `[GenerateSecretCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateSecretResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateSecret(request)
    
    
    public generateSecret(request: google.cloud.chronicle.v1.IGenerateSecretRequest): Promise<google.cloud.chronicle.v1.GenerateSecretResponse>;

Calls GenerateSecret.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igeneratesecretrequest)`   
GenerateSecretRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.GenerateSecretResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.generatesecretresponse)>` | Promise  
  
### getFeed(request, callback)
    
    
    public getFeed(request: google.cloud.chronicle.v1.IGetFeedRequest, callback: google.cloud.chronicle.v1.FeedsService.GetFeedCallback): void;

Calls GetFeed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetfeedrequest)`   
GetFeedRequest message or plain object  
`callback` |  `[GetFeedCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Feed  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeed(request)
    
    
    public getFeed(request: google.cloud.chronicle.v1.IGetFeedRequest): Promise<google.cloud.chronicle.v1.Feed>;

Calls GetFeed.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetfeedrequest)`   
GetFeedRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.Feed](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feed-class)>` | Promise  
  
### getFeedPack(request, callback)
    
    
    public getFeedPack(request: google.cloud.chronicle.v1.IGetFeedPackRequest, callback: google.cloud.chronicle.v1.FeedsService.GetFeedPackCallback): void;

Calls GetFeedPack.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFeedPackRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetfeedpackrequest)`   
GetFeedPackRequest message or plain object  
`callback` |  `[GetFeedPackCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and FeedPack  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFeedPack(request)
    
    
    public getFeedPack(request: google.cloud.chronicle.v1.IGetFeedPackRequest): Promise<google.cloud.chronicle.v1.FeedPack>;

Calls GetFeedPack.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFeedPackRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetfeedpackrequest)`   
GetFeedPackRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.FeedPack](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feedpack-class)>` | Promise  
  
### importPushLogs(request, callback)
    
    
    public importPushLogs(request: google.cloud.chronicle.v1.IImportPushLogsRequest, callback: google.cloud.chronicle.v1.FeedsService.ImportPushLogsCallback): void;

Calls ImportPushLogs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IImportPushLogsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iimportpushlogsrequest)`   
ImportPushLogsRequest message or plain object  
`callback` |  `[ImportPushLogsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and HttpBody  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### importPushLogs(request)
    
    
    public importPushLogs(request: google.cloud.chronicle.v1.IImportPushLogsRequest): Promise<google.api.HttpBody>;

Calls ImportPushLogs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IImportPushLogsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iimportpushlogsrequest)`   
ImportPushLogsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.HttpBody](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.api.httpbody)>` | Promise  
  
### listFeedPacks(request, callback)
    
    
    public listFeedPacks(request: google.cloud.chronicle.v1.IListFeedPacksRequest, callback: google.cloud.chronicle.v1.FeedsService.ListFeedPacksCallback): void;

Calls ListFeedPacks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeedPacksRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistfeedpacksrequest)`   
ListFeedPacksRequest message or plain object  
`callback` |  `[ListFeedPacksCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFeedPacksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeedPacks(request)
    
    
    public listFeedPacks(request: google.cloud.chronicle.v1.IListFeedPacksRequest): Promise<google.cloud.chronicle.v1.ListFeedPacksResponse>;

Calls ListFeedPacks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFeedPacksRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistfeedpacksrequest)`   
ListFeedPacksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListFeedPacksResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listfeedpacksresponse)>` | Promise  
  
### listFeeds(request, callback)
    
    
    public listFeeds(request: google.cloud.chronicle.v1.IListFeedsRequest, callback: google.cloud.chronicle.v1.FeedsService.ListFeedsCallback): void;

Calls ListFeeds.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeedsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistfeedsrequest)`   
ListFeedsRequest message or plain object  
`callback` |  `[ListFeedsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFeedsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeeds(request)
    
    
    public listFeeds(request: google.cloud.chronicle.v1.IListFeedsRequest): Promise<google.cloud.chronicle.v1.ListFeedsResponse>;

Calls ListFeeds.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFeedsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistfeedsrequest)`   
ListFeedsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListFeedsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listfeedsresponse)>` | Promise  
  
### listFeedSourceTypeSchemas(request, callback)
    
    
    public listFeedSourceTypeSchemas(request: google.cloud.chronicle.v1.IListFeedSourceTypeSchemasRequest, callback: google.cloud.chronicle.v1.FeedsService.ListFeedSourceTypeSchemasCallback): void;

Calls ListFeedSourceTypeSchemas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFeedSourceTypeSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistfeedsourcetypeschemasrequest)`   
ListFeedSourceTypeSchemasRequest message or plain object  
`callback` |  `[ListFeedSourceTypeSchemasCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFeedSourceTypeSchemasResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFeedSourceTypeSchemas(request)
    
    
    public listFeedSourceTypeSchemas(request: google.cloud.chronicle.v1.IListFeedSourceTypeSchemasRequest): Promise<google.cloud.chronicle.v1.ListFeedSourceTypeSchemasResponse>;

Calls ListFeedSourceTypeSchemas.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFeedSourceTypeSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistfeedsourcetypeschemasrequest)`   
ListFeedSourceTypeSchemasRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListFeedSourceTypeSchemasResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listfeedsourcetypeschemasresponse)>` | Promise  
  
### listLogTypeSchemas(request, callback)
    
    
    public listLogTypeSchemas(request: google.cloud.chronicle.v1.IListLogTypeSchemasRequest, callback: google.cloud.chronicle.v1.FeedsService.ListLogTypeSchemasCallback): void;

Calls ListLogTypeSchemas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListLogTypeSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistlogtypeschemasrequest)`   
ListLogTypeSchemasRequest message or plain object  
`callback` |  `[ListLogTypeSchemasCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListLogTypeSchemasResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listLogTypeSchemas(request)
    
    
    public listLogTypeSchemas(request: google.cloud.chronicle.v1.IListLogTypeSchemasRequest): Promise<google.cloud.chronicle.v1.ListLogTypeSchemasResponse>;

Calls ListLogTypeSchemas.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListLogTypeSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistlogtypeschemasrequest)`   
ListLogTypeSchemasRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListLogTypeSchemasResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listlogtypeschemasresponse)>` | Promise  
  
### updateFeed(request, callback)
    
    
    public updateFeed(request: google.cloud.chronicle.v1.IUpdateFeedRequest, callback: google.cloud.chronicle.v1.FeedsService.UpdateFeedCallback): void;

Calls UpdateFeed.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatefeedrequest)`   
UpdateFeedRequest message or plain object  
`callback` |  `[UpdateFeedCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Feed  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFeed(request)
    
    
    public updateFeed(request: google.cloud.chronicle.v1.IUpdateFeedRequest): Promise<google.cloud.chronicle.v1.Feed>;

Calls UpdateFeed.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFeedRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatefeedrequest)`   
UpdateFeedRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.Feed](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.feed-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
