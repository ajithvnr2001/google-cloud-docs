---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription-LinkedResource/
title: Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::LinkedResource (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:40.320165+00:00
---

# Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::LinkedResource (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription-LinkedResource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::LinkedResource (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Analytics Hub V1 API class Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription::LinkedResource.

Reference to a linked resource tracked by this Subscription.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #linked_dataset
    
    
    def linked_dataset() -> ::String

**Returns**

  * (::String) — Output only. Name of the linked dataset, e.g. projects/subscriberproject/datasets/linked_dataset

Note: The following fields are mutually exclusive: `linked_dataset`, `linked_pubsub_subscription`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #linked_pubsub_subscription
    
    
    def linked_pubsub_subscription() -> ::String

**Returns**

  * (::String) — Output only. Name of the Pub/Sub subscription, e.g. projects/subscriberproject/subscriptions/subscriptions/sub_id

Note: The following fields are mutually exclusive: `linked_pubsub_subscription`, `linked_dataset`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #listing
    
    
    def listing() -> ::String

**Returns**

  * (::String) — Output only. Listing for which linked resource is created. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
