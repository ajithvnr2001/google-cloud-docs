---
url: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.analyzeentitiesresponse
title: Class protos.google.cloud.language.v1.AnalyzeEntitiesResponse (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:32.114221+00:00
---

# Class protos.google.cloud.language.v1.AnalyzeEntitiesResponse (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.analyzeentitiesresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.language.v1.AnalyzeEntitiesResponse (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.1.0  6.5.0  5.2.2  5.1.2  5.0.2  4.3.2  4.2.9 

Represents an AnalyzeEntitiesResponse.

## Implements

[protos.google.cloud.language.v1.IAnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.ianalyzeentitiesresponse)

## Package

[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.language.v1.IAnalyzeEntitiesResponse);

Constructs a new AnalyzeEntitiesResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.ianalyzeentitiesresponse)`   
Properties to set  
  
## Properties 

### entities
    
    
    public entities: google.cloud.language.v1.IEntity[];

AnalyzeEntitiesResponse entities.

### language
    
    
    public language: string;

AnalyzeEntitiesResponse language.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.language.v1.IAnalyzeEntitiesResponse): google.cloud.language.v1.AnalyzeEntitiesResponse;

Creates a new AnalyzeEntitiesResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.ianalyzeentitiesresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.analyzeentitiesresponse)` | AnalyzeEntitiesResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.language.v1.AnalyzeEntitiesResponse;

Decodes an AnalyzeEntitiesResponse message from the specified reader or buffer.

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
`[AnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.analyzeentitiesresponse)` | AnalyzeEntitiesResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.language.v1.AnalyzeEntitiesResponse;

Decodes an AnalyzeEntitiesResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.analyzeentitiesresponse)` | AnalyzeEntitiesResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.language.v1.IAnalyzeEntitiesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnalyzeEntitiesResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.ianalyzeentitiesresponse)`   
AnalyzeEntitiesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.language.v1.IAnalyzeEntitiesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnalyzeEntitiesResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.ianalyzeentitiesresponse)`   
AnalyzeEntitiesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.language.v1.AnalyzeEntitiesResponse;

Creates an AnalyzeEntitiesResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.analyzeentitiesresponse)` | AnalyzeEntitiesResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AnalyzeEntitiesResponse

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

Converts this AnalyzeEntitiesResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.language.v1.AnalyzeEntitiesResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AnalyzeEntitiesResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AnalyzeEntitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v1.analyzeentitiesresponse)`   
AnalyzeEntitiesResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AnalyzeEntitiesResponse message.

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
