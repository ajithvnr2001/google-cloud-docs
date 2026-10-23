---
url: https://docs.cloud.google.com/service-infrastructure/docs/telemetry-reporting/
title: Telemetry Reporting \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:09.907683+00:00
---

# Telemetry Reporting  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/telemetry-reporting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Telemetry Reporting Stay organized with collections  Save and categorize content based on your preferences. 

**Alpha**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Introduction

This page describes how to use the Service Control API v2 for telemetry reporting for [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) that are integrated with Service Infrastructure. It is intended for service producers who want to deeply integrate their services with Google Cloud.

Service Infrastructure is a foundational platform for developers to produce, manage, secure and consume APIs and services. It uses a simple, generic service usage model: a consumer consumes a service managed by a producer. All Google APIs and [Google Cloud APIs](https://docs.cloud.google.com/apis) use this model, since they are also built on top of Service Infrastructure.

When a consumer accesses a service, the service reports relevant telemetry data to the platform, so both the consumer and the producer can observe the access. With Service Infrastructure, this process is called telemetry reporting, which includes analytics, auditing, billing, logging, and monitoring.

**Note:** For terminology used in this page, see [API Glossary](https://docs.cloud.google.com/apis/design/glossary).

## Service Control API v2

The Service Control API v2 provides a simple [`services.report`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/services/report) method that provides telemetry reporting to all services integrated with Service Infrastructure. This method lets you do the following in a single method call:

  * Analytics
  * Auditing
  * Billing
  * Logging
  * Monitoring



When a service reports telemetry data to the Service Control API, the data is distributed to the consumer, or the producer, or both, depending on the service configuration. For more information about configuring telemetry, see the logging and monitoring sections of [`google.api.Service`](https://github.com/googleapis/googleapis/blob/master/google/api/service.proto).

In order for a service to call the Service Control API, the producer must enable the Service Control API on the producer project, and the caller must have proper permissions on the service. For more information, see Cloud APIs [Getting Started](https://docs.cloud.google.com/apis/docs/getting-started) and [Service Control API Access Control](https://docs.cloud.google.com/service-infrastructure/docs/service-control/access-control).

### Request attributes

When a client accesses a service, the service needs to model the access in terms of a set of API requests, and describe each request using an [`AttributeContext`](https://github.com/googleapis/googleapis/blob/master/google/rpc/context/attribute_context.proto).

To report [API metrics](https://cloud.google.com/apis/docs/monitoring) using the Service Control API, the service needs to call the [`services.report`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/services/report) method for each request with the following attributes. The Service Control API will generate the API metrics and send them to [Cloud Monitoring](https://docs.cloud.google.com/monitoring).

Attribute | Description | Example  
---|---|---  
`origin.ip` | The IP address of the caller. | "1.2.3.4"  
`api.service` | The API service name. | "endpointsapis.appspot.com"  
`api.operation` | The API method name. | "google.example.hello.v1.HelloService.GetHello"  
`api.version` | The API version string. | "v1"  
`api.protocol` | The API protocol name. | "https"  
`request.id` | A unique request id. | "123e4567-e89b-12d3-a456-426655440000"  
`request.time` | The request timestamp. | "2019-07-31T05:20:00Z"  
`request.method` | The HTTP method name. | "POST"  
`request.scheme` | The URL scheme. | "https"  
`request.host` | The HTTP host header. | "endpointsapis.appspot.com"  
`request.path` | The URL path. | "/v1/hello"  
`response.code` | The response status code. | 200  
`response.size` | The response size in bytes. | 100  
`response.time` | The response timestamp. | "2019-07-31T05:20:02Z"  
`response.backend_latency` | The backend latency. | "0.007s"  
  
## Performing telemetry reporting

Once you have deployed your service configuration to the Service Management API and your service is ready to serve requests from clients, you can begin calling `services.report` for your deployed service. You should call `services.report` to perform telemetry reporting after your service receives a request.

To quickly experiment with the telemetry reporting, you can use the `gcurl` command to call the `services.report` method. See [Getting Started with the Service Control API](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started) for the initial setup steps.

The following example shows you how to use `gcurl` command to call `services.report` over HTTP.
    
    
    gcurl -d '{
      "service_config_id": "latest",
      "operations": [{
        "origin": {
          "ip": "1.2.3.4"
        },
        "api": {
          "service": "endpointsapis.appspot.com",
          "operation", "google.example.endpointsapis.v1.Workspaces.GetWorkspace",
          "version": "v1",
          "protocol": "https"
        },
        "request": {
          "id": "123e4567-e89b-12d3-a456-426655440000",
          "size": 50,
          "time": "2019-07-31T05:20:00Z",
        },
        "response": {
          "size": 100,
          "code": 200,
          "time": "2019-07-31T05:20:02Z",
          "backend_latency": "0.007s"
        },
        "destination": {
          "region_code": "us-central1"
        }
        "resource": {
          "name": "projects/123/locations/us-central1/workspaces/default"
        }
      }]
    }' https://servicecontrol.googleapis.com/v2/services/endpointsapis.appspot.com:report
    

If successful, the response from the `services.report` method should be empty. If failed, the API error should contain detailed error information. For more information about error handling, see [API Design Guide > Errors](https://docs.cloud.google.com/apis/design/errors).

For production services, you should use one of Google-provided client libraries to call the Service Control API. Such libraries provide great usability and handle common functionality automatically, such as authentication. For more information, see [Client Libraries Explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
