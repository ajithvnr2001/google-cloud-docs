---
url: https://docs.cloud.google.com/transcoder/docs/how-to/convert-to-hdr/
title: Convert an input video to HDR \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:38.517718+00:00
---

# Convert an input video to HDR  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/convert-to-hdr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Convert an input video to HDR Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to convert the input video in a transcoding job to a supported high dynamic range (HDR) or standard dynamic range (SDR) format. The Transcoder API uses high-efficiency video coding (HEVC) as the primary codec for the color conversion. Passthrough is enabled by default if you don't specify a color conversion format.

## Color conversion formats

HEVC is the primary codec used for the supported color conversion formats, which include the following:

  * Hybrid log-gamma (HLG)
  * SDR
  * HDR10



For [H.264](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#VideoStream.FIELDS.h264) and [VP9](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#VideoStream.FIELDS.vp9) streams, only HLG and SDR are supported. All conversions between the supported codec and the preceding color formats are supported.

## Passthrough

Passthrough is enabled by default if you don't specify a color conversion format.

For passthrough, the Transcoder API honors the input color primaries, transfer function, range, chroma location, and color space; no color conversion is done in the process. If the input is HDR10 (or HDR10+) and HEVC, the Transcoder API also passes the metadata through to the output video.

If you specify an output codec that does not support the input's color format, the passthrough is best effort. For example, an input HDR10 video has 10-bit options for [`profile`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H265CodecSettings.FIELDS.profile) and [`pixelFormat`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H265CodecSettings.FIELDS.pixel_format). If you specify the output as H.265 with an 8-bit option for [`profile`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H265CodecSettings.FIELDS.profile), the output is not a valid HDR10 video because HDR10 does not work with an 8-bit option for [`profile`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H265CodecSettings.FIELDS.profile).

## Example conversions

To specify the color conversion format, use an empty [`hlg`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H264CodecSettings.FIELDS.hlg), [`hdr10`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H265CodecSettings.FIELDS.hdr10), or [`sdr`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H264CodecSettings.FIELDS.sdr) object. The following sections show the JSON object to add to a [`VideoStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#VideoStream) to perform a given conversion.

### Convert to HLG format

Use the [`hlg`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H264CodecSettings.FIELDS.hlg) object to convert an input video to HLG format.
    
    
    "elementaryStreams": [
      {
        "key": "video_hlg",
        "videoStream": {
          "h264": {
            "heightPixels": 720,
            "widthPixels": 1280,
            "bitrateBps": 5000000,
            "frameRate": 25,
            "hlg":{}
        }
      }
    ]
    

### Convert to HDR10 format

Use the [`hdr10`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H265CodecSettings.FIELDS.hdr10) object to convert an input video to HDR10 format.
    
    
    "elementaryStreams": [
      {
        "key": "video_hdr10",
        "videoStream": {
          "h265": {
            "heightPixels": 720,
            "widthPixels": 1280,
            "bitrateBps": 5000000,
            "frameRate": 25,
            "pixelFormat":"yuv420p10",
            "profile":"main10",
            "hdr10":{}
        }
      }
    ]
    

### Down-convert to SDR format

Use the [`sdr`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H264CodecSettings.FIELDS.sdr) object to down-convert an input video to SDR format.
    
    
    "elementaryStreams": [
      {
        "key": "video_sdr",
        "videoStream": {
          "h264": {
            "heightPixels": 720,
            "widthPixels": 1280,
            "bitrateBps": 5000000,
            "frameRate": 25,
            "sdr":{}
        }
      }
    ]
    

## Possible errors

If the Transcoder API cannot perform the conversion, the transcoding job fails. Possible errors include the following:

  * Conversion to HDR10 format with 8-bit pixel formats or profiles
  * SDR inputs that don't conform to [BT.709](https://www.itu.int/rec/R-REC-BT.709)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
