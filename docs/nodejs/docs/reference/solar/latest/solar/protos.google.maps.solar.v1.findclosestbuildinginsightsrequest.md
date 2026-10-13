---
url: https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.findclosestbuildinginsightsrequest
title: Class protos.google.maps.solar.v1.FindClosestBuildingInsightsRequest (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:20:33.384384+00:00
---

# Class protos.google.maps.solar.v1.FindClosestBuildingInsightsRequest (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.findclosestbuildinginsightsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.solar.v1.FindClosestBuildingInsightsRequest (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.1.0 

Represents a FindClosestBuildingInsightsRequest.

## Implements

[protos.google.maps.solar.v1.IFindClosestBuildingInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ifindclosestbuildinginsightsrequest)

## Package

[@googlemaps/solar](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.solar.v1.IFindClosestBuildingInsightsRequest);

Constructs a new FindClosestBuildingInsightsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFindClosestBuildingInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ifindclosestbuildinginsightsrequest)`   
Properties to set  
  
## Properties 

### additionalInsights
    
    
    public additionalInsights: google.maps.solar.v1.AdditionalInsights[];

FindClosestBuildingInsightsRequest additionalInsights.

### exactQualityRequired
    
    
    public exactQualityRequired: boolean;

FindClosestBuildingInsightsRequest exactQualityRequired.

### experiments
    
    
    public experiments: google.maps.solar.v1.Experiment[];

FindClosestBuildingInsightsRequest experiments.

### location
    
    
    public location?: (google.type.ILatLng|null);

FindClosestBuildingInsightsRequest location.

### requiredQuality
    
    
    public requiredQuality: (google.maps.solar.v1.ImageryQuality|keyof typeof google.maps.solar.v1.ImageryQuality);

FindClosestBuildingInsightsRequest requiredQuality.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.solar.v1.IFindClosestBuildingInsightsRequest): google.maps.solar.v1.FindClosestBuildingInsightsRequest;

Creates a new FindClosestBuildingInsightsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFindClosestBuildingInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ifindclosestbuildinginsightsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FindClosestBuildingInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.findclosestbuildinginsightsrequest)` | FindClosestBuildingInsightsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.solar.v1.FindClosestBuildingInsightsRequest;

Decodes a FindClosestBuildingInsightsRequest message from the specified reader or buffer.

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
`[FindClosestBuildingInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.findclosestbuildinginsightsrequest)` | FindClosestBuildingInsightsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.solar.v1.FindClosestBuildingInsightsRequest;

Decodes a FindClosestBuildingInsightsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FindClosestBuildingInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.findclosestbuildinginsightsrequest)` | FindClosestBuildingInsightsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.solar.v1.IFindClosestBuildingInsightsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FindClosestBuildingInsightsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFindClosestBuildingInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ifindclosestbuildinginsightsrequest)`   
FindClosestBuildingInsightsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.solar.v1.IFindClosestBuildingInsightsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FindClosestBuildingInsightsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFindClosestBuildingInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.ifindclosestbuildinginsightsrequest)`   
FindClosestBuildingInsightsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.solar.v1.FindClosestBuildingInsightsRequest;

Creates a FindClosestBuildingInsightsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FindClosestBuildingInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.findclosestbuildinginsightsrequest)` | FindClosestBuildingInsightsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FindClosestBuildingInsightsRequest

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

Converts this FindClosestBuildingInsightsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.solar.v1.FindClosestBuildingInsightsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FindClosestBuildingInsightsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FindClosestBuildingInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/solar/latest/solar/protos.google.maps.solar.v1.findclosestbuildinginsightsrequest)`   
FindClosestBuildingInsightsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FindClosestBuildingInsightsRequest message.

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
