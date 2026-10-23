---
url: https://docs.cloud.google.com/storage-transfer/docs/source-url-list/
title: Configure access to a source: URL list \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:38.777735+00:00
---

# Configure access to a source: URL list  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/source-url-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Configure access to a source: URL list Stay organized with collections  Save and categorize content based on your preferences. 

To transfer data using a [URL list](https://docs.cloud.google.com/storage-transfer/docs/create-url-list), ensure that the following requirements are met:

  * The URL list is publicly accessible from a URL beginning with either `http` or `https`.

  * Each URL you specify is publicly accessible.

For example, in Cloud Storage, you can [share an object publicly](https://docs.cloud.google.com/storage/docs/cloud-console#_sharingdata) and get a link to it.

  * The server's `robots.txt` file allows access to each URL.

  * The server hosting each object supports `Range` requests and returns a `Content-Length` header in each response.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
