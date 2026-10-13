---
url: https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.solarpotential
title: Class protos.google.maps.solar.v1.SolarPotential (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:30.012984+00:00
---

# Class protos.google.maps.solar.v1.SolarPotential (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.solarpotential

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.solar.v1.SolarPotential (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.1.0 

Represents a SolarPotential.

## Implements

[protos.google.maps.solar.v1.ISolarPotential](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.isolarpotential)

## Package

[@googlemaps/solar](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.solar.v1.ISolarPotential);

Constructs a new SolarPotential.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISolarPotential](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.isolarpotential)`   
Properties to set  
  
## Properties 

### buildingStats
    
    
    public buildingStats?: (google.maps.solar.v1.ISizeAndSunshineStats|null);

SolarPotential buildingStats.

### carbonOffsetFactorKgPerMwh
    
    
    public carbonOffsetFactorKgPerMwh: number;

SolarPotential carbonOffsetFactorKgPerMwh.

### financialAnalyses
    
    
    public financialAnalyses: google.maps.solar.v1.IFinancialAnalysis[];

SolarPotential financialAnalyses.

### maxArrayAreaMeters2
    
    
    public maxArrayAreaMeters2: number;

SolarPotential maxArrayAreaMeters2.

### maxArrayPanelsCount
    
    
    public maxArrayPanelsCount: number;

SolarPotential maxArrayPanelsCount.

### maxSunshineHoursPerYear
    
    
    public maxSunshineHoursPerYear: number;

SolarPotential maxSunshineHoursPerYear.

### panelCapacityWatts
    
    
    public panelCapacityWatts: number;

SolarPotential panelCapacityWatts.

### panelHeightMeters
    
    
    public panelHeightMeters: number;

SolarPotential panelHeightMeters.

### panelLifetimeYears
    
    
    public panelLifetimeYears: number;

SolarPotential panelLifetimeYears.

### panelWidthMeters
    
    
    public panelWidthMeters: number;

SolarPotential panelWidthMeters.

### roofSegmentStats
    
    
    public roofSegmentStats: google.maps.solar.v1.IRoofSegmentSizeAndSunshineStats[];

SolarPotential roofSegmentStats.

### solarPanelConfigs
    
    
    public solarPanelConfigs: google.maps.solar.v1.ISolarPanelConfig[];

SolarPotential solarPanelConfigs.

### solarPanels
    
    
    public solarPanels: google.maps.solar.v1.ISolarPanel[];

SolarPotential solarPanels.

### wholeRoofStats
    
    
    public wholeRoofStats?: (google.maps.solar.v1.ISizeAndSunshineStats|null);

SolarPotential wholeRoofStats.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.solar.v1.ISolarPotential): google.maps.solar.v1.SolarPotential;

Creates a new SolarPotential instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISolarPotential](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.isolarpotential)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SolarPotential](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.solarpotential)` | SolarPotential instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.solar.v1.SolarPotential;

Decodes a SolarPotential message from the specified reader or buffer.

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
`[SolarPotential](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.solarpotential)` | SolarPotential  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.solar.v1.SolarPotential;

Decodes a SolarPotential message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SolarPotential](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.solarpotential)` | SolarPotential  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.solar.v1.ISolarPotential, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SolarPotential message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISolarPotential](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.isolarpotential)`   
SolarPotential message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.solar.v1.ISolarPotential, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SolarPotential message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISolarPotential](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.isolarpotential)`   
SolarPotential message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.solar.v1.SolarPotential;

Creates a SolarPotential message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SolarPotential](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.solarpotential)` | SolarPotential  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SolarPotential

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

Converts this SolarPotential to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.solar.v1.SolarPotential, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SolarPotential message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SolarPotential](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.solarpotential)`   
SolarPotential  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SolarPotential message.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
