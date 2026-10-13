---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:35.117493+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics.

Describes the metrics produced by the evaluation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #doc_ndcg
    
    
    def doc_ndcg() -> ::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Normalized discounted cumulative gain (NDCG) per document, at various top-k cutoff levels.

NDCG measures the ranking quality, giving higher relevance to top results.

Example (top-3): Suppose [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)") with three retrieved documents (D1, D2, D3) and binary relevance judgements (1 for relevant, 0 for not relevant):

Retrieved: [D3 (0), D1 (1), D2 (1)] Ideal: [D1 (1), D2 (1), D3 (0)]

Calculate NDCG@3 for each [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"):

    * DCG@3: 0/log2(1+1) + 1/log2(2+1) + 1/log2(3+1) = 1.13
    * Ideal DCG@3: 1/log2(1+1) + 1/log2(2+1) + 0/log2(3+1) = 1.63
    * NDCG@3: 1.13/1.63 = 0.693



### #doc_ndcg=
    
    
    def doc_ndcg=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Normalized discounted cumulative gain (NDCG) per document, at various top-k cutoff levels.

NDCG measures the ranking quality, giving higher relevance to top results.

Example (top-3): Suppose [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)") with three retrieved documents (D1, D2, D3) and binary relevance judgements (1 for relevant, 0 for not relevant):

Retrieved: [D3 (0), D1 (1), D2 (1)] Ideal: [D1 (1), D2 (1), D3 (0)]

Calculate NDCG@3 for each [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"):

    * DCG@3: 0/log2(1+1) + 1/log2(2+1) + 1/log2(3+1) = 1.13
    * Ideal DCG@3: 1/log2(1+1) + 1/log2(2+1) + 0/log2(3+1) = 1.63
    * NDCG@3: 1.13/1.63 = 0.693



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Normalized discounted cumulative gain (NDCG) per document, at various top-k cutoff levels.

NDCG measures the ranking quality, giving higher relevance to top results.

Example (top-3): Suppose [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)") with three retrieved documents (D1, D2, D3) and binary relevance judgements (1 for relevant, 0 for not relevant):

Retrieved: [D3 (0), D1 (1), D2 (1)] Ideal: [D1 (1), D2 (1), D3 (0)]

Calculate NDCG@3 for each [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"):

    * DCG@3: 0/log2(1+1) + 1/log2(2+1) + 1/log2(3+1) = 1.13
    * Ideal DCG@3: 1/log2(1+1) + 1/log2(2+1) + 0/log2(3+1) = 1.63
    * NDCG@3: 1.13/1.63 = 0.693



### #doc_precision
    
    
    def doc_precision() -> ::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Precision per document, at various top-k cutoff levels.

Precision is the fraction of retrieved documents that are relevant.

Example (top-5):

    * For a single [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"), If 4 out of 5 retrieved documents in the top-5 are relevant, precision@5 = 4/5 = 0.8



### #doc_precision=
    
    
    def doc_precision=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Precision per document, at various top-k cutoff levels.

Precision is the fraction of retrieved documents that are relevant.

Example (top-5):

    * For a single [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"), If 4 out of 5 retrieved documents in the top-5 are relevant, precision@5 = 4/5 = 0.8



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Precision per document, at various top-k cutoff levels.

Precision is the fraction of retrieved documents that are relevant.

Example (top-5):

    * For a single [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"), If 4 out of 5 retrieved documents in the top-5 are relevant, precision@5 = 4/5 = 0.8



### #doc_recall
    
    
    def doc_recall() -> ::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Recall per document, at various top-k cutoff levels.

Recall is the fraction of relevant documents retrieved out of all relevant documents.

Example (top-5):

    * For a single [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"), If 3 out of 5 relevant documents are retrieved in the top-5, recall@5 = 3/5 = 0.6



### #doc_recall=
    
    
    def doc_recall=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Recall per document, at various top-k cutoff levels.

Recall is the fraction of relevant documents retrieved out of all relevant documents.

Example (top-5):

    * For a single [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"), If 3 out of 5 relevant documents are retrieved in the top-5, recall@5 = 3/5 = 0.6



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Recall per document, at various top-k cutoff levels.

Recall is the fraction of relevant documents retrieved out of all relevant documents.

Example (top-5):

    * For a single [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"), If 3 out of 5 relevant documents are retrieved in the top-5, recall@5 = 3/5 = 0.6



### #page_ndcg
    
    
    def page_ndcg() -> ::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Normalized discounted cumulative gain (NDCG) per page, at various top-k cutoff levels.

NDCG measures the ranking quality, giving higher relevance to top results.

Example (top-3): Suppose [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)") with three retrieved pages (P1, P2, P3) and binary relevance judgements (1 for relevant, 0 for not relevant):

Retrieved: [P3 (0), P1 (1), P2 (1)] Ideal: [P1 (1), P2 (1), P3 (0)]

Calculate NDCG@3 for [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"):

    * DCG@3: 0/log2(1+1) + 1/log2(2+1) + 1/log2(3+1) = 1.13
    * Ideal DCG@3: 1/log2(1+1) + 1/log2(2+1) + 0/log2(3+1) = 1.63
    * NDCG@3: 1.13/1.63 = 0.693



### #page_ndcg=
    
    
    def page_ndcg=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Normalized discounted cumulative gain (NDCG) per page, at various top-k cutoff levels.

NDCG measures the ranking quality, giving higher relevance to top results.

Example (top-3): Suppose [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)") with three retrieved pages (P1, P2, P3) and binary relevance judgements (1 for relevant, 0 for not relevant):

Retrieved: [P3 (0), P1 (1), P2 (1)] Ideal: [P1 (1), P2 (1), P3 (0)]

Calculate NDCG@3 for [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"):

    * DCG@3: 0/log2(1+1) + 1/log2(2+1) + 1/log2(3+1) = 1.13
    * Ideal DCG@3: 1/log2(1+1) + 1/log2(2+1) + 0/log2(3+1) = 1.63
    * NDCG@3: 1.13/1.63 = 0.693



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Normalized discounted cumulative gain (NDCG) per page, at various top-k cutoff levels.

NDCG measures the ranking quality, giving higher relevance to top results.

Example (top-3): Suppose [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)") with three retrieved pages (P1, P2, P3) and binary relevance judgements (1 for relevant, 0 for not relevant):

Retrieved: [P3 (0), P1 (1), P2 (1)] Ideal: [P1 (1), P2 (1), P3 (0)]

Calculate NDCG@3 for [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"):

    * DCG@3: 0/log2(1+1) + 1/log2(2+1) + 1/log2(3+1) = 1.13
    * Ideal DCG@3: 1/log2(1+1) + 1/log2(2+1) + 0/log2(3+1) = 1.63
    * NDCG@3: 1.13/1.63 = 0.693



### #page_recall
    
    
    def page_recall() -> ::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Recall per page, at various top-k cutoff levels.

Recall is the fraction of relevant pages retrieved out of all relevant pages.

Example (top-5):

    * For a single [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"), if 3 out of 5 relevant pages are retrieved in the top-5, recall@5 = 3/5 = 0.6



### #page_recall=
    
    
    def page_recall=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Recall per page, at various top-k cutoff levels.

Recall is the fraction of relevant pages retrieved out of all relevant pages.

Example (top-5):

    * For a single [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"), if 3 out of 5 relevant pages are retrieved in the top-5, recall@5 = 3/5 = 0.6



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::QualityMetrics::TopkMetrics](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-QualityMetrics-TopkMetrics)) — 

Recall per page, at various top-k cutoff levels.

Recall is the fraction of relevant pages retrieved out of all relevant pages.

Example (top-5):

    * For a single [SampleQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuery "Google::Cloud::DiscoveryEngine::V1beta::SampleQuery \(class\)"), if 3 out of 5 relevant pages are retrieved in the top-5, recall@5 = 3/5 = 0.6



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
