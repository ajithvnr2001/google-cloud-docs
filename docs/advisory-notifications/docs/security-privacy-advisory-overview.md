---
url: https://docs.cloud.google.com/advisory-notifications/docs/security-privacy-advisory-overview/
title: Overview of Security and Privacy Advisory notifications \u00a0|\u00a0 Advisory Notifications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:23.937378+00:00
---

# Overview of Security and Privacy Advisory notifications  |  Advisory Notifications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/advisory-notifications/docs/security-privacy-advisory-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Advisory Notifications ](https://docs.cloud.google.com/advisory-notifications/docs)
  * [ Guides ](https://docs.cloud.google.com/advisory-notifications/docs/overview)



Send feedback 

#  Overview of Security and Privacy Advisory notifications Stay organized with collections  Save and categorize content based on your preferences. 

The Advisory Notifications service uses Security and Privacy Advisory notifications to inform you of critical security and privacy events.

## Who receives Security and Privacy Advisory notifications

Advisory Notifications contacts different users depending on whether the notification is sent to an organization or project.

### Organization contacts

Advisory Notifications integrates with Essential Contacts to identify which users should receive notifications. Essential Contacts lets you control who receives notifications by providing a list of contacts. Security and privacy advisory notifications are sent to contacts in the **Security** and **All** categories at the **organization level**. For more information, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

If Essential Contacts hasn't been configured, Advisory Notifications sends notifications to the default contacts, which are determined by Identity and Access Management roles.

If one or more users have been granted the **Organization Administrator** role (`roles/resourcemanager.organizationAdmin`) on the organization, only they are contacted. If no users have been granted the **Organization Administrator** role, then Advisory Notifications moves on to the next role in the hierarchy and determines if one or more users have been granted the **Owner** basic role (`roles/owner`) on any project owned by the organization. If any are found, only they are contacted. Finally, if no users have been granted the **Organization Administrator** or **Project Owner** role, Advisory Notifications contacts any users who have been granted the **Billing Account Administrator** role (`roles/billing.admin`) on any billing account owned by the organization.

### Project contacts

When a notification is sent to a project, Advisory Notifications contacts Identity and Access Management roles in the following order. If one or more users have been granted the **Owner** basic role (`roles/owner`) on the project, only they are contacted. Otherwise, if no users have been granted the **Project Owner** role, Advisory Notifications contacts any users who have been granted the **Billing Account Administrator** role (`roles/billing.admin`) on the billing account associated with the project, if it exists.

## Opting out

Security and Privacy Advisory notifications are mandatory. You cannot opt out of receiving these notifications.

## What's next

  * Learn about [Sensitive Actions](https://docs.cloud.google.com/advisory-notifications/docs/sensitive-actions-overview) notifications.
  * Learn how to [view notifications](https://docs.cloud.google.com/advisory-notifications/docs/quickstart).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
