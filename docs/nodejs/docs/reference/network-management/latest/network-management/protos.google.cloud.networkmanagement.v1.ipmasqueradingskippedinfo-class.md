---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ipmasqueradingskippedinfo-class
title: Class protos.google.cloud.networkmanagement.v1.IpMasqueradingSkippedInfo (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:20.288339+00:00
---

# Class protos.google.cloud.networkmanagement.v1.IpMasqueradingSkippedInfo (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ipmasqueradingskippedinfo-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkmanagement.v1.IpMasqueradingSkippedInfo (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.2.0  4.2.0  3.11.0  3.10.0  3.9.0  3.7.0  3.3.0  3.0.0  2.4.2  2.3.1  2.2.0  1.1.2  1.0.2 

Represents an IpMasqueradingSkippedInfo.

## Implements

[protos.google.cloud.networkmanagement.v1.IIpMasqueradingSkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iipmasqueradingskippedinfo)

## Package

[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkmanagement.v1.IIpMasqueradingSkippedInfo);

Constructs a new IpMasqueradingSkippedInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIpMasqueradingSkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iipmasqueradingskippedinfo)`   
Properties to set  
  
## Properties 

### nonMasqueradeRange
    
    
    public nonMasqueradeRange: string;

IpMasqueradingSkippedInfo nonMasqueradeRange.

### reason
    
    
    public reason: (google.cloud.networkmanagement.v1.IpMasqueradingSkippedInfo.Reason|keyof typeof google.cloud.networkmanagement.v1.IpMasqueradingSkippedInfo.Reason);

IpMasqueradingSkippedInfo reason.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkmanagement.v1.IIpMasqueradingSkippedInfo): google.cloud.networkmanagement.v1.IpMasqueradingSkippedInfo;

Creates a new IpMasqueradingSkippedInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IIpMasqueradingSkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iipmasqueradingskippedinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[IpMasqueradingSkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ipmasqueradingskippedinfo-class)` | IpMasqueradingSkippedInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkmanagement.v1.IpMasqueradingSkippedInfo;

Decodes an IpMasqueradingSkippedInfo message from the specified reader or buffer.

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
`[IpMasqueradingSkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ipmasqueradingskippedinfo-class)` | IpMasqueradingSkippedInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkmanagement.v1.IpMasqueradingSkippedInfo;

Decodes an IpMasqueradingSkippedInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[IpMasqueradingSkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ipmasqueradingskippedinfo-class)` | IpMasqueradingSkippedInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkmanagement.v1.IIpMasqueradingSkippedInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IpMasqueradingSkippedInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIpMasqueradingSkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iipmasqueradingskippedinfo)`   
IpMasqueradingSkippedInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkmanagement.v1.IIpMasqueradingSkippedInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified IpMasqueradingSkippedInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IIpMasqueradingSkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.iipmasqueradingskippedinfo)`   
IpMasqueradingSkippedInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkmanagement.v1.IpMasqueradingSkippedInfo;

Creates an IpMasqueradingSkippedInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[IpMasqueradingSkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ipmasqueradingskippedinfo-class)` | IpMasqueradingSkippedInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for IpMasqueradingSkippedInfo

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

Converts this IpMasqueradingSkippedInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkmanagement.v1.IpMasqueradingSkippedInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an IpMasqueradingSkippedInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IpMasqueradingSkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.ipmasqueradingskippedinfo-class)`   
IpMasqueradingSkippedInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an IpMasqueradingSkippedInfo message.

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
