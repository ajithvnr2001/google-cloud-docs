---
url: https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.advancedvoiceoptions
title: Class protos.google.cloud.texttospeech.v1.AdvancedVoiceOptions (5.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:16.860639+00:00
---

# Class protos.google.cloud.texttospeech.v1.AdvancedVoiceOptions (5.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.advancedvoiceoptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.texttospeech.v1.AdvancedVoiceOptions (5.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  5.8.0  5.7.0  5.5.0  5.4.0  5.0.2  4.2.2  4.0.4  3.4.0  3.3.1  3.2.7 

Represents an AdvancedVoiceOptions.

## Package

[@google-cloud/text-to-speech](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.texttospeech.v1.IAdvancedVoiceOptions);

Constructs a new AdvancedVoiceOptions.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdvancedVoiceOptions](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.iadvancedvoiceoptions)`   
Properties to set  
  
## Properties 

### _lowLatencyJourneySynthesis
    
    
    public _lowLatencyJourneySynthesis?: "lowLatencyJourneySynthesis";

AdvancedVoiceOptions _lowLatencyJourneySynthesis.

### lowLatencyJourneySynthesis
    
    
    public lowLatencyJourneySynthesis?: (boolean|null);

AdvancedVoiceOptions lowLatencyJourneySynthesis.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.texttospeech.v1.IAdvancedVoiceOptions): google.cloud.texttospeech.v1.AdvancedVoiceOptions;

Creates a new AdvancedVoiceOptions instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdvancedVoiceOptions](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.iadvancedvoiceoptions)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AdvancedVoiceOptions](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.advancedvoiceoptions)` | AdvancedVoiceOptions instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.texttospeech.v1.AdvancedVoiceOptions;

Decodes an AdvancedVoiceOptions message from the specified reader or buffer.

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
`[AdvancedVoiceOptions](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.advancedvoiceoptions)` | AdvancedVoiceOptions  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.texttospeech.v1.AdvancedVoiceOptions;

Decodes an AdvancedVoiceOptions message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AdvancedVoiceOptions](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.advancedvoiceoptions)` | AdvancedVoiceOptions  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.texttospeech.v1.IAdvancedVoiceOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdvancedVoiceOptions message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdvancedVoiceOptions](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.iadvancedvoiceoptions)`   
AdvancedVoiceOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.texttospeech.v1.IAdvancedVoiceOptions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdvancedVoiceOptions message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdvancedVoiceOptions](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.iadvancedvoiceoptions)`   
AdvancedVoiceOptions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.texttospeech.v1.AdvancedVoiceOptions;

Creates an AdvancedVoiceOptions message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AdvancedVoiceOptions](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.advancedvoiceoptions)` | AdvancedVoiceOptions  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AdvancedVoiceOptions

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

Converts this AdvancedVoiceOptions to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.texttospeech.v1.AdvancedVoiceOptions, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AdvancedVoiceOptions message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AdvancedVoiceOptions](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.advancedvoiceoptions)`   
AdvancedVoiceOptions  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AdvancedVoiceOptions message.

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
