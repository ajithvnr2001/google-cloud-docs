---
url: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.fieldoptions-class
title: Class protos.google.protobuf.FieldOptions (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:18.231994+00:00
---

# Class protos.google.protobuf.FieldOptions (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.fieldoptions-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.FieldOptions (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.6.2  3.5.0  3.4.1  3.2.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.6 

Represents a FieldOptions.

## Implements

[protos.google.protobuf.IFieldOptions](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.ifieldoptions)

## Package

[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IFieldOptions);

Constructs a new FieldOptions.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFieldOptions](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.ifieldoptions)`   
Properties to set  
  
## Properties 

### ctype
    
    
    public ctype: (google.protobuf.FieldOptions.CType|keyof typeof google.protobuf.FieldOptions.CType);

FieldOptions ctype.

### debugRedact
    
    
    public debugRedact: boolean;

FieldOptions debugRedact.

### deprecated
    
    
    public deprecated: boolean;

FieldOptions deprecated.

### editionDefaults
    
    
    public editionDefaults: google.protobuf.FieldOptions.IEditionDefault[];

FieldOptions editionDefaults.

### features
    
    
    public features?: (google.protobuf.IFeatureSet|null);

FieldOptions features.

### featureSupport
    
    
    public featureSupport?: (google.protobuf.FieldOptions.IFeatureSupport|null);

FieldOptions featureSupport.

### jstype
    
    
    public jstype: (google.protobuf.FieldOptions.JSType|keyof typeof google.protobuf.FieldOptions.JSType);

FieldOptions jstype.

### lazy
    
    
    public lazy: boolean;

FieldOptions lazy.

### packed
    
    
    public packed: boolean;

FieldOptions packed.

### retention
    
    
    public retention: (google.protobuf.FieldOptions.OptionRetention|keyof typeof google.protobuf.FieldOptions.OptionRetention);

FieldOptions retention.

### targets
    
    
    public targets: google.protobuf.FieldOptions.OptionTargetType[];

FieldOptions targets.

### uninterpretedOption
    
    
    public uninterpretedOption: google.protobuf.IUninterpretedOption[];

FieldOptions uninterpretedOption.

### unverifiedLazy
    
    
    public unverifiedLazy: boolean;

FieldOptions unverifiedLazy.

### weak
    
    
    public weak: boolean;

FieldOptions weak.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IFieldOptions): google.protobuf.FieldOptions;

Creates a new FieldOptions instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFieldOptions](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.ifieldoptions)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FieldOptions](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.fieldoptions-class)` | FieldOptions instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.FieldOptions;

Decodes a FieldOptions message from the specified reader or buffer.

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
`[FieldOptions](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.fieldoptions-class)` | FieldOptions  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.FieldOptions;

Decodes a FieldOptions message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FieldOptions](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.fieldoptions-class)` | FieldOptions  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IFieldOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FieldOptions message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFieldOptions](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.ifieldoptions)`   
FieldOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IFieldOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FieldOptions message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFieldOptions](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.ifieldoptions)`   
FieldOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.FieldOptions;

Creates a FieldOptions message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FieldOptions](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.fieldoptions-class)` | FieldOptions  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FieldOptions

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

Converts this FieldOptions to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.FieldOptions, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FieldOptions message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FieldOptions](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.fieldoptions-class)`   
FieldOptions  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FieldOptions message.

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
