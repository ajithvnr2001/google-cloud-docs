---
url: https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.multispeakerprebuiltvoice
title: Class protos.google.cloud.texttospeech.v1.MultispeakerPrebuiltVoice (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:45.910945+00:00
---

# Class protos.google.cloud.texttospeech.v1.MultispeakerPrebuiltVoice (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.multispeakerprebuiltvoice

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.texttospeech.v1.MultispeakerPrebuiltVoice (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  5.8.0  5.7.0  5.5.0  5.4.0  5.0.2  4.2.2  4.0.4  3.4.0  3.3.1  3.2.7 

Represents a MultispeakerPrebuiltVoice.

## Implements

[protos.google.cloud.texttospeech.v1.IMultispeakerPrebuiltVoice](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.imultispeakerprebuiltvoice)

## Package

[@google-cloud/text-to-speech](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.texttospeech.v1.IMultispeakerPrebuiltVoice);

Constructs a new MultispeakerPrebuiltVoice.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMultispeakerPrebuiltVoice](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.imultispeakerprebuiltvoice)`   
Properties to set  
  
## Properties 

### speakerAlias
    
    
    public speakerAlias: string;

MultispeakerPrebuiltVoice speakerAlias.

### speakerId
    
    
    public speakerId: string;

MultispeakerPrebuiltVoice speakerId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.texttospeech.v1.IMultispeakerPrebuiltVoice): google.cloud.texttospeech.v1.MultispeakerPrebuiltVoice;

Creates a new MultispeakerPrebuiltVoice instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMultispeakerPrebuiltVoice](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.imultispeakerprebuiltvoice)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MultispeakerPrebuiltVoice](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.multispeakerprebuiltvoice)` | MultispeakerPrebuiltVoice instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.texttospeech.v1.MultispeakerPrebuiltVoice;

Decodes a MultispeakerPrebuiltVoice message from the specified reader or buffer.

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
`[MultispeakerPrebuiltVoice](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.multispeakerprebuiltvoice)` | MultispeakerPrebuiltVoice  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.texttospeech.v1.MultispeakerPrebuiltVoice;

Decodes a MultispeakerPrebuiltVoice message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MultispeakerPrebuiltVoice](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.multispeakerprebuiltvoice)` | MultispeakerPrebuiltVoice  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.texttospeech.v1.IMultispeakerPrebuiltVoice, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MultispeakerPrebuiltVoice message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMultispeakerPrebuiltVoice](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.imultispeakerprebuiltvoice)`   
MultispeakerPrebuiltVoice message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.texttospeech.v1.IMultispeakerPrebuiltVoice, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MultispeakerPrebuiltVoice message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMultispeakerPrebuiltVoice](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.imultispeakerprebuiltvoice)`   
MultispeakerPrebuiltVoice message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.texttospeech.v1.MultispeakerPrebuiltVoice;

Creates a MultispeakerPrebuiltVoice message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MultispeakerPrebuiltVoice](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.multispeakerprebuiltvoice)` | MultispeakerPrebuiltVoice  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MultispeakerPrebuiltVoice

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

Converts this MultispeakerPrebuiltVoice to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.texttospeech.v1.MultispeakerPrebuiltVoice, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MultispeakerPrebuiltVoice message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MultispeakerPrebuiltVoice](https://docs.cloud.google.com/nodejs/docs/reference/text-to-speech/latest/text-to-speech/protos.google.cloud.texttospeech.v1.multispeakerprebuiltvoice)`   
MultispeakerPrebuiltVoice  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MultispeakerPrebuiltVoice message.

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
