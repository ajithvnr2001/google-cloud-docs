---
url: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation
title: Class protos.google.cloud.automl.v1beta1.ModelEvaluation (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:05.792197+00:00
---

# Class protos.google.cloud.automl.v1beta1.ModelEvaluation (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.automl.v1beta1.ModelEvaluation (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.3  4.0.1  3.1.2  2.5.2  2.4.5 

Represents a ModelEvaluation.

## Implements

[protos.google.cloud.automl.v1beta1.IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation)

## Package

[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.automl.v1beta1.IModelEvaluation);

Constructs a new ModelEvaluation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation)`   
Properties to set  
  
## Properties 

### annotationSpecId
    
    
    public annotationSpecId: string;

ModelEvaluation annotationSpecId.

### classificationEvaluationMetrics
    
    
    public classificationEvaluationMetrics?: (google.cloud.automl.v1beta1.IClassificationEvaluationMetrics|null);

ModelEvaluation classificationEvaluationMetrics.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

ModelEvaluation createTime.

### displayName
    
    
    public displayName: string;

ModelEvaluation displayName.

### evaluatedExampleCount
    
    
    public evaluatedExampleCount: number;

ModelEvaluation evaluatedExampleCount.

### imageObjectDetectionEvaluationMetrics
    
    
    public imageObjectDetectionEvaluationMetrics?: (google.cloud.automl.v1beta1.IImageObjectDetectionEvaluationMetrics|null);

ModelEvaluation imageObjectDetectionEvaluationMetrics.

### metrics
    
    
    public metrics?: ("classificationEvaluationMetrics"|"regressionEvaluationMetrics"|"translationEvaluationMetrics"|"imageObjectDetectionEvaluationMetrics"|"videoObjectTrackingEvaluationMetrics"|"textSentimentEvaluationMetrics"|"textExtractionEvaluationMetrics");

ModelEvaluation metrics.

### name
    
    
    public name: string;

ModelEvaluation name.

### regressionEvaluationMetrics
    
    
    public regressionEvaluationMetrics?: (google.cloud.automl.v1beta1.IRegressionEvaluationMetrics|null);

ModelEvaluation regressionEvaluationMetrics.

### textExtractionEvaluationMetrics
    
    
    public textExtractionEvaluationMetrics?: (google.cloud.automl.v1beta1.ITextExtractionEvaluationMetrics|null);

ModelEvaluation textExtractionEvaluationMetrics.

### textSentimentEvaluationMetrics
    
    
    public textSentimentEvaluationMetrics?: (google.cloud.automl.v1beta1.ITextSentimentEvaluationMetrics|null);

ModelEvaluation textSentimentEvaluationMetrics.

### translationEvaluationMetrics
    
    
    public translationEvaluationMetrics?: (google.cloud.automl.v1beta1.ITranslationEvaluationMetrics|null);

ModelEvaluation translationEvaluationMetrics.

### videoObjectTrackingEvaluationMetrics
    
    
    public videoObjectTrackingEvaluationMetrics?: (google.cloud.automl.v1beta1.IVideoObjectTrackingEvaluationMetrics|null);

ModelEvaluation videoObjectTrackingEvaluationMetrics.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.automl.v1beta1.IModelEvaluation): google.cloud.automl.v1beta1.ModelEvaluation;

Creates a new ModelEvaluation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation)` | ModelEvaluation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.automl.v1beta1.ModelEvaluation;

Decodes a ModelEvaluation message from the specified reader or buffer.

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
`[ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation)` | ModelEvaluation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.automl.v1beta1.ModelEvaluation;

Decodes a ModelEvaluation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation)` | ModelEvaluation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.automl.v1beta1.IModelEvaluation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ModelEvaluation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation)`   
ModelEvaluation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.automl.v1beta1.IModelEvaluation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ModelEvaluation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodelevaluation)`   
ModelEvaluation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.automl.v1beta1.ModelEvaluation;

Creates a ModelEvaluation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation)` | ModelEvaluation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ModelEvaluation

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

Converts this ModelEvaluation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.automl.v1beta1.ModelEvaluation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ModelEvaluation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ModelEvaluation](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.modelevaluation)`   
ModelEvaluation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ModelEvaluation message.

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
