---
url: https://docs.cloud.google.com/web-risk/docs/submission-api-legacy/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:16.963641+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/submission-api-legacy/




Stay organized with collections  Save and categorize content based on your preferences. 

Using the Submission API

# Using the Submission API

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to use the Submission API to submit URLs that you suspect are unsafe to Safe Browsing for analysis. Any URLs that are confirmed to match the [Safe Browsing policies](https://safebrowsing.google.com/#policies) are added to the Safe Browsing service.

## Before you begin

[Contact our sales team](https://go.chronicle.security/webriskapi) or your customer engineer to obtain access to this feature.

## Submitting URLs

To submit a URL, send an HTTP `POST` request to the [`projects.submissions.create`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.submissions/create) method.

### API request

Before using any of the request data, make the following replacements: 

PROJECT_ID: your Google Cloud project ID 

HTTP method and URL: 
    
    
    POST https://webrisk.googleapis.com/v1/projects/PROJECT-ID/submissions

Request JSON body: 
    
    
    {
      "uri": "https://www.phishingsite.com/",
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://webrisk.googleapis.com/v1/projects/PROJECT-ID/submissions"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://webrisk.googleapis.com/v1/projects/PROJECT-ID/submissions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "uri": "https://www.phishingsite.com/",
    }
    

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
