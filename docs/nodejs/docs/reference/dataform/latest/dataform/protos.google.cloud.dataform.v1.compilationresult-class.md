---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult-class
title: Class protos.google.cloud.dataform.v1.CompilationResult (3.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:13.518133+00:00
---

# Class protos.google.cloud.dataform.v1.CompilationResult (3.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataform.v1.CompilationResult (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

Represents a CompilationResult.

## Implements

[protos.google.cloud.dataform.v1.ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icompilationresult)

## Package

[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataform.v1.ICompilationResult);

Constructs a new CompilationResult.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icompilationresult)`   
Properties to set  
  
## Properties 

### codeCompilationConfig
    
    
    public codeCompilationConfig?: (google.cloud.dataform.v1.ICodeCompilationConfig|null);

CompilationResult codeCompilationConfig.

### compilationErrors
    
    
    public compilationErrors: google.cloud.dataform.v1.CompilationResult.ICompilationError[];

CompilationResult compilationErrors.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

CompilationResult createTime.

### dataEncryptionState
    
    
    public dataEncryptionState?: (google.cloud.dataform.v1.IDataEncryptionState|null);

CompilationResult dataEncryptionState.

### dataformCoreVersion
    
    
    public dataformCoreVersion: string;

CompilationResult dataformCoreVersion.

### gcsRepositorySnapshotMetadata
    
    
    public gcsRepositorySnapshotMetadata?: (google.cloud.dataform.v1.IGcsRepositorySnapshotMetadata|null);

CompilationResult gcsRepositorySnapshotMetadata.

### gitCommitish
    
    
    public gitCommitish?: (string|null);

CompilationResult gitCommitish.

### internalMetadata
    
    
    public internalMetadata?: (string|null);

CompilationResult internalMetadata.

### name
    
    
    public name: string;

CompilationResult name.

### privateResourceMetadata
    
    
    public privateResourceMetadata?: (google.cloud.dataform.v1.IPrivateResourceMetadata|null);

CompilationResult privateResourceMetadata.

### releaseConfig
    
    
    public releaseConfig?: (string|null);

CompilationResult releaseConfig.

### resolvedGitCommitSha
    
    
    public resolvedGitCommitSha: string;

CompilationResult resolvedGitCommitSha.

### source
    
    
    public source?: ("gitCommitish"|"workspace"|"releaseConfig");

CompilationResult source.

### workspace
    
    
    public workspace?: (string|null);

CompilationResult workspace.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataform.v1.ICompilationResult): google.cloud.dataform.v1.CompilationResult;

Creates a new CompilationResult instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icompilationresult)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult-class)` | CompilationResult instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataform.v1.CompilationResult;

Decodes a CompilationResult message from the specified reader or buffer.

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
`[CompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult-class)` | CompilationResult  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataform.v1.CompilationResult;

Decodes a CompilationResult message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult-class)` | CompilationResult  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataform.v1.ICompilationResult, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CompilationResult message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icompilationresult)`   
CompilationResult message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataform.v1.ICompilationResult, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CompilationResult message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icompilationresult)`   
CompilationResult message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataform.v1.CompilationResult;

Creates a CompilationResult message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult-class)` | CompilationResult  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CompilationResult

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

Converts this CompilationResult to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataform.v1.CompilationResult, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CompilationResult message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CompilationResult](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult-class)`   
CompilationResult  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CompilationResult message.

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
