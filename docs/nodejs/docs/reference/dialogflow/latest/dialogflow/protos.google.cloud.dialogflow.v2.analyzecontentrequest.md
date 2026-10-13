---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.analyzecontentrequest
title: Class protos.google.cloud.dialogflow.v2.AnalyzeContentRequest (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:09.862811+00:00
---

# Class protos.google.cloud.dialogflow.v2.AnalyzeContentRequest (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.analyzecontentrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.AnalyzeContentRequest (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents an AnalyzeContentRequest.

## Implements

[protos.google.cloud.dialogflow.v2.IAnalyzeContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ianalyzecontentrequest)

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dialogflow.v2.IAnalyzeContentRequest);

Constructs a new AnalyzeContentRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnalyzeContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ianalyzecontentrequest)`   
Properties to set  
  
## Properties 

### assistQueryParams
    
    
    public assistQueryParams?: (google.cloud.dialogflow.v2.IAssistQueryParameters|null);

AnalyzeContentRequest assistQueryParams.

### audioInput
    
    
    public audioInput?: (google.cloud.dialogflow.v2.IAudioInput|null);

AnalyzeContentRequest audioInput.

### cxParameters
    
    
    public cxParameters?: (google.protobuf.IStruct|null);

AnalyzeContentRequest cxParameters.

### eventInput
    
    
    public eventInput?: (google.cloud.dialogflow.v2.IEventInput|null);

AnalyzeContentRequest eventInput.

### input
    
    
    public input?: ("textInput"|"audioInput"|"eventInput"|"suggestionInput");

AnalyzeContentRequest input.

### participant
    
    
    public participant: string;

AnalyzeContentRequest participant.

### queryParams
    
    
    public queryParams?: (google.cloud.dialogflow.v2.IQueryParameters|null);

AnalyzeContentRequest queryParams.

### replyAudioConfig
    
    
    public replyAudioConfig?: (google.cloud.dialogflow.v2.IOutputAudioConfig|null);

AnalyzeContentRequest replyAudioConfig.

### requestId
    
    
    public requestId: string;

AnalyzeContentRequest requestId.

### suggestionInput
    
    
    public suggestionInput?: (google.cloud.dialogflow.v2.ISuggestionInput|null);

AnalyzeContentRequest suggestionInput.

### textInput
    
    
    public textInput?: (google.cloud.dialogflow.v2.ITextInput|null);

AnalyzeContentRequest textInput.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dialogflow.v2.IAnalyzeContentRequest): google.cloud.dialogflow.v2.AnalyzeContentRequest;

Creates a new AnalyzeContentRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAnalyzeContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ianalyzecontentrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.analyzecontentrequest)` | AnalyzeContentRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dialogflow.v2.AnalyzeContentRequest;

Decodes an AnalyzeContentRequest message from the specified reader or buffer.

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
`[AnalyzeContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.analyzecontentrequest)` | AnalyzeContentRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dialogflow.v2.AnalyzeContentRequest;

Decodes an AnalyzeContentRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.analyzecontentrequest)` | AnalyzeContentRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dialogflow.v2.IAnalyzeContentRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnalyzeContentRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnalyzeContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ianalyzecontentrequest)`   
AnalyzeContentRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dialogflow.v2.IAnalyzeContentRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AnalyzeContentRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAnalyzeContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ianalyzecontentrequest)`   
AnalyzeContentRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dialogflow.v2.AnalyzeContentRequest;

Creates an AnalyzeContentRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.analyzecontentrequest)` | AnalyzeContentRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AnalyzeContentRequest

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

Converts this AnalyzeContentRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dialogflow.v2.AnalyzeContentRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AnalyzeContentRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AnalyzeContentRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.analyzecontentrequest)`   
AnalyzeContentRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AnalyzeContentRequest message.

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
