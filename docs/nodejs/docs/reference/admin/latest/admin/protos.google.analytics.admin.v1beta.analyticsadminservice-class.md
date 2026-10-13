---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.analyticsadminservice-class
title: Class protos.google.analytics.admin.v1beta.AnalyticsAdminService (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:45.420332+00:00
---

# Class protos.google.analytics.admin.v1beta.AnalyticsAdminService (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.analyticsadminservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.admin.v1beta.AnalyticsAdminService (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Represents an AnalyticsAdminService

## Inheritance

$protobuf.rpc.Service > protos.google.analytics.admin.v1beta.AnalyticsAdminService

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
    
    
    public acknowledgeUserDataCollection(request: google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.AcknowledgeUserDataCollectionCallback): void;

Calls AcknowledgeUserDataCollection.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionrequest)`   
AcknowledgeUserDataCollectionRequest message or plain object  
`callback` |  `[AcknowledgeUserDataCollectionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AcknowledgeUserDataCollectionResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### acknowledgeUserDataCollection(request)
    
    
    public acknowledgeUserDataCollection(request: google.analytics.admin.v1beta.IAcknowledgeUserDataCollectionRequest): Promise<google.analytics.admin.v1beta.AcknowledgeUserDataCollectionResponse>;

Calls AcknowledgeUserDataCollection.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeUserDataCollectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iacknowledgeuserdatacollectionrequest)`   
AcknowledgeUserDataCollectionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.AcknowledgeUserDataCollectionResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.acknowledgeuserdatacollectionresponse)>` | Promise  
  
### archiveCustomDimension(request, callback)
    
    
    public archiveCustomDimension(request: google.analytics.admin.v1beta.IArchiveCustomDimensionRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ArchiveCustomDimensionCallback): void;

