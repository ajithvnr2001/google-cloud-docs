---
url: https://docs.cloud.google.com/advisory-notifications/docs/sensitive-actions-overview/
title: Overview of Sensitive Actions notifications \u00a0|\u00a0 Advisory Notifications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:08.404085+00:00
---

# Overview of Sensitive Actions notifications  |  Advisory Notifications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/advisory-notifications/docs/sensitive-actions-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Advisory Notifications ](https://docs.cloud.google.com/advisory-notifications/docs)
  * [ Guides ](https://docs.cloud.google.com/advisory-notifications/docs/overview)



Send feedback 

#  Overview of Sensitive Actions notifications Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Protecting cloud environments requires protecting Identity and Access Management accounts against compromise. Compromising a privileged user account enables an attacker to make changes to a cloud environment, so detecting potential compromises is essential for securing organizations of every size. To help organizations stay secure, Google Cloud logs sensitive actions that are taken by IAM user accounts and notifies organization administrators of those actions directly through Advisory Notifications.

Sensitive actions are actions that can have a significant negative effect on your Google Cloud organization if they are taken by a malicious actor using a compromised account. These actions by themselves do not necessarily represent a threat to your organization or indicate that an account has been compromised. However, we recommend that you confirm that the actions were taken by your users with legitimate purposes.

## Who receives Sensitive Actions notifications

Google Cloud notifies your organization of sensitive actions by sending an email notification to your organization-level [essential contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) for security. If there are no essential contacts configured, the email notification is sent to all accounts that have the Organization Admin IAM role at the organization level.

**Important:** If you are using Google Cloud without an organization, you do not receive Sensitive Actions notifications.

### Opting out

If you don't want to receive Sensitive Actions notifications in your organization, you can opt out of these notifications. For more information, see [Configure notifications](https://docs.cloud.google.com/advisory-notifications/docs/opt-in-out-notifications). Opting out of Sensitive Actions notifications only affects the notifications delivered through Advisory Notifications. [Sensitive Actions logs](https://docs.cloud.google.com/advisory-notifications/docs/sensitive-actions-logs) are always generated and are not affected by opting out of notifications. If you use Security Command Center, the Sensitive Actions Service is not affected by opting out of Sensitive Actions notifications.

## How Sensitive Actions works

Google Cloud detects sensitive actions by monitoring your organization's [Admin Activity Audit Logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity). When a sensitive action is detected, Google Cloud writes the action in the [Sensitive Actions Service platform log](https://docs.cloud.google.com/logging/docs/api/platform-logs#sensitive_actions_service) in the same resource where the activity occurred. Google Cloud also includes the event in a notification delivered through Advisory Notifications.

### Notification frequency

The first time a sensitive action is observed in your organization, you receive a report that includes the initial action, plus any other actions that occur in the following hour. After the initial report, you receive reports for new sensitive actions in your organization at most once every 30 days. If there have not been any sensitive actions in your organization for a long time, you might receive the one-hour report the next time a sensitive action is observed.

### When Sensitive Actions are not produced

Google Cloud reports sensitive actions only if the principal that performs the action is a user account. Actions taken by a [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) are not reported. Google developed this capability to protect against adversaries who gain access to end-user credentials and use those to take unwanted actions in cloud environments. Because many of these actions are common behavior for service accounts, logs and advisory notifications are not produced for these identities.

To help the appropriate teams receive critical alerts in the Security category promptly, configure custom contacts using [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

Sensitive actions cannot be detected if you have configured your Admin Activity Audit Logs to be located in a specific region (that is, not the `global` region). For example, if you have [specified a storage region](https://docs.cloud.google.com/logging/docs/default-settings#specify-region) for the `_Required` logs bucket in a certain resource, logs from that resource cannot be scanned for sensitive actions.

If you have configured your Admin Activity Audit Logs to be encrypted with [customer-managed encryption keys](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage), your logs cannot be scanned for sensitive actions.

### Sensitive Actions in Security Command Center

If you use Security Command Center, you can receive Sensitive Actions as findings through the Sensitive Actions Service.

Although the Sensitive Actions logs and Advisory Notifications provide one lens on account behavior in your organization, Security Command Center provides additional insight and management capabilities for security teams who are protecting more complex, large, or important workloads and environments. We recommend monitoring Sensitive Actions as one piece of your overall security monitoring strategy.

For more information about Security Command Center, see the following:

  * [Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview)
  * [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



### Pricing

Notifications for Sensitive Actions in Advisory Notifications are provided at no additional charge. Sensitive Actions logs in Cloud Logging incur ingestion and storage costs in accordance with [Logging pricing](https://cloud.google.com/stackdriver/pricing). The volume of Sensitive Actions log entries depends on how often user accounts in your organization perform sensitive actions. These actions are typically uncommon.

## Types of Sensitive Actions

Google Cloud informs you of the following types of sensitive actions.

### `Sensitive Roles Added`

A principal with an Owner (`roles/owner`) or Editor (`roles/editor`) IAM role was granted at the organization level. These roles permit a large number of actions across your organization.

### `Billing Admin Removed`

A Billing Account Administrator (`roles/billing.admin`) IAM role was removed at the organization level. Removing this role can prevent users from having visibility into billing activity and provide a mechanism for an adversary to remain undetected.

### `Organization Policy Changed`

An [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) was created, updated, or deleted at the organization level. Organization policies at this level can affect the security of all your organization's Google Cloud resources.

### `Project-level SSH Key Added`

A project-level SSH key was added to a Google Cloud project that did not previously have such a key. Project-level SSH keys can grant access to all the virtual machines (VMs) in the project.

### `GPU Instance Created`

A VM with a GPU was created in a project by a person who had not created a GPU instance in that project recently. Compute Engine instances with GPUs can host workloads such as cryptocurrency mining.

### `Many Instances Created`

Multiple VM instances were created by a user in a certain project. Large numbers of VM instances can be used for unexpected workloads such as cryptocurrency mining or denial-of-service attacks.

### `Many Instances Deleted`

Multiple VM instances were deleted by a user in a certain project. Large numbers of instance deletions can disrupt your business.

## What's next

  * Learn how to [view notifications](https://docs.cloud.google.com/advisory-notifications/docs/quickstart).
  * Learn how to [respond to Sensitive Actions notifications](https://docs.cloud.google.com/advisory-notifications/docs/respond-to-sensitive-actions).
  * Learn how to [opt in to or out of notifications](https://docs.cloud.google.com/advisory-notifications/docs/opt-in-out-notifications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
