---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SearchAllAssignmentsRequest/
title: BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::SearchAllAssignmentsRequest (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:27.325105+00:00
---

# BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::SearchAllAssignmentsRequest (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-SearchAllAssignmentsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Reservation V1 API - Class Google::Cloud::Bigquery::Reservation::V1::SearchAllAssignmentsRequest (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.12.0  0.11.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.2 

Reference documentation and code samples for the BigQuery Reservation V1 API class Google::Cloud::Bigquery::Reservation::V1::SearchAllAssignmentsRequest.

The request for [ReservationService.SearchAllAssignments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-reservation-v1/latest/Google-Cloud-Bigquery-Reservation-V1-ReservationService-Client#Google__Cloud__Bigquery__Reservation__V1__ReservationService__Client_search_all_assignments_instance_ "Google::Cloud::Bigquery::Reservation::V1::ReservationService::Client#search_all_assignments \(method\)"). Note: "bigquery.reservationAssignments.search" permission is required on the related assignee.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of items to return per page. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of items to return per page. 



**Returns**

  * (::Integer) — The maximum number of items to return per page. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — The next_page_token value returned from a previous List request, if any. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The next_page_token value returned from a previous List request, if any. 



**Returns**

  * (::String) — The next_page_token value returned from a previous List request, if any. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name with location (project name could be the wildcard '-'), e.g.: `projects/-/locations/US`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name with location (project name could be the wildcard '-'), e.g.: `projects/-/locations/US`. 



**Returns**

  * (::String) — Required. The resource name with location (project name could be the wildcard '-'), e.g.: `projects/-/locations/US`. 



### #query
    
    
    def query() -> ::String

**Returns**

  * (::String) — 

Please specify resource name as assignee in the query.

Examples:

    * `assignee=projects/myproject`
    * `assignee=folders/123`
    * `assignee=organizations/456`



### #query=
    
    
    def query=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Please specify resource name as assignee in the query.

Examples:

    * `assignee=projects/myproject`
    * `assignee=folders/123`
    * `assignee=organizations/456`



**Returns**

  * (::String) — 

Please specify resource name as assignee in the query.

Examples:

    * `assignee=projects/myproject`
    * `assignee=folders/123`
    * `assignee=organizations/456`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
