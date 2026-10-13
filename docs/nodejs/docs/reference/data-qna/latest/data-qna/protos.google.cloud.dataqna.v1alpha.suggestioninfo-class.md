---
url: https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.suggestioninfo-class
title: Class protos.google.cloud.dataqna.v1alpha.SuggestionInfo (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:04.725751+00:00
---

# Class protos.google.cloud.dataqna.v1alpha.SuggestionInfo (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.suggestioninfo-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataqna.v1alpha.SuggestionInfo (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  3.1.0  2.1.2  2.0.2  1.1.0  1.0.8 

Represents a SuggestionInfo.

## Implements

[protos.google.cloud.dataqna.v1alpha.ISuggestionInfo](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.isuggestioninfo)

## Package

[@google-cloud/data-qna](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataqna.v1alpha.ISuggestionInfo);

Constructs a new SuggestionInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISuggestionInfo](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.isuggestioninfo)`   
Properties to set  
  
## Properties 

### annotatedSuggestion
    
    
    public annotatedSuggestion?: (google.cloud.dataqna.v1alpha.IAnnotatedString|null);

SuggestionInfo annotatedSuggestion.

### queryMatches
    
    
    public queryMatches: google.cloud.dataqna.v1alpha.SuggestionInfo.IMatchInfo[];

SuggestionInfo queryMatches.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataqna.v1alpha.ISuggestionInfo): google.cloud.dataqna.v1alpha.SuggestionInfo;

Creates a new SuggestionInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISuggestionInfo](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.isuggestioninfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SuggestionInfo](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.suggestioninfo-class)` | SuggestionInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataqna.v1alpha.SuggestionInfo;

Decodes a SuggestionInfo message from the specified reader or buffer.

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
`[SuggestionInfo](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.suggestioninfo-class)` | SuggestionInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataqna.v1alpha.SuggestionInfo;

Decodes a SuggestionInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SuggestionInfo](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.suggestioninfo-class)` | SuggestionInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataqna.v1alpha.ISuggestionInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SuggestionInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISuggestionInfo](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.isuggestioninfo)`   
SuggestionInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataqna.v1alpha.ISuggestionInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SuggestionInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISuggestionInfo](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.isuggestioninfo)`   
SuggestionInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataqna.v1alpha.SuggestionInfo;

Creates a SuggestionInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SuggestionInfo](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.suggestioninfo-class)` | SuggestionInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SuggestionInfo

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

Converts this SuggestionInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataqna.v1alpha.SuggestionInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SuggestionInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SuggestionInfo](https://docs.cloud.google.com/nodejs/docs/reference/data-qna/latest/data-qna/protos.google.cloud.dataqna.v1alpha.suggestioninfo-class)`   
SuggestionInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SuggestionInfo message.

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
