---
url: https://docs.cloud.google.com/looker/docs/following-alerts/
title: Following alerts \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:10.456505+00:00
---

# Following alerts  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/following-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Following alerts Stay organized with collections  Save and categorize content based on your preferences. 

If you have the appropriate user [permissions](https://docs.cloud.google.com/looker/docs/alerts-for-admins), you can "follow" an alert so that you receive an email notification when its conditions are triggered. You automatically follow any email alert on which you are listed as a recipient.

## Following alerts

To follow another user's alert, click the add_alert **Alerts** icon to open the list of alerts, and click the **Follow** button next to the alert that you want to receive a notification for. You'll [receive an alert notification](https://docs.cloud.google.com/looker/docs/receiving-alerts) to wherever the alert is configured to send notifications.

Some alerts cannot be followed, including:

  * Alerts marked [**Private**](https://docs.cloud.google.com/looker/docs/creating-alerts#setting_alert_permissions) by their creators
  * Alerts that have settings that cannot be exposed for security reasons
  * Alerts to the Slack or Slack Attachment (API Token) integrations



## Unfollowing alerts

To stop receiving notifications when the alert is triggered, click the **Unfollow** button next to the alert in the alert view window. You can also [unsubscribe](https://docs.cloud.google.com/looker/docs/glossary#unsubscribe) directly from the alert notification by clicking **Unfollow this alert** at the bottom of your alert email.

**Note:** If you unfollow an alert that uses an email notification, you'll be removed from its recipient list. You can still view the alert from the list of alerts on a tile; or, if you created the alert, you can view its information on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts).

## Alerts that are not eligible for following

Some types of alerts cannot be viewed or followed by other users for security purposes. When you create these alerts, you won't be able to view or set the alert [permissions](https://docs.cloud.google.com/looker/docs/creating-alerts#setting_alert_permissions). An alert does not permit following if it meets one or more of these conditions:

  * The alert is based on any models with [database connection strings](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#connections) that contain user attributes.
  * The alert is based on an [Explore](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#user_attributes_adapt_filters_to_the_user), a Look, a [dashboard](https://docs.cloud.google.com/looker/docs/dashboards), or a [LookML dashboard](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards) that uses [filters](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#filters) that are based on user attributes.
  * The alert is based on any models with [access grants](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant).



> If you create a **Public** alert based on a model that does not meet any of these conditions and you later update the model or filter so that the alert does meet one or more of these conditions, then the alert remains **Public** and users may still follow it.

### Following and Slack alerts

Alerts to the Slack and Slack Attachment (API Token) integrations cannot be followed by default, and the **Follow** button next to the alert will be disabled. However, users with [permissions to create alerts](https://docs.cloud.google.com/looker/docs/alerts-for-admins) and access to the specific Slack channels in the alert settings can duplicate Slack alerts that are marked **Public**.

## Viewing alerts from the Manage Alerts user page

You can view additional details and history information about alerts you are following that are set on [dashboard tiles](https://docs.cloud.google.com/looker/docs/viewing-dashboards#alerts) from the [**Alert Details** page](https://docs.cloud.google.com/looker/docs/user-alerts#viewing_the_alert_details_page), available on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-31 UTC."],[],[]] 
