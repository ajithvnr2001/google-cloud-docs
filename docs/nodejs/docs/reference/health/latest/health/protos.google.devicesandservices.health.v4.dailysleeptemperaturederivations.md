---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailysleeptemperaturederivations
title: Class protos.google.devicesandservices.health.v4.DailySleepTemperatureDerivations (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:12.199482+00:00
---

# Class protos.google.devicesandservices.health.v4.DailySleepTemperatureDerivations (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailysleeptemperaturederivations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.DailySleepTemperatureDerivations (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DailySleepTemperatureDerivations.

## Implements

[protos.google.devicesandservices.health.v4.IDailySleepTemperatureDerivations](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailysleeptemperaturederivations)

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devicesandservices.health.v4.IDailySleepTemperatureDerivations);

Constructs a new DailySleepTemperatureDerivations.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDailySleepTemperatureDerivations](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailysleeptemperaturederivations)`   
Properties to set  
  
## Properties 

### baselineTemperatureCelsius
    
    
    public baselineTemperatureCelsius?: (number|null);

DailySleepTemperatureDerivations baselineTemperatureCelsius.

### date
    
    
    public date?: (google.type.IDate|null);

DailySleepTemperatureDerivations date.

### nightlyTemperatureCelsius
    
    
    public nightlyTemperatureCelsius?: (number|null);

DailySleepTemperatureDerivations nightlyTemperatureCelsius.

### relativeNightlyStddev_30dCelsius
    
    
    public relativeNightlyStddev_30dCelsius?: (number|null);

DailySleepTemperatureDerivations relativeNightlyStddev_30dCelsius.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devicesandservices.health.v4.IDailySleepTemperatureDerivations): google.devicesandservices.health.v4.DailySleepTemperatureDerivations;

Creates a new DailySleepTemperatureDerivations instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDailySleepTemperatureDerivations](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailysleeptemperaturederivations)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DailySleepTemperatureDerivations](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailysleeptemperaturederivations)` | DailySleepTemperatureDerivations instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devicesandservices.health.v4.DailySleepTemperatureDerivations;

Decodes a DailySleepTemperatureDerivations message from the specified reader or buffer.

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
`[DailySleepTemperatureDerivations](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailysleeptemperaturederivations)` | DailySleepTemperatureDerivations  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devicesandservices.health.v4.DailySleepTemperatureDerivations;

Decodes a DailySleepTemperatureDerivations message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DailySleepTemperatureDerivations](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailysleeptemperaturederivations)` | DailySleepTemperatureDerivations  
  
### encode(message, writer)
    
    
    public static encode(message: google.devicesandservices.health.v4.IDailySleepTemperatureDerivations, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DailySleepTemperatureDerivations message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDailySleepTemperatureDerivations](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailysleeptemperaturederivations)`   
DailySleepTemperatureDerivations message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devicesandservices.health.v4.IDailySleepTemperatureDerivations, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DailySleepTemperatureDerivations message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDailySleepTemperatureDerivations](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.idailysleeptemperaturederivations)`   
DailySleepTemperatureDerivations message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devicesandservices.health.v4.DailySleepTemperatureDerivations;

Creates a DailySleepTemperatureDerivations message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DailySleepTemperatureDerivations](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailysleeptemperaturederivations)` | DailySleepTemperatureDerivations  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DailySleepTemperatureDerivations

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

Converts this DailySleepTemperatureDerivations to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devicesandservices.health.v4.DailySleepTemperatureDerivations, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DailySleepTemperatureDerivations message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DailySleepTemperatureDerivations](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.dailysleeptemperaturederivations)`   
DailySleepTemperatureDerivations  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DailySleepTemperatureDerivations message.

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
