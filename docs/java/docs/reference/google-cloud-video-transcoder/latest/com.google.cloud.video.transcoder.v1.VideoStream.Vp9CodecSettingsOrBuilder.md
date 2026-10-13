---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Vp9CodecSettingsOrBuilder
title: Interface VideoStream.Vp9CodecSettingsOrBuilder (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:07.791385+00:00
---

# Interface VideoStream.Vp9CodecSettingsOrBuilder (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Vp9CodecSettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface VideoStream.Vp9CodecSettingsOrBuilder (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.5  1.0.4  0.4.3 
    
    
    public static interface VideoStream.Vp9CodecSettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBitrateBps()
    
    
    public abstract int getBitrateBps()

Required. The video bitrate in bits per second. The minimum value is 1,000. The maximum value is 480,000,000.

`int32 bitrate_bps = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bitrateBps.  
  
### getColorFormatCase()
    
    
    public abstract VideoStream.Vp9CodecSettings.ColorFormatCase getColorFormatCase()

**Returns**  
---  
**Type** | **Description**  
`[VideoStream.Vp9CodecSettings.ColorFormatCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Vp9CodecSettings.ColorFormatCase)` |   
  
### getCrfLevel()
    
    
    public abstract int getCrfLevel()

Target CRF level. Must be between 10 and 36, where 10 is the highest quality and 36 is the most efficient compression. The default is 21.

**Note:** This field is not supported.

`int32 crf_level = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The crfLevel.  
  
### getFrameRate()
    
    
    public abstract double getFrameRate()

Required. The target video frame rate in frames per second (FPS). Must be less than or equal to 120.

`double frame_rate = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The frameRate.  
  
### getFrameRateConversionStrategy()
    
    
    public abstract VideoStream.FrameRateConversionStrategy getFrameRateConversionStrategy()

Optional. Frame rate conversion strategy for desired frame rate. The default is `DOWNSAMPLE`.

` .google.cloud.video.transcoder.v1.VideoStream.FrameRateConversionStrategy frame_rate_conversion_strategy = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VideoStream.FrameRateConversionStrategy](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.FrameRateConversionStrategy)` | The frameRateConversionStrategy.  
  
### getFrameRateConversionStrategyValue()
    
    
    public abstract int getFrameRateConversionStrategyValue()

Optional. Frame rate conversion strategy for desired frame rate. The default is `DOWNSAMPLE`.

` .google.cloud.video.transcoder.v1.VideoStream.FrameRateConversionStrategy frame_rate_conversion_strategy = 13 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for frameRateConversionStrategy.  
  
### getGopDuration()
    
    
    public abstract Duration getGopDuration()

Select the GOP size based on the specified duration. The default is `3s`. Note that `gopDuration` must be less than or equal to `segmentDuration`, and `segmentDuration` must be divisible by `gopDuration`.

`.google.protobuf.Duration gop_duration = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The gopDuration.  
  
### getGopDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getGopDurationOrBuilder()

Select the GOP size based on the specified duration. The default is `3s`. Note that `gopDuration` must be less than or equal to `segmentDuration`, and `segmentDuration` must be divisible by `gopDuration`.

`.google.protobuf.Duration gop_duration = 9;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getGopFrameCount()
    
    
    public abstract int getGopFrameCount()

Select the GOP size based on the specified frame count. Must be greater than zero.

`int32 gop_frame_count = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The gopFrameCount.  
  
### getGopModeCase()
    
    
    public abstract VideoStream.Vp9CodecSettings.GopModeCase getGopModeCase()

**Returns**  
---  
**Type** | **Description**  
`[VideoStream.Vp9CodecSettings.GopModeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Vp9CodecSettings.GopModeCase)` |   
  
### getHeightPixels()
    
    
    public abstract int getHeightPixels()

The height of the video in pixels. Must be an even integer. When not specified, the height is adjusted to match the specified width and input aspect ratio. If both are omitted, the input height is used.

For portrait videos that contain horizontal ASR and rotation metadata, provide the height, in pixels, per the horizontal ASR. The API calculates the width per the horizontal ASR. The API detects any rotation metadata and swaps the requested height and width for the output.

`int32 height_pixels = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The heightPixels.  
  
### getHlg()
    
    
    public abstract VideoStream.Vp9ColorFormatHLG getHlg()

Optional. HLG color format setting for VP9.

` .google.cloud.video.transcoder.v1.VideoStream.Vp9ColorFormatHLG hlg = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VideoStream.Vp9ColorFormatHLG](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Vp9ColorFormatHLG)` | The hlg.  
  
### getHlgOrBuilder()
    
    
    public abstract VideoStream.Vp9ColorFormatHLGOrBuilder getHlgOrBuilder()

Optional. HLG color format setting for VP9.

` .google.cloud.video.transcoder.v1.VideoStream.Vp9ColorFormatHLG hlg = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VideoStream.Vp9ColorFormatHLGOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Vp9ColorFormatHLGOrBuilder)` |   
  
