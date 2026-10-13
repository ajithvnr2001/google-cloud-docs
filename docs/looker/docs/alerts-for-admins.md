---
url: https://docs.cloud.google.com/looker/docs/alerts-for-admins/
title: Configuring alerts for Looker users \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:20.538692+00:00
---

# Configuring alerts for Looker users  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/alerts-for-admins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Configuring alerts for Looker users Stay organized with collections  Save and categorize content based on your preferences. 

Looker has several user permissions that are associated with alerts. Some permissions determine what the user can do with alerts; others determine what destinations a user can send an alert notification to. See the [Roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) documentation page for more information about Looker permissions, including dependencies.

Looker user permissions are distinct from the alert setting called [**Permissions**](https://docs.cloud.google.com/looker/docs/creating-alerts#setting_alert_permissions), which lets the alert's creator determine whether other users will be able to view and potentially follow the alert.

In addition to the permissions that are described in the following table, users need `see_looks` permissions and `see_user_dashboards` and/or `see_lookml_dashboards` permissions for the models on which the dashboard or LookML dashboard tiles, respectively, are based.

Permission | Lets Users | Notes  
---|---|---  
[`admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) | 

  * See the tile's bell icon: The numeric indicator shows the total number of enabled public alerts on the tile
  * Manage alerts from the [**Alerts**](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alerts) management admin page, even [private](https://docs.cloud.google.com/looker/docs/creating-alerts#setting_alert_visibility) alerts that are created by other users
  * Access the [**Alert History**](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alert-history) admin page
  * View, follow, edit, self-assign, and disable any alert on the Looker instance 

| The user must be signed in to Slack from Looker to see alerts that send Slack notifications.  
[`see_alerts`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_alerts) | 

  * Access the [**Alerts**](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alerts) management admin page
  * View, follow, edit, self-assign, disable any alert on the Looker instance, even [private](https://docs.cloud.google.com/looker/docs/creating-alerts#setting_alert_visibility) alerts that are created by other users
  * Access the [**Alert History**](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alert-history) admin page


* Users must have permissions to access the alert's underlying content to view or explore from the alert's visualization (in the [**Alert Details**](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alerts#alert_details_page) page) or to navigate to its dashboard.
* This permission does _not_ grant the ability to create, follow, or delete alerts from the dashboard tile.  
[`create_alerts`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_alerts) | 

  * See the tile's bell icon: The numeric indicator shows the sum of any public or private alerts that the user has created and other users' alerts that are marked **Public**
  * From the dashboard tile: create, duplicate, and delete their own alerts; duplicate alerts marked **Public** by other users
  * View, edit, disable, and enable their alerts on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts)

| The user must be signed in to Slack to see alerts that send Slack notifications.  
[`follow_alerts`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#follow_alerts) | 

  * View and follow [public](https://docs.cloud.google.com/looker/docs/alerts-overview#setting_alert_permissions), [followable](https://docs.cloud.google.com/looker/docs/following-alerts) alerts on a dashboard tile
  * View the alerts that they have followed or for which they are listed as a recipient from the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts)

|   
[`schedule_look_emails`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#schedule_look_emails) | Send email notifications | Users must also have `create_alerts` permissions.  
[`schedule_external_look_emails`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#schedule_external_look_emails) | Send notifications to emails with any domain | Users must also have `create_alerts` permissions.  
[`send_to_integration`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#send_to_integration) | Send alert notifications to the [Slack](https://docs.cloud.google.com/looker/docs/scheduling-slack) or [Slack Attachment (API Token)](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-Looker-slack-attachment-api-token-action) integrations, if enabled for the Looker instance | Users must also have `create_alerts` permissions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
