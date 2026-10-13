---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.changehistoryresource
title: Class protos.google.analytics.admin.v1alpha.ChangeHistoryChange.ChangeHistoryResource (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:42:25.672240+00:00
---

# Class protos.google.analytics.admin.v1alpha.ChangeHistoryChange.ChangeHistoryResource (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.changehistoryresource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.admin.v1alpha.ChangeHistoryChange.ChangeHistoryResource (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Represents a ChangeHistoryResource.

## Implements

[protos.google.analytics.admin.v1alpha.ChangeHistoryChange.IChangeHistoryResource](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.ichangehistoryresource)

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.analytics.admin.v1alpha.ChangeHistoryChange.IChangeHistoryResource);

Constructs a new ChangeHistoryResource.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IChangeHistoryResource](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.ichangehistoryresource)`   
Properties to set  
  
## Properties 

### account
    
    
    public account?: (google.analytics.admin.v1alpha.IAccount|null);

ChangeHistoryResource account.

### adsenseLink
    
    
    public adsenseLink?: (google.analytics.admin.v1alpha.IAdSenseLink|null);

ChangeHistoryResource adsenseLink.

### attributionSettings
    
    
    public attributionSettings?: (google.analytics.admin.v1alpha.IAttributionSettings|null);

ChangeHistoryResource attributionSettings.

### audience
    
    
    public audience?: (google.analytics.admin.v1alpha.IAudience|null);

ChangeHistoryResource audience.

### bigqueryLink
    
    
    public bigqueryLink?: (google.analytics.admin.v1alpha.IBigQueryLink|null);

ChangeHistoryResource bigqueryLink.

### calculatedMetric
    
    
    public calculatedMetric?: (google.analytics.admin.v1alpha.ICalculatedMetric|null);

ChangeHistoryResource calculatedMetric.

### channelGroup
    
    
    public channelGroup?: (google.analytics.admin.v1alpha.IChannelGroup|null);

ChangeHistoryResource channelGroup.

### conversionEvent
    
    
    public conversionEvent?: (google.analytics.admin.v1alpha.IConversionEvent|null);

ChangeHistoryResource conversionEvent.

### customDimension
    
    
    public customDimension?: (google.analytics.admin.v1alpha.ICustomDimension|null);

ChangeHistoryResource customDimension.

### customMetric
    
    
    public customMetric?: (google.analytics.admin.v1alpha.ICustomMetric|null);

ChangeHistoryResource customMetric.

### dataRedactionSettings
    
    
    public dataRedactionSettings?: (google.analytics.admin.v1alpha.IDataRedactionSettings|null);

ChangeHistoryResource dataRedactionSettings.

### dataRetentionSettings
    
    
    public dataRetentionSettings?: (google.analytics.admin.v1alpha.IDataRetentionSettings|null);

ChangeHistoryResource dataRetentionSettings.

### dataStream
    
    
    public dataStream?: (google.analytics.admin.v1alpha.IDataStream|null);

ChangeHistoryResource dataStream.

### displayVideo_360AdvertiserLink
    
    
    public displayVideo_360AdvertiserLink?: (google.analytics.admin.v1alpha.IDisplayVideo360AdvertiserLink|null);

ChangeHistoryResource displayVideo_360AdvertiserLink.

### displayVideo_360AdvertiserLinkProposal
    
    
    public displayVideo_360AdvertiserLinkProposal?: (google.analytics.admin.v1alpha.IDisplayVideo360AdvertiserLinkProposal|null);

ChangeHistoryResource displayVideo_360AdvertiserLinkProposal.

### enhancedMeasurementSettings
    
    
    public enhancedMeasurementSettings?: (google.analytics.admin.v1alpha.IEnhancedMeasurementSettings|null);

ChangeHistoryResource enhancedMeasurementSettings.

### eventCreateRule
    
    
    public eventCreateRule?: (google.analytics.admin.v1alpha.IEventCreateRule|null);

ChangeHistoryResource eventCreateRule.

### expandedDataSet
    
    
    public expandedDataSet?: (google.analytics.admin.v1alpha.IExpandedDataSet|null);

ChangeHistoryResource expandedDataSet.

### firebaseLink
    
    
    public firebaseLink?: (google.analytics.admin.v1alpha.IFirebaseLink|null);

ChangeHistoryResource firebaseLink.

### googleAdsLink
    
    
    public googleAdsLink?: (google.analytics.admin.v1alpha.IGoogleAdsLink|null);

ChangeHistoryResource googleAdsLink.

### googleSignalsSettings
    
    
    public googleSignalsSettings?: (google.analytics.admin.v1alpha.IGoogleSignalsSettings|null);

ChangeHistoryResource googleSignalsSettings.

### keyEvent
    
    
    public keyEvent?: (google.analytics.admin.v1alpha.IKeyEvent|null);

ChangeHistoryResource keyEvent.

### measurementProtocolSecret
    
    
    public measurementProtocolSecret?: (google.analytics.admin.v1alpha.IMeasurementProtocolSecret|null);

ChangeHistoryResource measurementProtocolSecret.

### property
    
    
    public property?: (google.analytics.admin.v1alpha.IProperty|null);

ChangeHistoryResource property.

### reportingDataAnnotation
    
    
    public reportingDataAnnotation?: (google.analytics.admin.v1alpha.IReportingDataAnnotation|null);

ChangeHistoryResource reportingDataAnnotation.

### reportingIdentitySettings
    
    
    public reportingIdentitySettings?: (google.analytics.admin.v1alpha.IReportingIdentitySettings|null);

ChangeHistoryResource reportingIdentitySettings.

### resource
    
    
    public resource?: ("account"|"property"|"firebaseLink"|"googleAdsLink"|"googleSignalsSettings"|"displayVideo_360AdvertiserLink"|"displayVideo_360AdvertiserLinkProposal"|"conversionEvent"|"measurementProtocolSecret"|"customDimension"|"customMetric"|"dataRetentionSettings"|"searchAds_360Link"|"dataStream"|"attributionSettings"|"expandedDataSet"|"channelGroup"|"bigqueryLink"|"enhancedMeasurementSettings"|"dataRedactionSettings"|"skadnetworkConversionValueSchema"|"adsenseLink"|"audience"|"eventCreateRule"|"keyEvent"|"calculatedMetric"|"reportingDataAnnotation"|"subpropertySyncConfig"|"reportingIdentitySettings"|"userProvidedDataSettings");

ChangeHistoryResource resource.

### searchAds_360Link
    
    
    public searchAds_360Link?: (google.analytics.admin.v1alpha.ISearchAds360Link|null);

ChangeHistoryResource searchAds_360Link.

### skadnetworkConversionValueSchema
    
    
    public skadnetworkConversionValueSchema?: (google.analytics.admin.v1alpha.ISKAdNetworkConversionValueSchema|null);

ChangeHistoryResource skadnetworkConversionValueSchema.

### subpropertySyncConfig
    
    
    public subpropertySyncConfig?: (google.analytics.admin.v1alpha.ISubpropertySyncConfig|null);

ChangeHistoryResource subpropertySyncConfig.

### userProvidedDataSettings
    
    
    public userProvidedDataSettings?: (google.analytics.admin.v1alpha.IUserProvidedDataSettings|null);

ChangeHistoryResource userProvidedDataSettings.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.analytics.admin.v1alpha.ChangeHistoryChange.IChangeHistoryResource): google.analytics.admin.v1alpha.ChangeHistoryChange.ChangeHistoryResource;

Creates a new ChangeHistoryResource instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IChangeHistoryResource](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.ichangehistoryresource)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ChangeHistoryResource](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.changehistoryresource)` | ChangeHistoryResource instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.analytics.admin.v1alpha.ChangeHistoryChange.ChangeHistoryResource;

