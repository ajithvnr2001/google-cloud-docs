---
url: https://docs.cloud.google.com/chronicle/docs/onboard/log-in-to-new-instance/
title: Access a Google SecOps instance \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:36.879955+00:00
---

# Access a Google SecOps instance  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/onboard/log-in-to-new-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access a Google SecOps instance

Supported in:

Google SecOps 

This guide helps Google SecOps administrators configure user access to a newly provisioned Google SecOps instance. Properly configuring access control and understanding how to troubleshoot common issues is crucial for maintaining security and operational efficiency.

## Before you begin

  * Confirm that you completed the initial Google SecOps instance setup. For more information, see [Link a Google SecOps instance to Google Cloud services](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud#before_you_begin).
  * You must have administrative privileges in both Google Cloud IAM and Google SecOps. For more information, see [Required roles and permissions](https://docs.cloud.google.com/chronicle/docs/onboard#required-roles).

Make sure your identity provider (IdP) group or email has been granted the `Chronicle API Admin` role within [Google Cloud IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project).

  * Familiarize yourself with the authentication method chosen for your instance: [Cloud Identity](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication) or [Workforce Identity Federation](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).




## Configure user access

Sign in to the Google SecOps instance and complete the following steps to enable users to access the instance.

  1. **Configure users:** Work with your Identity Admin to configure the users in your chosen authentication setup:

     * **Cloud Identity:** You need to add user accounts to Cloud Identity. For more information, see [Configure a Google Cloud Identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication).
     * **Third-party identity provider:**

       * You need to add user and group accounts to the third-party identity provider.
       * You must configure users and groups as part of setting up the Workforce Identity Federation. For more information, see [Configure a third-party identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).
  2. **Grant IAM roles:** Assign users the specific predefined or custom roles in IAM based on the features they need to access. For more information, see [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).

  3. **Map SOAR permissions:** Map users to the required SOAR environments, SOAR permission groups (if you haven't migrated to IAM), and SOAR SOC roles on the **Group Mapping** page. For more information, see [Control access to the platform](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/control-access-to-platform).

**Note:** SOAR permissions groups are replaced with IAM roles post migration to Google Cloud. For more information, see [Migrate to Google Cloud IAM for SOAR](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#permissions-iam).



### Disable the default SOAR access settings

By default, the SOAR **Group Mapping** page enables the **Default Access Settings** toggle. This grants the following to any users and groups who are not explicitly defined in the **Group Mapping** table:

  * The **Administrator** SOC role
  * Access to **All environments**
  * **Admins permission group** (if you haven't completed [Permission Groups Migration to Google Cloud IAM](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#permissions-iam))



After you configure the required records (rows) in the **Group Mappings** table, we recommend that you disable the **Default Access Settings** toggle to enforce the principle of _least privilege_.

## Troubleshoot access issues

If users have trouble logging in to Google SecOps, the IAM configuration in the Google Cloud project linked to your Google SecOps instance might be the cause.

For example, users might see the following error message: `Cannot Authenticate user, because user does not have access to the GCP project associated with this Chronicle customer.`

This error typically means the associated Google Cloud project does not grant the necessary IAM roles to the user's account or group.

### Common causes and solutions

Error | Description | Solution  
---|---|---  
User or group missing from IAM configuration | The linked Google Cloud project's IAM policy might not include the user or group, or an administrator might have removed them. | 

  1. Verify user or group membership in the Google Cloud console by going to the **IAM & Admin** > **IAM** section of the Google Cloud project linked to your Google SecOps instance.
  2. Check that the user or group is listed in the IAM settings and that they have the necessary roles to access the Google SecOps instance.
  3. Grant the appropriate roles if necessary. For more information on required roles, see [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).

  
Incorrect IAM roles | The user or group is included in the IAM configuration, but they lack the specific roles required to access the Google SecOps instance. | 

  * Check that the user or group is assigned the correct roles (predefined roles or custom roles) in Google Cloud IAM (**IAM & Admin > IAM** section) per your organization's access policies. For more information on roles, see [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).
  * Add the user or group to the IAM policies or adjust their roles as needed to grant access. Note: These IAM changes can only be made by your organization's project administrators. Google Cloud Support cannot make these changes.

  
Recent IAM changes | An administrator or automation tool might have recently modified the IAM policies, inadvertently affecting user access. | 

  * Review [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) in the linked Google Cloud project to track recent changes to IAM permissions. Filter logs for IAM policy changes to identify any modifications that might have removed or altered required access.
  * To review audit logs in the Google Cloud console, go to **Logging** > **Logs Explorer**. Check the Cloud Audit Logs for any recent `SetIamPolicy` operations that might indicate changes to permissions.

  
  
For more information on required roles, see [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
