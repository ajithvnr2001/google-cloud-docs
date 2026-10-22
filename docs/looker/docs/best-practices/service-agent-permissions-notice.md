---
url: https://docs.cloud.google.com/looker/docs/best-practices/service-agent-permissions-notice/
title: Security update for Looker (Google Cloud core) service agent permissions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:35.552767+00:00
---

# Security update for Looker (Google Cloud core) service agent permissions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/service-agent-permissions-notice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Security update for Looker (Google Cloud core) service agent permissions Stay organized with collections  Save and categorize content based on your preferences. 

This document provides details about a security update regarding the default IAM permissions assigned to the Looker (Google Cloud core) service agent.

To adhere to the principle of least privilege and enhance the security of your data, Google is deprecating the legacy Looker Service Agent role ([`roles/looker.serviceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.serviceAgent)) and replacing it with a new, scoped-down role ([`roles/looker.restrictedServiceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.restrictedServiceAgent)).

The legacy role grants broad BigQuery permissions by default, which can allow Looker administrators to execute data modification queries using the Looker SQL Runner. To mitigate this risk, Google has proactively attached the new restricted role to your existing Looker service accounts. However, **you must take manual action** to re-grant necessary BigQuery permissions before the legacy role is permanently retired.

## What you need to do

To ensure that your Looker workflows and persistent derived tables (PDTs) continue to function without interruption, complete the following steps before the legacy role is deprecated on **January 11, 2027** :

### 1\. Grant explicit BigQuery permissions

If your Looker instance relies on BigQuery, you must explicitly grant the required BigQuery roles to your Looker service agent:

`service-PROJECT_NUMBER@gcp-sa-looker.iam.gserviceaccount.com`

Replace `PROJECT_NUMBER` with your Google Cloud project number.

At a minimum, grant the following roles:

  * **[BigQuery Job User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser)** (`roles/bigquery.jobUser`): Grant this role on your designated billing project to allow query execution.
  * **[BigQuery Data Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer)** (`roles/bigquery.dataViewer`): Grant this role on the specific projects where your data resides.
  * **[BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor)** (`roles/bigquery.dataEditor`): Grant this role on the specific dataset or project that's used for PDTs (if your instance builds PDTs).



Alternatively, you can configure the Looker service agent to [impersonate a dedicated service account](https://docs.cloud.google.com/iam/docs/service-account-impersonation) that holds these specific permissions.

### 2\. Remove the legacy role

After granting the explicit BigQuery permissions, manually remove the legacy `roles/looker.serviceAgent` role binding from your Looker service agent in the Google Cloud console:

  1. In the Google Cloud console, go to the **IAM** page.
  2. Locate your Looker service agent (`service-PROJECT_NUMBER@gcp-sa-looker.iam.gserviceaccount.com`).
  3. Remove the legacy `roles/looker.serviceAgent` role binding.

**Note:** In the Google Cloud console IAM page, both the legacy and restricted roles might be displayed as **Looker Service Agent**. Review the role description or the underlying role ID to ensure that you are removing the legacy role (`roles/looker.serviceAgent`) and keeping the restricted role (`roles/looker.restrictedServiceAgent`).

## Impact of inaction

If you don't grant explicit BigQuery roles and the legacy role is automatically deprecated on **January 11, 2027** , your Looker instance might lose the ability to run BigQuery jobs, which will result in interrupted queries, failing dashboards, and broken PDT builds.

## Need help?

For detailed instructions about configuring BigQuery permissions for Looker, see the [Google BigQuery documentation](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery).

If you have questions or require assistance during this migration, contact [Google Cloud Support](https://cloud.google.com/support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
