---
url: https://docs.cloud.google.com/vision-ai/docs/create-manage-streams/
title: Create streams and ingest data \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:54.260483+00:00
---

# Create streams and ingest data  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/create-manage-streams/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Create streams and ingest data Stay organized with collections  Save and categorize content based on your preferences. 

The first step in analyzing your video data with an application is creating a pipeline for the continuous flow of data. Streams offers the ability to ingest real-time video data, which then can be used as input for models or stored in a Warehouse.

## Create a Stream

To be able to stream video data you must first create a stream.

The first time you create a stream in a new project it can take some time to create the stream. This time is around 30 minutes. This time is due to the system needing to initialize a computation cluster for subsequent computations. 

### Console

Create a stream in the Google Cloud console.

  1. Open the **Streams** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Streams tab](https://console.cloud.google.com/ai/vision-ai/video-streams)

  2. Click add**Register**.

  3. Enter the stream name and select a region. You can click **Add Row** to register multiple streams at the same time.

  4. Click the **Register** button to create one or more streams.




## Ingest videos

After you have created a stream you can begin to ingest data using that stream.

Some limitations and considerations apply to ingested video:

  * The input video source must have the following specifications: 
    * [H.264 encoding](https://en.wikipedia.org/wiki/Advanced_Video_Coding)
    * <= 1080p resolution
    * ~25 FPS

If the video doesn't meet these specifications Gemini Enterprise Agent Platform Vision may not process the input well. 

  * Audio is dropped during ingestion.
  * If the stream is part of an app connected to a warehouse, video parameters (such as FPS or resolution) must be the same for the whole stream ; variations in RTSP video data parameters or local video data parameters are not supported. 
  * Due to model startup latency, ingested videos may have the first few seconds of content missing. This amount of time can reach up to fifteen seconds. 
  * Ingestion termination can happen after long connection (~5 hours, on average). There's no reconnection capability from the `vaictl` tool ; users must manually reconnect. 
  * While `vaictl` is a useful tool for ingesting video data, the tool does not automatically handle recovery from network errors. These errors may either come from the data-source side or the Cloud-ingestion side. It's the user's responsibility to create a restart script to handle unexpected `vaictl` operation terminations. 



###  Gemini Enterprise Agent Platform Vision SDK 

To send a request to ingest video data using an existing stream you must [install the Gemini Enterprise Agent Platform Vision SDK](https://docs.cloud.google.com/vision-ai/docs/cloud-environment#install_the_streams_sdk).

**Note** : You may need to establish user access credentials by running the following command: `gcloud auth application-default login`. For more information about this command, see the [Gemini Enterprise Agent Platform Vision SDK reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login). 

Make the following variable substitutions:

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: Your location ID. For example, `us-central1`. [More information](https://docs.cloud.google.com/about/locations). [Supported regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions).
  * LOCAL_FILE.EXT: The filename of a local video file. For example, `my-video.mp4`.
  * STREAM_ID: The stream ID that you created in the cluster For example, `input-1`.
  * RTSP_ADDRESS: The address of your Real Time Streaming Protocol ([RTSP](https://en.wikipedia.org/wiki/Real_Time_Streaming_Protocol)) feed. For example, `rtsp://my-ip-camera`.



**Local video data:**
    
    
    # This command streams a video file to a stream. Streaming ends when the video ends.
    vaictl -p PROJECT_ID \
             -l LOCATION_ID \
             -c application-cluster-0 \
             --service-endpoint visionai.googleapis.com \
    send video-file to streams STREAM_ID --file-path LOCAL_FILE.EXT
    

**Local video data (looped):**
    
    
    # This command streams a video file to a stream. Video is looped into the stream until you stop the command.
    vaictl -p PROJECT_ID \
             -l LOCATION_ID \
             -c application-cluster-0 \
             --service-endpoint visionai.googleapis.com \
    send video-file to streams STREAM_ID --file-path LOCAL_FILE.EXT **--loop**
    

**Real Time Streaming Protocol (RTSP) feed data:**
    
    
    # This command will send an RTSP feed into the stream.
    # This command has to run in the network that has direct access to the RTSP feed.
    vaictl -p PROJECT_ID \
             -l LOCATION_ID \
             -c application-cluster-0 \
             --service-endpoint visionai.googleapis.com \
    send rtsp to streams STREAM_ID --rtsp-uri RTSP_ADDRESS
    

## Play ingested videos

After you have created a stream and sent video content to the stream you can play the video content.

If you leave the stream view tab open for more than one hour, you must refresh the page to continue to load video contents.

### Console

Play ingested video in the Google Cloud console.

  1. Open the **Streams** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Streams tab](https://console.cloud.google.com/ai/vision-ai/video-streams)

  2. Click on the stream name from the streams list.

  3. In the video stream detail page the ingested video live view automatically loads.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
