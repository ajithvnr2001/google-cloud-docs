---
url: https://docs.cloud.google.com/security-command-center/docs/automate-recommendations-playbook/
title: Automate IAM recommendations using playbooks \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:36.520700+00:00
---

# Automate IAM recommendations using playbooks  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/automate-recommendations-playbook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Automate IAM recommendations using playbooks Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document explains how to enable the **IAM Recommender Response** playbook in Security Command Center Enterprise to identify the over-permissioned identities and automatically and safely remove the excess permissions.

## Overview

The IAM recommender provides you with security insights that assess how your principals use resources and recommends you to take an action on the encountered insight. For example, when a permission was not used for the last 90 days, the IAM recommender highlights it as an excess permission and recommends you to remove it safely.

The **IAM Recommender Response** playbook uses the IAM recommender to scan your environment for the workload identities that possess excess permissions or service account impersonations. Instead of [reviewing and applying recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations#review-apply) manually in Identity and Access Management, enable the playbook to do it automatically in Security Command Center.

## Prerequisites

Before activating the **IAM Recommender Response** playbook, complete the following prerequisite steps:

  1. Create a custom IAM role and configure a specific permission for it.
  2. Define the **Workload Identity Email** value.
  3. Grant the custom role you've created to an existing principal.



### Create a custom IAM role

  1. In the Google Cloud console, go to the **IAM Roles** page.

[Go to IAM Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click **Create role** to create a custom role with the required permissions for the integration.

  3. For a new custom role, provide the **Title** , **Description** , and a unique **ID**.

  4. Set the **Role Launch Stage** to **General Availability**.

  5. Add the following permission to the created role:
         
         resourcemanager.organizations.setIamPolicy
         

  6. Click **Create**.




### Define the Workload Identity Email value

To define what [identity](https://docs.cloud.google.com/iam/docs/workload-identities) to grant the custom role to, complete the following steps:

  1. In the Google Cloud console, go to **Response > Playbooks** to open the Security Operations console navigation.
  2. In the Security Operations console navigation, go to **Response > Integrations Setup**.
  3. In the integration **Search** field, type in `Google Cloud Recommender`.
  4. Click settings **Configure Instance**. The dialog window opens.
  5. Copy the value of the **Workload Identity Email** parameter to your clipboard. The value must be in the following format: `username@example.com`



### Grant a custom role to an existing principal

After you grant your new custom role to a selected principal, they can change permissions for any user in your organization.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. In the **Filter** field, paste the **Workload Identity Email** value and search for the existing principal.

  3. Click edit **Edit principal**. The dialog window opens.

  4. In the **Edit access** pane under the **Assign roles** , click add **Add another role**.

  5. Select the custom role that you've created and click **Save**.




## Enable playbook

By default, the **IAM Recommender Response** playbook is disabled. To use the playbook, enable it manually:

  1. In the Security Operations console, go to **Response > Playbooks**.
  2. In the playbook **Search** field, input `IAM Recommender`.
  3. In the search result, select the **IAM Recommender Response** playbook.
  4. In the playbook header, switch the toggle to **enable the playbook**.
  5. In the playbook header, click **Save**.



### Configure the automatic approval flow

Changing the playbook settings is an advanced and optional configuration.

By default, every time the playbook identifies unused permissions, it awaits for you to approve or decline the remediation before completing the run.

To configure the playbook flow to automatically remove the unused permissions every time they are found without requesting your approval, complete the following steps:

  1. In the Google Cloud console, go to **Response > Playbooks**.
  2. Select the **IAM Recommender Response** playbook.
  3. In the playbook building blocks, select the **IAM Setup Block_1**. The block configuration window opens. By default, the **remediation_mode** parameter is set to `Manual`.
  4. In the **remediation_mode** parameter field, enter `Automatic`.
  5. Click **Save** to confirm the new remediation mode settings.
  6. In the playbook header, click **Save**.



## What's next?

  * Learn more about [playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen) in the Google SecOps documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
