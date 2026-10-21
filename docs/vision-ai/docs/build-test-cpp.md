---
url: https://docs.cloud.google.com/vision-ai/docs/build-test-cpp/
title: Build and test with the C++ SDK \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:36.222274+00:00
---

# Build and test with the C++ SDK  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/build-test-cpp/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Build and test with the C++ SDK Stay organized with collections  Save and categorize content based on your preferences. 

The C++ SDK is a tool available as part of the Gemini Enterprise Agent Platform Vision SDK. You can use the C++ SDK to programmatically manage, control, and perform different forms of I/O with Gemini Enterprise Agent Platform Vision.

This page describes how to use the C++ SDK to build and test.

## Before you begin

  * Complete the steps to [set up your Google Cloud project](https://docs.cloud.google.com/vision-ai/docs/cloud-environment).
  * Review [system requirements](https://docs.cloud.google.com/vision-ai/docs/cloud-environment#cpp-supported-platforms) before trying to use the C++ SDK.
  * Get the Gemini Enterprise Agent Platform Vision SDK source code from the publicly available [GitHub](https://github.com/google/visionai) repository:
        
        git clone https://github.com/google/visionai.git
        

The C++ public SDK is located in `visionai/public/streams.h`. For reference information, see the [reference documentation](https://docs.cloud.google.com/vision-ai/docs/reference/cpp).

  * Install any [system dependencies](https://docs.cloud.google.com/vision-ai/docs/cloud-environment#cpp-system-deps) you might need.

  * Use the [create streams and ingest data](https://docs.cloud.google.com/vision-ai/docs/create-manage-streams) topic to create stream resources to use in the following code samples.




## Build and test programs

The following example shows you how to use the C++ programming SDK to build your own programs. The sample shows this process directly by walking through an example for sending and receiving [`Packets`](https://docs.cloud.google.com/vision-ai/docs/reference/cpp/group/packet).

These instructions show you how to build two simple programs. The first program sends messages at regular intervals, while the second program receives the messages that the first program sends. You can use these programs as a starting point to build your own custom applications with the C++ SDK.

  1. Go to the root of the source code directory.

The contents of the directory resemble the following:
         
         bazel  BUILD  CONTRIBUTING.md  debian  deps.bzl  LICENSE  README.md  third_party  visionai [...]
         

  2. Optional: Read the tutorial source code instructions.

**Sender app:**
         
         cat visionai/public/tutorial/sender_app.cc
         

**Receiver app:**
         
         cat visionai/public/tutorial/receiver_app.cc
         

  3. Build the sender and receiver apps.
         
         bazel build //visionai/public/tutorial/...
         

  4. Verify the build worked. In one terminal, run the following command for the sender app. Replace the following:

     * PROJECT_ID: Your project ID.
     * LOCATION_ID: Your location ID. For example, `us-central1`. [Supported regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). [More information](https://docs.cloud.google.com/about/locations).
     * STREAM_ID: The stream ID that you created in the cluster. For example, `input-1`.
    
    ./bazel-bin/visionai/public/tutorial/sender_app \
    --service_endpoint visionai.googleapis.com \
    --project_id PROJECT_ID \
    --location_id LOCATION_ID \
    --cluster_id application-cluster-0 \
    --stream_id STREAM_ID

  5. In a different terminal, run the following command for the receiver app. Replace the following:

     * PROJECT_ID: Your project ID.
     * LOCATION_ID: Your location ID. For example, `us-central1`. [Supported regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). [More information](https://docs.cloud.google.com/about/locations).
     * STREAM_ID: The stream ID that you created in the cluster. For example, `input-1`.
    
    ./bazel-bin/visionai/public/tutorial/receiver_app \
    --service_endpoint visionai.googleapis.com \
    --project_id PROJECT_ID \
    --location_id LOCATION_ID \
    --cluster_id application-cluster-0 \
    --stream_id STREAM_ID




## What's next

  * Read about processing components you can add to an app in [Build an app](https://docs.cloud.google.com/vision-ai/docs/build-app).
  * Learn about output storage and processing options in [Connect app output to a data destination ](https://docs.cloud.google.com/vision-ai/docs/connect-data-destination).
  * Read about how to [Search Warehouse data in the console](https://docs.cloud.google.com/vision-ai/docs/search-streaming-warehouse).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
