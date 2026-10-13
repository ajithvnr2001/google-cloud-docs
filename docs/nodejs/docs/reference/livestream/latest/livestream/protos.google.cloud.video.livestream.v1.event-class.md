---
url: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.event-class
title: Class protos.google.cloud.video.livestream.v1.Event (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:16.917320+00:00
---

# Class protos.google.cloud.video.livestream.v1.Event (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.event-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.video.livestream.v1.Event (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.0.2  0.5.1  0.4.1  0.3.4  0.1.0 

Represents an Event.

## Implements

[protos.google.cloud.video.livestream.v1.IEvent](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ievent)

## Package

[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.video.livestream.v1.IEvent);

Constructs a new Event.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEvent](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ievent)`   
Properties to set  
  
## Properties 

### adBreak
    
    
    public adBreak?: (google.cloud.video.livestream.v1.Event.IAdBreakTask|null);

Event adBreak.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Event createTime.

### error
    
    
    public error?: (google.rpc.IStatus|null);

Event error.

### executeNow
    
    
    public executeNow: boolean;

Event executeNow.

### executionTime
    
    
    public executionTime?: (google.protobuf.ITimestamp|null);

Event executionTime.

### inputSwitch
    
    
    public inputSwitch?: (google.cloud.video.livestream.v1.Event.IInputSwitchTask|null);

Event inputSwitch.

### labels
    
    
    public labels: { [k: string]: string };

Event labels.

### mute
    
    
    public mute?: (google.cloud.video.livestream.v1.Event.IMuteTask|null);

Event mute.

### name
    
    
    public name: string;

Event name.

### returnToProgram
    
    
    public returnToProgram?: (google.cloud.video.livestream.v1.Event.IReturnToProgramTask|null);

Event returnToProgram.

### slate
    
    
    public slate?: (google.cloud.video.livestream.v1.Event.ISlateTask|null);

Event slate.

### state
    
    
    public state: (google.cloud.video.livestream.v1.Event.State|keyof typeof google.cloud.video.livestream.v1.Event.State);

Event state.

### task
    
    
    public task?: ("inputSwitch"|"adBreak"|"returnToProgram"|"slate"|"mute"|"unmute"|"updateEncryptions");

Event task.

### unmute
    
    
    public unmute?: (google.cloud.video.livestream.v1.Event.IUnmuteTask|null);

Event unmute.

### updateEncryptions
    
    
    public updateEncryptions?: (google.cloud.video.livestream.v1.Event.IUpdateEncryptionsTask|null);

Event updateEncryptions.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Event updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.video.livestream.v1.IEvent): google.cloud.video.livestream.v1.Event;

Creates a new Event instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEvent](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ievent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.event-class)` | Event instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.video.livestream.v1.Event;

Decodes an Event message from the specified reader or buffer.

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
`[Event](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.event-class)` | Event  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.video.livestream.v1.Event;

Decodes an Event message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.event-class)` | Event  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.video.livestream.v1.IEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Event message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEvent](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ievent)`   
Event message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.video.livestream.v1.IEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Event message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEvent](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ievent)`   
Event message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.video.livestream.v1.Event;

Creates an Event message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Event](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.event-class)` | Event  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Event

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

Converts this Event to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.video.livestream.v1.Event, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Event message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Event](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.event-class)`   
Event  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Event message.

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
