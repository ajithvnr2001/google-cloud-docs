---
url: https://docs.cloud.google.com/service-health/docs/project-events/
title: Manage events for a project \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:08.667066+00:00
---

# Manage events for a project  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/project-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Manage events for a project Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how-tos for using the Service Health API to manage events affecting a single project.

## Before you begin

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  1. [Enable the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#enable-service-health-api-single-project) for the project you want to manage events for.
  2. Set [permissions to access the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#access-service-health-api-dashboard).



## References

See the Events API reference ([v1](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/projects.locations.events), [v1beta](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/projects.locations.events)) for the methods you can use and the meaning of the fields in the responses. In the API response, each entry in the `impact` list includes the granular disruption `state` (`AFFECTED` or `RESOLVED`), `startTime`, and `endTime` (when resolved) for each impacted product and location.

When setting the product or location, use the values found at [Google Cloud products](https://docs.cloud.google.com/service-health/docs/supported-products-locations) and [locations](https://docs.cloud.google.com/service-health/docs/supported-products-locations#locations).

## List all active incidents for a project

See the [quickstart](https://docs.cloud.google.com/service-health/docs/list-events#list_all_active_incidents_for_a_project).

## Get incident details

You can use the Get API to view detailed information about an event.

Before using any of the request data, make the following replacements: 

  * API_VERSION: The API version to use. Use `v1` or `v1beta`.
  * PROJECT_ID: your Google Cloud project ID.
  * EVENT_ID: the ID of the event.



HTTP method and URL: 
    
    
    GET https://servicehealth.googleapis.com/API VERSION/projects/PROJECT_ID/locations/global/events/EVENT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://servicehealth.googleapis.com/API VERSION/projects/PROJECT_ID/locations/global/events/EVENT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://servicehealth.googleapis.com/API VERSION/projects/PROJECT_ID/locations/global/events/EVENT_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/events/EVENT_ID",
          "title": "We are experiencing a connectivity issue affecting Google Cloud SQL in us-east1, australia-southeast2.",
          "description": "The issue with Google Cloud SQL has been resolved for all affected projects as of Tuesday, 2022-10-18 11:00 US/Pacific. We thank you for your patience while we worked on resolving the issue.",
          "category": "INCIDENT",
          "detailedCategory": "CONFIRMED_INCIDENT",
          "state": "CLOSED",
          "detailedState": "RESOLVED",
          "artifacts": [
            {
              "artifact": "projects/PROJECT_ID/locations/global/artifacts/artifact_id",
              "artifactCategory": "ARTIFACT_CATEGORY_INCIDENT_REPORT",
            }
          ],
          "eventImpacts": [
            {
              "product": {
                "productName": "Google Cloud SQL",
                "id": "hV87iK5DcEXKgWU2kDri",
              },
              "location": {
                "locationName": "us-central1",
              }
            }
          ],
          "relevance": "RELATED",
       "updates": [
        {
          "updateTime": "2022-10-18T17:41:20.112287Z",
                  "title": "We are experiencing a connectivity issue affecting Google Cloud SQL in us-east1, australia-southeast2.",
          "description": "We are experiencing an intermittent issue with Google Cloud SQL. Our engineering team continues to investigate the issue.",
          "symptom": "None at this time.",
          "workaround": "None at this time."
        },
        {
          "updateTime": "2022-10-18T18:00:05.690761Z",
          "title": "We are experiencing a connectivity issue affecting Google Cloud SQL in us-east1, australia-southeast2.",
          "description": "The issue with Google Cloud SQL has been resolved for all affected projects as of Tuesday, 2022-10-18 11:00 US/Pacific.\n\nWe thank you for your patience while we worked on resolving the issue.",
          "symptom": "None at this time.",
          "workaround": "None at this time."
        }
      ],
      "updateTime": "2022-10-18T18:00:05.690761Z",
      "startTime": "2022-10-18T17:41:20.112287Z",
      "endTime":  "2022-10-18T18:00:05.690761Z",
    }
    

If you don't have the permissions to get events, you will get the following `PERMISSION_DENIED` error.
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'servicehealth.events.get' denied on resource '//servicehealth.googleapis.com/projects/PROJECT_ID/locations/global/events/EVENT_ID' (or it may not exist).",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "IAM_PERMISSION_DENIED",
            "domain": "servicehealth.googleapis.com",
            "metadata": {
              "resource": "projects/PROJECT_ID/locations/global/events/EVENT_ID",
              "permission": "servicehealth.events.get"
            }
          }
        ]
      }
    }
    

To fix the error, set the [required permissions](https://docs.cloud.google.com/service-health/docs/manage-access#access-service-health-api-dashboard).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
