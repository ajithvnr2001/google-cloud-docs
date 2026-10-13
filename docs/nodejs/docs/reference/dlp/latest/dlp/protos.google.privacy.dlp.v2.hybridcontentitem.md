---
url: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.hybridcontentitem
title: Class protos.google.privacy.dlp.v2.HybridContentItem (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:53.691097+00:00
---

# Class protos.google.privacy.dlp.v2.HybridContentItem (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.hybridcontentitem

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.privacy.dlp.v2.HybridContentItem (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.6.0  6.2.0  6.1.0  5.13.0  5.11.0  5.10.0  5.7.0  5.5.0  5.3.0  5.0.0  4.4.2  4.2.0  4.1.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.8 

Represents a HybridContentItem.

## Implements

[protos.google.privacy.dlp.v2.IHybridContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.ihybridcontentitem)

## Package

[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.privacy.dlp.v2.IHybridContentItem);

Constructs a new HybridContentItem.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHybridContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.ihybridcontentitem)`   
Properties to set  
  
## Properties 

### findingDetails
    
    
    public findingDetails?: (google.privacy.dlp.v2.IHybridFindingDetails|null);

HybridContentItem findingDetails.

### item
    
    
    public item?: (google.privacy.dlp.v2.IContentItem|null);

HybridContentItem item.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.privacy.dlp.v2.IHybridContentItem): google.privacy.dlp.v2.HybridContentItem;

Creates a new HybridContentItem instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHybridContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.ihybridcontentitem)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[HybridContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.hybridcontentitem)` | HybridContentItem instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.privacy.dlp.v2.HybridContentItem;

Decodes a HybridContentItem message from the specified reader or buffer.

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
`[HybridContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.hybridcontentitem)` | HybridContentItem  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.privacy.dlp.v2.HybridContentItem;

Decodes a HybridContentItem message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[HybridContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.hybridcontentitem)` | HybridContentItem  
  
### encode(message, writer)
    
    
    public static encode(message: google.privacy.dlp.v2.IHybridContentItem, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HybridContentItem message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHybridContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.ihybridcontentitem)`   
HybridContentItem message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.privacy.dlp.v2.IHybridContentItem, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HybridContentItem message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHybridContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.ihybridcontentitem)`   
HybridContentItem message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.privacy.dlp.v2.HybridContentItem;

Creates a HybridContentItem message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[HybridContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.hybridcontentitem)` | HybridContentItem  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for HybridContentItem

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

Converts this HybridContentItem to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.privacy.dlp.v2.HybridContentItem, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a HybridContentItem message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[HybridContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.hybridcontentitem)`   
HybridContentItem  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a HybridContentItem message.

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
