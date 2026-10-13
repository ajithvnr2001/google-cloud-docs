---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-HealthCheckService-HealthStatusAggregationPolicy/
title: Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::HealthCheckService::HealthStatusAggregationPolicy (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:43.516449+00:00
---

# Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::HealthCheckService::HealthStatusAggregationPolicy (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-HealthCheckService-HealthStatusAggregationPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::HealthCheckService::HealthStatusAggregationPolicy (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API module Google::Cloud::Compute::V1::HealthCheckService::HealthStatusAggregationPolicy.

Optional. Policy for how the results from multiple health checks for the same endpoint are aggregated. Defaults to NO_AGGREGATION if unspecified.

  * NO_AGGREGATION. An EndpointHealth message is returned for each pair in the health check service.
  * AND. If any health check of an endpoint reportsUNHEALTHY, then UNHEALTHY is theHealthState of the endpoint. If all health checks reportHEALTHY, the HealthState of the endpoint isHEALTHY.



. This is only allowed with regional HealthCheckService.

## Constants 

### UNDEFINED_HEALTH_STATUS_AGGREGATION_POLICY

**value:** 0  
A value indicating that the enum field is not set.

### AND

**value:** 64_951  
If any backend's health check reports UNHEALTHY, then UNHEALTHY is the HealthState of the entire health check service. If all backend's are healthy, the HealthState of the health check service isHEALTHY.

### NO_AGGREGATION

**value:** 426_445_124  
An EndpointHealth message is returned for each backend in the health check service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
