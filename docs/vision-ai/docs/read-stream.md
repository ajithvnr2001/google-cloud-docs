---
url: https://docs.cloud.google.com/vision-ai/docs/read-stream/
title: Read and save stream data \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:37.452920+00:00
---

# Read and save stream data  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/read-stream/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Read and save stream data Stay organized with collections  Save and categorize content based on your preferences. 

After you have started to ingest streaming data into a deployed application you can view a stream's output.

## Read stream outputs

After you have successfully created an application that [saves results into a stream](https://docs.cloud.google.com/vision-ai/docs/manage-app#view-app-output) you can read a data source input stream or a model output stream.

###  Gemini Enterprise Agent Platform Vision SDK 

To send a request to read a model output stream you must [install the Gemini Enterprise Agent Platform Vision SDK](https://docs.cloud.google.com/vision-ai/docs/cloud-environment#install_the_streams_sdk).

**Note** : You may need to establish user access credentials by running the following command: `gcloud auth application-default login`. For more information about this command, see the [Gemini Enterprise Agent Platform Vision SDK reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login). 

Make the following variable substitutions:

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: Your location ID. For example, `us-central1`. [Supported regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). [More information](https://docs.cloud.google.com/about/locations).
  * STREAM_ID: The stream ID that you created in the cluster For example, `application-output-1234abcd`.



**Print stream content:**
    
    
    # This will print packets from a stream to stdout.
    # This will work for *any* stream, independent of the data type.
    vaictl -p PROJECT_ID \
             -l LOCATION_ID \
             -c application-cluster-0 \
             --service-endpoint visionai.googleapis.com \
    receive streams packets STREAM_ID
    

## Save video from a stream

Use the following command to save video stream output. This command reads the data from an ongoing live stream, and saves the video segments in an MP4 file format to the user specified output directory:

###  Gemini Enterprise Agent Platform Vision SDK 

To send a request to save video output from a stream you must [install the Gemini Enterprise Agent Platform Vision SDK](https://docs.cloud.google.com/vision-ai/docs/cloud-environment#install_the_streams_sdk).

**Note** : You may need to establish user access credentials by running the following command: `gcloud auth application-default login`. For more information about this command, see the [Gemini Enterprise Agent Platform Vision SDK reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login). 

Make the following variable substitutions:

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: Your location ID. For example, `us-central1`. [Supported regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). [More information](https://docs.cloud.google.com/about/locations).
  * STREAM_ID: The stream ID that you created in the cluster For example, `application-output-1234abcd`.
  * OUTPUT_PATH: The output video path. The default value is `/tmp/`.


    
    
    vaictl -p PROJECT_ID \
             -l LOCATION_ID \
             -c application-cluster-0 \
             --service-endpoint visionai.googleapis.com \
    receive streams video-file STREAM_ID --output OUTPUT_PATH
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
