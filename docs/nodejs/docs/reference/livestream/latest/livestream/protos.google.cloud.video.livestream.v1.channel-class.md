---
url: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.channel-class
title: Class protos.google.cloud.video.livestream.v1.Channel (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:10.228690+00:00
---

# Class protos.google.cloud.video.livestream.v1.Channel (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.channel-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.video.livestream.v1.Channel (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.0.2  0.5.1  0.4.1  0.3.4  0.1.0 

Represents a Channel.

## Implements

[protos.google.cloud.video.livestream.v1.IChannel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ichannel)

## Package

[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.video.livestream.v1.IChannel);

Constructs a new Channel.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IChannel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ichannel)`   
Properties to set  
  
## Properties 

### activeInput
    
    
    public activeInput: string;

Channel activeInput.

### autoTranscriptionConfig
    
    
    public autoTranscriptionConfig?: (google.cloud.video.livestream.v1.IAutoTranscriptionConfig|null);

Channel autoTranscriptionConfig.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Channel createTime.

### distributions
    
    
    public distributions: google.cloud.video.livestream.v1.IDistribution[];

Channel distributions.

### distributionStreams
    
    
    public distributionStreams: google.cloud.video.livestream.v1.IDistributionStream[];

Channel distributionStreams.

### elementaryStreams
    
    
    public elementaryStreams: google.cloud.video.livestream.v1.IElementaryStream[];

Channel elementaryStreams.

### encryptions
    
    
    public encryptions: google.cloud.video.livestream.v1.IEncryption[];

Channel encryptions.

### inputAttachments
    
    
    public inputAttachments: google.cloud.video.livestream.v1.IInputAttachment[];

Channel inputAttachments.

### inputConfig
    
    
    public inputConfig?: (google.cloud.video.livestream.v1.IInputConfig|null);

Channel inputConfig.

### labels
    
    
    public labels: { [k: string]: string };

Channel labels.

### logConfig
    
    
    public logConfig?: (google.cloud.video.livestream.v1.ILogConfig|null);

Channel logConfig.

### manifests
    
    
    public manifests: google.cloud.video.livestream.v1.IManifest[];

Channel manifests.

### muxStreams
    
    
    public muxStreams: google.cloud.video.livestream.v1.IMuxStream[];

Channel muxStreams.

### name
    
    
    public name: string;

Channel name.

### output
    
    
    public output?: (google.cloud.video.livestream.v1.Channel.IOutput|null);

Channel output.

### retentionConfig
    
    
    public retentionConfig?: (google.cloud.video.livestream.v1.IRetentionConfig|null);

Channel retentionConfig.

### spriteSheets
    
    
    public spriteSheets: google.cloud.video.livestream.v1.ISpriteSheet[];

Channel spriteSheets.

### staticOverlays
    
    
    public staticOverlays: google.cloud.video.livestream.v1.IStaticOverlay[];

Channel staticOverlays.

### streamingError
    
    
    public streamingError?: (google.rpc.IStatus|null);

Channel streamingError.

### streamingState
    
    
    public streamingState: (google.cloud.video.livestream.v1.Channel.StreamingState|keyof typeof google.cloud.video.livestream.v1.Channel.StreamingState);

Channel streamingState.

### timecodeConfig
    
    
    public timecodeConfig?: (google.cloud.video.livestream.v1.ITimecodeConfig|null);

Channel timecodeConfig.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Channel updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.video.livestream.v1.IChannel): google.cloud.video.livestream.v1.Channel;

Creates a new Channel instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IChannel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ichannel)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Channel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.channel-class)` | Channel instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.video.livestream.v1.Channel;

Decodes a Channel message from the specified reader or buffer.

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
`[Channel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.channel-class)` | Channel  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.video.livestream.v1.Channel;

Decodes a Channel message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Channel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.channel-class)` | Channel  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.video.livestream.v1.IChannel, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Channel message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IChannel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ichannel)`   
Channel message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.video.livestream.v1.IChannel, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Channel message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IChannel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.ichannel)`   
Channel message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.video.livestream.v1.Channel;

Creates a Channel message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Channel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.channel-class)` | Channel  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Channel

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

Converts this Channel to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.video.livestream.v1.Channel, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Channel message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Channel](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.channel-class)`   
Channel  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Channel message.

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
