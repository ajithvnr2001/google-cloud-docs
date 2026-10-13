---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.analyticsadminservice-class
title: Class protos.google.analytics.admin.v1alpha.AnalyticsAdminService (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:42:17.774084+00:00
---

# Class protos.google.analytics.admin.v1alpha.AnalyticsAdminService (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.analyticsadminservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.admin.v1alpha.AnalyticsAdminService (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Represents an AnalyticsAdminService

## Inheritance

$protobuf.rpc.Service > protos.google.analytics.admin.v1alpha.AnalyticsAdminService

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AnalyticsAdminService service.

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

### acknowledgeUserDataCollection(request, callback)
    
    
    public acknowledgeUserDataCollection(request: google.analytics.admin.v1alpha.IAcknowledgeUserDataCollectionRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.AcknowledgeUserDataCollectionCallback): void;

Calls AcknowledgeUserDataCollection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iacknowledgeuserdatacollectionrequest)`   
AcknowledgeUserDataCollectionRequest message or plain object  
`callback` |  `[AcknowledgeUserDataCollectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AcknowledgeUserDataCollectionResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### acknowledgeUserDataCollection(request)
    
    
    public acknowledgeUserDataCollection(request: google.analytics.admin.v1alpha.IAcknowledgeUserDataCollectionRequest): Promise<google.analytics.admin.v1alpha.AcknowledgeUserDataCollectionResponse>;

Calls AcknowledgeUserDataCollection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iacknowledgeuserdatacollectionrequest)`   
AcknowledgeUserDataCollectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.AcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.acknowledgeuserdatacollectionresponse)>` | Promise  
  
### approveDisplayVideo360AdvertiserLinkProposal(request, callback)
    
    
    public approveDisplayVideo360AdvertiserLinkProposal(request: google.analytics.admin.v1alpha.IApproveDisplayVideo360AdvertiserLinkProposalRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ApproveDisplayVideo360AdvertiserLinkProposalCallback): void;

Calls ApproveDisplayVideo360AdvertiserLinkProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IApproveDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iapprovedisplayvideo360advertiserlinkproposalrequest)`   
ApproveDisplayVideo360AdvertiserLinkProposalRequest message or plain object  
`callback` |  `[ApproveDisplayVideo360AdvertiserLinkProposalCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ApproveDisplayVideo360AdvertiserLinkProposalResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### approveDisplayVideo360AdvertiserLinkProposal(request)
    
    
    public approveDisplayVideo360AdvertiserLinkProposal(request: google.analytics.admin.v1alpha.IApproveDisplayVideo360AdvertiserLinkProposalRequest): Promise<google.analytics.admin.v1alpha.ApproveDisplayVideo360AdvertiserLinkProposalResponse>;

Calls ApproveDisplayVideo360AdvertiserLinkProposal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IApproveDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iapprovedisplayvideo360advertiserlinkproposalrequest)`   
ApproveDisplayVideo360AdvertiserLinkProposalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ApproveDisplayVideo360AdvertiserLinkProposalResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.approvedisplayvideo360advertiserlinkproposalresponse)>` | Promise  
  
### archiveAudience(request, callback)
    
    
    public archiveAudience(request: google.analytics.admin.v1alpha.IArchiveAudienceRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ArchiveAudienceCallback): void;

Calls ArchiveAudience.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveAudienceRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iarchiveaudiencerequest)`   
ArchiveAudienceRequest message or plain object  
`callback` |  `[ArchiveAudienceCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### archiveAudience(request)
    
    
    public archiveAudience(request: google.analytics.admin.v1alpha.IArchiveAudienceRequest): Promise<google.protobuf.Empty>;

Calls ArchiveAudience.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IArchiveAudienceRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iarchiveaudiencerequest)`   
ArchiveAudienceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### archiveCustomDimension(request, callback)
    
    
    public archiveCustomDimension(request: google.analytics.admin.v1alpha.IArchiveCustomDimensionRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ArchiveCustomDimensionCallback): void;

Calls ArchiveCustomDimension.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iarchivecustomdimensionrequest)`   
ArchiveCustomDimensionRequest message or plain object  
`callback` |  `[ArchiveCustomDimensionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### archiveCustomDimension(request)
    
    
    public archiveCustomDimension(request: google.analytics.admin.v1alpha.IArchiveCustomDimensionRequest): Promise<google.protobuf.Empty>;

Calls ArchiveCustomDimension.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iarchivecustomdimensionrequest)`   
ArchiveCustomDimensionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### archiveCustomMetric(request, callback)
    
    
    public archiveCustomMetric(request: google.analytics.admin.v1alpha.IArchiveCustomMetricRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ArchiveCustomMetricCallback): void;

Calls ArchiveCustomMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iarchivecustommetricrequest)`   
ArchiveCustomMetricRequest message or plain object  
`callback` |  `[ArchiveCustomMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### archiveCustomMetric(request)
    
    
    public archiveCustomMetric(request: google.analytics.admin.v1alpha.IArchiveCustomMetricRequest): Promise<google.protobuf.Empty>;

Calls ArchiveCustomMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iarchivecustommetricrequest)`   
ArchiveCustomMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### batchCreateAccessBindings(request, callback)
    
    
    public batchCreateAccessBindings(request: google.analytics.admin.v1alpha.IBatchCreateAccessBindingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.BatchCreateAccessBindingsCallback): void;

Calls BatchCreateAccessBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ibatchcreateaccessbindingsrequest)`   
BatchCreateAccessBindingsRequest message or plain object  
`callback` |  `[BatchCreateAccessBindingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateAccessBindingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateAccessBindings(request)
    
    
    public batchCreateAccessBindings(request: google.analytics.admin.v1alpha.IBatchCreateAccessBindingsRequest): Promise<google.analytics.admin.v1alpha.BatchCreateAccessBindingsResponse>;

Calls BatchCreateAccessBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ibatchcreateaccessbindingsrequest)`   
BatchCreateAccessBindingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.BatchCreateAccessBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.batchcreateaccessbindingsresponse)>` | Promise  
  
### batchDeleteAccessBindings(request, callback)
    
    
    public batchDeleteAccessBindings(request: google.analytics.admin.v1alpha.IBatchDeleteAccessBindingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.BatchDeleteAccessBindingsCallback): void;

Calls BatchDeleteAccessBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ibatchdeleteaccessbindingsrequest)`   
BatchDeleteAccessBindingsRequest message or plain object  
`callback` |  `[BatchDeleteAccessBindingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteAccessBindings(request)
    
    
    public batchDeleteAccessBindings(request: google.analytics.admin.v1alpha.IBatchDeleteAccessBindingsRequest): Promise<google.protobuf.Empty>;

Calls BatchDeleteAccessBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ibatchdeleteaccessbindingsrequest)`   
BatchDeleteAccessBindingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### batchGetAccessBindings(request, callback)
    
    
    public batchGetAccessBindings(request: google.analytics.admin.v1alpha.IBatchGetAccessBindingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.BatchGetAccessBindingsCallback): void;

Calls BatchGetAccessBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchGetAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ibatchgetaccessbindingsrequest)`   
BatchGetAccessBindingsRequest message or plain object  
`callback` |  `[BatchGetAccessBindingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchGetAccessBindingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchGetAccessBindings(request)
    
    
    public batchGetAccessBindings(request: google.analytics.admin.v1alpha.IBatchGetAccessBindingsRequest): Promise<google.analytics.admin.v1alpha.BatchGetAccessBindingsResponse>;

Calls BatchGetAccessBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchGetAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ibatchgetaccessbindingsrequest)`   
BatchGetAccessBindingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.BatchGetAccessBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.batchgetaccessbindingsresponse)>` | Promise  
  
### batchUpdateAccessBindings(request, callback)
    
    
    public batchUpdateAccessBindings(request: google.analytics.admin.v1alpha.IBatchUpdateAccessBindingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.BatchUpdateAccessBindingsCallback): void;

Calls BatchUpdateAccessBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ibatchupdateaccessbindingsrequest)`   
BatchUpdateAccessBindingsRequest message or plain object  
`callback` |  `[BatchUpdateAccessBindingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateAccessBindingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateAccessBindings(request)
    
    
    public batchUpdateAccessBindings(request: google.analytics.admin.v1alpha.IBatchUpdateAccessBindingsRequest): Promise<google.analytics.admin.v1alpha.BatchUpdateAccessBindingsResponse>;

Calls BatchUpdateAccessBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ibatchupdateaccessbindingsrequest)`   
BatchUpdateAccessBindingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.BatchUpdateAccessBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.batchupdateaccessbindingsresponse)>` | Promise  
  
### cancelDisplayVideo360AdvertiserLinkProposal(request, callback)
    
    
    public cancelDisplayVideo360AdvertiserLinkProposal(request: google.analytics.admin.v1alpha.ICancelDisplayVideo360AdvertiserLinkProposalRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CancelDisplayVideo360AdvertiserLinkProposalCallback): void;

Calls CancelDisplayVideo360AdvertiserLinkProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icanceldisplayvideo360advertiserlinkproposalrequest)`   
CancelDisplayVideo360AdvertiserLinkProposalRequest message or plain object  
`callback` |  `[CancelDisplayVideo360AdvertiserLinkProposalCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DisplayVideo360AdvertiserLinkProposal  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelDisplayVideo360AdvertiserLinkProposal(request)
    
    
    public cancelDisplayVideo360AdvertiserLinkProposal(request: google.analytics.admin.v1alpha.ICancelDisplayVideo360AdvertiserLinkProposalRequest): Promise<google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLinkProposal>;

Calls CancelDisplayVideo360AdvertiserLinkProposal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icanceldisplayvideo360advertiserlinkproposalrequest)`   
CancelDisplayVideo360AdvertiserLinkProposalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.displayvideo360advertiserlinkproposal)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AnalyticsAdminService;

Creates new AnalyticsAdminService service using the specified rpc implementation.

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
`[AnalyticsAdminService](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.analyticsadminservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAccessBinding(request, callback)
    
    
    public createAccessBinding(request: google.analytics.admin.v1alpha.ICreateAccessBindingRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateAccessBindingCallback): void;

Calls CreateAccessBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateaccessbindingrequest)`   
CreateAccessBindingRequest message or plain object  
`callback` |  `[CreateAccessBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AccessBinding  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAccessBinding(request)
    
    
    public createAccessBinding(request: google.analytics.admin.v1alpha.ICreateAccessBindingRequest): Promise<google.analytics.admin.v1alpha.AccessBinding>;

Calls CreateAccessBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateaccessbindingrequest)`   
CreateAccessBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.AccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.accessbinding)>` | Promise  
  
### createAdSenseLink(request, callback)
    
    
    public createAdSenseLink(request: google.analytics.admin.v1alpha.ICreateAdSenseLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateAdSenseLinkCallback): void;

Calls CreateAdSenseLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdSenseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateadsenselinkrequest)`   
CreateAdSenseLinkRequest message or plain object  
`callback` |  `[CreateAdSenseLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AdSenseLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAdSenseLink(request)
    
    
    public createAdSenseLink(request: google.analytics.admin.v1alpha.ICreateAdSenseLinkRequest): Promise<google.analytics.admin.v1alpha.AdSenseLink>;

Calls CreateAdSenseLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAdSenseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateadsenselinkrequest)`   
CreateAdSenseLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.AdSenseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.adsenselink)>` | Promise  
  
### createAudience(request, callback)
    
    
    public createAudience(request: google.analytics.admin.v1alpha.ICreateAudienceRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateAudienceCallback): void;

Calls CreateAudience.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAudienceRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateaudiencerequest)`   
CreateAudienceRequest message or plain object  
`callback` |  `[CreateAudienceCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Audience  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAudience(request)
    
    
    public createAudience(request: google.analytics.admin.v1alpha.ICreateAudienceRequest): Promise<google.analytics.admin.v1alpha.Audience>;

Calls CreateAudience.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAudienceRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateaudiencerequest)`   
CreateAudienceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.Audience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audience-class)>` | Promise  
  
### createBigQueryLink(request, callback)
    
    
    public createBigQueryLink(request: google.analytics.admin.v1alpha.ICreateBigQueryLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateBigQueryLinkCallback): void;

Calls CreateBigQueryLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBigQueryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatebigquerylinkrequest)`   
CreateBigQueryLinkRequest message or plain object  
`callback` |  `[CreateBigQueryLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and BigQueryLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBigQueryLink(request)
    
    
    public createBigQueryLink(request: google.analytics.admin.v1alpha.ICreateBigQueryLinkRequest): Promise<google.analytics.admin.v1alpha.BigQueryLink>;

Calls CreateBigQueryLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateBigQueryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatebigquerylinkrequest)`   
CreateBigQueryLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.BigQueryLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.bigquerylink)>` | Promise  
  
### createCalculatedMetric(request, callback)
    
    
    public createCalculatedMetric(request: google.analytics.admin.v1alpha.ICreateCalculatedMetricRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateCalculatedMetricCallback): void;

Calls CreateCalculatedMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCalculatedMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatecalculatedmetricrequest)`   
CreateCalculatedMetricRequest message or plain object  
`callback` |  `[CreateCalculatedMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CalculatedMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCalculatedMetric(request)
    
    
    public createCalculatedMetric(request: google.analytics.admin.v1alpha.ICreateCalculatedMetricRequest): Promise<google.analytics.admin.v1alpha.CalculatedMetric>;

Calls CreateCalculatedMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCalculatedMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatecalculatedmetricrequest)`   
CreateCalculatedMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.CalculatedMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.calculatedmetric-class)>` | Promise  
  
### createChannelGroup(request, callback)
    
    
    public createChannelGroup(request: google.analytics.admin.v1alpha.ICreateChannelGroupRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateChannelGroupCallback): void;

Calls CreateChannelGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatechannelgrouprequest)`   
CreateChannelGroupRequest message or plain object  
`callback` |  `[CreateChannelGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ChannelGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createChannelGroup(request)
    
    
    public createChannelGroup(request: google.analytics.admin.v1alpha.ICreateChannelGroupRequest): Promise<google.analytics.admin.v1alpha.ChannelGroup>;

Calls CreateChannelGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateChannelGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatechannelgrouprequest)`   
CreateChannelGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ChannelGroup](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.channelgroup)>` | Promise  
  
### createConversionEvent(request, callback)
    
    
    public createConversionEvent(request: google.analytics.admin.v1alpha.ICreateConversionEventRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateConversionEventCallback): void;

Calls CreateConversionEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateconversioneventrequest)`   
CreateConversionEventRequest message or plain object  
`callback` |  `[CreateConversionEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversionEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversionEvent(request)
    
    
    public createConversionEvent(request: google.analytics.admin.v1alpha.ICreateConversionEventRequest): Promise<google.analytics.admin.v1alpha.ConversionEvent>;

Calls CreateConversionEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateconversioneventrequest)`   
CreateConversionEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.conversionevent-class)>` | Promise  
  
### createCustomDimension(request, callback)
    
    
    public createCustomDimension(request: google.analytics.admin.v1alpha.ICreateCustomDimensionRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateCustomDimensionCallback): void;

Calls CreateCustomDimension.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatecustomdimensionrequest)`   
CreateCustomDimensionRequest message or plain object  
`callback` |  `[CreateCustomDimensionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomDimension  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomDimension(request)
    
    
    public createCustomDimension(request: google.analytics.admin.v1alpha.ICreateCustomDimensionRequest): Promise<google.analytics.admin.v1alpha.CustomDimension>;

Calls CreateCustomDimension.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatecustomdimensionrequest)`   
CreateCustomDimensionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.CustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.customdimension-class)>` | Promise  
  
### createCustomMetric(request, callback)
    
    
    public createCustomMetric(request: google.analytics.admin.v1alpha.ICreateCustomMetricRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateCustomMetricCallback): void;

Calls CreateCustomMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatecustommetricrequest)`   
CreateCustomMetricRequest message or plain object  
`callback` |  `[CreateCustomMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomMetric(request)
    
    
    public createCustomMetric(request: google.analytics.admin.v1alpha.ICreateCustomMetricRequest): Promise<google.analytics.admin.v1alpha.CustomMetric>;

Calls CreateCustomMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatecustommetricrequest)`   
CreateCustomMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.CustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.custommetric-class)>` | Promise  
  
