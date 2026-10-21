---
url: https://docs.cloud.google.com/transcoder/docs/concepts/overview/
title: Overview of the Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:36.847670+00:00
---

# Overview of the Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Overview of the Transcoder API Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a technical overview of the Transcoder API, including features, terminology, and useful concepts. The Transcoder API implements a REST and RPC API that lets you submit, monitor, and manage transcoding jobs in Google Cloud. To submit jobs using the Transcoder API, you first upload media assets to Cloud Storage. After processing a job, the Transcoder API saves the resulting media back to Cloud Storage.

**Key Point:** The Transcoder API service is designed for asynchronous work. It does not provide strong guarantees around the timing of job processing and is therefore unsuitable for interactive applications where a user waits for the result.

## Features

The Transcoder API includes support for the following features:

  * [Output in different container formats](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats), including MPEG-4 (MP4), Dynamic Adaptive Streaming over HTTP (DASH, also known as MPEG-DASH), and HTTP Live Streaming (HLS)
  * Output at different bitrates and resolutions, including [audio-only output](https://docs.cloud.google.com/transcoder/docs/concepts/config-examples#audio-only)
  * Conversion to a [high dynamic range](https://docs.cloud.google.com/transcoder/docs/how-to/convert-to-hdr) (HDR) format
  * Enhance the video output programmatically, including: 
    * [Crop video dimensions](https://docs.cloud.google.com/transcoder/docs/how-to/crop-videos)
    * Insert [overlay images or animations](https://docs.cloud.google.com/transcoder/docs/how-to/create-overlays)
  * Configure low-level encoding parameters, such as the bitrate
  * Remix existing media content using comprehensive edit lists
  * Set the job mode to low-latency interactive mode or batch mode
  * Specify [audio loudness normalization](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#Audio.FIELDS.lufs)
  * Configure encryption of your output video to [support digital rights management and content protection](https://docs.cloud.google.com/transcoder/docs/how-to/encrypt-content)
  * [Insert ad keyframes](https://docs.cloud.google.com/transcoder/docs/how-to/insert-ad-breaks) to allow video player clients to insert ads
  * Create thumbnails from a generated [spritesheet of video frames](https://docs.cloud.google.com/transcoder/docs/how-to/generate-spritesheet)
  * Create job templates to save and reuse custom or complex configurations for transcoding jobs



For more information about the MP4 and MPEG-DASH standards, see [The Moving Picture Experts Group website](https://mpeg.chiariglione.org/). For more information about the HLS standard, see [HTTP Live Streaming](https://developer.apple.com/streaming/).

### Supported containers for content encryption

The following table shows the containers that are supported for content encryption.

Streaming protocol | Container | DRM system | Encryption scheme  
---|---|---|---  
HLS | TS | ClearKey | aes128  
HLS | TS | FairPlay | sampleAes  
HLS | fMP4 | FairPlay | mpegCenc cbcs only  
MPEG-DASH | fMP4 | Widevine | mpegCenc cenc or cbcs  
MPEG-DASH | fMP4 | PlayReady | mpegCenc cenc or cbcs  
  
### Access control

The Transcoder API [access control](https://docs.cloud.google.com/transcoder/docs/access-control) model is based on Google's [Identity and Access Management](https://docs.cloud.google.com/iam). IAM's fine-grained permissions give you control over what can be done with media data, and by whom.

## Limits

The following table shows limits per transcoding job.

Job limits  
---  
**Maximum input width**|  4096 px  
**Maximum input height**|  4096 px  
**Maximum output width**|  4096 px  
**Maximum output height**|  2160 px  
**Total output size**|  400 GB  
**Maximum[`EditList`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig) duration**| 24 hours  
**Maximum number of video streams**|  70  
**Maximum number of audio streams**|  50  
**Maximum number of text streams**|  50  
**Maximum number of mux streams**|  100  
**Maximum number of manifests**|  100  
**Maximum number of spritesheets**|  10  
  
## Concepts

This section provides important concepts regarding video files and how they are used with the Transcoder API.

### Components of a video file

Each video file has a container, which is the wrapper for the entire file. The Transcoder API uses [MuxStreams](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#muxstream) to define the container. Each container includes a set of [ElementaryStreams](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#elementarystream) to define the encoding of the video, audio, and caption text tracks for the file. Video and audio are compressed using codecs.

In the following example, the video is compressed using H.264 and the audio is compressed using AAC. Both are placed in an MP4 container.

![Components of a video file and an example](https://docs.cloud.google.com/static/transcoder/images/video-file-example.svg)  
**Figure 1.** Components of a video file (left) and an example MP4 file (right).

### Streaming protocol structure

For streaming media, content providers encode the same content at multiple bitrates (measured in Kilobits per second). The provider then generates a manifest file that points to the different files with different bitrates. The streaming media player uses the manifest file to select the appropriate file, and then pulls video a few seconds at a time. Each bitrate may be a single file or multiple short files, depending upon what the player supports.

Different resolutions of media are typically encoded to target different bitrates. For example, lower bitrates are encoded at standard definition (SD) instead of high definition (HD). The set of bitrates, resolutions, and codecs is called the Adaptive Bitrate (ABR) ladder. Streaming content providers may tune their own ladder based on CDN costs, user device types, bandwidth in-region, and other factors.

![Components of a streaming protocol structure and an example](https://docs.cloud.google.com/static/transcoder/images/streaming-protocol-example.svg)  
**Figure 2.** Components of a streaming protocol structure (top) and an example HTTP Live Streaming (HLS) implementation (bottom).

## Terminology

This section provides a glossary of useful terms for working with the Transcoder API.

### Ad break

An ad break is a short advertisement that appears before or during media playback. The Transcoder API supports an [ad break keyframe](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#adbreak) in the job configuration. The Transcoder API does not insert or play ads, or stop media playback; video player clients are responsible for handling the keyframe.

### Atom

An atom is a foundational data structure for defining a video's metadata and location. A video can comprise a complex nested hierarchy of different types of atoms, including audio, edit, and text atoms.

### Audio atom

An audio atom maps the audio from an elementary stream to an edit list.

### Codec type and profile

When selecting the codec for a video stream, you specify the codec type, such as H.264 and the profile, such as the default `high` profile.

### Container

A container is a wrapper that describes the relationship between the various components in a multiplexed stream, including media files and metadata. The Transcoder API supports the MP4, MPEG-DASH, and HLS container formats.

### Edit atom

An edit atom defines the start and end offsets for the individual segments of a stream that you want to combine in an edit list.

### Edit list

An edit list defines a sequence of edits as a timeline for the resulting file or manifest from a transcoding job.

### Elementary stream

An elementary stream is an encoding of an input file, such as an audio, video, or caption text track. You must package elementary streams before mapping and sharing the stream to different output formats.

### Entropy encoding

Entropy encoding is a form of lossless compression that the Transcoder API supports. When configuring jobs, you can specify either the Context-Adaptive Variable-Length Coding (CAVLC) or Context-Adaptive Binary Arithmetic Coding (CABAC) entropy coders.

### Job

A job is the basic unit for managing work with the Transcoder API. When you submit a job to the Transcoder API, it is processed asynchronously in a geographic location known as a [_region_](https://docs.cloud.google.com/transcoder/docs/locations). You can list and manage all jobs for a region.

The lifecycle of a job includes three steps: prepare, transcode, and package.

  * Prepare 
    * Download inputs from Cloud Storage
    * Analyze inputs
    * Validate inputs
  * Transcode 
    * Run transcoding operations on inputs
  * Package 
    * Stitch inputs
    * Multiplex inputs
    * Upload outputs to Cloud Storage



A job has an updated [state](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#ProcessingState). The service reports errors using the [`error`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.error) field.

### Job configuration

A job configuration represents many of the various settings you can customize when creating and submitting a job to the Transcoder API. You can specify configuration settings such as edit lists and where to insert ad break tags in an output manifest. You can create reusable job configurations as job templates for use in a Google Cloud region.

### Job mode

The Transcoder API supports two [job modes](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.mode): interactive and batch.

Interactive mode is the default job mode. Use this mode if you want job processing to start as soon as possible or if you want to have more granular control on which jobs are executed first. In this mode, the [concurrent job count quota](https://docs.cloud.google.com/transcoder/quotas#interactive-mode-quotas) controls how many jobs are run concurrently. After this quota is reached, any jobs you try to start are rejected.

Use batch mode to submit many jobs for which the processing latency isn't as critical as jobs submitted in the default interactive mode. You can specify the [job processing priority](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.batch_mode_priority) for a job in this mode. Jobs submitted in batch mode with the same priority value are put in a first-in, first out queue and have a job state of `PENDING` while they wait to be run. In this mode, the [batch pending job count quota](https://docs.cloud.google.com/transcoder/quotas#batch-mode-quotas) controls how many jobs are queued. After this quota is reached, any jobs you try to start are rejected. A job transitions to the `RUNNING` state when it is executed. The [batch concurrent job count quota](https://docs.cloud.google.com/transcoder/quotas#batch-mode-quotas) controls how many jobs are run concurrently.

You can use both modes at the same time. One mode does not have priority over the other. For more information on setting the job mode, see [Creating jobs in batch mode](https://docs.cloud.google.com/transcoder/docs/how-to/create-batch-jobs).

### Job template

By default, the Transcoder API applies a preset template called [`preset/web-hd`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.template_id) for populating a job configuration. This job configuration produces the following output files:

  * `manifest.m3u8`: The [primary playlist](https://developer.apple.com/documentation/http_live_streaming/example_playlists_for_http_live_streaming/creating_a_primary_playlist) for an HLS media stream. This file contains references to playlists for the high definition (HD) variant of the output and the standard definition (SD) variant of the output. 
    * `media-hd.m3u8`: Playlist for the high definition variant 
      * `media-hd0000000000.ts`: High definition video segment file
    * `media-sd.m3u8`: Playlist for the standard definition variant 
      * `media-sd0000000000.ts`: Standard definition video segment file
  * `manifest.mpd`: The playlist for an MPEG-DASH media stream. This file contains references to video-only and audio-only segment files. 
    * `audio-only0000000000.m4s`: Audio-only segment file
    * `video-only-hd0000000000.m4s`: High definition video-only segment file
    * `video-only-sd0000000000.m4s`: Standard definition video-only segment file
  * `sd.mp4`: Standalone standard definition video file
  * `hd.mp4`: Standalone high definition video file



You can [create and manage your own custom job templates](https://docs.cloud.google.com/transcoder/docs/how-to/job-templates) and specify them when creating jobs.

### Preprocessing

Preprocessing is the stage of a job that takes place prior to the main transcoding.

### Preprocessing configuration

A preprocessing configuration represents the settings you can apply to a video before the transcoding stage of a job. You can apply cropping or padding as part of this configuration.

### Rate control mode

The rate control mode indicates whether to process a job using either the constant rate factor (CRF) or variable bitrate (VBR) modes. CRF ensures constant quality throughout the processed media assets. VBR optimizes the encoding process to reduce the file size of the processed media assets. For streaming use cases, select the VBR rate control mode. For archival purposes, select the CRF rate control mode.

### Manifest

A manifest is a description of the available contents and metadata of an adaptive media stream to a client. In the Transcoder API, you can configure a job to output a manifest with a file name, a list of multiplexed streams, as well as the type of the manifest, which must be either HLS or MPEG-DASH.

### Text atom

A text atom maps the text from an elementary stream to an edit list.

### Text stream

A text stream encodes text data associated with a video, such as closed captions or subtitles.

## What's next

  * Try the [quickstart](https://docs.cloud.google.com/transcoder/docs/quickstart).
  * Learn how to complete specific [Transcoder API tasks](https://docs.cloud.google.com/transcoder/docs/how-to).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
