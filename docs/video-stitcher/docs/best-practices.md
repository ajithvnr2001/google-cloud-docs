---
url: https://docs.cloud.google.com/video-stitcher/docs/best-practices/
title: Best practices for the Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:40.883188+00:00
---

# Best practices for the Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/best-practices/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Best practices for the Video Stitcher API Stay organized with collections  Save and categorize content based on your preferences. 

This page contains a summary of best practices for the Video Stitcher API. If you are just starting out with the Video Stitcher API, refer to the [quickstart for livestreams](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-live) or the [quickstart for VOD assets](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod).

## Condition VOD assets

Configure source encoders and transcoders to output manifests that support ad breaks between DASH periods and HLS segments. The Video Stitcher API won't split periods or segments to stitch ad breaks, so ad breaks are only stitched at period and segment boundaries.

For ad tags that return VMAP responses, each ad break specified in the VMAP should match with a period or segment boundary. Otherwise, ad breaks will be stitched at the closest boundary.

### Avoid ad-break misalignment for HLS

For VOD stitching, you should precondition the source video manifest for midroll ad breaks and configure the Video Multiple Ad Playlist (VMAP) ad tag to return midroll ad breaks at the pre-conditioned offset positions. The Video Stitcher API takes the result of the transcoded output and inserts ads as close as possible to where you specify. Use pre-conditioned inputs for midroll ad breaks to make ad stitching behavior consistent and accurate.

For example, the following video playlist shows an ad placement opportunity at the seven second mark:
    
    
    #EXTM3U
    
    #EXT-X-VERSION:3
    #EXT-X-MEDIA-SEQUENCE:0
    #EXT-X-TARGETDURATION:4
    
    #EXTINF:2.0
    ../video/180_250000/hls/segment_0.ts
    #EXTINF:2.0
    ../video/180_250000/hls/segment_1.ts
    #EXTINF:2.0
    ../video/180_250000/hls/segment_2.ts
    #EXTINF:1.0
    ../video/180_250000/hls/segment_3.ts
    #EXT-X-PLACEMENT-OPPORTUNITY
    #EXTINF:2.0
    ../video/180_250000/hls/segment_4.ts
    

The following audio playlist shows an ad placement opportunity at the seven second mark:
    
    
    #EXTM3U
    
    #EXT-X-VERSION:3
    #EXT-X-MEDIA-SEQUENCE:0
    #EXT-X-TARGETDURATION:4
    
    #EXTINF:1.99
    ../audio/1_stereo_128000/hls/segment_0.ts
    #EXTINF:1.99
    ../audio/1_stereo_128000/hls/segment_1.ts
    #EXTINF:1.99
    ../audio/1_stereo_128000/hls/segment_2.ts
    #EXTINF:1.03
    ../audio/1_stereo_128000/hls/segment_3.ts
    #EXT-X-PLACEMENT-OPPORTUNITY
    #EXTINF:1.99
    ../audio/1_stereo_128000/hls/segment_4.ts
    

The following VMAP configuration specifies an ad break to occur at the seven second mark. The video and audio playlists will contain ad breaks at exactly the seven second mark:
    
    
    <vmap:VMAP xmlns:vmap="http://www.iab.net/videosuite/vmap" version="1.0">
      <vmap:AdBreak timeOffset="00:00:07.000" breakType="linear" breakId="midroll‑1">
        <vmap:AdSource id="midroll-1‑ad‑1" allowMultipleAds="false" followRedirects="true">
          <vmap:AdTagURI templateType="vast3">
          <![CDATA[
          https://securepubads.g.doubleclick.net/gampad/ads?...
          ]]>
          </vmap:AdTagURI>
        </vmap:AdSource>
      </vmap:AdBreak>
    </vmap:VMAP>
    

## Set EXT-X-PROGRAM-DATE-TIME for HLS

To ensure that segment timings are synced across HLS renditions, we recommend that you set `EXT-X-PROGRAM-DATE-TIME` for each HLS rendition. This helps the players transition smoothly when changing renditions during playback.

## Use multi-period DASH manifests for live and VOD assets

Configure source encoders and transcoders to output DASH manifests with multiple periods rather than a single period. For reasons similar to VOD conditioning, the Video Stitcher API won't split periods to stitch ad breaks, so a DASH manifest with multiple periods will have more opportunities to stitch ad breaks at the expected durations.

### Encapsulate subtitles in ISOBMFF

Subtitles for DASH manifests should be encapsulated in ISO base media file format (ISOBMFF), such as MP4, for compatibility with the most media players.

## Use constant bitrates

To ensure a stable playback experience for livestreams, configure the source encoder or transcoder to use constant bitrates when outputting stream manifests. This allows the Video Stitcher API to stitch ads more consistently to match the encoding profiles specified in the manifests.

## Use supported ad markers

Consult the [ad markers](https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-markers) documentation to understand what ad markers are supported and how source encoders or transcoders should output ad markers to ensure ad breaks are stitched successfully.

## Verify source playback

To ensure a stable playback experience for live and VOD streams, consider using widely available client players to verify that source streams are playable before stitching with the Video Stitcher API.

HLS:

  * [hls.js](https://hlsjs.video-dev.org/demo/)
  * [Safari](https://support.apple.com/downloads/safari)
  * [Shaka Player](https://shaka-player-demo.appspot.com/)
  * [video.js](https://videojs.com/)



DASH:

  * [dash.js](https://reference.dashif.org/dash.js/nightly/samples/dash-if-reference-player/index.html)
  * [Shaka Player](https://shaka-player-demo.appspot.com/)
  * [video.js](https://videojs.com/)



## Manage CDN keys

If the source media is protected by URL signing, then you need to register CDN keys with the Video Stitcher API. This allows the API to:

  * Fetch the source video manifests for stitching
  * Sign the source video segments, so that players can fetch the video segments for playback



See information on how to [manage CDN keys](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys).

## Set up Media CDN

If you want to set up Media CDN to distribute the media assets, follow the [Media CDN quickstart](https://docs.cloud.google.com/media-edge/docs/quickstart).

Configure separate routes with appropriate TTLs for your manifests and media segments. For details and examples, see the [Media CDN Advanced Routing guide](https://docs.cloud.google.com/media-cdn/docs/routing).

If any of your routes use private Cloud Storage origins, see [Using private Cloud Storage buckets](https://docs.cloud.google.com/media-cdn/docs/origins#private-storage-buckets). **In particular, set the cache mode for these routes to`FORCE_CACHE_ALL`**.

For directions on setting up HTTPS, see [Configure SSL (TLS) certificates](https://docs.cloud.google.com/media-edge/docs/configure-ssl-certificates).

### Media CDN signed requests

To use Media CDN with signed requests enabled, see [Use signed requests](https://docs.cloud.google.com/media-edge/docs/signed-requests) and then do the following:

  1. [Create an asymmetric key pair](https://docs.cloud.google.com/media-cdn/docs/create-keys). For information on creating a private key that is compatible with the Video Stitcher API, see [Create a private key for Media CDN](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn) .

  2. [Register the private Media CDN key](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#register_cdn_key) with the Video Stitcher API.




## Duration limit for long-running live sessions

A [LiveSession](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions) resource won't expire unless 5 minutes has elapsed without any playlist requests. However, a maximum lifetime of 180 days is enforced for all playback URIs. In order to continue playback after 180 days has elapsed, you must create a new live session. For reliability, you should create a new live session at least every 30 days.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