### createDataStream(request, callback)
    
    
    public createDataStream(request: google.analytics.admin.v1alpha.ICreateDataStreamRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateDataStreamCallback): void;

Calls CreateDataStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedatastreamrequest)`   
CreateDataStreamRequest message or plain object  
`callback` |  `[CreateDataStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataStream  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataStream(request)
    
    
    public createDataStream(request: google.analytics.admin.v1alpha.ICreateDataStreamRequest): Promise<google.analytics.admin.v1alpha.DataStream>;

Calls CreateDataStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedatastreamrequest)`   
CreateDataStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.datastream-class)>` | Promise  
  
### createDisplayVideo360AdvertiserLink(request, callback)
    
    
    public createDisplayVideo360AdvertiserLink(request: google.analytics.admin.v1alpha.ICreateDisplayVideo360AdvertiserLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateDisplayVideo360AdvertiserLinkCallback): void;

Calls CreateDisplayVideo360AdvertiserLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedisplayvideo360advertiserlinkrequest)`   
CreateDisplayVideo360AdvertiserLinkRequest message or plain object  
`callback` |  `[CreateDisplayVideo360AdvertiserLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DisplayVideo360AdvertiserLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDisplayVideo360AdvertiserLink(request)
    
    
    public createDisplayVideo360AdvertiserLink(request: google.analytics.admin.v1alpha.ICreateDisplayVideo360AdvertiserLinkRequest): Promise<google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLink>;

Calls CreateDisplayVideo360AdvertiserLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedisplayvideo360advertiserlinkrequest)`   
CreateDisplayVideo360AdvertiserLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.displayvideo360advertiserlink)>` | Promise  
  
### createDisplayVideo360AdvertiserLinkProposal(request, callback)
    
    
    public createDisplayVideo360AdvertiserLinkProposal(request: google.analytics.admin.v1alpha.ICreateDisplayVideo360AdvertiserLinkProposalRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateDisplayVideo360AdvertiserLinkProposalCallback): void;

Calls CreateDisplayVideo360AdvertiserLinkProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedisplayvideo360advertiserlinkproposalrequest)`   
CreateDisplayVideo360AdvertiserLinkProposalRequest message or plain object  
`callback` |  `[CreateDisplayVideo360AdvertiserLinkProposalCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DisplayVideo360AdvertiserLinkProposal  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDisplayVideo360AdvertiserLinkProposal(request)
    
    
    public createDisplayVideo360AdvertiserLinkProposal(request: google.analytics.admin.v1alpha.ICreateDisplayVideo360AdvertiserLinkProposalRequest): Promise<google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLinkProposal>;

Calls CreateDisplayVideo360AdvertiserLinkProposal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatedisplayvideo360advertiserlinkproposalrequest)`   
CreateDisplayVideo360AdvertiserLinkProposalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.displayvideo360advertiserlinkproposal)>` | Promise  
  
### createEventCreateRule(request, callback)
    
    
    public createEventCreateRule(request: google.analytics.admin.v1alpha.ICreateEventCreateRuleRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateEventCreateRuleCallback): void;

Calls CreateEventCreateRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEventCreateRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateeventcreaterulerequest)`   
CreateEventCreateRuleRequest message or plain object  
`callback` |  `[CreateEventCreateRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and EventCreateRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEventCreateRule(request)
    
    
    public createEventCreateRule(request: google.analytics.admin.v1alpha.ICreateEventCreateRuleRequest): Promise<google.analytics.admin.v1alpha.EventCreateRule>;

Calls CreateEventCreateRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEventCreateRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateeventcreaterulerequest)`   
CreateEventCreateRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.EventCreateRule](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.eventcreaterule)>` | Promise  
  
### createEventEditRule(request, callback)
    
    
    public createEventEditRule(request: google.analytics.admin.v1alpha.ICreateEventEditRuleRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateEventEditRuleCallback): void;

Calls CreateEventEditRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEventEditRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateeventeditrulerequest)`   
CreateEventEditRuleRequest message or plain object  
`callback` |  `[CreateEventEditRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and EventEditRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEventEditRule(request)
    
    
    public createEventEditRule(request: google.analytics.admin.v1alpha.ICreateEventEditRuleRequest): Promise<google.analytics.admin.v1alpha.EventEditRule>;

Calls CreateEventEditRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEventEditRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateeventeditrulerequest)`   
CreateEventEditRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.EventEditRule](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.eventeditrule)>` | Promise  
  
### createExpandedDataSet(request, callback)
    
    
    public createExpandedDataSet(request: google.analytics.admin.v1alpha.ICreateExpandedDataSetRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateExpandedDataSetCallback): void;

Calls CreateExpandedDataSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateExpandedDataSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateexpandeddatasetrequest)`   
CreateExpandedDataSetRequest message or plain object  
`callback` |  `[CreateExpandedDataSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ExpandedDataSet  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createExpandedDataSet(request)
    
    
    public createExpandedDataSet(request: google.analytics.admin.v1alpha.ICreateExpandedDataSetRequest): Promise<google.analytics.admin.v1alpha.ExpandedDataSet>;

Calls CreateExpandedDataSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateExpandedDataSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateexpandeddatasetrequest)`   
CreateExpandedDataSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ExpandedDataSet](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.expandeddataset)>` | Promise  
  
### createFirebaseLink(request, callback)
    
    
    public createFirebaseLink(request: google.analytics.admin.v1alpha.ICreateFirebaseLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateFirebaseLinkCallback): void;

Calls CreateFirebaseLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatefirebaselinkrequest)`   
CreateFirebaseLinkRequest message or plain object  
`callback` |  `[CreateFirebaseLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and FirebaseLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFirebaseLink(request)
    
    
    public createFirebaseLink(request: google.analytics.admin.v1alpha.ICreateFirebaseLinkRequest): Promise<google.analytics.admin.v1alpha.FirebaseLink>;

Calls CreateFirebaseLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatefirebaselinkrequest)`   
CreateFirebaseLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.FirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.firebaselink)>` | Promise  
  
### createGoogleAdsLink(request, callback)
    
    
    public createGoogleAdsLink(request: google.analytics.admin.v1alpha.ICreateGoogleAdsLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateGoogleAdsLinkCallback): void;

Calls CreateGoogleAdsLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreategoogleadslinkrequest)`   
CreateGoogleAdsLinkRequest message or plain object  
`callback` |  `[CreateGoogleAdsLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and GoogleAdsLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGoogleAdsLink(request)
    
    
    public createGoogleAdsLink(request: google.analytics.admin.v1alpha.ICreateGoogleAdsLinkRequest): Promise<google.analytics.admin.v1alpha.GoogleAdsLink>;

Calls CreateGoogleAdsLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreategoogleadslinkrequest)`   
CreateGoogleAdsLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.GoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.googleadslink)>` | Promise  
  
### createKeyEvent(request, callback)
    
    
    public createKeyEvent(request: google.analytics.admin.v1alpha.ICreateKeyEventRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateKeyEventCallback): void;

Calls CreateKeyEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatekeyeventrequest)`   
CreateKeyEventRequest message or plain object  
`callback` |  `[CreateKeyEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and KeyEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createKeyEvent(request)
    
    
    public createKeyEvent(request: google.analytics.admin.v1alpha.ICreateKeyEventRequest): Promise<google.analytics.admin.v1alpha.KeyEvent>;

Calls CreateKeyEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatekeyeventrequest)`   
CreateKeyEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.KeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.keyevent-class)>` | Promise  
  
### createMeasurementProtocolSecret(request, callback)
    
    
    public createMeasurementProtocolSecret(request: google.analytics.admin.v1alpha.ICreateMeasurementProtocolSecretRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateMeasurementProtocolSecretCallback): void;

Calls CreateMeasurementProtocolSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatemeasurementprotocolsecretrequest)`   
CreateMeasurementProtocolSecretRequest message or plain object  
`callback` |  `[CreateMeasurementProtocolSecretCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and MeasurementProtocolSecret  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMeasurementProtocolSecret(request)
    
    
    public createMeasurementProtocolSecret(request: google.analytics.admin.v1alpha.ICreateMeasurementProtocolSecretRequest): Promise<google.analytics.admin.v1alpha.MeasurementProtocolSecret>;

Calls CreateMeasurementProtocolSecret.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatemeasurementprotocolsecretrequest)`   
CreateMeasurementProtocolSecretRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.measurementprotocolsecret)>` | Promise  
  
### createProperty(request, callback)
    
    
    public createProperty(request: google.analytics.admin.v1alpha.ICreatePropertyRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreatePropertyCallback): void;

Calls CreateProperty.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatepropertyrequest)`   
CreatePropertyRequest message or plain object  
`callback` |  `[CreatePropertyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Property  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProperty(request)
    
    
    public createProperty(request: google.analytics.admin.v1alpha.ICreatePropertyRequest): Promise<google.analytics.admin.v1alpha.Property>;

Calls CreateProperty.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatepropertyrequest)`   
CreatePropertyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.property)>` | Promise  
  
### createReportingDataAnnotation(request, callback)
    
    
    public createReportingDataAnnotation(request: google.analytics.admin.v1alpha.ICreateReportingDataAnnotationRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateReportingDataAnnotationCallback): void;

Calls CreateReportingDataAnnotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateReportingDataAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatereportingdataannotationrequest)`   
CreateReportingDataAnnotationRequest message or plain object  
`callback` |  `[CreateReportingDataAnnotationCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ReportingDataAnnotation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createReportingDataAnnotation(request)
    
    
    public createReportingDataAnnotation(request: google.analytics.admin.v1alpha.ICreateReportingDataAnnotationRequest): Promise<google.analytics.admin.v1alpha.ReportingDataAnnotation>;

Calls CreateReportingDataAnnotation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateReportingDataAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatereportingdataannotationrequest)`   
CreateReportingDataAnnotationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ReportingDataAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.reportingdataannotation-class)>` | Promise  
  
### createRollupProperty(request, callback)
    
    
    public createRollupProperty(request: google.analytics.admin.v1alpha.ICreateRollupPropertyRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateRollupPropertyCallback): void;

Calls CreateRollupProperty.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRollupPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreaterolluppropertyrequest)`   
CreateRollupPropertyRequest message or plain object  
`callback` |  `[CreateRollupPropertyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CreateRollupPropertyResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRollupProperty(request)
    
    
    public createRollupProperty(request: google.analytics.admin.v1alpha.ICreateRollupPropertyRequest): Promise<google.analytics.admin.v1alpha.CreateRollupPropertyResponse>;

Calls CreateRollupProperty.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateRollupPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreaterolluppropertyrequest)`   
CreateRollupPropertyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.CreateRollupPropertyResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.createrolluppropertyresponse)>` | Promise  
  
### createRollupPropertySourceLink(request, callback)
    
    
    public createRollupPropertySourceLink(request: google.analytics.admin.v1alpha.ICreateRollupPropertySourceLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateRollupPropertySourceLinkCallback): void;

Calls CreateRollupPropertySourceLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateRollupPropertySourceLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreaterolluppropertysourcelinkrequest)`   
CreateRollupPropertySourceLinkRequest message or plain object  
`callback` |  `[CreateRollupPropertySourceLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and RollupPropertySourceLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createRollupPropertySourceLink(request)
    
    
    public createRollupPropertySourceLink(request: google.analytics.admin.v1alpha.ICreateRollupPropertySourceLinkRequest): Promise<google.analytics.admin.v1alpha.RollupPropertySourceLink>;

Calls CreateRollupPropertySourceLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateRollupPropertySourceLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreaterolluppropertysourcelinkrequest)`   
CreateRollupPropertySourceLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.RollupPropertySourceLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.rolluppropertysourcelink)>` | Promise  
  
### createSearchAds360Link(request, callback)
    
    
    public createSearchAds360Link(request: google.analytics.admin.v1alpha.ICreateSearchAds360LinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateSearchAds360LinkCallback): void;

Calls CreateSearchAds360Link.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSearchAds360LinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatesearchads360linkrequest)`   
CreateSearchAds360LinkRequest message or plain object  
`callback` |  `[CreateSearchAds360LinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchAds360Link  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSearchAds360Link(request)
    
    
    public createSearchAds360Link(request: google.analytics.admin.v1alpha.ICreateSearchAds360LinkRequest): Promise<google.analytics.admin.v1alpha.SearchAds360Link>;

Calls CreateSearchAds360Link.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSearchAds360LinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatesearchads360linkrequest)`   
CreateSearchAds360LinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SearchAds360Link](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.searchads360link)>` | Promise  
  
### createSKAdNetworkConversionValueSchema(request, callback)
    
    
    public createSKAdNetworkConversionValueSchema(request: google.analytics.admin.v1alpha.ICreateSKAdNetworkConversionValueSchemaRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateSKAdNetworkConversionValueSchemaCallback): void;

Calls CreateSKAdNetworkConversionValueSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateskadnetworkconversionvalueschemarequest)`   
CreateSKAdNetworkConversionValueSchemaRequest message or plain object  
`callback` |  `[CreateSKAdNetworkConversionValueSchemaCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SKAdNetworkConversionValueSchema  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSKAdNetworkConversionValueSchema(request)
    
    
    public createSKAdNetworkConversionValueSchema(request: google.analytics.admin.v1alpha.ICreateSKAdNetworkConversionValueSchemaRequest): Promise<google.analytics.admin.v1alpha.SKAdNetworkConversionValueSchema>;

Calls CreateSKAdNetworkConversionValueSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreateskadnetworkconversionvalueschemarequest)`   
CreateSKAdNetworkConversionValueSchemaRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.skadnetworkconversionvalueschema)>` | Promise  
  
### createSubpropertyEventFilter(request, callback)
    
    
    public createSubpropertyEventFilter(request: google.analytics.admin.v1alpha.ICreateSubpropertyEventFilterRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.CreateSubpropertyEventFilterCallback): void;

Calls CreateSubpropertyEventFilter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSubpropertyEventFilterRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatesubpropertyeventfilterrequest)`   
CreateSubpropertyEventFilterRequest message or plain object  
`callback` |  `[CreateSubpropertyEventFilterCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SubpropertyEventFilter  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSubpropertyEventFilter(request)
    
    
    public createSubpropertyEventFilter(request: google.analytics.admin.v1alpha.ICreateSubpropertyEventFilterRequest): Promise<google.analytics.admin.v1alpha.SubpropertyEventFilter>;

Calls CreateSubpropertyEventFilter.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSubpropertyEventFilterRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.icreatesubpropertyeventfilterrequest)`   
CreateSubpropertyEventFilterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SubpropertyEventFilter](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.subpropertyeventfilter)>` | Promise  
  
### deleteAccessBinding(request, callback)
    
    
    public deleteAccessBinding(request: google.analytics.admin.v1alpha.IDeleteAccessBindingRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteAccessBindingCallback): void;

Calls DeleteAccessBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteaccessbindingrequest)`   
DeleteAccessBindingRequest message or plain object  
`callback` |  `[DeleteAccessBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAccessBinding(request)
    
    
    public deleteAccessBinding(request: google.analytics.admin.v1alpha.IDeleteAccessBindingRequest): Promise<google.protobuf.Empty>;

Calls DeleteAccessBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteaccessbindingrequest)`   
DeleteAccessBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteAccount(request, callback)
    
    
    public deleteAccount(request: google.analytics.admin.v1alpha.IDeleteAccountRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteAccountCallback): void;

Calls DeleteAccount.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteaccountrequest)`   
DeleteAccountRequest message or plain object  
`callback` |  `[DeleteAccountCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAccount(request)
    
    
    public deleteAccount(request: google.analytics.admin.v1alpha.IDeleteAccountRequest): Promise<google.protobuf.Empty>;

Calls DeleteAccount.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteaccountrequest)`   
DeleteAccountRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteAdSenseLink(request, callback)
    
    
    public deleteAdSenseLink(request: google.analytics.admin.v1alpha.IDeleteAdSenseLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteAdSenseLinkCallback): void;

