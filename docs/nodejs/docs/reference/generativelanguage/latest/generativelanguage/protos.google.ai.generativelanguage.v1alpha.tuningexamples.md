---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.tuningexamples
title: Class protos.google.ai.generativelanguage.v1alpha.TuningExamples (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:20.651063+00:00
---

# Class protos.google.ai.generativelanguage.v1alpha.TuningExamples (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.tuningexamples

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ai.generativelanguage.v1alpha.TuningExamples (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

Represents a TuningExamples.

## Implements

[protos.google.ai.generativelanguage.v1alpha.ITuningExamples](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ituningexamples)

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ai.generativelanguage.v1alpha.ITuningExamples);

Constructs a new TuningExamples.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITuningExamples](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ituningexamples)`   
Properties to set  
  
## Properties 

### examples
    
    
    public examples: google.ai.generativelanguage.v1alpha.ITuningExample[];

TuningExamples examples.

### multiturnExamples
    
    
    public multiturnExamples: google.ai.generativelanguage.v1alpha.ITuningMultiturnExample[];

TuningExamples multiturnExamples.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ai.generativelanguage.v1alpha.ITuningExamples): google.ai.generativelanguage.v1alpha.TuningExamples;

Creates a new TuningExamples instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITuningExamples](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ituningexamples)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[TuningExamples](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.tuningexamples)` | TuningExamples instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ai.generativelanguage.v1alpha.TuningExamples;

Decodes a TuningExamples message from the specified reader or buffer.

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
`[TuningExamples](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.tuningexamples)` | TuningExamples  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ai.generativelanguage.v1alpha.TuningExamples;

Decodes a TuningExamples message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[TuningExamples](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.tuningexamples)` | TuningExamples  
  
### encode(message, writer)
    
    
    public static encode(message: google.ai.generativelanguage.v1alpha.ITuningExamples, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TuningExamples message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITuningExamples](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ituningexamples)`   
TuningExamples message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ai.generativelanguage.v1alpha.ITuningExamples, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TuningExamples message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITuningExamples](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.ituningexamples)`   
TuningExamples message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ai.generativelanguage.v1alpha.TuningExamples;

Creates a TuningExamples message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[TuningExamples](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.tuningexamples)` | TuningExamples  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for TuningExamples

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

Converts this TuningExamples to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ai.generativelanguage.v1alpha.TuningExamples, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a TuningExamples message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[TuningExamples](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1alpha.tuningexamples)`   
TuningExamples  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a TuningExamples message.

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
