---
url: https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.createmirrormetadata
title: Class protos.google.cloud.lustre.v1.CreateMirrorMetadata (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:30.651139+00:00
---

# Class protos.google.cloud.lustre.v1.CreateMirrorMetadata (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.createmirrormetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.lustre.v1.CreateMirrorMetadata (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.1 (latest)  0.5.0 

Represents a CreateMirrorMetadata.

## Implements

[protos.google.cloud.lustre.v1.ICreateMirrorMetadata](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreatemirrormetadata)

## Package

[@google-cloud/lustre](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.lustre.v1.ICreateMirrorMetadata);

Constructs a new CreateMirrorMetadata.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateMirrorMetadata](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreatemirrormetadata)`   
Properties to set  
  
## Properties 

### apiVersion
    
    
    public apiVersion: string;

CreateMirrorMetadata apiVersion.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

CreateMirrorMetadata createTime.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

CreateMirrorMetadata endTime.

### operationMetadata
    
    
    public operationMetadata?: (google.cloud.lustre.v1.ITransferOperationMetadata|null);

CreateMirrorMetadata operationMetadata.

### requestedCancellation
    
    
    public requestedCancellation: boolean;

CreateMirrorMetadata requestedCancellation.

### statusMessage
    
    
    public statusMessage: string;

CreateMirrorMetadata statusMessage.

### target
    
    
    public target: string;

CreateMirrorMetadata target.

### verb
    
    
    public verb: string;

CreateMirrorMetadata verb.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.lustre.v1.ICreateMirrorMetadata): google.cloud.lustre.v1.CreateMirrorMetadata;

Creates a new CreateMirrorMetadata instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateMirrorMetadata](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreatemirrormetadata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateMirrorMetadata](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.createmirrormetadata)` | CreateMirrorMetadata instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.lustre.v1.CreateMirrorMetadata;

Decodes a CreateMirrorMetadata message from the specified reader or buffer.

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
`[CreateMirrorMetadata](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.createmirrormetadata)` | CreateMirrorMetadata  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.lustre.v1.CreateMirrorMetadata;

Decodes a CreateMirrorMetadata message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateMirrorMetadata](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.createmirrormetadata)` | CreateMirrorMetadata  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.lustre.v1.ICreateMirrorMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateMirrorMetadata message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateMirrorMetadata](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreatemirrormetadata)`   
CreateMirrorMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.lustre.v1.ICreateMirrorMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateMirrorMetadata message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateMirrorMetadata](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.icreatemirrormetadata)`   
CreateMirrorMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.lustre.v1.CreateMirrorMetadata;

Creates a CreateMirrorMetadata message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateMirrorMetadata](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.createmirrormetadata)` | CreateMirrorMetadata  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateMirrorMetadata

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

Converts this CreateMirrorMetadata to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.lustre.v1.CreateMirrorMetadata, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateMirrorMetadata message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateMirrorMetadata](https://docs.cloud.google.com/nodejs/docs/reference/lustre/latest/lustre/protos.google.cloud.lustre.v1.createmirrormetadata)`   
CreateMirrorMetadata  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateMirrorMetadata message.

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
