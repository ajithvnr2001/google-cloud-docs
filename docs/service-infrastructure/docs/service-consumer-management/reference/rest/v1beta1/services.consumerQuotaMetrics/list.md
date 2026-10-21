---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics/list/
title: Method: services.consumerQuotaMetrics.list \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:41.569890+00:00
---

# Method: services.consumerQuotaMetrics.list  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.consumerQuotaMetrics.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Retrieves a summary of all quota information about this consumer that is visible to the service producer, for each quota metric defined by the service. Each metric includes information about all of its defined limits. Each limit includes the limit configuration (quota unit, preciseness, default value), the current effective limit value, and all of the overrides applied to the limit.

### HTTP request

`GET https://serviceconsumermanagement.googleapis.com/v1beta1/{parent=services/*/*/*}/consumerQuotaMetrics`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Parent of the quotas resource.An example parent would be: `services/serviceconsumermanagement.googleapis.com/projects/123` Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource `parent`:

  * `serviceconsumermanagement.quota.get`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Requested size of the next page of data.  
`pageToken` |  `string` Token identifying which result to start with; returned by a previous list call.  
`view` |  `enum (`[QuotaView](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/QuotaView)`)` Specifies the level of detail for quota information in the response.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response message for consumerQuotaMetrics.list.

JSON representation  
---  
      
    
    {
      "metrics": [
        {
          object ([ConsumerQuotaMetric](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics#ConsumerQuotaMetric))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`metrics[]` |  `object (`[ConsumerQuotaMetric](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1beta1/services.consumerQuotaMetrics#ConsumerQuotaMetric)`)` Quota settings for the consumer, organized by quota metric.  
`nextPageToken` |  `string` Token identifying which result to start with; returned by a previous list call.  
  
### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Try it!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
