---
url: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.attributionsettings-class
title: Class protos.google.analytics.admin.v1alpha.AttributionSettings (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:42:19.279081+00:00
---

# Class protos.google.analytics.admin.v1alpha.AttributionSettings (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.attributionsettings-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.analytics.admin.v1alpha.AttributionSettings (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.1.0  9.2.0  7.6.0  7.3.0  4.6.0  4.5.1  4.4.0 

Represents an AttributionSettings.

## Implements

[protos.google.analytics.admin.v1alpha.IAttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iattributionsettings)

## Package

[@google-analytics/admin](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.analytics.admin.v1alpha.IAttributionSettings);

Constructs a new AttributionSettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iattributionsettings)`   
Properties to set  
  
## Properties 

### acquisitionConversionEventLookbackWindow
    
    
    public acquisitionConversionEventLookbackWindow: (google.analytics.admin.v1alpha.AttributionSettings.AcquisitionConversionEventLookbackWindow|keyof typeof google.analytics.admin.v1alpha.AttributionSettings.AcquisitionConversionEventLookbackWindow);

AttributionSettings acquisitionConversionEventLookbackWindow.

### adsWebConversionDataExportScope
    
    
    public adsWebConversionDataExportScope: (google.analytics.admin.v1alpha.AttributionSettings.AdsWebConversionDataExportScope|keyof typeof google.analytics.admin.v1alpha.AttributionSettings.AdsWebConversionDataExportScope);

AttributionSettings adsWebConversionDataExportScope.

### name
    
    
    public name: string;

AttributionSettings name.

### otherConversionEventLookbackWindow
    
    
    public otherConversionEventLookbackWindow: (google.analytics.admin.v1alpha.AttributionSettings.OtherConversionEventLookbackWindow|keyof typeof google.analytics.admin.v1alpha.AttributionSettings.OtherConversionEventLookbackWindow);

AttributionSettings otherConversionEventLookbackWindow.

### reportingAttributionModel
    
    
    public reportingAttributionModel: (google.analytics.admin.v1alpha.AttributionSettings.ReportingAttributionModel|keyof typeof google.analytics.admin.v1alpha.AttributionSettings.ReportingAttributionModel);

AttributionSettings reportingAttributionModel.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.analytics.admin.v1alpha.IAttributionSettings): google.analytics.admin.v1alpha.AttributionSettings;

Creates a new AttributionSettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iattributionsettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.attributionsettings-class)` | AttributionSettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.analytics.admin.v1alpha.AttributionSettings;

Decodes an AttributionSettings message from the specified reader or buffer.

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
`[AttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.attributionsettings-class)` | AttributionSettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.analytics.admin.v1alpha.AttributionSettings;

Decodes an AttributionSettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.attributionsettings-class)` | AttributionSettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.analytics.admin.v1alpha.IAttributionSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AttributionSettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iattributionsettings)`   
AttributionSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.analytics.admin.v1alpha.IAttributionSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AttributionSettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.iattributionsettings)`   
AttributionSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.analytics.admin.v1alpha.AttributionSettings;

Creates an AttributionSettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.attributionsettings-class)` | AttributionSettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AttributionSettings

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

Converts this AttributionSettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.analytics.admin.v1alpha.AttributionSettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AttributionSettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AttributionSettings](https://docs.cloud.google.com/nodejs/docs/reference/admin/latest/admin/protos.google.analytics.admin.v1alpha.attributionsettings-class)`   
AttributionSettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AttributionSettings message.

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
