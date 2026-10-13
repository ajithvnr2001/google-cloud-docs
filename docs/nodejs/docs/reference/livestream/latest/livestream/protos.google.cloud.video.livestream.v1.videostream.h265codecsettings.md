---
url: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.h265codecsettings
title: Class protos.google.cloud.video.livestream.v1.VideoStream.H265CodecSettings (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:18.932527+00:00
---

# Class protos.google.cloud.video.livestream.v1.VideoStream.H265CodecSettings (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.h265codecsettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.video.livestream.v1.VideoStream.H265CodecSettings (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.0.2  0.5.1  0.4.1  0.3.4  0.1.0 

Represents a H265CodecSettings.

## Implements

[protos.google.cloud.video.livestream.v1.VideoStream.IH265CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.ih265codecsettings)

## Package

[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.video.livestream.v1.VideoStream.IH265CodecSettings);

Constructs a new H265CodecSettings.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IH265CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.ih265codecsettings)`   
Properties to set  
  
## Properties 

### aqStrength
    
    
    public aqStrength: number;

H265CodecSettings aqStrength.

### bFrameCount
    
    
    public bFrameCount: number;

H265CodecSettings bFrameCount.

### bitrateBps
    
    
    public bitrateBps: number;

H265CodecSettings bitrateBps.

### bPyramid
    
    
    public bPyramid: boolean;

H265CodecSettings bPyramid.

### frameRate
    
    
    public frameRate: number;

H265CodecSettings frameRate.

### gopDuration
    
    
    public gopDuration?: (google.protobuf.IDuration|null);

H265CodecSettings gopDuration.

### gopFrameCount
    
    
    public gopFrameCount?: (number|null);

H265CodecSettings gopFrameCount.

### gopMode
    
    
    public gopMode?: ("gopFrameCount"|"gopDuration");

H265CodecSettings gopMode.

### heightPixels
    
    
    public heightPixels: number;

H265CodecSettings heightPixels.

### vbvFullnessBits
    
    
    public vbvFullnessBits: number;

H265CodecSettings vbvFullnessBits.

### vbvSizeBits
    
    
    public vbvSizeBits: number;

H265CodecSettings vbvSizeBits.

### widthPixels
    
    
    public widthPixels: number;

H265CodecSettings widthPixels.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.video.livestream.v1.VideoStream.IH265CodecSettings): google.cloud.video.livestream.v1.VideoStream.H265CodecSettings;

Creates a new H265CodecSettings instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IH265CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.ih265codecsettings)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[H265CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.h265codecsettings)` | H265CodecSettings instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.video.livestream.v1.VideoStream.H265CodecSettings;

Decodes a H265CodecSettings message from the specified reader or buffer.

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
`[H265CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.h265codecsettings)` | H265CodecSettings  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.video.livestream.v1.VideoStream.H265CodecSettings;

Decodes a H265CodecSettings message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[H265CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.h265codecsettings)` | H265CodecSettings  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.video.livestream.v1.VideoStream.IH265CodecSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified H265CodecSettings message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IH265CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.ih265codecsettings)`   
H265CodecSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.video.livestream.v1.VideoStream.IH265CodecSettings, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified H265CodecSettings message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IH265CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.ih265codecsettings)`   
H265CodecSettings message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.video.livestream.v1.VideoStream.H265CodecSettings;

Creates a H265CodecSettings message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[H265CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.h265codecsettings)` | H265CodecSettings  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for H265CodecSettings

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

Converts this H265CodecSettings to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.video.livestream.v1.VideoStream.H265CodecSettings, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a H265CodecSettings message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[H265CodecSettings](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.videostream.h265codecsettings)`   
H265CodecSettings  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a H265CodecSettings message.

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
