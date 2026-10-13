---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.goldenexpectation
title: Class protos.google.cloud.ces.v1beta.Evaluation.GoldenExpectation (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:50.863436+00:00
---

# Class protos.google.cloud.ces.v1beta.Evaluation.GoldenExpectation (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.goldenexpectation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1beta.Evaluation.GoldenExpectation (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents a GoldenExpectation.

## Implements

[protos.google.cloud.ces.v1beta.Evaluation.IGoldenExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.igoldenexpectation)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1beta.Evaluation.IGoldenExpectation);

Constructs a new GoldenExpectation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGoldenExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.igoldenexpectation)`   
Properties to set  
  
## Properties 

### agentResponse
    
    
    public agentResponse?: (google.cloud.ces.v1beta.IMessage|null);

GoldenExpectation agentResponse.

### agentResponseHallucinationMetricsConfigOverride
    
    
    public agentResponseHallucinationMetricsConfigOverride?: (google.cloud.ces.v1beta.EvaluationMetricsConfig.IHallucinationMetricsConfig|null);

GoldenExpectation agentResponseHallucinationMetricsConfigOverride.

### agentResponseSemanticSimilarityMetricsConfigOverride
    
    
    public agentResponseSemanticSimilarityMetricsConfigOverride?: (google.cloud.ces.v1beta.EvaluationMetricsConfig.ISemanticSimilarityMetricsConfig|null);

GoldenExpectation agentResponseSemanticSimilarityMetricsConfigOverride.

### agentTransfer
    
    
    public agentTransfer?: (google.cloud.ces.v1beta.IAgentTransfer|null);

GoldenExpectation agentTransfer.

### comparisonType
    
    
    public comparisonType: (google.cloud.ces.v1beta.EvaluationMetricsConfig.ComparisonType|keyof typeof google.cloud.ces.v1beta.EvaluationMetricsConfig.ComparisonType);

GoldenExpectation comparisonType.

### condition
    
    
    public condition?: ("toolCall"|"toolResponse"|"agentResponse"|"agentTransfer"|"updatedVariables"|"mockToolResponse"|"noToolCalls");

GoldenExpectation condition.

### expectationLevelMetricsThresholdsOverride
    
    
    public expectationLevelMetricsThresholdsOverride?: (google.cloud.ces.v1beta.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.IExpectationLevelMetricsThresholds|null);

GoldenExpectation expectationLevelMetricsThresholdsOverride.

### mockToolResponse
    
    
    public mockToolResponse?: (google.cloud.ces.v1beta.IToolResponse|null);

GoldenExpectation mockToolResponse.

### note
    
    
    public note: string;

GoldenExpectation note.

### noToolCalls
    
    
    public noToolCalls?: (boolean|null);

GoldenExpectation noToolCalls.

### skipEvaluation
    
    
    public skipEvaluation: boolean;

GoldenExpectation skipEvaluation.

### toolCall
    
    
    public toolCall?: (google.cloud.ces.v1beta.IToolCall|null);

GoldenExpectation toolCall.

### toolResponse
    
    
    public toolResponse?: (google.cloud.ces.v1beta.IToolResponse|null);

GoldenExpectation toolResponse.

### updatedVariables
    
    
    public updatedVariables?: (google.protobuf.IStruct|null);

GoldenExpectation updatedVariables.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1beta.Evaluation.IGoldenExpectation): google.cloud.ces.v1beta.Evaluation.GoldenExpectation;

Creates a new GoldenExpectation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGoldenExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.igoldenexpectation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GoldenExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.goldenexpectation)` | GoldenExpectation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1beta.Evaluation.GoldenExpectation;

Decodes a GoldenExpectation message from the specified reader or buffer.

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
`[GoldenExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.goldenexpectation)` | GoldenExpectation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1beta.Evaluation.GoldenExpectation;

Decodes a GoldenExpectation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GoldenExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.goldenexpectation)` | GoldenExpectation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1beta.Evaluation.IGoldenExpectation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GoldenExpectation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGoldenExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.igoldenexpectation)`   
GoldenExpectation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1beta.Evaluation.IGoldenExpectation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GoldenExpectation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGoldenExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.igoldenexpectation)`   
GoldenExpectation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1beta.Evaluation.GoldenExpectation;

Creates a GoldenExpectation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GoldenExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.goldenexpectation)` | GoldenExpectation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GoldenExpectation

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

Converts this GoldenExpectation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1beta.Evaluation.GoldenExpectation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GoldenExpectation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GoldenExpectation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1beta.evaluation.goldenexpectation)`   
GoldenExpectation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GoldenExpectation message.

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
