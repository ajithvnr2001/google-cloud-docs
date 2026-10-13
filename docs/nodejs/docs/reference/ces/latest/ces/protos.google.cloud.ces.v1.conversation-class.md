---
url: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.conversation-class
title: Class protos.google.cloud.ces.v1.Conversation (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:05.029776+00:00
---

# Class protos.google.cloud.ces.v1.Conversation (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.conversation-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ces.v1.Conversation (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0 

Represents a Conversation.

## Implements

[protos.google.cloud.ces.v1.IConversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iconversation)

## Package

[@google-cloud/ces](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ces.v1.IConversation);

Constructs a new Conversation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iconversation)`   
Properties to set  
  
## Properties 

### appVersion
    
    
    public appVersion: string;

Conversation appVersion.

### channelType
    
    
    public channelType: (google.cloud.ces.v1.Conversation.ChannelType|keyof typeof google.cloud.ces.v1.Conversation.ChannelType);

Conversation channelType.

### deployment
    
    
    public deployment: string;

Conversation deployment.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

Conversation endTime.

### entryAgent
    
    
    public entryAgent: string;

Conversation entryAgent.

### inputTypes
    
    
    public inputTypes: google.cloud.ces.v1.Conversation.InputType[];

Conversation inputTypes.

### languageCode
    
    
    public languageCode: string;

Conversation languageCode.

### messages
    
    
    public messages: google.cloud.ces.v1.IMessage[];

Conversation messages.

### name
    
    
    public name: string;

Conversation name.

### source
    
    
    public source: (google.cloud.ces.v1.Conversation.Source|keyof typeof google.cloud.ces.v1.Conversation.Source);

Conversation source.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

Conversation startTime.

### turnCount
    
    
    public turnCount: number;

Conversation turnCount.

### turns
    
    
    public turns: google.cloud.ces.v1.Conversation.ITurn[];

Conversation turns.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ces.v1.IConversation): google.cloud.ces.v1.Conversation;

Creates a new Conversation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iconversation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.conversation-class)` | Conversation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ces.v1.Conversation;

Decodes a Conversation message from the specified reader or buffer.

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
`[Conversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.conversation-class)` | Conversation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ces.v1.Conversation;

Decodes a Conversation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.conversation-class)` | Conversation  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ces.v1.IConversation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Conversation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iconversation)`   
Conversation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ces.v1.IConversation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Conversation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.iconversation)`   
Conversation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ces.v1.Conversation;

Creates a Conversation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.conversation-class)` | Conversation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Conversation

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

Converts this Conversation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ces.v1.Conversation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Conversation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Conversation](https://docs.cloud.google.com/nodejs/docs/reference/ces/latest/ces/protos.google.cloud.ces.v1.conversation-class)`   
Conversation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Conversation message.

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
