---
url: https://docs.cloud.google.com/vision-ai/docs/image-warehouse-overview/
title: Image Warehouse overview \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:54.822637+00:00
---

# Image Warehouse overview  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/image-warehouse-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Image Warehouse overview Stay organized with collections  Save and categorize content based on your preferences. 

The Image Warehouse API is a powerful tool for storing, managing, and searching images. With Image Warehouse, you can:

  * Store images in a secure and scalable manner.
  * Manage annotations on images.
  * Build indexes from images and annotations for similarity matching.
  * Perform image similarity search with image or text query.
  * Search images with criteria on annotations.



The Image Warehouse API is powered by a Google AI multimodal embedding model that turns images (and text query) into a numerical feature space representation. This allows the API to achieve state-of-the-art results in image similarity search.

## Image Warehouse journey

Start onboarding with this demo [colab](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/vision/image_warehouse_sdk.ipynb)

  1. Create a corpus of image type.
  2. Optionally create data schema if managing annotations is needed.
  3. Import image assets and optionally annotations into the corpus. We will make copy of the images to store in warehouse. The corresponding storage [Pricing](https://docs.cloud.google.com/vision-ai/pricing).
  4. Perform AnalyzeCorpus to generate embedding signals from the images.
  5. Create index from corpus.
  6. Create index endpoint and deploy index to this index endpoint.
  7. Perform search with either image or text query on this index endpoint. The Search will match against all the data contained in the deployed Index on this index endpoint.
  8. Optional: Specify criteria in the search query, which will be used to match against the annotations in the index data. Only exact match is support in criteria matching.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
