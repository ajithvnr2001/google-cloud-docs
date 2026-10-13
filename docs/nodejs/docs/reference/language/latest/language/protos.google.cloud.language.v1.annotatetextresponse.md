---
url: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.annotatetextresponse
title: Class protos.google.cloud.language.v1.AnnotateTextResponse (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:54.698866+00:00
---

# Class protos.google.cloud.language.v1.AnnotateTextResponse (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.annotatetextresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.language.v1.AnnotateTextResponse (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.1.0  6.5.0  5.2.2  5.1.2  5.0.2  4.3.2  4.2.9 

Represents an AnnotateTextResponse.

## Implements

[protos.google.cloud.language.v1.IAnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.iannotatetextresponse)

## Package

[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.language.v1.IAnnotateTextResponse);

Constructs a new AnnotateTextResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.iannotatetextresponse)`   
Properties to set  
  
## Properties 

### categories
    
    
    public categories: google.cloud.language.v1.IClassificationCategory[];

AnnotateTextResponse categories.

### documentSentiment
    
    
    public documentSentiment?: (google.cloud.language.v1.ISentiment|null);

AnnotateTextResponse documentSentiment.

### entities
    
    
    public entities: google.cloud.language.v1.IEntity[];

AnnotateTextResponse entities.

### language
    
    
    public language: string;

AnnotateTextResponse language.

### moderationCategories
    
    
    public moderationCategories: google.cloud.language.v1.IClassificationCategory[];

AnnotateTextResponse moderationCategories.

### sentences
    
    
    public sentences: google.cloud.language.v1.ISentence[];

AnnotateTextResponse sentences.

### tokens
    
    
    public tokens: google.cloud.language.v1.IToken[];

AnnotateTextResponse tokens.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.language.v1.IAnnotateTextResponse): google.cloud.language.v1.AnnotateTextResponse;

Creates a new AnnotateTextResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.iannotatetextresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.annotatetextresponse)` | AnnotateTextResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.language.v1.AnnotateTextResponse;

Decodes an AnnotateTextResponse message from the specified reader or buffer.

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
`[AnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.annotatetextresponse)` | AnnotateTextResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.language.v1.AnnotateTextResponse;

Decodes an AnnotateTextResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.annotatetextresponse)` | AnnotateTextResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.language.v1.IAnnotateTextResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnnotateTextResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.iannotatetextresponse)`   
AnnotateTextResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.language.v1.IAnnotateTextResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnnotateTextResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.iannotatetextresponse)`   
AnnotateTextResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.language.v1.AnnotateTextResponse;

Creates an AnnotateTextResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.annotatetextresponse)` | AnnotateTextResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AnnotateTextResponse

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

Converts this AnnotateTextResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.language.v1.AnnotateTextResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AnnotateTextResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AnnotateTextResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.annotatetextresponse)`   
AnnotateTextResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AnnotateTextResponse message.

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
