---
url: https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.effectivetag
title: Class protos.google.cloud.resourcemanager.v3.EffectiveTag (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:25.452893+00:00
---

# Class protos.google.cloud.resourcemanager.v3.EffectiveTag (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.effectivetag

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.resourcemanager.v3.EffectiveTag (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.3.0  6.1.0  4.3.0  4.2.1  4.1.3  3.2.0  3.1.0  3.0.0  2.0.1 

Represents an EffectiveTag.

## Implements

[protos.google.cloud.resourcemanager.v3.IEffectiveTag](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.ieffectivetag)

## Package

[@google-cloud/resource-manager](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.resourcemanager.v3.IEffectiveTag);

Constructs a new EffectiveTag.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEffectiveTag](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.ieffectivetag)`   
Properties to set  
  
## Properties 

### inherited
    
    
    public inherited: boolean;

EffectiveTag inherited.

### namespacedTagKey
    
    
    public namespacedTagKey: string;

EffectiveTag namespacedTagKey.

### namespacedTagValue
    
    
    public namespacedTagValue: string;

EffectiveTag namespacedTagValue.

### tagKey
    
    
    public tagKey: string;

EffectiveTag tagKey.

### tagKeyParentName
    
    
    public tagKeyParentName: string;

EffectiveTag tagKeyParentName.

### tagValue
    
    
    public tagValue: string;

EffectiveTag tagValue.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.resourcemanager.v3.IEffectiveTag): google.cloud.resourcemanager.v3.EffectiveTag;

Creates a new EffectiveTag instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEffectiveTag](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.ieffectivetag)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveTag](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.effectivetag)` | EffectiveTag instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.resourcemanager.v3.EffectiveTag;

Decodes an EffectiveTag message from the specified reader or buffer.

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
`[EffectiveTag](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.effectivetag)` | EffectiveTag  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.resourcemanager.v3.EffectiveTag;

Decodes an EffectiveTag message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveTag](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.effectivetag)` | EffectiveTag  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.resourcemanager.v3.IEffectiveTag, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EffectiveTag message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEffectiveTag](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.ieffectivetag)`   
EffectiveTag message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.resourcemanager.v3.IEffectiveTag, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EffectiveTag message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEffectiveTag](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.ieffectivetag)`   
EffectiveTag message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.resourcemanager.v3.EffectiveTag;

Creates an EffectiveTag message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EffectiveTag](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.effectivetag)` | EffectiveTag  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EffectiveTag

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

Converts this EffectiveTag to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.resourcemanager.v3.EffectiveTag, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EffectiveTag message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EffectiveTag](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.effectivetag)`   
EffectiveTag  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EffectiveTag message.

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
