---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegment-class
title: Class protos.google.ads.admanager.v1.AudienceSegment (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:48.976051+00:00
---

# Class protos.google.ads.admanager.v1.AudienceSegment (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegment-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.AudienceSegment (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an AudienceSegment.

## Implements

[protos.google.ads.admanager.v1.IAudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iaudiencesegment)

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.admanager.v1.IAudienceSegment);

Constructs a new AudienceSegment.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iaudiencesegment)`   
Properties to set  
  
## Properties 

### adIdSize
    
    
    public adIdSize?: (number|Long|string|null);

AudienceSegment adIdSize.

### categoryIds
    
    
    public categoryIds: (number|Long|string)[];

AudienceSegment categoryIds.

### dataProviderDisplayName
    
    
    public dataProviderDisplayName?: (string|null);

AudienceSegment dataProviderDisplayName.

### description
    
    
    public description?: (string|null);

AudienceSegment description.

### displayName
    
    
    public displayName?: (string|null);

AudienceSegment displayName.

### idfaSize
    
    
    public idfaSize?: (number|Long|string|null);

AudienceSegment idfaSize.

### mobileWebSize
    
    
    public mobileWebSize?: (number|Long|string|null);

AudienceSegment mobileWebSize.

### name
    
    
    public name: string;

AudienceSegment name.

### nonRuleBasedFirstPartyAudienceSegment
    
    
    public nonRuleBasedFirstPartyAudienceSegment?: (google.ads.admanager.v1.AudienceSegment.INonRuleBasedFirstPartyAudienceSegment|null);

AudienceSegment nonRuleBasedFirstPartyAudienceSegment.

### ppidSize
    
    
    public ppidSize?: (number|Long|string|null);

AudienceSegment ppidSize.

### ruleBasedFirstPartyAudienceSegment
    
    
    public ruleBasedFirstPartyAudienceSegment?: (google.ads.admanager.v1.AudienceSegment.IRuleBasedFirstPartyAudienceSegment|null);

AudienceSegment ruleBasedFirstPartyAudienceSegment.

### segmentType
    
    
    public segmentType?: (google.ads.admanager.v1.AudienceSegmentTypeEnum.AudienceSegmentType|keyof typeof google.ads.admanager.v1.AudienceSegmentTypeEnum.AudienceSegmentType|null);

AudienceSegment segmentType.

### sharedId
    
    
    public sharedId: (number|Long|string);

AudienceSegment sharedId.

### size
    
    
    public size?: (number|Long|string|null);

AudienceSegment size.

### status
    
    
    public status?: (google.ads.admanager.v1.AudienceSegmentStatusEnum.AudienceSegmentStatus|keyof typeof google.ads.admanager.v1.AudienceSegmentStatusEnum.AudienceSegmentStatus|null);

AudienceSegment status.

### subType
    
    
    public subType?: ("nonRuleBasedFirstPartyAudienceSegment"|"ruleBasedFirstPartyAudienceSegment"|"thirdPartyAudienceSegment");

AudienceSegment subType.

### thirdPartyAudienceSegment
    
    
    public thirdPartyAudienceSegment?: (google.ads.admanager.v1.AudienceSegment.IThirdPartyAudienceSegment|null);

AudienceSegment thirdPartyAudienceSegment.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.admanager.v1.IAudienceSegment): google.ads.admanager.v1.AudienceSegment;

Creates a new AudienceSegment instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iaudiencesegment)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegment-class)` | AudienceSegment instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.admanager.v1.AudienceSegment;

Decodes an AudienceSegment message from the specified reader or buffer.

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
`[AudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegment-class)` | AudienceSegment  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.admanager.v1.AudienceSegment;

Decodes an AudienceSegment message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegment-class)` | AudienceSegment  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.admanager.v1.IAudienceSegment, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AudienceSegment message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iaudiencesegment)`   
AudienceSegment message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.admanager.v1.IAudienceSegment, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AudienceSegment message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iaudiencesegment)`   
AudienceSegment message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.admanager.v1.AudienceSegment;

Creates an AudienceSegment message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegment-class)` | AudienceSegment  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AudienceSegment

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

Converts this AudienceSegment to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.admanager.v1.AudienceSegment, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AudienceSegment message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AudienceSegment](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.audiencesegment-class)`   
AudienceSegment  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AudienceSegment message.

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
