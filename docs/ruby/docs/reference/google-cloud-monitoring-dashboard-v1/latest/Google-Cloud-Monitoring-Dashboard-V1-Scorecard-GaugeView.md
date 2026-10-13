---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Scorecard-GaugeView/
title: Cloud Monitoring Dashboards V1 API - Class Google::Cloud::Monitoring::Dashboard::V1::Scorecard::GaugeView (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:02.076871+00:00
---

# Cloud Monitoring Dashboards V1 API - Class Google::Cloud::Monitoring::Dashboard::V1::Scorecard::GaugeView (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-Scorecard-GaugeView/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Monitoring Dashboards V1 API - Class Google::Cloud::Monitoring::Dashboard::V1::Scorecard::GaugeView (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.16.0  0.15.0  0.14.2  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.6 

Reference documentation and code samples for the Cloud Monitoring Dashboards V1 API class Google::Cloud::Monitoring::Dashboard::V1::Scorecard::GaugeView.

A gauge chart shows where the current value sits within a pre-defined range. The upper and lower bounds should define the possible range of values for the scorecard's query (inclusive).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #lower_bound
    
    
    def lower_bound() -> ::Float

**Returns**

  * (::Float) — The lower bound for this gauge chart. The value of the chart should always be greater than or equal to this. 



### #lower_bound=
    
    
    def lower_bound=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The lower bound for this gauge chart. The value of the chart should always be greater than or equal to this. 



**Returns**

  * (::Float) — The lower bound for this gauge chart. The value of the chart should always be greater than or equal to this. 



### #upper_bound
    
    
    def upper_bound() -> ::Float

**Returns**

  * (::Float) — The upper bound for this gauge chart. The value of the chart should always be less than or equal to this. 



### #upper_bound=
    
    
    def upper_bound=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The upper bound for this gauge chart. The value of the chart should always be less than or equal to this. 



**Returns**

  * (::Float) — The upper bound for this gauge chart. The value of the chart should always be less than or equal to this. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
