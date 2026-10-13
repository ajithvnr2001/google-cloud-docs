---
url: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.deleteinstancepartitionrequest
title: Class protos.google.spanner.admin.instance.v1.DeleteInstancePartitionRequest (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:46.914586+00:00
---

# Class protos.google.spanner.admin.instance.v1.DeleteInstancePartitionRequest (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.deleteinstancepartitionrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.spanner.admin.instance.v1.DeleteInstancePartitionRequest (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DeleteInstancePartitionRequest.

## Implements

[protos.google.spanner.admin.instance.v1.IDeleteInstancePartitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.ideleteinstancepartitionrequest)

## Package

[@google-cloud/spanner-api](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.spanner.admin.instance.v1.IDeleteInstancePartitionRequest);

Constructs a new DeleteInstancePartitionRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteInstancePartitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.ideleteinstancepartitionrequest)`   
Properties to set  
  
## Properties 

### etag
    
    
    public etag: string;

DeleteInstancePartitionRequest etag.

### name
    
    
    public name: string;

DeleteInstancePartitionRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.spanner.admin.instance.v1.IDeleteInstancePartitionRequest): google.spanner.admin.instance.v1.DeleteInstancePartitionRequest;

Creates a new DeleteInstancePartitionRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteInstancePartitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.ideleteinstancepartitionrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeleteInstancePartitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.deleteinstancepartitionrequest)` | DeleteInstancePartitionRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.spanner.admin.instance.v1.DeleteInstancePartitionRequest;

Decodes a DeleteInstancePartitionRequest message from the specified reader or buffer.

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
`[DeleteInstancePartitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.deleteinstancepartitionrequest)` | DeleteInstancePartitionRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.spanner.admin.instance.v1.DeleteInstancePartitionRequest;

Decodes a DeleteInstancePartitionRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeleteInstancePartitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.deleteinstancepartitionrequest)` | DeleteInstancePartitionRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.spanner.admin.instance.v1.IDeleteInstancePartitionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteInstancePartitionRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteInstancePartitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.ideleteinstancepartitionrequest)`   
DeleteInstancePartitionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.spanner.admin.instance.v1.IDeleteInstancePartitionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteInstancePartitionRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteInstancePartitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.ideleteinstancepartitionrequest)`   
DeleteInstancePartitionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.spanner.admin.instance.v1.DeleteInstancePartitionRequest;

Creates a DeleteInstancePartitionRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeleteInstancePartitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.deleteinstancepartitionrequest)` | DeleteInstancePartitionRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeleteInstancePartitionRequest

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

Converts this DeleteInstancePartitionRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.spanner.admin.instance.v1.DeleteInstancePartitionRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeleteInstancePartitionRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeleteInstancePartitionRequest](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.instance.v1.deleteinstancepartitionrequest)`   
DeleteInstancePartitionRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeleteInstancePartitionRequest message.

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

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
