---
url: https://docs.cloud.google.com/looker/docs/alerts-overview/
title: Alerts overview \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:20.443176+00:00
---

# Alerts overview  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/alerts-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Alerts overview Stay organized with collections  Save and categorize content based on your preferences. 

With alerts, you can specify conditions in your data that, when met or exceeded, trigger a notification to be sent to specific recipients at a predetermined frequency.

## Alerts overview

Alerts are set on [query-based](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#query_tiles) or [Look-linked](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#look-linked_tiles) tiles on [dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards). Based on the alert's [frequency](https://docs.cloud.google.com/looker/docs/creating-alerts#setting_alert_frequency), Looker checks whether each alert's conditions have been met or exceeded; if so, Looker notifies users of this change.

In addition to creating alerts, users can view, duplicate, and follow some alerts created by other users, depending on their [permissions](https://docs.cloud.google.com/looker/docs/alerts-for-admins). Alert conditions will also take into account any [dashboard filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards) that exist when the alert is created.

Depending on the dashboard tile's visualization type and the kinds of fields that are present in the visualization, Looker checks your data in different ways. When you create an alert, it will be one of these types:

  * _Single value alerts_ (used only with single value visualizations) — Looker checks the data based on the value that is used in the visualization, which is the first row of the results table.

**Note:** For [single value visualizations](https://docs.cloud.google.com/looker/docs/single-value-options), the notification will include the single value as text, rather than a PNG of the visualization.
  * _Time series alerts_ (used when there is a date or time dimension in the query results) — Looker checks all new rows that have not been seen before (based on the date or time dimension in the query).

  * _Categorical alerts_ (neither single value nor time series) — Looker checks all rows and pivot values unless a specific row or pivot value was selected when the alert was created.




## Limits of alerts

The following limitations apply to alerts that are created on dashboard tiles:

  * Alerts can be set only on tiles that have at least one [numeric measure](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number) or [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations) in the tile's visualization. The visualization type and the fields that are present in the dashboard tile visualization determine whether you can set an alert condition that is based on a single field or table calculation value or on "any" field or table calculation value.
  * Alerts that are based on a table calculation that includes a row total are not supported.
  * You can only create an alert when viewing the dashboard. The add_alert **Alerts** icon isn't visible when in [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  * You can only create an alert when in [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode).
  * Alerts to the [Slack](https://docs.cloud.google.com/looker/docs/creating-alerts#sending_alerts_to_the_slack_integration) and [Slack Attachment (API Token)](https://docs.cloud.google.com/looker/docs/creating-alerts#sending_alerts_to_the_slack_attachment_api_token_integration) integrations cannot be followed; however, if you are creating an alert to one of these destinations and mark it **Public** , other users will be able to see and duplicate your alert settings.



## Alerts documentation

See the following links for documentation that is relevant to the Admin role and to all Looker users.

### Alerts documentation for Looker admins

Looker admins play critical roles in configuring alert permissions so that Looker users can create and follow alerts to receive alert notifications.

  * [Configuring alerts for Looker users](https://docs.cloud.google.com/looker/docs/alerts-for-admins) discusses how to configure permissions for creating, following, and managing alerts. [Alerts](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alerts) discusses the **Alerts** page in the **Alerts & Schedules** section of the **Admin** panel, where admins can see and manage all active and inactive alerts for the Looker instance.
  * [Alert History](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alert-history) discusses the **Alert History** page in the **Alerts & Schedules** section of the **Admin** panel, which lists information about all active alerts that are running, complete, or failed.



### Alerts documentation for Looker users

  * [Viewing alerts](https://docs.cloud.google.com/looker/docs/viewing-alerts) discusses how to view alerts on a dashboard tile.
  * [Following alerts](https://docs.cloud.google.com/looker/docs/following-alerts) discusses how to follow alerts to receive notifications when alerts are triggered.
  * [Creating alerts](https://docs.cloud.google.com/looker/docs/creating-alerts) discusses how to create an alert.
  * [Modifying alerts](https://docs.cloud.google.com/looker/docs/modifying-alerts) discusses how to edit an existing alert.
  * [Receiving alert notifications](https://docs.cloud.google.com/looker/docs/receiving-alerts) discusses what information is sent in an alert notification.
  * [Effect of dashboard edits on alerts](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts) discusses how changes made to dashboard affect any alerts associated with that dashboard.
  * [Viewing alerts that you own or follow](https://docs.cloud.google.com/looker/docs/user-alerts) discusses the **Manage Alerts** page in the Looker UI, which shows a list of all the alerts that a user owns or follows, or for which they are listed as a recipient, depending on their [alerts permissions](https://docs.cloud.google.com/looker/docs/alerts-for-admins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
