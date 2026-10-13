---
url: https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.durationlimit
title: Class protos.google.maps.routeoptimization.v1.Vehicle.DurationLimit (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:18.279150+00:00
---

# Class protos.google.maps.routeoptimization.v1.Vehicle.DurationLimit (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.durationlimit

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.routeoptimization.v1.Vehicle.DurationLimit (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.3.0  0.2.0  0.1.0 

Represents a DurationLimit.

## Implements

[protos.google.maps.routeoptimization.v1.Vehicle.IDurationLimit](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.idurationlimit)

## Package

[@googlemaps/routeoptimization](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.routeoptimization.v1.Vehicle.IDurationLimit);

Constructs a new DurationLimit.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDurationLimit](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.idurationlimit)`   
Properties to set  
  
## Properties 

### costPerHourAfterSoftMax
    
    
    public costPerHourAfterSoftMax?: (number|null);

DurationLimit costPerHourAfterSoftMax.

### costPerSquareHourAfterQuadraticSoftMax
    
    
    public costPerSquareHourAfterQuadraticSoftMax?: (number|null);

DurationLimit costPerSquareHourAfterQuadraticSoftMax.

### maxDuration
    
    
    public maxDuration?: (google.protobuf.IDuration|null);

DurationLimit maxDuration.

### quadraticSoftMaxDuration
    
    
    public quadraticSoftMaxDuration?: (google.protobuf.IDuration|null);

DurationLimit quadraticSoftMaxDuration.

### softMaxDuration
    
    
    public softMaxDuration?: (google.protobuf.IDuration|null);

DurationLimit softMaxDuration.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.routeoptimization.v1.Vehicle.IDurationLimit): google.maps.routeoptimization.v1.Vehicle.DurationLimit;

Creates a new DurationLimit instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDurationLimit](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.idurationlimit)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DurationLimit](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.durationlimit)` | DurationLimit instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.routeoptimization.v1.Vehicle.DurationLimit;

Decodes a DurationLimit message from the specified reader or buffer.

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
`[DurationLimit](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.durationlimit)` | DurationLimit  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.routeoptimization.v1.Vehicle.DurationLimit;

Decodes a DurationLimit message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DurationLimit](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.durationlimit)` | DurationLimit  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.routeoptimization.v1.Vehicle.IDurationLimit, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DurationLimit message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDurationLimit](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.idurationlimit)`   
DurationLimit message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.routeoptimization.v1.Vehicle.IDurationLimit, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DurationLimit message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDurationLimit](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.idurationlimit)`   
DurationLimit message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.routeoptimization.v1.Vehicle.DurationLimit;

Creates a DurationLimit message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DurationLimit](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.durationlimit)` | DurationLimit  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DurationLimit

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

Converts this DurationLimit to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.routeoptimization.v1.Vehicle.DurationLimit, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DurationLimit message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DurationLimit](https://docs.cloud.google.com/nodejs/docs/reference/routeoptimization/latest/routeoptimization/protos.google.maps.routeoptimization.v1.vehicle.durationlimit)`   
DurationLimit  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DurationLimit message.

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
