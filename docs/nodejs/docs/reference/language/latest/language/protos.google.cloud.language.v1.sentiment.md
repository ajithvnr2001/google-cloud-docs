---
url: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.sentiment
title: Class protos.google.cloud.language.v1.Sentiment (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:56.984552+00:00
---

# Class protos.google.cloud.language.v1.Sentiment (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.sentiment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.language.v1.Sentiment (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.1.0  6.5.0  5.2.2  5.1.2  5.0.2  4.3.2  4.2.9 

Represents a Sentiment.

## Implements

[protos.google.cloud.language.v1.ISentiment](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.isentiment)

## Package

[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.language.v1.ISentiment);

Constructs a new Sentiment.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISentiment](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.isentiment)`   
Properties to set  
  
## Properties 

### magnitude
    
    
    public magnitude: number;

Sentiment magnitude.

### score
    
    
    public score: number;

Sentiment score.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.language.v1.ISentiment): google.cloud.language.v1.Sentiment;

Creates a new Sentiment instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISentiment](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.isentiment)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Sentiment](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.sentiment)` | Sentiment instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.language.v1.Sentiment;

Decodes a Sentiment message from the specified reader or buffer.

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
`[Sentiment](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.sentiment)` | Sentiment  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.language.v1.Sentiment;

Decodes a Sentiment message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Sentiment](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.sentiment)` | Sentiment  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.language.v1.ISentiment, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Sentiment message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISentiment](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.isentiment)`   
Sentiment message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.language.v1.ISentiment, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Sentiment message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISentiment](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.isentiment)`   
Sentiment message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.language.v1.Sentiment;

Creates a Sentiment message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Sentiment](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.sentiment)` | Sentiment  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Sentiment

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

Converts this Sentiment to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.language.v1.Sentiment, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Sentiment message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Sentiment](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.sentiment)`   
Sentiment  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Sentiment message.

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
