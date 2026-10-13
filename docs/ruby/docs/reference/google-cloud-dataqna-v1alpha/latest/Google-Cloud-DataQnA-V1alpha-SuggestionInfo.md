---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-SuggestionInfo/
title: BigQuery Data QnA V1alpha API - Class Google::Cloud::DataQnA::V1alpha::SuggestionInfo (v0.13.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:52.700409+00:00
---

# BigQuery Data QnA V1alpha API - Class Google::Cloud::DataQnA::V1alpha::SuggestionInfo (v0.13.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-SuggestionInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Data QnA V1alpha API - Class Google::Cloud::DataQnA::V1alpha::SuggestionInfo (v0.13.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.2 (latest)  0.13.1  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.2  0.6.2  0.5.0  0.4.0  0.3.0  0.2.6 

Reference documentation and code samples for the BigQuery Data QnA V1alpha API class Google::Cloud::DataQnA::V1alpha::SuggestionInfo.

Detailed information about the suggestion.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #annotated_suggestion
    
    
    def annotated_suggestion() -> ::Google::Cloud::DataQnA::V1alpha::AnnotatedString

**Returns**

  * ([::Google::Cloud::DataQnA::V1alpha::AnnotatedString](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-AnnotatedString)) — Annotations for the suggestion. This provides information about which part of the suggestion corresponds to what semantic meaning (e.g. a metric). 



### #annotated_suggestion=
    
    
    def annotated_suggestion=(value) -> ::Google::Cloud::DataQnA::V1alpha::AnnotatedString

**Parameter**

  * **value** ([::Google::Cloud::DataQnA::V1alpha::AnnotatedString](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-AnnotatedString)) — Annotations for the suggestion. This provides information about which part of the suggestion corresponds to what semantic meaning (e.g. a metric). 



**Returns**

  * ([::Google::Cloud::DataQnA::V1alpha::AnnotatedString](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-AnnotatedString)) — Annotations for the suggestion. This provides information about which part of the suggestion corresponds to what semantic meaning (e.g. a metric). 



### #query_matches
    
    
    def query_matches() -> ::Array<::Google::Cloud::DataQnA::V1alpha::SuggestionInfo::MatchInfo>

**Returns**

  * (::Array<[::Google::Cloud::DataQnA::V1alpha::SuggestionInfo::MatchInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-SuggestionInfo-MatchInfo)>) — Matches between user query and the annotated string. 



### #query_matches=
    
    
    def query_matches=(value) -> ::Array<::Google::Cloud::DataQnA::V1alpha::SuggestionInfo::MatchInfo>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DataQnA::V1alpha::SuggestionInfo::MatchInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-SuggestionInfo-MatchInfo)>) — Matches between user query and the annotated string. 



**Returns**

  * (::Array<[::Google::Cloud::DataQnA::V1alpha::SuggestionInfo::MatchInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-SuggestionInfo-MatchInfo)>) — Matches between user query and the annotated string. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
