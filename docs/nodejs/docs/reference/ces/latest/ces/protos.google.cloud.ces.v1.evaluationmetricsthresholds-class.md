---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.evaluationmetricsthresholds-class
title: Class protos.google.cloud.ces.v1.EvaluationMetricsThresholds (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:15.425170+00:00
---

# Class protos.google.cloud.ces.v1.EvaluationMetricsThresholds (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.evaluationmetricsthresholds-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.EvaluationMetricsThresholds (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents an EvaluationMetricsThresholds.

## Implements

[protos.google.cloud.ces.v1.IEvaluationMetricsThresholds](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ievaluationmetricsthresholds)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IEvaluationMetricsThresholds);

Constructs a new EvaluationMetricsThresholds.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEvaluationMetricsThresholds](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ievaluationmetricsthresholds)`   
Properties to set  
  
## Properties 

### goldenEvaluationMetricsThresholds
    
    
    public goldenEvaluationMetricsThresholds?: (google.cloud.ces.v1.EvaluationMetricsThresholds.IGoldenEvaluationMetricsThresholds|null);

EvaluationMetricsThresholds goldenEvaluationMetricsThresholds.

### goldenHallucinationMetricBehavior
    
    
    public goldenHallucinationMetricBehavior: (google.cloud.ces.v1.EvaluationMetricsThresholds.HallucinationMetricBehavior|keyof typeof google.cloud.ces.v1.EvaluationMetricsThresholds.HallucinationMetricBehavior);

EvaluationMetricsThresholds goldenHallucinationMetricBehavior.

### hallucinationMetricBehavior
    
    
    public hallucinationMetricBehavior: (google.cloud.ces.v1.EvaluationMetricsThresholds.HallucinationMetricBehavior|keyof typeof google.cloud.ces.v1.EvaluationMetricsThresholds.HallucinationMetricBehavior);

EvaluationMetricsThresholds hallucinationMetricBehavior.

### scenarioHallucinationMetricBehavior
    
    
    public scenarioHallucinationMetricBehavior: (google.cloud.ces.v1.EvaluationMetricsThresholds.HallucinationMetricBehavior|keyof typeof google.cloud.ces.v1.EvaluationMetricsThresholds.HallucinationMetricBehavior);

EvaluationMetricsThresholds scenarioHallucinationMetricBehavior.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IEvaluationMetricsThresholds): google.cloud.ces.v1.EvaluationMetricsThresholds;

Creates a new EvaluationMetricsThresholds instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEvaluationMetricsThresholds](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ievaluationmetricsthresholds)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EvaluationMetricsThresholds](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.evaluationmetricsthresholds-class)` | EvaluationMetricsThresholds instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.EvaluationMetricsThresholds;

Decodes an EvaluationMetricsThresholds message from the specified reader or buffer.

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
`[EvaluationMetricsThresholds](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.evaluationmetricsthresholds-class)` | EvaluationMetricsThresholds  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.EvaluationMetricsThresholds;

Decodes an EvaluationMetricsThresholds message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EvaluationMetricsThresholds](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.evaluationmetricsthresholds-class)` | EvaluationMetricsThresholds  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IEvaluationMetricsThresholds, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EvaluationMetricsThresholds message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEvaluationMetricsThresholds](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ievaluationmetricsthresholds)`   
EvaluationMetricsThresholds message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IEvaluationMetricsThresholds, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EvaluationMetricsThresholds message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEvaluationMetricsThresholds](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.ievaluationmetricsthresholds)`   
EvaluationMetricsThresholds message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.EvaluationMetricsThresholds;

Creates an EvaluationMetricsThresholds message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EvaluationMetricsThresholds](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.evaluationmetricsthresholds-class)` | EvaluationMetricsThresholds  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EvaluationMetricsThresholds

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

Converts this EvaluationMetricsThresholds to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.EvaluationMetricsThresholds, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EvaluationMetricsThresholds message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EvaluationMetricsThresholds](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.evaluationmetricsthresholds-class)`   
EvaluationMetricsThresholds  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EvaluationMetricsThresholds message.

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
