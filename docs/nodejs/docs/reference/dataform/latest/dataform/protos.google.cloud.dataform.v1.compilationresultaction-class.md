---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresultaction-class
title: Class protos.google.cloud.dataform.v1.CompilationResultAction (3.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:13.009459+00:00
---

# Class protos.google.cloud.dataform.v1.CompilationResultAction (3.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresultaction-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataform.v1.CompilationResultAction (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

Represents a CompilationResultAction.

## Implements

[protos.google.cloud.dataform.v1.ICompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icompilationresultaction)

## Package

[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataform.v1.ICompilationResultAction);

Constructs a new CompilationResultAction.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icompilationresultaction)`   
Properties to set  
  
## Properties 

### assertion
    
    
    public assertion?: (google.cloud.dataform.v1.CompilationResultAction.IAssertion|null);

CompilationResultAction assertion.

### canonicalTarget
    
    
    public canonicalTarget?: (google.cloud.dataform.v1.ITarget|null);

CompilationResultAction canonicalTarget.

### compiledObject
    
    
    public compiledObject?: ("relation"|"operations"|"assertion"|"declaration"|"notebook"|"dataPreparation");

CompilationResultAction compiledObject.

### dataPreparation
    
    
    public dataPreparation?: (google.cloud.dataform.v1.CompilationResultAction.IDataPreparation|null);

CompilationResultAction dataPreparation.

### declaration
    
    
    public declaration?: (google.cloud.dataform.v1.CompilationResultAction.IDeclaration|null);

CompilationResultAction declaration.

### filePath
    
    
    public filePath: string;

CompilationResultAction filePath.

### internalMetadata
    
    
    public internalMetadata?: (string|null);

CompilationResultAction internalMetadata.

### notebook
    
    
    public notebook?: (google.cloud.dataform.v1.CompilationResultAction.INotebook|null);

CompilationResultAction notebook.

### operations
    
    
    public operations?: (google.cloud.dataform.v1.CompilationResultAction.IOperations|null);

CompilationResultAction operations.

### relation
    
    
    public relation?: (google.cloud.dataform.v1.CompilationResultAction.IRelation|null);

CompilationResultAction relation.

### target
    
    
    public target?: (google.cloud.dataform.v1.ITarget|null);

CompilationResultAction target.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataform.v1.ICompilationResultAction): google.cloud.dataform.v1.CompilationResultAction;

Creates a new CompilationResultAction instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icompilationresultaction)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresultaction-class)` | CompilationResultAction instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataform.v1.CompilationResultAction;

Decodes a CompilationResultAction message from the specified reader or buffer.

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
`[CompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresultaction-class)` | CompilationResultAction  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataform.v1.CompilationResultAction;

Decodes a CompilationResultAction message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresultaction-class)` | CompilationResultAction  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataform.v1.ICompilationResultAction, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CompilationResultAction message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icompilationresultaction)`   
CompilationResultAction message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataform.v1.ICompilationResultAction, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CompilationResultAction message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icompilationresultaction)`   
CompilationResultAction message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataform.v1.CompilationResultAction;

Creates a CompilationResultAction message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresultaction-class)` | CompilationResultAction  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CompilationResultAction

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

Converts this CompilationResultAction to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataform.v1.CompilationResultAction, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CompilationResultAction message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CompilationResultAction](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresultaction-class)`   
CompilationResultAction  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CompilationResultAction message.

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
