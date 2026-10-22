---
url: https://docs.cloud.google.com/chronicle/docs/administration/migrate-instance-from-one-project-to-another/
title: Migrate a Google SecOps instance to a BYOP project \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:46.598156+00:00
---

# Migrate a Google SecOps instance to a BYOP project  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/migrate-instance-from-one-project-to-another/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate a Google SecOps instance to a BYOP project

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide helps Google Cloud administrators and security engineers to migrate an existing Google SecOps instance, including its data, to a different Google Cloud project using the Bring Your Own Project (BYOP) model. This process helps you consolidate resources, realign billing, or adapt to organizational changes while preserving your security data and instance configuration.

## Key terminology

  * Bring Your Own Project (BYOP): A model where you use your own Google Cloud project to host and manage the Google SecOps instance.
  * Proof of Concept (POC): A non-production instance used for evaluation or testing.
  * Technical Point of Contact (TPOC): The designated contact person in your organization for technical communications regarding the migration.



## Before you begin

Before starting the migration, confirm that the target Google Cloud project meets the following requirements:

  * Permissions: To perform a self-service migration for a POC instance, you must have the IAM role `chroniclesm.admin`, which includes the `chroniclesm.projectLink.enable` permission.

  * Billing account: You **must** link the Google SecOps instance to a target BYOP project that uses the same Google Cloud billing account as the original project. Confirm that the billing account subscription is active.

    * [Find a Cloud Billing account ID](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-id)
    * [Manage your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account)
    * [Confirm the status of the linked Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#billing_account_status)
  * Project availability: You can use an existing or a new Google Cloud project as the target:

    * Existing project: Confirm it's a valid Google Cloud project and not already linked to an active Google SecOps instance.
    * New project: Configure the project as described in [Configure a Google Cloud project for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project).
  * Organization policies: If the current Google Cloud project has active organization policies, such as [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), CMEK, FedRAMP, or other compliance frameworks, contact [Google SecOps Support](https://console.cloud.google.com/support) for assistance _before_ initiating the migration.

  * Chronicle API: Enable the Chronicle API in the target Google Cloud project. For more information, see [Enable the Chronicle API](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project#enable-chronicle-api-in-proj).

  * Authentication (BYOID only): If your instance uses Bring Your Own Identity (BYOID), configure the workforce pool in the target project. For more information, see [Configure a third-party identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

  * SCC-E associations: If your Google SecOps instance is linked to Security Command Center Enterprise (SCC-E), BYOP project migration is not supported. Contact [Google SecOps Support](https://console.cloud.google.com/support) for assistance.

  * Downtime: Be aware that the migration process requires downtime. To maintain data integrity, the Google SecOps instance and its APIs are temporarily unavailable and return an HTTP 503 error. Ingestion and feeds are also affected.




## Migrate the instance to a BYOP project

The migration process depends on whether you are migrating a POC instance or a non-POC production instance.

### Migrate a POC to a production BYOP

If you are moving from a POC to a full production environment, you can initiate the migration yourself. This process starts automatically when your new production contract begins. Your designated TPOC receives a contract start notification email with a setup link.

Follow the instructions in [Link a Google SecOps instance to a new subscription](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud#instance-to-new-subscription), specifically the subsection [To link an existing POC Google SecOps instance to a new subscription](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud#link-existing-poc).

### Migrate a non-POC project to a BYOP

For non-POC projects, such as for internal organization restructuring or Managed Service Provider (MSP) transitions, [Google SecOps Support](https://console.cloud.google.com/support) manages the migration.

  1. Initiate the request: Open a standard support ticket to request the project migration. Include details such as whether you have a new subscription and want to change the linked Google Cloud project for the Google SecOps instance.
  2. Migration process: Google SecOps Support triggers the update. You don't need to take any action in the console. Automated status emails are sent to your team as the migration progresses.



## During the migration process

A brief maintenance window is required to move your instance to the target project and maintain data integrity.

  * During the critical phase, your Google SecOps instance and its APIs are temporarily unavailable and return an **HTTP 503 (Service Unavailable)** error. This is expected. Normal service resumes automatically when the project update completes.
  * For more information on how data feeds are affected, see [Impact of changing your linked Cloud Project on data feeds](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#impact_of_changing_your_linked_cloud_project_on_data_feeds).



## Complete post-migration actions

After you receive the migration completion notification email, your TPOC must perform the following actions to restore full functionality:

  * Configure authorization: Set up all required IAM authorization rules on the target project. For more information, see [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).

  * Recreate specific ingestion feeds:

    * Automatically migrated feeds: Most ingestion feeds are automatically migrated and require no action. This includes the following STS feeds, which are automatically relinked and enabled:

      * Non-FedAuth AMAZON_S3_V2
      * Non-FedAuth AMAZON_SQS_V2
      * Non-FedAuth AZURE_BLOBSTORE_V2
    * Feeds requiring manual recreation: You must delete and manually recreate the following feeds in the target environment because they are disabled post-migration. Follow the steps in [Required actions for customers](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#required_actions_for_customers):

      * [GOOGLE_CLOUD_STORAGE_V2](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#gc-storage-v2)
      * [GOOGLE_CLOUD_STORAGE_EVENT_DRIVEN](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#gcs-edt)
      * Any STS feeds using Federated Authentication (FedAuth) (due to trust policy changes associated with the new project number).
  * Verify other ingestion: Confirm that all other ingestion mechanisms are working as expected. Contact [Google SecOps Support](https://console.cloud.google.com/support) if you encounter issues.

  * BigQuery data: If you store data in BigQuery associated with the _old_ project, contact [Google SecOps Support](https://console.cloud.google.com/support) to help migrate this data to the target project.

  * Update automations: Reconfigure any external automations or scripts that rely on the Chronicle API. Update them with the target project ID, generate new API keys, and create any necessary service accounts in the target project.

  * Migrate POC data: If you migrated an existing POC instance to a new subscription, contact [Google SecOps Support](https://console.cloud.google.com/support) or your Google representative to assist with migrating the POC data after activation.




## Troubleshooting

  * HTTP 503 Error: This error is expected during the migration window, as mentioned in the During the migration process section. Service should be restored automatically upon completion.
  * Feed issues: If feeds other than the ones listed for manual recreation are not working post-migration, contact [Google SecOps Support](https://console.cloud.google.com/support).
  * Permission errors: Double-check the IAM roles and permissions in the _target_ project.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
