---
url: https://docs.cloud.google.com/video-stitcher/docs/concepts/manifest-options/
title: Manifest options \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:38.951677+00:00
---

# Manifest options  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/concepts/manifest-options/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Manifest options Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes the supported manifest options feature of the Video Stitcher API. This lets you customize the stitched video manifest. The manifest options are configured in the session creation request. For more information, see the following:

  * [Manage a live session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions)
  * [Manage a live session enabled by Google Ad Manager](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions-gam)
  * [Manage a VOD session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions)
  * [Manage a VOD session enabled by Google Ad Manager](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions-gam)



## Before you begin

Make sure you are familiar with the introductory concepts and terminology in the Video Stitcher API. For more information, see the technical [overview](https://docs.cloud.google.com/video-stitcher/docs/concepts/overview).

## Introduction

By default, the stitched video manifest will contain the same media renditions as the source video manifest. The source manifest may contain several media renditions that not all players can play. For example, an encoded video may contain both H.264 and H.265 video codecs, but a player on one device may only be able to play H.264.

By specifying which codecs or bitrates to include in the video manifest, you can specify which video renditions to output in the stitched video manifest.

## Manifest options

The [`ManifestOptions`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/ManifestOptions) object provides you with some options to customize the stitched video manifest.

### HLS

You can customize the following for stitched HLS video manifests:

  * Filter by codecs
  * Include only certain video resolutions
  * Include only certain frame rates
  * Include only certain bitrates
  * Order the video renditions



For the next sections, assume the following source video manifest:
    
    
    #EXTM3U
    #EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=1920x1080,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/fhd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/sd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=240000,RESOLUTION=1280x720,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/hd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=400000,RESOLUTION=1920x1080,CODECS="hvc1.1.4.L126.B0,mp4a.40.2,FRAME-RATE=50.000"
    h265/fhd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=100000,RESOLUTION=640x360,CODECS="hvc1.1.4.L126.B0,mp4a.40.2,FRAME-RATE=50.000"
    h265/sd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=200000,RESOLUTION=1280x720,CODECS="hvc1.1.4.L126.B0,mp4a.40.2,FRAME-RATE=50.000"
    h265/hd/index.m3u8
    

#### Filter by codecs

To filter video rendition by codecs, set the codecs in the optional `manifestOptions` field when creating a session. For example, to only display H.264 in the stitched manifest, set the codec in the `includeRenditions` array:
    
    
    {
      "manifestOptions": {
        "includeRenditions": [
          {
            "codecs": "avc1.42e00a,mp4a.40.2",
          },
        ],
      },
    }

The following will be displayed in the stitched manifest:
    
    
    #EXTM3U
    #EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=1920x1080,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=240000,RESOLUTION=1280x720,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/index.m3u8
    

#### Include only certain video resolutions

To filter video rendition by video resolution, set the video resolution in the optional `manifestOptions` field when creating a session. For example, to only display `1920x1080` and `640x360` video resolutions in the stitched manifest, set the video resolutions in the `includeRenditions` array:
    
    
    {
      "manifestOptions": {
        "includeRenditions": [
          {
            "videoResolution": {
              "widthPixels": 1920,
              "heightPixels": 1080,
            },
          },
          {
            "videoResolution": {
              "widthPixels": 640,
              "heightPixels": 360,
            },
          },
        ],
      },
    }

The following will be displayed in the stitched manifest:
    
    
    #EXTM3U
    #EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=1920x1080,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=400000,RESOLUTION=1920x1080,CODECS="hvc1.1.4.L126.B0,mp4a.40.2,FRAME-RATE=50.000"
    h265/fhd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=100000,RESOLUTION=640x360,CODECS="hvc1.1.4.L126.B0,mp4a.40.2,FRAME-RATE=50.000"
    h265/sd/index.m3u8
    

#### Include only certain frame rates

To filter video rendition by frame rates, set the frame rate in the optional `manifestOptions` field when creating a session. For example, to only display `25.0` frame rates in the stitched manifest, set the frame rate in the `includeRenditions` array:
    
    
    {
      "manifestOptions": {
        "includeRenditions": [
          {
            "frameRate": 25.0
          },
        ],
      },
    }

The following will be displayed in the stitched manifest:
    
    
    #EXTM3U
    #EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=1920x1080,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/fhd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/sd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=240000,RESOLUTION=1280x720,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/hd/index.m3u8
    

#### Include only certain bitrates

To filter video rendition by bitrates, set the bitrates in the optional `manifestOptions` field when creating a session. For example, to only display two bitrates in the stitched manifest, set the bitrates in the `includeRenditions` array:
    
    
    {
      "manifestOptions": {
        "includeRenditions": [
          {
            "bitrateBps": 150000,
          },
          {
            "bitrateBps": 440000,
          },
        ],
      },
    }

The following will be displayed in the stitched manifest:
    
    
    #EXTM3U
    #EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=1920x1080,CODECS="avc1.42e00a,mp4a.40.2"
    h264/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2"
    h264/index.m3u8
    

#### Order by bitrate

Some players may be sensitive to the ordering of the video renditions. You can set the order of the video renditions to `ascending` or `descending`, as in the following:
    
    
    {
      "manifestOptions": {
        "bitrateOrder": "ascending",
      },
    }

The following will be displayed in the stitched manifest:
    
    
    #EXTM3U
    #EXT-X-STREAM-INF:BANDWIDTH=100000,RESOLUTION=640x360,CODECS="hvc1.1.4.L126.B0,mp4a.40.2,FRAME-RATE=50.000"
    h265/sd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=150000,RESOLUTION=640x360,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/sd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=200000,RESOLUTION=1280x720,CODECS="hvc1.1.4.L126.B0,mp4a.40.2,FRAME-RATE=50.000"
    h265/hd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=240000,RESOLUTION=1280x720,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/hd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=400000,RESOLUTION=1920x1080,CODECS="hvc1.1.4.L126.B0,mp4a.40.2,FRAME-RATE=50.000"
    h265/fhd/index.m3u8
    #EXT-X-STREAM-INF:BANDWIDTH=440000,RESOLUTION=1920x1080,CODECS="avc1.42e00a,mp4a.40.2,FRAME-RATE=25.000"
    h264/fhd/index.m3u8
    

### DASH

You can customize the following for stitched DASH video manifests:

  * Filter by codecs
  * Include only certain video resolutions
  * Include only certain frame rates
  * Include only certain bitrates
  * Order the video renditions



For the next sections, assume the following source video manifest:
    
    
    <Period id="0" start="PT33160.000S">
      <AdaptationSet segmentAlignment="true" maxWidth="1280" maxHeight="720">
        <Representation mimeType="video/mp4" id="640x360-h264" codecs="avc1.64001E" width="640" height="360" startWithSAP="1" bandwidth="150000" frameRate="25/1">
          ...
        </Representation>
        <Representation mimeType="video/mp4" id="1280x720-h264" codecs="avc1.64001E" width="1280" height="720" startWithSAP="1" bandwidth="240000" frameRate="25/1">
          ...
        </Representation>
        <Representation mimeType="video/mp4" id="640x360-h265" codecs="hvc1.1.4.L126.B0" width="640" height="360" startWithSAP="1" bandwidth="100000" frameRate="50/1">
          ...
        </Representation>
        <Representation mimeType="video/mp4" id="1280x720-h265" codecs="hvc1.1.4.L126.B0" width="1280" height="720" startWithSAP="1" bandwidth="200000" frameRate="50/1">
          ...
        </Representation>
      </AdaptationSet>
      <AdaptationSet segmentAlignment="true">
        <Representation mimeType="audio/mp4" id="640x360-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
        <Representation mimeType="audio/mp4" id="1280x720-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
      </AdaptationSet>
    </Period>
    

#### Filter by codecs

To filter video rendition by codecs, set the codecs in the optional `manifestOptions` field when creating a session. For example, to only display H.264 in the stitched manifest, set the codec in the `includeRenditions` array:
    
    
    {
      "manifestOptions": {
        "includeRenditions": [
          {
            "codecs": "hvc1.1.4.L126.B0",
          },
        ],
      },
    }

The following will be displayed in the stitched manifest:
    
    
    <Period id="0" start="PT33160.000S">
      <AdaptationSet segmentAlignment="true" maxWidth="1280" maxHeight="720">
        <Representation mimeType="video/mp4" id="640x360-h265" codecs="hvc1.1.4.L126.B0" width="640" height="360" startWithSAP="1" bandwidth="100000" frameRate="50/1">
          ...
        </Representation>
        <Representation mimeType="video/mp4" id="1280x720-h265" codecs="hvc1.1.4.L126.B0" width="1280" height="720" startWithSAP="1" bandwidth="200000" frameRate="50/1">
          ...
        </Representation>
      </AdaptationSet>
      <AdaptationSet segmentAlignment="true">
        <Representation mimeType="audio/mp4" id="640x360-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
        <Representation mimeType="audio/mp4" id="1280x720-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
      </AdaptationSet>
    </Period>
    

#### Include only certain video resolutions

To filter video rendition by video resolution, set the video resolution in the optional `manifestOptions` field when creating a session. For example, to only display `640x360` video resolutions in the stitched manifest, set the video resolution in the `includeRenditions` array:
    
    
    {
      "manifestOptions": {
        "includeRenditions": [
          {
            "videoResolution": {
              "widthPixels": 640,
              "heightPixels": 360,
            },
          },
        ],
      },
    }

The following will be displayed in the stitched manifest:
    
    
    <Period id="0" start="PT33160.000S">
      <AdaptationSet segmentAlignment="true" maxWidth="1280" maxHeight="720">
        <Representation mimeType="video/mp4" id="640x360-h264" codecs="avc1.64001E" width="640" height="360" startWithSAP="1" bandwidth="150000" frameRate="25/1">
          ...
        </Representation>
        <Representation mimeType="video/mp4" id="640x360-h265" codecs="hvc1.1.4.L126.B0" width="640" height="360" startWithSAP="1" bandwidth="100000" frameRate="50/1">
          ...
        </Representation>
      </AdaptationSet>
      <AdaptationSet segmentAlignment="true">
        <Representation mimeType="audio/mp4" id="640x360-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
        <Representation mimeType="audio/mp4" id="1280x720-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
      </AdaptationSet>
    </Period>
    

#### Include only certain frame rates

To filter video rendition by frame rates, set the frame rate in the optional `manifestOptions` field when creating a session. For example, to only display `25.0` frame rate in the stitched manifest, set the frame rate in the `includeRenditions` array:
    
    
    {
      "manifestOptions": {
        "includeRenditions": [
          {
            "frameRate": 25.0
          },
        ],
      },
    }

The following will be displayed in the stitched manifest:
    
    
    <Period id="0" start="PT33160.000S">
      <AdaptationSet segmentAlignment="true" maxWidth="1280" maxHeight="720">
        <Representation mimeType="video/mp4" id="640x360-h264" codecs="avc1.64001E" width="640" height="360" startWithSAP="1" bandwidth="150000" frameRate="25/1">
          ...
        </Representation>
        <Representation mimeType="video/mp4" id="1280x720-h264" codecs="avc1.64001E" width="1280" height="720" startWithSAP="1" bandwidth="240000" frameRate="25/1">
          ...
        </Representation>
      </AdaptationSet>
      <AdaptationSet segmentAlignment="true">
        <Representation mimeType="audio/mp4" id="640x360-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
        <Representation mimeType="audio/mp4" id="1280x720-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
      </AdaptationSet>
    </Period>
    

#### Include certain bitrates

To filter video rendition by bitrates, set the bitrates in the optional `manifestOptions` field when creating a session. For example, to only display two bitrates in the stitched manifest, set the bitrates in the `includeRenditions` array:
    
    
    {
      "manifestOptions": {
        "includeRenditions": [
          {
            "bitrateBps": 150000,
          },
          {
            "bitrateBps": 240000,
          },
        ],
      },
    }

The following will be displayed in the stitched manifest:
    
    
    <Period id="0" start="PT33160.000S">
      <AdaptationSet segmentAlignment="true" maxWidth="1280" maxHeight="720">
        <Representation mimeType="video/mp4" id="640x360-h264" codecs="avc1.64001E" width="640" height="360" startWithSAP="1" bandwidth="150000" frameRate="25/1">
          ...
        </Representation>
        <Representation mimeType="video/mp4" id="1280x720-h264" codecs="avc1.64001E" width="1280" height="720" startWithSAP="1" bandwidth="240000" frameRate="25/1">
          ...
        </Representation>
      </AdaptationSet>
      <AdaptationSet segmentAlignment="true">
        <Representation mimeType="audio/mp4" id="640x360-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
        <Representation mimeType="audio/mp4" id="1280x720-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
      </AdaptationSet>
    </Period>
    

#### Order by bitrate

Some players may be sensitive to the ordering of the video renditions. You can set the order of the video renditions to `ascending` or `descending`, as in the following:
    
    
    {
      "manifestOptions": {
        "bitrateOrder": "descending",
      },
    }

The following will be displayed in the stitched manifest:
    
    
    <Period id="0" start="PT33160.000S">
      <AdaptationSet segmentAlignment="true" maxWidth="1280" maxHeight="720">
        <Representation mimeType="video/mp4" id="1280x720-h264" codecs="avc1.64001E" width="1280" height="720" startWithSAP="1" bandwidth="240000" frameRate="25/1">
          ...
        </Representation>
        <Representation mimeType="video/mp4" id="1280x720-h265" codecs="hvc1.1.4.L126.B0" width="1280" height="720" startWithSAP="1" bandwidth="200000" frameRate="50/1">
          ...
        </Representation>
        <Representation mimeType="video/mp4" id="640x360-h264" codecs="avc1.64001E" width="640" height="360" startWithSAP="1" bandwidth="150000" frameRate="25/1">
          ...
        </Representation>
        <Representation mimeType="video/mp4" id="640x360-h265" codecs="hvc1.1.4.L126.B0" width="640" height="360" startWithSAP="1" bandwidth="100000" frameRate="50/1">
          ...
        </Representation>
      </AdaptationSet>
      <AdaptationSet segmentAlignment="true">
        <Representation mimeType="audio/mp4" id="640x360-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
        <Representation mimeType="audio/mp4" id="1280x720-audio" codecs="mp4a.40.2" audioSamplingRate="44100" startWithSAP="1" bandwidth="48472">
          ...
        </Representation>
      </AdaptationSet>
    </Period>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
