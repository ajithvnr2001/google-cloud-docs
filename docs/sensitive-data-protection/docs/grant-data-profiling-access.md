---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access/
title: Grant discovery access to a service agent \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:04.501976+00:00
---

# Grant discovery access to a service agent  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Grant discovery access to a service agent Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant the required role to a service agent so that it can be used to profile data at the organization or folder level.

Perform these tasks if both of the following conditions apply:

  * You created a scan configuration at the organization or folder level.
  * Sensitive Data Protection isn't generating any data profiles for the scan configuration. When you [view configuration errors](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-scan-configurations#view-errors), you see the following error message:
        
        None of the driver projects (PROJECT_ID) have MISSING_PERMISSION
        permission for organizations/ORGANIZATION_ID.




## Get the ID of the service agent

Get the service agent ID that is associated with your scan configuration:

  1. Go to the discovery scan configurations list.

[Go to discovery scan configurations](https://console.cloud.google.com/security/sensitive-data-protection/landing/configuration/dataProfiles/configurations;source=7)

  2. On the toolbar, select your organization.
  3. Select your scan configuration.
  4. On the **Scan configuration details** page, copy the value of the **Service agent** field. The service agent ID is in the format of an email address.



Give your service agent ID to a Google Cloud administrator, who must then [grant data profiling access](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access#grant-roles-org) to the service agent.

## Grant data profiling access

This section describes how to grant access to a service agent so that it can be used to profile data at the organization or folder level.

Only someone who has the [permissions to grant IAM roles to a service agent](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#permissions-to-grant-profiling-access), such as a Google Cloud administrator, can perform these steps.

To complete these steps, you need the [ID of the service agent](https://docs.cloud.google.com/sensitive-data-protection/docs/grant-data-profiling-access#get-sa-id) that you want to grant data profiling access to.

To grant data profiling access at the organization or folder level, follow these steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. On the toolbar, select your organization.

  3. Click person_add **Grant access**.

  4. In the **New principals** field, enter the service agent ID.

  5. In the **Select a role** field, enter and select **DLP Organization Data Profiles Driver**.

  6. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
