---
url: https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.videoannotationprogress
title: Class protos.google.cloud.videointelligence.v1p2beta1.VideoAnnotationProgress (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:05.086084+00:00
---

# Class protos.google.cloud.videointelligence.v1p2beta1.VideoAnnotationProgress (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.videoannotationprogress

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.videointelligence.v1p2beta1.VideoAnnotationProgress (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.1.0  5.0.2  4.2.2  4.1.1  3.4.1  3.3.6  3.1.0  3.0.0 

Represents a VideoAnnotationProgress.

## Implements

[protos.google.cloud.videointelligence.v1p2beta1.IVideoAnnotationProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.ivideoannotationprogress)

## Package

[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.videointelligence.v1p2beta1.IVideoAnnotationProgress);

Constructs a new VideoAnnotationProgress.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVideoAnnotationProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.ivideoannotationprogress)`   
Properties to set  
  
## Properties 

### inputUri
    
    
    public inputUri: string;

VideoAnnotationProgress inputUri.

### progressPercent
    
    
    public progressPercent: number;

VideoAnnotationProgress progressPercent.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

VideoAnnotationProgress startTime.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

VideoAnnotationProgress updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.videointelligence.v1p2beta1.IVideoAnnotationProgress): google.cloud.videointelligence.v1p2beta1.VideoAnnotationProgress;

Creates a new VideoAnnotationProgress instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IVideoAnnotationProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.ivideoannotationprogress)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[VideoAnnotationProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.videoannotationprogress)` | VideoAnnotationProgress instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.videointelligence.v1p2beta1.VideoAnnotationProgress;

Decodes a VideoAnnotationProgress message from the specified reader or buffer.

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
`[VideoAnnotationProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.videoannotationprogress)` | VideoAnnotationProgress  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.videointelligence.v1p2beta1.VideoAnnotationProgress;

Decodes a VideoAnnotationProgress message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[VideoAnnotationProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.videoannotationprogress)` | VideoAnnotationProgress  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.videointelligence.v1p2beta1.IVideoAnnotationProgress, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified VideoAnnotationProgress message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVideoAnnotationProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.ivideoannotationprogress)`   
VideoAnnotationProgress message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.videointelligence.v1p2beta1.IVideoAnnotationProgress, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified VideoAnnotationProgress message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IVideoAnnotationProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.ivideoannotationprogress)`   
VideoAnnotationProgress message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.videointelligence.v1p2beta1.VideoAnnotationProgress;

Creates a VideoAnnotationProgress message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[VideoAnnotationProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.videoannotationprogress)` | VideoAnnotationProgress  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for VideoAnnotationProgress

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

Converts this VideoAnnotationProgress to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.videointelligence.v1p2beta1.VideoAnnotationProgress, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a VideoAnnotationProgress message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[VideoAnnotationProgress](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p2beta1.videoannotationprogress)`   
VideoAnnotationProgress  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a VideoAnnotationProgress message.

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