Calls DeleteAdSenseLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAdSenseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteadsenselinkrequest)`   
DeleteAdSenseLinkRequest message or plain object  
`callback` |  `[DeleteAdSenseLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAdSenseLink(request)
    
    
    public deleteAdSenseLink(request: google.analytics.admin.v1alpha.IDeleteAdSenseLinkRequest): Promise<google.protobuf.Empty>;

Calls DeleteAdSenseLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAdSenseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteadsenselinkrequest)`   
DeleteAdSenseLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteBigQueryLink(request, callback)
    
    
    public deleteBigQueryLink(request: google.analytics.admin.v1alpha.IDeleteBigQueryLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteBigQueryLinkCallback): void;

Calls DeleteBigQueryLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBigQueryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletebigquerylinkrequest)`   
DeleteBigQueryLinkRequest message or plain object  
`callback` |  `[DeleteBigQueryLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBigQueryLink(request)
    
    
    public deleteBigQueryLink(request: google.analytics.admin.v1alpha.IDeleteBigQueryLinkRequest): Promise<google.protobuf.Empty>;

Calls DeleteBigQueryLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBigQueryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletebigquerylinkrequest)`   
DeleteBigQueryLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteCalculatedMetric(request, callback)
    
    
    public deleteCalculatedMetric(request: google.analytics.admin.v1alpha.IDeleteCalculatedMetricRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteCalculatedMetricCallback): void;

Calls DeleteCalculatedMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCalculatedMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletecalculatedmetricrequest)`   
DeleteCalculatedMetricRequest message or plain object  
`callback` |  `[DeleteCalculatedMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteCalculatedMetric(request)
    
    
    public deleteCalculatedMetric(request: google.analytics.admin.v1alpha.IDeleteCalculatedMetricRequest): Promise<google.protobuf.Empty>;

Calls DeleteCalculatedMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteCalculatedMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletecalculatedmetricrequest)`   
DeleteCalculatedMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteChannelGroup(request, callback)
    
    
    public deleteChannelGroup(request: google.analytics.admin.v1alpha.IDeleteChannelGroupRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteChannelGroupCallback): void;

Calls DeleteChannelGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChannelGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletechannelgrouprequest)`   
DeleteChannelGroupRequest message or plain object  
`callback` |  `[DeleteChannelGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteChannelGroup(request)
    
    
    public deleteChannelGroup(request: google.analytics.admin.v1alpha.IDeleteChannelGroupRequest): Promise<google.protobuf.Empty>;

Calls DeleteChannelGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteChannelGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletechannelgrouprequest)`   
DeleteChannelGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteConversionEvent(request, callback)
    
    
    public deleteConversionEvent(request: google.analytics.admin.v1alpha.IDeleteConversionEventRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteConversionEventCallback): void;

Calls DeleteConversionEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteconversioneventrequest)`   
DeleteConversionEventRequest message or plain object  
`callback` |  `[DeleteConversionEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversionEvent(request)
    
    
    public deleteConversionEvent(request: google.analytics.admin.v1alpha.IDeleteConversionEventRequest): Promise<google.protobuf.Empty>;

Calls DeleteConversionEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteconversioneventrequest)`   
DeleteConversionEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteDataStream(request, callback)
    
    
    public deleteDataStream(request: google.analytics.admin.v1alpha.IDeleteDataStreamRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteDataStreamCallback): void;

Calls DeleteDataStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletedatastreamrequest)`   
DeleteDataStreamRequest message or plain object  
`callback` |  `[DeleteDataStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataStream(request)
    
    
    public deleteDataStream(request: google.analytics.admin.v1alpha.IDeleteDataStreamRequest): Promise<google.protobuf.Empty>;

Calls DeleteDataStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletedatastreamrequest)`   
DeleteDataStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteDisplayVideo360AdvertiserLink(request, callback)
    
    
    public deleteDisplayVideo360AdvertiserLink(request: google.analytics.admin.v1alpha.IDeleteDisplayVideo360AdvertiserLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteDisplayVideo360AdvertiserLinkCallback): void;

Calls DeleteDisplayVideo360AdvertiserLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletedisplayvideo360advertiserlinkrequest)`   
DeleteDisplayVideo360AdvertiserLinkRequest message or plain object  
`callback` |  `[DeleteDisplayVideo360AdvertiserLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDisplayVideo360AdvertiserLink(request)
    
    
    public deleteDisplayVideo360AdvertiserLink(request: google.analytics.admin.v1alpha.IDeleteDisplayVideo360AdvertiserLinkRequest): Promise<google.protobuf.Empty>;

Calls DeleteDisplayVideo360AdvertiserLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletedisplayvideo360advertiserlinkrequest)`   
DeleteDisplayVideo360AdvertiserLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteDisplayVideo360AdvertiserLinkProposal(request, callback)
    
    
    public deleteDisplayVideo360AdvertiserLinkProposal(request: google.analytics.admin.v1alpha.IDeleteDisplayVideo360AdvertiserLinkProposalRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteDisplayVideo360AdvertiserLinkProposalCallback): void;

Calls DeleteDisplayVideo360AdvertiserLinkProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletedisplayvideo360advertiserlinkproposalrequest)`   
DeleteDisplayVideo360AdvertiserLinkProposalRequest message or plain object  
`callback` |  `[DeleteDisplayVideo360AdvertiserLinkProposalCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDisplayVideo360AdvertiserLinkProposal(request)
    
    
    public deleteDisplayVideo360AdvertiserLinkProposal(request: google.analytics.admin.v1alpha.IDeleteDisplayVideo360AdvertiserLinkProposalRequest): Promise<google.protobuf.Empty>;

Calls DeleteDisplayVideo360AdvertiserLinkProposal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletedisplayvideo360advertiserlinkproposalrequest)`   
DeleteDisplayVideo360AdvertiserLinkProposalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteEventCreateRule(request, callback)
    
    
    public deleteEventCreateRule(request: google.analytics.admin.v1alpha.IDeleteEventCreateRuleRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteEventCreateRuleCallback): void;

Calls DeleteEventCreateRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEventCreateRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteeventcreaterulerequest)`   
DeleteEventCreateRuleRequest message or plain object  
`callback` |  `[DeleteEventCreateRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEventCreateRule(request)
    
    
    public deleteEventCreateRule(request: google.analytics.admin.v1alpha.IDeleteEventCreateRuleRequest): Promise<google.protobuf.Empty>;

Calls DeleteEventCreateRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEventCreateRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteeventcreaterulerequest)`   
DeleteEventCreateRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteEventEditRule(request, callback)
    
    
    public deleteEventEditRule(request: google.analytics.admin.v1alpha.IDeleteEventEditRuleRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteEventEditRuleCallback): void;

Calls DeleteEventEditRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEventEditRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteeventeditrulerequest)`   
DeleteEventEditRuleRequest message or plain object  
`callback` |  `[DeleteEventEditRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEventEditRule(request)
    
    
    public deleteEventEditRule(request: google.analytics.admin.v1alpha.IDeleteEventEditRuleRequest): Promise<google.protobuf.Empty>;

Calls DeleteEventEditRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEventEditRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteeventeditrulerequest)`   
DeleteEventEditRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteExpandedDataSet(request, callback)
    
    
    public deleteExpandedDataSet(request: google.analytics.admin.v1alpha.IDeleteExpandedDataSetRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteExpandedDataSetCallback): void;

Calls DeleteExpandedDataSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteExpandedDataSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteexpandeddatasetrequest)`   
DeleteExpandedDataSetRequest message or plain object  
`callback` |  `[DeleteExpandedDataSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteExpandedDataSet(request)
    
    
    public deleteExpandedDataSet(request: google.analytics.admin.v1alpha.IDeleteExpandedDataSetRequest): Promise<google.protobuf.Empty>;

Calls DeleteExpandedDataSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteExpandedDataSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteexpandeddatasetrequest)`   
DeleteExpandedDataSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteFirebaseLink(request, callback)
    
    
    public deleteFirebaseLink(request: google.analytics.admin.v1alpha.IDeleteFirebaseLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteFirebaseLinkCallback): void;

Calls DeleteFirebaseLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletefirebaselinkrequest)`   
DeleteFirebaseLinkRequest message or plain object  
`callback` |  `[DeleteFirebaseLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFirebaseLink(request)
    
    
    public deleteFirebaseLink(request: google.analytics.admin.v1alpha.IDeleteFirebaseLinkRequest): Promise<google.protobuf.Empty>;

Calls DeleteFirebaseLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletefirebaselinkrequest)`   
DeleteFirebaseLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteGoogleAdsLink(request, callback)
    
    
    public deleteGoogleAdsLink(request: google.analytics.admin.v1alpha.IDeleteGoogleAdsLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteGoogleAdsLinkCallback): void;

Calls DeleteGoogleAdsLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletegoogleadslinkrequest)`   
DeleteGoogleAdsLinkRequest message or plain object  
`callback` |  `[DeleteGoogleAdsLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGoogleAdsLink(request)
    
    
    public deleteGoogleAdsLink(request: google.analytics.admin.v1alpha.IDeleteGoogleAdsLinkRequest): Promise<google.protobuf.Empty>;

Calls DeleteGoogleAdsLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletegoogleadslinkrequest)`   
DeleteGoogleAdsLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteKeyEvent(request, callback)
    
    
    public deleteKeyEvent(request: google.analytics.admin.v1alpha.IDeleteKeyEventRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteKeyEventCallback): void;

Calls DeleteKeyEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletekeyeventrequest)`   
DeleteKeyEventRequest message or plain object  
`callback` |  `[DeleteKeyEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteKeyEvent(request)
    
    
    public deleteKeyEvent(request: google.analytics.admin.v1alpha.IDeleteKeyEventRequest): Promise<google.protobuf.Empty>;

Calls DeleteKeyEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletekeyeventrequest)`   
DeleteKeyEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteMeasurementProtocolSecret(request, callback)
    
    
    public deleteMeasurementProtocolSecret(request: google.analytics.admin.v1alpha.IDeleteMeasurementProtocolSecretRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteMeasurementProtocolSecretCallback): void;

Calls DeleteMeasurementProtocolSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletemeasurementprotocolsecretrequest)`   
DeleteMeasurementProtocolSecretRequest message or plain object  
`callback` |  `[DeleteMeasurementProtocolSecretCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMeasurementProtocolSecret(request)
    
    
    public deleteMeasurementProtocolSecret(request: google.analytics.admin.v1alpha.IDeleteMeasurementProtocolSecretRequest): Promise<google.protobuf.Empty>;

Calls DeleteMeasurementProtocolSecret.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletemeasurementprotocolsecretrequest)`   
DeleteMeasurementProtocolSecretRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteProperty(request, callback)
    
    
    public deleteProperty(request: google.analytics.admin.v1alpha.IDeletePropertyRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeletePropertyCallback): void;

Calls DeleteProperty.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletepropertyrequest)`   
DeletePropertyRequest message or plain object  
`callback` |  `[DeletePropertyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Property  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProperty(request)
    
    
    public deleteProperty(request: google.analytics.admin.v1alpha.IDeletePropertyRequest): Promise<google.analytics.admin.v1alpha.Property>;

Calls DeleteProperty.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletepropertyrequest)`   
DeletePropertyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.property)>` | Promise  
  
### deleteReportingDataAnnotation(request, callback)
    
    
    public deleteReportingDataAnnotation(request: google.analytics.admin.v1alpha.IDeleteReportingDataAnnotationRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteReportingDataAnnotationCallback): void;

Calls DeleteReportingDataAnnotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReportingDataAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletereportingdataannotationrequest)`   
DeleteReportingDataAnnotationRequest message or plain object  
`callback` |  `[DeleteReportingDataAnnotationCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteReportingDataAnnotation(request)
    
    
    public deleteReportingDataAnnotation(request: google.analytics.admin.v1alpha.IDeleteReportingDataAnnotationRequest): Promise<google.protobuf.Empty>;

Calls DeleteReportingDataAnnotation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReportingDataAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletereportingdataannotationrequest)`   
DeleteReportingDataAnnotationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteRollupPropertySourceLink(request, callback)
    
    
    public deleteRollupPropertySourceLink(request: google.analytics.admin.v1alpha.IDeleteRollupPropertySourceLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteRollupPropertySourceLinkCallback): void;

Calls DeleteRollupPropertySourceLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRollupPropertySourceLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleterolluppropertysourcelinkrequest)`   
DeleteRollupPropertySourceLinkRequest message or plain object  
`callback` |  `[DeleteRollupPropertySourceLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteRollupPropertySourceLink(request)
    
    
    public deleteRollupPropertySourceLink(request: google.analytics.admin.v1alpha.IDeleteRollupPropertySourceLinkRequest): Promise<google.protobuf.Empty>;

Calls DeleteRollupPropertySourceLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRollupPropertySourceLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleterolluppropertysourcelinkrequest)`   
DeleteRollupPropertySourceLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteSearchAds360Link(request, callback)
    
    
    public deleteSearchAds360Link(request: google.analytics.admin.v1alpha.IDeleteSearchAds360LinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteSearchAds360LinkCallback): void;

Calls DeleteSearchAds360Link.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSearchAds360LinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletesearchads360linkrequest)`   
DeleteSearchAds360LinkRequest message or plain object  
`callback` |  `[DeleteSearchAds360LinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSearchAds360Link(request)
    
    
    public deleteSearchAds360Link(request: google.analytics.admin.v1alpha.IDeleteSearchAds360LinkRequest): Promise<google.protobuf.Empty>;

Calls DeleteSearchAds360Link.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSearchAds360LinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletesearchads360linkrequest)`   
DeleteSearchAds360LinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteSKAdNetworkConversionValueSchema(request, callback)
    
    
    public deleteSKAdNetworkConversionValueSchema(request: google.analytics.admin.v1alpha.IDeleteSKAdNetworkConversionValueSchemaRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteSKAdNetworkConversionValueSchemaCallback): void;

Calls DeleteSKAdNetworkConversionValueSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteskadnetworkconversionvalueschemarequest)`   
DeleteSKAdNetworkConversionValueSchemaRequest message or plain object  
`callback` |  `[DeleteSKAdNetworkConversionValueSchemaCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSKAdNetworkConversionValueSchema(request)
    
    
    public deleteSKAdNetworkConversionValueSchema(request: google.analytics.admin.v1alpha.IDeleteSKAdNetworkConversionValueSchemaRequest): Promise<google.protobuf.Empty>;

Calls DeleteSKAdNetworkConversionValueSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideleteskadnetworkconversionvalueschemarequest)`   
DeleteSKAdNetworkConversionValueSchemaRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteSubpropertyEventFilter(request, callback)
    
    
    public deleteSubpropertyEventFilter(request: google.analytics.admin.v1alpha.IDeleteSubpropertyEventFilterRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.DeleteSubpropertyEventFilterCallback): void;

Calls DeleteSubpropertyEventFilter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubpropertyEventFilterRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletesubpropertyeventfilterrequest)`   
DeleteSubpropertyEventFilterRequest message or plain object  
`callback` |  `[DeleteSubpropertyEventFilterCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSubpropertyEventFilter(request)
    
    
    public deleteSubpropertyEventFilter(request: google.analytics.admin.v1alpha.IDeleteSubpropertyEventFilterRequest): Promise<google.protobuf.Empty>;

Calls DeleteSubpropertyEventFilter.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubpropertyEventFilterRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ideletesubpropertyeventfilterrequest)`   
DeleteSubpropertyEventFilterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### getAccessBinding(request, callback)
    
    
    public getAccessBinding(request: google.analytics.admin.v1alpha.IGetAccessBindingRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetAccessBindingCallback): void;

Calls GetAccessBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetaccessbindingrequest)`   
GetAccessBindingRequest message or plain object  
`callback` |  `[GetAccessBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AccessBinding  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAccessBinding(request)
    
    
    public getAccessBinding(request: google.analytics.admin.v1alpha.IGetAccessBindingRequest): Promise<google.analytics.admin.v1alpha.AccessBinding>;

Calls GetAccessBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetaccessbindingrequest)`   
GetAccessBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.AccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.accessbinding)>` | Promise  
  
