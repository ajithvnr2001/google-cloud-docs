---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/regionUrlMaps/validate/
title: Method: googleapis.compute.v1.regionUrlMaps.validate \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:00.584217+00:00
---

# Method: googleapis.compute.v1.regionUrlMaps.validate  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/regionUrlMaps/validate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.compute.v1.regionUrlMaps.validate Stay organized with collections  Save and categorize content based on your preferences. 

Runs static validation for the UrlMap. In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create the UrlMap.

## Arguments

Parameters  
---  
`project` |  `string` Required. Project ID for this request.  
`region` |  `string` Required. Name of the region scoping this request.  
`urlMap` |  `string` Required. Name of the UrlMap resource to be validated as.  
`body` |  `object ([RegionUrlMapsValidateRequest](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/Overview#RegionUrlMapsValidateRequest))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`UrlMapsValidateResponse`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/Overview#UrlMapsValidateResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps/validate).

### YAML
    
    
    - validate:
        call: googleapis.compute.v1.regionUrlMaps.validate
        args:
            project: ...
            region: ...
            urlMap: ...
            body:
                resource:
                    defaultRouteAction:
                        corsPolicy:
                            allowCredentials: ...
                            allowHeaders: ...
                            allowMethods: ...
                            allowOriginRegexes: ...
                            allowOrigins: ...
                            disabled: ...
                            exposeHeaders: ...
                            maxAge: ...
                        faultInjectionPolicy:
                            abort:
                                httpStatus: ...
                                percentage: ...
                            delay:
                                fixedDelay:
                                    nanos: ...
                                    seconds: ...
                                percentage: ...
                        maxStreamDuration: ...
                        requestMirrorPolicy:
                            backendService: ...
                        retryPolicy:
                            numRetries: ...
                            perTryTimeout: ...
                            retryConditions: ...
                        timeout: ...
                        urlRewrite:
                            hostRewrite: ...
                            pathPrefixRewrite: ...
                            pathTemplateRewrite: ...
                        weightedBackendServices: ...
                    defaultService: ...
                    defaultUrlRedirect:
                        hostRedirect: ...
                        httpsRedirect: ...
                        pathRedirect: ...
                        prefixRedirect: ...
                        redirectResponseCode: ...
                        stripQuery: ...
                    description: ...
                    fingerprint: ...
                    headerAction:
                        requestHeadersToAdd: ...
                        requestHeadersToRemove: ...
                        responseHeadersToAdd: ...
                        responseHeadersToRemove: ...
                    hostRules: ...
                    name: ...
                    pathMatchers: ...
                    tests: ...
        result: validateResult

### JSON
    
    
    [
      {
        "validate": {
          "call": "googleapis.compute.v1.regionUrlMaps.validate",
          "args": {
            "project": "...",
            "region": "...",
            "urlMap": "...",
            "body": {
              "resource": {
                "defaultRouteAction": {
                  "corsPolicy": {
                    "allowCredentials": "...",
                    "allowHeaders": "...",
                    "allowMethods": "...",
                    "allowOriginRegexes": "...",
                    "allowOrigins": "...",
                    "disabled": "...",
                    "exposeHeaders": "...",
                    "maxAge": "..."
                  },
                  "faultInjectionPolicy": {
                    "abort": {
                      "httpStatus": "...",
                      "percentage": "..."
                    },
                    "delay": {
                      "fixedDelay": {
                        "nanos": "...",
                        "seconds": "..."
                      },
                      "percentage": "..."
                    }
                  },
                  "maxStreamDuration": "...",
                  "requestMirrorPolicy": {
                    "backendService": "..."
                  },
                  "retryPolicy": {
                    "numRetries": "...",
                    "perTryTimeout": "...",
                    "retryConditions": "..."
                  },
                  "timeout": "...",
                  "urlRewrite": {
                    "hostRewrite": "...",
                    "pathPrefixRewrite": "...",
                    "pathTemplateRewrite": "..."
                  },
                  "weightedBackendServices": "..."
                },
                "defaultService": "...",
                "defaultUrlRedirect": {
                  "hostRedirect": "...",
                  "httpsRedirect": "...",
                  "pathRedirect": "...",
                  "prefixRedirect": "...",
                  "redirectResponseCode": "...",
                  "stripQuery": "..."
                },
                "description": "...",
                "fingerprint": "...",
                "headerAction": {
                  "requestHeadersToAdd": "...",
                  "requestHeadersToRemove": "...",
                  "responseHeadersToAdd": "...",
                  "responseHeadersToRemove": "..."
                },
                "hostRules": "...",
                "name": "...",
                "pathMatchers": "...",
                "tests": "..."
              }
            }
          },
          "result": "validateResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
