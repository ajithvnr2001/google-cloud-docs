---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.errortable
title: Class protos.google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.ErrorTable (3.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:16.802723+00:00
---

# Class protos.google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.ErrorTable (3.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.errortable

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.ErrorTable (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

Represents an ErrorTable.

## Implements

[protos.google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.IErrorTable](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.ierrortable)

## Package

[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.IErrorTable);

Constructs a new ErrorTable.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IErrorTable](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.ierrortable)`   
Properties to set  
  
## Properties 

### retentionDays
    
    
    public retentionDays: number;

ErrorTable retentionDays.

### target
    
    
    public target?: (google.cloud.dataform.v1beta1.ITarget|null);

ErrorTable target.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.IErrorTable): google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.ErrorTable;

Creates a new ErrorTable instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IErrorTable](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.ierrortable)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ErrorTable](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.errortable)` | ErrorTable instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.ErrorTable;

Decodes an ErrorTable message from the specified reader or buffer.

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
`[ErrorTable](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.errortable)` | ErrorTable  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.ErrorTable;

Decodes an ErrorTable message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ErrorTable](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.errortable)` | ErrorTable  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.IErrorTable, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ErrorTable message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IErrorTable](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.ierrortable)`   
ErrorTable message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.IErrorTable, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ErrorTable message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IErrorTable](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.ierrortable)`   
ErrorTable message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.ErrorTable;

Creates an ErrorTable message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ErrorTable](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.errortable)` | ErrorTable  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ErrorTable

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

Converts this ErrorTable to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataform.v1beta1.CompilationResultAction.DataPreparation.ErrorTable, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ErrorTable message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ErrorTable](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.compilationresultaction.datapreparation.errortable)`   
ErrorTable  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ErrorTable message.

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
