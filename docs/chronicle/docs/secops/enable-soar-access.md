---
url: https://docs.cloud.google.com/chronicle/docs/secops/enable-soar-access/
title: Enable SOAR access \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:43.949532+00:00
---

# Enable SOAR access  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/enable-soar-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable SOAR access

Supported in:

Google SecOps 

This document is for Google Security Operations admins who want to provide users with access to SOAR features in Google SecOps (such as managing cases).

## Before you begin

These procedures are based on the assumption that you have already onboarded to the Google SecOps platform, enabled the Chronicle API, and started working with IAM permissions. The following procedures may vary slightly, depending on whether you configured a [Cloud Identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication) or a [third-party identity provider](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

## Enable access

  1. Define either a [predefined role](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#predefined-roles) or a [custom role](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#custom-role). The custom role must contain the following minimum baseline permissions:

     * `chronicle.dataAccessScopes.list`
     * `chronicle.preferenceSets.get`
     * `chronicle.preferenceSets.update`
     * `chronicle.instances.get`
     * `chronicle.socRoles.get`
     * `chronicle.userNotifications.get`
     * `chronicle.userLocalizations.get`
     * `chronicle.moduleSettings.rebranding`
     * `chronicle.integrations.get`
     * `chronicle.legacySoarAdvancedReports.get`
     * `chronicle.environmentGroups.get`
     * `chronicle.moduleSettingsProperties.get`
     * `chronicle.legacySoarUsers.get`

For more information about baseline permissions and mapping to specific SOAR actions, see [Required permissions for every role](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/map-soar-permissions-to-iam#required_permissions_for_every_role).

  2. If you're using the Cloud Identity provider, map user email groups into the [email group mapping page](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform-first-party).

  3. If you're using a third-party identity provider, map IdP groups into the [IdP group mapping page](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform).




You can choose the control access parameters that meet your needs. For more information, see [SOAR access overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/control-access-to-platform).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
