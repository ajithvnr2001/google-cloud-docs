---
url: https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.objectrangedata
title: Class protos.google.storage.v2.ObjectRangeData (0.8.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:50.770427+00:00
---

# Class protos.google.storage.v2.ObjectRangeData (0.8.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.objectrangedata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.storage.v2.ObjectRangeData (0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.1.1 

Represents an ObjectRangeData.

## Package

[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.storage.v2.IObjectRangeData);

Constructs a new ObjectRangeData.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IObjectRangeData](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.iobjectrangedata)`   
Properties to set  
  
## Properties 

### checksummedData
    
    
    public checksummedData?: (google.storage.v2.IChecksummedData|null);

ObjectRangeData checksummedData.

### rangeEnd
    
    
    public rangeEnd: boolean;

ObjectRangeData rangeEnd.

### readRange
    
    
    public readRange?: (google.storage.v2.IReadRange|null);

ObjectRangeData readRange.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.storage.v2.IObjectRangeData): google.storage.v2.ObjectRangeData;

Creates a new ObjectRangeData instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IObjectRangeData](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.iobjectrangedata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ObjectRangeData](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.objectrangedata)` | ObjectRangeData instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.storage.v2.ObjectRangeData;

Decodes an ObjectRangeData message from the specified reader or buffer.

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
`[ObjectRangeData](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.objectrangedata)` | ObjectRangeData  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.storage.v2.ObjectRangeData;

Decodes an ObjectRangeData message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ObjectRangeData](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.objectrangedata)` | ObjectRangeData  
  
### encode(message, writer)
    
    
    public static encode(message: google.storage.v2.IObjectRangeData, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ObjectRangeData message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IObjectRangeData](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.iobjectrangedata)`   
ObjectRangeData message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.storage.v2.IObjectRangeData, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ObjectRangeData message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IObjectRangeData](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.iobjectrangedata)`   
ObjectRangeData message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.storage.v2.ObjectRangeData;

Creates an ObjectRangeData message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ObjectRangeData](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.objectrangedata)` | ObjectRangeData  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ObjectRangeData

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

Converts this ObjectRangeData to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.storage.v2.ObjectRangeData, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ObjectRangeData message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ObjectRangeData](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.objectrangedata)`   
ObjectRangeData  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ObjectRangeData message.

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
