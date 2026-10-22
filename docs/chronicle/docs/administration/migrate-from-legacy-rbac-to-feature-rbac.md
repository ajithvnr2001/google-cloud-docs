---
url: https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-rbac-to-feature-rbac/
title: Migrate from legacy RBAC to feature RBAC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:56.543316+00:00
---

# Migrate from legacy RBAC to feature RBAC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-rbac-to-feature-rbac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate from legacy RBAC to feature RBAC

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** For a comprehensive, end-to-end demo on the Migration process, see the [Google SecOps SIEM Legacy Infra Migration video ](https://youtu.be/Bg8VZftcrlg?si=3mvcaSucWS-KfZkd).

This document explains how to migrate your existing Google SecOps instance from legacy RBAC to feature RBAC using Google Cloud IAM.

## Before you begin

Make sure you have the following prerequisites:

  * The [required permissions](https://docs.cloud.google.com/chronicle/docs/onboard#roles-configure-idp) in your Google Cloud instance to perform the steps in this document.
  * Your Google SecOps instance has been migrated to your Google Cloud project and has been set up using Google Cloud authentication. 



## Overview

You can use auto-generated commands to migrate legacy RBAC roles and permissions to Google Cloud IAM. Google SecOps creates these commands using your pre-migration _feature RBAC_ access control configuration. When run, they create new IAM policies equivalent to your existing configuration, as defined in Google SecOps on the **SIEM Settings** > **Users and Groups** page.

After you run these commands, you can't revert to the previous _feature RBAC_ access control feature. If you encounter an issue, contact [Google SecOps Technical Support](https://docs.cloud.google.com/chronicle/docs/getting-support).

  1. In the Google Cloud console, go to the **Security** > **Google SecOps** > **Access management** tab.
  2. Under **Migrate role bindings** , you see a set of auto-generated Google Cloud CLI commands.
  3. Review and verify that the commands create the expected permissions. For information about Google SecOps roles and permissions, see [How IAM permissions map to each feature RBAC role](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#roles-permissions).
  4. Launch a Cloud Shell session.
  5. Copy the auto-generated commands, and then paste and run them in the gcloud CLI.
  6. After you execute all commands, click **Verify access**. If successful, you see the message **Access verified** on the Google SecOps **Access management** page. Otherwise, you see the message **Access denied**. This message might take 1-2 minutes to appear.
  7. To complete the migration, return to the **Security** > **Google SecOps** > **Access management** tab, and then click **Enable IAM**.
  8. Verify that you can access Google SecOps as a user with the Chronicle API Admin role: 
     1. Sign in to Google SecOps as a user with the Chronicle API Admin predefined role. For more information, see [Sign in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).
     2. Open the **SIEM Settings > Users and Groups** page. You should see the following message: _To manage users and groups, go to**Identity Access Management (IAM)** in the Google Cloud console. Learn more about managing users and groups._
  9. Sign in to Google SecOps as a user with a different role. For more information, see [Sign in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).
  10. Verify that the available features in the application match the permissions defined in IAM.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
