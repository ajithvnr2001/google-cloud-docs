---
url: https://docs.cloud.google.com/service-health/docs/troubleshooting/
title: Troubleshoot common issues in Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:10.763181+00:00
---

# Troubleshoot common issues in Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Troubleshoot common issues in Personalized Service Health Stay organized with collections  Save and categorize content based on your preferences. 

This document describes issues you may encounter in using Personalized Service Health and how to resolve them.

## The API is throwing a 403 error

If you access the API when it is not enabled, you will receive the following error message:
    
    
    {
      "error": {
        "code": 403,
        "message": "Service Health API has not been used in project PROJECT_ID before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/servicehealth.googleapis.com/overview?project=PROJECT_ID then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.",
        "status": "PERMISSION_DENIED",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.Help",
            "links": [
              {
                "description": "Google developers console API activation",
                "url": "https://console.developers.google.com/apis/api/servicehealth.googleapis.com/overview?project=PROJECT_ID"
              }
            ]
          },
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "SERVICE_DISABLED",
            "domain": "googleapis.com",
            "metadata": {
              "consumer": "projects/PROJECT_ID",
              "service": "servicehealth.googleapis.com"
            }
          }
        ]
      }
    }
    

## An alert was not fired for a new incident

Personalized Service Health won't send a notification if an incident has a relevance of **Unknown**. Alternatively, your alert policy may be misconfigured.

## Give feedback, request features, or report issues

  1. Navigate to the **Help** button in the Google Cloud console global navigation bar.
  2. Select **Send feedback**.
  3. Write feedback, suggest features, or report an issue.
  4. (Optional) Include a screenshot.
  5. Select **Send**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
