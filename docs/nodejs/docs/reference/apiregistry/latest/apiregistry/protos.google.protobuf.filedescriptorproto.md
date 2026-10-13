---
url: https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.filedescriptorproto
title: Class protos.google.protobuf.FileDescriptorProto (0.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:31:18.212264+00:00
---

# Class protos.google.protobuf.FileDescriptorProto (0.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.filedescriptorproto

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.FileDescriptorProto (0.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.2.0  0.1.0 

Represents a FileDescriptorProto.

## Implements

[protos.google.protobuf.IFileDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.ifiledescriptorproto)

## Package

[@google-cloud/apiregistry](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IFileDescriptorProto);

Constructs a new FileDescriptorProto.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFileDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.ifiledescriptorproto)`   
Properties to set  
  
## Properties 

### dependency
    
    
    public dependency: string[];

FileDescriptorProto dependency.

### edition
    
    
    public edition: (google.protobuf.Edition|keyof typeof google.protobuf.Edition);

FileDescriptorProto edition.

### enumType
    
    
    public enumType: google.protobuf.IEnumDescriptorProto[];

FileDescriptorProto enumType.

### extension
    
    
    public extension: google.protobuf.IFieldDescriptorProto[];

FileDescriptorProto extension.

### messageType
    
    
    public messageType: google.protobuf.IDescriptorProto[];

FileDescriptorProto messageType.

### name
    
    
    public name: string;

FileDescriptorProto name.

### optionDependency
    
    
    public optionDependency: string[];

FileDescriptorProto optionDependency.

### options
    
    
    public options?: (google.protobuf.IFileOptions|null);

FileDescriptorProto options.

### package
    
    
    public package: string;

FileDescriptorProto package.

### publicDependency
    
    
    public publicDependency: number[];

FileDescriptorProto publicDependency.

### service
    
    
    public service: google.protobuf.IServiceDescriptorProto[];

FileDescriptorProto service.

### sourceCodeInfo
    
    
    public sourceCodeInfo?: (google.protobuf.ISourceCodeInfo|null);

FileDescriptorProto sourceCodeInfo.

### syntax
    
    
    public syntax: string;

FileDescriptorProto syntax.

### weakDependency
    
    
    public weakDependency: number[];

FileDescriptorProto weakDependency.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IFileDescriptorProto): google.protobuf.FileDescriptorProto;

Creates a new FileDescriptorProto instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFileDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.ifiledescriptorproto)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FileDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.filedescriptorproto)` | FileDescriptorProto instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.FileDescriptorProto;

Decodes a FileDescriptorProto message from the specified reader or buffer.

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
`[FileDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.filedescriptorproto)` | FileDescriptorProto  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.FileDescriptorProto;

Decodes a FileDescriptorProto message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FileDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.filedescriptorproto)` | FileDescriptorProto  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IFileDescriptorProto, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FileDescriptorProto message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFileDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.ifiledescriptorproto)`   
FileDescriptorProto message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IFileDescriptorProto, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FileDescriptorProto message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFileDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.ifiledescriptorproto)`   
FileDescriptorProto message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.FileDescriptorProto;

Creates a FileDescriptorProto message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FileDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.filedescriptorproto)` | FileDescriptorProto  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FileDescriptorProto

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

Converts this FileDescriptorProto to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.FileDescriptorProto, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FileDescriptorProto message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FileDescriptorProto](https://docs.cloud.google.com/nodejs/docs/reference/apiregistry/latest/apiregistry/protos.google.protobuf.filedescriptorproto)`   
FileDescriptorProto  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FileDescriptorProto message.

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
