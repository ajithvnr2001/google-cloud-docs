---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.spokestatereasoncount
title: Class protos.google.cloud.networkconnectivity.v1.SpokeSummary.SpokeStateReasonCount (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:19.133308+00:00
---

# Class protos.google.cloud.networkconnectivity.v1.SpokeSummary.SpokeStateReasonCount (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.spokestatereasoncount

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkconnectivity.v1.SpokeSummary.SpokeStateReasonCount (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.6.0  4.2.0  3.6.0  3.2.0  2.3.3  2.2.0  2.1.2  1.5.0  1.4.2  1.3.0  1.2.1  1.1.6 

Represents a SpokeStateReasonCount.

## Implements

[protos.google.cloud.networkconnectivity.v1.SpokeSummary.ISpokeStateReasonCount](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.ispokestatereasoncount)

## Package

[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkconnectivity.v1.SpokeSummary.ISpokeStateReasonCount);

Constructs a new SpokeStateReasonCount.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISpokeStateReasonCount](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.ispokestatereasoncount)`   
Properties to set  
  
## Properties 

### count
    
    
    public count: (number|Long|string);

SpokeStateReasonCount count.

### stateReasonCode
    
    
    public stateReasonCode: (google.cloud.networkconnectivity.v1.Spoke.StateReason.Code|keyof typeof google.cloud.networkconnectivity.v1.Spoke.StateReason.Code);

SpokeStateReasonCount stateReasonCode.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkconnectivity.v1.SpokeSummary.ISpokeStateReasonCount): google.cloud.networkconnectivity.v1.SpokeSummary.SpokeStateReasonCount;

Creates a new SpokeStateReasonCount instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISpokeStateReasonCount](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.ispokestatereasoncount)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SpokeStateReasonCount](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.spokestatereasoncount)` | SpokeStateReasonCount instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkconnectivity.v1.SpokeSummary.SpokeStateReasonCount;

Decodes a SpokeStateReasonCount message from the specified reader or buffer.

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
`[SpokeStateReasonCount](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.spokestatereasoncount)` | SpokeStateReasonCount  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkconnectivity.v1.SpokeSummary.SpokeStateReasonCount;

Decodes a SpokeStateReasonCount message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SpokeStateReasonCount](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.spokestatereasoncount)` | SpokeStateReasonCount  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkconnectivity.v1.SpokeSummary.ISpokeStateReasonCount, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SpokeStateReasonCount message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISpokeStateReasonCount](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.ispokestatereasoncount)`   
SpokeStateReasonCount message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkconnectivity.v1.SpokeSummary.ISpokeStateReasonCount, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SpokeStateReasonCount message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISpokeStateReasonCount](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.ispokestatereasoncount)`   
SpokeStateReasonCount message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkconnectivity.v1.SpokeSummary.SpokeStateReasonCount;

Creates a SpokeStateReasonCount message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SpokeStateReasonCount](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.spokestatereasoncount)` | SpokeStateReasonCount  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SpokeStateReasonCount

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

Converts this SpokeStateReasonCount to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkconnectivity.v1.SpokeSummary.SpokeStateReasonCount, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SpokeStateReasonCount message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SpokeStateReasonCount](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1.spokesummary.spokestatereasoncount)`   
SpokeStateReasonCount  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SpokeStateReasonCount message.

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
