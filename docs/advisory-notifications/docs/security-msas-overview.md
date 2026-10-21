---
url: https://docs.cloud.google.com/advisory-notifications/docs/security-msas-overview/
title: Overview of Security MSAs \u00a0|\u00a0 Advisory Notifications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:14.154426+00:00
---

# Overview of Security MSAs  |  Advisory Notifications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/advisory-notifications/docs/security-msas-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Advisory Notifications ](https://docs.cloud.google.com/advisory-notifications/docs)
  * [ Guides ](https://docs.cloud.google.com/advisory-notifications/docs/overview)



Send feedback 

#  Overview of Security MSAs Stay organized with collections  Save and categorize content based on your preferences. 

Security Mandatory Service Announcements (MSA) inform customers about important security updates or changes that are required for continued use of Google Cloud services.

## Who receives Security MSAs

Advisory Notifications contacts different users depending on whether the notification is sent to an organization or project.

### Organization contacts

Advisory Notifications integrates with Essential Contacts to identify which users should receive notifications. Essential Contacts lets you control who receives notifications by providing a list of contacts. Security MSAs are sent to contacts in the **Security** and **All** categories at the organization level. For more information, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

If you haven't configured Essential Contacts, Advisory Notifications sends notifications to the default contacts, which are determined by Identity and Access Management roles.

If you have granted the **Organization Administrator** role (`roles/resourcemanager.organizationAdmin`) to one or more users, only they are contacted. If you haven't granted the **Organization Administrator** role to any user, then Advisory Notifications moves on to the next role in the hierarchy and determines if one or more users have been granted the **Owner** basic role (`roles/owner`) on any project owned by the organization. If any are found, only they are contacted. Finally, if you haven't granted the **Organization Administrator** or **Project Owner** role to any user, Advisory Notifications contacts any user who has been granted the **Billing Account Administrator** role (`roles/billing.admin`) on any billing account owned by the organization.

### Project contacts

When a notification is sent to a project, Advisory Notifications contacts Identity and Access Management roles in the following order. If one or more users have been granted the **Owner** basic role (`roles/owner`) on the project, only they are contacted. Otherwise, if no users have been granted the **Project Owner** role, Advisory Notifications contacts any users who have been granted the **Billing Account Administrator** role (`roles/billing.admin`) on the billing account associated with the project, if it exists.

### Opting out

Security MSAs are mandatory. You cannot opt out of receiving these notifications.

## What's next

  * Learn how to [view notifications](https://docs.cloud.google.com/advisory-notifications/docs/quickstart).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