### getAccount(request, callback)
    
    
    public getAccount(request: google.analytics.admin.v1alpha.IGetAccountRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetAccountCallback): void;

Calls GetAccount.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetaccountrequest)`   
GetAccountRequest message or plain object  
`callback` |  `[GetAccountCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Account  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAccount(request)
    
    
    public getAccount(request: google.analytics.admin.v1alpha.IGetAccountRequest): Promise<google.analytics.admin.v1alpha.Account>;

Calls GetAccount.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetaccountrequest)`   
GetAccountRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.Account](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.account)>` | Promise  
  
### getAdSenseLink(request, callback)
    
    
    public getAdSenseLink(request: google.analytics.admin.v1alpha.IGetAdSenseLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetAdSenseLinkCallback): void;

Calls GetAdSenseLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAdSenseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetadsenselinkrequest)`   
GetAdSenseLinkRequest message or plain object  
`callback` |  `[GetAdSenseLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AdSenseLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAdSenseLink(request)
    
    
    public getAdSenseLink(request: google.analytics.admin.v1alpha.IGetAdSenseLinkRequest): Promise<google.analytics.admin.v1alpha.AdSenseLink>;

Calls GetAdSenseLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAdSenseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetadsenselinkrequest)`   
GetAdSenseLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.AdSenseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.adsenselink)>` | Promise  
  
### getAttributionSettings(request, callback)
    
    
    public getAttributionSettings(request: google.analytics.admin.v1alpha.IGetAttributionSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetAttributionSettingsCallback): void;

Calls GetAttributionSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAttributionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetattributionsettingsrequest)`   
GetAttributionSettingsRequest message or plain object  
`callback` |  `[GetAttributionSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AttributionSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAttributionSettings(request)
    
    
    public getAttributionSettings(request: google.analytics.admin.v1alpha.IGetAttributionSettingsRequest): Promise<google.analytics.admin.v1alpha.AttributionSettings>;

Calls GetAttributionSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAttributionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetattributionsettingsrequest)`   
GetAttributionSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.AttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.attributionsettings-class)>` | Promise  
  
### getAudience(request, callback)
    
    
    public getAudience(request: google.analytics.admin.v1alpha.IGetAudienceRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetAudienceCallback): void;

Calls GetAudience.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAudienceRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetaudiencerequest)`   
GetAudienceRequest message or plain object  
`callback` |  `[GetAudienceCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Audience  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAudience(request)
    
    
    public getAudience(request: google.analytics.admin.v1alpha.IGetAudienceRequest): Promise<google.analytics.admin.v1alpha.Audience>;

Calls GetAudience.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAudienceRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetaudiencerequest)`   
GetAudienceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.Audience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audience-class)>` | Promise  
  
### getBigQueryLink(request, callback)
    
    
    public getBigQueryLink(request: google.analytics.admin.v1alpha.IGetBigQueryLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetBigQueryLinkCallback): void;

Calls GetBigQueryLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBigQueryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetbigquerylinkrequest)`   
GetBigQueryLinkRequest message or plain object  
`callback` |  `[GetBigQueryLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and BigQueryLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBigQueryLink(request)
    
    
    public getBigQueryLink(request: google.analytics.admin.v1alpha.IGetBigQueryLinkRequest): Promise<google.analytics.admin.v1alpha.BigQueryLink>;

Calls GetBigQueryLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBigQueryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetbigquerylinkrequest)`   
GetBigQueryLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.BigQueryLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.bigquerylink)>` | Promise  
  
### getCalculatedMetric(request, callback)
    
    
    public getCalculatedMetric(request: google.analytics.admin.v1alpha.IGetCalculatedMetricRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetCalculatedMetricCallback): void;

Calls GetCalculatedMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCalculatedMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetcalculatedmetricrequest)`   
GetCalculatedMetricRequest message or plain object  
`callback` |  `[GetCalculatedMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CalculatedMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCalculatedMetric(request)
    
    
    public getCalculatedMetric(request: google.analytics.admin.v1alpha.IGetCalculatedMetricRequest): Promise<google.analytics.admin.v1alpha.CalculatedMetric>;

Calls GetCalculatedMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCalculatedMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetcalculatedmetricrequest)`   
GetCalculatedMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.CalculatedMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.calculatedmetric-class)>` | Promise  
  
### getChannelGroup(request, callback)
    
    
    public getChannelGroup(request: google.analytics.admin.v1alpha.IGetChannelGroupRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetChannelGroupCallback): void;

Calls GetChannelGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetchannelgrouprequest)`   
GetChannelGroupRequest message or plain object  
`callback` |  `[GetChannelGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ChannelGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getChannelGroup(request)
    
    
    public getChannelGroup(request: google.analytics.admin.v1alpha.IGetChannelGroupRequest): Promise<google.analytics.admin.v1alpha.ChannelGroup>;

Calls GetChannelGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetChannelGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetchannelgrouprequest)`   
GetChannelGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ChannelGroup](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.channelgroup)>` | Promise  
  
### getConversionEvent(request, callback)
    
    
    public getConversionEvent(request: google.analytics.admin.v1alpha.IGetConversionEventRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetConversionEventCallback): void;

Calls GetConversionEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetconversioneventrequest)`   
GetConversionEventRequest message or plain object  
`callback` |  `[GetConversionEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversionEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversionEvent(request)
    
    
    public getConversionEvent(request: google.analytics.admin.v1alpha.IGetConversionEventRequest): Promise<google.analytics.admin.v1alpha.ConversionEvent>;

Calls GetConversionEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetconversioneventrequest)`   
GetConversionEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.conversionevent-class)>` | Promise  
  
### getCustomDimension(request, callback)
    
    
    public getCustomDimension(request: google.analytics.admin.v1alpha.IGetCustomDimensionRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetCustomDimensionCallback): void;

Calls GetCustomDimension.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetcustomdimensionrequest)`   
GetCustomDimensionRequest message or plain object  
`callback` |  `[GetCustomDimensionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomDimension  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomDimension(request)
    
    
    public getCustomDimension(request: google.analytics.admin.v1alpha.IGetCustomDimensionRequest): Promise<google.analytics.admin.v1alpha.CustomDimension>;

Calls GetCustomDimension.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetcustomdimensionrequest)`   
GetCustomDimensionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.CustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.customdimension-class)>` | Promise  
  
### getCustomMetric(request, callback)
    
    
    public getCustomMetric(request: google.analytics.admin.v1alpha.IGetCustomMetricRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetCustomMetricCallback): void;

Calls GetCustomMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetcustommetricrequest)`   
GetCustomMetricRequest message or plain object  
`callback` |  `[GetCustomMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomMetric(request)
    
    
    public getCustomMetric(request: google.analytics.admin.v1alpha.IGetCustomMetricRequest): Promise<google.analytics.admin.v1alpha.CustomMetric>;

Calls GetCustomMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetcustommetricrequest)`   
GetCustomMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.CustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.custommetric-class)>` | Promise  
  
### getDataRedactionSettings(request, callback)
    
    
    public getDataRedactionSettings(request: google.analytics.admin.v1alpha.IGetDataRedactionSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetDataRedactionSettingsCallback): void;

Calls GetDataRedactionSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataRedactionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdataredactionsettingsrequest)`   
GetDataRedactionSettingsRequest message or plain object  
`callback` |  `[GetDataRedactionSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataRedactionSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataRedactionSettings(request)
    
    
    public getDataRedactionSettings(request: google.analytics.admin.v1alpha.IGetDataRedactionSettingsRequest): Promise<google.analytics.admin.v1alpha.DataRedactionSettings>;

Calls GetDataRedactionSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataRedactionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdataredactionsettingsrequest)`   
GetDataRedactionSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DataRedactionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.dataredactionsettings)>` | Promise  
  
### getDataRetentionSettings(request, callback)
    
    
    public getDataRetentionSettings(request: google.analytics.admin.v1alpha.IGetDataRetentionSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetDataRetentionSettingsCallback): void;

Calls GetDataRetentionSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdataretentionsettingsrequest)`   
GetDataRetentionSettingsRequest message or plain object  
`callback` |  `[GetDataRetentionSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataRetentionSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataRetentionSettings(request)
    
    
    public getDataRetentionSettings(request: google.analytics.admin.v1alpha.IGetDataRetentionSettingsRequest): Promise<google.analytics.admin.v1alpha.DataRetentionSettings>;

Calls GetDataRetentionSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdataretentionsettingsrequest)`   
GetDataRetentionSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DataRetentionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.dataretentionsettings-class)>` | Promise  
  
### getDataSharingSettings(request, callback)
    
    
    public getDataSharingSettings(request: google.analytics.admin.v1alpha.IGetDataSharingSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetDataSharingSettingsCallback): void;

Calls GetDataSharingSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSharingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdatasharingsettingsrequest)`   
GetDataSharingSettingsRequest message or plain object  
`callback` |  `[GetDataSharingSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataSharingSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataSharingSettings(request)
    
    
    public getDataSharingSettings(request: google.analytics.admin.v1alpha.IGetDataSharingSettingsRequest): Promise<google.analytics.admin.v1alpha.DataSharingSettings>;

Calls GetDataSharingSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSharingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdatasharingsettingsrequest)`   
GetDataSharingSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DataSharingSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.datasharingsettings)>` | Promise  
  
### getDataStream(request, callback)
    
    
    public getDataStream(request: google.analytics.admin.v1alpha.IGetDataStreamRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetDataStreamCallback): void;

Calls GetDataStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdatastreamrequest)`   
GetDataStreamRequest message or plain object  
`callback` |  `[GetDataStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataStream  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataStream(request)
    
    
    public getDataStream(request: google.analytics.admin.v1alpha.IGetDataStreamRequest): Promise<google.analytics.admin.v1alpha.DataStream>;

Calls GetDataStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdatastreamrequest)`   
GetDataStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.datastream-class)>` | Promise  
  
### getDisplayVideo360AdvertiserLink(request, callback)
    
    
    public getDisplayVideo360AdvertiserLink(request: google.analytics.admin.v1alpha.IGetDisplayVideo360AdvertiserLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetDisplayVideo360AdvertiserLinkCallback): void;

Calls GetDisplayVideo360AdvertiserLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdisplayvideo360advertiserlinkrequest)`   
GetDisplayVideo360AdvertiserLinkRequest message or plain object  
`callback` |  `[GetDisplayVideo360AdvertiserLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DisplayVideo360AdvertiserLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDisplayVideo360AdvertiserLink(request)
    
    
    public getDisplayVideo360AdvertiserLink(request: google.analytics.admin.v1alpha.IGetDisplayVideo360AdvertiserLinkRequest): Promise<google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLink>;

Calls GetDisplayVideo360AdvertiserLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdisplayvideo360advertiserlinkrequest)`   
GetDisplayVideo360AdvertiserLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.displayvideo360advertiserlink)>` | Promise  
  
### getDisplayVideo360AdvertiserLinkProposal(request, callback)
    
    
    public getDisplayVideo360AdvertiserLinkProposal(request: google.analytics.admin.v1alpha.IGetDisplayVideo360AdvertiserLinkProposalRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetDisplayVideo360AdvertiserLinkProposalCallback): void;

Calls GetDisplayVideo360AdvertiserLinkProposal.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdisplayvideo360advertiserlinkproposalrequest)`   
GetDisplayVideo360AdvertiserLinkProposalRequest message or plain object  
`callback` |  `[GetDisplayVideo360AdvertiserLinkProposalCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DisplayVideo360AdvertiserLinkProposal  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDisplayVideo360AdvertiserLinkProposal(request)
    
    
    public getDisplayVideo360AdvertiserLinkProposal(request: google.analytics.admin.v1alpha.IGetDisplayVideo360AdvertiserLinkProposalRequest): Promise<google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLinkProposal>;

Calls GetDisplayVideo360AdvertiserLinkProposal.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDisplayVideo360AdvertiserLinkProposalRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetdisplayvideo360advertiserlinkproposalrequest)`   
GetDisplayVideo360AdvertiserLinkProposalRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLinkProposal](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.displayvideo360advertiserlinkproposal)>` | Promise  
  
### getEnhancedMeasurementSettings(request, callback)
    
    
    public getEnhancedMeasurementSettings(request: google.analytics.admin.v1alpha.IGetEnhancedMeasurementSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetEnhancedMeasurementSettingsCallback): void;

Calls GetEnhancedMeasurementSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEnhancedMeasurementSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetenhancedmeasurementsettingsrequest)`   
GetEnhancedMeasurementSettingsRequest message or plain object  
`callback` |  `[GetEnhancedMeasurementSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and EnhancedMeasurementSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEnhancedMeasurementSettings(request)
    
    
    public getEnhancedMeasurementSettings(request: google.analytics.admin.v1alpha.IGetEnhancedMeasurementSettingsRequest): Promise<google.analytics.admin.v1alpha.EnhancedMeasurementSettings>;

Calls GetEnhancedMeasurementSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEnhancedMeasurementSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetenhancedmeasurementsettingsrequest)`   
GetEnhancedMeasurementSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.EnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.enhancedmeasurementsettings)>` | Promise  
  
### getEventCreateRule(request, callback)
    
    
    public getEventCreateRule(request: google.analytics.admin.v1alpha.IGetEventCreateRuleRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetEventCreateRuleCallback): void;

Calls GetEventCreateRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEventCreateRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igeteventcreaterulerequest)`   
GetEventCreateRuleRequest message or plain object  
`callback` |  `[GetEventCreateRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and EventCreateRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEventCreateRule(request)
    
    
    public getEventCreateRule(request: google.analytics.admin.v1alpha.IGetEventCreateRuleRequest): Promise<google.analytics.admin.v1alpha.EventCreateRule>;

Calls GetEventCreateRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEventCreateRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igeteventcreaterulerequest)`   
GetEventCreateRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.EventCreateRule](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.eventcreaterule)>` | Promise  
  
### getEventEditRule(request, callback)
    
    
    public getEventEditRule(request: google.analytics.admin.v1alpha.IGetEventEditRuleRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetEventEditRuleCallback): void;

Calls GetEventEditRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEventEditRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igeteventeditrulerequest)`   
GetEventEditRuleRequest message or plain object  
`callback` |  `[GetEventEditRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and EventEditRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEventEditRule(request)
    
    
    public getEventEditRule(request: google.analytics.admin.v1alpha.IGetEventEditRuleRequest): Promise<google.analytics.admin.v1alpha.EventEditRule>;

Calls GetEventEditRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEventEditRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igeteventeditrulerequest)`   
GetEventEditRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.EventEditRule](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.eventeditrule)>` | Promise  
  
### getExpandedDataSet(request, callback)
    
    
    public getExpandedDataSet(request: google.analytics.admin.v1alpha.IGetExpandedDataSetRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetExpandedDataSetCallback): void;

Calls GetExpandedDataSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetExpandedDataSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetexpandeddatasetrequest)`   
GetExpandedDataSetRequest message or plain object  
`callback` |  `[GetExpandedDataSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ExpandedDataSet  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getExpandedDataSet(request)
    
    
    public getExpandedDataSet(request: google.analytics.admin.v1alpha.IGetExpandedDataSetRequest): Promise<google.analytics.admin.v1alpha.ExpandedDataSet>;

Calls GetExpandedDataSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetExpandedDataSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetexpandeddatasetrequest)`   
GetExpandedDataSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ExpandedDataSet](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.expandeddataset)>` | Promise  
  
### getGlobalSiteTag(request, callback)
    
    
    public getGlobalSiteTag(request: google.analytics.admin.v1alpha.IGetGlobalSiteTagRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetGlobalSiteTagCallback): void;

Calls GetGlobalSiteTag.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGlobalSiteTagRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetglobalsitetagrequest)`   
GetGlobalSiteTagRequest message or plain object  
`callback` |  `[GetGlobalSiteTagCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and GlobalSiteTag  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGlobalSiteTag(request)
    
    
    public getGlobalSiteTag(request: google.analytics.admin.v1alpha.IGetGlobalSiteTagRequest): Promise<google.analytics.admin.v1alpha.GlobalSiteTag>;

Calls GetGlobalSiteTag.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGlobalSiteTagRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetglobalsitetagrequest)`   
GetGlobalSiteTagRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.GlobalSiteTag](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.globalsitetag)>` | Promise  
  
