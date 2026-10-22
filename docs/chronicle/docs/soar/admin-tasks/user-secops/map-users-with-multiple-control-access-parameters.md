---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-with-multiple-control-access-parameters/
title: Apply multiple control access parameters \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:24.022601+00:00
---

# Apply multiple control access parameters  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-with-multiple-control-access-parameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Apply multiple control access parameters

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document describes the algorithms that the Google Security Operations platform uses to apply multiple control access parameters for user groups.

## Assign permission groups

**Note:** This section only applies to customers who haven't migrated to Google Cloud. After completing Stage 1 of the migration, see [Migrate to Google Cloud](https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication).

You can assign a maximum of five permission groups for each user or user group. The users get a combination of all the permissions from each of the permission groups.

### Assigned landing page for permissions groups

**Note:** This section only applies to customers who haven't migrated to Google Cloud. After completing Stage 1 of the migration, the landing page option appears under your Avatar in the platform.

Each permission group has a designated landing page that users are directed to when they first sign in to the Google SecOps platform. If a user (or user group) is assigned to multiple permission groups, Google SecOps selects the landing page based on the highest-ranking option in the following hierarchy: 

  * Cases > Case Overview
  * Homepage (Workdesk) > My Cases
  * Cases > Case Wall
  * Homepage (Workdesk)> Pending Actions
  * Dashboards
  * Playbooks
  * Reports
  * Search
  * Homepage (Workdesk) > Requests
  * Command Center (Incident Manager)
  * Legacy SIEM Search



## Map SOC roles

You can map each user with up to five SOC roles plus additional roles.

### Create playbook views per SOC roles

Each playbook customized view is assigned to a specific SOC role. If a user is assigned to several SOC roles, then all widgets are displayed. Exception: If one SOC role includes another, the system displays the parent SOC role's playbook view 

### Assign environments

You can assign both environments and environment groups at the same time. You can assign each user to multiple environments and environment groups, granting them access to all cases and data within each assigned environment or environment group.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
