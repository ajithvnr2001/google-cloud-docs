---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics
title: REST Resource: services.consumerQuotaMetrics \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:43.270527+00:00
---

# REST Resource: services.consumerQuotaMetrics  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  REST Resource: services.consumerQuotaMetrics Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConsumerQuotaMetric
    * JSON representation
  * Methods



## Resource: ConsumerQuotaMetric

Consumer quota settings for a quota metric.

JSON representation  
---  
      
    
    {
      "name": string,
      "metric": string,
      "displayName": string,
      "consumerQuotaLimits": [
        {
          object ([ConsumerQuotaLimit](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits#ConsumerQuotaLimit))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The resource name of the quota settings on this metric for this consumer.An example name would be: `services/serviceconsumermanagement.googleapis.com/projects/123/quota/metrics/compute.googleapis.com%2FcpusThe resource name is intended to be opaque and should not be parsed for its component strings, since its representation could change in the future.  
`metric` |  `string` The name of the metric.An example name would be: `compute.googleapis.com/cpus`  
`displayName` |  `string` The display name of the metric.An example name would be: "CPUs"  
`consumerQuotaLimits[]` |  `object (`[ConsumerQuotaLimit](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits#ConsumerQuotaLimit)`)` The consumer quota for each quota limit defined on the metric.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics/get)`

|  Retrieves a summary of quota information for a specific quota metric.  
  
### `[importProducerOverrides](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics/importProducerOverrides)`

|  Create or update multiple producer overrides atomically, all on the same consumer, but on many different metrics or limits.  
  
### `[list](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics/list)`

|  Retrieves a summary of all quota information about this consumer that is visible to the service producer, for each quota metric defined by the service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
