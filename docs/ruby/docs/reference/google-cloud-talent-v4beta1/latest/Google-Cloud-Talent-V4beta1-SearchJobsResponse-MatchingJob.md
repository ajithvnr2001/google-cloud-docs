---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-SearchJobsResponse-MatchingJob/
title: Cloud Talent Solution V4beta1 API - Class Google::Cloud::Talent::V4beta1::SearchJobsResponse::MatchingJob (v0.19.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:16.362604+00:00
---

# Cloud Talent Solution V4beta1 API - Class Google::Cloud::Talent::V4beta1::SearchJobsResponse::MatchingJob (v0.19.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-SearchJobsResponse-MatchingJob/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Talent Solution V4beta1 API - Class Google::Cloud::Talent::V4beta1::SearchJobsResponse::MatchingJob (v0.19.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.1 (latest)  0.19.0  0.18.1  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.0  0.4.6 

Reference documentation and code samples for the Cloud Talent Solution V4beta1 API class Google::Cloud::Talent::V4beta1::SearchJobsResponse::MatchingJob.

Job entry with metadata inside [SearchJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-SearchJobsResponse "Google::Cloud::Talent::V4beta1::SearchJobsResponse \(class\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #commute_info
    
    
    def commute_info() -> ::Google::Cloud::Talent::V4beta1::SearchJobsResponse::CommuteInfo

**Returns**

  * ([::Google::Cloud::Talent::V4beta1::SearchJobsResponse::CommuteInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-SearchJobsResponse-CommuteInfo)) — Commute information which is generated based on specified [CommuteFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CommuteFilter "Google::Cloud::Talent::V4beta1::CommuteFilter \(class\)"). 



### #commute_info=
    
    
    def commute_info=(value) -> ::Google::Cloud::Talent::V4beta1::SearchJobsResponse::CommuteInfo

**Parameter**

  * **value** ([::Google::Cloud::Talent::V4beta1::SearchJobsResponse::CommuteInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-SearchJobsResponse-CommuteInfo)) — Commute information which is generated based on specified [CommuteFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CommuteFilter "Google::Cloud::Talent::V4beta1::CommuteFilter \(class\)"). 



**Returns**

  * ([::Google::Cloud::Talent::V4beta1::SearchJobsResponse::CommuteInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-SearchJobsResponse-CommuteInfo)) — Commute information which is generated based on specified [CommuteFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-CommuteFilter "Google::Cloud::Talent::V4beta1::CommuteFilter \(class\)"). 



### #job
    
    
    def job() -> ::Google::Cloud::Talent::V4beta1::Job

**Returns**

  * ([::Google::Cloud::Talent::V4beta1::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job)) — Job resource that matches the specified [SearchJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-SearchJobsRequest "Google::Cloud::Talent::V4beta1::SearchJobsRequest \(class\)"). 



### #job=
    
    
    def job=(value) -> ::Google::Cloud::Talent::V4beta1::Job

**Parameter**

  * **value** ([::Google::Cloud::Talent::V4beta1::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job)) — Job resource that matches the specified [SearchJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-SearchJobsRequest "Google::Cloud::Talent::V4beta1::SearchJobsRequest \(class\)"). 



**Returns**

  * ([::Google::Cloud::Talent::V4beta1::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job)) — Job resource that matches the specified [SearchJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-SearchJobsRequest "Google::Cloud::Talent::V4beta1::SearchJobsRequest \(class\)"). 



### #job_summary
    
    
    def job_summary() -> ::String

**Returns**

  * (::String) — A summary of the job with core information that's displayed on the search results listing page. 



### #job_summary=
    
    
    def job_summary=(value) -> ::String

**Parameter**

  * **value** (::String) — A summary of the job with core information that's displayed on the search results listing page. 



**Returns**

  * (::String) — A summary of the job with core information that's displayed on the search results listing page. 



### #job_title_snippet
    
    
    def job_title_snippet() -> ::String

**Returns**

  * (::String) — Contains snippets of text from the [Job.title](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_title_instance_ "Google::Cloud::Talent::V4beta1::Job#title \(method\)") field most closely matching a search query's keywords, if available. The matching query keywords are enclosed in HTML bold tags. 



### #job_title_snippet=
    
    
    def job_title_snippet=(value) -> ::String

**Parameter**

  * **value** (::String) — Contains snippets of text from the [Job.title](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_title_instance_ "Google::Cloud::Talent::V4beta1::Job#title \(method\)") field most closely matching a search query's keywords, if available. The matching query keywords are enclosed in HTML bold tags. 



**Returns**

  * (::String) — Contains snippets of text from the [Job.title](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_title_instance_ "Google::Cloud::Talent::V4beta1::Job#title \(method\)") field most closely matching a search query's keywords, if available. The matching query keywords are enclosed in HTML bold tags. 



### #search_text_snippet
    
    
    def search_text_snippet() -> ::String

**Returns**

  * (::String) — Contains snippets of text from the [Job.description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_description_instance_ "Google::Cloud::Talent::V4beta1::Job#description \(method\)") and similar fields that most closely match a search query's keywords, if available. All HTML tags in the original fields are stripped when returned in this field, and matching query keywords are enclosed in HTML bold tags. 



### #search_text_snippet=
    
    
    def search_text_snippet=(value) -> ::String

**Parameter**

  * **value** (::String) — Contains snippets of text from the [Job.description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_description_instance_ "Google::Cloud::Talent::V4beta1::Job#description \(method\)") and similar fields that most closely match a search query's keywords, if available. All HTML tags in the original fields are stripped when returned in this field, and matching query keywords are enclosed in HTML bold tags. 



**Returns**

  * (::String) — Contains snippets of text from the [Job.description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4beta1/latest/Google-Cloud-Talent-V4beta1-Job#Google__Cloud__Talent__V4beta1__Job_description_instance_ "Google::Cloud::Talent::V4beta1::Job#description \(method\)") and similar fields that most closely match a search query's keywords, if available. All HTML tags in the original fields are stripped when returned in this field, and matching query keywords are enclosed in HTML bold tags. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
