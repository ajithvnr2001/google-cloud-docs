---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.operationmetadatav1
title: Class protos.google.appengine.v1.OperationMetadataV1 (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:41.134480+00:00
---

# Class protos.google.appengine.v1.OperationMetadataV1 (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.operationmetadatav1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.OperationMetadataV1 (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents an OperationMetadataV1.

## Implements

[protos.google.appengine.v1.IOperationMetadataV1](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ioperationmetadatav1)

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.appengine.v1.IOperationMetadataV1);

Constructs a new OperationMetadataV1.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOperationMetadataV1](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ioperationmetadatav1)`   
Properties to set  
  
## Properties 

### createVersionMetadata
    
    
    public createVersionMetadata?: (google.appengine.v1.ICreateVersionMetadataV1|null);

OperationMetadataV1 createVersionMetadata.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

OperationMetadataV1 endTime.

### ephemeralMessage
    
    
    public ephemeralMessage: string;

OperationMetadataV1 ephemeralMessage.

### insertTime
    
    
    public insertTime?: (google.protobuf.ITimestamp|null);

OperationMetadataV1 insertTime.

### method
    
    
    public method: string;

OperationMetadataV1 method.

### methodMetadata
    
    
    public methodMetadata?: "createVersionMetadata";

OperationMetadataV1 methodMetadata.

### target
    
    
    public target: string;

OperationMetadataV1 target.

### user
    
    
    public user: string;

OperationMetadataV1 user.

### warning
    
    
    public warning: string[];

OperationMetadataV1 warning.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.appengine.v1.IOperationMetadataV1): google.appengine.v1.OperationMetadataV1;

Creates a new OperationMetadataV1 instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOperationMetadataV1](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ioperationmetadatav1)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OperationMetadataV1](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.operationmetadatav1)` | OperationMetadataV1 instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.appengine.v1.OperationMetadataV1;

Decodes an OperationMetadataV1 message from the specified reader or buffer.

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
`[OperationMetadataV1](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.operationmetadatav1)` | OperationMetadataV1  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.appengine.v1.OperationMetadataV1;

Decodes an OperationMetadataV1 message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OperationMetadataV1](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.operationmetadatav1)` | OperationMetadataV1  
  
### encode(message, writer)
    
    
    public static encode(message: google.appengine.v1.IOperationMetadataV1, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OperationMetadataV1 message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOperationMetadataV1](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ioperationmetadatav1)`   
OperationMetadataV1 message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.appengine.v1.IOperationMetadataV1, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OperationMetadataV1 message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOperationMetadataV1](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ioperationmetadatav1)`   
OperationMetadataV1 message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.appengine.v1.OperationMetadataV1;

Creates an OperationMetadataV1 message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OperationMetadataV1](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.operationmetadatav1)` | OperationMetadataV1  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OperationMetadataV1

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

Converts this OperationMetadataV1 to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.appengine.v1.OperationMetadataV1, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OperationMetadataV1 message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OperationMetadataV1](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.operationmetadatav1)`   
OperationMetadataV1  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OperationMetadataV1 message.

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