### getGoogleSignalsSettings(request, callback)
    
    
    public getGoogleSignalsSettings(request: google.analytics.admin.v1alpha.IGetGoogleSignalsSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetGoogleSignalsSettingsCallback): void;

Calls GetGoogleSignalsSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGoogleSignalsSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetgooglesignalssettingsrequest)`   
GetGoogleSignalsSettingsRequest message or plain object  
`callback` |  `[GetGoogleSignalsSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and GoogleSignalsSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGoogleSignalsSettings(request)
    
    
    public getGoogleSignalsSettings(request: google.analytics.admin.v1alpha.IGetGoogleSignalsSettingsRequest): Promise<google.analytics.admin.v1alpha.GoogleSignalsSettings>;

Calls GetGoogleSignalsSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGoogleSignalsSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetgooglesignalssettingsrequest)`   
GetGoogleSignalsSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.GoogleSignalsSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.googlesignalssettings)>` | Promise  
  
### getKeyEvent(request, callback)
    
    
    public getKeyEvent(request: google.analytics.admin.v1alpha.IGetKeyEventRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetKeyEventCallback): void;

Calls GetKeyEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetkeyeventrequest)`   
GetKeyEventRequest message or plain object  
`callback` |  `[GetKeyEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and KeyEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getKeyEvent(request)
    
    
    public getKeyEvent(request: google.analytics.admin.v1alpha.IGetKeyEventRequest): Promise<google.analytics.admin.v1alpha.KeyEvent>;

Calls GetKeyEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetkeyeventrequest)`   
GetKeyEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.KeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.keyevent-class)>` | Promise  
  
### getMeasurementProtocolSecret(request, callback)
    
    
    public getMeasurementProtocolSecret(request: google.analytics.admin.v1alpha.IGetMeasurementProtocolSecretRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetMeasurementProtocolSecretCallback): void;

Calls GetMeasurementProtocolSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetmeasurementprotocolsecretrequest)`   
GetMeasurementProtocolSecretRequest message or plain object  
`callback` |  `[GetMeasurementProtocolSecretCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and MeasurementProtocolSecret  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMeasurementProtocolSecret(request)
    
    
    public getMeasurementProtocolSecret(request: google.analytics.admin.v1alpha.IGetMeasurementProtocolSecretRequest): Promise<google.analytics.admin.v1alpha.MeasurementProtocolSecret>;

Calls GetMeasurementProtocolSecret.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetmeasurementprotocolsecretrequest)`   
GetMeasurementProtocolSecretRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.measurementprotocolsecret)>` | Promise  
  
### getProperty(request, callback)
    
    
    public getProperty(request: google.analytics.admin.v1alpha.IGetPropertyRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetPropertyCallback): void;

Calls GetProperty.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetpropertyrequest)`   
GetPropertyRequest message or plain object  
`callback` |  `[GetPropertyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Property  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProperty(request)
    
    
    public getProperty(request: google.analytics.admin.v1alpha.IGetPropertyRequest): Promise<google.analytics.admin.v1alpha.Property>;

Calls GetProperty.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetpropertyrequest)`   
GetPropertyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.property)>` | Promise  
  
### getReportingDataAnnotation(request, callback)
    
    
    public getReportingDataAnnotation(request: google.analytics.admin.v1alpha.IGetReportingDataAnnotationRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetReportingDataAnnotationCallback): void;

Calls GetReportingDataAnnotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReportingDataAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetreportingdataannotationrequest)`   
GetReportingDataAnnotationRequest message or plain object  
`callback` |  `[GetReportingDataAnnotationCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ReportingDataAnnotation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getReportingDataAnnotation(request)
    
    
    public getReportingDataAnnotation(request: google.analytics.admin.v1alpha.IGetReportingDataAnnotationRequest): Promise<google.analytics.admin.v1alpha.ReportingDataAnnotation>;

Calls GetReportingDataAnnotation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetReportingDataAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetreportingdataannotationrequest)`   
GetReportingDataAnnotationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ReportingDataAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.reportingdataannotation-class)>` | Promise  
  
### getReportingIdentitySettings(request, callback)
    
    
    public getReportingIdentitySettings(request: google.analytics.admin.v1alpha.IGetReportingIdentitySettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetReportingIdentitySettingsCallback): void;

Calls GetReportingIdentitySettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReportingIdentitySettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetreportingidentitysettingsrequest)`   
GetReportingIdentitySettingsRequest message or plain object  
`callback` |  `[GetReportingIdentitySettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ReportingIdentitySettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getReportingIdentitySettings(request)
    
    
    public getReportingIdentitySettings(request: google.analytics.admin.v1alpha.IGetReportingIdentitySettingsRequest): Promise<google.analytics.admin.v1alpha.ReportingIdentitySettings>;

Calls GetReportingIdentitySettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetReportingIdentitySettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetreportingidentitysettingsrequest)`   
GetReportingIdentitySettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ReportingIdentitySettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.reportingidentitysettings-class)>` | Promise  
  
### getRollupPropertySourceLink(request, callback)
    
    
    public getRollupPropertySourceLink(request: google.analytics.admin.v1alpha.IGetRollupPropertySourceLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetRollupPropertySourceLinkCallback): void;

Calls GetRollupPropertySourceLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRollupPropertySourceLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetrolluppropertysourcelinkrequest)`   
GetRollupPropertySourceLinkRequest message or plain object  
`callback` |  `[GetRollupPropertySourceLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and RollupPropertySourceLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRollupPropertySourceLink(request)
    
    
    public getRollupPropertySourceLink(request: google.analytics.admin.v1alpha.IGetRollupPropertySourceLinkRequest): Promise<google.analytics.admin.v1alpha.RollupPropertySourceLink>;

Calls GetRollupPropertySourceLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRollupPropertySourceLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetrolluppropertysourcelinkrequest)`   
GetRollupPropertySourceLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.RollupPropertySourceLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.rolluppropertysourcelink)>` | Promise  
  
### getSearchAds360Link(request, callback)
    
    
    public getSearchAds360Link(request: google.analytics.admin.v1alpha.IGetSearchAds360LinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetSearchAds360LinkCallback): void;

Calls GetSearchAds360Link.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSearchAds360LinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetsearchads360linkrequest)`   
GetSearchAds360LinkRequest message or plain object  
`callback` |  `[GetSearchAds360LinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchAds360Link  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSearchAds360Link(request)
    
    
    public getSearchAds360Link(request: google.analytics.admin.v1alpha.IGetSearchAds360LinkRequest): Promise<google.analytics.admin.v1alpha.SearchAds360Link>;

Calls GetSearchAds360Link.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSearchAds360LinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetsearchads360linkrequest)`   
GetSearchAds360LinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SearchAds360Link](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.searchads360link)>` | Promise  
  
### getSKAdNetworkConversionValueSchema(request, callback)
    
    
    public getSKAdNetworkConversionValueSchema(request: google.analytics.admin.v1alpha.IGetSKAdNetworkConversionValueSchemaRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetSKAdNetworkConversionValueSchemaCallback): void;

Calls GetSKAdNetworkConversionValueSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetskadnetworkconversionvalueschemarequest)`   
GetSKAdNetworkConversionValueSchemaRequest message or plain object  
`callback` |  `[GetSKAdNetworkConversionValueSchemaCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SKAdNetworkConversionValueSchema  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSKAdNetworkConversionValueSchema(request)
    
    
    public getSKAdNetworkConversionValueSchema(request: google.analytics.admin.v1alpha.IGetSKAdNetworkConversionValueSchemaRequest): Promise<google.analytics.admin.v1alpha.SKAdNetworkConversionValueSchema>;

Calls GetSKAdNetworkConversionValueSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetskadnetworkconversionvalueschemarequest)`   
GetSKAdNetworkConversionValueSchemaRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.skadnetworkconversionvalueschema)>` | Promise  
  
### getSubpropertyEventFilter(request, callback)
    
    
    public getSubpropertyEventFilter(request: google.analytics.admin.v1alpha.IGetSubpropertyEventFilterRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetSubpropertyEventFilterCallback): void;

Calls GetSubpropertyEventFilter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSubpropertyEventFilterRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetsubpropertyeventfilterrequest)`   
GetSubpropertyEventFilterRequest message or plain object  
`callback` |  `[GetSubpropertyEventFilterCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SubpropertyEventFilter  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSubpropertyEventFilter(request)
    
    
    public getSubpropertyEventFilter(request: google.analytics.admin.v1alpha.IGetSubpropertyEventFilterRequest): Promise<google.analytics.admin.v1alpha.SubpropertyEventFilter>;

Calls GetSubpropertyEventFilter.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSubpropertyEventFilterRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetsubpropertyeventfilterrequest)`   
GetSubpropertyEventFilterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SubpropertyEventFilter](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.subpropertyeventfilter)>` | Promise  
  
### getSubpropertySyncConfig(request, callback)
    
    
    public getSubpropertySyncConfig(request: google.analytics.admin.v1alpha.IGetSubpropertySyncConfigRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetSubpropertySyncConfigCallback): void;

Calls GetSubpropertySyncConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSubpropertySyncConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetsubpropertysyncconfigrequest)`   
GetSubpropertySyncConfigRequest message or plain object  
`callback` |  `[GetSubpropertySyncConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SubpropertySyncConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSubpropertySyncConfig(request)
    
    
    public getSubpropertySyncConfig(request: google.analytics.admin.v1alpha.IGetSubpropertySyncConfigRequest): Promise<google.analytics.admin.v1alpha.SubpropertySyncConfig>;

Calls GetSubpropertySyncConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSubpropertySyncConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetsubpropertysyncconfigrequest)`   
GetSubpropertySyncConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SubpropertySyncConfig](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.subpropertysyncconfig-class)>` | Promise  
  
### getUserProvidedDataSettings(request, callback)
    
    
    public getUserProvidedDataSettings(request: google.analytics.admin.v1alpha.IGetUserProvidedDataSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.GetUserProvidedDataSettingsCallback): void;

Calls GetUserProvidedDataSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetUserProvidedDataSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetuserprovideddatasettingsrequest)`   
GetUserProvidedDataSettingsRequest message or plain object  
`callback` |  `[GetUserProvidedDataSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and UserProvidedDataSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getUserProvidedDataSettings(request)
    
    
    public getUserProvidedDataSettings(request: google.analytics.admin.v1alpha.IGetUserProvidedDataSettingsRequest): Promise<google.analytics.admin.v1alpha.UserProvidedDataSettings>;

Calls GetUserProvidedDataSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetUserProvidedDataSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.igetuserprovideddatasettingsrequest)`   
GetUserProvidedDataSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.UserProvidedDataSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.userprovideddatasettings)>` | Promise  
  
### listAccessBindings(request, callback)
    
    
    public listAccessBindings(request: google.analytics.admin.v1alpha.IListAccessBindingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListAccessBindingsCallback): void;

Calls ListAccessBindings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistaccessbindingsrequest)`   
ListAccessBindingsRequest message or plain object  
`callback` |  `[ListAccessBindingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAccessBindingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccessBindings(request)
    
    
    public listAccessBindings(request: google.analytics.admin.v1alpha.IListAccessBindingsRequest): Promise<google.analytics.admin.v1alpha.ListAccessBindingsResponse>;

Calls ListAccessBindings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAccessBindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistaccessbindingsrequest)`   
ListAccessBindingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListAccessBindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listaccessbindingsresponse)>` | Promise  
  
### listAccounts(request, callback)
    
    
    public listAccounts(request: google.analytics.admin.v1alpha.IListAccountsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListAccountsCallback): void;

Calls ListAccounts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistaccountsrequest)`   
ListAccountsRequest message or plain object  
`callback` |  `[ListAccountsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAccountsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccounts(request)
    
    
    public listAccounts(request: google.analytics.admin.v1alpha.IListAccountsRequest): Promise<google.analytics.admin.v1alpha.ListAccountsResponse>;

Calls ListAccounts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistaccountsrequest)`   
ListAccountsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListAccountsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listaccountsresponse)>` | Promise  
  
### listAccountSummaries(request, callback)
    
    
    public listAccountSummaries(request: google.analytics.admin.v1alpha.IListAccountSummariesRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListAccountSummariesCallback): void;

Calls ListAccountSummaries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistaccountsummariesrequest)`   
ListAccountSummariesRequest message or plain object  
`callback` |  `[ListAccountSummariesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAccountSummariesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccountSummaries(request)
    
    
    public listAccountSummaries(request: google.analytics.admin.v1alpha.IListAccountSummariesRequest): Promise<google.analytics.admin.v1alpha.ListAccountSummariesResponse>;

Calls ListAccountSummaries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistaccountsummariesrequest)`   
ListAccountSummariesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListAccountSummariesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listaccountsummariesresponse)>` | Promise  
  
### listAdSenseLinks(request, callback)
    
    
    public listAdSenseLinks(request: google.analytics.admin.v1alpha.IListAdSenseLinksRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListAdSenseLinksCallback): void;

Calls ListAdSenseLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAdSenseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistadsenselinksrequest)`   
ListAdSenseLinksRequest message or plain object  
`callback` |  `[ListAdSenseLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAdSenseLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAdSenseLinks(request)
    
    
    public listAdSenseLinks(request: google.analytics.admin.v1alpha.IListAdSenseLinksRequest): Promise<google.analytics.admin.v1alpha.ListAdSenseLinksResponse>;

Calls ListAdSenseLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAdSenseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistadsenselinksrequest)`   
ListAdSenseLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListAdSenseLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listadsenselinksresponse)>` | Promise  
  
### listAudiences(request, callback)
    
    
    public listAudiences(request: google.analytics.admin.v1alpha.IListAudiencesRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListAudiencesCallback): void;

Calls ListAudiences.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAudiencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistaudiencesrequest)`   
ListAudiencesRequest message or plain object  
`callback` |  `[ListAudiencesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAudiencesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAudiences(request)
    
    
    public listAudiences(request: google.analytics.admin.v1alpha.IListAudiencesRequest): Promise<google.analytics.admin.v1alpha.ListAudiencesResponse>;

Calls ListAudiences.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAudiencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistaudiencesrequest)`   
ListAudiencesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListAudiencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listaudiencesresponse)>` | Promise  
  
### listBigQueryLinks(request, callback)
    
    
    public listBigQueryLinks(request: google.analytics.admin.v1alpha.IListBigQueryLinksRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListBigQueryLinksCallback): void;

Calls ListBigQueryLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBigQueryLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistbigquerylinksrequest)`   
ListBigQueryLinksRequest message or plain object  
`callback` |  `[ListBigQueryLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListBigQueryLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBigQueryLinks(request)
    
    
    public listBigQueryLinks(request: google.analytics.admin.v1alpha.IListBigQueryLinksRequest): Promise<google.analytics.admin.v1alpha.ListBigQueryLinksResponse>;

Calls ListBigQueryLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListBigQueryLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistbigquerylinksrequest)`   
ListBigQueryLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListBigQueryLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listbigquerylinksresponse)>` | Promise  
  
### listCalculatedMetrics(request, callback)
    
    
    public listCalculatedMetrics(request: google.analytics.admin.v1alpha.IListCalculatedMetricsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListCalculatedMetricsCallback): void;

Calls ListCalculatedMetrics.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCalculatedMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistcalculatedmetricsrequest)`   
ListCalculatedMetricsRequest message or plain object  
`callback` |  `[ListCalculatedMetricsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCalculatedMetricsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCalculatedMetrics(request)
    
    
    public listCalculatedMetrics(request: google.analytics.admin.v1alpha.IListCalculatedMetricsRequest): Promise<google.analytics.admin.v1alpha.ListCalculatedMetricsResponse>;

Calls ListCalculatedMetrics.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCalculatedMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistcalculatedmetricsrequest)`   
ListCalculatedMetricsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListCalculatedMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listcalculatedmetricsresponse)>` | Promise  
  
