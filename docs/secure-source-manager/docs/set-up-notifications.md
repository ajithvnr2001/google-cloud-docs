---
url: https://docs.cloud.google.com/secure-source-manager/docs/set-up-notifications/
title: Set up notifications \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:25.083702+00:00
---

# Set up notifications  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/set-up-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Set up notifications Stay organized with collections  Save and categorize content based on your preferences. 

Secure Source Manager can send email notifications to your login email address for issue and pull request related events. For a full list of events that can send notifications, see [Notifications overview](https://docs.cloud.google.com/secure-source-manager/docs/notifications-overview).

## Limitations

The following limitations apply to email notifications in Secure Source Manager:

  * Email notifications aren't available for Workforce Identity Federation users.
  * The email address that notifications are sent to is the same as your Secure Source Manager login email address, and can't be changed.



## Before you begin

  1. [Create a Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance).
  2. [Create a Secure Source Manager repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository).



### Required roles

To get the permissions that you need to enable notifications, ask your administrator to grant you the [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) IAM role on the Secure Source Manager instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable or disable notifications

To enable or disable email notifications in Secure Source Manager, do the following:

  1. In the Secure Source Manager web interface, click the more_vert **more options** menu.
  2. Click **Notification settings**.
  3. Click the **Enabled** toggle to turn your notifications on or off.
  4. Select which events you want to send you notifications.

Notifications for selected events are sent to you if you are a participant in the issue or pull request where the event occurred. To be notified for events where you aren't a participant, you need to watch the individual repository.

  5. Click **Update** to save your notifications settings.




## Watch or unwatch a repository

To get notifications for events in a repository, even if you aren't a participant in the issue or pull request where the event occurred, you can watch the repository.

To watch or unwatch a repository, do the following:

  1. Navigate to the repository you want to watch.
  2. Click the notifications_off **Notifications** icon to toggle notifications on or off for the repository.



## What's next

  * [Work with issues and pull requests](https://docs.cloud.google.com/secure-source-manager/docs/work-with-issues-pull-requests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
