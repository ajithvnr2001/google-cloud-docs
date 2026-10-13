---
url: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.model-class
title: Class protos.google.cloud.automl.v1beta1.Model (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:06.114924+00:00
---

# Class protos.google.cloud.automl.v1beta1.Model (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.model-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.automl.v1beta1.Model (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.3  4.0.1  3.1.2  2.5.2  2.4.5 

Represents a Model.

## Implements

[protos.google.cloud.automl.v1beta1.IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel)

## Package

[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.automl.v1beta1.IModel);

Constructs a new Model.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel)`   
Properties to set  
  
## Properties 

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Model createTime.

### datasetId
    
    
    public datasetId: string;

Model datasetId.

### deploymentState
    
    
    public deploymentState: (google.cloud.automl.v1beta1.Model.DeploymentState|keyof typeof google.cloud.automl.v1beta1.Model.DeploymentState);

Model deploymentState.

### displayName
    
    
    public displayName: string;

Model displayName.

### imageClassificationModelMetadata
    
    
    public imageClassificationModelMetadata?: (google.cloud.automl.v1beta1.IImageClassificationModelMetadata|null);

Model imageClassificationModelMetadata.

### imageObjectDetectionModelMetadata
    
    
    public imageObjectDetectionModelMetadata?: (google.cloud.automl.v1beta1.IImageObjectDetectionModelMetadata|null);

Model imageObjectDetectionModelMetadata.

### modelMetadata
    
    
    public modelMetadata?: ("translationModelMetadata"|"imageClassificationModelMetadata"|"textClassificationModelMetadata"|"imageObjectDetectionModelMetadata"|"videoClassificationModelMetadata"|"videoObjectTrackingModelMetadata"|"textExtractionModelMetadata"|"tablesModelMetadata"|"textSentimentModelMetadata");

Model modelMetadata.

### name
    
    
    public name: string;

Model name.

### tablesModelMetadata
    
    
    public tablesModelMetadata?: (google.cloud.automl.v1beta1.ITablesModelMetadata|null);

Model tablesModelMetadata.

### textClassificationModelMetadata
    
    
    public textClassificationModelMetadata?: (google.cloud.automl.v1beta1.ITextClassificationModelMetadata|null);

Model textClassificationModelMetadata.

### textExtractionModelMetadata
    
    
    public textExtractionModelMetadata?: (google.cloud.automl.v1beta1.ITextExtractionModelMetadata|null);

Model textExtractionModelMetadata.

### textSentimentModelMetadata
    
    
    public textSentimentModelMetadata?: (google.cloud.automl.v1beta1.ITextSentimentModelMetadata|null);

Model textSentimentModelMetadata.

### translationModelMetadata
    
    
    public translationModelMetadata?: (google.cloud.automl.v1beta1.ITranslationModelMetadata|null);

Model translationModelMetadata.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Model updateTime.

### videoClassificationModelMetadata
    
    
    public videoClassificationModelMetadata?: (google.cloud.automl.v1beta1.IVideoClassificationModelMetadata|null);

Model videoClassificationModelMetadata.

### videoObjectTrackingModelMetadata
    
    
    public videoObjectTrackingModelMetadata?: (google.cloud.automl.v1beta1.IVideoObjectTrackingModelMetadata|null);

Model videoObjectTrackingModelMetadata.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.automl.v1beta1.IModel): google.cloud.automl.v1beta1.Model;

Creates a new Model instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.model-class)` | Model instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.automl.v1beta1.Model;

Decodes a Model message from the specified reader or buffer.

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
`[Model](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.model-class)` | Model  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.automl.v1beta1.Model;

Decodes a Model message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.model-class)` | Model  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.automl.v1beta1.IModel, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Model message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel)`   
Model message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.automl.v1beta1.IModel, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Model message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IModel](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.imodel)`   
Model message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.automl.v1beta1.Model;

Creates a Model message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.model-class)` | Model  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Model

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

Converts this Model to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.automl.v1beta1.Model, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Model message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Model](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1beta1.model-class)`   
Model  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Model message.

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
