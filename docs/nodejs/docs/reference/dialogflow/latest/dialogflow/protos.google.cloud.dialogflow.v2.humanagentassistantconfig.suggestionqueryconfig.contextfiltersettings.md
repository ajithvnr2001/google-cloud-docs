---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.contextfiltersettings
title: Class protos.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:59:32.914952+00:00
---

# Class protos.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.contextfiltersettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a ContextFilterSettings.

## Implements

[protos.google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.IContextFilterSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.icontextfiltersettings)

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.IContextFilterSettings);

Constructs a new ContextFilterSettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IContextFilterSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.icontextfiltersettings)`   
Properties to set  
  
## Properties 

### dropHandoffMessages
    
    
    public dropHandoffMessages: boolean;

ContextFilterSettings dropHandoffMessages.

### dropIvrMessages
    
    
    public dropIvrMessages: boolean;

ContextFilterSettings dropIvrMessages.

### dropVirtualAgentMessages
    
    
    public dropVirtualAgentMessages: boolean;

ContextFilterSettings dropVirtualAgentMessages.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.IContextFilterSettings): google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings;

Creates a new ContextFilterSettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IContextFilterSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.icontextfiltersettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ContextFilterSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.contextfiltersettings)` | ContextFilterSettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings;

Decodes a ContextFilterSettings message from the specified reader or buffer.

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
`[ContextFilterSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.contextfiltersettings)` | ContextFilterSettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings;

Decodes a ContextFilterSettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ContextFilterSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.contextfiltersettings)` | ContextFilterSettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.IContextFilterSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ContextFilterSettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IContextFilterSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.icontextfiltersettings)`   
ContextFilterSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.IContextFilterSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ContextFilterSettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IContextFilterSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.icontextfiltersettings)`   
ContextFilterSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings;

Creates a ContextFilterSettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ContextFilterSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.contextfiltersettings)` | ContextFilterSettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ContextFilterSettings

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

Converts this ContextFilterSettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ContextFilterSettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ContextFilterSettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.humanagentassistantconfig.suggestionqueryconfig.contextfiltersettings)`   
ContextFilterSettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ContextFilterSettings message.

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
