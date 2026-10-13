---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.safetyspec
title: Class protos.google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.SafetySpec (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:40.800666+00:00
---

# Class protos.google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.SafetySpec (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.safetyspec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.SafetySpec (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents a SafetySpec.

## Implements

[protos.google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.ISafetySpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.isafetyspec)

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.ISafetySpec);

Constructs a new SafetySpec.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISafetySpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.isafetyspec)`   
Properties to set  
  
## Properties 

### enable
    
    
    public enable: boolean;

SafetySpec enable.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.ISafetySpec): google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.SafetySpec;

Creates a new SafetySpec instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISafetySpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.isafetyspec)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SafetySpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.safetyspec)` | SafetySpec instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.SafetySpec;

Decodes a SafetySpec message from the specified reader or buffer.

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
`[SafetySpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.safetyspec)` | SafetySpec  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.SafetySpec;

Decodes a SafetySpec message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SafetySpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.safetyspec)` | SafetySpec  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.ISafetySpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SafetySpec message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISafetySpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.isafetyspec)`   
SafetySpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.ISafetySpec, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SafetySpec message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISafetySpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.isafetyspec)`   
SafetySpec message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.SafetySpec;

Creates a SafetySpec message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SafetySpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.safetyspec)` | SafetySpec  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SafetySpec

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

Converts this SafetySpec to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.discoveryengine.v1alpha.AnswerQueryRequest.SafetySpec, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SafetySpec message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SafetySpec](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.answerqueryrequest.safetyspec)`   
SafetySpec  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SafetySpec message.

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
