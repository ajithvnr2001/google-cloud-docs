---
url: https://docs.cloud.google.com/video-intelligence/docs/streaming/streaming/
title: Streaming video annotation \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:38.454301+00:00
---

# Streaming video annotation  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/streaming/streaming/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Streaming video annotation Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to retrieve analyses of a video stream from a discrete file or from archived data. See [live video streaming](https://docs.cloud.google.com/video-intelligence/docs/streaming/live-streaming-overview) to learn how to annotate a live video stream.

You can use the streaming API ([StreamingVideoIntelligenceService](https://docs.cloud.google.com/video-intelligence/docs/reference/rpc/google.cloud.videointelligence.v1p3beta1#google.cloud.videointelligence.v1p3beta1.StreamingVideoIntelligenceService)) for real-time video detection with the following features:

  * [Analyze labels](https://docs.cloud.google.com/video-intelligence/docs/streaming/label-analysis).
  * [Detect shot changes](https://docs.cloud.google.com/video-intelligence/docs/streaming/shot-change).
  * [Detect explicit content](https://docs.cloud.google.com/video-intelligence/docs/streaming/explicit-content).
  * [Stream annotation to storage](https://docs.cloud.google.com/video-intelligence/docs/streaming/streaming-to-storage).
  * [Track objects](https://docs.cloud.google.com/video-intelligence/docs/streaming/object-tracking).



You can use [Vertex AI AutoML](https://docs.cloud.google.com/vertex-ai/docs/beginner/beginners-guide) for the following features:

  * [Action recognition](https://docs.cloud.google.com/video-intelligence/docs/streaming/action-recognition).
  * [Video classification](https://docs.cloud.google.com/video-intelligence/docs/streaming/video-classification).
  * [Object tracking](https://docs.cloud.google.com/video-intelligence/docs/streaming/automl-object-tracking).



## Using the Streaming API

You can split a video file into chunks and stream each chunk by using gRPC to send multiple messages to the Video Intelligence API streaming service. The first message can only contain a [StreamingVideoConfig](https://docs.cloud.google.com/video-intelligence/docs/reference/rpc/google.cloud.videointelligence.v1p3beta1#google.cloud.videointelligence.v1p3beta1.StreamingVideoConfig) message. All subsequent messages must only contain video data.

The Video Intelligence API streaming service returns a [response](https://docs.cloud.google.com/video-intelligence/docs/reference/rpc/google.cloud.videointelligence.v1p3beta1#google.cloud.videointelligence.v1p3beta1.StreamingAnnotateVideoResponse) that contains [results](https://docs.cloud.google.com/video-intelligence/docs/reference/rpc/google.cloud.videointelligence.v1p3beta1#google.cloud.videointelligence.v1p3beta1.StreamingVideoAnnotationResults) based on the [feature](https://docs.cloud.google.com/video-intelligence/docs/reference/rpc/google.cloud.videointelligence.v1p3beta1#google.cloud.videointelligence.v1p3beta1.StreamingFeature) that you specified in your video config.

In a gRPC request, you write the binary data directly to the stream. You do not need to convert the video content to base64.

We recommend that you keep the size of your video chunks to less than 10 MB.

The Video Intelligence also allows you to specify a [Google Cloud Storage bucket](https://docs.cloud.google.com/video-intelligence/docs/reference/rpc/google.cloud.videointelligence.v1p3beta1#google.cloud.videointelligence.v1p3beta1.StreamingAnnotateVideoResponse) for your results.

## Supported Video Codecs

Video Intelligence supports the following common video formats:

Format | Notes  
---|---  
MTS, FLV | All MTS, FLV video formats are supported.  
MP4 (MPEG4), MOV, 3GP | The MOOV atom must be at the beginning of the file. You can use the [ffmpeg](http://ffmpeg.org) tool to put the MOOV atom at the beginning of your video file, as shown in the following example:
    
    
    $ ffmpeg -i input_file.mp4 -c copy -map 0 -movflags faststart output_file.mp4  
  
MKV, WebM | Cues must be at the beginning of the file. You can use the [mkclean](https://www.matroska.org/downloads/mkclean.html) tool to move the cue to the start of the file, as shown in the following example:
    
    
    $ mkclean --keep-cues --optimize in.mkv out.mkv
    $ mkclean --keep-cues --optimize --doctype 4 in.webm out.webm  
  
For video formats that are not listed as supported, you can determine if your video file supports streaming by using a named pipe and the [ffmpeg](http://ffmpeg.org) tool. The following sample commands decode a video into PNG images at a rate of 0.2 fps. If your file can be successfully decoded using these commands, then you can stream it using the Video Intelligence streaming service.
    
    
    $ mkfifo /tmp/inpipe
    $ ffmpeg -i /tmp/inpipe -r 0.2 output_%04d.png
    $ cat [FILE NAME] > /tmp/inpipe

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
