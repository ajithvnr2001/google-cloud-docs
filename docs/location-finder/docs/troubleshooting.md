---
url: https://docs.cloud.google.com/location-finder/docs/troubleshooting/
title: Troubleshoot Cloud Location Finder \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:39.978368+00:00
---

# Troubleshoot Cloud Location Finder  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/location-finder/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Cloud Location Finder ](https://docs.cloud.google.com/location-finder/docs)
  * [ Guides ](https://docs.cloud.google.com/location-finder/docs/overview)



Send feedback 

#  Troubleshoot Cloud Location Finder Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Cloud Location Finder.

## The API returns a 403 error

The following issue occurs when:

  * Cloud Location Finder isn't enabled in your project
  * You don't have permission for a resource



### Cloud Location Finder isn't enabled in your project
    
    
    {
      "error": {
        "code": 403,
        "message": "Cloud Location Finder API has not been used in project PROJECT_ID before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/cloudlocationfinder.googleapis.com/overview?project=PROJECT_ID then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "SERVICE_DISABLED",
            "domain": "googleapis.com",
            "metadata": {
              "activationUrl": "https://console.developers.google.com/apis/api/cloudlocationfinder.googleapis.com/overview?project=PROJECT_ID",
              "serviceTitle": "Cloud Location Finder API",
              "service": "cloudlocationfinder.googleapis.com",
              "containerInfo": "PROJECT_ID",
              "consumer": "projects/PROJECT_ID"
            }
          },
          {
            "@type": "type.googleapis.com/google.rpc.LocalizedMessage",
            "locale": "en-US",
            "message": "Cloud Location Finder API has not been used in project PROJECT_ID before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/cloudlocationfinder.googleapis.com/overview?project=PROJECT_ID then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry."
          },
          {
            "@type": "type.googleapis.com/google.rpc.Help",
            "links": [
              {
                "description": "Google developers console API activation",
                "url": "https://console.developers.google.com/apis/api/cloudlocationfinder.googleapis.com/overview?project=PROJECT_ID"
              }
            ]
          }
        ]
      }
    }
    

To resolve this issue, enable the Cloud Location Finder API in your project. For instructions, see the [Quickstart](https://docs.cloud.google.com/third_party/devsite/cloud/en/location-finder/docs/quickstart).

### You don't have permission for a resource
    
    
    {
      "error": {
        "code": 403,
        "message": "Permission 'cloudlocationfinder.cloudLocations.list' denied on resource '//cloudlocationfinder.googleapis.com/projects/PROJECT_ID/locations/global' (or it may not exist).",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "IAM_PERMISSION_DENIED",
            "domain": "cloudlocationfinder.googleapis.com",
            "metadata": {
              "resource": "projects/PROJECT_ID/locations/global",
              "permission": "cloudlocationfinder.cloudLocations.list"
            }
          }
        ]
      }
    }
    

To resolve this issue, add the `cloudlocationfinder.viewer` role to projects with resources you want to reference in a query. For instructions, see the [Quickstart](https://docs.cloud.google.com/third_party/devsite/cloud/en/location-finder/docs/quickstart).

## The API returns a 400 error

The following issue occurs when a query is invalid:
    
    
    $ curl -H "Authorization: Bearer $(gcloud auth print-access-token)" 'https://cloudlocationfinder.googleapis.com/v1/projects/PROJECT_ID/locations/global/cloudLocations?filter=cloud_location_type=FAKE_LOCATION'
    {
      "error": {
        "code": 400,
        "message": "Bad usage: Invalid enum name \"FAKE_LOCATION\" for type `cloud.reliability.cloudlocationfinder.storage.CloudLocation.CloudLocationType`.",
        "status": "INVALID_ARGUMENT",
        "details": [
    ...
    }
    

To resolve this issue, review the error message. For guidance on query syntax and acceptable syntax, see the [REST API reference](https://docs.cloud.google.com/third_party/devsite/cloud/en/location-finder/docs/reference/rest).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
