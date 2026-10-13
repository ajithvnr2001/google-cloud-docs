---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.heartratezone
title: Class protos.google.devicesandservices.health.v4.DailyHeartRateZones.HeartRateZone (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:20.180295+00:00
---

# Class protos.google.devicesandservices.health.v4.DailyHeartRateZones.HeartRateZone (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.heartratezone

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.DailyHeartRateZones.HeartRateZone (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a HeartRateZone.

## Implements

[protos.google.devicesandservices.health.v4.DailyHeartRateZones.IHeartRateZone](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.iheartratezone)

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devicesandservices.health.v4.DailyHeartRateZones.IHeartRateZone);

Constructs a new HeartRateZone.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHeartRateZone](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.iheartratezone)`   
Properties to set  
  
## Properties 

### heartRateZoneType
    
    
    public heartRateZoneType: (google.devicesandservices.health.v4.HeartRateZoneType|keyof typeof google.devicesandservices.health.v4.HeartRateZoneType);

HeartRateZone heartRateZoneType.

### maxBeatsPerMinute
    
    
    public maxBeatsPerMinute?: (number|Long|string|null);

HeartRateZone maxBeatsPerMinute.

### minBeatsPerMinute
    
    
    public minBeatsPerMinute?: (number|Long|string|null);

HeartRateZone minBeatsPerMinute.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devicesandservices.health.v4.DailyHeartRateZones.IHeartRateZone): google.devicesandservices.health.v4.DailyHeartRateZones.HeartRateZone;

Creates a new HeartRateZone instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHeartRateZone](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.iheartratezone)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[HeartRateZone](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.heartratezone)` | HeartRateZone instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devicesandservices.health.v4.DailyHeartRateZones.HeartRateZone;

Decodes a HeartRateZone message from the specified reader or buffer.

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
`[HeartRateZone](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.heartratezone)` | HeartRateZone  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devicesandservices.health.v4.DailyHeartRateZones.HeartRateZone;

Decodes a HeartRateZone message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[HeartRateZone](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.heartratezone)` | HeartRateZone  
  
### encode(message, writer)
    
    
    public static encode(message: google.devicesandservices.health.v4.DailyHeartRateZones.IHeartRateZone, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HeartRateZone message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHeartRateZone](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.iheartratezone)`   
HeartRateZone message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devicesandservices.health.v4.DailyHeartRateZones.IHeartRateZone, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HeartRateZone message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHeartRateZone](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.iheartratezone)`   
HeartRateZone message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devicesandservices.health.v4.DailyHeartRateZones.HeartRateZone;

Creates a HeartRateZone message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[HeartRateZone](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.heartratezone)` | HeartRateZone  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for HeartRateZone

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

Converts this HeartRateZone to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devicesandservices.health.v4.DailyHeartRateZones.HeartRateZone, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a HeartRateZone message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[HeartRateZone](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyheartratezones.heartratezone)`   
HeartRateZone  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a HeartRateZone message.

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
