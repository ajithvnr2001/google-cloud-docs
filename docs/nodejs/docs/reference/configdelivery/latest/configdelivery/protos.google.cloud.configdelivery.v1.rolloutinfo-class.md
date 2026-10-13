---
url: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.rolloutinfo-class
title: Class protos.google.cloud.configdelivery.v1.RolloutInfo (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:31.059815+00:00
---

# Class protos.google.cloud.configdelivery.v1.RolloutInfo (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.rolloutinfo-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.configdelivery.v1.RolloutInfo (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a RolloutInfo.

## Implements

[protos.google.cloud.configdelivery.v1.IRolloutInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.irolloutinfo)

## Package

[@google-cloud/configdelivery](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.configdelivery.v1.IRolloutInfo);

Constructs a new RolloutInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRolloutInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.irolloutinfo)`   
Properties to set  
  
## Properties 

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

RolloutInfo endTime.

### message
    
    
    public message: string;

RolloutInfo message.

### rolloutStrategyInfo
    
    
    public rolloutStrategyInfo?: (google.cloud.configdelivery.v1.IRolloutStrategyInfo|null);

RolloutInfo rolloutStrategyInfo.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

RolloutInfo startTime.

### state
    
    
    public state: (google.cloud.configdelivery.v1.RolloutInfo.State|keyof typeof google.cloud.configdelivery.v1.RolloutInfo.State);

RolloutInfo state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.configdelivery.v1.IRolloutInfo): google.cloud.configdelivery.v1.RolloutInfo;

Creates a new RolloutInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRolloutInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.irolloutinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RolloutInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.rolloutinfo-class)` | RolloutInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.configdelivery.v1.RolloutInfo;

Decodes a RolloutInfo message from the specified reader or buffer.

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
`[RolloutInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.rolloutinfo-class)` | RolloutInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.configdelivery.v1.RolloutInfo;

Decodes a RolloutInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RolloutInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.rolloutinfo-class)` | RolloutInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.configdelivery.v1.IRolloutInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RolloutInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRolloutInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.irolloutinfo)`   
RolloutInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.configdelivery.v1.IRolloutInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RolloutInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRolloutInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.irolloutinfo)`   
RolloutInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.configdelivery.v1.RolloutInfo;

Creates a RolloutInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RolloutInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.rolloutinfo-class)` | RolloutInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RolloutInfo

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

Converts this RolloutInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.configdelivery.v1.RolloutInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RolloutInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RolloutInfo](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.rolloutinfo-class)`   
RolloutInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RolloutInfo message.

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
