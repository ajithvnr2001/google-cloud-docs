---
url: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.analyzesentimentresponse
title: Class protos.google.cloud.language.v2.AnalyzeSentimentResponse (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:03.404747+00:00
---

# Class protos.google.cloud.language.v2.AnalyzeSentimentResponse (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.analyzesentimentresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.language.v2.AnalyzeSentimentResponse (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.1.0  6.5.0  5.2.2  5.1.2  5.0.2  4.3.2  4.2.9 

Represents an AnalyzeSentimentResponse.

## Implements

[protos.google.cloud.language.v2.IAnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.ianalyzesentimentresponse)

## Package

[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.language.v2.IAnalyzeSentimentResponse);

Constructs a new AnalyzeSentimentResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.ianalyzesentimentresponse)`   
Properties to set  
  
## Properties 

### documentSentiment
    
    
    public documentSentiment?: (google.cloud.language.v2.ISentiment|null);

AnalyzeSentimentResponse documentSentiment.

### languageCode
    
    
    public languageCode: string;

AnalyzeSentimentResponse languageCode.

### languageSupported
    
    
    public languageSupported: boolean;

AnalyzeSentimentResponse languageSupported.

### sentences
    
    
    public sentences: google.cloud.language.v2.ISentence[];

AnalyzeSentimentResponse sentences.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.language.v2.IAnalyzeSentimentResponse): google.cloud.language.v2.AnalyzeSentimentResponse;

Creates a new AnalyzeSentimentResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.ianalyzesentimentresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.analyzesentimentresponse)` | AnalyzeSentimentResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.language.v2.AnalyzeSentimentResponse;

Decodes an AnalyzeSentimentResponse message from the specified reader or buffer.

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
`[AnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.analyzesentimentresponse)` | AnalyzeSentimentResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.language.v2.AnalyzeSentimentResponse;

Decodes an AnalyzeSentimentResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.analyzesentimentresponse)` | AnalyzeSentimentResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.language.v2.IAnalyzeSentimentResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnalyzeSentimentResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.ianalyzesentimentresponse)`   
AnalyzeSentimentResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.language.v2.IAnalyzeSentimentResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnalyzeSentimentResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.ianalyzesentimentresponse)`   
AnalyzeSentimentResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.language.v2.AnalyzeSentimentResponse;

Creates an AnalyzeSentimentResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.analyzesentimentresponse)` | AnalyzeSentimentResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AnalyzeSentimentResponse

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

Converts this AnalyzeSentimentResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.language.v2.AnalyzeSentimentResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AnalyzeSentimentResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AnalyzeSentimentResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.analyzesentimentresponse)`   
AnalyzeSentimentResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AnalyzeSentimentResponse message.

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
