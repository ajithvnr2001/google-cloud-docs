---
url: https://docs.cloud.google.com/vision-ai/docs/batch-video-warehouse-overview/
title: Batch Video Warehouse Overview \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:03.909520+00:00
---

# Batch Video Warehouse Overview  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/batch-video-warehouse-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Batch Video Warehouse Overview Stay organized with collections  Save and categorize content based on your preferences. 

Batch Video Warehouse (also known as Video on Demand Warehouse) helps developers to:

  * Import video files from Cloud Storage.
  * Import video metadata.
  * Analyze video content embeddings.
  * Construct and deploy search indexes for AI-powered video search.

**Important:** Batch Video Warehouse does not copy or store video data. There is no additional storage charge by importing video files.

There are a few basic steps to use a Batch Video Warehouse:

  1. **Upload and analyze videos** : Create a [`corpus`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora), [`upload`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.assets/upload) video assets, generate video embeddings by [`analyze`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.assets/analyze) the video assets. Additionally, developers can define [`data schema`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.dataSchemas) and [`annotations`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.assets.annotations) to enrich videos with supplementary metadata.
  2. **Build and deploy search indexes** : Create an [`index`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes) and [`deploy`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.indexEndpoints/deployIndex) the index to an [`index endpoint`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.indexEndpoints) for search. A deployed index is managed by a dedicated pool of resources that scales with the size of the index.
  3. **Search, browse, and update index data** : Perform semantic [`search`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.indexEndpoints/searchIndexEndpoint) for relevant video partitions on a deployed index with text queries, images, or filter criteria on the annotation metadata. Users can also browse the corpus or index contents through [`ListAssets`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.assets/list) and [`ViewIndexedAssets`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes/viewAssets) respectively. Batch Video Warehouse provides two ways for updating video assets in the index: 
     * **Incremental update** : Use the [`IndexAsset`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.assets) or [`RemoveIndexAsset`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.assets/removeIndex) APIs to update one video at a time. This method leads to limited throughput, but low update latency.
     * **Batch update** : Use the [`UpdateIndex`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes/patch) API with the [`asset_filter`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.indexes) parameter to fully rebuild the index. This way is preferred when you have a large number of videos to add or remove from the index.



## Supported video formats

Warehouse backends support popular formats such as MP4, AVI, FLV, MKV, MOV, MXF, WMV, and the formats decodable by [FFmpeg](https://ffmpeg.org/).

The frontend, which is only for demo purposes, supports MP4 and MKV.

## What's next

Start onboarding with the demo [colab](https://colab.sandbox.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/vision/video_warehouse_sdk.ipynb).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
