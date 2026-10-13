---
url: https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.getsupportedlanguagesrequest
title: Class protos.google.cloud.translation.v3.GetSupportedLanguagesRequest (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:55.748270+00:00
---

# Class protos.google.cloud.translation.v3.GetSupportedLanguagesRequest (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.getsupportedlanguagesrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.translation.v3.GetSupportedLanguagesRequest (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.0.1  9.3.0  8.5.0  8.0.3  7.2.1  7.1.1  7.0.4  6.3.1  6.2.7  6.1.0 

Represents a GetSupportedLanguagesRequest.

## Implements

[protos.google.cloud.translation.v3.IGetSupportedLanguagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.igetsupportedlanguagesrequest)

## Package

[@google-cloud/translate](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.translation.v3.IGetSupportedLanguagesRequest);

Constructs a new GetSupportedLanguagesRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetSupportedLanguagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.igetsupportedlanguagesrequest)`   
Properties to set  
  
## Properties 

### displayLanguageCode
    
    
    public displayLanguageCode: string;

GetSupportedLanguagesRequest displayLanguageCode.

### model
    
    
    public model: string;

GetSupportedLanguagesRequest model.

### parent
    
    
    public parent: string;

GetSupportedLanguagesRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.translation.v3.IGetSupportedLanguagesRequest): google.cloud.translation.v3.GetSupportedLanguagesRequest;

Creates a new GetSupportedLanguagesRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetSupportedLanguagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.igetsupportedlanguagesrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GetSupportedLanguagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.getsupportedlanguagesrequest)` | GetSupportedLanguagesRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.translation.v3.GetSupportedLanguagesRequest;

Decodes a GetSupportedLanguagesRequest message from the specified reader or buffer.

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
`[GetSupportedLanguagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.getsupportedlanguagesrequest)` | GetSupportedLanguagesRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.translation.v3.GetSupportedLanguagesRequest;

Decodes a GetSupportedLanguagesRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GetSupportedLanguagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.getsupportedlanguagesrequest)` | GetSupportedLanguagesRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.translation.v3.IGetSupportedLanguagesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetSupportedLanguagesRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetSupportedLanguagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.igetsupportedlanguagesrequest)`   
GetSupportedLanguagesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.translation.v3.IGetSupportedLanguagesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetSupportedLanguagesRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetSupportedLanguagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.igetsupportedlanguagesrequest)`   
GetSupportedLanguagesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.translation.v3.GetSupportedLanguagesRequest;

Creates a GetSupportedLanguagesRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GetSupportedLanguagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.getsupportedlanguagesrequest)` | GetSupportedLanguagesRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GetSupportedLanguagesRequest

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

Converts this GetSupportedLanguagesRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.translation.v3.GetSupportedLanguagesRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GetSupportedLanguagesRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GetSupportedLanguagesRequest](https://docs.cloud.google.com/nodejs/docs/reference/translate/latest/translate/protos.google.cloud.translation.v3.getsupportedlanguagesrequest)`   
GetSupportedLanguagesRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GetSupportedLanguagesRequest message.

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
