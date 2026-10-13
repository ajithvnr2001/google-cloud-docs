---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.gkenetworkpolicyskippedinfo-class
title: Class protos.google.cloud.networkmanagement.v1.GkeNetworkPolicySkippedInfo (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:19.553618+00:00
---

# Class protos.google.cloud.networkmanagement.v1.GkeNetworkPolicySkippedInfo (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.gkenetworkpolicyskippedinfo-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkmanagement.v1.GkeNetworkPolicySkippedInfo (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.2.0  4.2.0  3.11.0  3.10.0  3.9.0  3.7.0  3.3.0  3.0.0  2.4.2  2.3.1  2.2.0  1.1.2  1.0.2 

Represents a GkeNetworkPolicySkippedInfo.

## Implements

[protos.google.cloud.networkmanagement.v1.IGkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.igkenetworkpolicyskippedinfo)

## Package

[@google-cloud/network-management](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkmanagement.v1.IGkeNetworkPolicySkippedInfo);

Constructs a new GkeNetworkPolicySkippedInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.igkenetworkpolicyskippedinfo)`   
Properties to set  
  
## Properties 

### reason
    
    
    public reason: (google.cloud.networkmanagement.v1.GkeNetworkPolicySkippedInfo.Reason|keyof typeof google.cloud.networkmanagement.v1.GkeNetworkPolicySkippedInfo.Reason);

GkeNetworkPolicySkippedInfo reason.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkmanagement.v1.IGkeNetworkPolicySkippedInfo): google.cloud.networkmanagement.v1.GkeNetworkPolicySkippedInfo;

Creates a new GkeNetworkPolicySkippedInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.igkenetworkpolicyskippedinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.gkenetworkpolicyskippedinfo-class)` | GkeNetworkPolicySkippedInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkmanagement.v1.GkeNetworkPolicySkippedInfo;

Decodes a GkeNetworkPolicySkippedInfo message from the specified reader or buffer.

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
`[GkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.gkenetworkpolicyskippedinfo-class)` | GkeNetworkPolicySkippedInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkmanagement.v1.GkeNetworkPolicySkippedInfo;

Decodes a GkeNetworkPolicySkippedInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.gkenetworkpolicyskippedinfo-class)` | GkeNetworkPolicySkippedInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkmanagement.v1.IGkeNetworkPolicySkippedInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GkeNetworkPolicySkippedInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.igkenetworkpolicyskippedinfo)`   
GkeNetworkPolicySkippedInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkmanagement.v1.IGkeNetworkPolicySkippedInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GkeNetworkPolicySkippedInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.igkenetworkpolicyskippedinfo)`   
GkeNetworkPolicySkippedInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkmanagement.v1.GkeNetworkPolicySkippedInfo;

Creates a GkeNetworkPolicySkippedInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.gkenetworkpolicyskippedinfo-class)` | GkeNetworkPolicySkippedInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GkeNetworkPolicySkippedInfo

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

Converts this GkeNetworkPolicySkippedInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkmanagement.v1.GkeNetworkPolicySkippedInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GkeNetworkPolicySkippedInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/nodejs/docs/reference/network-management/latest/network-management/protos.google.cloud.networkmanagement.v1.gkenetworkpolicyskippedinfo-class)`   
GkeNetworkPolicySkippedInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GkeNetworkPolicySkippedInfo message.

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
