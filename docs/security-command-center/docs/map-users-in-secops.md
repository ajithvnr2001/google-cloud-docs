---
url: https://docs.cloud.google.com/security-command-center/docs/map-users-in-secops/
title: Map and authenticate users to enable SOAR-related features \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:47.012565+00:00
---

# Map and authenticate users to enable SOAR-related features  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/map-users-in-secops/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Map and authenticate users to enable SOAR-related features Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This article shows you how to authorize and map users using Identity and Access Management (IAM) with secure identification in the SOAR-related features on Security Operations console pages. 

## Before you begin

Make sure you have defined and mapped users using IAM to the SIEM-related features on Security Operations console pages. For more information, see [ Control feature access using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access). 

## Grant IAM roles in the Google Cloud console

Three predefined IAM roles have been added to your Security Command Center Enterprise project in the Google Cloud console.

  * Chronicle SOAR Admin (`roles/chronicle.soarAdmin`)
  * Chronicle SOAR Threat Manager (`roles/chronicle.soarThreatManager`)
  * Chronicle SOAR Vulnerability Manager (`roles/chronicle.soarVulnerabilityManager`)



The following procedure explains how to grant the IAM roles to users in the Google Cloud console.

  1. Open the console and select your Security Command Center.
  2. Click **IAM & Admin**.
  3. Select **IAM** from the navigation tree and then select **Grant Access**.
  4. In the **Grant Access dialog box** go to the **Add Principals** field, and enter the email addresses of users or user groups for one of the three IAM roles.
  5. In the **Select a role** field, search for the required role: **Chronicle SOAR Admin** , **Chronicle SOAR Threat Manager** , or **Chronicle SOAR Vulnerability Manager**.
  6. Repeat this process for all three roles or as needed.
  7. Click **Save**.



## Control user access

In the Google Cloud console navigation, go to the **Settings > SOAR settings**. In the Security Operations console **SOAR settings** page, there are several different ways to determine which users have access to which aspects of the platform. 

  * **Permissions groups** : Set permissions groups for user types which determine which modules and submodules will be visible or editable for users. For example, you can set permissions such that the user sees the cases and the workdesk but doesn't have access to the playbooks and settings. For more information, see [ Working with Permission Groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups) in the Google SecOps documentation. 
  * **SOC roles** : Define the role of a group of users. You can set cases or actions or playbooks to a SOC role instead of a specific user. Users see cases that are assigned to them personally, or to their role, or to one of the additional roles. For more information, see [Working with Roles](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-roles) in the Google SecOps documentation.
  * **Environments** : Set environments that enterprises can use to manage different networks or business units within the same organization. Users only see data for those environments they have access to. For more information, see [Add a new environment](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/work-with-environments#add-a-new-environment) in the Google SecOps documentation.



## Map the IAM roles using the SOAR settings Security Operations console page

  1. In the Google Cloud console, go to **Settings > SOAR settings > Advanced > IAM Role mapping**.
  2. Using the display name (e.g. Chronicle SOAR Admin), assign each IAM role to the corresponding SOC roles (Threat Manager, Vulnerability Manager or Admin), permission groups (select Admins permission group), and environments (select the default environment). Alternatively, add an email address instead of an IAM role. 
  3. Click **Save**.

When each user logs in to the platform, they are automatically added to the **User Management page** (which is located in **SOAR settings > Organization **). 

Sometimes users will try to access Security Operations console features, but their IAM role has not been mapped in the platform. In order for these users not to be rejected, we recommend enabling and setting the **Default Access Settings** on this page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
