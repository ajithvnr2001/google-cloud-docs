---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.safetysignals-class
title: Class protos.google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:20.100779+00:00
---

# Class protos.google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.safetysignals-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.6.0  5.5.0  5.1.0  5.0.1  4.10.0  4.9.0  4.8.0  4.6.0  4.3.1  4.2.0  4.0.0  3.4.2  3.2.1  3.1.2  2.15.0  2.14.0  2.13.0  2.12.1 

Represents a SafetySignals.

## Implements

[protos.google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.ISafetySignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.isafetysignals)

## Package

[@google-cloud/dialogflow-cx](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.ISafetySignals);

Constructs a new SafetySignals.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISafetySignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.isafetysignals)`   
Properties to set  
  
## Properties 

### bannedPhraseMatch
    
    
    public bannedPhraseMatch: (google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch|keyof typeof google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals.BannedPhraseMatch);

SafetySignals bannedPhraseMatch.

### decision
    
    
    public decision: (google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals.SafetyDecision|keyof typeof google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals.SafetyDecision);

SafetySignals decision.

### matchedBannedPhrase
    
    
    public matchedBannedPhrase: string;

SafetySignals matchedBannedPhrase.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.ISafetySignals): google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals;

Creates a new SafetySignals instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISafetySignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.isafetysignals)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SafetySignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.safetysignals-class)` | SafetySignals instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals;

Decodes a SafetySignals message from the specified reader or buffer.

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
`[SafetySignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.safetysignals-class)` | SafetySignals  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals;

Decodes a SafetySignals message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SafetySignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.safetysignals-class)` | SafetySignals  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.ISafetySignals, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SafetySignals message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISafetySignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.isafetysignals)`   
SafetySignals message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.ISafetySignals, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SafetySignals message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISafetySignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.isafetysignals)`   
SafetySignals message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals;

Creates a SafetySignals message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SafetySignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.safetysignals-class)` | SafetySignals  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SafetySignals

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

Converts this SafetySignals to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dialogflow.cx.v3.DataStoreConnectionSignals.SafetySignals, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SafetySignals message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SafetySignals](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow-cx/latest/dialogflow-cx/protos.google.cloud.dialogflow.cx.v3.datastoreconnectionsignals.safetysignals-class)`   
SafetySignals  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SafetySignals message.

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
