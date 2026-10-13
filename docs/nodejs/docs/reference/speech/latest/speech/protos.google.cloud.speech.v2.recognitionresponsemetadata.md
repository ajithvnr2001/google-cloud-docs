---
url: https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.recognitionresponsemetadata
title: Class protos.google.cloud.speech.v2.RecognitionResponseMetadata (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:26.693511+00:00
---

# Class protos.google.cloud.speech.v2.RecognitionResponseMetadata (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.recognitionresponsemetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.speech.v2.RecognitionResponseMetadata (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.5.0  7.4.0  6.6.1  6.3.0  6.1.1  6.0.1  5.4.1  5.3.1  5.1.0  5.0.3  4.10.0  4.9.0  4.8.1  4.7.0  4.6.1  4.5.6  4.1.3 

Represents a RecognitionResponseMetadata.

## Implements

[protos.google.cloud.speech.v2.IRecognitionResponseMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.irecognitionresponsemetadata)

## Package

[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.speech.v2.IRecognitionResponseMetadata);

Constructs a new RecognitionResponseMetadata.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRecognitionResponseMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.irecognitionresponsemetadata)`   
Properties to set  
  
## Properties 

### prompt
    
    
    public prompt?: (string|null);

RecognitionResponseMetadata prompt.

### requestId
    
    
    public requestId: string;

RecognitionResponseMetadata requestId.

### totalBilledDuration
    
    
    public totalBilledDuration?: (google.protobuf.IDuration|null);

RecognitionResponseMetadata totalBilledDuration.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.speech.v2.IRecognitionResponseMetadata): google.cloud.speech.v2.RecognitionResponseMetadata;

Creates a new RecognitionResponseMetadata instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRecognitionResponseMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.irecognitionresponsemetadata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RecognitionResponseMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.recognitionresponsemetadata)` | RecognitionResponseMetadata instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.speech.v2.RecognitionResponseMetadata;

Decodes a RecognitionResponseMetadata message from the specified reader or buffer.

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
`[RecognitionResponseMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.recognitionresponsemetadata)` | RecognitionResponseMetadata  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.speech.v2.RecognitionResponseMetadata;

Decodes a RecognitionResponseMetadata message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RecognitionResponseMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.recognitionresponsemetadata)` | RecognitionResponseMetadata  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.speech.v2.IRecognitionResponseMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RecognitionResponseMetadata message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRecognitionResponseMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.irecognitionresponsemetadata)`   
RecognitionResponseMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.speech.v2.IRecognitionResponseMetadata, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RecognitionResponseMetadata message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRecognitionResponseMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.irecognitionresponsemetadata)`   
RecognitionResponseMetadata message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.speech.v2.RecognitionResponseMetadata;

Creates a RecognitionResponseMetadata message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RecognitionResponseMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.recognitionresponsemetadata)` | RecognitionResponseMetadata  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RecognitionResponseMetadata

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

Converts this RecognitionResponseMetadata to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.speech.v2.RecognitionResponseMetadata, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RecognitionResponseMetadata message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RecognitionResponseMetadata](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.recognitionresponsemetadata)`   
RecognitionResponseMetadata  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RecognitionResponseMetadata message.

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
