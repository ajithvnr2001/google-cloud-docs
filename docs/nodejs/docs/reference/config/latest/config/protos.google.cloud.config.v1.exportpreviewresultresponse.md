---
url: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.exportpreviewresultresponse
title: Class protos.google.cloud.config.v1.ExportPreviewResultResponse (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:54.516896+00:00
---

# Class protos.google.cloud.config.v1.ExportPreviewResultResponse (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.exportpreviewresultresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.config.v1.ExportPreviewResultResponse (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.14.0  0.12.0  0.7.0  0.5.0  0.2.0  0.1.1 

Represents an ExportPreviewResultResponse.

## Implements

[protos.google.cloud.config.v1.IExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportpreviewresultresponse)

## Package

[@google-cloud/config](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.config.v1.IExportPreviewResultResponse);

Constructs a new ExportPreviewResultResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportpreviewresultresponse)`   
Properties to set  
  
## Properties 

### result
    
    
    public result?: (google.cloud.config.v1.IPreviewResult|null);

ExportPreviewResultResponse result.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.config.v1.IExportPreviewResultResponse): google.cloud.config.v1.ExportPreviewResultResponse;

Creates a new ExportPreviewResultResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportpreviewresultresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.exportpreviewresultresponse)` | ExportPreviewResultResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.config.v1.ExportPreviewResultResponse;

Decodes an ExportPreviewResultResponse message from the specified reader or buffer.

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
`[ExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.exportpreviewresultresponse)` | ExportPreviewResultResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.config.v1.ExportPreviewResultResponse;

Decodes an ExportPreviewResultResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.exportpreviewresultresponse)` | ExportPreviewResultResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.config.v1.IExportPreviewResultResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ExportPreviewResultResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportpreviewresultresponse)`   
ExportPreviewResultResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.config.v1.IExportPreviewResultResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ExportPreviewResultResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.iexportpreviewresultresponse)`   
ExportPreviewResultResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.config.v1.ExportPreviewResultResponse;

Creates an ExportPreviewResultResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.exportpreviewresultresponse)` | ExportPreviewResultResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ExportPreviewResultResponse

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

Converts this ExportPreviewResultResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.config.v1.ExportPreviewResultResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ExportPreviewResultResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ExportPreviewResultResponse](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.exportpreviewresultresponse)`   
ExportPreviewResultResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ExportPreviewResultResponse message.

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