Calls ArchiveCustomDimension.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustomdimensionrequest)`   
ArchiveCustomDimensionRequest message or plain object  
`callback` |  `[ArchiveCustomDimensionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### archiveCustomDimension(request)
    
    
    public archiveCustomDimension(request: google.analytics.admin.v1beta.IArchiveCustomDimensionRequest): Promise<google.protobuf.Empty>;

Calls ArchiveCustomDimension.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustomdimensionrequest)`   
ArchiveCustomDimensionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### archiveCustomMetric(request, callback)
    
    
    public archiveCustomMetric(request: google.analytics.admin.v1beta.IArchiveCustomMetricRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ArchiveCustomMetricCallback): void;

Calls ArchiveCustomMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustommetricrequest)`   
ArchiveCustomMetricRequest message or plain object  
`callback` |  `[ArchiveCustomMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### archiveCustomMetric(request)
    
    
    public archiveCustomMetric(request: google.analytics.admin.v1beta.IArchiveCustomMetricRequest): Promise<google.protobuf.Empty>;

Calls ArchiveCustomMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IArchiveCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iarchivecustommetricrequest)`   
ArchiveCustomMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
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
`[AnalyticsAdminService](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.analyticsadminservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createConversionEvent(request, callback)
    
    
    public createConversionEvent(request: google.analytics.admin.v1beta.ICreateConversionEventRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.CreateConversionEventCallback): void;

Calls CreateConversionEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreateconversioneventrequest)`   
CreateConversionEventRequest message or plain object  
`callback` |  `[CreateConversionEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversionEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createConversionEvent(request)
    
    
    public createConversionEvent(request: google.analytics.admin.v1beta.ICreateConversionEventRequest): Promise<google.analytics.admin.v1beta.ConversionEvent>;

Calls CreateConversionEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreateconversioneventrequest)`   
CreateConversionEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.conversionevent-class)>` | Promise  
  
### createCustomDimension(request, callback)
    
    
    public createCustomDimension(request: google.analytics.admin.v1beta.ICreateCustomDimensionRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.CreateCustomDimensionCallback): void;

Calls CreateCustomDimension.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustomdimensionrequest)`   
CreateCustomDimensionRequest message or plain object  
`callback` |  `[CreateCustomDimensionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomDimension  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomDimension(request)
    
    
    public createCustomDimension(request: google.analytics.admin.v1beta.ICreateCustomDimensionRequest): Promise<google.analytics.admin.v1beta.CustomDimension>;

Calls CreateCustomDimension.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustomdimensionrequest)`   
CreateCustomDimensionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.CustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.customdimension-class)>` | Promise  
  
### createCustomMetric(request, callback)
    
    
    public createCustomMetric(request: google.analytics.admin.v1beta.ICreateCustomMetricRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.CreateCustomMetricCallback): void;

Calls CreateCustomMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustommetricrequest)`   
CreateCustomMetricRequest message or plain object  
`callback` |  `[CreateCustomMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCustomMetric(request)
    
    
    public createCustomMetric(request: google.analytics.admin.v1beta.ICreateCustomMetricRequest): Promise<google.analytics.admin.v1beta.CustomMetric>;

Calls CreateCustomMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatecustommetricrequest)`   
CreateCustomMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.CustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.custommetric-class)>` | Promise  
  
### createDataStream(request, callback)
    
    
    public createDataStream(request: google.analytics.admin.v1beta.ICreateDataStreamRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.CreateDataStreamCallback): void;

Calls CreateDataStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatedatastreamrequest)`   
CreateDataStreamRequest message or plain object  
`callback` |  `[CreateDataStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataStream  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataStream(request)
    
    
    public createDataStream(request: google.analytics.admin.v1beta.ICreateDataStreamRequest): Promise<google.analytics.admin.v1beta.DataStream>;

Calls CreateDataStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatedatastreamrequest)`   
CreateDataStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.DataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.datastream-class)>` | Promise  
  
### createFirebaseLink(request, callback)
    
    
    public createFirebaseLink(request: google.analytics.admin.v1beta.ICreateFirebaseLinkRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.CreateFirebaseLinkCallback): void;

Calls CreateFirebaseLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatefirebaselinkrequest)`   
CreateFirebaseLinkRequest message or plain object  
`callback` |  `[CreateFirebaseLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and FirebaseLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFirebaseLink(request)
    
    
    public createFirebaseLink(request: google.analytics.admin.v1beta.ICreateFirebaseLinkRequest): Promise<google.analytics.admin.v1beta.FirebaseLink>;

Calls CreateFirebaseLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatefirebaselinkrequest)`   
CreateFirebaseLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.FirebaseLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.firebaselink)>` | Promise  
  
### createGoogleAdsLink(request, callback)
    
    
    public createGoogleAdsLink(request: google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.CreateGoogleAdsLinkCallback): void;

Calls CreateGoogleAdsLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreategoogleadslinkrequest)`   
CreateGoogleAdsLinkRequest message or plain object  
`callback` |  `[CreateGoogleAdsLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and GoogleAdsLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGoogleAdsLink(request)
    
    
    public createGoogleAdsLink(request: google.analytics.admin.v1beta.ICreateGoogleAdsLinkRequest): Promise<google.analytics.admin.v1beta.GoogleAdsLink>;

Calls CreateGoogleAdsLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreategoogleadslinkrequest)`   
CreateGoogleAdsLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.GoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.googleadslink)>` | Promise  
  
### createKeyEvent(request, callback)
    
    
    public createKeyEvent(request: google.analytics.admin.v1beta.ICreateKeyEventRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.CreateKeyEventCallback): void;

Calls CreateKeyEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatekeyeventrequest)`   
CreateKeyEventRequest message or plain object  
`callback` |  `[CreateKeyEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and KeyEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createKeyEvent(request)
    
    
    public createKeyEvent(request: google.analytics.admin.v1beta.ICreateKeyEventRequest): Promise<google.analytics.admin.v1beta.KeyEvent>;

Calls CreateKeyEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatekeyeventrequest)`   
CreateKeyEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.KeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.keyevent-class)>` | Promise  
  
### createMeasurementProtocolSecret(request, callback)
    
    
    public createMeasurementProtocolSecret(request: google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.CreateMeasurementProtocolSecretCallback): void;

Calls CreateMeasurementProtocolSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatemeasurementprotocolsecretrequest)`   
CreateMeasurementProtocolSecretRequest message or plain object  
`callback` |  `[CreateMeasurementProtocolSecretCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and MeasurementProtocolSecret  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createMeasurementProtocolSecret(request)
    
    
    public createMeasurementProtocolSecret(request: google.analytics.admin.v1beta.ICreateMeasurementProtocolSecretRequest): Promise<google.analytics.admin.v1beta.MeasurementProtocolSecret>;

Calls CreateMeasurementProtocolSecret.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatemeasurementprotocolsecretrequest)`   
CreateMeasurementProtocolSecretRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.measurementprotocolsecret)>` | Promise  
  
### createProperty(request, callback)
    
    
    public createProperty(request: google.analytics.admin.v1beta.ICreatePropertyRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.CreatePropertyCallback): void;

Calls CreateProperty.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatepropertyrequest)`   
CreatePropertyRequest message or plain object  
`callback` |  `[CreatePropertyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Property  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProperty(request)
    
    
    public createProperty(request: google.analytics.admin.v1beta.ICreatePropertyRequest): Promise<google.analytics.admin.v1beta.Property>;

Calls CreateProperty.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.icreatepropertyrequest)`   
CreatePropertyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property)>` | Promise  
  
### deleteAccount(request, callback)
    
    
    public deleteAccount(request: google.analytics.admin.v1beta.IDeleteAccountRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.DeleteAccountCallback): void;

Calls DeleteAccount.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteaccountrequest)`   
DeleteAccountRequest message or plain object  
`callback` |  `[DeleteAccountCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAccount(request)
    
    
    public deleteAccount(request: google.analytics.admin.v1beta.IDeleteAccountRequest): Promise<google.protobuf.Empty>;

Calls DeleteAccount.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteaccountrequest)`   
DeleteAccountRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteConversionEvent(request, callback)
    
    
    public deleteConversionEvent(request: google.analytics.admin.v1beta.IDeleteConversionEventRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.DeleteConversionEventCallback): void;

