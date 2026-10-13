---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agent-class
title: Class protos.google.cloud.dialogflow.cx.v3.Agent (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:52:52.147634+00:00
---

# Class protos.google.cloud.dialogflow.cx.v3.Agent (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agent-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.cx.v3.Agent (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Represents an Agent.

## Implements

[protos.google.cloud.dialogflow.cx.v3.IAgent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iagent)

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dialogflow.cx.v3.IAgent);

Constructs a new Agent.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAgent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iagent)`   
Properties to set  
  
## Properties 

### advancedSettings
    
    
    public advancedSettings?: (google.cloud.dialogflow.cx.v3.IAdvancedSettings|null);

Agent advancedSettings.

### answerFeedbackSettings
    
    
    public answerFeedbackSettings?: (google.cloud.dialogflow.cx.v3.Agent.IAnswerFeedbackSettings|null);

Agent answerFeedbackSettings.

### avatarUri
    
    
    public avatarUri: string;

Agent avatarUri.

### clientCertificateSettings
    
    
    public clientCertificateSettings?: (google.cloud.dialogflow.cx.v3.Agent.IClientCertificateSettings|null);

Agent clientCertificateSettings.

### defaultLanguageCode
    
    
    public defaultLanguageCode: string;

Agent defaultLanguageCode.

### description
    
    
    public description: string;

Agent description.

### displayName
    
    
    public displayName: string;

Agent displayName.

### enableMultiLanguageTraining
    
    
    public enableMultiLanguageTraining: boolean;

Agent enableMultiLanguageTraining.

### enableSpellCorrection
    
    
    public enableSpellCorrection: boolean;

Agent enableSpellCorrection.

### enableStackdriverLogging
    
    
    public enableStackdriverLogging: boolean;

Agent enableStackdriverLogging.

### genAppBuilderSettings
    
    
    public genAppBuilderSettings?: (google.cloud.dialogflow.cx.v3.Agent.IGenAppBuilderSettings|null);

Agent genAppBuilderSettings.

### gitIntegrationSettings
    
    
    public gitIntegrationSettings?: (google.cloud.dialogflow.cx.v3.Agent.IGitIntegrationSettings|null);

Agent gitIntegrationSettings.

### locked
    
    
    public locked: boolean;

Agent locked.

### name
    
    
    public name: string;

Agent name.

### personalizationSettings
    
    
    public personalizationSettings?: (google.cloud.dialogflow.cx.v3.Agent.IPersonalizationSettings|null);

Agent personalizationSettings.

### satisfiesPzi
    
    
    public satisfiesPzi?: (boolean|null);

Agent satisfiesPzi.

### satisfiesPzs
    
    
    public satisfiesPzs?: (boolean|null);

Agent satisfiesPzs.

### securitySettings
    
    
    public securitySettings: string;

Agent securitySettings.

### sessionEntryResource
    
    
    public sessionEntryResource?: ("startFlow"|"startPlaybook");

Agent sessionEntryResource.

### speechToTextSettings
    
    
    public speechToTextSettings?: (google.cloud.dialogflow.cx.v3.ISpeechToTextSettings|null);

Agent speechToTextSettings.

### startFlow
    
    
    public startFlow?: (string|null);

Agent startFlow.

### startPlaybook
    
    
    public startPlaybook?: (string|null);

Agent startPlaybook.

### supportedLanguageCodes
    
    
    public supportedLanguageCodes: string[];

Agent supportedLanguageCodes.

### textToSpeechSettings
    
    
    public textToSpeechSettings?: (google.cloud.dialogflow.cx.v3.ITextToSpeechSettings|null);

Agent textToSpeechSettings.

### timeZone
    
    
    public timeZone: string;

Agent timeZone.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dialogflow.cx.v3.IAgent): google.cloud.dialogflow.cx.v3.Agent;

Creates a new Agent instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAgent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iagent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agent-class)` | Agent instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dialogflow.cx.v3.Agent;

Decodes an Agent message from the specified reader or buffer.

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
`[Agent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agent-class)` | Agent  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dialogflow.cx.v3.Agent;

Decodes an Agent message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agent-class)` | Agent  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dialogflow.cx.v3.IAgent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Agent message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAgent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iagent)`   
Agent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dialogflow.cx.v3.IAgent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Agent message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAgent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.iagent)`   
Agent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dialogflow.cx.v3.Agent;

Creates an Agent message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agent-class)` | Agent  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Agent

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

Converts this Agent to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dialogflow.cx.v3.Agent, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Agent message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Agent](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.agent-class)`   
Agent  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Agent message.

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
