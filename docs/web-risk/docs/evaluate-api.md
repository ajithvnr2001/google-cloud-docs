---
url: https://docs.cloud.google.com/web-risk/docs/evaluate-api/
title: Using the Evaluate API \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:03.573153+00:00
---

# Using the Evaluate API  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/evaluate-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Guides ](https://docs.cloud.google.com/web-risk/docs/detect-malicious-urls)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using the Evaluate API

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The page explains how to use the Evaluate API to let your client applications evaluate the maliciousness of a URL. This API returns a per-threat-type confidence score that indicates the likelihood that the URL is malicious. This likelihood is computed based on Safe Browsing blocklists, generative AI models, machine learning models and heuristic rules. If you want a binary result instead of a confidence score, use the [Lookup API](https://docs.cloud.google.com/web-risk/docs/lookup-api).

**Note:** Any URLs submitted to the Evaluate API may undergo additional processing, including crawls.

## Before you begin

This feature is available in private preview to a limited set of customers whose use case directly aligns to its capabilities. Contact our sales team to request a review of your use case by our product and engineering teams.

## Evaluating URLs

To evaluate a URL, send an HTTP `POST` request to the [`evaluateUri`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1eap1/TopLevel/evaluateUri) method. Understand the following considerations when evaluating URLs:

  * The Evaluate API supports one URL per request. If you want to check multiple URLs, send a separate request for each URL.
  * The URL must be valid and doesn't need to be canonicalized. For more information, see [RFC 2396](http://www.ietf.org/rfc/rfc2396.txt).
  * The Evaluate API supports three threatTypes: SOCIAL_ENGINEERING, MALWARE and UNWANTED_SOFTWARE.
  * Deprecated. The `allow_scan` field was used to determine whether Web Risk is allowed to scan the URL provided. This functionality can no longer be disabled in the Evaluate API. See the [Lookup](https://docs.cloud.google.com/web-risk/docs/lookup-api) and [Update](https://docs.cloud.google.com/web-risk/docs/update-api) APIs for crawl-free options.
  * The HTTP `POST` response returns a confidence score for the specified threatType. The confidence score represents the confidence level indicating how risky the specified URL is.



### API request

Before using any of the request data, make the following replacements: 

URL: a URL that needs to be evaluated. 

HTTP method and URL: 
    
    
    POST https://webrisk.googleapis.com/v1eap1:evaluateUri?key=API_KEY

Request JSON body: 
    
    
    {
      "uri": "URL",
      "threatTypes": ["SOCIAL_ENGINEERING", "MALWARE", "UNWANTED_SOFTWARE"]
    }
    

To send your request, choose one of these options:

#### curl

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://webrisk.googleapis.com/v1eap1:evaluateUri?key=API_KEY"

#### PowerShell

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://webrisk.googleapis.com/v1eap1:evaluateUri?key=API_KEY" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "scores": [
        {
          "threatType": "MALWARE",
          "confidenceLevel": "EXTREMELY_HIGH"
        },
        {
          "threatType": "SOCIAL_ENGINEERING",
          "confidenceLevel": "SAFE"
        },
        {
          "threatType": "UNWANTED_SOFTWARE",
          "confidenceLevel": "SAFE"
        }
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
