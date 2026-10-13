---
url: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.sourcecodeinfo-class
title: Class protos.google.protobuf.SourceCodeInfo (0.29.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:02.980378+00:00
---

# Class protos.google.protobuf.SourceCodeInfo (0.29.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.sourcecodeinfo-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.SourceCodeInfo (0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.25.0  0.23.0  0.19.1  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.4.0 

Represents a SourceCodeInfo.

## Implements

[protos.google.protobuf.ISourceCodeInfo](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.isourcecodeinfo)

## Package

[@google-cloud/sql](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.ISourceCodeInfo);

Constructs a new SourceCodeInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISourceCodeInfo](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.isourcecodeinfo)`   
Properties to set  
  
## Properties 

### location
    
    
    public location: google.protobuf.SourceCodeInfo.ILocation[];

SourceCodeInfo location.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.ISourceCodeInfo): google.protobuf.SourceCodeInfo;

Creates a new SourceCodeInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISourceCodeInfo](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.isourcecodeinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SourceCodeInfo](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.sourcecodeinfo-class)` | SourceCodeInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.SourceCodeInfo;

Decodes a SourceCodeInfo message from the specified reader or buffer.

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
`[SourceCodeInfo](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.sourcecodeinfo-class)` | SourceCodeInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.SourceCodeInfo;

Decodes a SourceCodeInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SourceCodeInfo](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.sourcecodeinfo-class)` | SourceCodeInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.ISourceCodeInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SourceCodeInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISourceCodeInfo](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.isourcecodeinfo)`   
SourceCodeInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.ISourceCodeInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SourceCodeInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISourceCodeInfo](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.isourcecodeinfo)`   
SourceCodeInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.SourceCodeInfo;

Creates a SourceCodeInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SourceCodeInfo](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.sourcecodeinfo-class)` | SourceCodeInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SourceCodeInfo

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

Converts this SourceCodeInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.SourceCodeInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SourceCodeInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SourceCodeInfo](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.protobuf.sourcecodeinfo-class)`   
SourceCodeInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SourceCodeInfo message.

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
