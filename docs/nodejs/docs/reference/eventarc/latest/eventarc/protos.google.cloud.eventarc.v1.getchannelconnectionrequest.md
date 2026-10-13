---
url: https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.getchannelconnectionrequest
title: Class protos.google.cloud.eventarc.v1.GetChannelConnectionRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:59:50.151374+00:00
---

# Class protos.google.cloud.eventarc.v1.GetChannelConnectionRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.getchannelconnectionrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.eventarc.v1.GetChannelConnectionRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.3.0  4.1.0  4.0.1  3.2.0  2.3.2  2.2.0  2.1.1  1.2.0  1.1.2  1.0.3 

Represents a GetChannelConnectionRequest.

## Implements

[protos.google.cloud.eventarc.v1.IGetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetchannelconnectionrequest)

## Package

[@google-cloud/eventarc](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.eventarc.v1.IGetChannelConnectionRequest);

Constructs a new GetChannelConnectionRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetchannelconnectionrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

GetChannelConnectionRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.eventarc.v1.IGetChannelConnectionRequest): google.cloud.eventarc.v1.GetChannelConnectionRequest;

Creates a new GetChannelConnectionRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetchannelconnectionrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.getchannelconnectionrequest)` | GetChannelConnectionRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.eventarc.v1.GetChannelConnectionRequest;

Decodes a GetChannelConnectionRequest message from the specified reader or buffer.

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
`[GetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.getchannelconnectionrequest)` | GetChannelConnectionRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.eventarc.v1.GetChannelConnectionRequest;

Decodes a GetChannelConnectionRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.getchannelconnectionrequest)` | GetChannelConnectionRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.eventarc.v1.IGetChannelConnectionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetChannelConnectionRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetchannelconnectionrequest)`   
GetChannelConnectionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.eventarc.v1.IGetChannelConnectionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetChannelConnectionRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.igetchannelconnectionrequest)`   
GetChannelConnectionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.eventarc.v1.GetChannelConnectionRequest;

Creates a GetChannelConnectionRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.getchannelconnectionrequest)` | GetChannelConnectionRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GetChannelConnectionRequest

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

Converts this GetChannelConnectionRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.eventarc.v1.GetChannelConnectionRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GetChannelConnectionRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GetChannelConnectionRequest](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.getchannelconnectionrequest)`   
GetChannelConnectionRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GetChannelConnectionRequest message.

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
