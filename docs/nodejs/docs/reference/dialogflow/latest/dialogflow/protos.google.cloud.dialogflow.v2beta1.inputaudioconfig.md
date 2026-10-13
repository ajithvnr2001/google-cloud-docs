---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.inputaudioconfig
title: Class protos.google.cloud.dialogflow.v2beta1.InputAudioConfig (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:17.999688+00:00
---

# Class protos.google.cloud.dialogflow.v2beta1.InputAudioConfig (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.inputaudioconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2beta1.InputAudioConfig (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents an InputAudioConfig.

## Implements

[protos.google.cloud.dialogflow.v2beta1.IInputAudioConfig](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iinputaudioconfig)

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dialogflow.v2beta1.IInputAudioConfig);

Constructs a new InputAudioConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInputAudioConfig](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iinputaudioconfig)`   
Properties to set  
  
## Properties 

### audioEncoding
    
    
    public audioEncoding: (google.cloud.dialogflow.v2beta1.AudioEncoding|keyof typeof google.cloud.dialogflow.v2beta1.AudioEncoding);

InputAudioConfig audioEncoding.

### bargeInConfig
    
    
    public bargeInConfig?: (google.cloud.dialogflow.v2beta1.IBargeInConfig|null);

InputAudioConfig bargeInConfig.

### defaultNoSpeechTimeout
    
    
    public defaultNoSpeechTimeout?: (google.protobuf.IDuration|null);

InputAudioConfig defaultNoSpeechTimeout.

### disableNoSpeechRecognizedEvent
    
    
    public disableNoSpeechRecognizedEvent: boolean;

InputAudioConfig disableNoSpeechRecognizedEvent.

### enableAutomaticPunctuation
    
    
    public enableAutomaticPunctuation: boolean;

InputAudioConfig enableAutomaticPunctuation.

### enableVoiceActivityEvents
    
    
    public enableVoiceActivityEvents: boolean;

InputAudioConfig enableVoiceActivityEvents.

### enableWordInfo
    
    
    public enableWordInfo: boolean;

InputAudioConfig enableWordInfo.

### languageCode
    
    
    public languageCode: string;

InputAudioConfig languageCode.

### model
    
    
    public model: string;

InputAudioConfig model.

### modelVariant
    
    
    public modelVariant: (google.cloud.dialogflow.v2beta1.SpeechModelVariant|keyof typeof google.cloud.dialogflow.v2beta1.SpeechModelVariant);

InputAudioConfig modelVariant.

### optOutConformerModelMigration
    
    
    public optOutConformerModelMigration: boolean;

InputAudioConfig optOutConformerModelMigration.

### phraseHints
    
    
    public phraseHints: string[];

InputAudioConfig phraseHints.

### phraseSets
    
    
    public phraseSets: string[];

InputAudioConfig phraseSets.

### sampleRateHertz
    
    
    public sampleRateHertz: number;

InputAudioConfig sampleRateHertz.

### singleUtterance
    
    
    public singleUtterance: boolean;

InputAudioConfig singleUtterance.

### speechContexts
    
    
    public speechContexts: google.cloud.dialogflow.v2beta1.ISpeechContext[];

InputAudioConfig speechContexts.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dialogflow.v2beta1.IInputAudioConfig): google.cloud.dialogflow.v2beta1.InputAudioConfig;

Creates a new InputAudioConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInputAudioConfig](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iinputaudioconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[InputAudioConfig](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.inputaudioconfig)` | InputAudioConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dialogflow.v2beta1.InputAudioConfig;

Decodes an InputAudioConfig message from the specified reader or buffer.

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
`[InputAudioConfig](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.inputaudioconfig)` | InputAudioConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dialogflow.v2beta1.InputAudioConfig;

Decodes an InputAudioConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[InputAudioConfig](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.inputaudioconfig)` | InputAudioConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dialogflow.v2beta1.IInputAudioConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InputAudioConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInputAudioConfig](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iinputaudioconfig)`   
InputAudioConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dialogflow.v2beta1.IInputAudioConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InputAudioConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInputAudioConfig](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.iinputaudioconfig)`   
InputAudioConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dialogflow.v2beta1.InputAudioConfig;

Creates an InputAudioConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[InputAudioConfig](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.inputaudioconfig)` | InputAudioConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for InputAudioConfig

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

Converts this InputAudioConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dialogflow.v2beta1.InputAudioConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an InputAudioConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[InputAudioConfig](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2beta1.inputaudioconfig)`   
InputAudioConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an InputAudioConfig message.

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
