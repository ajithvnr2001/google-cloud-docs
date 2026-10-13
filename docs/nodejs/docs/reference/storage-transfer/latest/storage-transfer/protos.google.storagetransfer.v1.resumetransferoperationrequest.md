---
url: https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.resumetransferoperationrequest
title: Class protos.google.storagetransfer.v1.ResumeTransferOperationRequest (5.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:08.757443+00:00
---

# Class protos.google.storagetransfer.v1.ResumeTransferOperationRequest (5.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.resumetransferoperationrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.storagetransfer.v1.ResumeTransferOperationRequest (5.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.0.1 (latest)  4.1.0  4.0.1  3.6.0  3.5.0  3.4.0  3.0.0  2.3.2  2.2.1  2.1.1  1.2.0  1.1.1  1.0.1 

Represents a ResumeTransferOperationRequest.

## Implements

[protos.google.storagetransfer.v1.IResumeTransferOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.iresumetransferoperationrequest)

## Package

[@google-cloud/storage-transfer](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.storagetransfer.v1.IResumeTransferOperationRequest);

Constructs a new ResumeTransferOperationRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IResumeTransferOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.iresumetransferoperationrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

ResumeTransferOperationRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.storagetransfer.v1.IResumeTransferOperationRequest): google.storagetransfer.v1.ResumeTransferOperationRequest;

Creates a new ResumeTransferOperationRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IResumeTransferOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.iresumetransferoperationrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ResumeTransferOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.resumetransferoperationrequest)` | ResumeTransferOperationRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.storagetransfer.v1.ResumeTransferOperationRequest;

Decodes a ResumeTransferOperationRequest message from the specified reader or buffer.

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
`[ResumeTransferOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.resumetransferoperationrequest)` | ResumeTransferOperationRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.storagetransfer.v1.ResumeTransferOperationRequest;

Decodes a ResumeTransferOperationRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ResumeTransferOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.resumetransferoperationrequest)` | ResumeTransferOperationRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.storagetransfer.v1.IResumeTransferOperationRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ResumeTransferOperationRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IResumeTransferOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.iresumetransferoperationrequest)`   
ResumeTransferOperationRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.storagetransfer.v1.IResumeTransferOperationRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ResumeTransferOperationRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IResumeTransferOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.iresumetransferoperationrequest)`   
ResumeTransferOperationRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.storagetransfer.v1.ResumeTransferOperationRequest;

Creates a ResumeTransferOperationRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ResumeTransferOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.resumetransferoperationrequest)` | ResumeTransferOperationRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ResumeTransferOperationRequest

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

Converts this ResumeTransferOperationRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.storagetransfer.v1.ResumeTransferOperationRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ResumeTransferOperationRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ResumeTransferOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.resumetransferoperationrequest)`   
ResumeTransferOperationRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ResumeTransferOperationRequest message.

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
