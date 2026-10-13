---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.loggingsettings
title: Class protos.google.cloud.ces.v1.LoggingSettings (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:34.599116+00:00
---

# Class protos.google.cloud.ces.v1.LoggingSettings (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.loggingsettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.LoggingSettings (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents a LoggingSettings.

## Implements

[protos.google.cloud.ces.v1.ILoggingSettings](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iloggingsettings)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.ILoggingSettings);

Constructs a new LoggingSettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILoggingSettings](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iloggingsettings)`   
Properties to set  
  
## Properties 

### audioRecordingConfig
    
    
    public audioRecordingConfig?: (google.cloud.ces.v1.IAudioRecordingConfig|null);

LoggingSettings audioRecordingConfig.

### bigqueryExportSettings
    
    
    public bigqueryExportSettings?: (google.cloud.ces.v1.IBigQueryExportSettings|null);

LoggingSettings bigqueryExportSettings.

### cloudLoggingSettings
    
    
    public cloudLoggingSettings?: (google.cloud.ces.v1.ICloudLoggingSettings|null);

LoggingSettings cloudLoggingSettings.

### conversationLoggingSettings
    
    
    public conversationLoggingSettings?: (google.cloud.ces.v1.IConversationLoggingSettings|null);

LoggingSettings conversationLoggingSettings.

### evaluationAudioRecordingConfig
    
    
    public evaluationAudioRecordingConfig?: (google.cloud.ces.v1.IAudioRecordingConfig|null);

LoggingSettings evaluationAudioRecordingConfig.

### metricAnalysisSettings
    
    
    public metricAnalysisSettings?: (google.cloud.ces.v1.IMetricAnalysisSettings|null);

LoggingSettings metricAnalysisSettings.

### redactionConfig
    
    
    public redactionConfig?: (google.cloud.ces.v1.IRedactionConfig|null);

LoggingSettings redactionConfig.

### unredactedAudioRecordingConfig
    
    
    public unredactedAudioRecordingConfig?: (google.cloud.ces.v1.IAudioRecordingConfig|null);

LoggingSettings unredactedAudioRecordingConfig.

### unredactedBigqueryExportSettings
    
    
    public unredactedBigqueryExportSettings?: (google.cloud.ces.v1.IBigQueryExportSettings|null);

LoggingSettings unredactedBigqueryExportSettings.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.ILoggingSettings): google.cloud.ces.v1.LoggingSettings;

Creates a new LoggingSettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILoggingSettings](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iloggingsettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LoggingSettings](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.loggingsettings)` | LoggingSettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.LoggingSettings;

Decodes a LoggingSettings message from the specified reader or buffer.

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
`[LoggingSettings](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.loggingsettings)` | LoggingSettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.LoggingSettings;

Decodes a LoggingSettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LoggingSettings](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.loggingsettings)` | LoggingSettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.ILoggingSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LoggingSettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILoggingSettings](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iloggingsettings)`   
LoggingSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.ILoggingSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LoggingSettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILoggingSettings](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iloggingsettings)`   
LoggingSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.LoggingSettings;

Creates a LoggingSettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LoggingSettings](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.loggingsettings)` | LoggingSettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LoggingSettings

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

Converts this LoggingSettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.LoggingSettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LoggingSettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LoggingSettings](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.loggingsettings)`   
LoggingSettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LoggingSettings message.

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

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
