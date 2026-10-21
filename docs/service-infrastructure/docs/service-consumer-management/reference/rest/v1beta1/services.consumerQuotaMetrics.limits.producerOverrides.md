---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides
title: REST Resource: services.consumerQuotaMetrics.limits.producerOverrides \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:48.730210+00:00
---

# REST Resource: services.consumerQuotaMetrics.limits.producerOverrides  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  REST Resource: services.consumerQuotaMetrics.limits.producerOverrides Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: QuotaOverride
    * JSON representation
  * Methods



## Resource: QuotaOverride

A quota override

JSON representation  
---  
      
    
    {
      "name": string,
      "metric": string,
      "unit": string,
      "overrideValue": string,
      "dimensions": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` The resource name of the producer override. An example name would be: `services/compute.googleapis.com/projects/123/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/producerOverrides/4a3f2c1d`  
`metric` |  `string` The name of the metric to which this override applies.An example name would be: `compute.googleapis.com/cpus`  
`unit` |  `string` The limit unit of the limit to which this override applies.An example unit would be: `1/{project}/{region}` Note that `{project}` and `{region}` are not placeholders in this example; the literal characters `{` and `}` occur in the string.  
`overrideValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The overriding quota limit value. Can be any nonnegative integer, or -1 (unlimited quota).  
`dimensions` |  `map (key: string, value: string)` If this map is nonempty, then this override applies only to specific values for dimensions defined in the limit unit.For example, an override on a limit with the unit 1/{project}/{region} could contain an entry with the key "region" and the value "us-east-1"; the override is only applied to quota consumed in that region.This map has the following restrictions:

  * Keys that are not defined in the limit's unit are not valid keys. Any string appearing in {brackets} in the unit (besides {project} or {user}) is a defined key.
  * "project" is not a valid key; the project is already specified in the parent resource name.
  * "user" is not a valid key; the API does not support quota overrides that apply only to a specific user.
  * If "region" appears as a key, its value must be a valid Cloud region.
  * If "zone" appears as a key, its value must be a valid Cloud zone.
  * If any valid key other than "region" or "zone" appears in the map, then all valid keys other than "region" or "zone" must also appear in the map.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides/create)`

|  Creates a producer override.  
  
### `[delete](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides/delete)`

|  Deletes a producer override.  
  
### `[list](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides/list)`

|  Lists all producer overrides on this limit.  
  
### `[patch](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides/patch)`

|  Updates a producer override.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
