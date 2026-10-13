---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeaturedContentNativeDashboard/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeaturedContentNativeDashboard (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:49.855588+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeaturedContentNativeDashboard (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeaturedContentNativeDashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeaturedContentNativeDashboard (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::FeaturedContentNativeDashboard.

FeaturedContentNativeDashboard resource.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #content_metadata
    
    
    def content_metadata() -> ::Google::Cloud::Chronicle::V1::FeaturedContentMetadata

**Returns**

  * ([::Google::Cloud::Chronicle::V1::FeaturedContentMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeaturedContentMetadata)) — Output only. Metadata about the FeaturedContentNativeDashboard. 



### #dashboard_content
    
    
    def dashboard_content() -> ::Google::Cloud::Chronicle::V1::NativeDashboardWithChartsAndQueries

**Returns**

  * ([::Google::Cloud::Chronicle::V1::NativeDashboardWithChartsAndQueries](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-NativeDashboardWithChartsAndQueries)) — Optional. The dashboard content. 



### #dashboard_content=
    
    
    def dashboard_content=(value) -> ::Google::Cloud::Chronicle::V1::NativeDashboardWithChartsAndQueries

**Parameter**

  * **value** ([::Google::Cloud::Chronicle::V1::NativeDashboardWithChartsAndQueries](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-NativeDashboardWithChartsAndQueries)) — Optional. The dashboard content. 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::NativeDashboardWithChartsAndQueries](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-NativeDashboardWithChartsAndQueries)) — Optional. The dashboard content. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The resource name of the FeaturedContentNativeDashboard. Format: projects/{project}/locations/{location}/instances/{instance}/contentHub/featuredContentNativeDashboards/{featured_content_native_dashboard} 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The resource name of the FeaturedContentNativeDashboard. Format: projects/{project}/locations/{location}/instances/{instance}/contentHub/featuredContentNativeDashboards/{featured_content_native_dashboard} 



**Returns**

  * (::String) — Identifier. The resource name of the FeaturedContentNativeDashboard. Format: projects/{project}/locations/{location}/instances/{instance}/contentHub/featuredContentNativeDashboards/{featured_content_native_dashboard} 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
