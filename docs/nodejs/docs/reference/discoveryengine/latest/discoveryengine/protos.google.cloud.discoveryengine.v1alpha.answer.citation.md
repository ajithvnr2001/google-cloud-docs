---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.citation
title: Class protos.google.cloud.discoveryengine.v1alpha.Answer.Citation (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:51.819093+00:00
---

# Class protos.google.cloud.discoveryengine.v1alpha.Answer.Citation (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.citation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1alpha.Answer.Citation (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents a Citation.

## Implements

[protos.google.cloud.discoveryengine.v1alpha.Answer.ICitation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.icitation)

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.discoveryengine.v1alpha.Answer.ICitation);

Constructs a new Citation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICitation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.icitation)`   
Properties to set  
  
## Properties 

### endIndex
    
    
    public endIndex: (number|Long|string);

Citation endIndex.

### sources
    
    
    public sources: google.cloud.discoveryengine.v1alpha.Answer.ICitationSource[];

Citation sources.

### startIndex
    
    
    public startIndex: (number|Long|string);

Citation startIndex.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.discoveryengine.v1alpha.Answer.ICitation): google.cloud.discoveryengine.v1alpha.Answer.Citation;

Creates a new Citation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICitation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.icitation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Citation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.citation)` | Citation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.discoveryengine.v1alpha.Answer.Citation;

Decodes a Citation message from the specified reader or buffer.

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
`[Citation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.citation)` | Citation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.discoveryengine.v1alpha.Answer.Citation;

Decodes a Citation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Citation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.citation)` | Citation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.discoveryengine.v1alpha.Answer.ICitation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Citation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICitation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.icitation)`   
Citation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.discoveryengine.v1alpha.Answer.ICitation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Citation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICitation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.icitation)`   
Citation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.discoveryengine.v1alpha.Answer.Citation;

Creates a Citation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Citation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.citation)` | Citation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Citation

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

Converts this Citation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.discoveryengine.v1alpha.Answer.Citation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Citation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Citation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answer.citation)`   
Citation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Citation message.

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
