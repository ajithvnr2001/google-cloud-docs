---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.settings-class
title: Class protos.google.devicesandservices.health.v4.Settings (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:16.451276+00:00
---

# Class protos.google.devicesandservices.health.v4.Settings (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.settings-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.Settings (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Settings.

## Implements

[protos.google.devicesandservices.health.v4.ISettings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.isettings)

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devicesandservices.health.v4.ISettings);

Constructs a new Settings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISettings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.isettings)`   
Properties to set  
  
## Properties 

### autoStrideEnabled
    
    
    public autoStrideEnabled: boolean;

Settings autoStrideEnabled.

### distanceUnit
    
    
    public distanceUnit: (google.devicesandservices.health.v4.Settings.DistanceUnit|keyof typeof google.devicesandservices.health.v4.Settings.DistanceUnit);

Settings distanceUnit.

### foodLanguageCode
    
    
    public foodLanguageCode: string;

Settings foodLanguageCode.

### glucoseUnit
    
    
    public glucoseUnit: (google.devicesandservices.health.v4.Settings.GlucoseUnit|keyof typeof google.devicesandservices.health.v4.Settings.GlucoseUnit);

Settings glucoseUnit.

### heightUnit
    
    
    public heightUnit: (google.devicesandservices.health.v4.Settings.HeightUnit|keyof typeof google.devicesandservices.health.v4.Settings.HeightUnit);

Settings heightUnit.

### languageLocale
    
    
    public languageLocale: string;

Settings languageLocale.

### name
    
    
    public name: string;

Settings name.

### strideLengthRunningType
    
    
    public strideLengthRunningType: (google.devicesandservices.health.v4.Settings.StrideLengthType|keyof typeof google.devicesandservices.health.v4.Settings.StrideLengthType);

Settings strideLengthRunningType.

### strideLengthWalkingType
    
    
    public strideLengthWalkingType: (google.devicesandservices.health.v4.Settings.StrideLengthType|keyof typeof google.devicesandservices.health.v4.Settings.StrideLengthType);

Settings strideLengthWalkingType.

### swimUnit
    
    
    public swimUnit: (google.devicesandservices.health.v4.Settings.SwimUnit|keyof typeof google.devicesandservices.health.v4.Settings.SwimUnit);

Settings swimUnit.

### temperatureUnit
    
    
    public temperatureUnit: (google.devicesandservices.health.v4.Settings.TemperatureUnit|keyof typeof google.devicesandservices.health.v4.Settings.TemperatureUnit);

Settings temperatureUnit.

### timeZone
    
    
    public timeZone: string;

Settings timeZone.

### utcOffset
    
    
    public utcOffset?: (google.protobuf.IDuration|null);

Settings utcOffset.

### waterUnit
    
    
    public waterUnit: (google.devicesandservices.health.v4.Settings.WaterUnit|keyof typeof google.devicesandservices.health.v4.Settings.WaterUnit);

Settings waterUnit.

### weightUnit
    
    
    public weightUnit: (google.devicesandservices.health.v4.Settings.WeightUnit|keyof typeof google.devicesandservices.health.v4.Settings.WeightUnit);

Settings weightUnit.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devicesandservices.health.v4.ISettings): google.devicesandservices.health.v4.Settings;

Creates a new Settings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISettings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.isettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.settings-class)` | Settings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devicesandservices.health.v4.Settings;

Decodes a Settings message from the specified reader or buffer.

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
`[Settings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.settings-class)` | Settings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devicesandservices.health.v4.Settings;

Decodes a Settings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.settings-class)` | Settings  
  
### encode(message, writer)
    
    
    public static encode(message: google.devicesandservices.health.v4.ISettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Settings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISettings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.isettings)`   
Settings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devicesandservices.health.v4.ISettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Settings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISettings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.isettings)`   
Settings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devicesandservices.health.v4.Settings;

Creates a Settings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Settings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.settings-class)` | Settings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Settings

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

Converts this Settings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devicesandservices.health.v4.Settings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Settings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Settings](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.settings-class)`   
Settings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Settings message.

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
