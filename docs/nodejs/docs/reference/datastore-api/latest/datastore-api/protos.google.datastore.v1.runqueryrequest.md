---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.runqueryrequest
title: Class protos.google.datastore.v1.RunQueryRequest (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:47:54.641391+00:00
---

# Class protos.google.datastore.v1.RunQueryRequest (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.runqueryrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.datastore.v1.RunQueryRequest (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a RunQueryRequest.

## Implements

[protos.google.datastore.v1.IRunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irunqueryrequest)

## Package

[@google-cloud/datastore-api](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.datastore.v1.IRunQueryRequest);

Constructs a new RunQueryRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irunqueryrequest)`   
Properties to set  
  
## Properties 

### databaseId
    
    
    public databaseId: string;

RunQueryRequest databaseId.

### explainOptions
    
    
    public explainOptions?: (google.datastore.v1.IExplainOptions|null);

RunQueryRequest explainOptions.

### gqlQuery
    
    
    public gqlQuery?: (google.datastore.v1.IGqlQuery|null);

RunQueryRequest gqlQuery.

### partitionId
    
    
    public partitionId?: (google.datastore.v1.IPartitionId|null);

RunQueryRequest partitionId.

### projectId
    
    
    public projectId: string;

RunQueryRequest projectId.

### propertyMask
    
    
    public propertyMask?: (google.datastore.v1.IPropertyMask|null);

RunQueryRequest propertyMask.

### query
    
    
    public query?: (google.datastore.v1.IQuery|null);

RunQueryRequest query.

### queryType
    
    
    public queryType?: ("query"|"gqlQuery");

RunQueryRequest queryType.

### readOptions
    
    
    public readOptions?: (google.datastore.v1.IReadOptions|null);

RunQueryRequest readOptions.

### requestOptions
    
    
    public requestOptions?: (google.datastore.v1.IRequestOptions|null);

RunQueryRequest requestOptions.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.datastore.v1.IRunQueryRequest): google.datastore.v1.RunQueryRequest;

Creates a new RunQueryRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irunqueryrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.runqueryrequest)` | RunQueryRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.datastore.v1.RunQueryRequest;

Decodes a RunQueryRequest message from the specified reader or buffer.

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
`[RunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.runqueryrequest)` | RunQueryRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.datastore.v1.RunQueryRequest;

Decodes a RunQueryRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.runqueryrequest)` | RunQueryRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.datastore.v1.IRunQueryRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RunQueryRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irunqueryrequest)`   
RunQueryRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.datastore.v1.IRunQueryRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RunQueryRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.irunqueryrequest)`   
RunQueryRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.datastore.v1.RunQueryRequest;

Creates a RunQueryRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.runqueryrequest)` | RunQueryRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RunQueryRequest

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

Converts this RunQueryRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.datastore.v1.RunQueryRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RunQueryRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RunQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.v1.runqueryrequest)`   
RunQueryRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RunQueryRequest message.

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

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
