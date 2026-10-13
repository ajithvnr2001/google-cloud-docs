---
url: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.classificationcategory
title: Class protos.google.cloud.language.v2.ClassificationCategory (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:03.775366+00:00
---

# Class protos.google.cloud.language.v2.ClassificationCategory (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.classificationcategory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.language.v2.ClassificationCategory (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.1.0  6.5.0  5.2.2  5.1.2  5.0.2  4.3.2  4.2.9 

Represents a ClassificationCategory.

## Implements

[protos.google.cloud.language.v2.IClassificationCategory](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.iclassificationcategory)

## Package

[@google-cloud/language](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.language.v2.IClassificationCategory);

Constructs a new ClassificationCategory.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IClassificationCategory](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.iclassificationcategory)`   
Properties to set  
  
## Properties 

### confidence
    
    
    public confidence: number;

ClassificationCategory confidence.

### name
    
    
    public name: string;

ClassificationCategory name.

### severity
    
    
    public severity: number;

ClassificationCategory severity.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.language.v2.IClassificationCategory): google.cloud.language.v2.ClassificationCategory;

Creates a new ClassificationCategory instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IClassificationCategory](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.iclassificationcategory)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationCategory](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.classificationcategory)` | ClassificationCategory instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.language.v2.ClassificationCategory;

Decodes a ClassificationCategory message from the specified reader or buffer.

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
`[ClassificationCategory](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.classificationcategory)` | ClassificationCategory  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.language.v2.ClassificationCategory;

Decodes a ClassificationCategory message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationCategory](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.classificationcategory)` | ClassificationCategory  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.language.v2.IClassificationCategory, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ClassificationCategory message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IClassificationCategory](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.iclassificationcategory)`   
ClassificationCategory message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.language.v2.IClassificationCategory, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ClassificationCategory message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IClassificationCategory](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.iclassificationcategory)`   
ClassificationCategory message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.language.v2.ClassificationCategory;

Creates a ClassificationCategory message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ClassificationCategory](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.classificationcategory)` | ClassificationCategory  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ClassificationCategory

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

Converts this ClassificationCategory to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.language.v2.ClassificationCategory, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ClassificationCategory message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ClassificationCategory](https://docs.cloud.google.com/nodejs/docs/reference/language/latest/language/protos.google.cloud.language.v2.classificationcategory)`   
ClassificationCategory  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ClassificationCategory message.

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
