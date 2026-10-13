---
url: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.imagefallbacklocation
title: Class protos.google.privacy.dlp.v2.ProcessingLocation.ImageFallbackLocation (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:14.592828+00:00
---

# Class protos.google.privacy.dlp.v2.ProcessingLocation.ImageFallbackLocation (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.imagefallbacklocation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.privacy.dlp.v2.ProcessingLocation.ImageFallbackLocation (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.6.0  6.2.0  6.1.0  5.13.0  5.11.0  5.10.0  5.7.0  5.5.0  5.3.0  5.0.0  4.4.2  4.2.0  4.1.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.8 

Represents an ImageFallbackLocation.

## Implements

[protos.google.privacy.dlp.v2.ProcessingLocation.IImageFallbackLocation](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.iimagefallbacklocation)

## Package

[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.privacy.dlp.v2.ProcessingLocation.IImageFallbackLocation);

Constructs a new ImageFallbackLocation.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImageFallbackLocation](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.iimagefallbacklocation)`   
Properties to set  
  
## Properties 

### globalProcessing
    
    
    public globalProcessing?: (google.privacy.dlp.v2.ProcessingLocation.IGlobalProcessing|null);

ImageFallbackLocation globalProcessing.

### multiRegionProcessing
    
    
    public multiRegionProcessing?: (google.privacy.dlp.v2.ProcessingLocation.IMultiRegionProcessing|null);

ImageFallbackLocation multiRegionProcessing.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.privacy.dlp.v2.ProcessingLocation.IImageFallbackLocation): google.privacy.dlp.v2.ProcessingLocation.ImageFallbackLocation;

Creates a new ImageFallbackLocation instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IImageFallbackLocation](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.iimagefallbacklocation)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ImageFallbackLocation](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.imagefallbacklocation)` | ImageFallbackLocation instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.privacy.dlp.v2.ProcessingLocation.ImageFallbackLocation;

Decodes an ImageFallbackLocation message from the specified reader or buffer.

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
`[ImageFallbackLocation](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.imagefallbacklocation)` | ImageFallbackLocation  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.privacy.dlp.v2.ProcessingLocation.ImageFallbackLocation;

Decodes an ImageFallbackLocation message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ImageFallbackLocation](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.imagefallbacklocation)` | ImageFallbackLocation  
  
### encode(message, writer)
    
    
    public static encode(message: google.privacy.dlp.v2.ProcessingLocation.IImageFallbackLocation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImageFallbackLocation message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImageFallbackLocation](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.iimagefallbacklocation)`   
ImageFallbackLocation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.privacy.dlp.v2.ProcessingLocation.IImageFallbackLocation, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ImageFallbackLocation message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IImageFallbackLocation](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.iimagefallbacklocation)`   
ImageFallbackLocation message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.privacy.dlp.v2.ProcessingLocation.ImageFallbackLocation;

Creates an ImageFallbackLocation message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ImageFallbackLocation](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.imagefallbacklocation)` | ImageFallbackLocation  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ImageFallbackLocation

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

Converts this ImageFallbackLocation to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.privacy.dlp.v2.ProcessingLocation.ImageFallbackLocation, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an ImageFallbackLocation message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ImageFallbackLocation](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.processinglocation.imagefallbacklocation)`   
ImageFallbackLocation  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an ImageFallbackLocation message.

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
