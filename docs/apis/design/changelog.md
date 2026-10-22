---
url: https://docs.cloud.google.com/apis/design/changelog/
title: Changelog \u00a0|\u00a0 Cloud API Design Guide \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:18.977244+00:00
---

# Changelog  |  Cloud API Design Guide  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/design/changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Cloud API Design Guide ](https://docs.cloud.google.com/apis/design)



Send feedback 

#  Changelog Stay organized with collections  Save and categorize content based on your preferences. 

This changelog highlights notable historical changes to the [API Design Guide](https://docs.cloud.google.com/apis/design), such as revisions to naming conventions, error handling, and standard fields. It also logs the documentation migrations to Google API Improvement Proposals (AIPs).

## 2025-06

  * Redirected Design page Naming Convention to Google AIP.



## 2024-10

  * Redirected Design pages to Google AIPs, except for Directory Structure and Naming Conventions.



## 2021-12

  * Changed terminology Networked API to Network API for consistency with https://google.aip.dev/9.



## 2021-09

  * Document both Google API error format v1 and v2.



## 2021-04

  * Introduced visibility-based versioning.

  * Introduced API title to glossary.




## 2021-03

  * Added annotation for output only fields.

  * Update enum value guidance to always include an explicit `_UNSPECIFIED` value.

  * Add guidance on how to generate and parse resource names.

  * Add `progress_percent` to standard fields.




## 2021-02

  * Added guidance on proto3 `optional` primitive fields.



## 2021-01

  * Updated the Errors page to cover the latest improvement related to `google.rpc.ErrorInfo` and `google.api.ErrorReason`.

  * Added guidance on how to use `oauth2l`, `curl`, and System Parameters to troubleshoot errors with Google APIs.

  * Added `502` error code explanation to the Errors page. It is a network error instead of an API error.




## 2020-12

  * Package names should use singlar component names for global consistency. Package names must not use underscores.



## 2020-09

  * Cleaned up some field description requirements; changed some uses of "must" outside RFC 2119 to be RFC 2119 "should" directives.

  * Removed the `bool deleted` standard field, in favor of `google.protobuf.Timestamp delete_time` (which was already listed).




## 2020-07

  * Updated documentation.md to match https://google.aip.dev/192#formatting. Markdown tables and raw HTML must not be used in proto comments.

  * Added `ErrorInfo` for error handling.

  * Added Large Payloads for design patterns.




## 2020-04

  * Renamed Cloud APIs to Google Cloud APIs in glossary.
  * Introduced API and service as synonyms of API service.



## 2020-02

  * Updated versioning to add two versioning strategies (channel-based and release-based), remove guidance on point versions, and change how we refer to semantic versioning.



## 2020-01

  * Add data retention to design patterns.



## 2019-11

  * Add terminology Cloud APIs to glossary.
  * Recommend clients to retry only for UNAVAILABLE errors.



## 2019-06

  * Add "Bool vs Enum vs String" to design patterns.



## 2019-03

  * Add system parameters to standard fields.



## 2019-02

  * Add domain-scoped names to design patterns.



## 2018-03

  * Add streaming half-close semantics to design patterns.



## 2018-02

  * Add `read_time` to Standard Fields.



## 2018-01

  * Add schema reference for API Service Definition.



## 2017-12

  * Clarify API major version must be the last component of proto package name.



## 2017-11

  * Clarify why the `Create` method take an input resource.
  * Clarify collection IDs that don't have plural form, such as evidence and weather.
  * Add singleton resource to design patterns.
  * Clarify C# naming conventions for acronyms and versions.



## 2017-09

  * Add `mime_type` to standard fields.
  * Add `expire_time` to standard fields.
  * Add `start_time` and `end_time` to standard fields.



## 2017-02

  * Add "API endpoint" to glossary.
  * Add `update_mask` to standard fields.
  * Add a link to `FieldMask` to standard methods.
  * Mention that OpenAPI spec does not support unsigned integers.
  * Clarify that method names should use verbs in the imperative mood.



[ Previous arrow_back  Directory structure  ](https://docs.cloud.google.com/apis/design/directory_structure)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
