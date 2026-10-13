---
url: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.UptimeCheckConfig.ContentMatcher
title: Class ContentMatcher (2.32.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:35.080308+00:00
---

# Class ContentMatcher (2.32.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.UptimeCheckConfig.ContentMatcher

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ContentMatcher (2.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.32.0 (latest)  2.31.0  2.30.0  2.29.1  2.28.0  2.27.2  2.26.0  2.25.0  2.24.0  2.23.1  2.22.2  2.21.0  2.20.0  2.19.4  2.18.0  2.17.0  2.16.0  2.15.1  2.14.2  2.13.0  2.12.0  2.11.3  2.10.1  2.9.2  2.8.0  2.7.0  2.6.0  2.5.2  2.4.2  2.3.0  2.2.1  2.1.0  2.0.1  1.1.2  1.0.0  0.36.2  0.35.0  0.34.0  0.33.0  0.32.0 
    
    
    ContentMatcher(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Optional. Used to perform content matching. This allows matching based on substrings and regular expressions, together with their negations. Only the first 4 MB of an HTTP or HTTPS check's response (and the first 1 MB of a TCP check's response) are examined for purposes of content matching.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`content` |  `str`   
String, regex or JSON content to match. Maximum 1024 bytes. An empty `content` string indicates no content matching is to be performed.   
`matcher` |  `[google.cloud.monitoring_v3.types.UptimeCheckConfig.ContentMatcher.ContentMatcherOption](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.UptimeCheckConfig.ContentMatcher.ContentMatcherOption)`   
The type of content matcher that will be applied to the server output, compared to the `content` string when the check is run.   
`json_path_matcher` |  `[google.cloud.monitoring_v3.types.UptimeCheckConfig.ContentMatcher.JsonPathMatcher](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.UptimeCheckConfig.ContentMatcher.JsonPathMatcher)`   
Matcher information for `MATCHES_JSON_PATH` and `NOT_MATCHES_JSON_PATH` This field is a member of `oneof`_ `additional_matcher_info`.   
  
## Classes 

### ContentMatcherOption
    
    
    ContentMatcherOption(value)

Options to perform content matching.

### JsonPathMatcher
    
    
    JsonPathMatcher(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information needed to perform a JSONPath content match. Used for `ContentMatcherOption::MATCHES_JSON_PATH` and `ContentMatcherOption::NOT_MATCHES_JSON_PATH`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