### listChannelGroups(request, callback)
    
    
    public listChannelGroups(request: google.analytics.admin.v1alpha.IListChannelGroupsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListChannelGroupsCallback): void;

Calls ListChannelGroups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListChannelGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistchannelgroupsrequest)`   
ListChannelGroupsRequest message or plain object  
`callback` |  `[ListChannelGroupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListChannelGroupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listChannelGroups(request)
    
    
    public listChannelGroups(request: google.analytics.admin.v1alpha.IListChannelGroupsRequest): Promise<google.analytics.admin.v1alpha.ListChannelGroupsResponse>;

Calls ListChannelGroups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListChannelGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistchannelgroupsrequest)`   
ListChannelGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListChannelGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listchannelgroupsresponse)>` | Promise  
  
### listConversionEvents(request, callback)
    
    
    public listConversionEvents(request: google.analytics.admin.v1alpha.IListConversionEventsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListConversionEventsCallback): void;

Calls ListConversionEvents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistconversioneventsrequest)`   
ListConversionEventsRequest message or plain object  
`callback` |  `[ListConversionEventsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConversionEventsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversionEvents(request)
    
    
    public listConversionEvents(request: google.analytics.admin.v1alpha.IListConversionEventsRequest): Promise<google.analytics.admin.v1alpha.ListConversionEventsResponse>;

Calls ListConversionEvents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistconversioneventsrequest)`   
ListConversionEventsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListConversionEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listconversioneventsresponse)>` | Promise  
  
### listCustomDimensions(request, callback)
    
    
    public listCustomDimensions(request: google.analytics.admin.v1alpha.IListCustomDimensionsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListCustomDimensionsCallback): void;

Calls ListCustomDimensions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistcustomdimensionsrequest)`   
ListCustomDimensionsRequest message or plain object  
`callback` |  `[ListCustomDimensionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCustomDimensionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomDimensions(request)
    
    
    public listCustomDimensions(request: google.analytics.admin.v1alpha.IListCustomDimensionsRequest): Promise<google.analytics.admin.v1alpha.ListCustomDimensionsResponse>;

Calls ListCustomDimensions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistcustomdimensionsrequest)`   
ListCustomDimensionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListCustomDimensionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listcustomdimensionsresponse)>` | Promise  
  
### listCustomMetrics(request, callback)
    
    
    public listCustomMetrics(request: google.analytics.admin.v1alpha.IListCustomMetricsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListCustomMetricsCallback): void;

Calls ListCustomMetrics.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistcustommetricsrequest)`   
ListCustomMetricsRequest message or plain object  
`callback` |  `[ListCustomMetricsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCustomMetricsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomMetrics(request)
    
    
    public listCustomMetrics(request: google.analytics.admin.v1alpha.IListCustomMetricsRequest): Promise<google.analytics.admin.v1alpha.ListCustomMetricsResponse>;

Calls ListCustomMetrics.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistcustommetricsrequest)`   
ListCustomMetricsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListCustomMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listcustommetricsresponse)>` | Promise  
  
### listDataStreams(request, callback)
    
    
    public listDataStreams(request: google.analytics.admin.v1alpha.IListDataStreamsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListDataStreamsCallback): void;

Calls ListDataStreams.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistdatastreamsrequest)`   
ListDataStreamsRequest message or plain object  
`callback` |  `[ListDataStreamsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataStreamsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataStreams(request)
    
    
    public listDataStreams(request: google.analytics.admin.v1alpha.IListDataStreamsRequest): Promise<google.analytics.admin.v1alpha.ListDataStreamsResponse>;

Calls ListDataStreams.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistdatastreamsrequest)`   
ListDataStreamsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListDataStreamsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listdatastreamsresponse)>` | Promise  
  
### listDisplayVideo360AdvertiserLinkProposals(request, callback)
    
    
    public listDisplayVideo360AdvertiserLinkProposals(request: google.analytics.admin.v1alpha.IListDisplayVideo360AdvertiserLinkProposalsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListDisplayVideo360AdvertiserLinkProposalsCallback): void;

Calls ListDisplayVideo360AdvertiserLinkProposals.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDisplayVideo360AdvertiserLinkProposalsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistdisplayvideo360advertiserlinkproposalsrequest)`   
ListDisplayVideo360AdvertiserLinkProposalsRequest message or plain object  
`callback` |  `[ListDisplayVideo360AdvertiserLinkProposalsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDisplayVideo360AdvertiserLinkProposalsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDisplayVideo360AdvertiserLinkProposals(request)
    
    
    public listDisplayVideo360AdvertiserLinkProposals(request: google.analytics.admin.v1alpha.IListDisplayVideo360AdvertiserLinkProposalsRequest): Promise<google.analytics.admin.v1alpha.ListDisplayVideo360AdvertiserLinkProposalsResponse>;

Calls ListDisplayVideo360AdvertiserLinkProposals.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDisplayVideo360AdvertiserLinkProposalsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistdisplayvideo360advertiserlinkproposalsrequest)`   
ListDisplayVideo360AdvertiserLinkProposalsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListDisplayVideo360AdvertiserLinkProposalsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listdisplayvideo360advertiserlinkproposalsresponse)>` | Promise  
  
### listDisplayVideo360AdvertiserLinks(request, callback)
    
    
    public listDisplayVideo360AdvertiserLinks(request: google.analytics.admin.v1alpha.IListDisplayVideo360AdvertiserLinksRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListDisplayVideo360AdvertiserLinksCallback): void;

Calls ListDisplayVideo360AdvertiserLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDisplayVideo360AdvertiserLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistdisplayvideo360advertiserlinksrequest)`   
ListDisplayVideo360AdvertiserLinksRequest message or plain object  
`callback` |  `[ListDisplayVideo360AdvertiserLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDisplayVideo360AdvertiserLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDisplayVideo360AdvertiserLinks(request)
    
    
    public listDisplayVideo360AdvertiserLinks(request: google.analytics.admin.v1alpha.IListDisplayVideo360AdvertiserLinksRequest): Promise<google.analytics.admin.v1alpha.ListDisplayVideo360AdvertiserLinksResponse>;

Calls ListDisplayVideo360AdvertiserLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDisplayVideo360AdvertiserLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistdisplayvideo360advertiserlinksrequest)`   
ListDisplayVideo360AdvertiserLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListDisplayVideo360AdvertiserLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listdisplayvideo360advertiserlinksresponse)>` | Promise  
  
### listEventCreateRules(request, callback)
    
    
    public listEventCreateRules(request: google.analytics.admin.v1alpha.IListEventCreateRulesRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListEventCreateRulesCallback): void;

Calls ListEventCreateRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEventCreateRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilisteventcreaterulesrequest)`   
ListEventCreateRulesRequest message or plain object  
`callback` |  `[ListEventCreateRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEventCreateRulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEventCreateRules(request)
    
    
    public listEventCreateRules(request: google.analytics.admin.v1alpha.IListEventCreateRulesRequest): Promise<google.analytics.admin.v1alpha.ListEventCreateRulesResponse>;

Calls ListEventCreateRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEventCreateRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilisteventcreaterulesrequest)`   
ListEventCreateRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListEventCreateRulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listeventcreaterulesresponse)>` | Promise  
  
### listEventEditRules(request, callback)
    
    
    public listEventEditRules(request: google.analytics.admin.v1alpha.IListEventEditRulesRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListEventEditRulesCallback): void;

Calls ListEventEditRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEventEditRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilisteventeditrulesrequest)`   
ListEventEditRulesRequest message or plain object  
`callback` |  `[ListEventEditRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEventEditRulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEventEditRules(request)
    
    
    public listEventEditRules(request: google.analytics.admin.v1alpha.IListEventEditRulesRequest): Promise<google.analytics.admin.v1alpha.ListEventEditRulesResponse>;

Calls ListEventEditRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEventEditRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilisteventeditrulesrequest)`   
ListEventEditRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListEventEditRulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listeventeditrulesresponse)>` | Promise  
  
### listExpandedDataSets(request, callback)
    
    
    public listExpandedDataSets(request: google.analytics.admin.v1alpha.IListExpandedDataSetsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListExpandedDataSetsCallback): void;

Calls ListExpandedDataSets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListExpandedDataSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistexpandeddatasetsrequest)`   
ListExpandedDataSetsRequest message or plain object  
`callback` |  `[ListExpandedDataSetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListExpandedDataSetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listExpandedDataSets(request)
    
    
    public listExpandedDataSets(request: google.analytics.admin.v1alpha.IListExpandedDataSetsRequest): Promise<google.analytics.admin.v1alpha.ListExpandedDataSetsResponse>;

Calls ListExpandedDataSets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListExpandedDataSetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistexpandeddatasetsrequest)`   
ListExpandedDataSetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListExpandedDataSetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listexpandeddatasetsresponse)>` | Promise  
  
### listFirebaseLinks(request, callback)
    
    
    public listFirebaseLinks(request: google.analytics.admin.v1alpha.IListFirebaseLinksRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListFirebaseLinksCallback): void;

Calls ListFirebaseLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistfirebaselinksrequest)`   
ListFirebaseLinksRequest message or plain object  
`callback` |  `[ListFirebaseLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFirebaseLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFirebaseLinks(request)
    
    
    public listFirebaseLinks(request: google.analytics.admin.v1alpha.IListFirebaseLinksRequest): Promise<google.analytics.admin.v1alpha.ListFirebaseLinksResponse>;

Calls ListFirebaseLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistfirebaselinksrequest)`   
ListFirebaseLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListFirebaseLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listfirebaselinksresponse)>` | Promise  
  
### listGoogleAdsLinks(request, callback)
    
    
    public listGoogleAdsLinks(request: google.analytics.admin.v1alpha.IListGoogleAdsLinksRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListGoogleAdsLinksCallback): void;

Calls ListGoogleAdsLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistgoogleadslinksrequest)`   
ListGoogleAdsLinksRequest message or plain object  
`callback` |  `[ListGoogleAdsLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGoogleAdsLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGoogleAdsLinks(request)
    
    
    public listGoogleAdsLinks(request: google.analytics.admin.v1alpha.IListGoogleAdsLinksRequest): Promise<google.analytics.admin.v1alpha.ListGoogleAdsLinksResponse>;

Calls ListGoogleAdsLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistgoogleadslinksrequest)`   
ListGoogleAdsLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListGoogleAdsLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listgoogleadslinksresponse)>` | Promise  
  
### listKeyEvents(request, callback)
    
    
    public listKeyEvents(request: google.analytics.admin.v1alpha.IListKeyEventsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListKeyEventsCallback): void;

Calls ListKeyEvents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistkeyeventsrequest)`   
ListKeyEventsRequest message or plain object  
`callback` |  `[ListKeyEventsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListKeyEventsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listKeyEvents(request)
    
    
    public listKeyEvents(request: google.analytics.admin.v1alpha.IListKeyEventsRequest): Promise<google.analytics.admin.v1alpha.ListKeyEventsResponse>;

Calls ListKeyEvents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistkeyeventsrequest)`   
ListKeyEventsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListKeyEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listkeyeventsresponse)>` | Promise  
  
### listMeasurementProtocolSecrets(request, callback)
    
    
    public listMeasurementProtocolSecrets(request: google.analytics.admin.v1alpha.IListMeasurementProtocolSecretsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListMeasurementProtocolSecretsCallback): void;

Calls ListMeasurementProtocolSecrets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistmeasurementprotocolsecretsrequest)`   
ListMeasurementProtocolSecretsRequest message or plain object  
`callback` |  `[ListMeasurementProtocolSecretsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMeasurementProtocolSecretsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMeasurementProtocolSecrets(request)
    
    
    public listMeasurementProtocolSecrets(request: google.analytics.admin.v1alpha.IListMeasurementProtocolSecretsRequest): Promise<google.analytics.admin.v1alpha.ListMeasurementProtocolSecretsResponse>;

Calls ListMeasurementProtocolSecrets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistmeasurementprotocolsecretsrequest)`   
ListMeasurementProtocolSecretsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListMeasurementProtocolSecretsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listmeasurementprotocolsecretsresponse)>` | Promise  
  
### listProperties(request, callback)
    
    
    public listProperties(request: google.analytics.admin.v1alpha.IListPropertiesRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListPropertiesCallback): void;

Calls ListProperties.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistpropertiesrequest)`   
ListPropertiesRequest message or plain object  
`callback` |  `[ListPropertiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPropertiesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProperties(request)
    
    
    public listProperties(request: google.analytics.admin.v1alpha.IListPropertiesRequest): Promise<google.analytics.admin.v1alpha.ListPropertiesResponse>;

Calls ListProperties.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistpropertiesrequest)`   
ListPropertiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListPropertiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listpropertiesresponse)>` | Promise  
  
### listReportingDataAnnotations(request, callback)
    
    
    public listReportingDataAnnotations(request: google.analytics.admin.v1alpha.IListReportingDataAnnotationsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListReportingDataAnnotationsCallback): void;

Calls ListReportingDataAnnotations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReportingDataAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistreportingdataannotationsrequest)`   
ListReportingDataAnnotationsRequest message or plain object  
`callback` |  `[ListReportingDataAnnotationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListReportingDataAnnotationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReportingDataAnnotations(request)
    
    
    public listReportingDataAnnotations(request: google.analytics.admin.v1alpha.IListReportingDataAnnotationsRequest): Promise<google.analytics.admin.v1alpha.ListReportingDataAnnotationsResponse>;

Calls ListReportingDataAnnotations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListReportingDataAnnotationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistreportingdataannotationsrequest)`   
ListReportingDataAnnotationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListReportingDataAnnotationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listreportingdataannotationsresponse)>` | Promise  
  
### listRollupPropertySourceLinks(request, callback)
    
    
    public listRollupPropertySourceLinks(request: google.analytics.admin.v1alpha.IListRollupPropertySourceLinksRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListRollupPropertySourceLinksCallback): void;

Calls ListRollupPropertySourceLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRollupPropertySourceLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistrolluppropertysourcelinksrequest)`   
ListRollupPropertySourceLinksRequest message or plain object  
`callback` |  `[ListRollupPropertySourceLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRollupPropertySourceLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRollupPropertySourceLinks(request)
    
    
    public listRollupPropertySourceLinks(request: google.analytics.admin.v1alpha.IListRollupPropertySourceLinksRequest): Promise<google.analytics.admin.v1alpha.ListRollupPropertySourceLinksResponse>;

Calls ListRollupPropertySourceLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRollupPropertySourceLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistrolluppropertysourcelinksrequest)`   
ListRollupPropertySourceLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListRollupPropertySourceLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listrolluppropertysourcelinksresponse)>` | Promise  
  
### listSearchAds360Links(request, callback)
    
    
    public listSearchAds360Links(request: google.analytics.admin.v1alpha.IListSearchAds360LinksRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListSearchAds360LinksCallback): void;

Calls ListSearchAds360Links.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSearchAds360LinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistsearchads360linksrequest)`   
ListSearchAds360LinksRequest message or plain object  
`callback` |  `[ListSearchAds360LinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSearchAds360LinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSearchAds360Links(request)
    
    
    public listSearchAds360Links(request: google.analytics.admin.v1alpha.IListSearchAds360LinksRequest): Promise<google.analytics.admin.v1alpha.ListSearchAds360LinksResponse>;

Calls ListSearchAds360Links.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSearchAds360LinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistsearchads360linksrequest)`   
ListSearchAds360LinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListSearchAds360LinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listsearchads360linksresponse)>` | Promise  
  
### listSKAdNetworkConversionValueSchemas(request, callback)
    
    
    public listSKAdNetworkConversionValueSchemas(request: google.analytics.admin.v1alpha.IListSKAdNetworkConversionValueSchemasRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListSKAdNetworkConversionValueSchemasCallback): void;

