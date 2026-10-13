---
url: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.audiomapping
title: Class protos.google.cloud.video.livestream.v1.AudioStream.AudioMapping (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:09.156489+00:00
---

# Class protos.google.cloud.video.livestream.v1.AudioStream.AudioMapping (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.audiomapping

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.video.livestream.v1.AudioStream.AudioMapping (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.0.2  0.5.1  0.4.1  0.3.4  0.1.0 

Represents an AudioMapping.

## Implements

[protos.google.cloud.video.livestream.v1.AudioStream.IAudioMapping](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.iaudiomapping)

## Package

[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.video.livestream.v1.AudioStream.IAudioMapping);

Constructs a new AudioMapping.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAudioMapping](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.iaudiomapping)`   
Properties to set  
  
## Properties 

### gainDb
    
    
    public gainDb: number;

AudioMapping gainDb.

### inputChannel
    
    
    public inputChannel: number;

AudioMapping inputChannel.

### inputKey
    
    
    public inputKey: string;

AudioMapping inputKey.

### inputTrack
    
    
    public inputTrack: number;

AudioMapping inputTrack.

### outputChannel
    
    
    public outputChannel: number;

AudioMapping outputChannel.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.video.livestream.v1.AudioStream.IAudioMapping): google.cloud.video.livestream.v1.AudioStream.AudioMapping;

Creates a new AudioMapping instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAudioMapping](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.iaudiomapping)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AudioMapping](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.audiomapping)` | AudioMapping instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.video.livestream.v1.AudioStream.AudioMapping;

Decodes an AudioMapping message from the specified reader or buffer.

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
`[AudioMapping](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.audiomapping)` | AudioMapping  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.video.livestream.v1.AudioStream.AudioMapping;

Decodes an AudioMapping message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AudioMapping](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.audiomapping)` | AudioMapping  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.video.livestream.v1.AudioStream.IAudioMapping, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AudioMapping message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAudioMapping](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.iaudiomapping)`   
AudioMapping message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.video.livestream.v1.AudioStream.IAudioMapping, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AudioMapping message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAudioMapping](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.iaudiomapping)`   
AudioMapping message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.video.livestream.v1.AudioStream.AudioMapping;

Creates an AudioMapping message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AudioMapping](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.audiomapping)` | AudioMapping  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AudioMapping

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

Converts this AudioMapping to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.video.livestream.v1.AudioStream.AudioMapping, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AudioMapping message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AudioMapping](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.audiostream.audiomapping)`   
AudioMapping  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AudioMapping message.

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
