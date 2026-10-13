---
url: https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.enumoptions
title: Class protos.google.protobuf.EnumOptions (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:53.985595+00:00
---

# Class protos.google.protobuf.EnumOptions (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.enumoptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.EnumOptions (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.0  5.0.1  3.0.8  2.5.0  2.4.7 

Represents an EnumOptions.

## Implements

[protos.google.protobuf.IEnumOptions](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.ienumoptions)

## Package

[@google-cloud/phishing-protection](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IEnumOptions);

Constructs a new EnumOptions.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEnumOptions](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.ienumoptions)`   
Properties to set  
  
## Properties 

### allowAlias
    
    
    public allowAlias: boolean;

EnumOptions allowAlias.

### deprecated
    
    
    public deprecated: boolean;

EnumOptions deprecated.

### deprecatedLegacyJsonFieldConflicts
    
    
    public deprecatedLegacyJsonFieldConflicts: boolean;

EnumOptions deprecatedLegacyJsonFieldConflicts.

### features
    
    
    public features?: (google.protobuf.IFeatureSet|null);

EnumOptions features.

### uninterpretedOption
    
    
    public uninterpretedOption: google.protobuf.IUninterpretedOption[];

EnumOptions uninterpretedOption.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IEnumOptions): google.protobuf.EnumOptions;

Creates a new EnumOptions instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEnumOptions](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.ienumoptions)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EnumOptions](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.enumoptions)` | EnumOptions instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.EnumOptions;

Decodes an EnumOptions message from the specified reader or buffer.

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
`[EnumOptions](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.enumoptions)` | EnumOptions  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.EnumOptions;

Decodes an EnumOptions message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EnumOptions](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.enumoptions)` | EnumOptions  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IEnumOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EnumOptions message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEnumOptions](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.ienumoptions)`   
EnumOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IEnumOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EnumOptions message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEnumOptions](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.ienumoptions)`   
EnumOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.EnumOptions;

Creates an EnumOptions message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EnumOptions](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.enumoptions)` | EnumOptions  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EnumOptions

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

Converts this EnumOptions to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.EnumOptions, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EnumOptions message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EnumOptions](https://docs.cloud.google.com/nodejs/docs/reference/phishing-protection/latest/phishing-protection/protos.google.protobuf.enumoptions)`   
EnumOptions  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EnumOptions message.

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
