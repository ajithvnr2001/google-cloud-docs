---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-AggregateIssueStatsResponse/
title: Database Center V1BETA API - Class Google::Cloud::DatabaseCenter::V1beta::AggregateIssueStatsResponse (v0.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:32.870761+00:00
---

# Database Center V1BETA API - Class Google::Cloud::DatabaseCenter::V1beta::AggregateIssueStatsResponse (v0.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-AggregateIssueStatsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Database Center V1BETA API - Class Google::Cloud::DatabaseCenter::V1beta::AggregateIssueStatsResponse (v0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Database Center V1BETA API class Google::Cloud::DatabaseCenter::V1beta::AggregateIssueStatsResponse.

The response message containing one of more group of relevant health issues for database resources.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #issue_group_stats
    
    
    def issue_group_stats() -> ::Array<::Google::Cloud::DatabaseCenter::V1beta::IssueGroupStats>

**Returns**

  * (::Array<[::Google::Cloud::DatabaseCenter::V1beta::IssueGroupStats](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-IssueGroupStats)>) — List of issue group stats where each group contains stats for resources having a particular combination of relevant issues. 



### #issue_group_stats=
    
    
    def issue_group_stats=(value) -> ::Array<::Google::Cloud::DatabaseCenter::V1beta::IssueGroupStats>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DatabaseCenter::V1beta::IssueGroupStats](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-IssueGroupStats)>) — List of issue group stats where each group contains stats for resources having a particular combination of relevant issues. 



**Returns**

  * (::Array<[::Google::Cloud::DatabaseCenter::V1beta::IssueGroupStats](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-database_center-v1beta/latest/Google-Cloud-DatabaseCenter-V1beta-IssueGroupStats)>) — List of issue group stats where each group contains stats for resources having a particular combination of relevant issues. 



### #total_resource_groups_count
    
    
    def total_resource_groups_count() -> ::Integer

**Returns**

  * (::Integer) — Total count of the resource filtered in based on the user given filter. 



### #total_resource_groups_count=
    
    
    def total_resource_groups_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Total count of the resource filtered in based on the user given filter. 



**Returns**

  * (::Integer) — Total count of the resource filtered in based on the user given filter. 



### #total_resources_count
    
    
    def total_resources_count() -> ::Integer

**Returns**

  * (::Integer) — Total count of the resources filtered in based on the user given filter. 



### #total_resources_count=
    
    
    def total_resources_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Total count of the resources filtered in based on the user given filter. 



**Returns**

  * (::Integer) — Total count of the resources filtered in based on the user given filter. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Unordered list. List of unreachable regions from where data could not be retrieved. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Unordered list. List of unreachable regions from where data could not be retrieved. 



**Returns**

  * (::Array<::String>) — Unordered list. List of unreachable regions from where data could not be retrieved. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
