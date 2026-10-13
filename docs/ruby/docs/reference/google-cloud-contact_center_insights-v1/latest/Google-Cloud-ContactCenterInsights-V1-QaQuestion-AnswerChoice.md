---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-contact_center_insights-v1/latest/Google-Cloud-ContactCenterInsights-V1-QaQuestion-AnswerChoice/
title: Contact Center AI Insights V1 API - Class Google::Cloud::ContactCenterInsights::V1::QaQuestion::AnswerChoice (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:54.993186+00:00
---

# Contact Center AI Insights V1 API - Class Google::Cloud::ContactCenterInsights::V1::QaQuestion::AnswerChoice (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-contact_center_insights-v1/latest/Google-Cloud-ContactCenterInsights-V1-QaQuestion-AnswerChoice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Contact Center AI Insights V1 API - Class Google::Cloud::ContactCenterInsights::V1::QaQuestion::AnswerChoice (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.22.0  0.21.1  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.2  0.7.2  0.6.0 

Reference documentation and code samples for the Contact Center AI Insights V1 API class Google::Cloud::ContactCenterInsights::V1::QaQuestion::AnswerChoice.

Message representing a possible answer to the question.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bool_value
    
    
    def bool_value() -> ::Boolean

**Returns**

  * (::Boolean) — Boolean value.

Note: The following fields are mutually exclusive: `bool_value`, `str_value`, `num_value`, `na_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bool_value=
    
    
    def bool_value=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Boolean value.

Note: The following fields are mutually exclusive: `bool_value`, `str_value`, `num_value`, `na_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Boolean) — Boolean value.

Note: The following fields are mutually exclusive: `bool_value`, `str_value`, `num_value`, `na_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #key
    
    
    def key() -> ::String

**Returns**

  * (::String) — A short string used as an identifier. 



### #key=
    
    
    def key=(value) -> ::String

**Parameter**

  * **value** (::String) — A short string used as an identifier. 



**Returns**

  * (::String) — A short string used as an identifier. 



### #na_value
    
    
    def na_value() -> ::Boolean

**Returns**

  * (::Boolean) — A value of "Not Applicable (N/A)". If provided, this field may only be set to `true`. If a question receives this answer, it will be excluded from any score calculations.

Note: The following fields are mutually exclusive: `na_value`, `str_value`, `num_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #na_value=
    
    
    def na_value=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — A value of "Not Applicable (N/A)". If provided, this field may only be set to `true`. If a question receives this answer, it will be excluded from any score calculations.

Note: The following fields are mutually exclusive: `na_value`, `str_value`, `num_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Boolean) — A value of "Not Applicable (N/A)". If provided, this field may only be set to `true`. If a question receives this answer, it will be excluded from any score calculations.

Note: The following fields are mutually exclusive: `na_value`, `str_value`, `num_value`, `bool_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #num_value
    
    
    def num_value() -> ::Float

**Returns**

  * (::Float) — Numerical value.

Note: The following fields are mutually exclusive: `num_value`, `str_value`, `bool_value`, `na_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #num_value=
    
    
    def num_value=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Numerical value.

Note: The following fields are mutually exclusive: `num_value`, `str_value`, `bool_value`, `na_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Float) — Numerical value.

Note: The following fields are mutually exclusive: `num_value`, `str_value`, `bool_value`, `na_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #score
    
    
    def score() -> ::Float

**Returns**

  * (::Float) — Numerical score of the answer, used for generating the overall score of a QaScorecardResult. If the answer uses na_value, this field is unused. 



### #score=
    
    
    def score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Numerical score of the answer, used for generating the overall score of a QaScorecardResult. If the answer uses na_value, this field is unused. 



**Returns**

  * (::Float) — Numerical score of the answer, used for generating the overall score of a QaScorecardResult. If the answer uses na_value, this field is unused. 



### #str_value
    
    
    def str_value() -> ::String

**Returns**

  * (::String) — String value.

Note: The following fields are mutually exclusive: `str_value`, `num_value`, `bool_value`, `na_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #str_value=
    
    
    def str_value=(value) -> ::String

**Parameter**

  * **value** (::String) — String value.

Note: The following fields are mutually exclusive: `str_value`, `num_value`, `bool_value`, `na_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — String value.

Note: The following fields are mutually exclusive: `str_value`, `num_value`, `bool_value`, `na_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
