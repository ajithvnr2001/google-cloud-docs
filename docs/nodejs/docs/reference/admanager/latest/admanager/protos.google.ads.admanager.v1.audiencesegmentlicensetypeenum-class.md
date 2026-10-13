---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegmentlicensetypeenum-class
title: Class protos.google.ads.admanager.v1.AudienceSegmentLicenseTypeEnum (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:50.200407+00:00
---

# Class protos.google.ads.admanager.v1.AudienceSegmentLicenseTypeEnum (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegmentlicensetypeenum-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.AudienceSegmentLicenseTypeEnum (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an AudienceSegmentLicenseTypeEnum.

## Implements

[protos.google.ads.admanager.v1.IAudienceSegmentLicenseTypeEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iaudiencesegmentlicensetypeenum)

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.admanager.v1.IAudienceSegmentLicenseTypeEnum);

Constructs a new AudienceSegmentLicenseTypeEnum.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAudienceSegmentLicenseTypeEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iaudiencesegmentlicensetypeenum)`   
Properties to set  
  
## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.admanager.v1.IAudienceSegmentLicenseTypeEnum): google.ads.admanager.v1.AudienceSegmentLicenseTypeEnum;

Creates a new AudienceSegmentLicenseTypeEnum instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAudienceSegmentLicenseTypeEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iaudiencesegmentlicensetypeenum)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegmentLicenseTypeEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegmentlicensetypeenum-class)` | AudienceSegmentLicenseTypeEnum instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.admanager.v1.AudienceSegmentLicenseTypeEnum;

Decodes an AudienceSegmentLicenseTypeEnum message from the specified reader or buffer.

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
`[AudienceSegmentLicenseTypeEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegmentlicensetypeenum-class)` | AudienceSegmentLicenseTypeEnum  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.admanager.v1.AudienceSegmentLicenseTypeEnum;

Decodes an AudienceSegmentLicenseTypeEnum message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegmentLicenseTypeEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegmentlicensetypeenum-class)` | AudienceSegmentLicenseTypeEnum  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.admanager.v1.IAudienceSegmentLicenseTypeEnum, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AudienceSegmentLicenseTypeEnum message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAudienceSegmentLicenseTypeEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iaudiencesegmentlicensetypeenum)`   
AudienceSegmentLicenseTypeEnum message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.admanager.v1.IAudienceSegmentLicenseTypeEnum, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AudienceSegmentLicenseTypeEnum message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAudienceSegmentLicenseTypeEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iaudiencesegmentlicensetypeenum)`   
AudienceSegmentLicenseTypeEnum message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.admanager.v1.AudienceSegmentLicenseTypeEnum;

Creates an AudienceSegmentLicenseTypeEnum message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegmentLicenseTypeEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegmentlicensetypeenum-class)` | AudienceSegmentLicenseTypeEnum  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AudienceSegmentLicenseTypeEnum

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

Converts this AudienceSegmentLicenseTypeEnum to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.admanager.v1.AudienceSegmentLicenseTypeEnum, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AudienceSegmentLicenseTypeEnum message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AudienceSegmentLicenseTypeEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegmentlicensetypeenum-class)`   
AudienceSegmentLicenseTypeEnum  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AudienceSegmentLicenseTypeEnum message.

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
