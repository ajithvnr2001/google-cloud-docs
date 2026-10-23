---
url: https://docs.cloud.google.com/vision-ai/docs/warehouse-overview/
title: Vision Warehouse overview \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:15.986540+00:00
---

# Vision Warehouse overview  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/warehouse-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Vision Warehouse overview Stay organized with collections  Save and categorize content based on your preferences. 

Vision Warehouse is an API that enables developers to integrate storage and AI-based search of unstructured media content (streaming video, images, and batch videos) into existing tools and applications.

Vision Warehouse is a major component of Gemini Enterprise Agent Platform Vision. It serves as the storage repository and provides advanced search capabilities for multiple data types and use cases. Specifically:

  * **Streaming video** : You can import live video streams and live video analytics data using the Gemini Enterprise Agent Platform Vision platform application or Vision Warehouse API, and search for images using the Vision Warehouse API or Google Cloud console.
  * **Image** : You can import image and metadata using Vision Warehouse API, analyze images using Vision Warehouse API, and search for images using the Vision Warehouse API or Google Cloud console.
  * **Batch video** : You can import batch video and metadata using the Vision Warehouse API, analyze batch video using Vision Warehouse API, and search for batch videos using the Vision Warehouse API or Google Cloud console.



## API resources overview

![API resource hierarchy diagram for Vision Warehouse.](https://docs.cloud.google.com/static/vision-ai/docs/images/vision-warehouse-resources.png)

### Storage API resources

**Corpus** : A container that holds media assets of a particular type. You can create multiple corpora to organize different types of media assets.

**Asset** : A media object stored within a corpus. Assets can be images, batch videos, or video streams. A corpus typically contains many assets of the same type. You can specify annotations associated with assets. Assets can also be grouped into collections for management.

**Collection** : A resource within a corpus that serves as a container of references to assets.

**Annotation** : User-supplied metadata or data derived from Gemini Enterprise Agent Platform Vision that is associated with an asset. An asset can have multiple annotations.

  * Example 1: Specify a text annotation named "video-title" for batch video assets.
  * Example 2: Store analyzed data from Gemini Enterprise Agent Platform Vision models as annotations. For example, object recognition labels in different video time frames can be stored as annotations.



**Data schema** : Defines how an annotation is interpreted within a corpus. A data schema defines one annotation type and its search strategy. Each annotation must be associated with a data schema.

### Search API resources

**Index** (available to image and batch video verticals): A corpus-level resource that is a managed representation of analyzed assets and annotations. An index can be viewed as a dataset of embedding vectors and semantic restrictions that represents the meaning of the media content. Indexes can be deployed into index endpoints for search.

**Index endpoint** (available to image and batch video verticals): A managed environment that serves Vision Warehouse indexes. Index endpoints provide a single point of access for sending search requests.

**Important:** `Index` and `IndexEndpoint` are not available in Streaming Warehouse. Users must use the [`projects.locations.corpora.searchAssets`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora/searchAssets) method to search in Streaming Warehouse.

**Search Configuration** : Stores various properties that affect search behaviors and search results.

  * Facet property (available to streaming video vertical): Creates a configuration to enable facet-based histogram search results.
  * Search criteria property (available to streaming video and batch video verticals): Creates a mapping between a custom search criteria and one or more data schema keys.



**Search Hypernym** : A specific type of search config that lets you customize the search service's ability to recognize hypernyms of words. For example, users can specify "animal" as a hypernym of "cat" and "dog". Searching for "animal" will also return results with "cat" and "dog" in the index data.

### Supported languages

Batch Video Warehouse and Image Warehouse support the following languages for semantic search:

  * English
  * Spanish
  * Portuguese
  * French
  * Japanese
  * Chinese



Streaming Warehouse does not have language restrictions.

## What's next

  * Understand the key API user flows for each media vertical: [streaming video](https://docs.cloud.google.com/vision-ai/docs/create-manage-streaming-warehouse), [image](https://docs.cloud.google.com/vision-ai/docs/image-warehouse-overview), and [batch video](https://docs.cloud.google.com/vision-ai/docs/batch-video-warehouse-overview).
  * Explore Vision Warehouse [Quotas](https://docs.cloud.google.com/vision-ai/quotas#warehouse-quotas) and [Limits](https://docs.cloud.google.com/vision-ai/quotas#warehouse-limits).
  * Get familiar with [Pricing](https://docs.cloud.google.com/vision-ai/pricing).
  * Discover how to obtain [support](https://docs.cloud.google.com/vision-ai/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
