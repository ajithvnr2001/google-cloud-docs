---
url: https://docs.cloud.google.com/video-intelligence/docs/streaming/live-streaming-overview/
title: Stream live videos \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:06.275456+00:00
---

# Stream live videos  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/streaming/live-streaming-overview/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Stream live videos Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to annotate a video stream from standard live streaming protocols.

The Video Intelligence API Streaming API enables real-time streaming analysis for live media. Supported features include:

  * Live Label Detection

  * Live Shot Change Detection

  * Live Explicit Content Detection

  * Live Object Detection and Tracking




The [AIStreamer](https://github.com/google/aistreamer/tree/master/ingestion) ingestion library provides a set of open source interfaces and example code to connect to the Video Intelligence API Streaming API. The library supports:

  * HTTP Live Streaming (HLS): an HTTP based media streaming and communication protocol.

  * Real Time Streaming Protocol (RTSP): a network control protocol for streaming media servers. It is used in conjunction with Real Time Protocol (RTP) and Real Time Control Protocol (RTCP).

  * Real Time Messaging Protocol (RTMP): a protocol for streaming audio, video, and data over the Internet.




## To start using AIStreamer

The AIStreamer ingestion library includes the following examples (incuding a Docker example).

  * [Live Streaming](https://docs.cloud.google.com/video-intelligence/docs/streaming/live-streaming): Instructions for supporting live streaming protocols (HLS, RTSP and RTMP) in Video Intelligence API.

  * [Docker & Kubernetes](https://docs.cloud.google.com/video-intelligence/docs/streaming/docker-kubernetes): Instructions for using our docker example and kubernetes deployment.

  * [Live Label Detection](https://docs.cloud.google.com/video-intelligence/docs/streaming/live-label-detection): Instructions for streaming label analysis.

  * [Live Shot Change Detection](https://docs.cloud.google.com/video-intelligence/docs/streaming/live-shot-change-detection): Instructions for streaming shot change analysis.

  * [Live Explicit Content Detection](https://docs.cloud.google.com/video-intelligence/docs/streaming/live-explicit-content): Instructions for streaming explicit content analysis.

  * [Live Object Detection and Tracking](https://docs.cloud.google.com/video-intelligence/docs/streaming/live-object-tracking): Instructions for streaming object detection and tracking analysis.




## Code architecture

The AIStreamer ingestion library includes the following three directories:

  * [client](https://github.com/google/aistreamer/tree/master/ingestion/client): Python & C++ client libraries for connecting to Video Intelligence.

  * [env](https://github.com/google/aistreamer/tree/master/ingestion/env): Docker example for AIStreamer ingestion.

  * [proto](https://github.com/google/aistreamer/tree/master/ingestion/proto): Proto definitions and gRPC interface for Video Intelligence.




## Third-party dependencies

The open source AIStreamer ingestion library is based on the following Google-owned and third-party open source libraries.

  * [Bazel](https://bazel.build/): A build and test tool with multi-language support.

  * [gRPC](https://grpc.io/): A high performance, open-source universal RPC framework.

  * [Protobuf](https://developers.google.com/protocol-buffers): Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data.

  * [rules_protobuf](https://github.com/pubref/rules_protobuf): Bazel rules for building protocol buffers and gRPC services.

  * [glog](https://github.com/google/glog): C++ implementation of the Google logging module.

  * [gflags](https://github.com/gflags/gflags): C++ library that implements command-line flags processing.

  * [ffmpeg](https://www.ffmpeg.org/): A complete, cross-platform solution to record, convert and stream audio and video.

  * [gStreamer](https://gstreamer.freedesktop.org/): Another cross-platform multimedia processing and streaming framework.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
