---
url: https://docs.cloud.google.com/document-ai/quotas/
title: Quotas \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:00.862607+00:00
---

# Quotas  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Resources ](https://docs.cloud.google.com/document-ai/docs/resources)



Send feedback 

#  Quotas Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Document AI.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

To increase available capacity for your projects, read about [capacity reservation requests](https://docs.cloud.google.com/document-ai/capacity-reservation).

## Online service tiers

Document AI supports two service tiers and associated quotas for online process requests to Generative AI-powered processor versions: provisioned and best effort tiers.

Provisioned tier quota provides 120 pages per minute for base processor versions, such as custom extractor v1.4 and v1.5, and 30 pages per minute for base processor versions like custom extractor v1.5 Pro.

Best effort tier quota provides 120 for base processor versions like custom extractor v1.4 and v1.5, 60 for Pro processor versions such as custom extractor v1.5 Pro, and is only used once the provisioned quota has been exhausted. This applies to quotas `BestEffortOnlineProcessDocumentPagesPerMinutePerProjectUS` (metric `best_effort_online_process_document_pages_us`), and `BestEffortOnlineProcessDocumentPagesPerMinutePerProjectEU` (metric `best_effort_online_process_document_pages_eu`) in the console.

Notes | Processors based on Gemini 2.0 Flash | Processors based on Gemini 2.5 Flash | Processors based on Gemini 2.5 Pro  
---|---|---|---  
Processors such as: | Custom extractor v1.4 | Custom extractor v1.5 | All Pro versions like Custom extractor v1.5 Pro and v1.6 Pro  
Provisioned | 120 | 120 | 30  
Best effort | 120 | 120 | 60  
Best effort with a quota increase request | 240 | 240 | 120  
Organization-level provisioned | 240 | 240 | 60  
Reserved capacity, purchased | Available | Available | Not available  
**Note:** The organization-level provisioned quotas for custom extractor v1.4 and v1.5 apply to `ProcessorOnlineRequestsPerMinutePerProjectUS` and `ProcessorOnlineRequestsPerMinutePerProjectEU`.

If you need more than the best effort quotas have listed, you can make a quota increase request (QIR) by [contacting the Sales team](https://cloud.google.com/contact/).

To secure more available capacity during high volume traffic, read the section on how to [make a capacity reservation request](https://docs.cloud.google.com/document-ai/quotas#capacity-reservation).

There is no [service level agreement](https://cloud.google.com//document-ai/sla) for best effort tier.

## Quotas list

The following quotas apply to Document AI. These quotas apply to each Google Cloud console project and are shared across all applications and IP addresses using that project.

If you would like to process more requests, submit a Document AI quota request for your project in the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas).

Provide information about your specific needs and use case in the request.

Base requests per minute (RPM) | Default Value | Notes  
---|---|---  
Requests per minute | 1,800 per user1 |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/default_requests)  
**Provisioned sync generic RPM**  
Online process requests per minute (US) | 120 per project per processor type |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/processor_online_process_document_requests_us)  
Online process requests per minute (EU) | 120 per project per processor type |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/processor_online_process_document_requests_eu)  
Online process requests per minute (single region) | 6 per project per processor type |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/processor_online_process_document_requests_regional)  
**Generative AI sync PPM**  
Number of online process document pages (US) per minute per processor type and model version (Custom Extractor v1.4 with Gemini 2.0 Flash only) | 120 pages per minute2 |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/online_process_document_pages_us)  
Number of online process document pages (EU) per minute per processor type and model version (Custom Extractor v1.4 with Gemini 2.0 Flash only) | 120 pages per minute2 |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/online_process_document_pages_eu)  
Number of online process document pages (US) per minute per processor type and model version (Custom Extractor v1.5 with Gemini 2.5 Flash only) | 120 pages per minute2 |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/online_process_document_pages_us)  
Number of online process document pages (EU) per minute per processor type and model version (Custom Extractor v1.5 with Gemini 2.5 Flash only) | 120 pages per minute2 |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/online_process_document_pages_eu)  
**Best effort sync PPM**  
Number of online best effort process document pages (US) per minute per processor type and model version | 120 pages per minute4 |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/best_effort_online_process_document_pages_us)  
Number of online best effort process document pages (EU) per minute per processor type and model version | 120 pages per minute4 |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/best_effort_online_process_document_pages_eu)  
Number of online best effort process document pages (single region) per minute per processor type and model version | 120 pages per minute4 |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/best_effort_online_process_document_pages_regional)  
**Concurrent batches**  
Concurrent batch process requests per project and region (US) | 5 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/processor_concurrent_batch_process_document_requests_us)  
Concurrent batch process requests per project and region (EU) | 5 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/processor_concurrent_batch_process_document_requests_eu)  
Concurrent batch process requests per processor (single region) | 5 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/processor_concurrent_batch_process_document_requests_regional)  
**Concurrent training**  
Concurrent processor version training requests (US) | 1 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/concurrent_train_processor_version_requests_us)  
Concurrent processor version training requests (EU) | 1 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/concurrent_train_processor_version_requests_eu)  
Concurrent processor version training requests (single region) | 1 per project3 |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/concurrent_train_processor_version_single_region_requests)  
**Deployed processors**  
Deployed custom processor versions (US) | 5 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/deployed_custom_processor_versions_us)  
Deployed custom processor versions (EU) | 5 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/deployed_custom_processor_versions_eu)  
Deployed custom processor versions (single region) | 5 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/deployed_custom_processor_versions_regional)  
**Deployed generative AI processors**  
Deployed generative processor versions (US) | 100 per project per custom extraction processor |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/deployed_generative_processor_versions_us)  
Deployed generative processor versions (EU) | 100 per project per custom extraction processor |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/deployed_generative_processor_versions_eu)  
Deployed generative processor versions (single region) | 100 per project per custom extraction processor |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/deployed_generative_processor_versions_regional)  
**Concurrent import**  
Concurrent import documents requests (US) | 3 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/concurrent_import_documents_requests_us)  
Concurrent import documents requests (EU) | 3 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/concurrent_import_documents_requests_eu)  
Concurrent import documents requests (single region) | 3 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/concurrent_import_documents_requests_regional)  
**Concurrent export**  
Concurrent export documents requests (US) | 1 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/concurrent_export_documents_requests_us)  
Concurrent export documents requests (EU) | 1 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/concurrent_export_documents_requests_eu)  
Concurrent export documents requests (single region) | 1 per project |  [ View quota in Google Cloud console ](https://console.cloud.google.com/iam-admin/quotas?service=documentai.googleapis.com&metric=documentai.googleapis.com/concurrent_export_documents_requests_regional)  
  
  1. The request per minute quota batch is for the number of documents being requested per minute, not the number of pages or `batchProcess` API calls.
  2. Quota adjustment requests are not yet supported for this version.
  3. Supported in `australia-southeast1` with a quota adjustment request.
  4. Varies depending on Gemini version, see [service tiers](https://docs.cloud.google.com/document-ai/quotas#service_tiers). Review [how to make a capacity reservation request](https://docs.cloud.google.com/document-ai/capacity-reservation).



If your project requires more capacity, read about [Capacity reservation](https://docs.cloud.google.com/document-ai/capacity-reservation).

[ Previous arrow_back  Service Level Agreement  ](https://cloud.google.com/document-ai/sla)

[ Next Limits  arrow_forward  ](https://docs.cloud.google.com/document-ai/limits)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
