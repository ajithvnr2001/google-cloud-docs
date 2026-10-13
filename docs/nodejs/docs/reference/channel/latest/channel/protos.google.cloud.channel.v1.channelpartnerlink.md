---
url: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerlink
title: Class protos.google.cloud.channel.v1.ChannelPartnerLink (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:15.006728+00:00
---

# Class protos.google.cloud.channel.v1.ChannelPartnerLink (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerlink

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.channel.v1.ChannelPartnerLink (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.2  3.6.0  3.2.1  3.0.0  2.5.1  2.4.1  2.2.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.6 

Represents a ChannelPartnerLink.

## Implements

[protos.google.cloud.channel.v1.IChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichannelpartnerlink)

## Package

[@google-cloud/channel](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.channel.v1.IChannelPartnerLink);

Constructs a new ChannelPartnerLink.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichannelpartnerlink)`   
Properties to set  
  
## Properties 

### channelPartnerCloudIdentityInfo
    
    
    public channelPartnerCloudIdentityInfo?: (google.cloud.channel.v1.ICloudIdentityInfo|null);

ChannelPartnerLink channelPartnerCloudIdentityInfo.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

ChannelPartnerLink createTime.

### inviteLinkUri
    
    
    public inviteLinkUri: string;

ChannelPartnerLink inviteLinkUri.

### linkState
    
    
    public linkState: (google.cloud.channel.v1.ChannelPartnerLinkState|keyof typeof google.cloud.channel.v1.ChannelPartnerLinkState);

ChannelPartnerLink linkState.

### name
    
    
    public name: string;

ChannelPartnerLink name.

### publicId
    
    
    public publicId: string;

ChannelPartnerLink publicId.

### resellerCloudIdentityId
    
    
    public resellerCloudIdentityId: string;

ChannelPartnerLink resellerCloudIdentityId.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

ChannelPartnerLink updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.channel.v1.IChannelPartnerLink): google.cloud.channel.v1.ChannelPartnerLink;

Creates a new ChannelPartnerLink instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichannelpartnerlink)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerlink)` | ChannelPartnerLink instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.channel.v1.ChannelPartnerLink;

Decodes a ChannelPartnerLink message from the specified reader or buffer.

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
`[ChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerlink)` | ChannelPartnerLink  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.channel.v1.ChannelPartnerLink;

Decodes a ChannelPartnerLink message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerlink)` | ChannelPartnerLink  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.channel.v1.IChannelPartnerLink, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ChannelPartnerLink message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichannelpartnerlink)`   
ChannelPartnerLink message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.channel.v1.IChannelPartnerLink, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ChannelPartnerLink message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ichannelpartnerlink)`   
ChannelPartnerLink message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.channel.v1.ChannelPartnerLink;

Creates a ChannelPartnerLink message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerlink)` | ChannelPartnerLink  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ChannelPartnerLink

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

Converts this ChannelPartnerLink to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.channel.v1.ChannelPartnerLink, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ChannelPartnerLink message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ChannelPartnerLink](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.channelpartnerlink)`   
ChannelPartnerLink  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ChannelPartnerLink message.

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
