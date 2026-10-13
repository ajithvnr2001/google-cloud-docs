---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.getjobrequest
title: Class protos.google.cloud.dataproc.v1.GetJobRequest (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:44.787271+00:00
---

# Class protos.google.cloud.dataproc.v1.GetJobRequest (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.getjobrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.GetJobRequest (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents a GetJobRequest.

## Implements

[protos.google.cloud.dataproc.v1.IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetjobrequest)

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataproc.v1.IGetJobRequest);

Constructs a new GetJobRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetjobrequest)`   
Properties to set  
  
## Properties 

### jobId
    
    
    public jobId: string;

GetJobRequest jobId.

### projectId
    
    
    public projectId: string;

GetJobRequest projectId.

### region
    
    
    public region: string;

GetJobRequest region.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataproc.v1.IGetJobRequest): google.cloud.dataproc.v1.GetJobRequest;

Creates a new GetJobRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetjobrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.getjobrequest)` | GetJobRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataproc.v1.GetJobRequest;

Decodes a GetJobRequest message from the specified reader or buffer.

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
`[GetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.getjobrequest)` | GetJobRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataproc.v1.GetJobRequest;

Decodes a GetJobRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.getjobrequest)` | GetJobRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataproc.v1.IGetJobRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetJobRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetjobrequest)`   
GetJobRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataproc.v1.IGetJobRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetJobRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetjobrequest)`   
GetJobRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataproc.v1.GetJobRequest;

Creates a GetJobRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.getjobrequest)` | GetJobRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GetJobRequest

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

Converts this GetJobRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataproc.v1.GetJobRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GetJobRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.getjobrequest)`   
GetJobRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GetJobRequest message.

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
