---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.cloudconversationdebugginginfo
title: Class protos.google.cloud.dialogflow.cx.v3.CloudConversationDebuggingInfo (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:53:03.842123+00:00
---

# Class protos.google.cloud.dialogflow.cx.v3.CloudConversationDebuggingInfo (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.cloudconversationdebugginginfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.cx.v3.CloudConversationDebuggingInfo (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Represents a CloudConversationDebuggingInfo.

## Implements

[protos.google.cloud.dialogflow.cx.v3.ICloudConversationDebuggingInfo](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.icloudconversationdebugginginfo)

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dialogflow.cx.v3.ICloudConversationDebuggingInfo);

Constructs a new CloudConversationDebuggingInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICloudConversationDebuggingInfo](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.icloudconversationdebugginginfo)`   
Properties to set  
  
## Properties 

### audioDataChunks
    
    
    public audioDataChunks: number;

CloudConversationDebuggingInfo audioDataChunks.

### bargeinEventTriggered
    
    
    public bargeinEventTriggered: boolean;

CloudConversationDebuggingInfo bargeinEventTriggered.

### clientHalfCloseStreamingTimeOffset
    
    
    public clientHalfCloseStreamingTimeOffset?: (google.protobuf.IDuration|null);

CloudConversationDebuggingInfo clientHalfCloseStreamingTimeOffset.

### clientHalfCloseTimeOffset
    
    
    public clientHalfCloseTimeOffset?: (google.protobuf.IDuration|null);

CloudConversationDebuggingInfo clientHalfCloseTimeOffset.

### dtmfFinalResultsTimes
    
    
    public dtmfFinalResultsTimes: google.protobuf.IDuration[];

CloudConversationDebuggingInfo dtmfFinalResultsTimes.

### dtmfPartialResultsTimes
    
    
    public dtmfPartialResultsTimes: google.protobuf.IDuration[];

CloudConversationDebuggingInfo dtmfPartialResultsTimes.

### endpointingTimeout
    
    
    public endpointingTimeout?: (google.protobuf.IDuration|null);

CloudConversationDebuggingInfo endpointingTimeout.

### firstAudioDuration
    
    
    public firstAudioDuration?: (google.protobuf.IDuration|null);

CloudConversationDebuggingInfo firstAudioDuration.

### isInputText
    
    
    public isInputText: boolean;

CloudConversationDebuggingInfo isInputText.

### noSpeechTimeout
    
    
    public noSpeechTimeout?: (google.protobuf.IDuration|null);

CloudConversationDebuggingInfo noSpeechTimeout.

### partialResponses
    
    
    public partialResponses: number;

CloudConversationDebuggingInfo partialResponses.

### resultEndTimeOffset
    
    
    public resultEndTimeOffset?: (google.protobuf.IDuration|null);

CloudConversationDebuggingInfo resultEndTimeOffset.

### singleUtterance
    
    
    public singleUtterance: boolean;

CloudConversationDebuggingInfo singleUtterance.

### singleUtteranceEndTimeOffset
    
    
    public singleUtteranceEndTimeOffset?: (google.protobuf.IDuration|null);

CloudConversationDebuggingInfo singleUtteranceEndTimeOffset.

### speakerIdPassiveLatencyMsOffset
    
    
    public speakerIdPassiveLatencyMsOffset: number;

CloudConversationDebuggingInfo speakerIdPassiveLatencyMsOffset.

### speechFinalResultsEndTimes
    
    
    public speechFinalResultsEndTimes: google.protobuf.IDuration[];

CloudConversationDebuggingInfo speechFinalResultsEndTimes.

### speechPartialResultsEndTimes
    
    
    public speechPartialResultsEndTimes: google.protobuf.IDuration[];

CloudConversationDebuggingInfo speechPartialResultsEndTimes.

### speechSingleUtterance
    
    
    public speechSingleUtterance: boolean;

CloudConversationDebuggingInfo speechSingleUtterance.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dialogflow.cx.v3.ICloudConversationDebuggingInfo): google.cloud.dialogflow.cx.v3.CloudConversationDebuggingInfo;

Creates a new CloudConversationDebuggingInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICloudConversationDebuggingInfo](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.icloudconversationdebugginginfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CloudConversationDebuggingInfo](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.cloudconversationdebugginginfo)` | CloudConversationDebuggingInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dialogflow.cx.v3.CloudConversationDebuggingInfo;

Decodes a CloudConversationDebuggingInfo message from the specified reader or buffer.

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
`[CloudConversationDebuggingInfo](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.cloudconversationdebugginginfo)` | CloudConversationDebuggingInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dialogflow.cx.v3.CloudConversationDebuggingInfo;

Decodes a CloudConversationDebuggingInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CloudConversationDebuggingInfo](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.cloudconversationdebugginginfo)` | CloudConversationDebuggingInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dialogflow.cx.v3.ICloudConversationDebuggingInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CloudConversationDebuggingInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICloudConversationDebuggingInfo](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.icloudconversationdebugginginfo)`   
CloudConversationDebuggingInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dialogflow.cx.v3.ICloudConversationDebuggingInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CloudConversationDebuggingInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICloudConversationDebuggingInfo](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.icloudconversationdebugginginfo)`   
CloudConversationDebuggingInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dialogflow.cx.v3.CloudConversationDebuggingInfo;

Creates a CloudConversationDebuggingInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CloudConversationDebuggingInfo](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.cloudconversationdebugginginfo)` | CloudConversationDebuggingInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CloudConversationDebuggingInfo

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

Converts this CloudConversationDebuggingInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dialogflow.cx.v3.CloudConversationDebuggingInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CloudConversationDebuggingInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CloudConversationDebuggingInfo](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.cloudconversationdebugginginfo)`   
CloudConversationDebuggingInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CloudConversationDebuggingInfo message.

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
