---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckConfig-ContentMatcher/
title: Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:07.147503+00:00
---

# Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckConfig-ContentMatcher/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.18.0  0.17.0  0.16.0  0.15.2  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Monitoring V3 API class Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher.

Optional. Used to perform content matching. This allows matching based on substrings and regular expressions, together with their negations. Only the first 4 MB of an HTTP or HTTPS check's response (and the first 1 MB of a TCP check's response) are examined for purposes of content matching.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #content
    
    
    def content() -> ::String

**Returns**

  * (::String) — String, regex or JSON content to match. Maximum 1024 bytes. An empty `content` string indicates no content matching is to be performed. 



### #content=
    
    
    def content=(value) -> ::String

**Parameter**

  * **value** (::String) — String, regex or JSON content to match. Maximum 1024 bytes. An empty `content` string indicates no content matching is to be performed. 



**Returns**

  * (::String) — String, regex or JSON content to match. Maximum 1024 bytes. An empty `content` string indicates no content matching is to be performed. 



### #json_path_matcher
    
    
    def json_path_matcher() -> ::Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher::JsonPathMatcher

**Returns**

  * ([::Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher::JsonPathMatcher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckConfig-ContentMatcher-JsonPathMatcher)) — Matcher information for `MATCHES_JSON_PATH` and `NOT_MATCHES_JSON_PATH`



### #json_path_matcher=
    
    
    def json_path_matcher=(value) -> ::Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher::JsonPathMatcher

**Parameter**

  * **value** ([::Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher::JsonPathMatcher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckConfig-ContentMatcher-JsonPathMatcher)) — Matcher information for `MATCHES_JSON_PATH` and `NOT_MATCHES_JSON_PATH`



**Returns**

  * ([::Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher::JsonPathMatcher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckConfig-ContentMatcher-JsonPathMatcher)) — Matcher information for `MATCHES_JSON_PATH` and `NOT_MATCHES_JSON_PATH`



### #matcher
    
    
    def matcher() -> ::Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher::ContentMatcherOption

**Returns**

  * ([::Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher::ContentMatcherOption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckConfig-ContentMatcher-ContentMatcherOption)) — The type of content matcher that will be applied to the server output, compared to the `content` string when the check is run. 



### #matcher=
    
    
    def matcher=(value) -> ::Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher::ContentMatcherOption

**Parameter**

  * **value** ([::Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher::ContentMatcherOption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckConfig-ContentMatcher-ContentMatcherOption)) — The type of content matcher that will be applied to the server output, compared to the `content` string when the check is run. 



**Returns**

  * ([::Google::Cloud::Monitoring::V3::UptimeCheckConfig::ContentMatcher::ContentMatcherOption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckConfig-ContentMatcher-ContentMatcherOption)) — The type of content matcher that will be applied to the server output, compared to the `content` string when the check is run. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
