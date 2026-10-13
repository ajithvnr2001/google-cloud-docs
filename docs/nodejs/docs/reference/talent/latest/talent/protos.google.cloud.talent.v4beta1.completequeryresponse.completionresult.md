---
url: https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.completionresult
title: Class protos.google.cloud.talent.v4beta1.CompleteQueryResponse.CompletionResult (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:21.747987+00:00
---

# Class protos.google.cloud.talent.v4beta1.CompleteQueryResponse.CompletionResult (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.completionresult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.talent.v4beta1.CompleteQueryResponse.CompletionResult (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  7.2.0  6.4.0  6.3.1  6.0.2  5.1.3  5.0.1  4.1.1  3.5.1  3.4.1  3.3.0  3.2.7 

Represents a CompletionResult.

## Implements

[protos.google.cloud.talent.v4beta1.CompleteQueryResponse.ICompletionResult](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.icompletionresult)

## Package

[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.talent.v4beta1.CompleteQueryResponse.ICompletionResult);

Constructs a new CompletionResult.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICompletionResult](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.icompletionresult)`   
Properties to set  
  
## Properties 

### imageUri
    
    
    public imageUri: string;

CompletionResult imageUri.

### suggestion
    
    
    public suggestion: string;

CompletionResult suggestion.

### type
    
    
    public type: (google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionType|keyof typeof google.cloud.talent.v4beta1.CompleteQueryRequest.CompletionType);

CompletionResult type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.talent.v4beta1.CompleteQueryResponse.ICompletionResult): google.cloud.talent.v4beta1.CompleteQueryResponse.CompletionResult;

Creates a new CompletionResult instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICompletionResult](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.icompletionresult)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CompletionResult](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.completionresult)` | CompletionResult instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.talent.v4beta1.CompleteQueryResponse.CompletionResult;

Decodes a CompletionResult message from the specified reader or buffer.

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
`[CompletionResult](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.completionresult)` | CompletionResult  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.talent.v4beta1.CompleteQueryResponse.CompletionResult;

Decodes a CompletionResult message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CompletionResult](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.completionresult)` | CompletionResult  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.talent.v4beta1.CompleteQueryResponse.ICompletionResult, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CompletionResult message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICompletionResult](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.icompletionresult)`   
CompletionResult message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.talent.v4beta1.CompleteQueryResponse.ICompletionResult, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CompletionResult message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICompletionResult](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.icompletionresult)`   
CompletionResult message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.talent.v4beta1.CompleteQueryResponse.CompletionResult;

Creates a CompletionResult message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CompletionResult](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.completionresult)` | CompletionResult  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CompletionResult

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

Converts this CompletionResult to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.talent.v4beta1.CompleteQueryResponse.CompletionResult, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CompletionResult message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CompletionResult](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.completequeryresponse.completionresult)`   
CompletionResult  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CompletionResult message.

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
