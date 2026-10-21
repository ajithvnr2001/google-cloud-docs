---
url: https://docs.cloud.google.com/service-infrastructure/docs/rate-limiting/
title: Rate Limiting \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:09.112142+00:00
---

# Rate Limiting  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/rate-limiting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Rate Limiting Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use Service Infrastructure to implement rate limiting for [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) that are integrated with the Service Management API.

A managed service can serve many [service consumers](https://docs.cloud.google.com/service-infrastructure/docs/glossary#consumer). In order to protect system capacity and ensure fair usage, a managed service often uses rate limiting to distribute its capacity among its service consumers. The [Service Management](https://docs.cloud.google.com/service-infrastructure/docs/glossary#management) and [Service Control](https://docs.cloud.google.com/service-infrastructure/docs/glossary#control) APIs allow you to manage and enforce rate limiting.

## Configuring rate limits

To use the rate limiting feature, configure `_quota metrics_` and `_quota limits_` in the [service configuration](https://docs.cloud.google.com/service-infrastructure/docs/glossary#config) for your [service producer](https://docs.cloud.google.com/service-infrastructure/docs/glossary#producer) project.

Currently, the supported rate limiting is the number of requests per minute per service consumer, where the service consumer is a Google Cloud project as identified by an API key, a project id, or a project number. For rate limiting, the concept of request is an opaque concept. A service can choose an HTTP request as a request, or a byte of payload as a request. The rate limiting feature is independent of the semantics of a request.

### Quota metrics

A metric is a named counter for measuring a certain value over time. For example, the number of HTTP requests a service receives is a metric. A quota metric is a metric that is used for quota and rate limiting purposes. When an activity occurs with a service, one or more quota metrics may increase. When the metric value hits the predefined quota limit, the service should reject the activity with a `429` error.

### Quota limits

A quota limit represents an enforceable limit on a quota metric. For example, the number of requests per service consumer per minute is a quota limit. At this time, the only supported type of quota limit is per minute per consumer, specifically, `1/min/{project}`.

The actual rate limit for a (service, consumer) pair is controlled by 3 settings:

  * The default limit specified for the managed service.
  * The service producer override for the service consumer.
  * The service consumer override for the service consumer.



The effective rate limit is:

  * The default limit if there is no override.
  * The service producer override if there is a service producer override, but no service consumer override.
  * The minimum(service consumer override, default limit) if there is a service consumer override, but no service producer override.
  * The minimum(service consumer override, service producer override) if there are both service producer and service consumer overrides.



## Enforcing rate limiting

To enforce rate limiting, each server that belongs to a managed service needs to call the Service Control API [`services.allocateQuota`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) method regularly. If the response of the [`services.allocateQuota`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) method indicates that the usage is above the limit, the server should reject the incoming request with a `429` error. For more information, see the reference documentation for the [`services.allocateQuota`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) method.

It is recommended that each server should use batching, caching, and predictive logic to improve system performance and reliability. In general, one server should only call the [`services.allocateQuota`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) method once per second for the same (service, consumer, metric) tuple.

The following example demonstrates how to call the [`services.allocateQuota`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) method to check for rate limiting. The important request parameters that must be set correctly are the service name, the consumer id, the metric name, and the metric value. The [`services.allocateQuota`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) method will try to increase the usage by the specified amount for the (service, consumer, metric) tuple. If the increased usage goes above the limit, an error is returned. The following example uses the `gcurl` command to demonstrate the call. To learn how to set this up, see [Getting Started with the Service Control API](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started).

**Note:** A service consumer can be specified using a project id, a project number, or an API key.
    
    
    gcurl -d '{
      "allocateOperation": {
        "operationId": "123e4567-e89b-12d3-a456-426655440000",
        "methodName": "google.example.hello.v1.HelloService.GetHello",
        "consumerId": "project:endpointsapis-consumer",
        "quotaMetrics": [{
          "metricName": "endpointsapis.appspot.com/requests",
          "metricValues": [{
            "int64Value": 1
          }]
        }],
        "quotaMode": "NORMAL"
      }
    }' https://servicecontrol.googleapis.com/v1/services/endpointsapis.appspot.com:allocateQuota
    {
      "operationId": "123e4567-e89b-12d3-a456-426655440000",
      "quotaMetrics": [
        {
          "metricName": "serviceruntime.googleapis.com/api/consumer/quota_used_count",
          "metricValues": [
            {
              "labels": {
                "/quota_name": "endpointsapis.appspot.com/requests"
              },
              "int64Value": "1"
            }
          ]
        }
      ],
      "serviceConfigId": "2017-09-10r0"
    }
    

## Error handling

If the HTTP response code is `200`, and the response contains [`RESOURCE_EXHAUSTED`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#Code) [`QuotaError`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#QuotaError), your server should reject the request with a `429` error. If the response doesn't contain any quota error, your server should continue serving the incoming requests. For all other quota errors, your server should reject the request with a `409` error. Due to the security risks, you need to be very careful about what error information you include in the error message.

For all other HTTP response codes, it is likely your server has some programming bug. It is recommended your server continue to serve the incoming requests while you debug the problem. If the [`services.allocateQuota`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) method returns any unexpected error, your service should log the error and accept the income requests. You can debug the error later.

### Fail Open

The rate limiting feature is for protecting your managed service from getting overloaded and distributing your service capacity fairly among service consumers. Because most service consumers should not reach their rate limits during normal operations, your managed service should accept all incoming requests if the rate limiting feature is unavailable, also known as _fail open_. This prevents your service availability being affected by the rate limiting system.

If you use the [`services.allocateQuota`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota) method, your service must ignore `500`, `503` and `504` errors without any retry. To prevent a hard dependency on the rate limiting feature, the Service Control API issues a limited amount of error injection on a regular basis.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
