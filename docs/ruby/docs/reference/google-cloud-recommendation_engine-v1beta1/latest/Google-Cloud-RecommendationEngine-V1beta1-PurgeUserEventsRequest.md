---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recommendation_engine-v1beta1/latest/Google-Cloud-RecommendationEngine-V1beta1-PurgeUserEventsRequest/
title: Recommendations AI V1beta1 API - Class Google::Cloud::RecommendationEngine::V1beta1::PurgeUserEventsRequest (v0.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:22.238437+00:00
---

# Recommendations AI V1beta1 API - Class Google::Cloud::RecommendationEngine::V1beta1::PurgeUserEventsRequest (v0.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-recommendation_engine-v1beta1/latest/Google-Cloud-RecommendationEngine-V1beta1-PurgeUserEventsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Recommendations AI V1beta1 API - Class Google::Cloud::RecommendationEngine::V1beta1::PurgeUserEventsRequest (v0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.17.1  0.16.0  0.15.1  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.2  0.8.2  0.7.0  0.6.1  0.5.0  0.4.1  0.3.7 

Reference documentation and code samples for the Recommendations AI V1beta1 API class Google::Cloud::RecommendationEngine::V1beta1::PurgeUserEventsRequest.

Request message for PurgeUserEvents method.

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

  * (::String) — 

Required. The filter string to specify the events to be deleted. Empty string filter is not allowed. This filter can also be used with ListUserEvents API to list events that will be deleted. The eligible fields for filtering are:

    * eventType - UserEvent.eventType field of type string.
    * eventTime - in ISO 8601 "zulu" format.
    * visitorId - field of type string. Specifying this will delete all events associated with a visitor.
    * userId - field of type string. Specifying this will delete all events associated with a user. Example 1: Deleting all events in a time range. `eventTime > "2012-04-23T18:25:43.511Z" eventTime < "2012-04-23T18:30:43.511Z"` Example 2: Deleting specific eventType in time range. `eventTime > "2012-04-23T18:25:43.511Z" eventType = "detail-page-view"` Example 3: Deleting all events for a specific visitor `visitorId = visitor1024` The filtering fields are assumed to have an implicit AND.



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Required. The filter string to specify the events to be deleted. Empty string filter is not allowed. This filter can also be used with ListUserEvents API to list events that will be deleted. The eligible fields for filtering are:

    * eventType - UserEvent.eventType field of type string.
    * eventTime - in ISO 8601 "zulu" format.
    * visitorId - field of type string. Specifying this will delete all events associated with a visitor.
    * userId - field of type string. Specifying this will delete all events associated with a user. Example 1: Deleting all events in a time range. `eventTime > "2012-04-23T18:25:43.511Z" eventTime < "2012-04-23T18:30:43.511Z"` Example 2: Deleting specific eventType in time range. `eventTime > "2012-04-23T18:25:43.511Z" eventType = "detail-page-view"` Example 3: Deleting all events for a specific visitor `visitorId = visitor1024` The filtering fields are assumed to have an implicit AND.



**Returns**

  * (::String) — 

Required. The filter string to specify the events to be deleted. Empty string filter is not allowed. This filter can also be used with ListUserEvents API to list events that will be deleted. The eligible fields for filtering are:

    * eventType - UserEvent.eventType field of type string.
    * eventTime - in ISO 8601 "zulu" format.
    * visitorId - field of type string. Specifying this will delete all events associated with a visitor.
    * userId - field of type string. Specifying this will delete all events associated with a user. Example 1: Deleting all events in a time range. `eventTime > "2012-04-23T18:25:43.511Z" eventTime < "2012-04-23T18:30:43.511Z"` Example 2: Deleting specific eventType in time range. `eventTime > "2012-04-23T18:25:43.511Z" eventType = "detail-page-view"` Example 3: Deleting all events for a specific visitor `visitorId = visitor1024` The filtering fields are assumed to have an implicit AND.



### #force
    
    
    def force() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. The default value is false. Override this flag to true to actually perform the purge. If the field is not set to true, a sampling of events to be deleted will be returned. 



### #force=
    
    
    def force=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. The default value is false. Override this flag to true to actually perform the purge. If the field is not set to true, a sampling of events to be deleted will be returned. 



**Returns**

  * (::Boolean) — Optional. The default value is false. Override this flag to true to actually perform the purge. If the field is not set to true, a sampling of events to be deleted will be returned. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the event_store under which the events are created. The format is `projects/${projectId}/locations/global/catalogs/${catalogId}/eventStores/${eventStoreId}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the event_store under which the events are created. The format is `projects/${projectId}/locations/global/catalogs/${catalogId}/eventStores/${eventStoreId}`



**Returns**

  * (::String) — Required. The resource name of the event_store under which the events are created. The format is `projects/${projectId}/locations/global/catalogs/${catalogId}/eventStores/${eventStoreId}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
