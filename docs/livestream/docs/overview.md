---
url: https://docs.cloud.google.com/livestream/docs/overview/
title: Overview of the Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:44.166955+00:00
---

# Overview of the Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Overview of the Live Stream API Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the Live Stream API. The Live Stream API transcodes mezzanine live signals into direct-to-consumer streaming formats, including Dynamic Adaptive Streaming over HTTP (DASH/MPEG-DASH), and HTTP Live Streaming (HLS), for multiple device platforms.

You first create an input endpoint, then create a channel resource that transcodes the live SRT or RTMP input signal into an HLS or DASH output stream. Output streams created by the Live Stream API are saved to Cloud Storage buckets. You can then configure a Cloud Storage bucket as a backend for Media CDN.

![Architecture overview for the Live Stream API.](https://docs.cloud.google.com/static/livestream/images/livestream_architecture_diagram.svg)

## Features

The Live Stream API includes support for the following features:

  * Automatic infrastructure provisioning

  * Integration with Cloud Storage, Cloud Audit Logs, and Google Cloud infrastructure

  * Configuration of a backup input stream for redundancy

  * Live to video on demand (VOD)

  * Content encryption

  * Slates (image and video)




### Supported inputs and outputs

The following tables show the supported input and output formats for the Live Stream API.

Input types | Supported formats  
---|---  
Protocols | SRT, RTMP  
Video codecs | H.264 (AVC)  
Audio codecs | AAC  
Captions | Embedded CEA-608/708 (passthrough)  
Output types | Supported formats  
---|---  
Protocols  | Apple HLS with fMP4 and MPEG2-TS segments, MPEG-DASH with fMP4 segments  
Video codecs | H.264 (AVC)  
Audio codecs | AAC  
Captions | Embedded CEA-608/708 (passthrough)  
Encryption | AES-128, SAMPLE-AES, MPEG-CENC  
Spritesheet images | JPG tiles, single images  
  
See the [supported configurations for content encryption](https://docs.cloud.google.com/livestream/docs/how-to/encrypt-content#supported-configurations).

## Access control

The Live Stream API access control model is based on [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs). IAM's fine-grained permissions give you control over what can be done with media data, and by whom.

## Concepts and terminology

This section provides a glossary of useful terms for working with the Live Stream API.

### Channels

A channel is a resource that ingests the input stream through an input endpoint, transcodes the input stream into multiple renditions, and publishes output live streams in certain formats in the specified location. You can include a primary and backup input stream in the same channel.

### Channel events

A channel event is a sub-resource of a channel that executes operations on a channel resource without needing to stop the channel. The following channel events are supported:

  * Create ad break markers
  * Mute/unmute the live stream
  * Insert a slate into the live stream
  * Return to program (live stream)
  * Switch the channel input



### Encoder

An encoder is a program used to send input streams, such as `ffmpeg`.

### Input endpoints

An input endpoint is an endpoint to which your encoder sends your input stream. You can use the input endpoint to specify configurations for your stream, such as input resolution, input type, and video cropping.

An input endpoint consists of either an RTMP or SRT URI that looks like the following:
    
    
    rtmp://192.0.2.1/live/STREAM_ID
    
    
    srt://192.0.2.1:4201?streamid=STREAM_ID

where `STREAM_ID` is a string such as `b8ebdd94-c8d9-4d88-a16e-b963c43a953b`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
