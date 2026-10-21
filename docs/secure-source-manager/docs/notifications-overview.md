---
url: https://docs.cloud.google.com/secure-source-manager/docs/notifications-overview/
title: Notifications overview \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:06.728946+00:00
---

# Notifications overview  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/notifications-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Notifications overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the behavior of notifications in Secure Source Manager. For instructions on how to set up notifications, see [Set up notifications](https://docs.cloud.google.com/secure-source-manager/docs/set-up-notifications).

Secure Source Manager notifications are disabled by default. When enabled, notifications are sent to your Secure Source Manager login email.

## Limitations

The following limitations apply to email notifications in Secure Source Manager:

  * Email notifications aren't available for Workforce Identity Federation users.
  * The email address that notifications are sent to is the same as your Secure Source Manager login email address, and can't be changed.



## Events that trigger notifications

The following issue events and pull request events can trigger notifications in Secure Source Manager when notifications are enabled:

Issues:

  * An issue is created
  * An issue is assigned
  * An issue has a new comment
  * An issue is closed
  * An issue is reopened



Pull requests:

  * A pull request is created
  * A pull request is assigned
  * A pull request has a new comment
  * A pull request is approved
  * A pull request is merged
  * A pull request is rejected
  * A pull request is closed
  * A pull request is reopened



## Notifications for participants

You can choose to be notified for events in issues and pull requests that you are a participant of.

For example, if you're the author or assignee of a pull request, you're a participant in that pull request, and events in that pull request send you notifications if you have enabled notifications for pull requests.

The following list gives some examples of actions that make you a participant in an issue or pull request:

  * You're the author of the pull request or issue.
  * You're CC'd on the pull request or issue.
  * You comment on the pull request or issue.
  * You're mentioned in the pull request or issue.



## Notifications for non-participants

After enabling notifications, you can choose to receive notifications from events in issues or pull requests that you're not participating in by _watching_ a repository. When a repository is watched, notifications are sent for all enabled events, even if you're not a participant in the issue or pull request where the event occurred.

For example, if `user1@example.com` has enabled notifications for pull requests, and watched a repository, and `user2@example.com` creates a pull request in that repository, a notification is sent to `user1@example.com`.

Repositories are not watched by default, except by the repository creator. When you create a new repository, that repository is watched by default and notifications are sent to you for events if you have notifications enabled.

## What's next

  * [Set up notifications](https://docs.cloud.google.com/secure-source-manager/docs/set-up-notifications) in Secure Source Manager.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
