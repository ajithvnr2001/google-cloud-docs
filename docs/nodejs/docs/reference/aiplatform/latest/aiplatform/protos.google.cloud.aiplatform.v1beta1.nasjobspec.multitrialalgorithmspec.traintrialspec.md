---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.traintrialspec
title: Class protos.google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:48.453098+00:00
---

# Class protos.google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.traintrialspec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Represents a TrainTrialSpec.

## Implements

[protos.google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.ITrainTrialSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.itraintrialspec)

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.ITrainTrialSpec);

Constructs a new TrainTrialSpec.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITrainTrialSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.itraintrialspec)`   
Properties to set  
  
## Properties 

### frequency
    
    
    public frequency: number;

TrainTrialSpec frequency.

### maxParallelTrialCount
    
    
    public maxParallelTrialCount: number;

TrainTrialSpec maxParallelTrialCount.

### trainTrialJobSpec
    
    
    public trainTrialJobSpec?: (google.cloud.aiplatform.v1beta1.ICustomJobSpec|null);

TrainTrialSpec trainTrialJobSpec.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.ITrainTrialSpec): google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec;

Creates a new TrainTrialSpec instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITrainTrialSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.itraintrialspec)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[TrainTrialSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.traintrialspec)` | TrainTrialSpec instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec;

Decodes a TrainTrialSpec message from the specified reader or buffer.

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
`[TrainTrialSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.traintrialspec)` | TrainTrialSpec  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec;

Decodes a TrainTrialSpec message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[TrainTrialSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.traintrialspec)` | TrainTrialSpec  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.ITrainTrialSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TrainTrialSpec message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITrainTrialSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.itraintrialspec)`   
TrainTrialSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.ITrainTrialSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified TrainTrialSpec message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITrainTrialSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.itraintrialspec)`   
TrainTrialSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec;

Creates a TrainTrialSpec message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[TrainTrialSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.traintrialspec)` | TrainTrialSpec  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for TrainTrialSpec

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

Converts this TrainTrialSpec to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.aiplatform.v1beta1.NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a TrainTrialSpec message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[TrainTrialSpec](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.nasjobspec.multitrialalgorithmspec.traintrialspec)`   
TrainTrialSpec  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a TrainTrialSpec message.

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
