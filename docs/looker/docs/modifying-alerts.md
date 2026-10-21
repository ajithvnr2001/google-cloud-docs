---
url: https://docs.cloud.google.com/looker/docs/modifying-alerts/
title: Modifying alerts \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:25:18.734106+00:00
---

# Modifying alerts  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/modifying-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Modifying alerts Stay organized with collections  Save and categorize content based on your preferences. 

This documentation page is about modifying alert settings. For information about modifying the dashboard or dashboard tile on which an alert is based, see the [Effect of dashboard edits on alerts](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts) documentation page.

If you have the appropriate user [permissions](https://docs.cloud.google.com/looker/docs/alerts-for-admins), you can modify alerts on [query-based](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#query_tiles) or [Look-linked](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#look-linked_tiles) tiles on user-defined dashboards or [LookML dashboards](https://docs.cloud.google.com/looker/docs/reference/lookml-dashboard-overview).

You can edit, duplicate, or delete the alerts that you have created. Admins can edit, duplicate, delete, or [pause](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alerts#status) any alert, even [private](https://docs.cloud.google.com/looker/docs/creating-alerts#setting_alert_visibility) alerts that were created by other users.

Modifying alert settings also changes those settings for users who follow the alert.

![](https://docs.cloud.google.com/static/looker/docs/images/modal-alert-edit-2214.png)

## Editing an alert

**Note:** Only Looker admins can edit alerts that send notifications to Slack.

To edit an alert, follow these steps:

  1. Select the **Alerts** icon on the dashboard tile to open the alert view dialog.
  2. Select the three-dot **Alert Options** menu.
  3. Select **Edit Alert** to open a dialog where you can edit the existing alert settings. Refer to the [Creating alerts](https://docs.cloud.google.com/looker/docs/creating-alerts) documentation page for more information about alert settings.
  4. When you're finished editing the alert settings, select **Save Alert**.



## Duplicating an alert

Duplicating an alert creates a new alert with identical settings to the original alert. The duplicated alert query will check if conditions are triggered based on the dashboard and tile settings at the time the _original_ alert was created. If any user has made changes to the dashboard or tile since the creation of the original alert, the duplicated alert may not reflect those changes. See the [Effect of dashboard edits on alerts](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts) documentation page for more information about what changes are incorporated into alert settings.

To duplicate an alert, follow these steps:

  1. Select the **Alerts** icon on the dashboard tile to open the alert view dialog.
  2. Select the three-dot **Alert Options** menu.
  3. Select **Duplicate** to open a dialog that is pre-populated with the existing alert settings, and then select **Create Alert**.



You _cannot_ duplicate another user's Slack alert delivery settings if either of these conditions is true:

  * The alert sends Slack notifications to a Slack channel that is not available to you. You must configure your own Slack delivery settings.
  * You don't have `send_to_integration` permissions.



Attempting to duplicate an alert in either of these cases will result in this displayed message:
    
    
    This alert delivers notifications to a destination that is not available to you.
    Click **Clear** to reset to default.
    

## Deleting an alert

**Note:** Only Looker admins can delete alerts that send notifications to Slack.

To delete an alert, follow these steps:

  1. Select the **Alerts** icon on the dashboard tile to open the alert view dialog.
  2. Select the three-dot **Alert Options** menu.
  3. Select **Delete** , and then confirm deletion in the resulting window.
  4. Select **Done** to close the alert view window.



Admins will see immediately that the name of the dashboard has been replaced with a **-** for the alert on the [**Alert History** page](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alert-history) of the **Admin** panel and that it has been deleted for the alert on the [**Alerts** page](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alerts) of the **Admin** panel. After the next time the alert query runs, the alert will be removed from the **Alert History** page of the **Admin** panel. On the **Alerts** admin page, the status shows as **Paused** with a tooltip message that indicates that the dashboard or dashboard element (tile) has been deleted.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
