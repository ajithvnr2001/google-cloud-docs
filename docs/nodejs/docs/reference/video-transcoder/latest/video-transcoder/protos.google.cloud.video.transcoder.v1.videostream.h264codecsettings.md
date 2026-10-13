---
url: https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.h264codecsettings
title: Class protos.google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:21.041787+00:00
---

# Class protos.google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.h264codecsettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  3.0.3  2.6.0  2.5.0  2.4.1  2.2.3  1.10.0  1.9.0  1.8.1  1.7.2  1.6.1  1.5.0  1.4.4 

Represents a H264CodecSettings.

## Implements

[protos.google.cloud.video.transcoder.v1.VideoStream.IH264CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.ih264codecsettings)

## Package

[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.video.transcoder.v1.VideoStream.IH264CodecSettings);

Constructs a new H264CodecSettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IH264CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.ih264codecsettings)`   
Properties to set  
  
## Properties 

### allowOpenGop
    
    
    public allowOpenGop: boolean;

H264CodecSettings allowOpenGop.

### aqStrength
    
    
    public aqStrength: number;

H264CodecSettings aqStrength.

### bFrameCount
    
    
    public bFrameCount: number;

H264CodecSettings bFrameCount.

### bitrateBps
    
    
    public bitrateBps: number;

H264CodecSettings bitrateBps.

### bPyramid
    
    
    public bPyramid: boolean;

H264CodecSettings bPyramid.

### colorFormat
    
    
    public colorFormat?: ("sdr"|"hlg");

H264CodecSettings colorFormat.

### crfLevel
    
    
    public crfLevel: number;

H264CodecSettings crfLevel.

### enableTwoPass
    
    
    public enableTwoPass: boolean;

H264CodecSettings enableTwoPass.

### entropyCoder
    
    
    public entropyCoder: string;

H264CodecSettings entropyCoder.

### frameRate
    
    
    public frameRate: number;

H264CodecSettings frameRate.

### frameRateConversionStrategy
    
    
    public frameRateConversionStrategy: (google.cloud.video.transcoder.v1.VideoStream.FrameRateConversionStrategy|keyof typeof google.cloud.video.transcoder.v1.VideoStream.FrameRateConversionStrategy);

H264CodecSettings frameRateConversionStrategy.

### gopDuration
    
    
    public gopDuration?: (google.protobuf.IDuration|null);

H264CodecSettings gopDuration.

### gopFrameCount
    
    
    public gopFrameCount?: (number|null);

H264CodecSettings gopFrameCount.

### gopMode
    
    
    public gopMode?: ("gopFrameCount"|"gopDuration");

H264CodecSettings gopMode.

### heightPixels
    
    
    public heightPixels: number;

H264CodecSettings heightPixels.

### hlg
    
    
    public hlg?: (google.cloud.video.transcoder.v1.VideoStream.IH264ColorFormatHLG|null);

H264CodecSettings hlg.

### pixelFormat
    
    
    public pixelFormat: string;

H264CodecSettings pixelFormat.

### preset
    
    
    public preset: string;

H264CodecSettings preset.

### profile
    
    
    public profile: string;

H264CodecSettings profile.

### rateControlMode
    
    
    public rateControlMode: string;

H264CodecSettings rateControlMode.

### sdr
    
    
    public sdr?: (google.cloud.video.transcoder.v1.VideoStream.IH264ColorFormatSDR|null);

H264CodecSettings sdr.

### tune
    
    
    public tune: string;

H264CodecSettings tune.

### vbvFullnessBits
    
    
    public vbvFullnessBits: number;

H264CodecSettings vbvFullnessBits.

### vbvSizeBits
    
    
    public vbvSizeBits: number;

H264CodecSettings vbvSizeBits.

### widthPixels
    
    
    public widthPixels: number;

H264CodecSettings widthPixels.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.video.transcoder.v1.VideoStream.IH264CodecSettings): google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings;

Creates a new H264CodecSettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IH264CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.ih264codecsettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[H264CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.h264codecsettings)` | H264CodecSettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings;

Decodes a H264CodecSettings message from the specified reader or buffer.

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
`[H264CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.h264codecsettings)` | H264CodecSettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings;

Decodes a H264CodecSettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[H264CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.h264codecsettings)` | H264CodecSettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.video.transcoder.v1.VideoStream.IH264CodecSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified H264CodecSettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IH264CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.ih264codecsettings)`   
H264CodecSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.video.transcoder.v1.VideoStream.IH264CodecSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified H264CodecSettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IH264CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.ih264codecsettings)`   
H264CodecSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings;

Creates a H264CodecSettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[H264CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.h264codecsettings)` | H264CodecSettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for H264CodecSettings

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

Converts this H264CodecSettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a H264CodecSettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[H264CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.videostream.h264codecsettings)`   
H264CodecSettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a H264CodecSettings message.

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
