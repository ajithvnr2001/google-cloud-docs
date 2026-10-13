---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyoxygensaturation
title: Class protos.google.devicesandservices.health.v4.DailyOxygenSaturation (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:10.404834+00:00
---

# Class protos.google.devicesandservices.health.v4.DailyOxygenSaturation (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyoxygensaturation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.DailyOxygenSaturation (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DailyOxygenSaturation.

## Implements

[protos.google.devicesandservices.health.v4.IDailyOxygenSaturation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailyoxygensaturation)

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devicesandservices.health.v4.IDailyOxygenSaturation);

Constructs a new DailyOxygenSaturation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDailyOxygenSaturation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailyoxygensaturation)`   
Properties to set  
  
## Properties 

### averagePercentage
    
    
    public averagePercentage?: (number|null);

DailyOxygenSaturation averagePercentage.

### date
    
    
    public date?: (google.type.IDate|null);

DailyOxygenSaturation date.

### lowerBoundPercentage
    
    
    public lowerBoundPercentage?: (number|null);

DailyOxygenSaturation lowerBoundPercentage.

### standardDeviationPercentage
    
    
    public standardDeviationPercentage?: (number|null);

DailyOxygenSaturation standardDeviationPercentage.

### upperBoundPercentage
    
    
    public upperBoundPercentage?: (number|null);

DailyOxygenSaturation upperBoundPercentage.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devicesandservices.health.v4.IDailyOxygenSaturation): google.devicesandservices.health.v4.DailyOxygenSaturation;

Creates a new DailyOxygenSaturation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDailyOxygenSaturation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailyoxygensaturation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DailyOxygenSaturation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyoxygensaturation)` | DailyOxygenSaturation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devicesandservices.health.v4.DailyOxygenSaturation;

Decodes a DailyOxygenSaturation message from the specified reader or buffer.

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
`[DailyOxygenSaturation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyoxygensaturation)` | DailyOxygenSaturation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devicesandservices.health.v4.DailyOxygenSaturation;

Decodes a DailyOxygenSaturation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DailyOxygenSaturation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyoxygensaturation)` | DailyOxygenSaturation  
  
### encode(message, writer)
    
    
    public static encode(message: google.devicesandservices.health.v4.IDailyOxygenSaturation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DailyOxygenSaturation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDailyOxygenSaturation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailyoxygensaturation)`   
DailyOxygenSaturation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devicesandservices.health.v4.IDailyOxygenSaturation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DailyOxygenSaturation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDailyOxygenSaturation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailyoxygensaturation)`   
DailyOxygenSaturation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devicesandservices.health.v4.DailyOxygenSaturation;

Creates a DailyOxygenSaturation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DailyOxygenSaturation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyoxygensaturation)` | DailyOxygenSaturation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DailyOxygenSaturation

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

Converts this DailyOxygenSaturation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devicesandservices.health.v4.DailyOxygenSaturation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DailyOxygenSaturation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DailyOxygenSaturation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailyoxygensaturation)`   
DailyOxygenSaturation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DailyOxygenSaturation message.

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
