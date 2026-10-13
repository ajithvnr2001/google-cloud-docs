---
url: https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.moveobjectrequest
title: Class protos.google.storage.v2.MoveObjectRequest (0.8.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:24.089239+00:00
---

# Class protos.google.storage.v2.MoveObjectRequest (0.8.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.moveobjectrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.storage.v2.MoveObjectRequest (0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.1.1 

Represents a MoveObjectRequest.

## Package

[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.storage.v2.IMoveObjectRequest);

Constructs a new MoveObjectRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMoveObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.imoveobjectrequest)`   
Properties to set  
  
## Properties 

### bucket
    
    
    public bucket: string;

MoveObjectRequest bucket.

### destinationObject
    
    
    public destinationObject: string;

MoveObjectRequest destinationObject.

### ifGenerationMatch
    
    
    public ifGenerationMatch?: (number|Long|string|null);

MoveObjectRequest ifGenerationMatch.

### ifGenerationNotMatch
    
    
    public ifGenerationNotMatch?: (number|Long|string|null);

MoveObjectRequest ifGenerationNotMatch.

### ifMetagenerationMatch
    
    
    public ifMetagenerationMatch?: (number|Long|string|null);

MoveObjectRequest ifMetagenerationMatch.

### ifMetagenerationNotMatch
    
    
    public ifMetagenerationNotMatch?: (number|Long|string|null);

MoveObjectRequest ifMetagenerationNotMatch.

### ifSourceGenerationMatch
    
    
    public ifSourceGenerationMatch?: (number|Long|string|null);

MoveObjectRequest ifSourceGenerationMatch.

### ifSourceGenerationNotMatch
    
    
    public ifSourceGenerationNotMatch?: (number|Long|string|null);

MoveObjectRequest ifSourceGenerationNotMatch.

### ifSourceMetagenerationMatch
    
    
    public ifSourceMetagenerationMatch?: (number|Long|string|null);

MoveObjectRequest ifSourceMetagenerationMatch.

### ifSourceMetagenerationNotMatch
    
    
    public ifSourceMetagenerationNotMatch?: (number|Long|string|null);

MoveObjectRequest ifSourceMetagenerationNotMatch.

### sourceObject
    
    
    public sourceObject: string;

MoveObjectRequest sourceObject.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.storage.v2.IMoveObjectRequest): google.storage.v2.MoveObjectRequest;

Creates a new MoveObjectRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMoveObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.imoveobjectrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MoveObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.moveobjectrequest)` | MoveObjectRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.storage.v2.MoveObjectRequest;

Decodes a MoveObjectRequest message from the specified reader or buffer.

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
`[MoveObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.moveobjectrequest)` | MoveObjectRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.storage.v2.MoveObjectRequest;

Decodes a MoveObjectRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MoveObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.moveobjectrequest)` | MoveObjectRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.storage.v2.IMoveObjectRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MoveObjectRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMoveObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.imoveobjectrequest)`   
MoveObjectRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.storage.v2.IMoveObjectRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MoveObjectRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMoveObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.imoveobjectrequest)`   
MoveObjectRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.storage.v2.MoveObjectRequest;

Creates a MoveObjectRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MoveObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.moveobjectrequest)` | MoveObjectRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MoveObjectRequest

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

Converts this MoveObjectRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.storage.v2.MoveObjectRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MoveObjectRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MoveObjectRequest](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.moveobjectrequest)`   
MoveObjectRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MoveObjectRequest message.

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
