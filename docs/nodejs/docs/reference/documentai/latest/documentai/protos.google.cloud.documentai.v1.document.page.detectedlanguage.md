---
url: https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.detectedlanguage
title: Class protos.google.cloud.documentai.v1.Document.Page.DetectedLanguage (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:57.041972+00:00
---

# Class protos.google.cloud.documentai.v1.Document.Page.DetectedLanguage (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.detectedlanguage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.documentai.v1.Document.Page.DetectedLanguage (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  9.6.0  9.2.0  8.12.0  8.10.0  8.8.0  8.6.0  8.5.0  8.4.0  8.2.0  8.1.2  8.0.0  7.3.1  7.1.0  7.0.1  6.3.0  6.1.0  6.0.0  3.3.0  3.2.1  3.1.0  3.0.2  2.10.0 

Represents a DetectedLanguage.

## Implements

[protos.google.cloud.documentai.v1.Document.Page.IDetectedLanguage](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.idetectedlanguage)

## Package

[@google-cloud/documentai](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.documentai.v1.Document.Page.IDetectedLanguage);

Constructs a new DetectedLanguage.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDetectedLanguage](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.idetectedlanguage)`   
Properties to set  
  
## Properties 

### confidence
    
    
    public confidence: number;

DetectedLanguage confidence.

### languageCode
    
    
    public languageCode: string;

DetectedLanguage languageCode.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.documentai.v1.Document.Page.IDetectedLanguage): google.cloud.documentai.v1.Document.Page.DetectedLanguage;

Creates a new DetectedLanguage instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDetectedLanguage](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.idetectedlanguage)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DetectedLanguage](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.detectedlanguage)` | DetectedLanguage instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.documentai.v1.Document.Page.DetectedLanguage;

Decodes a DetectedLanguage message from the specified reader or buffer.

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
`[DetectedLanguage](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.detectedlanguage)` | DetectedLanguage  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.documentai.v1.Document.Page.DetectedLanguage;

Decodes a DetectedLanguage message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DetectedLanguage](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.detectedlanguage)` | DetectedLanguage  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.documentai.v1.Document.Page.IDetectedLanguage, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DetectedLanguage message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDetectedLanguage](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.idetectedlanguage)`   
DetectedLanguage message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.documentai.v1.Document.Page.IDetectedLanguage, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DetectedLanguage message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDetectedLanguage](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.idetectedlanguage)`   
DetectedLanguage message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.documentai.v1.Document.Page.DetectedLanguage;

Creates a DetectedLanguage message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DetectedLanguage](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.detectedlanguage)` | DetectedLanguage  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DetectedLanguage

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

Converts this DetectedLanguage to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.documentai.v1.Document.Page.DetectedLanguage, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DetectedLanguage message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DetectedLanguage](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.document.page.detectedlanguage)`   
DetectedLanguage  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DetectedLanguage message.

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
