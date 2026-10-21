---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission/
title: Grant service account roles for Managed Service for Apache Spark \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:36.683116+00:00
---

# Grant service account roles for Managed Service for Apache Spark  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Grant service account roles for Managed Service for Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant the [Service Account User](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) role on Managed Service for Apache Spark Service Account to Cloud Data Fusion Service Agent to allow it to provision and run pipelines on Managed Service for Apache Spark clusters.

For service accounts that are used by Managed Service for Apache Spark, you also need to grant `datafusion.instances.runtime` permission to access Cloud Data Fusion runtime resources.

**Note:** Starting in Cloud Data Fusion versions 6.2.3, you can grant these permissions in the UI when you create an instance.  
To get the permissions that you need to create a Cloud Data Fusion instance, ask your administrator to grant you the [Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) IAM role on the Managed Service for Apache Spark service account.

Whether you use a user-managed service account, or the default Compute Engine service account on the virtual machines in a cluster, you must grant the Service Account User role to Cloud Data Fusion. Otherwise, Cloud Data Fusion cannot provision a Managed Service for Apache Spark cluster and the following error appears when you execute a data pipeline:

`PROVISION task failed in REQUESTING_CREATE state for program run [pipeline-name] due to Managed Service for Apache Spark operation failure: INVALID_ARGUMENT: User not authorized to act as service account '[service-account-name]'`

## Get the service account name

  1. In the Google Cloud console, go to the Identity and Access Management page.  
[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)
  2. From the project selector at the top of the page, choose the project, folder, or organization to which the Cloud Data Fusion instance belongs.
  3. Find and copy the [Cloud Data Fusion service account](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts#service_account_table) name. Use the following format: `service-[project-number]@gcp-sa-datafusion.iam.gserviceaccount.com`.



## Give service account user permission

  1. In the Google Cloud console, go to the **Service Accounts** page.  
[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)
  2. Click **Select a project** , choose a project where the service account you want to use for the Managed Service for Apache Spark cluster is located, and then click **Open**.
  3. Click the email address of the [Managed Service for Apache Spark service account](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts).

When Cloud Data Fusion provisions a Managed Service for Apache Spark cluster, you can specify which user-managed service account to use for the Managed Service for Apache Spark virtual machines in that cluster. If a service account is not specified, the default Compute Engine service account is used, which is in the format of `[project-number]-compute@developer.gserviceaccount.com`.
  4. Click the **Principals with access** tab. The page displays a list of principals that have been granted roles on the service account.

  5. Click person_add **Grant access**.

  6. In the **New principals** field, paste the Cloud Data Fusion service account name that you previously copied.

  7. Select the **Service Account User** role.

![Service account user](https://docs.cloud.google.com/data-fusion/docs/images/how-to/select-service-account-user-role.png)

  8. Click **Save**.




## Grant roles to Managed Service for Apache Spark service accounts

### Grant runner role permission

Grant the [Cloud Data Fusion runner role](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion) (`roles/datafusion.runner`) to service accounts that are used by Managed Service for Apache Spark. This authorizes the Managed Service for Apache Spark service account to run Cloud Data Fusion pipelines in your [project](https://docs.cloud.google.com/data-fusion/docs/concepts/security#projects). For more information, see [Requiring permission to attach service accounts to resources](https://docs.cloud.google.com/iam/docs/service-accounts-actas).

### Grant Cloud Storage admin permission

In Cloud Data Fusion versions 6.2.0 and above, grant the [Cloud Storage admin role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) (`roles/storage.admin`) to service accounts that are used by Managed Service for Apache Spark in your [project](https://docs.cloud.google.com/data-fusion/docs/concepts/security#projects).

## What's next

  * Learn more about [Access control](https://docs.cloud.google.com/data-fusion/docs/access-control) in Cloud Data Fusion.
  * Learn more about Cloud Data Fusion [service accounts](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
