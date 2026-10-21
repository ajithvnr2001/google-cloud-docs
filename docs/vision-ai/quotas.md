---
url: https://docs.cloud.google.com/vision-ai/quotas/
title: Quotas and limits \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:31.643032+00:00
---

# Quotas and limits  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/quotas/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Resources ](https://docs.cloud.google.com/vision-ai/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

## Quotas

The following quotas apply to Agent Platform Vision. These quotas apply to each Google Cloud console project and are shared across all applications and IP addresses using that project.

If you would like to process more requests, submit a Agent Platform Vision quota request for your project in the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas).

Please provide information about your specific needs and use case in the request.

### General quotas

The following general quotas apply when you use Gemini Enterprise Agent Platform Vision:

Quota | Value  
---|---  
API requests per minute per project | 1200  
  
### Stream quotas

The following quotas apply when using the Streams ingestion feature of Gemini Enterprise Agent Platform Vision:

Quota | Value  
---|---  
Streams per project per region | 1000  
Events per project per region | 20,000  
Analyses per project per region | 3000  
Series per project per region | 500,000  
Create event requests per minute per project per region | 600  
Sent packets per second per series | 100  
Sent bytes per second per series | 10MB  
  
### Application platform quotas

The following quotas apply when you create and use an app using Gemini Enterprise Agent Platform Vision's App platform:

Quota | Value  
---|---  
Application created per project per region | 100  
Application deployed per project per region | 10  
Processor(Custom Model) per project per region | 100  
Instance created per project per region | 1000  
Instance Deployed per project per region | 100  
  
### Vision Warehouse quotas

The following quotas apply to Vision Warehouse. Unless explicitly specified, quotas are per project, per region.

Vision Warehouse general quotas per project:

Quota | Value  
---|---  
Warehouse API requests per minute | 3,600  
Ingested* user specified annotation size per minute | 15 MB  
  
* This quota applies to annotations ingested using `CreateAnnotation` and `UpdateAnnotation` APIs.

Streaming Warehouse specific quotas per project:

Quota | Value  
---|---  
SearchAssets API requests per minute | 120  
Ingested media data per minute | 1,000 MB  
  
Warehouse storage and analysis quotas per project, per region:

Quota | Value  
---|---  
Number of images | 100,000,000  
Number of batch videos | 5,000,000  
Total duration of videos | 2,160,000 minutes  
Concurrent upload video operations | 100  
Concurrent analyze (video) asset operations | 100  
Concurrent analyze (image) corpus operations | 5  
  
Warehouse index and search quotas per project per region:

Quota | Value  
---|---  
Concurrent create index operations | 5  
Concurrent update index operations | 5  
Concurrent IndexAsset and RemoveIndexAsset operations | 100  
Search index endpint requests per minute | 6,000  
  
## Limitations

The following limitations apply for the Preview release of Gemini Enterprise Agent Platform Vision, and are subject to change in subsequent version releases.

Component | Limitation  
---|---  
Streams | Stream ingestion doesn't support a media type change ([video codec](https://en.wikipedia.org/wiki/Video_codec), resolution, etc.) after ingestion starts.  
Streams | The `vaictl` command line tool does not reconnect in the event that an ingestion stream RPC pauses.  
Streams | Ingestion video requirements: [H.264 encoding](https://en.wikipedia.org/wiki/Advanced_Video_Coding), < 1080p resolution, 25 FPS, no audio (audio is removed).  
Streams / Warehouse | A stream can connect to only one warehouse resource.  
Warehouse | Warehouse ingestion doesn't support media type change ([video codec](https://en.wikipedia.org/wiki/Video_codec), resolution, etc.) after ingestion starts.  
  
### Vision Warehouse limits

The following limits apply to Vision Warehouse. Unless explicitly specified, limits are for a given project in each region.

Warehouse storage limits:

Limit | Value  
---|---  
Maximum video length | 10 hours  
Maximum video file size | 10 GB  
Maximum image size | 10 MB  
Number of images per `ImportAssets` operation | 10,000,000  
Maximum annotation size | string: 1 MB, custom struct: 2 MB  
Number of asset-level annotations per asset | 1,000  
Number of partition-level annotations per video timestamp | 1,000  
Total partition-level annotation size per video timestamp | 5 MB  
Number of exact search leaf-level* data schemas | 10,000  
Number of smart search leaf-level* data schemas | 100  
  
* A data schema of `CUSTOMIZED_STRUCT` type can have multiple leaf-level data schemas. A data schema of non-`CUSTOMIZED_STRUCT` type is counted as one leaf-level data schema.

Warehouse index and search limits:

Limit | Value  
---|---  
Number of index endpoints | 15  
Number of indexes | 100  
Search request text query length | 1 KB  
Number of filter criteria in search request | 10  
Total length of text filter criteria | 1 KB  
Number of search configurations | 1,000  
Number of search hypernyms | 1,000  
Number of mapped facet fields | 3  
Number of mapped search criteria fields | 3  
Number of hyponyms per hypernym | 8  
Number of hypernym expansions in search request* | 10  
  
* One search request can contain multiple hypernyms and corresponds to more than 10 expanded requests. In this case, only the first 10 expansions are used in search.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
