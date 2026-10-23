---
url: https://docs.cloud.google.com/service-infrastructure/docs/admission-control/
title: Admission Control \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:09.677443+00:00
---

# Admission Control  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/admission-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Admission Control Stay organized with collections  Save and categorize content based on your preferences. 

## Introduction

This page describes how to use the Service Control API v2 for admission control for [managed services](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) that are integrated with Service Infrastructure. It is intended for service producers who want to deeply integrate their services with Google Cloud.

Service Infrastructure is a foundational platform for developers to produce, manage, secure and consume APIs and services. It uses a simple, generic service usage model: a consumer consumes a service managed by a producer. All Google APIs and [Google Cloud APIs](https://docs.cloud.google.com/apis) use this model, since they are also built on top of Service Infrastructure.

When a client accesses a service, all the entities involved in the access typically require a status and policy check, including the consumer, service, producer, user, application, network, and resources. With Service Infrastructure, this process is called admission control, which includes authentication, authorization, auditing, rate limiting, and more.

**Note:** For terminology used in this page, see [API Glossary](https://docs.cloud.google.com/apis/design/glossary).

## Service Control API v2

The Service Control API v2 provides a simple [`services.check`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/services/check) method that provides admission control to all services integrated with Service Infrastructure. This method lets you do the following in a single method call:

  * Status checking 
    * Abuse status
    * Billing status
    * Consumer status
    * Service status
    * Service enablement
  * Authentication 
    * Google OAuth access token
    * Google service account signed JWT
  * Authorization 
    * [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam)
  * Auditing 
    * [Cloud Audit Logs](https://cloud.google.com/logging/docs/audit). The audit log is associated with service "externalaudit.googleapis.com".



When a service calls the Service Control API, the producer is also a consumer of the Service Control API. Therefore, the `services.check` method also performs admission control on the call to the Service Control API.

In order for a service to call the Service Control API, you must enable the Service Control API on the producer project and have proper permissions on the service. For more information, see Cloud APIs [Getting Started](https://docs.cloud.google.com/apis/docs/getting-started) and Service Control [Access Control](https://docs.cloud.google.com/service-infrastructure/docs/service-control/access-control).

### Request attributes

When a client accesses a service, the service needs to abstract the access into one or more API requests that can be checked with admission control. In most cases, such accesses are indeed real API requests. In other cases, the access can be complicated data import jobs or SQL queries, and the service needs to model the access in terms of a set of virtual API requests and perform admission control on each request.

To perform admission control using the Service Control API, the service needs to call the [`services.check`](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/services/check) method with required request attributes. The following table lists the attributes needed for admission control. For the complete specification, see [`AttributeContext`](https://github.com/googleapis/googleapis/blob/master/google/rpc/context/attribute_context.proto).

Attibute | Description | Example  
---|---|---  
`origin.ip` | The IP address of the caller. | "1.2.3.4"  
`api.service` | The API service name. | "endpointsapis.appspot.com"  
`api.operation` | The API method name. | "google.example.hello.v1.HelloService.GetHello"  
`api.version` | The API version string. | "v1"  
`api.protocol` | The API protocol name. | "https"  
`request.id` | A unique request id. | "123e4567-e89b-12d3-a456-426655440000"  
`request.time` | The time of the request. | "2019-07-31T05:20:00Z"  
`request.method` | The HTTP method name. | "POST"  
`request.scheme` | The URL scheme. | "https"  
`request.host` | The HTTP host header. | "endpointsapis.appspot.com"  
`request.path` | The URL path. | "/v1/hello"  
`request.headers` | The HTTP request headers. The required headers are "authorization", "user-agent", "origin", "referer". |   
`resource.name` | The target resource name. | "projects/123/topics/news-feed"  
  
### Resource attributes

When a client accesses a service, the access may involve one or more resources inside the service, such as reading an object or creating a VM instance. The service can use Service Infrastructure admission control for access control on resources, supported by [IAM](https://docs.cloud.google.com/iam) and [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit). If your service doesn't need access control, you can skip this section.

For access control, a service needs to pass resource attributes to the `services.check` method along with the request attributes. The following table shows the resource attributes required for access control.

Attibute | Description | Example  
---|---|---  
`name` | The resource name. | "projects/123/locations/global/instances/instance-1"  
`type` | The resource type. The format is "{service}/{Kind}". | "endpointsapis.appspot.com/Instance"  
`permission` | The resource permission. The format is "{service}/{kinds}.{verb}". | "endpointsapis.appspot.com/instances.get"  
  
For performance and efficiency, the `services.check` method allows you to check multiple permissions on a single resource in one call.

## Performing admission control

Once you have deployed your service configuration to the Service Management API and your service is ready to serve requests from clients, you can begin calling `services.check` for your deployed service. You should call `services.check` to perform admission control whenever your service receives a request.

To quickly experiment with the admission control, you can use the `gcurl` command to call the `services.check` method. See [Getting Started with the Service Control API](https://docs.cloud.google.com/service-infrastructure/docs/service-control/getting-started) for the initial setup steps.

The following example shows you how to use `gcurl` command to call `services.check` over HTTP.
    
    
    gcurl -d '{
      "service_config_id": "latest",
      "attributes": {
        "origin": {
          "ip": "1.2.3.4"
        },
        "api": {
          "service": "endpointsapis.appspot.com",
          "operation": "google.example.hello.v1.HelloService.GetHello",
          "version": "v1",
          "protocol": "https"
        }
      },
      "request": {
        "id": "123e4567-e89b-12d3-a456-426655440000",
        "time": "2019-07-31T05:20:00Z",
        "scheme": "https",
        "host": "endpointsapis.appspot.com"
        "headers": {
          "authorization": "Bearer xxx",
          "user-agent": "curl/1.0"
        }
      },
      "resources": [
      ]
    }' https://servicecontrol.googleapis.com/v2/services/endpointsapis.appspot.com:check
    {
    }
    

The response from the `services.check` method indicates whether the admission control has passed. If it passes, the response should be empty. If it fails, the `status` in the response contains error information that the service should return to the client. The service often needs to translate the error information to its own format. The service can also use the information for logging and monitoring purposes.

For production services, you should use one of Google-provided client libraries to call the Service Control API. Such libraries provide great usability and handle common functionality automatically, such as authentication. For more information, see [Client Libraries Explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
