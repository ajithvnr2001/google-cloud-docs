---
url: https://docs.cloud.google.com/resource-manager/docs/managing-notifications/
title: Set up notification preferences \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:01.733148+00:00
---

# Set up notification preferences  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/managing-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Set up notification preferences Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to associate a domain with a project for verification purposes (required for push notifications from APIs), and also how to manage your personal notification preferences for maintenance and upgrades.

The **Communication** page in the Google Cloud console lets you manage your personal user preferences for product-specific notifications, such as upcoming maintenance windows and upgrade notifications. These preferences apply only to your user account for individual projects. Your personal preferences can't be set at the folder or organization level and don't inherit to child resources.

To control who receives organization-wide and project-level notifications for critical areas like billing, security alerts, and legal notices, use [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts). You can configure Essential Contacts on organizations, folders, or projects, and contacts inherit down the resource hierarchy. To configure or modify those contacts, see [Manage Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/manage-essential-contacts).

## Associate a domain with a project

Domain verification ensures that push notifications delivered from [Pub/Sub](https://docs.cloud.google.com/pubsub/overview) and other Google APIs are sent only to domains associated with the subscribing project. It serves as abuse prevention, to stop anyone from sending messages to someone else's domain.

To associate a domain with a project, follow the steps for the API from which you're receiving push notifications.

  * For Pub/Sub, see the [Subscriber Guide](https://docs.cloud.google.com/pubsub/subscriber).

  * For other APIs, see the following:

    * [Google Drive Push Notifications](https://developers.google.com/drive/v3/web/push)

    * [Google Calendar Push Notifications](https://developers.google.com/calendar/v3/push)




## Required permissions

To access the **Communication** page, you need the following permissions on the project:

  * `cloudnotifications.activities.list`
  * `resourcemanager.projects.get`



## Manage notification preferences

To opt into, or out of, product notifications:

  1. Go to the **Communication** page in the Google Cloud console: 

[Go to the Communication Page](https://console.cloud.google.com/user-preferences/communication)

  2. By default, any changes you make apply only to the current project. To select additional projects, click the drop-down list of projects, and select the projects you want to update. The **Communication** page only configures project-level preferences and doesn't support folder or organization-level settings.

  3. A toggle indicates whether each type of notification is check_circle **On** or circle **Off**. Click the toggles to turn each notification on or off.




Changes to notifications are automatically saved. When you're finished making changes, you can navigate away from the page or close the browser window. To receive mobile notifications, you must install the [Google Cloud console mobile app](https://play.google.com/store/apps/details?id=com.google.android.apps.cloudconsole).

## What's next

  * Learn about [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) to manage organization-wide contacts and review [best practices](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#best-practices).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
