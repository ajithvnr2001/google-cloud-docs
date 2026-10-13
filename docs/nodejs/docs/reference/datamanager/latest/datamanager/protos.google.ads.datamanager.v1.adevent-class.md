---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adevent-class
title: Class protos.google.ads.datamanager.v1.AdEvent (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:19.854521+00:00
---

# Class protos.google.ads.datamanager.v1.AdEvent (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adevent-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.AdEvent (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents an AdEvent.

## Implements

[protos.google.ads.datamanager.v1.IAdEvent](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iadevent)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.datamanager.v1.IAdEvent);

Constructs a new AdEvent.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdEvent](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iadevent)`   
Properties to set  
  
## Properties 

### adFormat
    
    
    public adFormat?: (google.ads.datamanager.v1.AdFormat|keyof typeof google.ads.datamanager.v1.AdFormat|null);

AdEvent adFormat.

### adFormatOneof
    
    
    public adFormatOneof?: ("adFormat"|"adFormatString");

AdEvent adFormatOneof.

### adFormatString
    
    
    public adFormatString?: (string|null);

AdEvent adFormatString.

### adGroupId
    
    
    public adGroupId: string;

AdEvent adGroupId.

### adHeight
    
    
    public adHeight: number;

AdEvent adHeight.

### adId
    
    
    public adId: string;

AdEvent adId.

### adPlacement
    
    
    public adPlacement?: (google.ads.datamanager.v1.AdPlacement|keyof typeof google.ads.datamanager.v1.AdPlacement|null);

AdEvent adPlacement.

### adPlacementOneof
    
    
    public adPlacementOneof?: ("adPlacement"|"adPlacementString");

AdEvent adPlacementOneof.

### adPlacementString
    
    
    public adPlacementString?: (string|null);

AdEvent adPlacementString.

### adType
    
    
    public adType?: (google.ads.datamanager.v1.AdType|keyof typeof google.ads.datamanager.v1.AdType|null);

AdEvent adType.

### adTypeOneof
    
    
    public adTypeOneof?: ("adType"|"adTypeString");

AdEvent adTypeOneof.

### adTypeString
    
    
    public adTypeString?: (string|null);

AdEvent adTypeString.

### advertiserId
    
    
    public advertiserId: string;

AdEvent advertiserId.

### adWidth
    
    
    public adWidth: number;

AdEvent adWidth.

### attributionHint
    
    
    public attributionHint: (google.ads.datamanager.v1.AttributionHint|keyof typeof google.ads.datamanager.v1.AttributionHint);

AdEvent attributionHint.

### campaignId
    
    
    public campaignId: string;

AdEvent campaignId.

### campaignName
    
    
    public campaignName: string;

AdEvent campaignName.

### deviceInfo
    
    
    public deviceInfo?: (google.ads.datamanager.v1.IDeviceInfo|null);

AdEvent deviceInfo.

### eventId
    
    
    public eventId: string;

AdEvent eventId.

### eventSubtype
    
    
    public eventSubtype?: (google.ads.datamanager.v1.AdEvent.EventSubtype|keyof typeof google.ads.datamanager.v1.AdEvent.EventSubtype|null);

AdEvent eventSubtype.

### eventSubtypeOneof
    
    
    public eventSubtypeOneof?: ("eventSubtype"|"eventSubtypeString");

AdEvent eventSubtypeOneof.

### eventSubtypeString
    
    
    public eventSubtypeString?: (string|null);

AdEvent eventSubtypeString.

### eventType
    
    
    public eventType: (google.ads.datamanager.v1.AdEvent.EventType|keyof typeof google.ads.datamanager.v1.AdEvent.EventType);

AdEvent eventType.

### measurementAllowed
    
    
    public measurementAllowed?: (boolean|null);

AdEvent measurementAllowed.

### medium
    
    
    public medium: string;

AdEvent medium.

### mobileDeviceId
    
    
    public mobileDeviceId: string;

AdEvent mobileDeviceId.

### platform
    
    
    public platform?: (google.ads.datamanager.v1.Platform|keyof typeof google.ads.datamanager.v1.Platform|null);

AdEvent platform.

### platformOneof
    
    
    public platformOneof?: ("platform"|"platformString");

AdEvent platformOneof.

### platformString
    
    
    public platformString?: (string|null);

AdEvent platformString.

### platformType
    
    
    public platformType?: (google.ads.datamanager.v1.PlatformType|keyof typeof google.ads.datamanager.v1.PlatformType|null);

AdEvent platformType.

### platformTypeOneof
    
    
    public platformTypeOneof?: ("platformType"|"platformTypeString");

AdEvent platformTypeOneof.

### platformTypeString
    
    
    public platformTypeString?: (string|null);

AdEvent platformTypeString.

### regionCode
    
    
    public regionCode: string;

AdEvent regionCode.

### source
    
    
    public source: string;

AdEvent source.

### targetingType
    
    
    public targetingType?: (google.ads.datamanager.v1.TargetingType|keyof typeof google.ads.datamanager.v1.TargetingType|null);

AdEvent targetingType.

### targetingTypeOneof
    
    
    public targetingTypeOneof?: ("targetingType"|"targetingTypeString");

AdEvent targetingTypeOneof.

### targetingTypeString
    
    
    public targetingTypeString?: (string|null);

AdEvent targetingTypeString.

### timestamp
    
    
    public timestamp?: (google.protobuf.ITimestamp|null);

AdEvent timestamp.

### userData
    
    
    public userData?: (google.ads.datamanager.v1.IUserData|null);

AdEvent userData.

### viewabilityInfo
    
    
    public viewabilityInfo?: (google.ads.datamanager.v1.IViewabilityInfo|null);

AdEvent viewabilityInfo.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.datamanager.v1.IAdEvent): google.ads.datamanager.v1.AdEvent;

Creates a new AdEvent instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdEvent](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iadevent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AdEvent](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adevent-class)` | AdEvent instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.datamanager.v1.AdEvent;

Decodes an AdEvent message from the specified reader or buffer.

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
`[AdEvent](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adevent-class)` | AdEvent  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.datamanager.v1.AdEvent;

Decodes an AdEvent message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AdEvent](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adevent-class)` | AdEvent  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.datamanager.v1.IAdEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdEvent message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdEvent](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iadevent)`   
AdEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.datamanager.v1.IAdEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdEvent message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdEvent](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iadevent)`   
AdEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.datamanager.v1.AdEvent;

Creates an AdEvent message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AdEvent](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adevent-class)` | AdEvent  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AdEvent

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

Converts this AdEvent to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.datamanager.v1.AdEvent, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AdEvent message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AdEvent](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adevent-class)`   
AdEvent  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AdEvent message.

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
