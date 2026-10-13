---
url: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.variant
title: Class protos.google.cloud.configdelivery.v1.Variant (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:12.558695+00:00
---

# Class protos.google.cloud.configdelivery.v1.Variant (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.variant

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.configdelivery.v1.Variant (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a Variant.

## Implements

[protos.google.cloud.configdelivery.v1.IVariant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ivariant)

## Package

[@google-cloud/configdelivery](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.configdelivery.v1.IVariant);

Constructs a new Variant.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVariant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ivariant)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Variant createTime.

### labels
    
    
    public labels: { [k: string]: string };

Variant labels.

### name
    
    
    public name: string;

Variant name.

### resources
    
    
    public resources: string[];

Variant resources.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Variant updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.configdelivery.v1.IVariant): google.cloud.configdelivery.v1.Variant;

Creates a new Variant instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVariant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ivariant)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Variant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.variant)` | Variant instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.configdelivery.v1.Variant;

Decodes a Variant message from the specified reader or buffer.

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
`[Variant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.variant)` | Variant  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.configdelivery.v1.Variant;

Decodes a Variant message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Variant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.variant)` | Variant  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.configdelivery.v1.IVariant, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Variant message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVariant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ivariant)`   
Variant message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.configdelivery.v1.IVariant, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Variant message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVariant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.ivariant)`   
Variant message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.configdelivery.v1.Variant;

Creates a Variant message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Variant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.variant)` | Variant  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Variant

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

Converts this Variant to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.configdelivery.v1.Variant, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Variant message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Variant](https://docs.cloud.google.com/nodejs/docs/reference/configdelivery/latest/configdelivery/protos.google.cloud.configdelivery.v1.variant)`   
Variant  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Variant message.

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