Calls DeleteConversionEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteconversioneventrequest)`   
DeleteConversionEventRequest message or plain object  
`callback` |  `[DeleteConversionEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteConversionEvent(request)
    
    
    public deleteConversionEvent(request: google.analytics.admin.v1beta.IDeleteConversionEventRequest): Promise<google.protobuf.Empty>;

Calls DeleteConversionEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideleteconversioneventrequest)`   
DeleteConversionEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteDataStream(request, callback)
    
    
    public deleteDataStream(request: google.analytics.admin.v1beta.IDeleteDataStreamRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.DeleteDataStreamCallback): void;

Calls DeleteDataStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletedatastreamrequest)`   
DeleteDataStreamRequest message or plain object  
`callback` |  `[DeleteDataStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataStream(request)
    
    
    public deleteDataStream(request: google.analytics.admin.v1beta.IDeleteDataStreamRequest): Promise<google.protobuf.Empty>;

Calls DeleteDataStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletedatastreamrequest)`   
DeleteDataStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteFirebaseLink(request, callback)
    
    
    public deleteFirebaseLink(request: google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.DeleteFirebaseLinkCallback): void;

Calls DeleteFirebaseLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletefirebaselinkrequest)`   
DeleteFirebaseLinkRequest message or plain object  
`callback` |  `[DeleteFirebaseLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteFirebaseLink(request)
    
    
    public deleteFirebaseLink(request: google.analytics.admin.v1beta.IDeleteFirebaseLinkRequest): Promise<google.protobuf.Empty>;

Calls DeleteFirebaseLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteFirebaseLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletefirebaselinkrequest)`   
DeleteFirebaseLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteGoogleAdsLink(request, callback)
    
    
    public deleteGoogleAdsLink(request: google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.DeleteGoogleAdsLinkCallback): void;

Calls DeleteGoogleAdsLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletegoogleadslinkrequest)`   
DeleteGoogleAdsLinkRequest message or plain object  
`callback` |  `[DeleteGoogleAdsLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteGoogleAdsLink(request)
    
    
    public deleteGoogleAdsLink(request: google.analytics.admin.v1beta.IDeleteGoogleAdsLinkRequest): Promise<google.protobuf.Empty>;

Calls DeleteGoogleAdsLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletegoogleadslinkrequest)`   
DeleteGoogleAdsLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteKeyEvent(request, callback)
    
    
    public deleteKeyEvent(request: google.analytics.admin.v1beta.IDeleteKeyEventRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.DeleteKeyEventCallback): void;

