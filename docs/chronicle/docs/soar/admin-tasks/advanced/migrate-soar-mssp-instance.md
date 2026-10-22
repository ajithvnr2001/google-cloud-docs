---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-mssp-instance/
title: Manage MSSP migration \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:49.217690+00:00
---

# Manage MSSP migration  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-mssp-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage MSSP migration

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document details Stage 1 of migrating the infrastructure of SOAR standalone instance of a managed security service provider (MSSP) to Google Cloud. 

After completing Stage 1, the MSSP should proceed with [Stage 2 in the SOAR migration overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#stage_2_migration_for_all_customers), because it is the same for all customers: MSSPs and non-MSSPs.

## Step 1: Google Cloud project identification and setup

The partner needs to identify a Google Cloud project to migrate the SOAR instance to according to the licenses, as follows:

  * If the partner has an ingest license (SIEM / unified SecOps) for their tenants, they can choose to use the Google Cloud project of the primary SIEM to host the primary SOAR. Alternatively, they can [create a separate Google Cloud project](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project) to keep the SIEM and SOAR separate.

  * If the partner has employee-based licenses for their tenants, they need to [create a separate Google Cloud project](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project) to host SOAR, keeping SIEM and SOAR separate.




The partner can also use a Google Cloud project that might have been set up to access Chronicle Support but doesn't yet have a Google SecOps tenant.

## Step 2: [Enable Chronicle API](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project#enable-chronicle-api-in-proj) in the customer Google Cloud project

## Step 3: Set up Google Cloud authentication to access SOAR

The partner needs to set up Google Cloud authentication to access SOAR.

If the partner has a single IdP, they can choose to configure [Cloud Identity](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#cloudid-auth) (Google managed accounts) or [Workforce Identity Federation](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#workforce-id). These are described as Option 1 and Option 2 respectively in the [SOAR migration overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#cloudid-auth) document.

If the partner has multiple IdPs, they need to complete the following steps to configure Workforce Identity Federation:

  1. For each frontend path in SOAR, the partner needs to set up an external IdP through Workforce Identity Federation for each frontend path.
  2. The partner needs to [create](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#workforce-id) one workforce pool for each IdP, and configure the mappings between the workforce pool provider and third-party IdP. Repeat this for each frontend path.
  3. Grant the required roles in IAM to the onboarding SME and all SOAR users by following the instructions in step 3 of [Option 2: Configure Workforce Identity Federation Auth in Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#workforce-id).
  4. Update the IdP groups mapping in the new **Group Mapping** page in SOAR for each workforce pool and IdP.

     1. Click add **Add** to the right of **Workforce Pools**.
     2. Add the name of the workforce pool that you have configured in Workforce Identity Federation.
     3. Do the following to add your IdP groups to the **Group Mapping** table.

        1. Click add **Add** to the right.
        2. Add the group name from your IdP.
        3. Choose the necessary access to SOAR permission groups, environments, and SOC roles.
        4. Click **Save**.
        5. Make sure that you have also added the Admin IdP group with Admin permissions for permission groups, SOC roles, and Select All Environments.
     4. Repeat steps a–c for other workforce pools.

  5. If you have any existing IdP group mappings in the **External Authentication** page, don't modify them, because they are still needed for you to authenticate to SOAR until the migration.

  6. After you have completed the previous steps, click **Add**. Each time a user signs in to the platform, they are automatically added to the **Settings > Organization > User Management** page.




![SOAR Settings - IAM Role Mapping](https://docs.cloud.google.com/static/chronicle/images/soar/soar-migration-settings-iam-role-mapping.png)

**Note:** All internal users in your existing SOAR platform will need to transition to the Google Cloud authentication, either Cloud Identity or Workforce Identity Federation. If you have multiple frontends, use Workforce Identity Federation.

## Step 4: Migration-date confirmation

Provide the Google Cloud project ID in the [Google form](https://docs.google.com/forms/d/1sBr_dDH6m1wjFZFaU5zPwnU5SDQE7HVFdebdmxKNoWU/preview) in the in-product notification, and confirm the migration date and time slot before you submit the form.

If the MSSP has multiple frontend paths, complete the Google form to add details on the workforce pool ID, provider ID, and frontend path for each provider.

![Provider details](https://docs.cloud.google.com/static/chronicle/images/soar/soar-migration-provider-details.png)

## Step 5: Invitation email

Accept the invitation email to the **Get Google Security Operations page** and complete the setup. Make sure your region information is accurate, as shared in the invitation email.

## Step 6: Setup validation

To validate your setup, we recommend that you follow the instructions in the [SOAR migration pre-validation guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/soar-pre-validation).

## Step 7: Migration

Google will perform the migration. During the migration, you will experience a downtime in SOAR services for two hours. 

After the migration completes, we will send an email along with a new URL to access the SOAR platform.

Coordinate with your partner representative during and after the migration to ensure you are not facing any issues after migration.

## What's Next

  * [SOAR migration overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp)
  * [Migrate SOAR endpoints to the Chronicle API](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/api-migration-guide)
  * [Migrate remote agents authentication infrastructure](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google)
  * [Frequently asked questions](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
