---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/exceptions/
title: Exceptions and HTTP status codes \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:44.954985+00:00
---

# Exceptions and HTTP status codes  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/exceptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Exceptions and HTTP status codes Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the exceptions provided by the `endpoints` library as well as HTTP status codes supported by Cloud Endpoints Frameworks.

In many situations, you might want to use common HTTP status codes to indicate the success or failure of a user's API request. For example, if a user is attempting to retrieve an entity which doesn't exist, you might want to send an HTTP `404` status code to say that no entity exists with ID: `entityId`.

You can send common HTTP status codes by throwing an exception provided by the `endpoints` library as follows:
    
    
    throw new NotFoundException(user.getEmail());

## Exceptions provided by Endpoints Frameworks

Endpoints Frameworks provides the following exceptions, corresponding to specific HTTP status codes:

Exception | Corresponding HTTP status code  
---|---  
`com.google.api.server.spi.response.BadRequestException` | HTTP `400`  
`com.google.api.server.spi.response.UnauthorizedException` | HTTP `401`  
`com.google.api.server.spi.response.ForbiddenException` | HTTP `403`  
`com.google.api.server.spi.response.NotFoundException` | HTTP `404`  
`com.google.api.server.spi.response.ConflictException` | HTTP `409`  
`com.google.api.server.spi.response.InternalServerErrorException` | HTTP `500`  
`com.google.api.server.spi.response.ServiceUnavailableException` | HTTP `503`  
  
## Supported HTTP status codes

Cloud Endpoints Frameworks supports a subset of HTTP status codes in API responses. The following table describes the supported codes.

HTTP status codes | Support  
---|---  
HTTP 2xx | HTTP `200` is typically assumed by Endpoints Frameworks if the API method returns successfully.If the API method response type is `void` or the return value of the API method is `null` , HTTP `204` is set instead.  
HTTP 3xx | HTTP 3xx codes aren't supported. Use of any HTTP 3xx codes results in an HTTP `404` response.  
HTTP 4xx | Only the following HTTP 4xx codes are supported: 

  * `400`
  * `401`
  * `403`
  * `404`
  * `409`
  * `410`
  * `412`
  * `413`

Any other HTTP 4xx codes are returned as error `404`, except for the following:

  * `405` is returned as `501`
  * `408` is returned as `503`

  
HTTP 5xx | All HTTP 5xx status codes are converted to HTTP `503` in the client response.  
**Important:** Don't use custom exception classes to return HTTP 2xx codes. Endpoints Frameworks doesn't support returning HTTP `201` or any other 2xx codes except HTTP `200` and HTTP `204` as described in the preceding table.

## Creating your own exception classes

If you want to create other exception classes for other HTTP status codes, you need to subclass `com.google.api.server.spi.ServiceException`. The following snippet shows how to create an exception class that represents an HTTP `408` status code:
    
    
    import com.google.api.server.spi.ServiceException;
    
    // Exceptions must inherit from ServiceException
    public class RequestTimeoutException extends ServiceException {
      public RequestTimeoutException(String message) {
        super(408, message);
      }
    }

**Important:** An uncaught exception in your application results in an HTTP `503` error from your Cloud Endpoints API, unless it extends `com.google.api.server.spi.ServiceException`.

## Using unsupported HTTP status codes

It is possible to use HTTP status codes that aren't in the preceding supported list. Note that if you decide to do so, it might have unintended consequences for client libraries that access the API. To use unsupported error codes, create your own exception class, as described in the previous section, and add a new servlet initialization parameter `enableExceptionCompatibility` to `EndpointsServlet`:
    
    
      <servlet>
        <servlet-name>com.google.api.server.spi.EndpointsServlet</servlet-name>
        <servlet-class>com.google.api.server.spi.EndpointsServlet</servlet-class>
        <init-param>
          <param-name>services</param-name>
          <param-value>...</param-value>
        </init-param>
        <init-param>
          <param-name>enableExceptionCompatibility</param-name>
          <param-value>true</param-value>
        </init-param>
      </servlet>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
