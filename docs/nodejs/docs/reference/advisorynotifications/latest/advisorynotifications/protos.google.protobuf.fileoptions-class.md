---
url: https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.fileoptions-class
title: Class protos.google.protobuf.FileOptions (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:51.498618+00:00
---

# Class protos.google.protobuf.FileOptions (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.fileoptions-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.FileOptions (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.1.0  0.2.1  0.1.0 

Represents a FileOptions.

## Implements

[protos.google.protobuf.IFileOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.ifileoptions)

## Package

[@google-cloud/advisorynotifications](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IFileOptions);

Constructs a new FileOptions.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFileOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.ifileoptions)`   
Properties to set  
  
## Properties 

### ccEnableArenas
    
    
    public ccEnableArenas: boolean;

FileOptions ccEnableArenas.

### ccGenericServices
    
    
    public ccGenericServices: boolean;

FileOptions ccGenericServices.

### csharpNamespace
    
    
    public csharpNamespace: string;

FileOptions csharpNamespace.

### deprecated
    
    
    public deprecated: boolean;

FileOptions deprecated.

### features
    
    
    public features?: (google.protobuf.IFeatureSet|null);

FileOptions features.

### goPackage
    
    
    public goPackage: string;

FileOptions goPackage.

### javaGenerateEqualsAndHash
    
    
    public javaGenerateEqualsAndHash: boolean;

FileOptions javaGenerateEqualsAndHash.

### javaGenericServices
    
    
    public javaGenericServices: boolean;

FileOptions javaGenericServices.

### javaMultipleFiles
    
    
    public javaMultipleFiles: boolean;

FileOptions javaMultipleFiles.

### javaOuterClassname
    
    
    public javaOuterClassname: string;

FileOptions javaOuterClassname.

### javaPackage
    
    
    public javaPackage: string;

FileOptions javaPackage.

### javaStringCheckUtf8
    
    
    public javaStringCheckUtf8: boolean;

FileOptions javaStringCheckUtf8.

### objcClassPrefix
    
    
    public objcClassPrefix: string;

FileOptions objcClassPrefix.

### optimizeFor
    
    
    public optimizeFor: (google.protobuf.FileOptions.OptimizeMode|keyof typeof google.protobuf.FileOptions.OptimizeMode);

FileOptions optimizeFor.

### phpClassPrefix
    
    
    public phpClassPrefix: string;

FileOptions phpClassPrefix.

### phpMetadataNamespace
    
    
    public phpMetadataNamespace: string;

FileOptions phpMetadataNamespace.

### phpNamespace
    
    
    public phpNamespace: string;

FileOptions phpNamespace.

### pyGenericServices
    
    
    public pyGenericServices: boolean;

FileOptions pyGenericServices.

### rubyPackage
    
    
    public rubyPackage: string;

FileOptions rubyPackage.

### swiftPrefix
    
    
    public swiftPrefix: string;

FileOptions swiftPrefix.

### uninterpretedOption
    
    
    public uninterpretedOption: google.protobuf.IUninterpretedOption[];

FileOptions uninterpretedOption.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IFileOptions): google.protobuf.FileOptions;

Creates a new FileOptions instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFileOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.ifileoptions)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FileOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.fileoptions-class)` | FileOptions instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.FileOptions;

Decodes a FileOptions message from the specified reader or buffer.

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
`[FileOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.fileoptions-class)` | FileOptions  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.FileOptions;

Decodes a FileOptions message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FileOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.fileoptions-class)` | FileOptions  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IFileOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FileOptions message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFileOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.ifileoptions)`   
FileOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IFileOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FileOptions message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFileOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.ifileoptions)`   
FileOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.FileOptions;

Creates a FileOptions message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FileOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.fileoptions-class)` | FileOptions  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FileOptions

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

Converts this FileOptions to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.FileOptions, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FileOptions message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FileOptions](https://docs.cloud.google.com/nodejs/docs/reference/advisorynotifications/latest/advisorynotifications/protos.google.protobuf.fileoptions-class)`   
FileOptions  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FileOptions message.

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
