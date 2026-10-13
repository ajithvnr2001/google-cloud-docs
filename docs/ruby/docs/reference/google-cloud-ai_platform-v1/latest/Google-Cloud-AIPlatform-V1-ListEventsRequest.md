---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListEventsRequest/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ListEventsRequest (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:31.312966+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ListEventsRequest (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListEventsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ListEventsRequest (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::ListEventsRequest.

Request message for [SessionService.ListEvents](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SessionService-Client#Google__Cloud__AIPlatform__V1__SessionService__Client_list_events_instance_ "Google::Cloud::AIPlatform::V1::SessionService::Client#list_events \(method\)").

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

  * (::String) — Optional. The standard list filter. Supported fields:

    * `timestamp` range (i.e. `timestamp>="2025-01-31T11:30:00-04:00"` where the timestamp is in RFC 3339 format)

More detail in [AIP-160](https://google.aip.dev/160). 




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The standard list filter. Supported fields:

    * `timestamp` range (i.e. `timestamp>="2025-01-31T11:30:00-04:00"` where the timestamp is in RFC 3339 format)

More detail in [AIP-160](https://google.aip.dev/160). 




**Returns**

  * (::String) — Optional. The standard list filter. Supported fields:

    * `timestamp` range (i.e. `timestamp>="2025-01-31T11:30:00-04:00"` where the timestamp is in RFC 3339 format)

More detail in [AIP-160](https://google.aip.dev/160). 




### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields:

    * `timestamp`

Example: `timestamp desc`. 




### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields:

    * `timestamp`

Example: `timestamp desc`. 




**Returns**

  * (::String) — Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields:

    * `timestamp`

Example: `timestamp desc`. 




### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of events to return. The service may return fewer than this value. If unspecified, at most 100 events will be returned. These events are ordered by timestamp in ascending order. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of events to return. The service may return fewer than this value. If unspecified, at most 100 events will be returned. These events are ordered by timestamp in ascending order. 



**Returns**

  * (::Integer) — Optional. The maximum number of events to return. The service may return fewer than this value. If unspecified, at most 100 events will be returned. These events are ordered by timestamp in ascending order. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. The [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListEventsResponse#Google__Cloud__AIPlatform__V1__ListEventsResponse_next_page_token_instance_ "Google::Cloud::AIPlatform::V1::ListEventsResponse#next_page_token \(method\)") value returned from a previous list [SessionService.ListEvents](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SessionService-Client#Google__Cloud__AIPlatform__V1__SessionService__Client_list_events_instance_ "Google::Cloud::AIPlatform::V1::SessionService::Client#list_events \(method\)") call. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListEventsResponse#Google__Cloud__AIPlatform__V1__ListEventsResponse_next_page_token_instance_ "Google::Cloud::AIPlatform::V1::ListEventsResponse#next_page_token \(method\)") value returned from a previous list [SessionService.ListEvents](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SessionService-Client#Google__Cloud__AIPlatform__V1__SessionService__Client_list_events_instance_ "Google::Cloud::AIPlatform::V1::SessionService::Client#list_events \(method\)") call. 



**Returns**

  * (::String) — Optional. The [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListEventsResponse#Google__Cloud__AIPlatform__V1__ListEventsResponse_next_page_token_instance_ "Google::Cloud::AIPlatform::V1::ListEventsResponse#next_page_token \(method\)") value returned from a previous list [SessionService.ListEvents](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SessionService-Client#Google__Cloud__AIPlatform__V1__SessionService__Client_list_events_instance_ "Google::Cloud::AIPlatform::V1::SessionService::Client#list_events \(method\)") call. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the session to list events from. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/sessions/{session}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the session to list events from. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/sessions/{session}`



**Returns**

  * (::String) — Required. The resource name of the session to list events from. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/sessions/{session}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
