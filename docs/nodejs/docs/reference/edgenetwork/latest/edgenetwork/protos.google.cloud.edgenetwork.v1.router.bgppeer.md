---
url: https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.bgppeer
title: Class protos.google.cloud.edgenetwork.v1.Router.BgpPeer (0.13.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:47.068414+00:00
---

# Class protos.google.cloud.edgenetwork.v1.Router.BgpPeer (0.13.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.bgppeer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.edgenetwork.v1.Router.BgpPeer (0.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.1 (latest)  0.9.0  0.7.1  0.6.0  0.4.0  0.2.0  0.1.0 

Represents a BgpPeer.

## Implements

[protos.google.cloud.edgenetwork.v1.Router.IBgpPeer](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.ibgppeer)

## Package

[@google-cloud/edgenetwork](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.edgenetwork.v1.Router.IBgpPeer);

Constructs a new BgpPeer.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBgpPeer](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.ibgppeer)`   
Properties to set  
  
## Properties 

### interface
    
    
    public interface: string;

BgpPeer interface.

### interfaceIpv4Cidr
    
    
    public interfaceIpv4Cidr: string;

BgpPeer interfaceIpv4Cidr.

### interfaceIpv6Cidr
    
    
    public interfaceIpv6Cidr: string;

BgpPeer interfaceIpv6Cidr.

### localAsn
    
    
    public localAsn: number;

BgpPeer localAsn.

### name
    
    
    public name: string;

BgpPeer name.

### peerAsn
    
    
    public peerAsn: number;

BgpPeer peerAsn.

### peerIpv4Cidr
    
    
    public peerIpv4Cidr: string;

BgpPeer peerIpv4Cidr.

### peerIpv6Cidr
    
    
    public peerIpv6Cidr: string;

BgpPeer peerIpv6Cidr.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.edgenetwork.v1.Router.IBgpPeer): google.cloud.edgenetwork.v1.Router.BgpPeer;

Creates a new BgpPeer instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBgpPeer](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.ibgppeer)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BgpPeer](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.bgppeer)` | BgpPeer instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.edgenetwork.v1.Router.BgpPeer;

Decodes a BgpPeer message from the specified reader or buffer.

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
`[BgpPeer](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.bgppeer)` | BgpPeer  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.edgenetwork.v1.Router.BgpPeer;

Decodes a BgpPeer message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BgpPeer](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.bgppeer)` | BgpPeer  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.edgenetwork.v1.Router.IBgpPeer, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BgpPeer message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBgpPeer](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.ibgppeer)`   
BgpPeer message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.edgenetwork.v1.Router.IBgpPeer, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BgpPeer message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBgpPeer](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.ibgppeer)`   
BgpPeer message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.edgenetwork.v1.Router.BgpPeer;

Creates a BgpPeer message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BgpPeer](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.bgppeer)` | BgpPeer  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BgpPeer

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

Converts this BgpPeer to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.edgenetwork.v1.Router.BgpPeer, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BgpPeer message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BgpPeer](https://docs.cloud.google.com/nodejs/docs/reference/edgenetwork/latest/edgenetwork/protos.google.cloud.edgenetwork.v1.router.bgppeer)`   
BgpPeer  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BgpPeer message.

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
