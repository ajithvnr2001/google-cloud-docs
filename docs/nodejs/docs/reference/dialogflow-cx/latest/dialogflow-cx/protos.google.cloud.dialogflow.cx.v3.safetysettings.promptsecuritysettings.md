---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.promptsecuritysettings
title: Class protos.google.cloud.dialogflow.cx.v3.SafetySettings.PromptSecuritySettings (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:39.678930+00:00
---

# Class protos.google.cloud.dialogflow.cx.v3.SafetySettings.PromptSecuritySettings (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.promptsecuritysettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.cx.v3.SafetySettings.PromptSecuritySettings (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Represents a PromptSecuritySettings.

## Implements

[protos.google.cloud.dialogflow.cx.v3.SafetySettings.IPromptSecuritySettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.ipromptsecuritysettings)

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dialogflow.cx.v3.SafetySettings.IPromptSecuritySettings);

Constructs a new PromptSecuritySettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPromptSecuritySettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.ipromptsecuritysettings)`   
Properties to set  
  
## Properties 

### enablePromptSecurity
    
    
    public enablePromptSecurity: boolean;

PromptSecuritySettings enablePromptSecurity.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dialogflow.cx.v3.SafetySettings.IPromptSecuritySettings): google.cloud.dialogflow.cx.v3.SafetySettings.PromptSecuritySettings;

Creates a new PromptSecuritySettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPromptSecuritySettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.ipromptsecuritysettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PromptSecuritySettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.promptsecuritysettings)` | PromptSecuritySettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dialogflow.cx.v3.SafetySettings.PromptSecuritySettings;

Decodes a PromptSecuritySettings message from the specified reader or buffer.

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
`[PromptSecuritySettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.promptsecuritysettings)` | PromptSecuritySettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dialogflow.cx.v3.SafetySettings.PromptSecuritySettings;

Decodes a PromptSecuritySettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PromptSecuritySettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.promptsecuritysettings)` | PromptSecuritySettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dialogflow.cx.v3.SafetySettings.IPromptSecuritySettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PromptSecuritySettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPromptSecuritySettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.ipromptsecuritysettings)`   
PromptSecuritySettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dialogflow.cx.v3.SafetySettings.IPromptSecuritySettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PromptSecuritySettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPromptSecuritySettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.ipromptsecuritysettings)`   
PromptSecuritySettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dialogflow.cx.v3.SafetySettings.PromptSecuritySettings;

Creates a PromptSecuritySettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PromptSecuritySettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.promptsecuritysettings)` | PromptSecuritySettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PromptSecuritySettings

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

Converts this PromptSecuritySettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dialogflow.cx.v3.SafetySettings.PromptSecuritySettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PromptSecuritySettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PromptSecuritySettings](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.safetysettings.promptsecuritysettings)`   
PromptSecuritySettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PromptSecuritySettings message.

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