### getPixelFormat()
    
    
    public abstract String getPixelFormat()

Pixel format to use. The default is `yuv420p`.

Supported pixel formats:

  * `yuv420p` pixel format
  * `yuv422p` pixel format
  * `yuv444p` pixel format
  * `yuv420p10` 10-bit HDR pixel format
  * `yuv422p10` 10-bit HDR pixel format
  * `yuv444p10` 10-bit HDR pixel format
  * `yuv420p12` 12-bit HDR pixel format
  * `yuv422p12` 12-bit HDR pixel format
  * `yuv444p12` 12-bit HDR pixel format



`string pixel_format = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pixelFormat.  
  
### getPixelFormatBytes()
    
    
    public abstract ByteString getPixelFormatBytes()

Pixel format to use. The default is `yuv420p`.

Supported pixel formats:

  * `yuv420p` pixel format
  * `yuv422p` pixel format
  * `yuv444p` pixel format
  * `yuv420p10` 10-bit HDR pixel format
  * `yuv422p10` 10-bit HDR pixel format
  * `yuv444p10` 10-bit HDR pixel format
  * `yuv420p12` 12-bit HDR pixel format
  * `yuv422p12` 12-bit HDR pixel format
  * `yuv444p12` 12-bit HDR pixel format



`string pixel_format = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pixelFormat.  
  
### getProfile()
    
    
    public abstract String getProfile()

Enforces the specified codec profile. The following profiles are supported:

  * `profile0` (default)
  * `profile1`
  * `profile2`
  * `profile3`

The available options are [WebM-compatible](https://www.webmproject.org/vp9/profiles/). Note that certain values for this field may cause the transcoder to override other fields you set in the `Vp9CodecSettings` message.




`string profile = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The profile.  
  
### getProfileBytes()
    
    
    public abstract ByteString getProfileBytes()

Enforces the specified codec profile. The following profiles are supported:

  * `profile0` (default)
  * `profile1`
  * `profile2`
  * `profile3`

The available options are [WebM-compatible](https://www.webmproject.org/vp9/profiles/). Note that certain values for this field may cause the transcoder to override other fields you set in the `Vp9CodecSettings` message.




`string profile = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for profile.  
  
### getRateControlMode()
    
    
    public abstract String getRateControlMode()

Specify the mode. The default is `vbr`.

Supported rate control modes:

  * `vbr` \- variable bitrate



`string rate_control_mode = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The rateControlMode.  
  
### getRateControlModeBytes()
    
    
    public abstract ByteString getRateControlModeBytes()

Specify the mode. The default is `vbr`.

Supported rate control modes:

  * `vbr` \- variable bitrate



`string rate_control_mode = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for rateControlMode.  
  
### getSdr()
    
    
    public abstract VideoStream.Vp9ColorFormatSDR getSdr()

Optional. SDR color format setting for VP9.

` .google.cloud.video.transcoder.v1.VideoStream.Vp9ColorFormatSDR sdr = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VideoStream.Vp9ColorFormatSDR](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Vp9ColorFormatSDR)` | The sdr.  
  
### getSdrOrBuilder()
    
    
    public abstract VideoStream.Vp9ColorFormatSDROrBuilder getSdrOrBuilder()

Optional. SDR color format setting for VP9.

` .google.cloud.video.transcoder.v1.VideoStream.Vp9ColorFormatSDR sdr = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VideoStream.Vp9ColorFormatSDROrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Vp9ColorFormatSDROrBuilder)` |   
  
### getWidthPixels()
    
    
    public abstract int getWidthPixels()

The width of the video in pixels. Must be an even integer. When not specified, the width is adjusted to match the specified height and input aspect ratio. If both are omitted, the input width is used.

For portrait videos that contain horizontal ASR and rotation metadata, provide the width, in pixels, per the horizontal ASR. The API calculates the height per the horizontal ASR. The API detects any rotation metadata and swaps the requested height and width for the output.

`int32 width_pixels = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The widthPixels.  
  
### hasGopDuration()
    
    
    public abstract boolean hasGopDuration()

Select the GOP size based on the specified duration. The default is `3s`. Note that `gopDuration` must be less than or equal to `segmentDuration`, and `segmentDuration` must be divisible by `gopDuration`.

`.google.protobuf.Duration gop_duration = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gopDuration field is set.  
  
### hasGopFrameCount()
    
    
    public abstract boolean hasGopFrameCount()

Select the GOP size based on the specified frame count. Must be greater than zero.

`int32 gop_frame_count = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gopFrameCount field is set.  
  
### hasHlg()
    
    
    public abstract boolean hasHlg()

Optional. HLG color format setting for VP9.

` .google.cloud.video.transcoder.v1.VideoStream.Vp9ColorFormatHLG hlg = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hlg field is set.  
  
### hasSdr()
    
    
    public abstract boolean hasSdr()

Optional. SDR color format setting for VP9.

` .google.cloud.video.transcoder.v1.VideoStream.Vp9ColorFormatSDR sdr = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sdr field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
