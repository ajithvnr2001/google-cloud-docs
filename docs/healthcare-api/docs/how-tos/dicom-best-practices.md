---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-best-practices/
title: DICOM best practices \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:54.049720+00:00
---

# DICOM best practices  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  DICOM best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page shows best practices for improving performance when working with DICOM data in the Cloud Healthcare API.

## Maximizing frames per second (FPS) in an imaging viewer

The [healthcare-imaging-performance-test](https://github.com/GoogleCloudPlatform/healthcare-imaging-performance-test) tool provides benchmarks that let you preview what FPS you can expect for a DICOM medical imaging viewer that pulls data from the Cloud Healthcare API.

### Sending requests concurrently

For the best FPS performance, send requests concurrently. For example, under the following conditions you can improve FPS from 30 FPS to 60 FPS when going from six concurrent requests to 20:

  * Using no compression
  * When the DICOM data is all in the same region
  * When the DICOM images are 0.5 MB in size



### Retrieving frames in a single request

The [`retrieveStudy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies/retrieveStudy) and [`retrieveSeries`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series/retrieveSeries) methods efficiently return multiple DICOM files in a single request. Using these methods, you can retrieve images at the same rate as using an optimal number of concurrent requests. You can call these methods in a single request instead of using concurrent requests if the following are true:

  * The client can store the entire study in memory, or the client can parse the response as a stream to handle one DICOM instance at a time
  * You don't need to customize the order of the retrieved images



## Improving performance for web viewers

The following sections apply to retrieving DICOM images when using a web viewer.

### Increasing maximum concurrent requests

When using a web-based viewer, most browsers enforce a maximum number of connections per host. This number is typically six. However, in practice there is no restriction on the maximum number of concurrent requests because:

  * Most browsers use HTTP/2 by default if the server supports HTTP/2
  * HTTP/2 uses a single connection for all requests



For example, if you use [Cornerstone.js](https://github.com/cornerstonejs/cornerstone) to build a viewer, you can modify the maximum number of concurrent requests to a number that is optimal for your viewer by changing [`maxSimultaneousRequests`](https://github.com/cornerstonejs/cornerstoneTools/blob/cefbb34e4a651ae49c0b066e36f6ccf0cb6ea89f/src/util/getMaxSimultaneousRequests.js#L5) when configuring Cornerstone.js.

### Using web workers

JavaScript is a single-threaded language, so extra care must be taken when applying concurrency patterns. You can use [web workers](https://en.wikipedia.org/wiki/Web_worker) to process both DICOM images and HTTP requests.

For example, if you modify your HTTP request processing to web workers, you can effectively double your viewer's FPS from 30 FPS to 60 FPS assuming a 30 millisecond request processing overhead.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
