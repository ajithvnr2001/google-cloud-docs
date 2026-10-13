---
url: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackageinfo-class
title: Class protos.google.cloud.configdelivery.v1beta.FleetPackageInfo (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:48.051374+00:00
---

# Class protos.google.cloud.configdelivery.v1beta.FleetPackageInfo (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackageinfo-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.configdelivery.v1beta.FleetPackageInfo (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a FleetPackageInfo.

## Implements

[protos.google.cloud.configdelivery.v1beta.IFleetPackageInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.ifleetpackageinfo)

## Package

[@google-cloud/configdelivery](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.configdelivery.v1beta.IFleetPackageInfo);

Constructs a new FleetPackageInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFleetPackageInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.ifleetpackageinfo)`   
Properties to set  
  
## Properties 

### activeRollout
    
    
    public activeRollout: string;

FleetPackageInfo activeRollout.

### errors
    
    
    public errors: google.cloud.configdelivery.v1beta.IFleetPackageError[];

FleetPackageInfo errors.

### lastCompletedRollout
    
    
    public lastCompletedRollout: string;

FleetPackageInfo lastCompletedRollout.

### state
    
    
    public state: (google.cloud.configdelivery.v1beta.FleetPackageInfo.State|keyof typeof google.cloud.configdelivery.v1beta.FleetPackageInfo.State);

FleetPackageInfo state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.configdelivery.v1beta.IFleetPackageInfo): google.cloud.configdelivery.v1beta.FleetPackageInfo;

Creates a new FleetPackageInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFleetPackageInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.ifleetpackageinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FleetPackageInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackageinfo-class)` | FleetPackageInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.configdelivery.v1beta.FleetPackageInfo;

Decodes a FleetPackageInfo message from the specified reader or buffer.

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
`[FleetPackageInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackageinfo-class)` | FleetPackageInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.configdelivery.v1beta.FleetPackageInfo;

Decodes a FleetPackageInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FleetPackageInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackageinfo-class)` | FleetPackageInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.configdelivery.v1beta.IFleetPackageInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FleetPackageInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFleetPackageInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.ifleetpackageinfo)`   
FleetPackageInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.configdelivery.v1beta.IFleetPackageInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FleetPackageInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFleetPackageInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.ifleetpackageinfo)`   
FleetPackageInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.configdelivery.v1beta.FleetPackageInfo;

Creates a FleetPackageInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FleetPackageInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackageinfo-class)` | FleetPackageInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FleetPackageInfo

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

Converts this FleetPackageInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.configdelivery.v1beta.FleetPackageInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FleetPackageInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FleetPackageInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1beta.fleetpackageinfo-class)`   
FleetPackageInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FleetPackageInfo message.

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
