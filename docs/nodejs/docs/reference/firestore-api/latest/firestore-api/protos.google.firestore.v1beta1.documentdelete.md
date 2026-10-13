---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.documentdelete
title: Class protos.google.firestore.v1beta1.DocumentDelete (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:27.216502+00:00
---

# Class protos.google.firestore.v1beta1.DocumentDelete (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.documentdelete

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.firestore.v1beta1.DocumentDelete (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DocumentDelete.

## Implements

[protos.google.firestore.v1beta1.IDocumentDelete](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocumentdelete)

## Package

[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.firestore.v1beta1.IDocumentDelete);

Constructs a new DocumentDelete.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDocumentDelete](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocumentdelete)`   
Properties to set  
  
## Properties 

### document
    
    
    public document: string;

DocumentDelete document.

### readTime
    
    
    public readTime?: (google.protobuf.ITimestamp|null);

DocumentDelete readTime.

### removedTargetIds
    
    
    public removedTargetIds: number[];

DocumentDelete removedTargetIds.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.firestore.v1beta1.IDocumentDelete): google.firestore.v1beta1.DocumentDelete;

Creates a new DocumentDelete instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDocumentDelete](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocumentdelete)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DocumentDelete](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.documentdelete)` | DocumentDelete instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.firestore.v1beta1.DocumentDelete;

Decodes a DocumentDelete message from the specified reader or buffer.

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
`[DocumentDelete](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.documentdelete)` | DocumentDelete  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.firestore.v1beta1.DocumentDelete;

Decodes a DocumentDelete message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DocumentDelete](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.documentdelete)` | DocumentDelete  
  
### encode(message, writer)
    
    
    public static encode(message: google.firestore.v1beta1.IDocumentDelete, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DocumentDelete message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDocumentDelete](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocumentdelete)`   
DocumentDelete message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.firestore.v1beta1.IDocumentDelete, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DocumentDelete message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDocumentDelete](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.idocumentdelete)`   
DocumentDelete message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.firestore.v1beta1.DocumentDelete;

Creates a DocumentDelete message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DocumentDelete](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.documentdelete)` | DocumentDelete  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DocumentDelete

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

Converts this DocumentDelete to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.firestore.v1beta1.DocumentDelete, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DocumentDelete message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DocumentDelete](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1beta1.documentdelete)`   
DocumentDelete  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DocumentDelete message.

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
