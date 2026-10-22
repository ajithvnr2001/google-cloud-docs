---
url: https://docs.cloud.google.com/migration-center/docs/get-started-with-migration-center/
title: Get started with Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:57.605099+00:00
---

# Get started with Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/get-started-with-migration-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Get started with Migration Center Stay organized with collections  Save and categorize content based on your preferences. 

To start using Google Cloud Migration Center, you need to create an [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) and a project in Google Cloud, and you need to activate Migration Center.

This document explains the different options you have to create a project, and how to activate Migration Center.

## Before you begin

  1. To use the Google Cloud console, you need a Google Account. To learn how to create a new Google Account, or to learn how to use an existing email address to create a new Google Account, see [Create a Google Account](https://support.google.com/accounts/answer/27441).



## Choose the right path to create a project

If you're new to Google Cloud, create a Google Cloud account and take advantage of the [Free Trial and Google Cloud Free Tier products](https://docs.cloud.google.com/free/docs/free-cloud-features) to get started with Google Cloud. You can use Migration Center to run a cost estimate and to create an assessment at no cost.

If you're working with a Google Cloud partner and want to perform an assessment, but don't have a Google Cloud organization, you have the following options:

  * **Use your partner's organization**. You can ask your Google Cloud partner to create a project for you in their Google Cloud organization.
  * **Request an Enterprise Trial**. You can ask your Google Cloud partner to obtain an Enterprise Trial for you. An Enterprise Trial provides you with a Google Cloud organization and project with no sign-up required, no payment card associated with the account, and with additional credits to start using other Google Cloud products.

**Note:** Google Cloud customer engineers have administrator access to the Enterprise Trial organization. To use an Enterprise Trial, you need to accept the terms and conditions.

If you already have an organization on Google Cloud, you can start using Migration Center immediately at no extra cost. You can create a new project to perform a cost estimation and run an assessment directly in Migration Center. You can also take advantage of a connected [StratoZone account](https://docs.cloud.google.com/migrate/stratozone/docs/about-stratozone) to perform additional assessments at no extra cost. If you need help and your organization policies allow, you can add your Google Cloud customer engineer to the project and let them handle the assessment.

Finally, if you already have an organization on Google Cloud, but cannot add your Google Cloud customer engineer due to your organization policies, request an Enterprise Trial.

The following diagram can help you decide the right path for you.

![Enterprise Trials diagram](https://docs.cloud.google.com/static/migration-center/images/enterprise-trials-diagram.svg)

## Activate Migration Center

The first time you access Google Cloud Migration Center from a Google Cloud project in the Google Cloud console, you need to activate Migration Center. However, if you want to generate a rapid, offline cost estimate, you can do this directly from the **Estimate cost** page without activating Migration Center. For more information, see [Start a cost estimation](https://docs.cloud.google.com/migration-center/docs/estimate/start-estimation).

#### Permissions required for this task

Review the [permissions required to activate Migration Center](https://docs.cloud.google.com/migration-center/docs/roles-and-permissions#activate). 

To activate Migration Center, follow these steps:

  1. In the Google Cloud console, go to the Migration Center page.

[Go to Migration Center](https://console.cloud.google.com/migration?gtm_source=documentation&gtm_source_id=activate_migration_center_migration_center)

  2. If prompted, to enable the required APIs for Migration Center, click **Enable APIs**.

  3. From the **Region** list, select the region where you want Migration Center to store and process the information about your migrations. For the full list of available regions, see [Migration Center locations](https://docs.cloud.google.com/migration-center/docs/locations).

**Note:** The region you select cannot be changed later.
  4. If you already have an Expert Request number provided by Google, enter it in the **Expert Request number** field, without the `ER-` prefix, then click **Next**. If you don't have an Expert Request number, click **Skip**.

  5. To accept the default migration preferences, click **Next**. You can edit or add migration preferences later.

  6. To confirm your activation, click **Continue**.




## Grant access to Google customer engineers

If you want to let Google Cloud customer engineers access your Migration Center project to help you with your migration, you must first give your consent by accepting the [terms and conditions](https://cloud.google.com/terms/migration-center). Do the following:

  1. In the Google Cloud console, go to the Migration Center page.

[Go to Migration Center](https://console.cloud.google.com/migration?gtm_source=documentation&gtm_source_id=ce_consent)

  2. Click settings **Configure Migration Center**.

  3. Click **Approve Google Cloud customer engineer access**. A dialog opens with the terms and conditions.

  4. Read the terms and conditions, then click **Accept**.




After you accept the terms and conditions agreement, you must give the appropriate permissions to your Google Cloud customer engineer. For more information, see the [list of permissions to give](https://docs.cloud.google.com/migration-center/docs/roles-and-permissions#manage).

## Update your Expert Request number

To update your Expert Request number after activating Migration Center, follow these steps:

  1. In the Google Cloud console, go to the Migration Center page.

[Go to Migration Center](https://console.cloud.google.com/migration?gtm_source=documentation&gtm_source_id=activate_migration_center_migration_center)

  2. Click settings **Configure Migration Center**.

  3. Select **I have an Expert Request number**.

  4. In the field that appears, enter your Expert Request number, without the `ER-` prefix.

  5. Click **Save**.




## (Optional) Enable a service perimeter

With VPC Service Controls, you can configure service perimeters around the Migration Center resources and control the movement of data across the perimeter boundary.

To learn how to enable a service perimeter, see [Secure your data with a service perimeter](https://docs.cloud.google.com/migration-center/docs/service-perimeter).

## Add users to your project

To let other users access your Google Cloud project, for example if you want a Google customer engineer to help you with your assessment, grant them the [permissions required to manage resources](https://docs.cloud.google.com/migration-center/docs/roles-and-permissions#manage_resources) in Migration Center.

Additional users must create their own Google Account before you can add them to your project. If you encounter issues, see how to [troubleshoot common login problems](https://docs.cloud.google.com/migration-center/docs/troubleshooting/troubleshoot-login).

## What's next

  * Learn how to [estimate your Google Cloud costs](https://docs.cloud.google.com/migration-center/docs/generate-estimate).
  * Learn how to [start an asset discovery](https://docs.cloud.google.com/migration-center/docs/start-asset-discovery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
