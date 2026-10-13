---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.compilationerror
title: Class protos.google.cloud.dataform.v1.CompilationResult.CompilationError (3.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:41.714328+00:00
---

# Class protos.google.cloud.dataform.v1.CompilationResult.CompilationError (3.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.compilationerror

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataform.v1.CompilationResult.CompilationError (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

Represents a CompilationError.

## Implements

[protos.google.cloud.dataform.v1.CompilationResult.ICompilationError](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.icompilationerror)

## Package

[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataform.v1.CompilationResult.ICompilationError);

Constructs a new CompilationError.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICompilationError](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.icompilationerror)`   
Properties to set  
  
## Properties 

### actionTarget
    
    
    public actionTarget?: (google.cloud.dataform.v1.ITarget|null);

CompilationError actionTarget.

### message
    
    
    public message: string;

CompilationError message.

### path
    
    
    public path: string;

CompilationError path.

### stack
    
    
    public stack: string;

CompilationError stack.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataform.v1.CompilationResult.ICompilationError): google.cloud.dataform.v1.CompilationResult.CompilationError;

Creates a new CompilationError instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICompilationError](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.icompilationerror)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CompilationError](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.compilationerror)` | CompilationError instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataform.v1.CompilationResult.CompilationError;

Decodes a CompilationError message from the specified reader or buffer.

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
`[CompilationError](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.compilationerror)` | CompilationError  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataform.v1.CompilationResult.CompilationError;

Decodes a CompilationError message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CompilationError](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.compilationerror)` | CompilationError  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataform.v1.CompilationResult.ICompilationError, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CompilationError message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICompilationError](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.icompilationerror)`   
CompilationError message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataform.v1.CompilationResult.ICompilationError, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CompilationError message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICompilationError](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.icompilationerror)`   
CompilationError message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataform.v1.CompilationResult.CompilationError;

Creates a CompilationError message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CompilationError](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.compilationerror)` | CompilationError  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CompilationError

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

Converts this CompilationError to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataform.v1.CompilationResult.CompilationError, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CompilationError message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CompilationError](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.compilationresult.compilationerror)`   
CompilationError  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CompilationError message.

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
