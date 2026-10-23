---
url: https://docs.cloud.google.com/transcoder/docs/release-notes/
title: Transcoder API release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:18.265147+00:00
---

# Transcoder API release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Resources ](https://docs.cloud.google.com/transcoder/docs/resources)



Send feedback 

#  Transcoder API release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to the Transcoder API. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/transcode-release-notes.xml) directly. 

## August 21, 2025

v1

Feature

You can automatically generate subtitle from your input video. For more information, see [Configure automatically generated subtitles](https://docs.cloud.google.com/transcoder/docs/how-to/configure-auto-generated-subtitles).

v1

Feature

You can process videos with significant number of missing frame by using the `fill_content_gaps` field. For more information, see [troubleshooting guide](https://docs.cloud.google.com/transcoder/docs/troubleshooting#quality-issues)

## May 22, 2025

v1

Feature

Standalone VTT outputs are now [supported](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats).

## February 04, 2025

v1

Feature

Standalone MP3 audio-only outputs are now [supported](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats).

## October 07, 2024

v1

Feature

Standalone OGG Vorbis audio-only outputs are now [supported](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats).

## February 23, 2024

v1

Feature

You can now set an exact frame rate on the output video. For more information, see [Frame rate conversion strategies](https://docs.cloud.google.com/transcoder/docs/concepts/frame-rate#conversion-strategies).

## February 05, 2024

v1

Feature

You can now convert the input video in a transcoding job to a supported [high dynamic range (HDR) format](https://docs.cloud.google.com/transcoder/docs/how-to/convert-to-hdr).

## July 10, 2023

v1

Feature

[Content encryption](https://docs.cloud.google.com/transcoder/docs/how-to/encrypt-content) (DRM) is now supported.

v1

Feature

[Job processing optimizations](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#optimizationstrategy) can now be disabled.

v1

Feature

You can now set the [priority of individual jobs](https://docs.cloud.google.com/transcoder/docs/concepts/overview#job_mode) in batch mode.

## April 06, 2023

v1

Feature

[Overlays](https://docs.cloud.google.com/transcoder/docs/how-to/create-overlays) can now be created using PNG images (with or without transparency).

## April 03, 2023

v1

Feature

[Batch mode](https://docs.cloud.google.com/transcoder/docs/concepts/overview#job_mode) is now supported. You can use it to create thousands of jobs that will be processed on a first in, first out basis.

## March 02, 2023

v1

Feature

You can now set the language code and display name for [text](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#TextStream.FIELDS.language_code) and [audio](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#AudioStream.FIELDS.language_code) streams.

## February 15, 2023

v1

Change

Validation checks added for [`segmentDuration`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#SegmentSettings.FIELDS.segment_duration) and [`gopDuration`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#H264CodecSettings.FIELDS.gop_duration) for all video codecs as outlined in the documentation. This change was released earlier this month.

## November 17, 2022

v1

Fixed

The output color space of transcoded videos matches the input color space.

## August 25, 2022

v1

Feature

[Deinterlace configurations](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#deinterlace) are now supported.

## August 23, 2022

v1

Feature

Audio-only outputs are now supported. For more information, see the [Pricing page](https://cloud.google.com/transcoder/pricing) and the [sample configuration](https://docs.cloud.google.com/transcoder/docs/concepts/config-examples#audio-only).

v1

Feature

Labels are now supported. Labels are key-value pairs you can use to [organize resources](https://docs.cloud.google.com/transcoder/docs/how-to/label-resources).

## March 01, 2022

v1

Issue

The following preprocessing configurations are not supported: [Color](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#color), [Denoise](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#denoise), [Deblock](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#deblock), and [Boost](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#audio).

## February 01, 2022

v1

Breaking

The v1beta1 API is no longer available. As [previously announced](https://docs.cloud.google.com/transcoder/docs/release-notes#July_13_2021), the v1beta1 API was deprecated in July 2021.

v1

Issue

VP9 codec settings do not support a [`rateControlMode`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#Vp9CodecSettings.FIELDS.rate_control_mode) set to `crf` (constant rate factor).

v1

Feature

Added v1 [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference/transcoder).

v1

Feature

Added a guide on how to [concatenate multiple input videos](https://docs.cloud.google.com/transcoder/docs/how-to/concatenate-videos) into a single output video.

v1

Feature

Added a guide on how to [include captions and subtitles in an output video](https://docs.cloud.google.com/transcoder/docs/how-to/captions-and-subtitles).

## November 01, 2021

v1

Feature

Added [PHP code samples](https://docs.cloud.google.com/transcoder/docs/samples).

## September 30, 2021

v1

Announcement

**Transcoder API is GA** : The Transcoder API has graduated out of beta and has reached v1. All API endpoints are updated to use `https://transcoder.googleapis.com/v1/`.

v1

Feature

Added [Troubleshooting](https://docs.cloud.google.com/transcoder/docs/troubleshooting) guide.

v1

Feature

Added [guidance on job limits](https://docs.cloud.google.com/transcoder/docs/concepts/overview#limits).

## August 31, 2021

v1

Feature

All client library [code samples](https://docs.cloud.google.com/transcoder/docs/samples) updated to v1 of the API.

v1

Issue

Encryption support (and its associated documentation) is temporarily unavailable.

v1

Change

Delete operations for [jobs](https://docs.cloud.google.com/transcoder/docs/how-to/jobs#delete_jobs) and [job templates](https://docs.cloud.google.com/transcoder/docs/how-to/job-templates#delete_job_template) now return a 404 resource not found error if the specified resource name does not exist. Previously, these delete operations failed silently in this case. To enable the previous behavior, set the `allowMissing` query parameter to `true` when sending a request to [delete a job](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs/delete#query-parameters) or [job template](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobTemplates/delete#query-parameters).

## August 02, 2021

v1

Change

Added new quotas in order to group requests into 3 buckets: mutation, get, and list. More information can be found at [Quotas and limits](https://docs.cloud.google.com/transcoder/quotas).

## July 13, 2021

v1 & v1beta1

Feature

Transcoder v1 API is now available. See the [migration guide](https://docs.cloud.google.com/transcoder/docs/how-to/migrate-to-v1) for information on how to update your job templates to the new version.

v1 & v1beta1

Deprecated

The Transcoder v1beta1 API is deprecated and will be turned down. It is replaced by the Transcoder v1 API.

v1 & v1beta1

Issue

The API outputs CEA-608 captions instead of CEA-708.

## March 31, 2021

v1beta1

Feature

Beta stage support for [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## February 26, 2021

v1beta1

Feature

[Sprite sheets](https://docs.cloud.google.com/transcoder/docs/how-to/generate-spritesheet) now preserve the source aspect ratio. Set the sprite width or height field, but not both (the API will automatically calculate the missing field).

v1beta1

Feature

[Sprite sheets](https://docs.cloud.google.com/transcoder/docs/how-to/generate-spritesheet) now support different image compression levels with the new [`quality`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1beta1/JobConfig#SpriteSheet.FIELDS.quality) setting.

v1beta1

Feature

The API now supports video [padding](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1beta1/JobConfig#pad) with black.

## November 16, 2020

v1beta1

Feature

The Transcoder API supports [overlays](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1beta1/JobConfig#overlay).

v1beta1

Feature

The Transcoder API preserves the aspect ratio of the source video.

v1beta1

Feature

Added Shaka player compatibility for Dash and HLS CEA608/CEA708. Shaka player version 3.0 is used for validation testing.

v1beta1

Feature

Content encryption is supported for the following containers:

Type | Technology | Format | Video Codecs |  | Audio Codecs  
---|---|---|---|---|---  
|  |  | H.264 | H.265 | AAC  
DRM | FairPlay | HLS | TS (SAMPLE-AES) | fMP4 (SAMPLE-AES) | TS (SAMPLE-AES)  
fMP4 (SAMPLE-AES) |  | fMP4 (SAMPLE-AES)  
DRM | Widevine, PlayReady | DASH | fMP4 (MPEG-CENC) | fMP4 (MPEG-CENC) |   
DRM | Widevine, PlayReady | HLS | fMP4 (MPEG-CENC) | fMP4 (MPEG-CENC) |   
Content protection | AES-128 | HLS, DASH | fMP4, TS (AES-128) | fMP4, TS (AES-128) | fMP4, TS (AES-128)  
  
v1beta1

Fixed

Improved performance for short input files.

v1beta1

Feature

[Client libraries](https://docs.cloud.google.com/transcoder/docs/reference/libraries) released.

v1beta1

Feature

The Transcoder API supports [cropping](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1beta1/JobConfig#crop).

v1beta1

Feature

The [Cloud SDK](https://docs.cloud.google.com/sdk) now supports the Transcoder API.

## July 22, 2020

The Transcoder API provides output Feature

video using the VP9 codec. 

The Transcoder API provides output Feature

subtitles using the WebVTT container. 

The Transcoder API supports the following encryption standards for audio and video outputs:

Feature

  * AES-128 and SAMPLE-AES for TS
  * MPEG Common Encryption (MPEG-CENC) for fmp4



## June 12, 2020

The Transcoder API provides output Feature

video using the H.265 codec. 

The cumulative size of input files was limited to Fixed

150 GB per job. This size has been increased to 400 GB per job. 

## April 15, 2020

**Private beta release:** The Feature

Transcoder API converts video files into formats suitable for consumer distribution. 

The Transcoder API provides output Feature

video using the H.264 codec. 

The Transcoder API supports the Feature

following audio coding standards for audio output: 

  * Dolby Digital audio codec (AC-3)
  * Dolby Digital plus, also known as enhanced AC-3 (E-AC-3)
  * Advanced audio coding high-efficiency (AAC-HE)
  * Advanced audio coding low-complexity (AAC-LC)



The Transcoder API supports the Feature

following output container formats: 

  * MPEG-4 (MP4)
  * Dynamic adaptive streaming over HTTP (DASH, also known as MPEG-DASH), comprising of a manifest and fMP4 files
  * HTTP Live Streaming (HLS), comprising of manifests and media files
  * MPEG transport stream



The Transcoder API supports the Feature

following additional advanced capabilities: 

  * Reusable job templates for managing job configurations
  * Caption mapping
  * Edit lists
  * Manifest naming and stream control
  * Priority queues
  * Ad-break and SCTE-35 insertion in streams and manifests
  * Flexible multiplexing and reusable elementary streams
  * Customizable H.264 codec parameters
  * Audio normalization during preprocessing
  * Sprite sheet generation, for previews and thumbnails
  * Pub/Sub notifications



The cumulative size of input files is limited to Issue

150 GB per job.

VPC Service Controls is not supported. If your Issue

Google Cloud project uses VPC Service Controls, you can't set up a service perimeter around the Transcoder API.

The default `preset/web-hd` preset Issue

assumes every input file has at least one audio and one video track. If the input doesn't include either audio or video, the job fails.

Output is limited to a maximum frame rate of Issue

120 fps and resolution of 3840 x 2160.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
