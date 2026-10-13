---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SummarizationEvaluationMetrics/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:23.922703+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SummarizationEvaluationMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics.

Evaluation metrics for summarization generator.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #conversation_details
    
    
    def conversation_details() -> ::Array<::Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics::ConversationDetail>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics::ConversationDetail](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SummarizationEvaluationMetrics-ConversationDetail)>) — Output only. List of conversation details. 



### #overall_metrics
    
    
    def overall_metrics() -> ::Array<::Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics::OverallScoresByMetric>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics::OverallScoresByMetric](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SummarizationEvaluationMetrics-OverallScoresByMetric)>) — Output only. A list of aggregated(average) scores per metric section. 



### #overall_section_tokens
    
    
    def overall_section_tokens() -> ::Array<::Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics::SectionToken>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics::SectionToken](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SummarizationEvaluationMetrics-SectionToken)>) — Output only. Overall token per section. This is an aggregated(sum) result of input token of summary acorss all conversations that are selected for summarization evaluation. 



### #summarization_evaluation_merged_results_uri
    
    
    def summarization_evaluation_merged_results_uri() -> ::String

**Returns**

  * (::String) — Output only. User bucket uri for merged evaluation score and aggregation score csv. 



### #summarization_evaluation_results
    
    
    def summarization_evaluation_results() -> ::Array<::Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics::SummarizationEvaluationResult>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::V2::SummarizationEvaluationMetrics::SummarizationEvaluationResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SummarizationEvaluationMetrics-SummarizationEvaluationResult)>) — Output only. A list of evaluation results per conversation(&summary), metric and section. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
