---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.enhancedmeasurementsettings
title: Class protos.google.analytics.admin.v1alpha.EnhancedMeasurementSettings (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:42:43.793091+00:00
---

# Class protos.google.analytics.admin.v1alpha.EnhancedMeasurementSettings (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.enhancedmeasurementsettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.admin.v1alpha.EnhancedMeasurementSettings (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Represents an EnhancedMeasurementSettings.

## Implements

[protos.google.analytics.admin.v1alpha.IEnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ienhancedmeasurementsettings)

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.analytics.admin.v1alpha.IEnhancedMeasurementSettings);

Constructs a new EnhancedMeasurementSettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ienhancedmeasurementsettings)`   
Properties to set  
  
## Properties 

### fileDownloadsEnabled
    
    
    public fileDownloadsEnabled: boolean;

EnhancedMeasurementSettings fileDownloadsEnabled.

### formInteractionsEnabled
    
    
    public formInteractionsEnabled: boolean;

EnhancedMeasurementSettings formInteractionsEnabled.

### name
    
    
    public name: string;

EnhancedMeasurementSettings name.

### outboundClicksEnabled
    
    
    public outboundClicksEnabled: boolean;

EnhancedMeasurementSettings outboundClicksEnabled.

### pageChangesEnabled
    
    
    public pageChangesEnabled: boolean;

EnhancedMeasurementSettings pageChangesEnabled.

### scrollsEnabled
    
    
    public scrollsEnabled: boolean;

EnhancedMeasurementSettings scrollsEnabled.

### searchQueryParameter
    
    
    public searchQueryParameter: string;

EnhancedMeasurementSettings searchQueryParameter.

### siteSearchEnabled
    
    
    public siteSearchEnabled: boolean;

EnhancedMeasurementSettings siteSearchEnabled.

### streamEnabled
    
    
    public streamEnabled: boolean;

EnhancedMeasurementSettings streamEnabled.

### uriQueryParameter
    
    
    public uriQueryParameter: string;

EnhancedMeasurementSettings uriQueryParameter.

### videoEngagementEnabled
    
    
    public videoEngagementEnabled: boolean;

EnhancedMeasurementSettings videoEngagementEnabled.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.analytics.admin.v1alpha.IEnhancedMeasurementSettings): google.analytics.admin.v1alpha.EnhancedMeasurementSettings;

Creates a new EnhancedMeasurementSettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ienhancedmeasurementsettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.enhancedmeasurementsettings)` | EnhancedMeasurementSettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.analytics.admin.v1alpha.EnhancedMeasurementSettings;

Decodes an EnhancedMeasurementSettings message from the specified reader or buffer.

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
`[EnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.enhancedmeasurementsettings)` | EnhancedMeasurementSettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.analytics.admin.v1alpha.EnhancedMeasurementSettings;

Decodes an EnhancedMeasurementSettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.enhancedmeasurementsettings)` | EnhancedMeasurementSettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.analytics.admin.v1alpha.IEnhancedMeasurementSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EnhancedMeasurementSettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ienhancedmeasurementsettings)`   
EnhancedMeasurementSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.analytics.admin.v1alpha.IEnhancedMeasurementSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EnhancedMeasurementSettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.ienhancedmeasurementsettings)`   
EnhancedMeasurementSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.analytics.admin.v1alpha.EnhancedMeasurementSettings;

Creates an EnhancedMeasurementSettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.enhancedmeasurementsettings)` | EnhancedMeasurementSettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EnhancedMeasurementSettings

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

Converts this EnhancedMeasurementSettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.analytics.admin.v1alpha.EnhancedMeasurementSettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EnhancedMeasurementSettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EnhancedMeasurementSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.enhancedmeasurementsettings)`   
EnhancedMeasurementSettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EnhancedMeasurementSettings message.

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
