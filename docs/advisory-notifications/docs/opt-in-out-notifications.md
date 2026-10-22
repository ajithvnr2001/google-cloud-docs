---
url: https://docs.cloud.google.com/advisory-notifications/docs/opt-in-out-notifications/
title: Opt in to or out of notifications \u00a0|\u00a0 Advisory Notifications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:48.014155+00:00
---

# Opt in to or out of notifications  |  Advisory Notifications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/advisory-notifications/docs/opt-in-out-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Advisory Notifications ](https://docs.cloud.google.com/advisory-notifications/docs)
  * [ Guides ](https://docs.cloud.google.com/advisory-notifications/docs/overview)



Send feedback 

#  Opt in to or out of notifications Stay organized with collections  Save and categorize content based on your preferences. 

You can configure which notification types your organization or project receives. Opting in to or out of notification types only affects new notifications of that type. If you opt out of a notification type, existing notifications of that type that you have previously received won't be deleted.

## Before you begin

To get the permissions that you need to view or update Advisory Notifications settings, ask your administrator to grant you the [Advisory Notifications Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/advisorynotifications#advisorynotifications.admin) (`roles/advisorynotifications.admin`) IAM role on your project or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view or update Advisory Notifications settings. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view or update Advisory Notifications settings:

  * `advisorynotifications.notifications.list`
  * `advisorynotifications.settings.get`
  * `advisorynotifications.settings.update`
  * If you are configuring notifications for an organization: `resourcemanager.organizations.get`
  * If you are configuring notifications for a project: `resourcemanager.projects.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Opt in to or out of notifications

  1. In the Google Cloud console, go to **Advisory Notifications**.

[Go to Advisory Notifications](https://console.cloud.google.com/security/advisorynotifications)

  2. Click **Settings** in the corner of the panel.

  3. Toggle the notification types you want to receive to **Opt in** , and those you do not want to receive to **Opt out**. You cannot opt out of mandatory notification types.

  4. Click **Save changes**.

  5. Review the changes, and then click **Confirm changes**.




## Mandatory notification types

The following notification types are mandatory and cannot be opted out of:

  * [Security and Privacy Advisory](https://docs.cloud.google.com/advisory-notifications/docs/security-privacy-advisory-overview)
  * [Security MSA](https://docs.cloud.google.com/advisory-notifications/docs/security-msas-overview)



Additional mandatory notification types may be added in the future.

## Optional notification types

The following notification types are optional and can be opted out of:

  * [Sensitive Actions](https://docs.cloud.google.com/advisory-notifications/docs/sensitive-actions-overview)
  * [Threat Horizons](https://docs.cloud.google.com/advisory-notifications/docs/threat-horizons-overview)



Additional optional notification types may be added in the future.

## What's next

  * Learn how to [view notifications](https://docs.cloud.google.com/advisory-notifications/docs/quickstart).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
