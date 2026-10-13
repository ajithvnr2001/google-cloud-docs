---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partneraudienceinfo-class
title: Class protos.google.ads.datamanager.v1.PartnerAudienceInfo (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:33.859003+00:00
---

# Class protos.google.ads.datamanager.v1.PartnerAudienceInfo (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partneraudienceinfo-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.PartnerAudienceInfo (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a PartnerAudienceInfo.

## Implements

[protos.google.ads.datamanager.v1.IPartnerAudienceInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ipartneraudienceinfo)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.datamanager.v1.IPartnerAudienceInfo);

Constructs a new PartnerAudienceInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPartnerAudienceInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ipartneraudienceinfo)`   
Properties to set  
  
## Properties 

### commercePartner
    
    
    public commercePartner?: (string|null);

PartnerAudienceInfo commercePartner.

### partnerAudienceSource
    
    
    public partnerAudienceSource?: (google.ads.datamanager.v1.PartnerAudienceInfo.PartnerAudienceSource|keyof typeof google.ads.datamanager.v1.PartnerAudienceInfo.PartnerAudienceSource|null);

PartnerAudienceInfo partnerAudienceSource.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.datamanager.v1.IPartnerAudienceInfo): google.ads.datamanager.v1.PartnerAudienceInfo;

Creates a new PartnerAudienceInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPartnerAudienceInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ipartneraudienceinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PartnerAudienceInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partneraudienceinfo-class)` | PartnerAudienceInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.datamanager.v1.PartnerAudienceInfo;

Decodes a PartnerAudienceInfo message from the specified reader or buffer.

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
`[PartnerAudienceInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partneraudienceinfo-class)` | PartnerAudienceInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.datamanager.v1.PartnerAudienceInfo;

Decodes a PartnerAudienceInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PartnerAudienceInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partneraudienceinfo-class)` | PartnerAudienceInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.datamanager.v1.IPartnerAudienceInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PartnerAudienceInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPartnerAudienceInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ipartneraudienceinfo)`   
PartnerAudienceInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.datamanager.v1.IPartnerAudienceInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PartnerAudienceInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPartnerAudienceInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.ipartneraudienceinfo)`   
PartnerAudienceInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.datamanager.v1.PartnerAudienceInfo;

Creates a PartnerAudienceInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PartnerAudienceInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partneraudienceinfo-class)` | PartnerAudienceInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PartnerAudienceInfo

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

Converts this PartnerAudienceInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.datamanager.v1.PartnerAudienceInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PartnerAudienceInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PartnerAudienceInfo](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.partneraudienceinfo-class)`   
PartnerAudienceInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PartnerAudienceInfo message.

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
