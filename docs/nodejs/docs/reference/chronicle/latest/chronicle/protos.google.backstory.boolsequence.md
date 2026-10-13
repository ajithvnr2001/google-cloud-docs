---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.boolsequence
title: Class protos.google.backstory.BoolSequence (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:34.576826+00:00
---

# Class protos.google.backstory.BoolSequence (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.boolsequence

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.backstory.BoolSequence (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a BoolSequence.

## Implements

[protos.google.backstory.IBoolSequence](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.iboolsequence)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.backstory.IBoolSequence);

Constructs a new BoolSequence.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBoolSequence](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.iboolsequence)`   
Properties to set  
  
## Properties 

### boolVals
    
    
    public boolVals: boolean[];

BoolSequence boolVals.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.backstory.IBoolSequence): google.backstory.BoolSequence;

Creates a new BoolSequence instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBoolSequence](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.iboolsequence)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BoolSequence](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.boolsequence)` | BoolSequence instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.backstory.BoolSequence;

Decodes a BoolSequence message from the specified reader or buffer.

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
`[BoolSequence](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.boolsequence)` | BoolSequence  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.backstory.BoolSequence;

Decodes a BoolSequence message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BoolSequence](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.boolsequence)` | BoolSequence  
  
### encode(message, writer)
    
    
    public static encode(message: google.backstory.IBoolSequence, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BoolSequence message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBoolSequence](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.iboolsequence)`   
BoolSequence message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.backstory.IBoolSequence, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BoolSequence message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBoolSequence](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.iboolsequence)`   
BoolSequence message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.backstory.BoolSequence;

Creates a BoolSequence message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BoolSequence](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.boolsequence)` | BoolSequence  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BoolSequence

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

Converts this BoolSequence to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.backstory.BoolSequence, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BoolSequence message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BoolSequence](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.boolsequence)`   
BoolSequence  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BoolSequence message.

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
