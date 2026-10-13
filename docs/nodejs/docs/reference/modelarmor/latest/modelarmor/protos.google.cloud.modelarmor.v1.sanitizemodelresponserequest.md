---
url: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.sanitizemodelresponserequest
title: Class protos.google.cloud.modelarmor.v1.SanitizeModelResponseRequest (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:11:52.935066+00:00
---

# Class protos.google.cloud.modelarmor.v1.SanitizeModelResponseRequest (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.sanitizemodelresponserequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.modelarmor.v1.SanitizeModelResponseRequest (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0 

Represents a SanitizeModelResponseRequest.

## Implements

[protos.google.cloud.modelarmor.v1.ISanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.isanitizemodelresponserequest)

## Package

[@google-cloud/modelarmor](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.modelarmor.v1.ISanitizeModelResponseRequest);

Constructs a new SanitizeModelResponseRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.isanitizemodelresponserequest)`   
Properties to set  
  
## Properties 

### modelResponseData
    
    
    public modelResponseData?: (google.cloud.modelarmor.v1.IDataItem|null);

SanitizeModelResponseRequest modelResponseData.

### multiLanguageDetectionMetadata
    
    
    public multiLanguageDetectionMetadata?: (google.cloud.modelarmor.v1.IMultiLanguageDetectionMetadata|null);

SanitizeModelResponseRequest multiLanguageDetectionMetadata.

### name
    
    
    public name: string;

SanitizeModelResponseRequest name.

### streamingMode
    
    
    public streamingMode?: (google.cloud.modelarmor.v1.StreamingMode|keyof typeof google.cloud.modelarmor.v1.StreamingMode|null);

SanitizeModelResponseRequest streamingMode.

### userPrompt
    
    
    public userPrompt: string;

SanitizeModelResponseRequest userPrompt.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.modelarmor.v1.ISanitizeModelResponseRequest): google.cloud.modelarmor.v1.SanitizeModelResponseRequest;

Creates a new SanitizeModelResponseRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.isanitizemodelresponserequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.sanitizemodelresponserequest)` | SanitizeModelResponseRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.modelarmor.v1.SanitizeModelResponseRequest;

Decodes a SanitizeModelResponseRequest message from the specified reader or buffer.

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
`[SanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.sanitizemodelresponserequest)` | SanitizeModelResponseRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.modelarmor.v1.SanitizeModelResponseRequest;

Decodes a SanitizeModelResponseRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.sanitizemodelresponserequest)` | SanitizeModelResponseRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.modelarmor.v1.ISanitizeModelResponseRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SanitizeModelResponseRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.isanitizemodelresponserequest)`   
SanitizeModelResponseRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.modelarmor.v1.ISanitizeModelResponseRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SanitizeModelResponseRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.isanitizemodelresponserequest)`   
SanitizeModelResponseRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.modelarmor.v1.SanitizeModelResponseRequest;

Creates a SanitizeModelResponseRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.sanitizemodelresponserequest)` | SanitizeModelResponseRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SanitizeModelResponseRequest

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

Converts this SanitizeModelResponseRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.modelarmor.v1.SanitizeModelResponseRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SanitizeModelResponseRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SanitizeModelResponseRequest](https://docs.cloud.google.com/nodejs/docs/reference/modelarmor/latest/modelarmor/protos.google.cloud.modelarmor.v1.sanitizemodelresponserequest)`   
SanitizeModelResponseRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SanitizeModelResponseRequest message.

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
