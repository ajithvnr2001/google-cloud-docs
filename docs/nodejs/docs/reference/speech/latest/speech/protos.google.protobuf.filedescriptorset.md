---
url: https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.filedescriptorset
title: Class protos.google.protobuf.FileDescriptorSet (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:06.290573+00:00
---

# Class protos.google.protobuf.FileDescriptorSet (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.filedescriptorset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.FileDescriptorSet (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.5.0  7.4.0  6.6.1  6.3.0  6.1.1  6.0.1  5.4.1  5.3.1  5.1.0  5.0.3  4.10.0  4.9.0  4.8.1  4.7.0  4.6.1  4.5.6  4.1.3 

Represents a FileDescriptorSet.

## Implements

[protos.google.protobuf.IFileDescriptorSet](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.ifiledescriptorset)

## Package

[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IFileDescriptorSet);

Constructs a new FileDescriptorSet.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFileDescriptorSet](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.ifiledescriptorset)`   
Properties to set  
  
## Properties 

### file
    
    
    public file: google.protobuf.IFileDescriptorProto[];

FileDescriptorSet file.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IFileDescriptorSet): google.protobuf.FileDescriptorSet;

Creates a new FileDescriptorSet instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFileDescriptorSet](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.ifiledescriptorset)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FileDescriptorSet](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.filedescriptorset)` | FileDescriptorSet instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.FileDescriptorSet;

Decodes a FileDescriptorSet message from the specified reader or buffer.

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
`[FileDescriptorSet](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.filedescriptorset)` | FileDescriptorSet  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.FileDescriptorSet;

Decodes a FileDescriptorSet message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FileDescriptorSet](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.filedescriptorset)` | FileDescriptorSet  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IFileDescriptorSet, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FileDescriptorSet message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFileDescriptorSet](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.ifiledescriptorset)`   
FileDescriptorSet message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IFileDescriptorSet, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FileDescriptorSet message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFileDescriptorSet](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.ifiledescriptorset)`   
FileDescriptorSet message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.FileDescriptorSet;

Creates a FileDescriptorSet message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FileDescriptorSet](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.filedescriptorset)` | FileDescriptorSet  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FileDescriptorSet

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

Converts this FileDescriptorSet to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.FileDescriptorSet, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FileDescriptorSet message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FileDescriptorSet](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.protobuf.filedescriptorset)`   
FileDescriptorSet  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FileDescriptorSet message.

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
