---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Cloud-Logging-V2-ListLogEntriesRequest/
title: Cloud Logging V2 API - Class Google::Cloud::Logging::V2::ListLogEntriesRequest (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:19.903783+00:00
---

# Cloud Logging V2 API - Class Google::Cloud::Logging::V2::ListLogEntriesRequest (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Cloud-Logging-V2-ListLogEntriesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Logging V2 API - Class Google::Cloud::Logging::V2::ListLogEntriesRequest (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.1  0.9.0  0.8.1  0.7.0  0.6.0  0.5.6 

Reference documentation and code samples for the Cloud Logging V2 API class Google::Cloud::Logging::V2::ListLogEntriesRequest.

The parameters to `ListLogEntries`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. Only log entries that match the filter are returned. An empty filter matches all log entries in the resources listed in `resource_names`. Referencing a parent resource that is not listed in `resource_names` will cause the filter to return no results. The maximum length of a filter is 20,000 characters. 



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Only log entries that match the filter are returned. An empty filter matches all log entries in the resources listed in `resource_names`. Referencing a parent resource that is not listed in `resource_names` will cause the filter to return no results. The maximum length of a filter is 20,000 characters. 



**Returns**

  * (::String) — Optional. Only log entries that match the filter are returned. An empty filter matches all log entries in the resources listed in `resource_names`. Referencing a parent resource that is not listed in `resource_names` will cause the filter to return no results. The maximum length of a filter is 20,000 characters. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. How the results should be sorted. Presently, the only permitted values are `"timestamp asc"` (default) and `"timestamp desc"`. The first option returns entries in order of increasing values of `LogEntry.timestamp` (oldest first), and the second option returns entries in order of decreasing timestamps (newest first). Entries with equal timestamps are returned in order of their `insert_id` values. 



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. How the results should be sorted. Presently, the only permitted values are `"timestamp asc"` (default) and `"timestamp desc"`. The first option returns entries in order of increasing values of `LogEntry.timestamp` (oldest first), and the second option returns entries in order of decreasing timestamps (newest first). Entries with equal timestamps are returned in order of their `insert_id` values. 



**Returns**

  * (::String) — Optional. How the results should be sorted. Presently, the only permitted values are `"timestamp asc"` (default) and `"timestamp desc"`. The first option returns entries in order of increasing values of `LogEntry.timestamp` (oldest first), and the second option returns entries in order of decreasing timestamps (newest first). Entries with equal timestamps are returned in order of their `insert_id` values. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of results to return from this request. Default is 50. If the value is negative or exceeds 1000, the request is rejected. The presence of `next_page_token` in the response indicates that more results might be available. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of results to return from this request. Default is 50. If the value is negative or exceeds 1000, the request is rejected. The presence of `next_page_token` in the response indicates that more results might be available. 



**Returns**

  * (::Integer) — Optional. The maximum number of results to return from this request. Default is 50. If the value is negative or exceeds 1000, the request is rejected. The presence of `next_page_token` in the response indicates that more results might be available. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. If present, then retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of other method parameters should be identical to those in the previous call. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. If present, then retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of other method parameters should be identical to those in the previous call. 



**Returns**

  * (::String) — Optional. If present, then retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of other method parameters should be identical to those in the previous call. 



### #resource_names
    
    
    def resource_names() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Required. Names of one or more parent resources from which to retrieve log entries:

    * `projects/[PROJECT_ID]`
    * `organizations/[ORGANIZATION_ID]`
    * `billingAccounts/[BILLING_ACCOUNT_ID]`
    * `folders/[FOLDER_ID]`

May alternatively be one or more views:

    * `projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`
    * `organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`
    * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`
    * `folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`

Projects listed in the `project_ids` field are added to this list. A maximum of 100 resources may be specified in a single request. 




### #resource_names=
    
    
    def resource_names=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Required. Names of one or more parent resources from which to retrieve log entries:

    * `projects/[PROJECT_ID]`
    * `organizations/[ORGANIZATION_ID]`
    * `billingAccounts/[BILLING_ACCOUNT_ID]`
    * `folders/[FOLDER_ID]`

May alternatively be one or more views:

    * `projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`
    * `organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`
    * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`
    * `folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`

Projects listed in the `project_ids` field are added to this list. A maximum of 100 resources may be specified in a single request. 




**Returns**

  * (::Array<::String>) — Required. Names of one or more parent resources from which to retrieve log entries:

    * `projects/[PROJECT_ID]`
    * `organizations/[ORGANIZATION_ID]`
    * `billingAccounts/[BILLING_ACCOUNT_ID]`
    * `folders/[FOLDER_ID]`

May alternatively be one or more views:

    * `projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`
    * `organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`
    * `billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`
    * `folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/views/[VIEW_ID]`

Projects listed in the `project_ids` field are added to this list. A maximum of 100 resources may be specified in a single request. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