Calls ListSKAdNetworkConversionValueSchemas.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSKAdNetworkConversionValueSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistskadnetworkconversionvalueschemasrequest)`   
ListSKAdNetworkConversionValueSchemasRequest message or plain object  
`callback` |  `[ListSKAdNetworkConversionValueSchemasCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSKAdNetworkConversionValueSchemasResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSKAdNetworkConversionValueSchemas(request)
    
    
    public listSKAdNetworkConversionValueSchemas(request: google.analytics.admin.v1alpha.IListSKAdNetworkConversionValueSchemasRequest): Promise<google.analytics.admin.v1alpha.ListSKAdNetworkConversionValueSchemasResponse>;

Calls ListSKAdNetworkConversionValueSchemas.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSKAdNetworkConversionValueSchemasRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistskadnetworkconversionvalueschemasrequest)`   
ListSKAdNetworkConversionValueSchemasRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListSKAdNetworkConversionValueSchemasResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listskadnetworkconversionvalueschemasresponse)>` | Promise  
  
### listSubpropertyEventFilters(request, callback)
    
    
    public listSubpropertyEventFilters(request: google.analytics.admin.v1alpha.IListSubpropertyEventFiltersRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListSubpropertyEventFiltersCallback): void;

Calls ListSubpropertyEventFilters.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSubpropertyEventFiltersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistsubpropertyeventfiltersrequest)`   
ListSubpropertyEventFiltersRequest message or plain object  
`callback` |  `[ListSubpropertyEventFiltersCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSubpropertyEventFiltersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSubpropertyEventFilters(request)
    
    
    public listSubpropertyEventFilters(request: google.analytics.admin.v1alpha.IListSubpropertyEventFiltersRequest): Promise<google.analytics.admin.v1alpha.ListSubpropertyEventFiltersResponse>;

Calls ListSubpropertyEventFilters.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSubpropertyEventFiltersRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistsubpropertyeventfiltersrequest)`   
ListSubpropertyEventFiltersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListSubpropertyEventFiltersResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listsubpropertyeventfiltersresponse)>` | Promise  
  
### listSubpropertySyncConfigs(request, callback)
    
    
    public listSubpropertySyncConfigs(request: google.analytics.admin.v1alpha.IListSubpropertySyncConfigsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ListSubpropertySyncConfigsCallback): void;

Calls ListSubpropertySyncConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSubpropertySyncConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistsubpropertysyncconfigsrequest)`   
ListSubpropertySyncConfigsRequest message or plain object  
`callback` |  `[ListSubpropertySyncConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSubpropertySyncConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSubpropertySyncConfigs(request)
    
    
    public listSubpropertySyncConfigs(request: google.analytics.admin.v1alpha.IListSubpropertySyncConfigsRequest): Promise<google.analytics.admin.v1alpha.ListSubpropertySyncConfigsResponse>;

Calls ListSubpropertySyncConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSubpropertySyncConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ilistsubpropertysyncconfigsrequest)`   
ListSubpropertySyncConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ListSubpropertySyncConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.listsubpropertysyncconfigsresponse)>` | Promise  
  
### provisionAccountTicket(request, callback)
    
    
    public provisionAccountTicket(request: google.analytics.admin.v1alpha.IProvisionAccountTicketRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ProvisionAccountTicketCallback): void;

Calls ProvisionAccountTicket.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProvisionAccountTicketRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iprovisionaccountticketrequest)`   
ProvisionAccountTicketRequest message or plain object  
`callback` |  `[ProvisionAccountTicketCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ProvisionAccountTicketResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### provisionAccountTicket(request)
    
    
    public provisionAccountTicket(request: google.analytics.admin.v1alpha.IProvisionAccountTicketRequest): Promise<google.analytics.admin.v1alpha.ProvisionAccountTicketResponse>;

Calls ProvisionAccountTicket.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IProvisionAccountTicketRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iprovisionaccountticketrequest)`   
ProvisionAccountTicketRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ProvisionAccountTicketResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.provisionaccountticketresponse)>` | Promise  
  
### provisionSubproperty(request, callback)
    
    
    public provisionSubproperty(request: google.analytics.admin.v1alpha.IProvisionSubpropertyRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ProvisionSubpropertyCallback): void;

Calls ProvisionSubproperty.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProvisionSubpropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iprovisionsubpropertyrequest)`   
ProvisionSubpropertyRequest message or plain object  
`callback` |  `[ProvisionSubpropertyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ProvisionSubpropertyResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### provisionSubproperty(request)
    
    
    public provisionSubproperty(request: google.analytics.admin.v1alpha.IProvisionSubpropertyRequest): Promise<google.analytics.admin.v1alpha.ProvisionSubpropertyResponse>;

Calls ProvisionSubproperty.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IProvisionSubpropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iprovisionsubpropertyrequest)`   
ProvisionSubpropertyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ProvisionSubpropertyResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.provisionsubpropertyresponse)>` | Promise  
  
### reorderEventEditRules(request, callback)
    
    
    public reorderEventEditRules(request: google.analytics.admin.v1alpha.IReorderEventEditRulesRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.ReorderEventEditRulesCallback): void;

