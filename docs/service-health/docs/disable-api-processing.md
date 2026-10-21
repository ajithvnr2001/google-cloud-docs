---
url: https://docs.cloud.google.com/service-health/docs/disable-api-processing/
title: Disable the Service Health API and processing \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:51.214801+00:00
---

# Disable the Service Health API and processing  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/disable-api-processing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Disable the Service Health API and processing Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to disable the Service Health API and stop event and log processing.

You can disable the Service Health API through the Google Cloud console or Google Cloud CLI. Event and log processing may take up to 24 hours to stop.

To disable the API through the Google Cloud console:

  1. In the APIs and Services library, go to the [Service Health API](https://console.cloud.google.com/apis/library/servicehealth.googleapis.com).

Alternatively, you can go to the [API Library](https://console.cloud.google.com/apis/library) and search "Service Health API".

  2. Select the project.

  3. Select the **DISABLE API** button.




To disable the API using the gcloud CLI:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI if you have not already done so.

  2. Disable the Service Health API.
         
         gcloud services disable servicehealth.googleapis.com  --project PROJECT_ID
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
