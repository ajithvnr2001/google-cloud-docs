---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp/
title: SOAR migration overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:13.122685+00:00
---

# SOAR migration overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SOAR migration overview

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes the process and timelines to migrate SOAR infrastructure to Google Cloud. The migration aims to modernize the infrastructure and enhance its integration with Google Cloud services, benefiting both Google Security Operations unified customers and standalone SOAR users transitioning to Google Cloud.

This migration is necessary to provide critical infrastructure upgrades including enhanced reliability, improved security, greater compliance, and more granular access control. It also enables access to Agentic AI capabilities through Model Context Protocol (MCP) integration and best-in-class services including IAM for access control, Cloud Monitoring, and Cloud Audit Logs.

The migration is carried out in two Stages - Stage 1 and Stage 2.

Stage 1 includes the following migrations:

  * Migration of your Google-owned SOAR Project to Google Cloud infrastructure. This is carried out by Google.
  * Migration of SOAR Authentication to Google Cloud (only applicable for SOAR standalone customers).



Stage 2 includes the following migrations: 

  * Migration of SOAR Permission Groups and Permissions to Google Cloud IAM.
  * Migration of SOAR APIs to the new unified Chronicle API, requiring updates to existing scripts and integrations.
  * Migration of webhooks.
  * Migration of remote agents authentication infrastructure.



## Check for successful migration

  * Check for successful completion of Stage 1 by going to **SOAR Settings > License Management** and verifying it says **Google.com** after the system version number.

  * Check for successful completion of Stage 2 migration of SOAR permissions to IAM roles by going to **SOAR Settings > License Management** and verifying it says **Google.com** and **CloudIAM Enabled** after the system version number.




## Migration stage 1 for Google SecOps unified customers

Check your in-product notification for your Stage 1 migration date and the included Google Form to confirm the time slot. Stage 1 includes the following migrations.

  * Migrate Google owned SOAR Project to Google Cloud



The migration involves up to 90 minute downtime where the Google SecOps platform is not accessible. During this downtime, your SIEM services will continue to operate in the background, while SOAR services will be temporarily paused. Following the downtime, the platform will be accessible, and SOAR services will resume processing any alerts generated or ingested during the downtime.

Once the migration is complete, we will send you an email. 

## Migration stage 1 for SOAR standalone customers