Calls ReorderEventEditRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReorderEventEditRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ireordereventeditrulesrequest)`   
ReorderEventEditRulesRequest message or plain object  
`callback` |  `[ReorderEventEditRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### reorderEventEditRules(request)
    
    
    public reorderEventEditRules(request: google.analytics.admin.v1alpha.IReorderEventEditRulesRequest): Promise<google.protobuf.Empty>;

Calls ReorderEventEditRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReorderEventEditRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ireordereventeditrulesrequest)`   
ReorderEventEditRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### runAccessReport(request, callback)
    
    
    public runAccessReport(request: google.analytics.admin.v1alpha.IRunAccessReportRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.RunAccessReportCallback): void;

Calls RunAccessReport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunAccessReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.irunaccessreportrequest)`   
RunAccessReportRequest message or plain object  
`callback` |  `[RunAccessReportCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and RunAccessReportResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runAccessReport(request)
    
    
    public runAccessReport(request: google.analytics.admin.v1alpha.IRunAccessReportRequest): Promise<google.analytics.admin.v1alpha.RunAccessReportResponse>;

Calls RunAccessReport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRunAccessReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.irunaccessreportrequest)`   
RunAccessReportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.RunAccessReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.runaccessreportresponse)>` | Promise  
  
### searchChangeHistoryEvents(request, callback)
    
    
    public searchChangeHistoryEvents(request: google.analytics.admin.v1alpha.ISearchChangeHistoryEventsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.SearchChangeHistoryEventsCallback): void;

Calls SearchChangeHistoryEvents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.isearchchangehistoryeventsrequest)`   
SearchChangeHistoryEventsRequest message or plain object  
`callback` |  `[SearchChangeHistoryEventsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchChangeHistoryEventsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchChangeHistoryEvents(request)
    
    
    public searchChangeHistoryEvents(request: google.analytics.admin.v1alpha.ISearchChangeHistoryEventsRequest): Promise<google.analytics.admin.v1alpha.SearchChangeHistoryEventsResponse>;

Calls SearchChangeHistoryEvents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.isearchchangehistoryeventsrequest)`   
SearchChangeHistoryEventsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SearchChangeHistoryEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.searchchangehistoryeventsresponse)>` | Promise  
  
### submitUserDeletion(request, callback)
    
    
    public submitUserDeletion(request: google.analytics.admin.v1alpha.ISubmitUserDeletionRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.SubmitUserDeletionCallback): void;

Calls SubmitUserDeletion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubmitUserDeletionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.isubmituserdeletionrequest)`   
SubmitUserDeletionRequest message or plain object  
`callback` |  `[SubmitUserDeletionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SubmitUserDeletionResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### submitUserDeletion(request)
    
    
    public submitUserDeletion(request: google.analytics.admin.v1alpha.ISubmitUserDeletionRequest): Promise<google.analytics.admin.v1alpha.SubmitUserDeletionResponse>;

Calls SubmitUserDeletion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISubmitUserDeletionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.isubmituserdeletionrequest)`   
SubmitUserDeletionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SubmitUserDeletionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.submituserdeletionresponse)>` | Promise  
  
### updateAccessBinding(request, callback)
    
    
    public updateAccessBinding(request: google.analytics.admin.v1alpha.IUpdateAccessBindingRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateAccessBindingCallback): void;

Calls UpdateAccessBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateaccessbindingrequest)`   
UpdateAccessBindingRequest message or plain object  
`callback` |  `[UpdateAccessBindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AccessBinding  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAccessBinding(request)
    
    
    public updateAccessBinding(request: google.analytics.admin.v1alpha.IUpdateAccessBindingRequest): Promise<google.analytics.admin.v1alpha.AccessBinding>;

Calls UpdateAccessBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateaccessbindingrequest)`   
UpdateAccessBindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.AccessBinding](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.accessbinding)>` | Promise  
  
### updateAccount(request, callback)
    
    
    public updateAccount(request: google.analytics.admin.v1alpha.IUpdateAccountRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateAccountCallback): void;

Calls UpdateAccount.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateaccountrequest)`   
UpdateAccountRequest message or plain object  
`callback` |  `[UpdateAccountCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Account  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAccount(request)
    
    
    public updateAccount(request: google.analytics.admin.v1alpha.IUpdateAccountRequest): Promise<google.analytics.admin.v1alpha.Account>;

Calls UpdateAccount.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateaccountrequest)`   
UpdateAccountRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.Account](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.account)>` | Promise  
  
### updateAttributionSettings(request, callback)
    
    
    public updateAttributionSettings(request: google.analytics.admin.v1alpha.IUpdateAttributionSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateAttributionSettingsCallback): void;

Calls UpdateAttributionSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttributionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateattributionsettingsrequest)`   
UpdateAttributionSettingsRequest message or plain object  
`callback` |  `[UpdateAttributionSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AttributionSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAttributionSettings(request)
    
    
    public updateAttributionSettings(request: google.analytics.admin.v1alpha.IUpdateAttributionSettingsRequest): Promise<google.analytics.admin.v1alpha.AttributionSettings>;

Calls UpdateAttributionSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAttributionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateattributionsettingsrequest)`   
UpdateAttributionSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.AttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.attributionsettings-class)>` | Promise  
  
### updateAudience(request, callback)
    
    
    public updateAudience(request: google.analytics.admin.v1alpha.IUpdateAudienceRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateAudienceCallback): void;

Calls UpdateAudience.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAudienceRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateaudiencerequest)`   
UpdateAudienceRequest message or plain object  
`callback` |  `[UpdateAudienceCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Audience  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAudience(request)
    
    
    public updateAudience(request: google.analytics.admin.v1alpha.IUpdateAudienceRequest): Promise<google.analytics.admin.v1alpha.Audience>;

Calls UpdateAudience.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAudienceRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateaudiencerequest)`   
UpdateAudienceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.Audience](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.audience-class)>` | Promise  
  
### updateBigQueryLink(request, callback)
    
    
    public updateBigQueryLink(request: google.analytics.admin.v1alpha.IUpdateBigQueryLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateBigQueryLinkCallback): void;

Calls UpdateBigQueryLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBigQueryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatebigquerylinkrequest)`   
UpdateBigQueryLinkRequest message or plain object  
`callback` |  `[UpdateBigQueryLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and BigQueryLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBigQueryLink(request)
    
    
    public updateBigQueryLink(request: google.analytics.admin.v1alpha.IUpdateBigQueryLinkRequest): Promise<google.analytics.admin.v1alpha.BigQueryLink>;

Calls UpdateBigQueryLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBigQueryLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatebigquerylinkrequest)`   
UpdateBigQueryLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.BigQueryLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.bigquerylink)>` | Promise  
  
### updateCalculatedMetric(request, callback)
    
    
    public updateCalculatedMetric(request: google.analytics.admin.v1alpha.IUpdateCalculatedMetricRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateCalculatedMetricCallback): void;

Calls UpdateCalculatedMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCalculatedMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatecalculatedmetricrequest)`   
UpdateCalculatedMetricRequest message or plain object  
`callback` |  `[UpdateCalculatedMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CalculatedMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCalculatedMetric(request)
    
    
    public updateCalculatedMetric(request: google.analytics.admin.v1alpha.IUpdateCalculatedMetricRequest): Promise<google.analytics.admin.v1alpha.CalculatedMetric>;

Calls UpdateCalculatedMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCalculatedMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatecalculatedmetricrequest)`   
UpdateCalculatedMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.CalculatedMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.calculatedmetric-class)>` | Promise  
  
### updateChannelGroup(request, callback)
    
    
    public updateChannelGroup(request: google.analytics.admin.v1alpha.IUpdateChannelGroupRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateChannelGroupCallback): void;

Calls UpdateChannelGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChannelGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatechannelgrouprequest)`   
UpdateChannelGroupRequest message or plain object  
`callback` |  `[UpdateChannelGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ChannelGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateChannelGroup(request)
    
    
    public updateChannelGroup(request: google.analytics.admin.v1alpha.IUpdateChannelGroupRequest): Promise<google.analytics.admin.v1alpha.ChannelGroup>;

Calls UpdateChannelGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateChannelGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatechannelgrouprequest)`   
UpdateChannelGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ChannelGroup](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.channelgroup)>` | Promise  
  
### updateConversionEvent(request, callback)
    
    
    public updateConversionEvent(request: google.analytics.admin.v1alpha.IUpdateConversionEventRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateConversionEventCallback): void;

Calls UpdateConversionEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateconversioneventrequest)`   
UpdateConversionEventRequest message or plain object  
`callback` |  `[UpdateConversionEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversionEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversionEvent(request)
    
    
    public updateConversionEvent(request: google.analytics.admin.v1alpha.IUpdateConversionEventRequest): Promise<google.analytics.admin.v1alpha.ConversionEvent>;

Calls UpdateConversionEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateconversioneventrequest)`   
UpdateConversionEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.conversionevent-class)>` | Promise  
  
### updateCustomDimension(request, callback)
    
    
    public updateCustomDimension(request: google.analytics.admin.v1alpha.IUpdateCustomDimensionRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateCustomDimensionCallback): void;

Calls UpdateCustomDimension.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatecustomdimensionrequest)`   
UpdateCustomDimensionRequest message or plain object  
`callback` |  `[UpdateCustomDimensionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomDimension  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomDimension(request)
    
    
    public updateCustomDimension(request: google.analytics.admin.v1alpha.IUpdateCustomDimensionRequest): Promise<google.analytics.admin.v1alpha.CustomDimension>;

Calls UpdateCustomDimension.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatecustomdimensionrequest)`   
UpdateCustomDimensionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.CustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.customdimension-class)>` | Promise  
  
### updateCustomMetric(request, callback)
    
    
    public updateCustomMetric(request: google.analytics.admin.v1alpha.IUpdateCustomMetricRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateCustomMetricCallback): void;

Calls UpdateCustomMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatecustommetricrequest)`   
UpdateCustomMetricRequest message or plain object  
`callback` |  `[UpdateCustomMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomMetric(request)
    
    
    public updateCustomMetric(request: google.analytics.admin.v1alpha.IUpdateCustomMetricRequest): Promise<google.analytics.admin.v1alpha.CustomMetric>;

Calls UpdateCustomMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatecustommetricrequest)`   
UpdateCustomMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.CustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.custommetric-class)>` | Promise  
  
### updateDataRedactionSettings(request, callback)
    
    
    public updateDataRedactionSettings(request: google.analytics.admin.v1alpha.IUpdateDataRedactionSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateDataRedactionSettingsCallback): void;

Calls UpdateDataRedactionSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataRedactionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatedataredactionsettingsrequest)`   
UpdateDataRedactionSettingsRequest message or plain object  
`callback` |  `[UpdateDataRedactionSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataRedactionSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataRedactionSettings(request)
    
    
    public updateDataRedactionSettings(request: google.analytics.admin.v1alpha.IUpdateDataRedactionSettingsRequest): Promise<google.analytics.admin.v1alpha.DataRedactionSettings>;

Calls UpdateDataRedactionSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataRedactionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatedataredactionsettingsrequest)`   
UpdateDataRedactionSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DataRedactionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.dataredactionsettings)>` | Promise  
  
### updateDataRetentionSettings(request, callback)
    
    
    public updateDataRetentionSettings(request: google.analytics.admin.v1alpha.IUpdateDataRetentionSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateDataRetentionSettingsCallback): void;

Calls UpdateDataRetentionSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatedataretentionsettingsrequest)`   
UpdateDataRetentionSettingsRequest message or plain object  
`callback` |  `[UpdateDataRetentionSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataRetentionSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataRetentionSettings(request)
    
    
    public updateDataRetentionSettings(request: google.analytics.admin.v1alpha.IUpdateDataRetentionSettingsRequest): Promise<google.analytics.admin.v1alpha.DataRetentionSettings>;

Calls UpdateDataRetentionSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatedataretentionsettingsrequest)`   
UpdateDataRetentionSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DataRetentionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.dataretentionsettings-class)>` | Promise  
  
### updateDataStream(request, callback)
    
    
    public updateDataStream(request: google.analytics.admin.v1alpha.IUpdateDataStreamRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateDataStreamCallback): void;

Calls UpdateDataStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatedatastreamrequest)`   
UpdateDataStreamRequest message or plain object  
`callback` |  `[UpdateDataStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataStream  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataStream(request)
    
    
    public updateDataStream(request: google.analytics.admin.v1alpha.IUpdateDataStreamRequest): Promise<google.analytics.admin.v1alpha.DataStream>;

Calls UpdateDataStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatedatastreamrequest)`   
UpdateDataStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.datastream-class)>` | Promise  
  
### updateDisplayVideo360AdvertiserLink(request, callback)
    
    
    public updateDisplayVideo360AdvertiserLink(request: google.analytics.admin.v1alpha.IUpdateDisplayVideo360AdvertiserLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateDisplayVideo360AdvertiserLinkCallback): void;

Calls UpdateDisplayVideo360AdvertiserLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatedisplayvideo360advertiserlinkrequest)`   
UpdateDisplayVideo360AdvertiserLinkRequest message or plain object  
`callback` |  `[UpdateDisplayVideo360AdvertiserLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DisplayVideo360AdvertiserLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDisplayVideo360AdvertiserLink(request)
    
    
    public updateDisplayVideo360AdvertiserLink(request: google.analytics.admin.v1alpha.IUpdateDisplayVideo360AdvertiserLinkRequest): Promise<google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLink>;

Calls UpdateDisplayVideo360AdvertiserLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDisplayVideo360AdvertiserLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatedisplayvideo360advertiserlinkrequest)`   
UpdateDisplayVideo360AdvertiserLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.displayvideo360advertiserlink)>` | Promise  
  
### updateEnhancedMeasurementSettings(request, callback)
    
    
    public updateEnhancedMeasurementSettings(request: google.analytics.admin.v1alpha.IUpdateEnhancedMeasurementSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateEnhancedMeasurementSettingsCallback): void;

Calls UpdateEnhancedMeasurementSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEnhancedMeasurementSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateenhancedmeasurementsettingsrequest)`   
UpdateEnhancedMeasurementSettingsRequest message or plain object  
`callback` |  `[UpdateEnhancedMeasurementSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and EnhancedMeasurementSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEnhancedMeasurementSettings(request)
    
    
    public updateEnhancedMeasurementSettings(request: google.analytics.admin.v1alpha.IUpdateEnhancedMeasurementSettingsRequest): Promise<google.analytics.admin.v1alpha.EnhancedMeasurementSettings>;

Calls UpdateEnhancedMeasurementSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEnhancedMeasurementSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateenhancedmeasurementsettingsrequest)`   
UpdateEnhancedMeasurementSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.EnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.enhancedmeasurementsettings)>` | Promise  
  
### updateEventCreateRule(request, callback)
    
    
    public updateEventCreateRule(request: google.analytics.admin.v1alpha.IUpdateEventCreateRuleRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateEventCreateRuleCallback): void;

Calls UpdateEventCreateRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEventCreateRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateeventcreaterulerequest)`   
UpdateEventCreateRuleRequest message or plain object  
`callback` |  `[UpdateEventCreateRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and EventCreateRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEventCreateRule(request)
    
    
    public updateEventCreateRule(request: google.analytics.admin.v1alpha.IUpdateEventCreateRuleRequest): Promise<google.analytics.admin.v1alpha.EventCreateRule>;

Calls UpdateEventCreateRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEventCreateRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateeventcreaterulerequest)`   
UpdateEventCreateRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.EventCreateRule](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.eventcreaterule)>` | Promise  
  
### updateEventEditRule(request, callback)
    
    
    public updateEventEditRule(request: google.analytics.admin.v1alpha.IUpdateEventEditRuleRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateEventEditRuleCallback): void;

Calls UpdateEventEditRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEventEditRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateeventeditrulerequest)`   
UpdateEventEditRuleRequest message or plain object  
`callback` |  `[UpdateEventEditRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and EventEditRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEventEditRule(request)
    
    
    public updateEventEditRule(request: google.analytics.admin.v1alpha.IUpdateEventEditRuleRequest): Promise<google.analytics.admin.v1alpha.EventEditRule>;

Calls UpdateEventEditRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEventEditRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateeventeditrulerequest)`   
UpdateEventEditRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.EventEditRule](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.eventeditrule)>` | Promise  
  
### updateExpandedDataSet(request, callback)
    
    
    public updateExpandedDataSet(request: google.analytics.admin.v1alpha.IUpdateExpandedDataSetRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateExpandedDataSetCallback): void;

Calls UpdateExpandedDataSet.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateExpandedDataSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateexpandeddatasetrequest)`   
UpdateExpandedDataSetRequest message or plain object  
`callback` |  `[UpdateExpandedDataSetCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ExpandedDataSet  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateExpandedDataSet(request)
    
    
    public updateExpandedDataSet(request: google.analytics.admin.v1alpha.IUpdateExpandedDataSetRequest): Promise<google.analytics.admin.v1alpha.ExpandedDataSet>;

Calls UpdateExpandedDataSet.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateExpandedDataSetRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateexpandeddatasetrequest)`   
UpdateExpandedDataSetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ExpandedDataSet](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.expandeddataset)>` | Promise  
  
### updateGoogleAdsLink(request, callback)
    
    
    public updateGoogleAdsLink(request: google.analytics.admin.v1alpha.IUpdateGoogleAdsLinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateGoogleAdsLinkCallback): void;

Calls UpdateGoogleAdsLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdategoogleadslinkrequest)`   
UpdateGoogleAdsLinkRequest message or plain object  
`callback` |  `[UpdateGoogleAdsLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and GoogleAdsLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGoogleAdsLink(request)
    
    
    public updateGoogleAdsLink(request: google.analytics.admin.v1alpha.IUpdateGoogleAdsLinkRequest): Promise<google.analytics.admin.v1alpha.GoogleAdsLink>;

Calls UpdateGoogleAdsLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdategoogleadslinkrequest)`   
UpdateGoogleAdsLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.GoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.googleadslink)>` | Promise  
  
### updateGoogleSignalsSettings(request, callback)
    
    
    public updateGoogleSignalsSettings(request: google.analytics.admin.v1alpha.IUpdateGoogleSignalsSettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateGoogleSignalsSettingsCallback): void;

Calls UpdateGoogleSignalsSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleSignalsSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdategooglesignalssettingsrequest)`   
UpdateGoogleSignalsSettingsRequest message or plain object  
`callback` |  `[UpdateGoogleSignalsSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and GoogleSignalsSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGoogleSignalsSettings(request)
    
    
    public updateGoogleSignalsSettings(request: google.analytics.admin.v1alpha.IUpdateGoogleSignalsSettingsRequest): Promise<google.analytics.admin.v1alpha.GoogleSignalsSettings>;

Calls UpdateGoogleSignalsSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleSignalsSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdategooglesignalssettingsrequest)`   
UpdateGoogleSignalsSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.GoogleSignalsSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.googlesignalssettings)>` | Promise  
  
### updateKeyEvent(request, callback)
    
    
    public updateKeyEvent(request: google.analytics.admin.v1alpha.IUpdateKeyEventRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateKeyEventCallback): void;

Calls UpdateKeyEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatekeyeventrequest)`   
UpdateKeyEventRequest message or plain object  
`callback` |  `[UpdateKeyEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and KeyEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateKeyEvent(request)
    
    
    public updateKeyEvent(request: google.analytics.admin.v1alpha.IUpdateKeyEventRequest): Promise<google.analytics.admin.v1alpha.KeyEvent>;

Calls UpdateKeyEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatekeyeventrequest)`   
UpdateKeyEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.KeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.keyevent-class)>` | Promise  
  
### updateMeasurementProtocolSecret(request, callback)
    
    
    public updateMeasurementProtocolSecret(request: google.analytics.admin.v1alpha.IUpdateMeasurementProtocolSecretRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateMeasurementProtocolSecretCallback): void;

Calls UpdateMeasurementProtocolSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatemeasurementprotocolsecretrequest)`   
UpdateMeasurementProtocolSecretRequest message or plain object  
`callback` |  `[UpdateMeasurementProtocolSecretCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and MeasurementProtocolSecret  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMeasurementProtocolSecret(request)
    
    
    public updateMeasurementProtocolSecret(request: google.analytics.admin.v1alpha.IUpdateMeasurementProtocolSecretRequest): Promise<google.analytics.admin.v1alpha.MeasurementProtocolSecret>;

Calls UpdateMeasurementProtocolSecret.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatemeasurementprotocolsecretrequest)`   
UpdateMeasurementProtocolSecretRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.measurementprotocolsecret)>` | Promise  
  
### updateProperty(request, callback)
    
    
    public updateProperty(request: google.analytics.admin.v1alpha.IUpdatePropertyRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdatePropertyCallback): void;

Calls UpdateProperty.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatepropertyrequest)`   
UpdatePropertyRequest message or plain object  
`callback` |  `[UpdatePropertyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Property  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProperty(request)
    
    
    public updateProperty(request: google.analytics.admin.v1alpha.IUpdatePropertyRequest): Promise<google.analytics.admin.v1alpha.Property>;

Calls UpdateProperty.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatepropertyrequest)`   
UpdatePropertyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.property)>` | Promise  
  
### updateReportingDataAnnotation(request, callback)
    
    
    public updateReportingDataAnnotation(request: google.analytics.admin.v1alpha.IUpdateReportingDataAnnotationRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateReportingDataAnnotationCallback): void;

Calls UpdateReportingDataAnnotation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReportingDataAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatereportingdataannotationrequest)`   
UpdateReportingDataAnnotationRequest message or plain object  
`callback` |  `[UpdateReportingDataAnnotationCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ReportingDataAnnotation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateReportingDataAnnotation(request)
    
    
    public updateReportingDataAnnotation(request: google.analytics.admin.v1alpha.IUpdateReportingDataAnnotationRequest): Promise<google.analytics.admin.v1alpha.ReportingDataAnnotation>;

Calls UpdateReportingDataAnnotation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReportingDataAnnotationRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatereportingdataannotationrequest)`   
UpdateReportingDataAnnotationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ReportingDataAnnotation](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.reportingdataannotation-class)>` | Promise  
  
### updateReportingIdentitySettings(request, callback)
    
    
    public updateReportingIdentitySettings(request: google.analytics.admin.v1alpha.IUpdateReportingIdentitySettingsRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateReportingIdentitySettingsCallback): void;

Calls UpdateReportingIdentitySettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReportingIdentitySettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatereportingidentitysettingsrequest)`   
UpdateReportingIdentitySettingsRequest message or plain object  
`callback` |  `[UpdateReportingIdentitySettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ReportingIdentitySettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateReportingIdentitySettings(request)
    
    
    public updateReportingIdentitySettings(request: google.analytics.admin.v1alpha.IUpdateReportingIdentitySettingsRequest): Promise<google.analytics.admin.v1alpha.ReportingIdentitySettings>;

Calls UpdateReportingIdentitySettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReportingIdentitySettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatereportingidentitysettingsrequest)`   
UpdateReportingIdentitySettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.ReportingIdentitySettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.reportingidentitysettings-class)>` | Promise  
  
### updateSearchAds360Link(request, callback)
    
    
    public updateSearchAds360Link(request: google.analytics.admin.v1alpha.IUpdateSearchAds360LinkRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateSearchAds360LinkCallback): void;

Calls UpdateSearchAds360Link.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSearchAds360LinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatesearchads360linkrequest)`   
UpdateSearchAds360LinkRequest message or plain object  
`callback` |  `[UpdateSearchAds360LinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchAds360Link  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSearchAds360Link(request)
    
    
    public updateSearchAds360Link(request: google.analytics.admin.v1alpha.IUpdateSearchAds360LinkRequest): Promise<google.analytics.admin.v1alpha.SearchAds360Link>;

Calls UpdateSearchAds360Link.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSearchAds360LinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatesearchads360linkrequest)`   
UpdateSearchAds360LinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SearchAds360Link](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.searchads360link)>` | Promise  
  
### updateSKAdNetworkConversionValueSchema(request, callback)
    
    
    public updateSKAdNetworkConversionValueSchema(request: google.analytics.admin.v1alpha.IUpdateSKAdNetworkConversionValueSchemaRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateSKAdNetworkConversionValueSchemaCallback): void;

Calls UpdateSKAdNetworkConversionValueSchema.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateskadnetworkconversionvalueschemarequest)`   
UpdateSKAdNetworkConversionValueSchemaRequest message or plain object  
`callback` |  `[UpdateSKAdNetworkConversionValueSchemaCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SKAdNetworkConversionValueSchema  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSKAdNetworkConversionValueSchema(request)
    
    
    public updateSKAdNetworkConversionValueSchema(request: google.analytics.admin.v1alpha.IUpdateSKAdNetworkConversionValueSchemaRequest): Promise<google.analytics.admin.v1alpha.SKAdNetworkConversionValueSchema>;

Calls UpdateSKAdNetworkConversionValueSchema.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSKAdNetworkConversionValueSchemaRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdateskadnetworkconversionvalueschemarequest)`   
UpdateSKAdNetworkConversionValueSchemaRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SKAdNetworkConversionValueSchema](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.skadnetworkconversionvalueschema)>` | Promise  
  
### updateSubpropertyEventFilter(request, callback)
    
    
    public updateSubpropertyEventFilter(request: google.analytics.admin.v1alpha.IUpdateSubpropertyEventFilterRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateSubpropertyEventFilterCallback): void;

Calls UpdateSubpropertyEventFilter.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSubpropertyEventFilterRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatesubpropertyeventfilterrequest)`   
UpdateSubpropertyEventFilterRequest message or plain object  
`callback` |  `[UpdateSubpropertyEventFilterCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SubpropertyEventFilter  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSubpropertyEventFilter(request)
    
    
    public updateSubpropertyEventFilter(request: google.analytics.admin.v1alpha.IUpdateSubpropertyEventFilterRequest): Promise<google.analytics.admin.v1alpha.SubpropertyEventFilter>;

Calls UpdateSubpropertyEventFilter.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSubpropertyEventFilterRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatesubpropertyeventfilterrequest)`   
UpdateSubpropertyEventFilterRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SubpropertyEventFilter](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.subpropertyeventfilter)>` | Promise  
  
### updateSubpropertySyncConfig(request, callback)
    
    
    public updateSubpropertySyncConfig(request: google.analytics.admin.v1alpha.IUpdateSubpropertySyncConfigRequest, callback: google.analytics.admin.v1alpha.AnalyticsAdminService.UpdateSubpropertySyncConfigCallback): void;

Calls UpdateSubpropertySyncConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSubpropertySyncConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatesubpropertysyncconfigrequest)`   
UpdateSubpropertySyncConfigRequest message or plain object  
`callback` |  `[UpdateSubpropertySyncConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SubpropertySyncConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSubpropertySyncConfig(request)
    
    
    public updateSubpropertySyncConfig(request: google.analytics.admin.v1alpha.IUpdateSubpropertySyncConfigRequest): Promise<google.analytics.admin.v1alpha.SubpropertySyncConfig>;

Calls UpdateSubpropertySyncConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSubpropertySyncConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iupdatesubpropertysyncconfigrequest)`   
UpdateSubpropertySyncConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1alpha.SubpropertySyncConfig](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.subpropertysyncconfig-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
