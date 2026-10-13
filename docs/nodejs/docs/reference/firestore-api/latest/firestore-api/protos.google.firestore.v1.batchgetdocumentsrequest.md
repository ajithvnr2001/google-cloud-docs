---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.batchgetdocumentsrequest
title: Class protos.google.firestore.v1.BatchGetDocumentsRequest (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:37.725358+00:00
---

# Class protos.google.firestore.v1.BatchGetDocumentsRequest (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.batchgetdocumentsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.firestore.v1.BatchGetDocumentsRequest (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a BatchGetDocumentsRequest.

## Implements

[protos.google.firestore.v1.IBatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.ibatchgetdocumentsrequest)

## Package

[@google-cloud/firestore-api](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.firestore.v1.IBatchGetDocumentsRequest);

Constructs a new BatchGetDocumentsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.ibatchgetdocumentsrequest)`   
Properties to set  
  
## Properties 

### consistencySelector
    
    
    public consistencySelector?: ("transaction"|"newTransaction"|"readTime");

BatchGetDocumentsRequest consistencySelector.

### database
    
    
    public database: string;

BatchGetDocumentsRequest database.

### documents
    
    
    public documents: string[];

BatchGetDocumentsRequest documents.

### mask
    
    
    public mask?: (google.firestore.v1.IDocumentMask|null);

BatchGetDocumentsRequest mask.

### newTransaction
    
    
    public newTransaction?: (google.firestore.v1.ITransactionOptions|null);

BatchGetDocumentsRequest newTransaction.

### readTime
    
    
    public readTime?: (google.protobuf.ITimestamp|null);

BatchGetDocumentsRequest readTime.

### transaction
    
    
    public transaction?: (Uint8Array|Buffer|string|null);

BatchGetDocumentsRequest transaction.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.firestore.v1.IBatchGetDocumentsRequest): google.firestore.v1.BatchGetDocumentsRequest;

Creates a new BatchGetDocumentsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.ibatchgetdocumentsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.batchgetdocumentsrequest)` | BatchGetDocumentsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.firestore.v1.BatchGetDocumentsRequest;

Decodes a BatchGetDocumentsRequest message from the specified reader or buffer.

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
`[BatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.batchgetdocumentsrequest)` | BatchGetDocumentsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.firestore.v1.BatchGetDocumentsRequest;

Decodes a BatchGetDocumentsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.batchgetdocumentsrequest)` | BatchGetDocumentsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.firestore.v1.IBatchGetDocumentsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BatchGetDocumentsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.ibatchgetdocumentsrequest)`   
BatchGetDocumentsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.firestore.v1.IBatchGetDocumentsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BatchGetDocumentsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.ibatchgetdocumentsrequest)`   
BatchGetDocumentsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.firestore.v1.BatchGetDocumentsRequest;

Creates a BatchGetDocumentsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.batchgetdocumentsrequest)` | BatchGetDocumentsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BatchGetDocumentsRequest

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

Converts this BatchGetDocumentsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.firestore.v1.BatchGetDocumentsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BatchGetDocumentsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BatchGetDocumentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/firestore-api/latest/firestore-api/protos.google.firestore.v1.batchgetdocumentsrequest)`   
BatchGetDocumentsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BatchGetDocumentsRequest message.

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