**Note:** For a comprehensive, end-to-end walkthrough on the instructions for Stage 1 of the SOAR Migration process, specifically for SOAR Standalone customers, see the [Google SecOps SOAR Migration video](https://www.youtube.com/watch?v=RRJu_YgXWn4).

Depending on your needs and use cases, you can choose one of the following migration options:

  * **Option 1 (Recommended) — Unify your SOAR instance with an existing SIEM instance** : if you have an existing SIEM instance that doesn't have SOAR enabled, we recommend unifying your SOAR instance into your existing SIEM deployment whenever possible. This option uses the Google Cloud project associated with your existing SIEM instance and unifies both products under a single Google SecOps interface with shared authentication, access control, and audit logging.

**Caution:** This option applies only if SOAR isn't already enabled in your existing SIEM instance. If your SIEM instance already includes SOAR as part of Google SecOps, don't choose this option, because migrating your standalone SOAR instance into it can overwrite the existing SOAR configuration and data. In this case, choose Option 2 or contact Google SecOps Support.**Important:** This option is available only if your existing SIEM instance has an ingestion-based license (SIEM or unified Google SecOps). If your SIEM instance has a legacy employee-based license, you can't reuse its Google Cloud project for SOAR. Instead, choose Option 2 to keep your SIEM and SOAR deployments separate. For more information, see [Migrate a SOAR MSSP instance to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-mssp-instance#gcp-project-identification-and-setup).
  * **Option 2 — Deploy a new Google SecOps instance** : alternatively, if you don't have an existing SIEM instance or need to keep your SOAR and SIEM deployments separate, you can deploy a new Google SecOps instance in a dedicated Google Cloud project.




You will get an in-product notification message when we are ready to initiate Stage 1 for you. Make sure to do the following:

  1. Identify or set up your Google Cloud project based on your chosen migration option: 
     * **Option 1 (Unify with an existing SIEM)** : use the existing Google Cloud project linked to your SIEM instance.
     * **Option 2 (Deploy a new Google SecOps instance)** : [set up a Google Cloud project](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project). You can also use a Google Cloud project that was set up to access Google SecOps Support but doesn't have a Google Security Operations instance yet.
  2. [Enable Chronicle API](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project#enable-chronicle-api-in-proj) in the Google Cloud project (if not already enabled).
  3. Set up Google Cloud Authentication to access SOAR. Refer to Set up Google Cloud Authentication to access SOAR.
  4. Provide the Google Cloud project ID in the Google form in the in-product notification and confirm the migration date and time slot before you submit the form. 
  5. Accept the invitation email to the "Get Google Security Operations page" and complete the set up (if deploying a new Google SecOps instance). Make sure your region information is accurate.
  6. Validate that the preceding steps have been set up correctly by consulting the [Pre-migration validation guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/soar-pre-validation).



After you complete the steps, Google performs the migration at your scheduled date and time. The migration requires approximately 2 hours of downtime for SOAR services. Upon completion, you will receive an email with the new URL to access the SOAR platform. The old URL remains functional until June 30, 2026, and redirects to the new URL.

### Set up Google Cloud authentication to access SOAR

Depending on the type of identity you want to use, configure one of the following options. You might need assistance from your Google Cloud and identity or IdP administrator to complete these steps.

#### Option 1: Configure Cloud Identity Authentication in Google Cloud (Google Managed accounts)

This scenario is applicable if you manage user accounts directly within Cloud Identity using Google-managed usernames and passwords. It does not apply if you are using Cloud Identity for SSO with a third-party identity provider such as Okta or Azure AD.

Complete the following steps:

  1. [Set up Cloud Identity in Google Cloud](https://docs.cloud.google.com/iam/docs/user-identities#google-accounts).

You can skip this step if you already have Cloud Identity set up with Google-managed username and password.

  2. Make sure all existing SOAR users are [configured in the Cloud Identity Admin console](https://support.google.com/cloudidentity/answer/7332836).

  3. Grant the required roles in IAM by [following the role assignment format for Google accounts](https://docs.cloud.google.com/iam/docs/principal-identifiers?_gl=1*npios2*_ga*OTMwNTQ5NzQwLjE3NTgyOTExMzQ.*_ga_WH2QY8WWF5*czE3NTg5MjkwODAkbzEkZzEkdDE3NTg5MzAwMzIkajUzJGwwJGgw#allow).

     1. Assign the following predefined IAM roles in Google Cloud to the onboarding SME:

        * [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin)
        * [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin)
        * [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin)
        * [Project IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin)
        * [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin)
     2. Assign one of the following predefined IAM roles to all existing SOAR users:

        * [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin)
        * [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor)
        * [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer)
        * [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer)
  4. Complete the authentication setup in SOAR by mapping each user (including administrators) to an [email user group](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party#map-email-user-groups).

     1. Go to **SOAR Settings > Advanced > Group Mapping**.
     2. Click add **Add** and fill in the following information:

        * **IdP / User group** : The name of the email user group (such as **T1 analysts**).
        * **Permission Groups** : Select the permission groups.
        * **SOC Roles** : Select the SOC roles.
        * **Environments** : Select the environments (such as **All Environments**).
        * **Group Members** : Enter the required user emails. Press **Enter** after adding each email.
**Note:** If you have any existing email user group mappings in the External Authentication page, you should leave them as is in order not to override your existing SOAR authentication. For the new Google Cloud authentication to access SOAR, you must still set up email user group mapping in the **SOAR Settings > Advanced > Group Mapping** page.
     3. Click **Add**. 

Each time a user signs in to the platform, they are automatically added to **SOAR Settings > Organization > User Management** page. The migrated instance retains these mappings, which serve as the basis for determining user access to SOAR. You must make sure that every user is mapped in this page in order to access Google SecOps.




#### Option 2: Configure Workforce Identity Federation Authentication in Google Cloud

This scenario is applicable if you manage your user identities using third party IdPs such as Microsoft Azure Active Directory, Okta, Ping Identity and AD FS.

  1. [Set up Workforce Identity Federation in Google Cloud](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication) You can skip this step if it was already set up.
  2. Make sure all the existing users in SOAR are part of the workforce pool groups set up in the Workforce Identity Federation. 
  3. Grant the required roles in IAM by [following the role assignment format for Workforce Identities](https://docs.cloud.google.com/iam/docs/principal-identifiers?_gl=1*npios2*_ga*OTMwNTQ5NzQwLjE3NTgyOTExMzQ.*_ga_WH2QY8WWF5*czE3NTg5MjkwODAkbzEkZzEkdDE3NTg5MzAwMzIkajUzJGwwJGgw#allow).

     1. Assign all of the following predefined IAM roles to the onboarding SME.

        * [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin)
        * [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin)
        * [Chronicle SOAR Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.soarAdmin)
        * [Project IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin)
        * [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin)
     2. Assign one of the following roles in IAM to all existing SOAR users:

        * [Chronicle API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.admin)
        * [Chronicle API Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.editor)
        * [Chronicle API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.viewer)
        * [Chronicle API Limited Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chronicle#chronicle.limitedViewer)
  4. Complete the authentication setup in SOAR by [mapping all the IdP groups that need access to SOAR](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform).

Make sure the existing users are mapped to at least one of the IdP groups. 

     1. Go to **SOAR Settings > Advanced > Group Mapping**.
     2. Click add **Add** and fill in the following information: 
        * **IdP / User group** : Enter the group name from your IdP.
        * **Permission Groups** : Select the permission groups.
        * **SOC Roles** : Select the SOC roles.
        * **Environments** : Select the environments (such as **All Environments**).
     3. Make sure you have added the Admin IdP group with Admin permissions for permission groups, SOC Roles and select All Environments.
     4. If you have any existing IdP group mappings in the External Authentication page, you should leave it as is in order not to override your existing SOAR authentication. For the new Google Cloud authentication to access SOAR, you must still set up IdP Group Mapping in **Settings > SOAR Settings > Advanced > Group Mapping** page.
     5. Click **Add**. Each time a user signs in to the platform, they are automatically added to **Settings > Organization > User Management** page. The migrated instance retains these mappings, which serve as the basis for determining user access to SOAR. You must make sure that every user is mapped in this page in order to access Google SecOps.
**Note:** This instruction is applicable if you are using Workforce Identity Federation for your integrations. If you have granted the **Service account token creator** IAM role to the python service account `gke-init-python@soar-yyyyyy.iam.gserviceaccount.com`, you must grant the same **Service account token creator** IAM role to the new Python service account `soar-python@yyyyyyyyyyy-tp.iam.gserviceaccount.com` after the migration. The new Service Account is sent by email post migration.



## Stage 2 migration for all customers

**Important** : You must complete Stage 1 before you begin the Stage 2 migration.

Stage 2 migration is generally available to all customers from January 26, 2026. 

The final deadline to complete the Stage 2 transition to IAM roles is November 30, 2026. The API migration deadline is extended until March 31, 2027.

**Note:** These procedures apply to both Google SecOps SOAR standalone customers and Google SecOps customers.

### Migrate SOAR permission groups to Google Cloud IAM

Migrate the SOAR permission groups and permissions to IAM through a single-click of the migration script in Google Cloud. The script creates new custom roles for each permission group and assigns them to users for Cloud Identity customers or IdP groups for Workforce Identity Federation customers. You can also migrate the SOAR permissions using Terraform.

For full details of the migration script and Terraform commands, see [Migrate SOAR permissions to Google Cloud IAM](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-permissions-iam).

For more information about how to set up permissions, see [Configure feature access](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).

After the migration of the permissions, the following happens: 

  * **SOAR Settings > Organization > Permissions** page is still available until March 31, 2027 (for backwards compatibility with legacy APIs). Don't make any changes to this page. The permissions are all managed through IAM.
  * The **Permission Group** column on the **Group Mapping** page is displayed for backwards compatibility with legacy SOAR API. Do not delete these assignments. The column will be automatically removed by March 31, 2027 without any customer impact.
  * The restricted actions section in the **Permissions** page will move to the **Group Mapping** page.

**Note:** If you don't see the migration script, you have probably not completed stage 1 of the migration. Contact your Google representative. 

### Migrate SOAR APIs to Chronicle API

If you use SOAR API programmatically using API calls or through integrations, you can migrate it to the new SOAR v1 beta endpoints available as part of Chronicle API. 

You must update your scripts and integrations to replace the SOAR API endpoints with the corresponding Chronicle API endpoints. The legacy SOAR API and API Keys are available until March 31, 2027 after which they will no longer function. For more information, refer to [Migrate endpoints to Chronicle API](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/api-migration-guide).

### Migrate webhooks

You need to migrate [SOAR webhooks](https://docs.cloud.google.com/chronicle/docs/soar/ingest/webhooks/setting-up-a-webhook) to the Chronicle API by doing the following before March 31, 2027:

Update the webhook URL on the client side by replacing the legacy `siemplify-soar.com` domain with the new `googleapis.com` domain using the [new request format](https://docs.cloud.google.com/chronicle/docs/reference/rest). The legacy `siemplify-soar.com` domain will continue to function until March 31, 2027.

For example, a webhook defined on: `https://xxxx.siemplify-soar.com/api/external/v1/webhooks/{webhook_id}?api_key=xxxx`

will need to be updated to: `https://us-chronicle.googleapis.com/v1alpha/projects/{project_id}/locations/{location}/instances/{instance/{instance_id}/webhooks/{webhook_id}?api_key=xxxx`

The authentication for webhooks remains unchanged. Webhooks continue to use the API key that was initially created alongside the webhook link.

### Migrate Remote Agent Authentication Infrastructure

The following steps detail how to migrate the authentication infrastructure of your Remote Agents to Google Cloud Service Account authentication. This process does not require migrating or replacing the Remote Agent instances or hosts.

  1. Create a Service Account instead of an API key for the remote agent.
  2. Perform a major version upgrade of the remote agent.



Existing Remote Agents will be available until November 30, 2026, after which they will no longer function. For detailed instructions, see [Migrate Remote Agents to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google).

### Impact on SOAR Audit Logs

SOAR logs will become available in Google Cloud once you complete the permissions migration to IAM. Any calls made to the legacy SOAR API until March 31, 2027 will remain accessible in the SOAR Audit logs For Google SecOps customers, see [Collect Google SecOps SOAR logs](https://docs.cloud.google.com/chronicle/docs/secops/collect-secops-soar-logs). For SOAR standalone customers, see [Collect SOAR logs](https://docs.cloud.google.com/chronicle/docs/soar/investigate/collecting-soar-logs)

### Further changes post migration:

**License type** The license type is now determined by the user's assigned permissions in IAM.

**Landing page** The landing page will move from the Permissions page to the **User Preferences** menu, accessible from your avatar.

## What's Next

  * [SOAR migration pre-validation guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/soar-pre-validation)
  * [Migrate a SOAR standalone instance of an MSSP](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-mssp-instance)
  * [Migrate SOAR endpoints to the Chronicle API](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/api-migration-guide)
  * [Migrate remote agents authentication infrastructure](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google)
  * [Migrate SOAR permissions to Google Cloud IAM](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-permissions-iam)
  * [Frequently asked questions](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
