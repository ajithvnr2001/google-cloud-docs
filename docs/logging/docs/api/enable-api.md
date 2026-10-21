---
url: https://docs.cloud.google.com/logging/docs/api/enable-api/
title: Enable the Logging API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:12.340428+00:00
---

# Enable the Logging API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/api/enable-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  Enable the Logging API Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable and authorize use of the Logging API v2.

## Enable the API

The Logging API must be enabled before it can be used. You can check the status of the API and, if necessary, enable it by using either the Google Cloud console or Google Cloud CLI.

###  Google Cloud console 

  1. Go to the Logging API library page in the Google Cloud console:

[Go to the **Library** page](https://console.cloud.google.com/apis/library/logging.googleapis.com)

  2. Select your project.

  3. The Logging API is enabled if you see a **Manage** button on the library page. If you see an **Enable** button, the API isn't enabled, and you must click the **Enable** button to enable it.




###  gcloud CLI 

  1. If you haven't already installed the Google Cloud CLI on your workstation, see [Installing the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  2. To see if the Logging API is enabled, run the following command on your workstation, after replacing PROJECT_ID with the ID of the project for which you want to enable the API:
         
         gcloud services list --project=PROJECT_ID
         

If `logging.googleapis.com` appears in the output, the API is enabled.

  3. If the API isn't enabled, then run the following command to enable it:
         
         gcloud services enable logging --project=PROJECT_ID
         

For more information about managing APIs with gcloud CLI, see [`gcloud services`](https://docs.cloud.google.com/sdk/gcloud/reference/services).




## Authorize use of the API

Before you can use the Cloud Logging API, you must authorize users to access it.

Access to the API is controlled by Identity and Access Management (IAM) roles and permissions. There is a permission associated with each method, and permissions for related methods are clustered into roles, which can then be granted to users. For more information, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

After access to the API is authorized, the API can be used from anywhere. For example, you can use the [entries.list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list) method from your local workstation to read log data from your Google Cloud resources.

The recommended [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries) use [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to automatically find credentials. For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

You can find out more about authentication for Cloud APIs in the [Cloud authentication documentation](https://docs.cloud.google.com/docs/authentication).

## Use client libraries

After you've enabled and authorized the use of the API, you're ready to start writing code. To get started using the Logging client libraries, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
