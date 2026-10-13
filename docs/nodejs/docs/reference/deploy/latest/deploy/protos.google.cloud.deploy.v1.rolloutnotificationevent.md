---
url: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rolloutnotificationevent
title: Class protos.google.cloud.deploy.v1.RolloutNotificationEvent (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:01:52.581767+00:00
---

# Class protos.google.cloud.deploy.v1.RolloutNotificationEvent (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rolloutnotificationevent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.deploy.v1.RolloutNotificationEvent (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.0.1  4.4.0  4.3.0  4.0.0  3.6.0  3.5.0  3.4.0  3.1.0  3.0.0  2.5.0  2.4.1  2.3.1  2.2.2  2.1.1  1.0.0  0.2.0 

Represents a RolloutNotificationEvent.

## Implements

[protos.google.cloud.deploy.v1.IRolloutNotificationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irolloutnotificationevent)

## Package

[@google-cloud/deploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.deploy.v1.IRolloutNotificationEvent);

Constructs a new RolloutNotificationEvent.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRolloutNotificationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irolloutnotificationevent)`   
Properties to set  
  
## Properties 

### message
    
    
    public message: string;

RolloutNotificationEvent message.

### pipelineUid
    
    
    public pipelineUid: string;

RolloutNotificationEvent pipelineUid.

### release
    
    
    public release: string;

RolloutNotificationEvent release.

### releaseUid
    
    
    public releaseUid: string;

RolloutNotificationEvent releaseUid.

### rollout
    
    
    public rollout: string;

RolloutNotificationEvent rollout.

### rolloutUid
    
    
    public rolloutUid: string;

RolloutNotificationEvent rolloutUid.

### targetId
    
    
    public targetId: string;

RolloutNotificationEvent targetId.

### type
    
    
    public type: (google.cloud.deploy.v1.Type|keyof typeof google.cloud.deploy.v1.Type);

RolloutNotificationEvent type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.deploy.v1.IRolloutNotificationEvent): google.cloud.deploy.v1.RolloutNotificationEvent;

Creates a new RolloutNotificationEvent instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRolloutNotificationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irolloutnotificationevent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RolloutNotificationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rolloutnotificationevent)` | RolloutNotificationEvent instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.deploy.v1.RolloutNotificationEvent;

Decodes a RolloutNotificationEvent message from the specified reader or buffer.

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
`[RolloutNotificationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rolloutnotificationevent)` | RolloutNotificationEvent  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.deploy.v1.RolloutNotificationEvent;

Decodes a RolloutNotificationEvent message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RolloutNotificationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rolloutnotificationevent)` | RolloutNotificationEvent  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.deploy.v1.IRolloutNotificationEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RolloutNotificationEvent message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRolloutNotificationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irolloutnotificationevent)`   
RolloutNotificationEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.deploy.v1.IRolloutNotificationEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RolloutNotificationEvent message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRolloutNotificationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.irolloutnotificationevent)`   
RolloutNotificationEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.deploy.v1.RolloutNotificationEvent;

Creates a RolloutNotificationEvent message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RolloutNotificationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rolloutnotificationevent)` | RolloutNotificationEvent  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RolloutNotificationEvent

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

Converts this RolloutNotificationEvent to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.deploy.v1.RolloutNotificationEvent, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RolloutNotificationEvent message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RolloutNotificationEvent](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.rolloutnotificationevent)`   
RolloutNotificationEvent  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RolloutNotificationEvent message.

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
