---
url: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjobconfig
title: Class protos.google.cloud.datalabeling.v1beta1.EvaluationJobConfig (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:53.525869+00:00
---

# Class protos.google.cloud.datalabeling.v1beta1.EvaluationJobConfig (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjobconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datalabeling.v1beta1.EvaluationJobConfig (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.2.2  3.1.1  2.3.0  2.2.7 

Represents an EvaluationJobConfig.

## Implements

[protos.google.cloud.datalabeling.v1beta1.IEvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjobconfig)

## Package

[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datalabeling.v1beta1.IEvaluationJobConfig);

Constructs a new EvaluationJobConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjobconfig)`   
Properties to set  
  
## Properties 

### bigqueryImportKeys
    
    
    public bigqueryImportKeys: { [k: string]: string };

EvaluationJobConfig bigqueryImportKeys.

### boundingPolyConfig
    
    
    public boundingPolyConfig?: (google.cloud.datalabeling.v1beta1.IBoundingPolyConfig|null);

EvaluationJobConfig boundingPolyConfig.

### evaluationConfig
    
    
    public evaluationConfig?: (google.cloud.datalabeling.v1beta1.IEvaluationConfig|null);

EvaluationJobConfig evaluationConfig.

### evaluationJobAlertConfig
    
    
    public evaluationJobAlertConfig?: (google.cloud.datalabeling.v1beta1.IEvaluationJobAlertConfig|null);

EvaluationJobConfig evaluationJobAlertConfig.

### exampleCount
    
    
    public exampleCount: number;

EvaluationJobConfig exampleCount.

### exampleSamplePercentage
    
    
    public exampleSamplePercentage: number;

EvaluationJobConfig exampleSamplePercentage.

### humanAnnotationConfig
    
    
    public humanAnnotationConfig?: (google.cloud.datalabeling.v1beta1.IHumanAnnotationConfig|null);

EvaluationJobConfig humanAnnotationConfig.

### humanAnnotationRequestConfig
    
    
    public humanAnnotationRequestConfig?: ("imageClassificationConfig"|"boundingPolyConfig"|"textClassificationConfig");

EvaluationJobConfig humanAnnotationRequestConfig.

### imageClassificationConfig
    
    
    public imageClassificationConfig?: (google.cloud.datalabeling.v1beta1.IImageClassificationConfig|null);

EvaluationJobConfig imageClassificationConfig.

### inputConfig
    
    
    public inputConfig?: (google.cloud.datalabeling.v1beta1.IInputConfig|null);

EvaluationJobConfig inputConfig.

### textClassificationConfig
    
    
    public textClassificationConfig?: (google.cloud.datalabeling.v1beta1.ITextClassificationConfig|null);

EvaluationJobConfig textClassificationConfig.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datalabeling.v1beta1.IEvaluationJobConfig): google.cloud.datalabeling.v1beta1.EvaluationJobConfig;

Creates a new EvaluationJobConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjobconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjobconfig)` | EvaluationJobConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datalabeling.v1beta1.EvaluationJobConfig;

Decodes an EvaluationJobConfig message from the specified reader or buffer.

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
`[EvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjobconfig)` | EvaluationJobConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datalabeling.v1beta1.EvaluationJobConfig;

Decodes an EvaluationJobConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjobconfig)` | EvaluationJobConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datalabeling.v1beta1.IEvaluationJobConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EvaluationJobConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjobconfig)`   
EvaluationJobConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datalabeling.v1beta1.IEvaluationJobConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EvaluationJobConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.ievaluationjobconfig)`   
EvaluationJobConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datalabeling.v1beta1.EvaluationJobConfig;

Creates an EvaluationJobConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjobconfig)` | EvaluationJobConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EvaluationJobConfig

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

Converts this EvaluationJobConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datalabeling.v1beta1.EvaluationJobConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EvaluationJobConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EvaluationJobConfig](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.evaluationjobconfig)`   
EvaluationJobConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EvaluationJobConfig message.

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
