---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.channelprofile-class
title: Class protos.google.cloud.ces.v1.ChannelProfile (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:01.233919+00:00
---

# Class protos.google.cloud.ces.v1.ChannelProfile (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.channelprofile-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.ChannelProfile (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents a ChannelProfile.

## Implements

[protos.google.cloud.ces.v1.IChannelProfile](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ichannelprofile)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IChannelProfile);

Constructs a new ChannelProfile.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IChannelProfile](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ichannelprofile)`   
Properties to set  
  
## Properties 

### channelType
    
    
    public channelType: (google.cloud.ces.v1.ChannelProfile.ChannelType|keyof typeof google.cloud.ces.v1.ChannelProfile.ChannelType);

ChannelProfile channelType.

### disableBargeInControl
    
    
    public disableBargeInControl: boolean;

ChannelProfile disableBargeInControl.

### disableDtmf
    
    
    public disableDtmf: boolean;

ChannelProfile disableDtmf.

### instagramConfig
    
    
    public instagramConfig?: (google.cloud.ces.v1.ChannelProfile.IInstagramConfig|null);

ChannelProfile instagramConfig.

### noiseSuppressionLevel
    
    
    public noiseSuppressionLevel: string;

ChannelProfile noiseSuppressionLevel.

### personaProperty
    
    
    public personaProperty?: (google.cloud.ces.v1.ChannelProfile.IPersonaProperty|null);

ChannelProfile personaProperty.

### profileId
    
    
    public profileId: string;

ChannelProfile profileId.

### webWidgetConfig
    
    
    public webWidgetConfig?: (google.cloud.ces.v1.ChannelProfile.IWebWidgetConfig|null);

ChannelProfile webWidgetConfig.

### whatsappConfig
    
    
    public whatsappConfig?: (google.cloud.ces.v1.ChannelProfile.IWhatsAppConfig|null);

ChannelProfile whatsappConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IChannelProfile): google.cloud.ces.v1.ChannelProfile;

Creates a new ChannelProfile instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IChannelProfile](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ichannelprofile)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ChannelProfile](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.channelprofile-class)` | ChannelProfile instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.ChannelProfile;

Decodes a ChannelProfile message from the specified reader or buffer.

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
`[ChannelProfile](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.channelprofile-class)` | ChannelProfile  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.ChannelProfile;

Decodes a ChannelProfile message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ChannelProfile](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.channelprofile-class)` | ChannelProfile  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IChannelProfile, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ChannelProfile message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IChannelProfile](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ichannelprofile)`   
ChannelProfile message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IChannelProfile, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ChannelProfile message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IChannelProfile](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ichannelprofile)`   
ChannelProfile message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.ChannelProfile;

Creates a ChannelProfile message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ChannelProfile](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.channelprofile-class)` | ChannelProfile  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ChannelProfile

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

Converts this ChannelProfile to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.ChannelProfile, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ChannelProfile message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ChannelProfile](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.channelprofile-class)`   
ChannelProfile  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ChannelProfile message.

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
