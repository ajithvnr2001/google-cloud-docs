---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/mart-logs/
title: MART logs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:36.645968+00:00
---

# MART logs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/mart-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  MART logs Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/mart-logs.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/mart-logs.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/mart-logs.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/mart-logs.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/mart-logs.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/mart-logs.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/mart-logs.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/mart-logs.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/mart-logs.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/mart-logs.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/mart-logs.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/mart-logs.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/mart-logs.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/mart-logs.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/mart-logs.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/mart-logs.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/mart-logs.html)



To troubleshoot MART issues in Apigee hybrid, look at the log files. MART logs are written to stdout/stderr and can be viewed using the [`kubectl`](https://kubernetes.io/docs/reference/kubectl/overview/) `logs` command.

On the Kubernetes administration machine, execute the following command:
    
    
    kubectl logs pod_name -n namespace

See also [Logging](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/logging) for details.

### MART error codes

The following error codes can occur in the MART logs:

Error | Description  
---|---  
`ROUTING_SERVICE_NOT_ENABLED` `routing.RoutingServiceNotEnabled` | Occurs when `routing.service.enable` is set to false in this file in the MART pod: `/opt/apigee/edge-hybrid-mart-server/conf/routing-service.properties`  
`HYBRID_MART_SERVER_ENDPOINT_NOT_FOUND  
  
routing.HybridMARTServerEndpointNotFound` | Occurs when the org does not have a value for the org property: `features.mart.server.endpoint`  
`HYBRID_AUTHN_AUTHZ_TOKEN_ERROR` `routing.HybridAuthNAuthZTokenError` | Occurs when the AuthN-AuthZ service returns a non-200 response code or an invalid token  
`MART_ENDPOINT_REQUIRED` `organizations.MartEndpointRequired` | Occurs when the org property `features.mart.server.endpoint` has a null or empty value.  
`HTTPS_MART_ENDPOINT_REQUIRED` `organizations.HttpsMartEndpointRequired` | Occurs when the org property `features.mart.server.endpoint` has a value starting with "http://" when `mart.routing.https.validation.enable` is set to true in this file in the MART pod: `/opt/apigee/edge-hybrid-mart-server/conf/routing-service.properties`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
