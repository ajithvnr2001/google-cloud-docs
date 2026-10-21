---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits
title: REST Resource: services.consumerQuotaMetrics.limits \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:44.134504+00:00
---

# REST Resource: services.consumerQuotaMetrics.limits  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  REST Resource: services.consumerQuotaMetrics.limits Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConsumerQuotaLimit
    * JSON representation
    * QuotaBucket
      * JSON representation
  * Methods



## Resource: ConsumerQuotaLimit

Consumer quota settings for a quota limit.

JSON representation  
---  
      
    
    {
      "name": string,
      "metric": string,
      "unit": string,
      "isPrecise": boolean,
      "quotaBuckets": [
        {
          object ([QuotaBucket](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits#ConsumerQuotaLimit.QuotaBucket))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The resource name of the quota limit.An example name would be: `services/compute.googleapis.com/projects/123/quotas/metrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion`The resource name is intended to be opaque and should not be parsed for its component strings, since its representation could change in the future.  
`metric` |  `string` The name of the parent metric of this limit.An example name would be: `compute.googleapis.com/cpus`  
`unit` |  `string` The limit unit.An example unit would be: `1/{project}/{region}` Note that `{project}` and `{region}` are not placeholders in this example; the literal characters `{` and `}` occur in the string.  
`isPrecise` |  `boolean` Whether this limit is precise or imprecise.  
`quotaBuckets[]` |  `object (`[QuotaBucket](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits#ConsumerQuotaLimit.QuotaBucket)`)` Summary of the enforced quota buckets, organized by quota dimension, ordered from least specific to most specific (for example, the global default bucket, with no quota dimensions, will always appear first).  
  
### QuotaBucket

A quota bucket is a quota provisioning unit for a specific set of dimensions.

JSON representation  
---  
      
    
    {
      "effectiveLimit": string,
      "defaultLimit": string,
      "producerOverride": {
        object ([QuotaOverride](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides#QuotaOverride))
      },
      "consumerOverride": {
        object ([QuotaOverride](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides#QuotaOverride))
      },
      "adminOverride": {
        object ([QuotaOverride](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides#QuotaOverride))
      },
      "dimensions": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`effectiveLimit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The effective limit of this quota bucket. Equal to defaultLimit if there are no overrides.  
`defaultLimit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The default limit of this quota bucket, as specified by the service configuration.  
`producerOverride` |  `object (`[QuotaOverride](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides#QuotaOverride)`)` Producer override on this quota bucket.  
`consumerOverride` |  `object (`[QuotaOverride](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides#QuotaOverride)`)` Consumer override on this quota bucket.  
`adminOverride` |  `object (`[QuotaOverride](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits.producerOverrides#QuotaOverride)`)` Admin override on this quota bucket.  
`dimensions` |  `map (key: string, value: string)` The dimensions of this quota bucket.If this map is empty, this is the global bucket, which is the default quota value applied to all requests that do not have a more specific override.If this map is nonempty, the default limit, effective limit, and quota overrides apply only to requests that have the dimensions given in the map.For example, if the map has key "region" and value "us-east-1", then the specified effective limit is only effective in that region, and the specified overrides apply only in that region.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits/get)`

|  Retrieves a summary of quota information for a specific quota limit.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
