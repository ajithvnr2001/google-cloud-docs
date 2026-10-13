---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.boostspec-class
title: Class protos.google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:21.465618+00:00
---

# Class protos.google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.boostspec-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a BoostSpec.

## Implements

[protos.google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.IBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.iboostspec)

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.IBoostSpec);

Constructs a new BoostSpec.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.iboostspec)`   
Properties to set  
  
## Properties 

### conditionBoostSpecs
    
    
    public conditionBoostSpecs: google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.IConditionBoostSpec[];

BoostSpec conditionBoostSpecs.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.IBoostSpec): google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec;

Creates a new BoostSpec instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.iboostspec)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.boostspec-class)` | BoostSpec instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec;

Decodes a BoostSpec message from the specified reader or buffer.

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
`[BoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.boostspec-class)` | BoostSpec  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec;

Decodes a BoostSpec message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.boostspec-class)` | BoostSpec  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.IBoostSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BoostSpec message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.iboostspec)`   
BoostSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.IBoostSpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BoostSpec message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.iboostspec)`   
BoostSpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec;

Creates a BoostSpec message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.boostspec-class)` | BoostSpec  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BoostSpec

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

Converts this BoostSpec to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dialogflow.v2.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BoostSpec message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BoostSpec](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.searchknowledgerequest.searchconfig.boostspecs.boostspec-class)`   
BoostSpec  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BoostSpec message.

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
