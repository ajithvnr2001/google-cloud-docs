---
url: https://docs.cloud.google.com/looker/docs/looker-core-service-account/
title: The Looker service account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:31.707373+00:00
---

# The Looker service account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  The Looker service account Stay organized with collections  Save and categorize content based on your preferences. 

Looker (Google Cloud core) uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), called a _Looker service account_ , to perform certain activities. A single Looker service account works on behalf of all Looker (Google Cloud core) instances in a given Google Cloud project. The Looker service account is automatically created the first time a Looker (Google Cloud core) instance is created in a project.

The service account allows Looker (Google Cloud core) to connect to other services, such as [BigQuery](https://docs.cloud.google.com/looker/docs/looker-core-dialects#using-application-default-credentials-to-connect-to-a).

**Note:** To enhance data security, Google is deprecating the legacy Looker Service Agent role (`roles/looker.serviceAgent`) in favor of a scoped-down role (`roles/looker.restrictedServiceAgent`). If your instance connects to BigQuery, you must grant explicit BigQuery permissions before the legacy role is retired. For more information, see the [Security update for Looker (Google Cloud core) service agent permissions](https://docs.cloud.google.com/looker/docs/best-practices/service-agent-permissions-notice) best practices page.

Sometimes, such as when you're using [Application Default Credentials (ADC) with a connection to BigQuery in another project](https://docs.cloud.google.com/looker/docs/looker-core-dialects#adc-different-project), you need to view information about the Looker service account, such as its email address.

Or, if you are planning to use [CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek) and are going to use the Google Cloud CLI, Terraform, or the API to configure CMEK before you create the Looker (Google Cloud core) instance, you must create the Looker service account manually _before_ you create the instance.

**Note:** You need to manually create a Looker service account only if you use the Google Cloud CLI, Terraform, or the API to configure CMEK and a Looker service account hasn't already been created for your project.

To view or create the Looker service account, select one of the following options:

### console

To view the Looker service account:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)
  2. Select the project that the Looker (Google Cloud core) instance resides in.
  3. Select the **Include Google-provided role grants** checkbox.



###  gcloud 

To create or view the Looker service account:
    
    
    
    gcloud beta services identity create --service=looker.googleapis.com --project=PROJECT_ID
    
    

Replace `PROJECT_ID` with the project that the Looker (Google Cloud core) instance resides in.

The service account name will be `Looker Service Account`. The email will have the format `service-<project number>@gcp-sa-looker.iam.gserviceaccount.com`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
