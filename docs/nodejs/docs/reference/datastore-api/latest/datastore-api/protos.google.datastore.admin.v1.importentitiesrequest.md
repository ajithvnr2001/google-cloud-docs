---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.importentitiesrequest
title: Class protos.google.datastore.admin.v1.ImportEntitiesRequest (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:47:45.499298+00:00
---

# Class protos.google.datastore.admin.v1.ImportEntitiesRequest (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.importentitiesrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.datastore.admin.v1.ImportEntitiesRequest (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an ImportEntitiesRequest.

## Implements

[protos.google.datastore.admin.v1.IImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.iimportentitiesrequest)

## Package

[@google-cloud/datastore-api](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.datastore.admin.v1.IImportEntitiesRequest);

Constructs a new ImportEntitiesRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.iimportentitiesrequest)`   
Properties to set  
  
## Properties 

### entityFilter
    
    
    public entityFilter?: (google.datastore.admin.v1.IEntityFilter|null);

ImportEntitiesRequest entityFilter.

### inputUrl
    
    
    public inputUrl: string;

ImportEntitiesRequest inputUrl.

### labels
    
    
    public labels: { [k: string]: string };

ImportEntitiesRequest labels.

### projectId
    
    
    public projectId: string;

ImportEntitiesRequest projectId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.datastore.admin.v1.IImportEntitiesRequest): google.datastore.admin.v1.ImportEntitiesRequest;

Creates a new ImportEntitiesRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.iimportentitiesrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.importentitiesrequest)` | ImportEntitiesRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.datastore.admin.v1.ImportEntitiesRequest;

Decodes an ImportEntitiesRequest message from the specified reader or buffer.

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
`[ImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.importentitiesrequest)` | ImportEntitiesRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.datastore.admin.v1.ImportEntitiesRequest;

Decodes an ImportEntitiesRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.importentitiesrequest)` | ImportEntitiesRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.datastore.admin.v1.IImportEntitiesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImportEntitiesRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.iimportentitiesrequest)`   
ImportEntitiesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.datastore.admin.v1.IImportEntitiesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImportEntitiesRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.iimportentitiesrequest)`   
ImportEntitiesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.datastore.admin.v1.ImportEntitiesRequest;

Creates an ImportEntitiesRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.importentitiesrequest)` | ImportEntitiesRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ImportEntitiesRequest

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

Converts this ImportEntitiesRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.datastore.admin.v1.ImportEntitiesRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ImportEntitiesRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ImportEntitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datastore-api/latest/datastore-api/protos.google.datastore.admin.v1.importentitiesrequest)`   
ImportEntitiesRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ImportEntitiesRequest message.

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
