---
url: https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview/
title: Overview of Sensitive Actions Service \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:10.681735+00:00
---

# Overview of Sensitive Actions Service  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of Sensitive Actions Service Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page provides an overview of Sensitive Actions Service, a built-in service of Security Command Center that detects when actions are performed in your Google Cloud organization, folders, and projects that could be damaging to your business if they are taken by a malicious actor.

In most cases, the actions that are detected by Sensitive Actions Service don't represent threats, because they are taken by legitimate users for legitimate purposes. However, the Sensitive Actions Service cannot conclusively determine legitimacy, so you might need to investigate the findings before you can be sure that they don't represent a threat.

## How Sensitive Actions Service works

Sensitive Actions Service automatically monitors all of your organization's [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) for sensitive actions. Admin Activity audit logs are always on, so you don't need to enable or configure them.

When Sensitive Actions Service detects a sensitive action that is taken by a [Google account](https://docs.cloud.google.com/iam/docs/overview#google_account), Sensitive Actions Service writes a finding to Security Command Center in the Google Cloud console and a log entry to the [Google Cloud platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs#sensitive_actions_service).

Sensitive Actions Service findings are classified as _observations_ and can be viewed by finding class or finding source on the **Findings** page in the [Security Command Center console](https://console.cloud.google.com/security/command-center/findings).

## Restrictions

The following sections describe restrictions that apply to Sensitive Actions Service.

### Account support

Sensitive Actions Service detection is limited to actions taken by user accounts.

### Encryption and data residency restrictions

To detect sensitive actions, Sensitive Actions Service must be able to analyze your organization's [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity).

If your organization encrypts your logs by using customer-managed encryption keys (CMEK) to encrypt your logs, Sensitive Actions Service cannot read your logs and, consequently, cannot alert you when sensitive actions occur.

Sensitive actions cannot be detected if you have configured the location of the log bucket for your your Admin Activity Audit Logs to be in a location other than the `global` location. For example, if you have [specified a storage location](https://docs.cloud.google.com/logging/docs/default-settings#specify-region) for the `_Required` logs bucket in a certain project, folder, or organization, logs from that project, folder, or organization cannot be scanned for sensitive actions.

## Sensitive Actions Service findings

The following table shows the finding categories that Sensitive Actions Service can produce. The display name for each finding starts with the [MITRE ATT&CK tactic](https://attack.mitre.org) that the detected action could be used for.

Display name | API name | Description  
---|---|---  
`Defense Evasion: Organization Policy Changed` | `change_organization_policy` |  An organization-level organization policy was created, updated, or deleted, in an organization that is more than 10 days old. This finding isn't available for project-level activations.  
`Defense Evasion: Remove Billing Admin` | `remove_billing_admin` | An organization-level billing administrator IAM role was removed, in an organization that is more than 10 days old.  
`Impact: GPU Instance Created` |  `gpu_instance_created` |  A GPU instance was created, where the creating principal has not created a GPU instance in the same project recently.   
`Impact: Many Instances Created` | `many_instances_created` | Many instances were created in a project by the same principal in one day.  
`Impact: Many Instances Deleted` | `many_instances_deleted` | Many instances were deleted in a project by the same principal in one day.  
`Persistence: Add Sensitive Role` | `add_sensitive_role` |  A sensitive or highly-privileged organization-level IAM role was granted in an organization that is more than 10 days old. This finding isn't available for project-level activations.  
`Persistence: Project SSH Key Added` | `add_ssh_key` | A project-level SSH key was created in a project, for a project that is more than 10 days old.  
  
## What's next

  * Learn about [using Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/how-to-use-sensitive-actions).
  * Learn how to [investigate and develop response plans](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats) for threats.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
