---
url: https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.deletefolderrecursiverequest
title: Class protos.google.storage.control.v2.DeleteFolderRecursiveRequest (0.8.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:30.509472+00:00
---

# Class protos.google.storage.control.v2.DeleteFolderRecursiveRequest (0.8.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.deletefolderrecursiverequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.storage.control.v2.DeleteFolderRecursiveRequest (0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.1.1 

Represents a DeleteFolderRecursiveRequest.

## Package

[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.storage.control.v2.IDeleteFolderRecursiveRequest);

Constructs a new DeleteFolderRecursiveRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteFolderRecursiveRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.ideletefolderrecursiverequest)`   
Properties to set  
  
## Properties 

### ifMetagenerationMatch
    
    
    public ifMetagenerationMatch?: (number|Long|string|null);

DeleteFolderRecursiveRequest ifMetagenerationMatch.

### ifMetagenerationNotMatch
    
    
    public ifMetagenerationNotMatch?: (number|Long|string|null);

DeleteFolderRecursiveRequest ifMetagenerationNotMatch.

### name
    
    
    public name: string;

DeleteFolderRecursiveRequest name.

### requestId
    
    
    public requestId: string;

DeleteFolderRecursiveRequest requestId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.storage.control.v2.IDeleteFolderRecursiveRequest): google.storage.control.v2.DeleteFolderRecursiveRequest;

Creates a new DeleteFolderRecursiveRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteFolderRecursiveRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.ideletefolderrecursiverequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeleteFolderRecursiveRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.deletefolderrecursiverequest)` | DeleteFolderRecursiveRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.storage.control.v2.DeleteFolderRecursiveRequest;

Decodes a DeleteFolderRecursiveRequest message from the specified reader or buffer.

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
`[DeleteFolderRecursiveRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.deletefolderrecursiverequest)` | DeleteFolderRecursiveRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.storage.control.v2.DeleteFolderRecursiveRequest;

Decodes a DeleteFolderRecursiveRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeleteFolderRecursiveRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.deletefolderrecursiverequest)` | DeleteFolderRecursiveRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.storage.control.v2.IDeleteFolderRecursiveRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteFolderRecursiveRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteFolderRecursiveRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.ideletefolderrecursiverequest)`   
DeleteFolderRecursiveRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.storage.control.v2.IDeleteFolderRecursiveRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteFolderRecursiveRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteFolderRecursiveRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.ideletefolderrecursiverequest)`   
DeleteFolderRecursiveRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.storage.control.v2.DeleteFolderRecursiveRequest;

Creates a DeleteFolderRecursiveRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeleteFolderRecursiveRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.deletefolderrecursiverequest)` | DeleteFolderRecursiveRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeleteFolderRecursiveRequest

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

Converts this DeleteFolderRecursiveRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.storage.control.v2.DeleteFolderRecursiveRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeleteFolderRecursiveRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeleteFolderRecursiveRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.control.v2.deletefolderrecursiverequest)`   
DeleteFolderRecursiveRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeleteFolderRecursiveRequest message.

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

Last updated 2026-03-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-26 UTC."],[],[]] 
