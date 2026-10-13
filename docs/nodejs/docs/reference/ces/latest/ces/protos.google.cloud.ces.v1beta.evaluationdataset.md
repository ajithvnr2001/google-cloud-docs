---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset
title: Class protos.google.cloud.ces.v1beta.EvaluationDataset (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:24.774232+00:00
---

# Class protos.google.cloud.ces.v1beta.EvaluationDataset (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1beta.EvaluationDataset (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents an EvaluationDataset.

## Implements

[protos.google.cloud.ces.v1beta.IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1beta.IEvaluationDataset);

Constructs a new EvaluationDataset.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset)`   
Properties to set  
  
## Properties 

### aggregatedMetrics
    
    
    public aggregatedMetrics?: (google.cloud.ces.v1beta.IAggregatedMetrics|null);

EvaluationDataset aggregatedMetrics.

### createdBy
    
    
    public createdBy: string;

EvaluationDataset createdBy.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

EvaluationDataset createTime.

### displayName
    
    
    public displayName: string;

EvaluationDataset displayName.

### etag
    
    
    public etag: string;

EvaluationDataset etag.

### evaluations
    
    
    public evaluations: string[];

EvaluationDataset evaluations.

### lastUpdatedBy
    
    
    public lastUpdatedBy: string;

EvaluationDataset lastUpdatedBy.

### name
    
    
    public name: string;

EvaluationDataset name.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

EvaluationDataset updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1beta.IEvaluationDataset): google.cloud.ces.v1beta.EvaluationDataset;

Creates a new EvaluationDataset instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset)` | EvaluationDataset instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1beta.EvaluationDataset;

Decodes an EvaluationDataset message from the specified reader or buffer.

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
`[EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset)` | EvaluationDataset  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1beta.EvaluationDataset;

Decodes an EvaluationDataset message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset)` | EvaluationDataset  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1beta.IEvaluationDataset, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EvaluationDataset message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset)`   
EvaluationDataset message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1beta.IEvaluationDataset, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EvaluationDataset message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.ievaluationdataset)`   
EvaluationDataset message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1beta.EvaluationDataset;

Creates an EvaluationDataset message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset)` | EvaluationDataset  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EvaluationDataset

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

Converts this EvaluationDataset to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1beta.EvaluationDataset, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EvaluationDataset message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EvaluationDataset](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluationdataset)`   
EvaluationDataset  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EvaluationDataset message.

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
