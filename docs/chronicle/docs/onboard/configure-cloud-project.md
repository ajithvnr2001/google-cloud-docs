---
url: https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project/
title: Configure a Google Cloud project \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:35.050782+00:00
---

# Configure a Google Cloud project  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure a Google Cloud project

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

A Google Cloud project acts as a control layer for the linked Google SecOps instance. It stores customer-specific data such as security telemetry, audit logs, ingestion alerts, and other sensitive instance-level information.

The following sections describe how to configure your Google Cloud project.

## Prerequisites

Each new Google SecOps instance should be linked to a single Google Cloud project. You can either link to an existing Google Cloud project or create a new one, depending on your organizational setup and requirements:

  * We recommend creating a new, dedicated Google Cloud project for each Google SecOps instance. This approach helps isolate sensitive security telemetry and audit data specific to the Google SecOps instance.

To create a new Google Cloud project, see [Create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).

  * If you link your Google SecOps instance to an existing Google Cloud project, review any existing permissions and restrictions that could affect the instance's behavior or access.

For more information, see [Grant permissions to the Google SecOps instance](https://docs.cloud.google.com/chronicle/docs/onboard#grant-permissions).




## Configure a Google Cloud project

The following sections describe how to enable the Chronicle API in the Google Cloud project and configure Essential Contacts.

### Enable the Chronicle API in the Google Cloud project

To allow the Google SecOps instance to read from and write to the linked Google Cloud project, do the following:

  1. Go to the **Manage resources** page in the Google Cloud console. 

[ Go to the Manage Resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. At the top, click the **Project picker** and select your **Organization** resource. 
  3. Select the newly created project.
  4. Go to **APIs & Services**.
  5. Click **\+ ENABLE APIS AND SERVICES**.
  6. Search for **Chronicle API** and select it.
  7. Click **Enable** to enable the Chronicle API for the project.



For more information, see [Enabling an API in your Google Cloud project](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api).

### Configure Essential Contacts

Configure Essential Contacts to receive targeted notifications from Google Cloud. Perform the steps in [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

## New service account in your project

A new service account is added to your project. The service account is managed by Google SecOps and has following attributes:

  * The service account naming pattern is as follows, where the `PROJECT_NUMBER` is unique to the project:

`service-PROJECT_NUMBER@gcp-sa-chronicle.iam.gserviceaccount.com`

  * The account has the **Chronicle Service Agent** role.

  * An IAM permission is granted to the project.

To see details of the IAM permission, do the following:

    1. Go to the **IAM** page of your Google Cloud project.
    2. At the top right, select the **Include Google-provided role grants** checkbox.

If you don't see the new service account, check that the **Include Google-provided role grants** button is enabled on the IAM page.




## Impact of updating a linked Google Cloud project

When you update the Google Cloud project linked to your Google Cloud instance, it impacts specific data ingestion paths. Feeds with the source-types AMAZON_S3_V2, AMAZON_SQS_V2, GOOGLE_CLOUD_STORAGE_V2, AZURE_BLOBSTORAGE_V2, and AZURE_EVENT_HUB, stop ingesting live data upon migration. You must re-create them from Feeds UI/API post migration to resume data ingestion. All other feed types continue to operate without interruption and require no manual intervention.

Impacted feeds created prior to the migration transition to a read-only state. This update also affects SOAR functionality and specific resources such as Cloud Storage buckets, service accounts, and secrets.

If your Google SecOps instance authenticates with a third-party identity provider (IdP), you must also configure the IdP in the new Google Cloud project. To set up a third-party IdP, see [Configure a third-party identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

For more information, see [Impact of changing your linked Cloud project](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#impact_of_changing_your_linked_cloud_project_on_data_feeds).

## What's next

After completing the steps in this document, perform the following:

  * Apply security and compliance controls to the project to satisfy your business use case and organization policies. For more information about how to do this, see the [Assured Workloads documentation](https://docs.cloud.google.com/assured-workloads/docs/overview). 

**Note:** Compliance restrictions required by your Google Cloud organization are not applied by default. You must configure them manually.
  * Integrate your Google SecOps instance with an Identity Provider (IdP), either [Cloud identity](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication) or a [third-party identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

  * The Google Cloud project serves as a control layer for you to do the following:

    * Enable, inspect, and manage access to audit logs generated by Google SecOps and stored in Cloud Audit Logs.
    * Set up custom ingestion outage alerts using Cloud Monitoring.
    * Store exported historical data. 

Enable Google SecOps audit logging by following the steps in [Google Security Operations audit logging information](https://docs.cloud.google.com/chronicle/docs/preview/audit-logging/audit-logging). Google SecOps writes Data Access and Admin Activity logs to the project. 

**Note:** You cannot disable Data Access logging using the Google Cloud console. To request to disable it, contact your Google SecOps representative.**Important:** If audit logging was previously enabled using the steps in the Google SecOps audit logging guide, when you complete the steps in this document, the log output redirects to the new Google Security Operations-bound project.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
