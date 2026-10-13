---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.answerqueryrequest-class
title: Class protos.google.cloud.discoveryengine.v1.AnswerQueryRequest (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:02:34.948585+00:00
---

# Class protos.google.cloud.discoveryengine.v1.AnswerQueryRequest (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.answerqueryrequest-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1.AnswerQueryRequest (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents an AnswerQueryRequest.

## Implements

[protos.google.cloud.discoveryengine.v1.IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ianswerqueryrequest)

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.discoveryengine.v1.IAnswerQueryRequest);

Constructs a new AnswerQueryRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ianswerqueryrequest)`   
Properties to set  
  
## Properties 

### answerGenerationSpec
    
    
    public answerGenerationSpec?: (google.cloud.discoveryengine.v1.AnswerQueryRequest.IAnswerGenerationSpec|null);

AnswerQueryRequest answerGenerationSpec.

### asynchronousMode
    
    
    public asynchronousMode: boolean;

AnswerQueryRequest asynchronousMode.

### endUserSpec
    
    
    public endUserSpec?: (google.cloud.discoveryengine.v1.AnswerQueryRequest.IEndUserSpec|null);

AnswerQueryRequest endUserSpec.

### groundingSpec
    
    
    public groundingSpec?: (google.cloud.discoveryengine.v1.AnswerQueryRequest.IGroundingSpec|null);

AnswerQueryRequest groundingSpec.

### query
    
    
    public query?: (google.cloud.discoveryengine.v1.IQuery|null);

AnswerQueryRequest query.

### queryUnderstandingSpec
    
    
    public queryUnderstandingSpec?: (google.cloud.discoveryengine.v1.AnswerQueryRequest.IQueryUnderstandingSpec|null);

AnswerQueryRequest queryUnderstandingSpec.

### relatedQuestionsSpec
    
    
    public relatedQuestionsSpec?: (google.cloud.discoveryengine.v1.AnswerQueryRequest.IRelatedQuestionsSpec|null);

AnswerQueryRequest relatedQuestionsSpec.

### safetySpec
    
    
    public safetySpec?: (google.cloud.discoveryengine.v1.AnswerQueryRequest.ISafetySpec|null);

AnswerQueryRequest safetySpec.

### searchSpec
    
    
    public searchSpec?: (google.cloud.discoveryengine.v1.AnswerQueryRequest.ISearchSpec|null);

AnswerQueryRequest searchSpec.

### servingConfig
    
    
    public servingConfig: string;

AnswerQueryRequest servingConfig.

### session
    
    
    public session: string;

AnswerQueryRequest session.

### userLabels
    
    
    public userLabels: { [k: string]: string };

AnswerQueryRequest userLabels.

### userPseudoId
    
    
    public userPseudoId: string;

AnswerQueryRequest userPseudoId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.discoveryengine.v1.IAnswerQueryRequest): google.cloud.discoveryengine.v1.AnswerQueryRequest;

Creates a new AnswerQueryRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ianswerqueryrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.answerqueryrequest-class)` | AnswerQueryRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.discoveryengine.v1.AnswerQueryRequest;

Decodes an AnswerQueryRequest message from the specified reader or buffer.

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
`[AnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.answerqueryrequest-class)` | AnswerQueryRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.discoveryengine.v1.AnswerQueryRequest;

Decodes an AnswerQueryRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.answerqueryrequest-class)` | AnswerQueryRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.discoveryengine.v1.IAnswerQueryRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnswerQueryRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ianswerqueryrequest)`   
AnswerQueryRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.discoveryengine.v1.IAnswerQueryRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnswerQueryRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.ianswerqueryrequest)`   
AnswerQueryRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.discoveryengine.v1.AnswerQueryRequest;

Creates an AnswerQueryRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.answerqueryrequest-class)` | AnswerQueryRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AnswerQueryRequest

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

Converts this AnswerQueryRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.discoveryengine.v1.AnswerQueryRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AnswerQueryRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AnswerQueryRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1.answerqueryrequest-class)`   
AnswerQueryRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AnswerQueryRequest message.

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
