---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.codecompilationconfig
title: Class protos.google.cloud.dataform.v1.CodeCompilationConfig (3.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:11.329749+00:00
---

# Class protos.google.cloud.dataform.v1.CodeCompilationConfig (3.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.codecompilationconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataform.v1.CodeCompilationConfig (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

Represents a CodeCompilationConfig.

## Implements

[protos.google.cloud.dataform.v1.ICodeCompilationConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icodecompilationconfig)

## Package

[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataform.v1.ICodeCompilationConfig);

Constructs a new CodeCompilationConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICodeCompilationConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icodecompilationconfig)`   
Properties to set  
  
## Properties 

### assertionSchema
    
    
    public assertionSchema: string;

CodeCompilationConfig assertionSchema.

### builtinAssertionNamePrefix
    
    
    public builtinAssertionNamePrefix: string;

CodeCompilationConfig builtinAssertionNamePrefix.

### databaseSuffix
    
    
    public databaseSuffix: string;

CodeCompilationConfig databaseSuffix.

### defaultDatabase
    
    
    public defaultDatabase: string;

CodeCompilationConfig defaultDatabase.

### defaultLocation
    
    
    public defaultLocation: string;

CodeCompilationConfig defaultLocation.

### defaultNotebookRuntimeOptions
    
    
    public defaultNotebookRuntimeOptions?: (google.cloud.dataform.v1.INotebookRuntimeOptions|null);

CodeCompilationConfig defaultNotebookRuntimeOptions.

### defaultSchema
    
    
    public defaultSchema: string;

CodeCompilationConfig defaultSchema.

### lineageEnabled
    
    
    public lineageEnabled?: (boolean|null);

CodeCompilationConfig lineageEnabled.

### pipelineConfig
    
    
    public pipelineConfig?: (google.cloud.dataform.v1.IPipelineConfig|null);

CodeCompilationConfig pipelineConfig.

### schemaSuffix
    
    
    public schemaSuffix: string;

CodeCompilationConfig schemaSuffix.

### tablePrefix
    
    
    public tablePrefix: string;

CodeCompilationConfig tablePrefix.

### vars
    
    
    public vars: { [k: string]: string };

CodeCompilationConfig vars.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataform.v1.ICodeCompilationConfig): google.cloud.dataform.v1.CodeCompilationConfig;

Creates a new CodeCompilationConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICodeCompilationConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icodecompilationconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CodeCompilationConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.codecompilationconfig)` | CodeCompilationConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataform.v1.CodeCompilationConfig;

Decodes a CodeCompilationConfig message from the specified reader or buffer.

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
`[CodeCompilationConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.codecompilationconfig)` | CodeCompilationConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataform.v1.CodeCompilationConfig;

Decodes a CodeCompilationConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CodeCompilationConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.codecompilationconfig)` | CodeCompilationConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataform.v1.ICodeCompilationConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CodeCompilationConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICodeCompilationConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icodecompilationconfig)`   
CodeCompilationConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataform.v1.ICodeCompilationConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CodeCompilationConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICodeCompilationConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icodecompilationconfig)`   
CodeCompilationConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataform.v1.CodeCompilationConfig;

Creates a CodeCompilationConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CodeCompilationConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.codecompilationconfig)` | CodeCompilationConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CodeCompilationConfig

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

Converts this CodeCompilationConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataform.v1.CodeCompilationConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CodeCompilationConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CodeCompilationConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.codecompilationconfig)`   
CodeCompilationConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CodeCompilationConfig message.

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
