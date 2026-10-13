---
url: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generationconfig
title: Class protos.google.ai.generativelanguage.v1.GenerationConfig (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:05.228227+00:00
---

# Class protos.google.ai.generativelanguage.v1.GenerationConfig (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generationconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ai.generativelanguage.v1.GenerationConfig (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  3.7.0  3.6.0  2.9.0  2.8.0  2.7.0  2.6.0  2.4.0  2.3.0 

Represents a GenerationConfig.

## Implements

[protos.google.ai.generativelanguage.v1.IGenerationConfig](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.igenerationconfig)

## Package

[@google-ai/generativelanguage](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ai.generativelanguage.v1.IGenerationConfig);

Constructs a new GenerationConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGenerationConfig](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.igenerationconfig)`   
Properties to set  
  
## Properties 

### candidateCount
    
    
    public candidateCount?: (number|null);

GenerationConfig candidateCount.

### enableEnhancedCivicAnswers
    
    
    public enableEnhancedCivicAnswers?: (boolean|null);

GenerationConfig enableEnhancedCivicAnswers.

### frequencyPenalty
    
    
    public frequencyPenalty?: (number|null);

GenerationConfig frequencyPenalty.

### logprobs
    
    
    public logprobs?: (number|null);

GenerationConfig logprobs.

### maxOutputTokens
    
    
    public maxOutputTokens?: (number|null);

GenerationConfig maxOutputTokens.

### presencePenalty
    
    
    public presencePenalty?: (number|null);

GenerationConfig presencePenalty.

### responseJsonSchemaOrdered
    
    
    public responseJsonSchemaOrdered?: (google.protobuf.IValue|null);

GenerationConfig responseJsonSchemaOrdered.

### responseLogprobs
    
    
    public responseLogprobs?: (boolean|null);

GenerationConfig responseLogprobs.

### seed
    
    
    public seed?: (number|null);

GenerationConfig seed.

### stopSequences
    
    
    public stopSequences: string[];

GenerationConfig stopSequences.

### temperature
    
    
    public temperature?: (number|null);

GenerationConfig temperature.

### topK
    
    
    public topK?: (number|null);

GenerationConfig topK.

### topP
    
    
    public topP?: (number|null);

GenerationConfig topP.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ai.generativelanguage.v1.IGenerationConfig): google.ai.generativelanguage.v1.GenerationConfig;

Creates a new GenerationConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGenerationConfig](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.igenerationconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GenerationConfig](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generationconfig)` | GenerationConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ai.generativelanguage.v1.GenerationConfig;

Decodes a GenerationConfig message from the specified reader or buffer.

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
`[GenerationConfig](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generationconfig)` | GenerationConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ai.generativelanguage.v1.GenerationConfig;

Decodes a GenerationConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GenerationConfig](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generationconfig)` | GenerationConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.ai.generativelanguage.v1.IGenerationConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GenerationConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGenerationConfig](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.igenerationconfig)`   
GenerationConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ai.generativelanguage.v1.IGenerationConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GenerationConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGenerationConfig](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.igenerationconfig)`   
GenerationConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ai.generativelanguage.v1.GenerationConfig;

Creates a GenerationConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GenerationConfig](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generationconfig)` | GenerationConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GenerationConfig

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

Converts this GenerationConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ai.generativelanguage.v1.GenerationConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GenerationConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GenerationConfig](https://docs.cloud.google.com/nodejs/docs/reference/generativelanguage/latest/generativelanguage/protos.google.ai.generativelanguage.v1.generationconfig)`   
GenerationConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GenerationConfig message.

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
