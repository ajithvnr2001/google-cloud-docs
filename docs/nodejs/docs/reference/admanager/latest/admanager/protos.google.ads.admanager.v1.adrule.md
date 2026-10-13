---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adrule
title: Class protos.google.ads.admanager.v1.AdRule (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:39.604607+00:00
---

# Class protos.google.ads.admanager.v1.AdRule (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adrule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.AdRule (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents an AdRule.

## Implements

[protos.google.ads.admanager.v1.IAdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iadrule)

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.admanager.v1.IAdRule);

Constructs a new AdRule.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iadrule)`   
Properties to set  
  
## Properties 

### displayName
    
    
    public displayName?: (string|null);

AdRule displayName.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

AdRule endTime.

### endTimeUnlimited
    
    
    public endTimeUnlimited?: (boolean|null);

AdRule endTimeUnlimited.

### frequencyCapBehavior
    
    
    public frequencyCapBehavior?: (google.ads.admanager.v1.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior|keyof typeof google.ads.admanager.v1.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior|null);

AdRule frequencyCapBehavior.

### maxImpressionsPerLineItemPerPod
    
    
    public maxImpressionsPerLineItemPerPod?: (number|null);

AdRule maxImpressionsPerLineItemPerPod.

### maxImpressionsPerLineItemPerStream
    
    
    public maxImpressionsPerLineItemPerStream?: (number|null);

AdRule maxImpressionsPerLineItemPerStream.

### midrolls
    
    
    public midrolls: google.ads.admanager.v1.IAdRuleSlot[];

AdRule midrolls.

### name
    
    
    public name: string;

AdRule name.

### postroll
    
    
    public postroll?: (google.ads.admanager.v1.IAdRuleSlot|null);

AdRule postroll.

### preroll
    
    
    public preroll?: (google.ads.admanager.v1.IAdRuleSlot|null);

AdRule preroll.

### priority
    
    
    public priority?: (number|null);

AdRule priority.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

AdRule startTime.

### status
    
    
    public status?: (google.ads.admanager.v1.AdRuleStatusEnum.AdRuleStatus|keyof typeof google.ads.admanager.v1.AdRuleStatusEnum.AdRuleStatus|null);

AdRule status.

### targeting
    
    
    public targeting?: (google.ads.admanager.v1.ITargeting|null);

AdRule targeting.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.admanager.v1.IAdRule): google.ads.admanager.v1.AdRule;

Creates a new AdRule instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iadrule)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adrule)` | AdRule instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.admanager.v1.AdRule;

Decodes an AdRule message from the specified reader or buffer.

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
`[AdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adrule)` | AdRule  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.admanager.v1.AdRule;

Decodes an AdRule message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adrule)` | AdRule  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.admanager.v1.IAdRule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdRule message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iadrule)`   
AdRule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.admanager.v1.IAdRule, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdRule message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iadrule)`   
AdRule message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.admanager.v1.AdRule;

Creates an AdRule message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adrule)` | AdRule  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AdRule

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

Converts this AdRule to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.admanager.v1.AdRule, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AdRule message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AdRule](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.adrule)`   
AdRule  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AdRule message.

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