Calls DeleteKeyEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletekeyeventrequest)`   
DeleteKeyEventRequest message or plain object  
`callback` |  `[DeleteKeyEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteKeyEvent(request)
    
    
    public deleteKeyEvent(request: google.analytics.admin.v1beta.IDeleteKeyEventRequest): Promise<google.protobuf.Empty>;

Calls DeleteKeyEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletekeyeventrequest)`   
DeleteKeyEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteMeasurementProtocolSecret(request, callback)
    
    
    public deleteMeasurementProtocolSecret(request: google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.DeleteMeasurementProtocolSecretCallback): void;

Calls DeleteMeasurementProtocolSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletemeasurementprotocolsecretrequest)`   
DeleteMeasurementProtocolSecretRequest message or plain object  
`callback` |  `[DeleteMeasurementProtocolSecretCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteMeasurementProtocolSecret(request)
    
    
    public deleteMeasurementProtocolSecret(request: google.analytics.admin.v1beta.IDeleteMeasurementProtocolSecretRequest): Promise<google.protobuf.Empty>;

Calls DeleteMeasurementProtocolSecret.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletemeasurementprotocolsecretrequest)`   
DeleteMeasurementProtocolSecretRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.protobuf.empty)>` | Promise  
  
### deleteProperty(request, callback)
    
    
    public deleteProperty(request: google.analytics.admin.v1beta.IDeletePropertyRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.DeletePropertyCallback): void;

Calls DeleteProperty.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletepropertyrequest)`   
DeletePropertyRequest message or plain object  
`callback` |  `[DeletePropertyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Property  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProperty(request)
    
    
    public deleteProperty(request: google.analytics.admin.v1beta.IDeletePropertyRequest): Promise<google.analytics.admin.v1beta.Property>;

Calls DeleteProperty.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ideletepropertyrequest)`   
DeletePropertyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property)>` | Promise  
  
### getAccount(request, callback)
    
    
    public getAccount(request: google.analytics.admin.v1beta.IGetAccountRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.GetAccountCallback): void;

Calls GetAccount.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetaccountrequest)`   
GetAccountRequest message or plain object  
`callback` |  `[GetAccountCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Account  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAccount(request)
    
    
    public getAccount(request: google.analytics.admin.v1beta.IGetAccountRequest): Promise<google.analytics.admin.v1beta.Account>;

Calls GetAccount.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetaccountrequest)`   
GetAccountRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.Account](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.account)>` | Promise  
  
### getConversionEvent(request, callback)
    
    
    public getConversionEvent(request: google.analytics.admin.v1beta.IGetConversionEventRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.GetConversionEventCallback): void;

Calls GetConversionEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetconversioneventrequest)`   
GetConversionEventRequest message or plain object  
`callback` |  `[GetConversionEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversionEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getConversionEvent(request)
    
    
    public getConversionEvent(request: google.analytics.admin.v1beta.IGetConversionEventRequest): Promise<google.analytics.admin.v1beta.ConversionEvent>;

Calls GetConversionEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetconversioneventrequest)`   
GetConversionEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.conversionevent-class)>` | Promise  
  
### getCustomDimension(request, callback)
    
    
    public getCustomDimension(request: google.analytics.admin.v1beta.IGetCustomDimensionRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.GetCustomDimensionCallback): void;

Calls GetCustomDimension.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustomdimensionrequest)`   
GetCustomDimensionRequest message or plain object  
`callback` |  `[GetCustomDimensionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomDimension  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomDimension(request)
    
    
    public getCustomDimension(request: google.analytics.admin.v1beta.IGetCustomDimensionRequest): Promise<google.analytics.admin.v1beta.CustomDimension>;

Calls GetCustomDimension.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustomdimensionrequest)`   
GetCustomDimensionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.CustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.customdimension-class)>` | Promise  
  
### getCustomMetric(request, callback)
    
    
    public getCustomMetric(request: google.analytics.admin.v1beta.IGetCustomMetricRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.GetCustomMetricCallback): void;

Calls GetCustomMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustommetricrequest)`   
GetCustomMetricRequest message or plain object  
`callback` |  `[GetCustomMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCustomMetric(request)
    
    
    public getCustomMetric(request: google.analytics.admin.v1beta.IGetCustomMetricRequest): Promise<google.analytics.admin.v1beta.CustomMetric>;

Calls GetCustomMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetcustommetricrequest)`   
GetCustomMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.CustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.custommetric-class)>` | Promise  
  
### getDataRetentionSettings(request, callback)
    
    
    public getDataRetentionSettings(request: google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.GetDataRetentionSettingsCallback): void;

Calls GetDataRetentionSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdataretentionsettingsrequest)`   
GetDataRetentionSettingsRequest message or plain object  
`callback` |  `[GetDataRetentionSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataRetentionSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataRetentionSettings(request)
    
    
    public getDataRetentionSettings(request: google.analytics.admin.v1beta.IGetDataRetentionSettingsRequest): Promise<google.analytics.admin.v1beta.DataRetentionSettings>;

Calls GetDataRetentionSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdataretentionsettingsrequest)`   
GetDataRetentionSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.DataRetentionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.dataretentionsettings-class)>` | Promise  
  
### getDataSharingSettings(request, callback)
    
    
    public getDataSharingSettings(request: google.analytics.admin.v1beta.IGetDataSharingSettingsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.GetDataSharingSettingsCallback): void;

Calls GetDataSharingSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSharingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatasharingsettingsrequest)`   
GetDataSharingSettingsRequest message or plain object  
`callback` |  `[GetDataSharingSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataSharingSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataSharingSettings(request)
    
    
    public getDataSharingSettings(request: google.analytics.admin.v1beta.IGetDataSharingSettingsRequest): Promise<google.analytics.admin.v1beta.DataSharingSettings>;

Calls GetDataSharingSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataSharingSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatasharingsettingsrequest)`   
GetDataSharingSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.DataSharingSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.datasharingsettings)>` | Promise  
  
### getDataStream(request, callback)
    
    
    public getDataStream(request: google.analytics.admin.v1beta.IGetDataStreamRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.GetDataStreamCallback): void;

Calls GetDataStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatastreamrequest)`   
GetDataStreamRequest message or plain object  
`callback` |  `[GetDataStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataStream  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataStream(request)
    
    
    public getDataStream(request: google.analytics.admin.v1beta.IGetDataStreamRequest): Promise<google.analytics.admin.v1beta.DataStream>;

Calls GetDataStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetdatastreamrequest)`   
GetDataStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.DataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.datastream-class)>` | Promise  
  
### getKeyEvent(request, callback)
    
    
    public getKeyEvent(request: google.analytics.admin.v1beta.IGetKeyEventRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.GetKeyEventCallback): void;

Calls GetKeyEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetkeyeventrequest)`   
GetKeyEventRequest message or plain object  
`callback` |  `[GetKeyEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and KeyEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getKeyEvent(request)
    
    
    public getKeyEvent(request: google.analytics.admin.v1beta.IGetKeyEventRequest): Promise<google.analytics.admin.v1beta.KeyEvent>;

Calls GetKeyEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetkeyeventrequest)`   
GetKeyEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.KeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.keyevent-class)>` | Promise  
  
### getMeasurementProtocolSecret(request, callback)
    
    
    public getMeasurementProtocolSecret(request: google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.GetMeasurementProtocolSecretCallback): void;

Calls GetMeasurementProtocolSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetmeasurementprotocolsecretrequest)`   
GetMeasurementProtocolSecretRequest message or plain object  
`callback` |  `[GetMeasurementProtocolSecretCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and MeasurementProtocolSecret  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getMeasurementProtocolSecret(request)
    
    
    public getMeasurementProtocolSecret(request: google.analytics.admin.v1beta.IGetMeasurementProtocolSecretRequest): Promise<google.analytics.admin.v1beta.MeasurementProtocolSecret>;

Calls GetMeasurementProtocolSecret.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetmeasurementprotocolsecretrequest)`   
GetMeasurementProtocolSecretRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.measurementprotocolsecret)>` | Promise  
  
### getProperty(request, callback)
    
    
    public getProperty(request: google.analytics.admin.v1beta.IGetPropertyRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.GetPropertyCallback): void;

Calls GetProperty.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetpropertyrequest)`   
GetPropertyRequest message or plain object  
`callback` |  `[GetPropertyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Property  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProperty(request)
    
    
    public getProperty(request: google.analytics.admin.v1beta.IGetPropertyRequest): Promise<google.analytics.admin.v1beta.Property>;

Calls GetProperty.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.igetpropertyrequest)`   
GetPropertyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property)>` | Promise  
  
### listAccounts(request, callback)
    
    
    public listAccounts(request: google.analytics.admin.v1beta.IListAccountsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListAccountsCallback): void;

Calls ListAccounts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsrequest)`   
ListAccountsRequest message or plain object  
`callback` |  `[ListAccountsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAccountsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccounts(request)
    
    
    public listAccounts(request: google.analytics.admin.v1beta.IListAccountsRequest): Promise<google.analytics.admin.v1beta.ListAccountsResponse>;

Calls ListAccounts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAccountsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsrequest)`   
ListAccountsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListAccountsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listaccountsresponse)>` | Promise  
  
### listAccountSummaries(request, callback)
    
    
    public listAccountSummaries(request: google.analytics.admin.v1beta.IListAccountSummariesRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListAccountSummariesCallback): void;

Calls ListAccountSummaries.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesrequest)`   
ListAccountSummariesRequest message or plain object  
`callback` |  `[ListAccountSummariesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAccountSummariesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccountSummaries(request)
    
    
    public listAccountSummaries(request: google.analytics.admin.v1beta.IListAccountSummariesRequest): Promise<google.analytics.admin.v1beta.ListAccountSummariesResponse>;

Calls ListAccountSummaries.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAccountSummariesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistaccountsummariesrequest)`   
ListAccountSummariesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListAccountSummariesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listaccountsummariesresponse)>` | Promise  
  
### listConversionEvents(request, callback)
    
    
    public listConversionEvents(request: google.analytics.admin.v1beta.IListConversionEventsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListConversionEventsCallback): void;

Calls ListConversionEvents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsrequest)`   
ListConversionEventsRequest message or plain object  
`callback` |  `[ListConversionEventsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListConversionEventsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listConversionEvents(request)
    
    
    public listConversionEvents(request: google.analytics.admin.v1beta.IListConversionEventsRequest): Promise<google.analytics.admin.v1beta.ListConversionEventsResponse>;

Calls ListConversionEvents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListConversionEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistconversioneventsrequest)`   
ListConversionEventsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListConversionEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listconversioneventsresponse)>` | Promise  
  
### listCustomDimensions(request, callback)
    
    
    public listCustomDimensions(request: google.analytics.admin.v1beta.IListCustomDimensionsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListCustomDimensionsCallback): void;

Calls ListCustomDimensions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsrequest)`   
ListCustomDimensionsRequest message or plain object  
`callback` |  `[ListCustomDimensionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCustomDimensionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomDimensions(request)
    
    
    public listCustomDimensions(request: google.analytics.admin.v1beta.IListCustomDimensionsRequest): Promise<google.analytics.admin.v1beta.ListCustomDimensionsResponse>;

Calls ListCustomDimensions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCustomDimensionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustomdimensionsrequest)`   
ListCustomDimensionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListCustomDimensionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listcustomdimensionsresponse)>` | Promise  
  
### listCustomMetrics(request, callback)
    
    
    public listCustomMetrics(request: google.analytics.admin.v1beta.IListCustomMetricsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListCustomMetricsCallback): void;

Calls ListCustomMetrics.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsrequest)`   
ListCustomMetricsRequest message or plain object  
`callback` |  `[ListCustomMetricsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCustomMetricsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCustomMetrics(request)
    
    
    public listCustomMetrics(request: google.analytics.admin.v1beta.IListCustomMetricsRequest): Promise<google.analytics.admin.v1beta.ListCustomMetricsResponse>;

Calls ListCustomMetrics.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCustomMetricsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistcustommetricsrequest)`   
ListCustomMetricsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListCustomMetricsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listcustommetricsresponse)>` | Promise  
  
### listDataStreams(request, callback)
    
    
    public listDataStreams(request: google.analytics.admin.v1beta.IListDataStreamsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListDataStreamsCallback): void;

Calls ListDataStreams.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsrequest)`   
ListDataStreamsRequest message or plain object  
`callback` |  `[ListDataStreamsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataStreamsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataStreams(request)
    
    
    public listDataStreams(request: google.analytics.admin.v1beta.IListDataStreamsRequest): Promise<google.analytics.admin.v1beta.ListDataStreamsResponse>;

Calls ListDataStreams.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataStreamsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistdatastreamsrequest)`   
ListDataStreamsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListDataStreamsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listdatastreamsresponse)>` | Promise  
  
### listFirebaseLinks(request, callback)
    
    
    public listFirebaseLinks(request: google.analytics.admin.v1beta.IListFirebaseLinksRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListFirebaseLinksCallback): void;

Calls ListFirebaseLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksrequest)`   
ListFirebaseLinksRequest message or plain object  
`callback` |  `[ListFirebaseLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFirebaseLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFirebaseLinks(request)
    
    
    public listFirebaseLinks(request: google.analytics.admin.v1beta.IListFirebaseLinksRequest): Promise<google.analytics.admin.v1beta.ListFirebaseLinksResponse>;

Calls ListFirebaseLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFirebaseLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistfirebaselinksrequest)`   
ListFirebaseLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListFirebaseLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listfirebaselinksresponse)>` | Promise  
  
### listGoogleAdsLinks(request, callback)
    
    
    public listGoogleAdsLinks(request: google.analytics.admin.v1beta.IListGoogleAdsLinksRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListGoogleAdsLinksCallback): void;

Calls ListGoogleAdsLinks.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksrequest)`   
ListGoogleAdsLinksRequest message or plain object  
`callback` |  `[ListGoogleAdsLinksCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGoogleAdsLinksResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGoogleAdsLinks(request)
    
    
    public listGoogleAdsLinks(request: google.analytics.admin.v1beta.IListGoogleAdsLinksRequest): Promise<google.analytics.admin.v1beta.ListGoogleAdsLinksResponse>;

Calls ListGoogleAdsLinks.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGoogleAdsLinksRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistgoogleadslinksrequest)`   
ListGoogleAdsLinksRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListGoogleAdsLinksResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listgoogleadslinksresponse)>` | Promise  
  
### listKeyEvents(request, callback)
    
    
    public listKeyEvents(request: google.analytics.admin.v1beta.IListKeyEventsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListKeyEventsCallback): void;

Calls ListKeyEvents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsrequest)`   
ListKeyEventsRequest message or plain object  
`callback` |  `[ListKeyEventsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListKeyEventsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listKeyEvents(request)
    
    
    public listKeyEvents(request: google.analytics.admin.v1beta.IListKeyEventsRequest): Promise<google.analytics.admin.v1beta.ListKeyEventsResponse>;

Calls ListKeyEvents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListKeyEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistkeyeventsrequest)`   
ListKeyEventsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListKeyEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listkeyeventsresponse)>` | Promise  
  
### listMeasurementProtocolSecrets(request, callback)
    
    
    public listMeasurementProtocolSecrets(request: google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListMeasurementProtocolSecretsCallback): void;

Calls ListMeasurementProtocolSecrets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsrequest)`   
ListMeasurementProtocolSecretsRequest message or plain object  
`callback` |  `[ListMeasurementProtocolSecretsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListMeasurementProtocolSecretsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listMeasurementProtocolSecrets(request)
    
    
    public listMeasurementProtocolSecrets(request: google.analytics.admin.v1beta.IListMeasurementProtocolSecretsRequest): Promise<google.analytics.admin.v1beta.ListMeasurementProtocolSecretsResponse>;

Calls ListMeasurementProtocolSecrets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListMeasurementProtocolSecretsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistmeasurementprotocolsecretsrequest)`   
ListMeasurementProtocolSecretsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListMeasurementProtocolSecretsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listmeasurementprotocolsecretsresponse)>` | Promise  
  
### listProperties(request, callback)
    
    
    public listProperties(request: google.analytics.admin.v1beta.IListPropertiesRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ListPropertiesCallback): void;

Calls ListProperties.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesrequest)`   
ListPropertiesRequest message or plain object  
`callback` |  `[ListPropertiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPropertiesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProperties(request)
    
    
    public listProperties(request: google.analytics.admin.v1beta.IListPropertiesRequest): Promise<google.analytics.admin.v1beta.ListPropertiesResponse>;

Calls ListProperties.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPropertiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.ilistpropertiesrequest)`   
ListPropertiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ListPropertiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.listpropertiesresponse)>` | Promise  
  
### provisionAccountTicket(request, callback)
    
    
    public provisionAccountTicket(request: google.analytics.admin.v1beta.IProvisionAccountTicketRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.ProvisionAccountTicketCallback): void;

Calls ProvisionAccountTicket.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProvisionAccountTicketRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketrequest)`   
ProvisionAccountTicketRequest message or plain object  
`callback` |  `[ProvisionAccountTicketCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ProvisionAccountTicketResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### provisionAccountTicket(request)
    
    
    public provisionAccountTicket(request: google.analytics.admin.v1beta.IProvisionAccountTicketRequest): Promise<google.analytics.admin.v1beta.ProvisionAccountTicketResponse>;

Calls ProvisionAccountTicket.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IProvisionAccountTicketRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iprovisionaccountticketrequest)`   
ProvisionAccountTicketRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ProvisionAccountTicketResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.provisionaccountticketresponse)>` | Promise  
  
### runAccessReport(request, callback)
    
    
    public runAccessReport(request: google.analytics.admin.v1beta.IRunAccessReportRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.RunAccessReportCallback): void;

Calls RunAccessReport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunAccessReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportrequest)`   
RunAccessReportRequest message or plain object  
`callback` |  `[RunAccessReportCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and RunAccessReportResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runAccessReport(request)
    
    
    public runAccessReport(request: google.analytics.admin.v1beta.IRunAccessReportRequest): Promise<google.analytics.admin.v1beta.RunAccessReportResponse>;

Calls RunAccessReport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRunAccessReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.irunaccessreportrequest)`   
RunAccessReportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.RunAccessReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.runaccessreportresponse)>` | Promise  
  
### searchChangeHistoryEvents(request, callback)
    
    
    public searchChangeHistoryEvents(request: google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.SearchChangeHistoryEventsCallback): void;

Calls SearchChangeHistoryEvents.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsrequest)`   
SearchChangeHistoryEventsRequest message or plain object  
`callback` |  `[SearchChangeHistoryEventsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchChangeHistoryEventsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchChangeHistoryEvents(request)
    
    
    public searchChangeHistoryEvents(request: google.analytics.admin.v1beta.ISearchChangeHistoryEventsRequest): Promise<google.analytics.admin.v1beta.SearchChangeHistoryEventsResponse>;

Calls SearchChangeHistoryEvents.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchChangeHistoryEventsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.isearchchangehistoryeventsrequest)`   
SearchChangeHistoryEventsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.SearchChangeHistoryEventsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.searchchangehistoryeventsresponse)>` | Promise  
  
### updateAccount(request, callback)
    
    
    public updateAccount(request: google.analytics.admin.v1beta.IUpdateAccountRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.UpdateAccountCallback): void;

Calls UpdateAccount.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateaccountrequest)`   
UpdateAccountRequest message or plain object  
`callback` |  `[UpdateAccountCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Account  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAccount(request)
    
    
    public updateAccount(request: google.analytics.admin.v1beta.IUpdateAccountRequest): Promise<google.analytics.admin.v1beta.Account>;

Calls UpdateAccount.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccountRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateaccountrequest)`   
UpdateAccountRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.Account](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.account)>` | Promise  
  
### updateConversionEvent(request, callback)
    
    
    public updateConversionEvent(request: google.analytics.admin.v1beta.IUpdateConversionEventRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.UpdateConversionEventCallback): void;

Calls UpdateConversionEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateconversioneventrequest)`   
UpdateConversionEventRequest message or plain object  
`callback` |  `[UpdateConversionEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ConversionEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateConversionEvent(request)
    
    
    public updateConversionEvent(request: google.analytics.admin.v1beta.IUpdateConversionEventRequest): Promise<google.analytics.admin.v1beta.ConversionEvent>;

Calls UpdateConversionEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateConversionEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdateconversioneventrequest)`   
UpdateConversionEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.ConversionEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.conversionevent-class)>` | Promise  
  
### updateCustomDimension(request, callback)
    
    
    public updateCustomDimension(request: google.analytics.admin.v1beta.IUpdateCustomDimensionRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.UpdateCustomDimensionCallback): void;

Calls UpdateCustomDimension.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustomdimensionrequest)`   
UpdateCustomDimensionRequest message or plain object  
`callback` |  `[UpdateCustomDimensionCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomDimension  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomDimension(request)
    
    
    public updateCustomDimension(request: google.analytics.admin.v1beta.IUpdateCustomDimensionRequest): Promise<google.analytics.admin.v1beta.CustomDimension>;

Calls UpdateCustomDimension.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomDimensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustomdimensionrequest)`   
UpdateCustomDimensionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.CustomDimension](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.customdimension-class)>` | Promise  
  
### updateCustomMetric(request, callback)
    
    
    public updateCustomMetric(request: google.analytics.admin.v1beta.IUpdateCustomMetricRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.UpdateCustomMetricCallback): void;

Calls UpdateCustomMetric.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustommetricrequest)`   
UpdateCustomMetricRequest message or plain object  
`callback` |  `[UpdateCustomMetricCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and CustomMetric  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCustomMetric(request)
    
    
    public updateCustomMetric(request: google.analytics.admin.v1beta.IUpdateCustomMetricRequest): Promise<google.analytics.admin.v1beta.CustomMetric>;

Calls UpdateCustomMetric.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCustomMetricRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatecustommetricrequest)`   
UpdateCustomMetricRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.CustomMetric](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.custommetric-class)>` | Promise  
  
### updateDataRetentionSettings(request, callback)
    
    
    public updateDataRetentionSettings(request: google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.UpdateDataRetentionSettingsCallback): void;

Calls UpdateDataRetentionSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedataretentionsettingsrequest)`   
UpdateDataRetentionSettingsRequest message or plain object  
`callback` |  `[UpdateDataRetentionSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataRetentionSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataRetentionSettings(request)
    
    
    public updateDataRetentionSettings(request: google.analytics.admin.v1beta.IUpdateDataRetentionSettingsRequest): Promise<google.analytics.admin.v1beta.DataRetentionSettings>;

Calls UpdateDataRetentionSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataRetentionSettingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedataretentionsettingsrequest)`   
UpdateDataRetentionSettingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.DataRetentionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.dataretentionsettings-class)>` | Promise  
  
### updateDataStream(request, callback)
    
    
    public updateDataStream(request: google.analytics.admin.v1beta.IUpdateDataStreamRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.UpdateDataStreamCallback): void;

Calls UpdateDataStream.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedatastreamrequest)`   
UpdateDataStreamRequest message or plain object  
`callback` |  `[UpdateDataStreamCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DataStream  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataStream(request)
    
    
    public updateDataStream(request: google.analytics.admin.v1beta.IUpdateDataStreamRequest): Promise<google.analytics.admin.v1beta.DataStream>;

Calls UpdateDataStream.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataStreamRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatedatastreamrequest)`   
UpdateDataStreamRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.DataStream](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.datastream-class)>` | Promise  
  
### updateGoogleAdsLink(request, callback)
    
    
    public updateGoogleAdsLink(request: google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.UpdateGoogleAdsLinkCallback): void;

Calls UpdateGoogleAdsLink.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdategoogleadslinkrequest)`   
UpdateGoogleAdsLinkRequest message or plain object  
`callback` |  `[UpdateGoogleAdsLinkCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and GoogleAdsLink  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateGoogleAdsLink(request)
    
    
    public updateGoogleAdsLink(request: google.analytics.admin.v1beta.IUpdateGoogleAdsLinkRequest): Promise<google.analytics.admin.v1beta.GoogleAdsLink>;

Calls UpdateGoogleAdsLink.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateGoogleAdsLinkRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdategoogleadslinkrequest)`   
UpdateGoogleAdsLinkRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.GoogleAdsLink](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.googleadslink)>` | Promise  
  
### updateKeyEvent(request, callback)
    
    
    public updateKeyEvent(request: google.analytics.admin.v1beta.IUpdateKeyEventRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.UpdateKeyEventCallback): void;

Calls UpdateKeyEvent.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatekeyeventrequest)`   
UpdateKeyEventRequest message or plain object  
`callback` |  `[UpdateKeyEventCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and KeyEvent  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateKeyEvent(request)
    
    
    public updateKeyEvent(request: google.analytics.admin.v1beta.IUpdateKeyEventRequest): Promise<google.analytics.admin.v1beta.KeyEvent>;

Calls UpdateKeyEvent.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateKeyEventRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatekeyeventrequest)`   
UpdateKeyEventRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.KeyEvent](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.keyevent-class)>` | Promise  
  
### updateMeasurementProtocolSecret(request, callback)
    
    
    public updateMeasurementProtocolSecret(request: google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.UpdateMeasurementProtocolSecretCallback): void;

Calls UpdateMeasurementProtocolSecret.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatemeasurementprotocolsecretrequest)`   
UpdateMeasurementProtocolSecretRequest message or plain object  
`callback` |  `[UpdateMeasurementProtocolSecretCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and MeasurementProtocolSecret  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateMeasurementProtocolSecret(request)
    
    
    public updateMeasurementProtocolSecret(request: google.analytics.admin.v1beta.IUpdateMeasurementProtocolSecretRequest): Promise<google.analytics.admin.v1beta.MeasurementProtocolSecret>;

Calls UpdateMeasurementProtocolSecret.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateMeasurementProtocolSecretRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatemeasurementprotocolsecretrequest)`   
UpdateMeasurementProtocolSecretRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.MeasurementProtocolSecret](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.measurementprotocolsecret)>` | Promise  
  
### updateProperty(request, callback)
    
    
    public updateProperty(request: google.analytics.admin.v1beta.IUpdatePropertyRequest, callback: google.analytics.admin.v1beta.AnalyticsAdminService.UpdatePropertyCallback): void;

Calls UpdateProperty.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatepropertyrequest)`   
UpdatePropertyRequest message or plain object  
`callback` |  `[UpdatePropertyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Property  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateProperty(request)
    
    
    public updateProperty(request: google.analytics.admin.v1beta.IUpdatePropertyRequest): Promise<google.analytics.admin.v1beta.Property>;

Calls UpdateProperty.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePropertyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.iupdatepropertyrequest)`   
UpdatePropertyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.analytics.admin.v1beta.Property](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1beta.property)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
