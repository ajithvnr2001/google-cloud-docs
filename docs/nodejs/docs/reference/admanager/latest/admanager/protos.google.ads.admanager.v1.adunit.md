---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunit
title: Class protos.google.ads.admanager.v1.AdUnit (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:44.926690+00:00
---

# Class protos.google.ads.admanager.v1.AdUnit (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunit

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.AdUnit (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an AdUnit.

## Implements

[protos.google.ads.admanager.v1.IAdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iadunit)

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.admanager.v1.IAdUnit);

Constructs a new AdUnit.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iadunit)`   
Properties to set  
  
## Properties 

### adUnitCode
    
    
    public adUnitCode?: (string|null);

AdUnit adUnitCode.

### adUnitId
    
    
    public adUnitId: (number|Long|string);

AdUnit adUnitId.

### adUnitSizes
    
    
    public adUnitSizes: google.ads.admanager.v1.IAdUnitSize[];

AdUnit adUnitSizes.

### appliedAdsenseEnabled
    
    
    public appliedAdsenseEnabled?: (boolean|null);

AdUnit appliedAdsenseEnabled.

### appliedLabelFrequencyCaps
    
    
    public appliedLabelFrequencyCaps: google.ads.admanager.v1.ILabelFrequencyCap[];

AdUnit appliedLabelFrequencyCaps.

### appliedLabels
    
    
    public appliedLabels: google.ads.admanager.v1.IAppliedLabel[];

AdUnit appliedLabels.

### appliedTargetWindow
    
    
    public appliedTargetWindow?: (google.ads.admanager.v1.TargetWindowEnum.TargetWindow|keyof typeof google.ads.admanager.v1.TargetWindowEnum.TargetWindow|null);

AdUnit appliedTargetWindow.

### appliedTeams
    
    
    public appliedTeams: string[];

AdUnit appliedTeams.

### description
    
    
    public description?: (string|null);

AdUnit description.

### displayName
    
    
    public displayName?: (string|null);

AdUnit displayName.

### effectiveAdsenseEnabled
    
    
    public effectiveAdsenseEnabled?: (boolean|null);

AdUnit effectiveAdsenseEnabled.

### effectiveAppliedLabels
    
    
    public effectiveAppliedLabels: google.ads.admanager.v1.IAppliedLabel[];

AdUnit effectiveAppliedLabels.

### effectiveLabelFrequencyCaps
    
    
    public effectiveLabelFrequencyCaps: google.ads.admanager.v1.ILabelFrequencyCap[];

AdUnit effectiveLabelFrequencyCaps.

### effectiveTargetWindow
    
    
    public effectiveTargetWindow?: (google.ads.admanager.v1.TargetWindowEnum.TargetWindow|keyof typeof google.ads.admanager.v1.TargetWindowEnum.TargetWindow|null);

AdUnit effectiveTargetWindow.

### explicitlyTargeted
    
    
    public explicitlyTargeted?: (boolean|null);

AdUnit explicitlyTargeted.

### externalSetTopBoxChannelId
    
    
    public externalSetTopBoxChannelId?: (string|null);

AdUnit externalSetTopBoxChannelId.

### hasChildren
    
    
    public hasChildren?: (boolean|null);

AdUnit hasChildren.

### name
    
    
    public name: string;

AdUnit name.

### parentAdUnit
    
    
    public parentAdUnit?: (string|null);

AdUnit parentAdUnit.

### parentPath
    
    
    public parentPath: google.ads.admanager.v1.IAdUnitParent[];

AdUnit parentPath.

### refreshDelay
    
    
    public refreshDelay?: (google.protobuf.IDuration|null);

AdUnit refreshDelay.

### refreshRateType
    
    
    public refreshRateType?: (google.ads.admanager.v1.RefreshRateTypeEnum.RefreshRateType|keyof typeof google.ads.admanager.v1.RefreshRateTypeEnum.RefreshRateType|null);

AdUnit refreshRateType.

### smartSizeMode
    
    
    public smartSizeMode?: (google.ads.admanager.v1.SmartSizeModeEnum.SmartSizeMode|keyof typeof google.ads.admanager.v1.SmartSizeModeEnum.SmartSizeMode|null);

AdUnit smartSizeMode.

### status
    
    
    public status?: (google.ads.admanager.v1.AdUnitStatusEnum.AdUnitStatus|keyof typeof google.ads.admanager.v1.AdUnitStatusEnum.AdUnitStatus|null);

AdUnit status.

### teams
    
    
    public teams: string[];

AdUnit teams.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

AdUnit updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.admanager.v1.IAdUnit): google.ads.admanager.v1.AdUnit;

Creates a new AdUnit instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iadunit)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunit)` | AdUnit instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.admanager.v1.AdUnit;

Decodes an AdUnit message from the specified reader or buffer.

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
`[AdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunit)` | AdUnit  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.admanager.v1.AdUnit;

Decodes an AdUnit message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunit)` | AdUnit  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.admanager.v1.IAdUnit, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdUnit message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iadunit)`   
AdUnit message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.admanager.v1.IAdUnit, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdUnit message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iadunit)`   
AdUnit message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.admanager.v1.AdUnit;

Creates an AdUnit message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunit)` | AdUnit  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AdUnit

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

Converts this AdUnit to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.admanager.v1.AdUnit, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AdUnit message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AdUnit](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adunit)`   
AdUnit  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AdUnit message.

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
