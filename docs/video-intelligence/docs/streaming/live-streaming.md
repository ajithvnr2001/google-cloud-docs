---
url: https://docs.cloud.google.com/video-intelligence/docs/streaming/live-streaming/
title: How-to stream live videos \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:28.507879+00:00
---

# How-to stream live videos  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/streaming/live-streaming/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  How-to stream live videos Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Video Intelligence Streaming API supports standard live streaming protocols like RTSP, RTMP, and HLS. The [AIStreamer](https://github.com/google/aistreamer/tree/master/ingestion) ingestion pipeline behaves as a streaming proxy, converting from live streaming protocols to bidirectional streaming gRPC connection.

To support live streaming protocols, the Video Intelligence API uses the [GStreamer](https://gstreamer.freedesktop.org/) open media framework.

## Step 1: Create a named pipe

A named pipe is created to communicate between GStreamer and the AIStreamer ingestion proxy. The two processes are running inside the same Docker container.

  * path_to_pipe: file path in your local environment. For example, /user/local/Desktop/
  * name_of_pipe: name of pipe you provide. For example, `my-football-game`


    
    
    $ export PIPE_NAME=/path_to_pipe/name_of_pipe
    $ mkfifo $PIPE_NAME

Example: `/user/local/Desktop/my-football-game`

## Step 2: Run AIStreamer ingestion proxy

These [C++ examples](https://github.com/google/aistreamer/tree/master/ingestion/client/cpp), available for your use, inclue a [single binary](https://github.com/google/aistreamer/blob/master/ingestion/client/cpp/BUILD) that supports all features. To build the examples, follow these build instructions.

The following example shows how to use the binary from the command line.
    
    
    $ export GOOGLE_APPLICATION_CREDENTIALS=/path_to_credential/credential_json
    $ export CONFIG=/path_to_config/config_json
    $ export PIPE_NAME=/path_to_pipe/name_of_pipe
    $ export TIMEOUT=3600
    $ ./streaming_client_main --alsologtostderr --endpoint "dns:///alpha-videointelligence.googleapis.com" \
          --video_path=$PIPE_NAME --use_pipe=true --config=$CONFIG --timeout=$TIMEOUT

`$GOOGLE_APPLICATION_CREDENTIALS` specifies the file path of the JSON file containing your service account key.

You can find an example configuration file—`$CONFIG` at [github](https://github.com/google/aistreamer/tree/master/ingestion/client/cpp/config).

Make sure to set the correct timeout flag in the command line. If you need to stream a 1 hour of video, timeout value should be at least 3600 seconds.

## Step 3: Run GStreamer pipeline

GStreamer supports multiple live streaming protocols including but not limited to:

  * HTTP Live Streaming (HLS)

  * Real-time Streaming Protocol (RTSP)

  * Real-time Protocol (RTP)

  * Real-time Messaging Protocol (RTMP)

  * WebRTC

  * Streaming from Webcam




The Video Intelligence API uses the GStreamer pipeline to convert from these live streaming protocols to a decodable video stream, and writes the stream into the named pipe created in Step 1.

The following examples demonstrate how to use the live streaming library using HLS, RTSP and RTMP protocols.

### HTTP Live Streaming (HLS)
    
    
    $ export PIPE_NAME=/path_to_pipe/name_of_pipe
    $ export HLS_SOURCE=http://abc.def/playlist.m3u8
    $ gst-launch-1.0 -v souphttpsrc location=$HLS_SOURCE ! hlsdemux ! filesink location=$PIPE_NAME

### Real-time Streaming Protocol (RTSP)
    
    
    $ export PIPE_NAME=/path_to_pipe/name_of_pipe
    $ export RTSP_SOURCE=rtsp://ip_addr:port/stream
    $ gst-launch-1.0 -v rtspsrc location=$RTSP_SOURCE ! rtpjitterbuffer ! rtph264depay \
          ! h264parse ! flvmux ! filesink location=$PIPE_NAME

**Note:** You can choose any muxer that supports streaming (for example, flvmux or mpegtsmux)

### Real-time Message Protocol (RTMP)
    
    
    $ export PIPE_NAME=/path_to_pipe/name_of_pipe
    $ export RTMP_SOURCE=rtmp://host/app/stream
    $ gst-launch-1.0 -v rtmpsrc location=$RTMP_SOURCE ! flvdemux ! flvmux ! filesink location=$PIPE_NAME

## Build instructions

The [binary example](https://github.com/google/aistreamer/blob/master/ingestion/client/cpp/BUILD) is built using [Bazel](https://bazel.build). A [Docker example](https://github.com/google/aistreamer/blob/master/ingestion/env/Dockerfile) that has all build dependencies configured is also provided. You can find the compiled `streaming_client_main` binary in the `$BIN_DIR` directory of the Docker image.

For more information on using Docker, see [Using Docker & Kubernetes](https://docs.cloud.google.com/video-intelligence/docs/streaming/docker-kubernetes).

## Flow control

The Video Intelligence Streaming API server has inherent flow control. In the following two cases,[`StreamingAnnotateVideoRequest`](https://docs.cloud.google.com/video-intelligence/docs/reference/rpc/google.cloud.videointelligence.v1#google.cloud.videointelligence.v1.StreamingAnnotateVideoRequest) requests are rejected, and gRPC streaming connections are stopped immediately:

  * The AIStreamer ingestion client is sending requests to Google servers too frequently.

  * The AIStreamer ingestion client is sending too much data to Google servers (beyond 20Mbytes per second).




## Visualizer

The visualizer code provided in AIStreamer should only be considered as a code example. The visualizer may _not_ be compatible with the user's local environment. AIStreamer users should _not_ rely on the client code to visualize annotation results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
