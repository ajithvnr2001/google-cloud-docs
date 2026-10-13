---
url: https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.page-class
title: Class protos.google.cloud.documentai.v1.Document.Page (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:03.926362+00:00
---

# Class protos.google.cloud.documentai.v1.Document.Page (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.page-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.documentai.v1.Document.Page (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  1.10.0  1.9.0  1.7.0  1.5.0  1.4.0  1.3.0  0.5.1  0.4.0  0.3.1  0.1.2 

Represents a Page.

## Implements

[protos.google.cloud.documentai.v1.Document.IPage](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.ipage)

## Package

[@google-cloud/contentwarehouse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.documentai.v1.Document.IPage);

Constructs a new Page.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPage](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.ipage)`   
Properties to set  
  
## Properties 

### blocks
    
    
    public blocks: google.cloud.documentai.v1.Document.Page.IBlock[];

Page blocks.

### detectedBarcodes
    
    
    public detectedBarcodes: google.cloud.documentai.v1.Document.Page.IDetectedBarcode[];

Page detectedBarcodes.

### detectedLanguages
    
    
    public detectedLanguages: google.cloud.documentai.v1.Document.Page.IDetectedLanguage[];

Page detectedLanguages.

### dimension
    
    
    public dimension?: (google.cloud.documentai.v1.Document.Page.IDimension|null);

Page dimension.

### formFields
    
    
    public formFields: google.cloud.documentai.v1.Document.Page.IFormField[];

Page formFields.

### image
    
    
    public image?: (google.cloud.documentai.v1.Document.Page.IImage|null);

Page image.

### imageQualityScores
    
    
    public imageQualityScores?: (google.cloud.documentai.v1.Document.Page.IImageQualityScores|null);

Page imageQualityScores.

### layout
    
    
    public layout?: (google.cloud.documentai.v1.Document.Page.ILayout|null);

Page layout.

### lines
    
    
    public lines: google.cloud.documentai.v1.Document.Page.ILine[];

Page lines.

### pageNumber
    
    
    public pageNumber: number;

Page pageNumber.

### paragraphs
    
    
    public paragraphs: google.cloud.documentai.v1.Document.Page.IParagraph[];

Page paragraphs.

### provenance
    
    
    public provenance?: (google.cloud.documentai.v1.Document.IProvenance|null);

Page provenance.

### symbols
    
    
    public symbols: google.cloud.documentai.v1.Document.Page.ISymbol[];

Page symbols.

### tables
    
    
    public tables: google.cloud.documentai.v1.Document.Page.ITable[];

Page tables.

### tokens
    
    
    public tokens: google.cloud.documentai.v1.Document.Page.IToken[];

Page tokens.

### transforms
    
    
    public transforms: google.cloud.documentai.v1.Document.Page.IMatrix[];

Page transforms.

### visualElements
    
    
    public visualElements: google.cloud.documentai.v1.Document.Page.IVisualElement[];

Page visualElements.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.documentai.v1.Document.IPage): google.cloud.documentai.v1.Document.Page;

Creates a new Page instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPage](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.ipage)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.page-class)` | Page instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.documentai.v1.Document.Page;

Decodes a Page message from the specified reader or buffer.

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
`[Page](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.page-class)` | Page  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.documentai.v1.Document.Page;

Decodes a Page message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.page-class)` | Page  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.documentai.v1.Document.IPage, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Page message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPage](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.ipage)`   
Page message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.documentai.v1.Document.IPage, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Page message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPage](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.ipage)`   
Page message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.documentai.v1.Document.Page;

Creates a Page message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.page-class)` | Page  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Page

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

Converts this Page to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.documentai.v1.Document.Page, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Page message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Page](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.documentai.v1.document.page-class)`   
Page  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Page message.

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
