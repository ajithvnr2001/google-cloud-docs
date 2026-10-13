---
url: https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.buildinginsights-class
title: Class protos.google.maps.solar.v1.BuildingInsights (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:20:32.102531+00:00
---

# Class protos.google.maps.solar.v1.BuildingInsights (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.buildinginsights-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.solar.v1.BuildingInsights (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.1.0 

Represents a BuildingInsights.

## Implements

[protos.google.maps.solar.v1.IBuildingInsights](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ibuildinginsights)

## Package

[@googlemaps/solar](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.solar.v1.IBuildingInsights);

Constructs a new BuildingInsights.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBuildingInsights](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ibuildinginsights)`   
Properties to set  
  
## Properties 

### administrativeArea
    
    
    public administrativeArea: string;

BuildingInsights administrativeArea.

### boundingBox
    
    
    public boundingBox?: (google.maps.solar.v1.ILatLngBox|null);

BuildingInsights boundingBox.

### center
    
    
    public center?: (google.type.ILatLng|null);

BuildingInsights center.

### detectedArrays
    
    
    public detectedArrays?: (google.maps.solar.v1.BuildingInsights.IDetectedArrays|null);

BuildingInsights detectedArrays.

### imageryDate
    
    
    public imageryDate?: (google.type.IDate|null);

BuildingInsights imageryDate.

### imageryProcessedDate
    
    
    public imageryProcessedDate?: (google.type.IDate|null);

BuildingInsights imageryProcessedDate.

### imageryQuality
    
    
    public imageryQuality: (google.maps.solar.v1.ImageryQuality|keyof typeof google.maps.solar.v1.ImageryQuality);

BuildingInsights imageryQuality.

### name
    
    
    public name: string;

BuildingInsights name.

### postalCode
    
    
    public postalCode: string;

BuildingInsights postalCode.

### regionCode
    
    
    public regionCode: string;

BuildingInsights regionCode.

### solarPotential
    
    
    public solarPotential?: (google.maps.solar.v1.ISolarPotential|null);

BuildingInsights solarPotential.

### statisticalArea
    
    
    public statisticalArea: string;

BuildingInsights statisticalArea.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.solar.v1.IBuildingInsights): google.maps.solar.v1.BuildingInsights;

Creates a new BuildingInsights instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBuildingInsights](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ibuildinginsights)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BuildingInsights](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.buildinginsights-class)` | BuildingInsights instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.solar.v1.BuildingInsights;

Decodes a BuildingInsights message from the specified reader or buffer.

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
`[BuildingInsights](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.buildinginsights-class)` | BuildingInsights  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.solar.v1.BuildingInsights;

Decodes a BuildingInsights message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BuildingInsights](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.buildinginsights-class)` | BuildingInsights  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.solar.v1.IBuildingInsights, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BuildingInsights message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBuildingInsights](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ibuildinginsights)`   
BuildingInsights message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.solar.v1.IBuildingInsights, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BuildingInsights message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBuildingInsights](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ibuildinginsights)`   
BuildingInsights message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.solar.v1.BuildingInsights;

Creates a BuildingInsights message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BuildingInsights](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.buildinginsights-class)` | BuildingInsights  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BuildingInsights

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

Converts this BuildingInsights to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.solar.v1.BuildingInsights, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BuildingInsights message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BuildingInsights](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.buildinginsights-class)`   
BuildingInsights  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BuildingInsights message.

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
