---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits/get/
title: Method: services.consumerQuotaMetrics.limits.get \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:55.255715+00:00
---

# Method: services.consumerQuotaMetrics.limits.get  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.consumerQuotaMetrics.limits.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Retrieves a summary of quota information for a specific quota limit.

### HTTP request

`GET https://serviceconsumermanagement.googleapis.com/v1beta1/{name=services/*/*/*/consumerQuotaMetrics/*/limits/*}`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The resource name of the quota limit, returned by a consumerQuotaMetrics.list or consumerQuotaMetrics.get call.An example name would be: `services/compute.googleapis.com/projects/123/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion` Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource `name`:

  * `serviceconsumermanagement.quota.get`

  
  
### Query parameters

Parameters  
---  
`view` |  `enum (`[QuotaView](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/QuotaView)`)` Specifies the level of detail for quota information in the response.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ConsumerQuotaLimit](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics.limits#ConsumerQuotaLimit)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Try it!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
