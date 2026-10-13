---
url: https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.routetraveladvisory
title: Class protos.google.maps.routing.v2.RouteTravelAdvisory (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:22.257312+00:00
---

# Class protos.google.maps.routing.v2.RouteTravelAdvisory (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.routetraveladvisory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.routing.v2.RouteTravelAdvisory (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.2.0  1.4.0  0.3.1  0.2.1 

Represents a RouteTravelAdvisory.

## Implements

[protos.google.maps.routing.v2.IRouteTravelAdvisory](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.iroutetraveladvisory)

## Package

[@googlemaps/routing](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.routing.v2.IRouteTravelAdvisory);

Constructs a new RouteTravelAdvisory.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRouteTravelAdvisory](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.iroutetraveladvisory)`   
Properties to set  
  
## Properties 

### fuelConsumptionMicroliters
    
    
    public fuelConsumptionMicroliters: (number|Long|string);

RouteTravelAdvisory fuelConsumptionMicroliters.

### routeRestrictionsPartiallyIgnored
    
    
    public routeRestrictionsPartiallyIgnored: boolean;

RouteTravelAdvisory routeRestrictionsPartiallyIgnored.

### speedReadingIntervals
    
    
    public speedReadingIntervals: google.maps.routing.v2.ISpeedReadingInterval[];

RouteTravelAdvisory speedReadingIntervals.

### tollInfo
    
    
    public tollInfo?: (google.maps.routing.v2.ITollInfo|null);

RouteTravelAdvisory tollInfo.

### transitFare
    
    
    public transitFare?: (google.type.IMoney|null);

RouteTravelAdvisory transitFare.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.routing.v2.IRouteTravelAdvisory): google.maps.routing.v2.RouteTravelAdvisory;

Creates a new RouteTravelAdvisory instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRouteTravelAdvisory](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.iroutetraveladvisory)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RouteTravelAdvisory](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.routetraveladvisory)` | RouteTravelAdvisory instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.routing.v2.RouteTravelAdvisory;

Decodes a RouteTravelAdvisory message from the specified reader or buffer.

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
`[RouteTravelAdvisory](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.routetraveladvisory)` | RouteTravelAdvisory  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.routing.v2.RouteTravelAdvisory;

Decodes a RouteTravelAdvisory message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RouteTravelAdvisory](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.routetraveladvisory)` | RouteTravelAdvisory  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.routing.v2.IRouteTravelAdvisory, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RouteTravelAdvisory message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRouteTravelAdvisory](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.iroutetraveladvisory)`   
RouteTravelAdvisory message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.routing.v2.IRouteTravelAdvisory, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RouteTravelAdvisory message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRouteTravelAdvisory](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.iroutetraveladvisory)`   
RouteTravelAdvisory message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.routing.v2.RouteTravelAdvisory;

Creates a RouteTravelAdvisory message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RouteTravelAdvisory](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.routetraveladvisory)` | RouteTravelAdvisory  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RouteTravelAdvisory

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

Converts this RouteTravelAdvisory to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.routing.v2.RouteTravelAdvisory, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RouteTravelAdvisory message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RouteTravelAdvisory](https://docs.cloud.google.com/nodejs/docs/reference/routing/latest/routing/protos.google.maps.routing.v2.routetraveladvisory)`   
RouteTravelAdvisory  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RouteTravelAdvisory message.

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
