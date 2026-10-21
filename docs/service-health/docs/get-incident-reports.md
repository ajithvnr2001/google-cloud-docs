---
url: https://docs.cloud.google.com/service-health/docs/get-incident-reports/
title: Get incident reports \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:17.018568+00:00
---

# Get incident reports  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/get-incident-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Get incident reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to get the incident report for a Google Cloud incident using the Service Health API.

Incident reports are available for incidents that meet the following conditions:

  * The incident has global impact or is affecting a significant percentage of customer projects across one or more regions.
  * One or more products are unavailable or severely degraded.
  * Twenty four hours before the start of the incident, you have [enabled the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#enable-service-health-api-single-project).



## Before you begin

  * Set [permissions to access the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#access-service-health-api-dashboard).
  * Get the event ID of the incident that you want to check for an incident report. You can [get a list of closed incidents](https://docs.cloud.google.com/service-health/docs/list-events) and find the ID of the incident.



## Get the ID for the incident report

To get the incident report for an incident:

  1. [Get the details](https://docs.cloud.google.com/service-health/docs/project-events#get_incident_details) for the incident.
  2. Look for the following line in the JSON response:
         
         "artifact": "projects/PROJECT_ID/locations/global/artifacts/ARTIFACT_ID",
         

  3. Take note of the ARTIFACT_ID.




## Get the content of the incident report

You can use the Get API to get the content of the incident report.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * ARTIFACT_ID: the ID of the incident report.



HTTP method and URL: 
    
    
    GET https://servicehealth.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/artifacts/ARTIFACT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://servicehealth.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/artifacts/ARTIFACT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://servicehealth.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/artifacts/ARTIFACT_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/artifacts/ARTIFACT_ID",
      "content": {
          "markdown": "Content of the incident report.",
        },
      "category": "ARTIFACT_CATEGORY_INCIDENT_REPORT",
      "createTime": "2022-10-18T18:00:05.690761Z",
      "updateTime": "2022-10-18T17:41:20.112287Z",
    }
    

If you don't have the permissions to get incident reports, you will get the following `PERMISSION_DENIED` error.
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'servicehealth.artifacts.get' denied on resource '//servicehealth.googleapis.com/projects/PROJECT_ID/locations/global/artifacts/ARTIFACT_ID' (or it may not exist).",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "IAM_PERMISSION_DENIED",
            "domain": "servicehealth.googleapis.com",
            "metadata": {
              "resource": "projects/PROJECT_ID/locations/global/artifacts/ARTIFACT_ID",
              "permission": "servicehealth.artifacts.get"
            }
          }
        ]
      }
    }
    

To fix the error, set the [required permissions](https://docs.cloud.google.com/service-health/docs/manage-access#access-service-health-api-dashboard).

## Retrieve a list of incident reports

You can use the `ListArtifacts` method to get a list of incident reports.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.



HTTP method and URL: 
    
    
    GET https://servicehealth.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/artifacts

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://servicehealth.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/artifacts"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://servicehealth.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/artifacts" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "artifacts": [
        {
          "name": "projects/PROJECT_ID/locations/global/artifacts/b2a4600f-33fb-4d33-a3ad-f43c8b8f2a3a",
          "content": {
              "markdown": "Content of the incident report.",
            },
          "category": "ARTIFACT_CATEGORY_INCIDENT_REPORT",
          "createTime": "2022-10-18T17:41:20.112287Z",
          "updateTime": "2022-10-18T18:00:05.690761Z",
        }
      ],
      "nextPageToken": "ABCREGI=",
      "unreachable": []
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
