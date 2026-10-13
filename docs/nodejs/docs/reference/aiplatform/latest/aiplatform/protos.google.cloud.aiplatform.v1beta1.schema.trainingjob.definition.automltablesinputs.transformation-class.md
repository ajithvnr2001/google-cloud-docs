---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.transformation-class
title: Class protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:12.156952+00:00
---

# Class protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.transformation-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a Transformation.

## Implements

[protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.ITransformation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.itransformation)

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.ITransformation);

Constructs a new Transformation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITransformation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.itransformation)`   
Properties to set  
  
## Properties 

### auto
    
    
    public auto?: (google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.IAutoTransformation|null);

Transformation auto.

### categorical
    
    
    public categorical?: (google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.ICategoricalTransformation|null);

Transformation categorical.

### numeric
    
    
    public numeric?: (google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.INumericTransformation|null);

Transformation numeric.

### repeatedCategorical
    
    
    public repeatedCategorical?: (google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.ICategoricalArrayTransformation|null);

Transformation repeatedCategorical.

### repeatedNumeric
    
    
    public repeatedNumeric?: (google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.INumericArrayTransformation|null);

Transformation repeatedNumeric.

### repeatedText
    
    
    public repeatedText?: (google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.ITextArrayTransformation|null);

Transformation repeatedText.

### text
    
    
    public text?: (google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.ITextTransformation|null);

Transformation text.

### timestamp
    
    
    public timestamp?: (google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.ITimestampTransformation|null);

Transformation timestamp.

### transformationDetail
    
    
    public transformationDetail?: ("auto"|"numeric"|"categorical"|"timestamp"|"text"|"repeatedNumeric"|"repeatedCategorical"|"repeatedText");

Transformation transformationDetail.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.ITransformation): google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation;

Creates a new Transformation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITransformation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.itransformation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Transformation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.transformation-class)` | Transformation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation;

Decodes a Transformation message from the specified reader or buffer.

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
`[Transformation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.transformation-class)` | Transformation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation;

Decodes a Transformation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Transformation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.transformation-class)` | Transformation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.ITransformation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Transformation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITransformation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.itransformation)`   
Transformation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.ITransformation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Transformation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITransformation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.itransformation)`   
Transformation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation;

Creates a Transformation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Transformation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.transformation-class)` | Transformation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Transformation

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

Converts this Transformation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Transformation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Transformation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.schema.trainingjob.definition.automltablesinputs.transformation-class)`   
Transformation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Transformation message.

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
