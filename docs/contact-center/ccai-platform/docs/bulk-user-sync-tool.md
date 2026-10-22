---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-sync-tool/
title: Bulk user sync tool \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:23.374893+00:00
---

# Bulk user sync tool  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-sync-tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Bulk user sync tool Stay organized with collections  Save and categorize content based on your preferences. 

The bulk user sync tool is a configurable, serverless utility for automating and managing user lifecycle operations between your organization's central directory service and CCAI Platform. It's an open source project that you can find in the [Google Cloud GitHub repository](https://github.com/GoogleCloudPlatform/ccaas-bulk-sync)

You can use the bulk user sync tool to synchronize user accounts, team assignments, and roles based on group memberships sin your source directory. This helps ensure that user permissions in CCAI Platform are always aligned with your organization's primary identity provider. This can help reduce manual administration, eliminate errors, and enhance security.

The service is managed through a web interface and supports the following three directory services:

  * Google Workspace

  * Microsoft Active Directory (via LDAP)

  * Microsoft Entra ID




## How synchronization works

The bulk user sync tool follows these steps every time it runs a synchronization:

  1. **Identify managed users** : This gets all users from CCAI Platform who are assigned the `User Sync Custom Role`. This is the current user list of all users managed by this tool.

  2. **Build directory list** : This connects to your configured directory (for example, Google Workspace) and gets all members from every directory group defined in the `Group Mappings` section. This creates a comprehensive directory user list of all active users in CCAI Platform.

  3. **Process additions** : The system compares the current user list with the directory user list. Any user in the directory user list who is not in the current user list (or is marked as `Inactive` in CCAI Platform) is added to an "add" list.

  4. **Process deactivations** : Any user who is `Active` in the current user list but is not in the directory user list is added to a "deactivate" list. Their status set to `Inactive`.

  5. **Process updates** : For users who are `Active` and present in both lists, the system compares their current CCAI Platform teams and roles against the rules defined in the `Group Mappings` section. If there is a mismatch, the user is added to an "update" list with the correct assignments.

  6. **Submit changes** : The "add", "deactivate", and "update" lists are combined into a single payload and submitted to the [Bulk user management API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management-api) to apply all of the changes in a single operation.




## Capabilities

The bulk user sync tool provides the following capabilities:

  * **Automated synchronization** : Set a schedule (hourly, daily, or custom cron) to automatically keep your users in sync.

  * **Flexible mapping engine** : Map directory groups to specific CCAI Platform teams and roles. A single directory group can grant multiple roles or a team assignment.

  * **Simulation Mode** : Run a "Simulate Only" sync to generate a report of all proposed changes (adds, updates, deactivations) without applying them. This capability allows the verification of rules before committing any live changes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
