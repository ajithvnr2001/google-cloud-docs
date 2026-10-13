---
url: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.confidencemetricsentry
title: Class protos.google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:49.110802+00:00
---

# Class protos.google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.confidencemetricsentry

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.2.2  3.1.1  2.3.0  2.2.7 

Represents a ConfidenceMetricsEntry.

## Implements

[protos.google.cloud.datalabeling.v1beta1.PrCurve.IConfidenceMetricsEntry](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.iconfidencemetricsentry)

## Package

[@google-cloud/datalabeling](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datalabeling.v1beta1.PrCurve.IConfidenceMetricsEntry);

Constructs a new ConfidenceMetricsEntry.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConfidenceMetricsEntry](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.iconfidencemetricsentry)`   
Properties to set  
  
## Properties 

### confidenceThreshold
    
    
    public confidenceThreshold: number;

ConfidenceMetricsEntry confidenceThreshold.

### f1Score
    
    
    public f1Score: number;

ConfidenceMetricsEntry f1Score.

### f1ScoreAt1
    
    
    public f1ScoreAt1: number;

ConfidenceMetricsEntry f1ScoreAt1.

### f1ScoreAt5
    
    
    public f1ScoreAt5: number;

ConfidenceMetricsEntry f1ScoreAt5.

### precision
    
    
    public precision: number;

ConfidenceMetricsEntry precision.

### precisionAt1
    
    
    public precisionAt1: number;

ConfidenceMetricsEntry precisionAt1.

### precisionAt5
    
    
    public precisionAt5: number;

ConfidenceMetricsEntry precisionAt5.

### recall
    
    
    public recall: number;

ConfidenceMetricsEntry recall.

### recallAt1
    
    
    public recallAt1: number;

ConfidenceMetricsEntry recallAt1.

### recallAt5
    
    
    public recallAt5: number;

ConfidenceMetricsEntry recallAt5.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datalabeling.v1beta1.PrCurve.IConfidenceMetricsEntry): google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry;

Creates a new ConfidenceMetricsEntry instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConfidenceMetricsEntry](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.iconfidencemetricsentry)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ConfidenceMetricsEntry](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.confidencemetricsentry)` | ConfidenceMetricsEntry instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry;

Decodes a ConfidenceMetricsEntry message from the specified reader or buffer.

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
`[ConfidenceMetricsEntry](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.confidencemetricsentry)` | ConfidenceMetricsEntry  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry;

Decodes a ConfidenceMetricsEntry message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ConfidenceMetricsEntry](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.confidencemetricsentry)` | ConfidenceMetricsEntry  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datalabeling.v1beta1.PrCurve.IConfidenceMetricsEntry, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConfidenceMetricsEntry message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConfidenceMetricsEntry](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.iconfidencemetricsentry)`   
ConfidenceMetricsEntry message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datalabeling.v1beta1.PrCurve.IConfidenceMetricsEntry, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConfidenceMetricsEntry message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConfidenceMetricsEntry](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.iconfidencemetricsentry)`   
ConfidenceMetricsEntry message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry;

Creates a ConfidenceMetricsEntry message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ConfidenceMetricsEntry](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.confidencemetricsentry)` | ConfidenceMetricsEntry  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ConfidenceMetricsEntry

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

Converts this ConfidenceMetricsEntry to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ConfidenceMetricsEntry message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ConfidenceMetricsEntry](https://docs.cloud.google.com/nodejs/docs/reference/datalabeling/latest/datalabeling/protos.google.cloud.datalabeling.v1beta1.prcurve.confidencemetricsentry)`   
ConfidenceMetricsEntry  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ConfidenceMetricsEntry message.

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