Decodes a ChangeHistoryResource message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[ChangeHistoryResource](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.changehistoryresource)` | ChangeHistoryResource  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.analytics.admin.v1alpha.ChangeHistoryChange.ChangeHistoryResource;

Decodes a ChangeHistoryResource message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ChangeHistoryResource](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.changehistoryresource)` | ChangeHistoryResource  
  
### encode(message, writer)
    
    
    public static encode(message: google.analytics.admin.v1alpha.ChangeHistoryChange.IChangeHistoryResource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ChangeHistoryResource message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IChangeHistoryResource](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.ichangehistoryresource)`   
ChangeHistoryResource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.analytics.admin.v1alpha.ChangeHistoryChange.IChangeHistoryResource, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ChangeHistoryResource message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IChangeHistoryResource](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.ichangehistoryresource)`   
ChangeHistoryResource message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.analytics.admin.v1alpha.ChangeHistoryChange.ChangeHistoryResource;

Creates a ChangeHistoryResource message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ChangeHistoryResource](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.changehistoryresource)` | ChangeHistoryResource  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ChangeHistoryResource

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this ChangeHistoryResource to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.analytics.admin.v1alpha.ChangeHistoryChange.ChangeHistoryResource, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ChangeHistoryResource message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ChangeHistoryResource](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.changehistorychange.changehistoryresource)`   
ChangeHistoryResource  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ChangeHistoryResource message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
