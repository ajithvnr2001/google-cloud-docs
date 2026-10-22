---
url: https://docs.cloud.google.com/endpoints/docs/openapi/support-cors/
title: Enabling CORS support for Endpoints \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:28.209604+00:00
---

# Enabling CORS support for Endpoints  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/support-cors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Enabling CORS support for Endpoints Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

CORS (Cross-origin resource sharing) is a standard mechanism that allows XMLHttpRequest (XHR) calls executed in a web page to interact with resources from different origins. Without CORS, the [same-origin policy](https://developer.mozilla.org/docs/Web/Security/Same-origin_policy) enforced by all browsers would prevent cross-origin requests. For more background information on CORS, see the [Mozilla Developer Network (MDN) reference documentation](https://developer.mozilla.org/docs/Web/HTTP/CORS).

The CORS standard requires that web clients issue a CORS preflight `OPTIONS` to determine if the requested web server supports CORS. If a web server supports CORS request, it will handle the `OPTIONS` request with proper CORS response headers.

## Handle CORS in your backend application

If your backend supports CORS, you can configure ESP or ESPv2 to pass the CORS request to your backend. you can enable pass-through in the OpenAPI spec for your API as shown:
    
    
    swagger: "2.0"
    host: "my-cool-api.endpoints.my-project-id.cloud.goog"
    x-google-endpoints:
    - name: "my-cool-api.endpoints.my-project-id.cloud.goog"
      allowCors: True

You can also enable pass-through in an OpenAPI 3.x spec for your API as shown:
    
    
    openapi: 3.0.4
    servers:
    - url: https://my-cool-api.endpoints.my-project-id.cloud.goog
      x-google-endpoint:
        allowCors: True

**Warning:** the `name` field under `x-google-endpoints` must match the `host` field value. Both fields should use the endpoint service name.

## Handle CORS with ESP or ESPv2

If your backend does not support CORS, you can configure ESP or ESPv2 to handle CORS requests by specifying CORS startup flags. In this approach, [CORS Preflight requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#preflighted_requests) will not pass through to your backend application. Additionally, ESP or ESPv2 will append the configured CORS headers to responses from the backend service when appropriate.

The following CORS startup options are available for ESP and ESPv2 

  * [ESP CORS startup flags](https://docs.cloud.google.com/endpoints/docs/openapi/specify-proxy-startup-options#adding_cors_support_to_esp)
  * [ESPv2 CORS startup flags](https://docs.cloud.google.com/endpoints/docs/openapi/specify-esp-v2-startup-options#cors)

**Warning:** if CORS is handled by ESPv2, the `OPTIONS` CORS preflight request must have a valid `Origin` and `Access-Control-Request-Method` headers, otherwise it will not be handled properly.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
