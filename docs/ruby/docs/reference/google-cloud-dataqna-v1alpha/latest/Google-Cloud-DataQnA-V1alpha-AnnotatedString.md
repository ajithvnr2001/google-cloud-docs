---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-AnnotatedString/
title: BigQuery Data QnA V1alpha API - Class Google::Cloud::DataQnA::V1alpha::AnnotatedString (v0.13.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:35.132843+00:00
---

# BigQuery Data QnA V1alpha API - Class Google::Cloud::DataQnA::V1alpha::AnnotatedString (v0.13.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-AnnotatedString/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Data QnA V1alpha API - Class Google::Cloud::DataQnA::V1alpha::AnnotatedString (v0.13.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.2 (latest)  0.13.1  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.2  0.6.2  0.5.0  0.4.0  0.3.0  0.2.6 

Reference documentation and code samples for the BigQuery Data QnA V1alpha API class Google::Cloud::DataQnA::V1alpha::AnnotatedString.

Describes string annotation from both semantic and formatting perspectives. Example:

User Query:

top countries by population in Africa

0 4 14 17 28 31 37

Table Data:

  * "country" - dimension
  * "population" - metric
  * "Africa" - value in the "continent" column



text_formatted = `"top countries by population in Africa"`

html_formatted = `"top <b>countries</b> by <b>population</b> in <i>Africa</i>"`

` markups = [ \{DIMENSION, 4, 12}, // 'countries' \{METRIC, 17, 26}, // 'population' \{FILTER, 31, 36} // 'Africa' ] `

Note that html formattings for 'DIMENSION' and 'METRIC' are the same, while semantic markups are different.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #html_formatted
    
    
    def html_formatted() -> ::String

**Returns**

  * (::String) — HTML version of the string annotation. 



### #html_formatted=
    
    
    def html_formatted=(value) -> ::String

**Parameter**

  * **value** (::String) — HTML version of the string annotation. 



**Returns**

  * (::String) — HTML version of the string annotation. 



### #markups
    
    
    def markups() -> ::Array<::Google::Cloud::DataQnA::V1alpha::AnnotatedString::SemanticMarkup>

**Returns**

  * (::Array<[::Google::Cloud::DataQnA::V1alpha::AnnotatedString::SemanticMarkup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-AnnotatedString-SemanticMarkup)>) — Semantic version of the string annotation. 



### #markups=
    
    
    def markups=(value) -> ::Array<::Google::Cloud::DataQnA::V1alpha::AnnotatedString::SemanticMarkup>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DataQnA::V1alpha::AnnotatedString::SemanticMarkup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-AnnotatedString-SemanticMarkup)>) — Semantic version of the string annotation. 



**Returns**

  * (::Array<[::Google::Cloud::DataQnA::V1alpha::AnnotatedString::SemanticMarkup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Cloud-DataQnA-V1alpha-AnnotatedString-SemanticMarkup)>) — Semantic version of the string annotation. 



### #text_formatted
    
    
    def text_formatted() -> ::String

**Returns**

  * (::String) — Text version of the string. 



### #text_formatted=
    
    
    def text_formatted=(value) -> ::String

**Parameter**

  * **value** (::String) — Text version of the string. 



**Returns**

  * (::String) — Text version of the string. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
