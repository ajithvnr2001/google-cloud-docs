---
url: https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/error-messages/
title: Error messages \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:15.718005+00:00
---

# Error messages  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/error-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Error messages Stay organized with collections  Save and categorize content based on your preferences. 

This page identifies some of the errors and messages that are returned when you use organization restrictions.

### Permission denied error message sample

If a request is denied due to an organization restrictions header violation, a 403 HTTP Response is returned with the following details:
    
    
    {
      "error": {
        "code": 403,
        "message": "Access denied by organization restriction. Please contact your administrator for additional information.",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "ORG_RESTRICTION_VIOLATION",
            "domain": "googleapis.com",
            "metadata": {
              "service": "abc.googleapis.com"
            }
          }
        ]
      }
    }
    
    

### Malformed header error message sample

If a request contains a malformed `X-Goog-Allowed-Resources` header, a 400 HTTP response is returned with the following details:
    
    
    {
      "error": {
        "code": 400,
        "message": "Org Restriction Header is not valid. Please pass a valid Org Restriction Header.",
        "status": "INVALID_ARGUMENT",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "ORG_RESTRICTION_HEADER_INVALID",
            "domain": "googleapis.com",
            "metadata": {
              "service": "abc.googleapis.com"
            }
          }
        ]
      }
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
