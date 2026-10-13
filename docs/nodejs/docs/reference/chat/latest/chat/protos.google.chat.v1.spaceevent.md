---
url: https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.spaceevent
title: Class protos.google.chat.v1.SpaceEvent (0.33.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:13.002244+00:00
---

# Class protos.google.chat.v1.SpaceEvent (0.33.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.spaceevent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.chat.v1.SpaceEvent (0.33.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.33.1 (latest)  0.33.0  0.32.0  0.26.0  0.25.0  0.24.0  0.22.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.6.0  0.4.0 

Represents a SpaceEvent.

## Implements

[protos.google.chat.v1.ISpaceEvent](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.ispaceevent)

## Package

[@google-apps/chat](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.chat.v1.ISpaceEvent);

Constructs a new SpaceEvent.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISpaceEvent](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.ispaceevent)`   
Properties to set  
  
## Properties 

### eventTime
    
    
    public eventTime?: (google.protobuf.ITimestamp|null);

SpaceEvent eventTime.

### eventType
    
    
    public eventType: string;

SpaceEvent eventType.

### membershipBatchCreatedEventData
    
    
    public membershipBatchCreatedEventData?: (google.chat.v1.IMembershipBatchCreatedEventData|null);

SpaceEvent membershipBatchCreatedEventData.

### membershipBatchDeletedEventData
    
    
    public membershipBatchDeletedEventData?: (google.chat.v1.IMembershipBatchDeletedEventData|null);

SpaceEvent membershipBatchDeletedEventData.

### membershipBatchUpdatedEventData
    
    
    public membershipBatchUpdatedEventData?: (google.chat.v1.IMembershipBatchUpdatedEventData|null);

SpaceEvent membershipBatchUpdatedEventData.

### membershipCreatedEventData
    
    
    public membershipCreatedEventData?: (google.chat.v1.IMembershipCreatedEventData|null);

SpaceEvent membershipCreatedEventData.

### membershipDeletedEventData
    
    
    public membershipDeletedEventData?: (google.chat.v1.IMembershipDeletedEventData|null);

SpaceEvent membershipDeletedEventData.

### membershipUpdatedEventData
    
    
    public membershipUpdatedEventData?: (google.chat.v1.IMembershipUpdatedEventData|null);

SpaceEvent membershipUpdatedEventData.

### messageBatchCreatedEventData
    
    
    public messageBatchCreatedEventData?: (google.chat.v1.IMessageBatchCreatedEventData|null);

SpaceEvent messageBatchCreatedEventData.

### messageBatchDeletedEventData
    
    
    public messageBatchDeletedEventData?: (google.chat.v1.IMessageBatchDeletedEventData|null);

SpaceEvent messageBatchDeletedEventData.

### messageBatchUpdatedEventData
    
    
    public messageBatchUpdatedEventData?: (google.chat.v1.IMessageBatchUpdatedEventData|null);

SpaceEvent messageBatchUpdatedEventData.

### messageCreatedEventData
    
    
    public messageCreatedEventData?: (google.chat.v1.IMessageCreatedEventData|null);

SpaceEvent messageCreatedEventData.

### messageDeletedEventData
    
    
    public messageDeletedEventData?: (google.chat.v1.IMessageDeletedEventData|null);

SpaceEvent messageDeletedEventData.

### messageUpdatedEventData
    
    
    public messageUpdatedEventData?: (google.chat.v1.IMessageUpdatedEventData|null);

SpaceEvent messageUpdatedEventData.

### name
    
    
    public name: string;

SpaceEvent name.

### payload
    
    
    public payload?: ("messageCreatedEventData"|"messageUpdatedEventData"|"messageDeletedEventData"|"messageBatchCreatedEventData"|"messageBatchUpdatedEventData"|"messageBatchDeletedEventData"|"spaceUpdatedEventData"|"spaceBatchUpdatedEventData"|"membershipCreatedEventData"|"membershipUpdatedEventData"|"membershipDeletedEventData"|"membershipBatchCreatedEventData"|"membershipBatchUpdatedEventData"|"membershipBatchDeletedEventData"|"reactionCreatedEventData"|"reactionDeletedEventData"|"reactionBatchCreatedEventData"|"reactionBatchDeletedEventData");

SpaceEvent payload.

### reactionBatchCreatedEventData
    
    
    public reactionBatchCreatedEventData?: (google.chat.v1.IReactionBatchCreatedEventData|null);

SpaceEvent reactionBatchCreatedEventData.

### reactionBatchDeletedEventData
    
    
    public reactionBatchDeletedEventData?: (google.chat.v1.IReactionBatchDeletedEventData|null);

SpaceEvent reactionBatchDeletedEventData.

### reactionCreatedEventData
    
    
    public reactionCreatedEventData?: (google.chat.v1.IReactionCreatedEventData|null);

SpaceEvent reactionCreatedEventData.

### reactionDeletedEventData
    
    
    public reactionDeletedEventData?: (google.chat.v1.IReactionDeletedEventData|null);

SpaceEvent reactionDeletedEventData.

### spaceBatchUpdatedEventData
    
    
    public spaceBatchUpdatedEventData?: (google.chat.v1.ISpaceBatchUpdatedEventData|null);

SpaceEvent spaceBatchUpdatedEventData.

### spaceUpdatedEventData
    
    
    public spaceUpdatedEventData?: (google.chat.v1.ISpaceUpdatedEventData|null);

SpaceEvent spaceUpdatedEventData.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.chat.v1.ISpaceEvent): google.chat.v1.SpaceEvent;

Creates a new SpaceEvent instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISpaceEvent](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.ispaceevent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SpaceEvent](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.spaceevent)` | SpaceEvent instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.chat.v1.SpaceEvent;

Decodes a SpaceEvent message from the specified reader or buffer.

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
`[SpaceEvent](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.spaceevent)` | SpaceEvent  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.chat.v1.SpaceEvent;

Decodes a SpaceEvent message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SpaceEvent](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.spaceevent)` | SpaceEvent  
  
### encode(message, writer)
    
    
    public static encode(message: google.chat.v1.ISpaceEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SpaceEvent message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISpaceEvent](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.ispaceevent)`   
SpaceEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.chat.v1.ISpaceEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SpaceEvent message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISpaceEvent](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.ispaceevent)`   
SpaceEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.chat.v1.SpaceEvent;

Creates a SpaceEvent message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SpaceEvent](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.spaceevent)` | SpaceEvent  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SpaceEvent

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

Converts this SpaceEvent to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.chat.v1.SpaceEvent, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SpaceEvent message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SpaceEvent](https://docs.cloud.google.com/nodejs/docs/reference/chat/latest/chat/protos.google.chat.v1.spaceevent)`   
SpaceEvent  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SpaceEvent message.

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
