---
url: https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.listruntimeversionsrequest
title: Class protos.google.cloud.tpu.v2.ListRuntimeVersionsRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:04.329928+00:00
---

# Class protos.google.cloud.tpu.v2.ListRuntimeVersionsRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.listruntimeversionsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.tpu.v2.ListRuntimeVersionsRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  3.8.0  3.7.0  3.6.0  3.2.1  2.6.1  2.4.1  2.2.0  2.1.0  1.2.0  1.1.1  1.0.5 

Represents a ListRuntimeVersionsRequest.

## Implements

[protos.google.cloud.tpu.v2.IListRuntimeVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.ilistruntimeversionsrequest)

## Package

[@google-cloud/tpu](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.tpu.v2.IListRuntimeVersionsRequest);

Constructs a new ListRuntimeVersionsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListRuntimeVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.ilistruntimeversionsrequest)`   
Properties to set  
  
## Properties 

### filter
    
    
    public filter: string;

ListRuntimeVersionsRequest filter.

### orderBy
    
    
    public orderBy: string;

ListRuntimeVersionsRequest orderBy.

### pageSize
    
    
    public pageSize: number;

ListRuntimeVersionsRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListRuntimeVersionsRequest pageToken.

### parent
    
    
    public parent: string;

ListRuntimeVersionsRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.tpu.v2.IListRuntimeVersionsRequest): google.cloud.tpu.v2.ListRuntimeVersionsRequest;

Creates a new ListRuntimeVersionsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListRuntimeVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.ilistruntimeversionsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListRuntimeVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.listruntimeversionsrequest)` | ListRuntimeVersionsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.tpu.v2.ListRuntimeVersionsRequest;

Decodes a ListRuntimeVersionsRequest message from the specified reader or buffer.

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
`[ListRuntimeVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.listruntimeversionsrequest)` | ListRuntimeVersionsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.tpu.v2.ListRuntimeVersionsRequest;

Decodes a ListRuntimeVersionsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListRuntimeVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.listruntimeversionsrequest)` | ListRuntimeVersionsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.tpu.v2.IListRuntimeVersionsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListRuntimeVersionsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListRuntimeVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.ilistruntimeversionsrequest)`   
ListRuntimeVersionsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.tpu.v2.IListRuntimeVersionsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListRuntimeVersionsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListRuntimeVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.ilistruntimeversionsrequest)`   
ListRuntimeVersionsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.tpu.v2.ListRuntimeVersionsRequest;

Creates a ListRuntimeVersionsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListRuntimeVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.listruntimeversionsrequest)` | ListRuntimeVersionsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListRuntimeVersionsRequest

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

Converts this ListRuntimeVersionsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.tpu.v2.ListRuntimeVersionsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListRuntimeVersionsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListRuntimeVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.listruntimeversionsrequest)`   
ListRuntimeVersionsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListRuntimeVersionsRequest message.

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
