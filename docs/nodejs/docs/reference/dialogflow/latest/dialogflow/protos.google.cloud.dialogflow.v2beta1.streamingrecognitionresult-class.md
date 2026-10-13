---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.streamingrecognitionresult-class
title: Class protos.google.cloud.dialogflow.v2beta1.StreamingRecognitionResult (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:29.522540+00:00
---

# Class protos.google.cloud.dialogflow.v2beta1.StreamingRecognitionResult (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.streamingrecognitionresult-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2beta1.StreamingRecognitionResult (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a StreamingRecognitionResult.

## Implements

[protos.google.cloud.dialogflow.v2beta1.IStreamingRecognitionResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.istreamingrecognitionresult)

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dialogflow.v2beta1.IStreamingRecognitionResult);

Constructs a new StreamingRecognitionResult.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStreamingRecognitionResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.istreamingrecognitionresult)`   
Properties to set  
  
## Properties 

### confidence
    
    
    public confidence: number;

StreamingRecognitionResult confidence.

### dtmfDigits
    
    
    public dtmfDigits?: (google.cloud.dialogflow.v2beta1.ITelephonyDtmfEvents|null);

StreamingRecognitionResult dtmfDigits.

### isFinal
    
    
    public isFinal: boolean;

StreamingRecognitionResult isFinal.

### languageCode
    
    
    public languageCode: string;

StreamingRecognitionResult languageCode.

### messageType
    
    
    public messageType: (google.cloud.dialogflow.v2beta1.StreamingRecognitionResult.MessageType|keyof typeof google.cloud.dialogflow.v2beta1.StreamingRecognitionResult.MessageType);

StreamingRecognitionResult messageType.

### speechEndOffset
    
    
    public speechEndOffset?: (google.protobuf.IDuration|null);

StreamingRecognitionResult speechEndOffset.

### speechWordInfo
    
    
    public speechWordInfo: google.cloud.dialogflow.v2beta1.ISpeechWordInfo[];

StreamingRecognitionResult speechWordInfo.

### stability
    
    
    public stability: number;

StreamingRecognitionResult stability.

### transcript
    
    
    public transcript: string;

StreamingRecognitionResult transcript.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dialogflow.v2beta1.IStreamingRecognitionResult): google.cloud.dialogflow.v2beta1.StreamingRecognitionResult;

Creates a new StreamingRecognitionResult instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStreamingRecognitionResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.istreamingrecognitionresult)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.streamingrecognitionresult-class)` | StreamingRecognitionResult instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dialogflow.v2beta1.StreamingRecognitionResult;

Decodes a StreamingRecognitionResult message from the specified reader or buffer.

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
`[StreamingRecognitionResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.streamingrecognitionresult-class)` | StreamingRecognitionResult  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dialogflow.v2beta1.StreamingRecognitionResult;

Decodes a StreamingRecognitionResult message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.streamingrecognitionresult-class)` | StreamingRecognitionResult  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dialogflow.v2beta1.IStreamingRecognitionResult, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified StreamingRecognitionResult message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStreamingRecognitionResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.istreamingrecognitionresult)`   
StreamingRecognitionResult message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dialogflow.v2beta1.IStreamingRecognitionResult, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified StreamingRecognitionResult message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStreamingRecognitionResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.istreamingrecognitionresult)`   
StreamingRecognitionResult message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dialogflow.v2beta1.StreamingRecognitionResult;

Creates a StreamingRecognitionResult message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.streamingrecognitionresult-class)` | StreamingRecognitionResult  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for StreamingRecognitionResult

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

Converts this StreamingRecognitionResult to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dialogflow.v2beta1.StreamingRecognitionResult, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a StreamingRecognitionResult message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[StreamingRecognitionResult](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.streamingrecognitionresult-class)`   
StreamingRecognitionResult  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a StreamingRecognitionResult message.

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
