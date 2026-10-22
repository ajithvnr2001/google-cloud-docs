---
url: https://docs.cloud.google.com/looker/docs/creating-alerts/
title: Creating alerts \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:38.334438+00:00
---

# Creating alerts  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/creating-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Creating alerts Stay organized with collections  Save and categorize content based on your preferences. 

If you have the appropriate user [permissions](https://docs.cloud.google.com/looker/docs/alerts-for-admins), you can create alerts on [query-based](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#query_tiles) or [Look-linked](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#look-linked_tiles) tiles on user-defined dashboards or [LookML dashboards](https://docs.cloud.google.com/looker/docs/reference/lookml-dashboard-overview).

## Creating an alert

To create an alert on a dashboard tile, click the tile's add_alert **Alerts** icon and then click the **New** button at the bottom of the list of the existing [alerts that you are permitted to see](https://docs.cloud.google.com/looker/docs/alerts-for-admins) (you may need to scroll to see the entire list). If no alerts are configured for that tile yet, or if you don't have permission to see any existing alerts on that tile, hold the pointer over the dashboard tile to reveal the add_alert **Alerts** icon. Click the add_alert **Alerts** icon on the dashboard tile to open the alert creation dialog.

**Note:** Alerts cannot be configured directly on a Look page. Alerts are designed to be set exclusively on tiles within a dashboard. To set an alert based on a Look, follow these steps:

  1. Add the Look as a tile to a dashboard.
  2. Navigate to the dashboard and locate the specific tile.
  3. Click the add_alert **Alerts** icon on the tile to configure and create the alert conditions.



![](https://docs.cloud.google.com/static/looker/docs/images/modal-alert-create-2300.png)

In the alert creation window, you can specify several components of your alert:

  * Custom title
  * Alert conditions
  * Recipients
  * Frequency
  * Permissions (this setting is also dictated by whether the alert is configured to allow [following](https://docs.cloud.google.com/looker/docs/following-alerts#unfollowable_alerts))
  * Gemini-powered analytics



Each alert query captures the dashboard and tile settings at the time the alert was created. However, an alert syncs with many of the common types of changes that you or other users make to its underlying dashboard or tile — without the need to recreate the alert. See the [Effect of dashboard edits on alerts](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts) documentation page for more information.

## Naming an alert

The default alert title indicates which conditions need to be true for the alert to be triggered. If you want to rename your alert, follow these steps:

  1. Click the three-dot menu, and then click **Edit Alert**.
  2. Click once on the alert title.
  3. Enter a custom title, and then click away from the field or hit the **Enter** key to see your update.
  4. Click **Save Alert** to save your new title.



Your custom alert title will appear in any publicly visible alerts that are listed in the alert view window on that tile. The custom title will also appear in the alert [notifications](https://docs.cloud.google.com/looker/docs/receiving-alerts).

Hover over the custom title of any alert in the alert view window to see the conditions that trigger that alert.

## Setting alert conditions

In the **Condition** drop-downs in the alert creation window, you can set the components that tell Looker how to check the tile data for changes and the kinds of changes that trigger an alert notification.

The alert condition is represented by these components:

  * The list of fields or table calculations that appear in the dashboard tile's visualization
  * The change that the selected field, fields, table calculation, or table calculations must undergo to trigger the alert notification
  * The magnitude of the change that would trigger the alert notification



These conditions include the following:

  * **Is greater than**
  * **Is less than**
  * **Is equal to**
  * **Is greater than or equal to**
  * **Is less than or equal to**



If the query contains a date or time field, these additional conditions are available:

  * **Increases by**
  * **Decreases by**
  * **Changes by** (a combination of **Increases by** and **Decreases by**)

**Caution:** Using these comparison conditions with time series data has some additional considerations. For more information, see this Best Practices page on [Setting alerts based on time series data](https://docs.cloud.google.com/looker/docs/best-practices/how-to-set-alerts-based-on-time-series-data).

You can create alerts that are based on comparisons of whole number and decimal data values only. To set alerts that are based on percentage changes of data values, see the [Setting alert conditions based on percentage changes of data values](https://docs.cloud.google.com/looker/docs/best-practices/how-to-set-alerts-based-on-percentage-changes) best practices page.

## Setting alert notifications

Under the **Where to send it** section of the alert creation window, you can specify the destination of the alert notification.

### Sending alerts to email

To send your alert notifications to email, select **Email** from the **Where to send it** drop-down. You can designate the recipients of the alert email notification. Your email will be listed by default, and you can modify the list of recipients as necessary. Your permissions determine which email domains you're able to send alert notifications to. Although there is no limit to the number of recipients that you can notify, if your organization is using an external SMTP server, the server may have its own daily or per-message recipient limits.

Each recipient will [receive an email](https://docs.cloud.google.com/looker/docs/receiving-alerts#alert_notifications_to_email) with information about the alert and an option to unfollow the alert. If they choose to unfollow the alert, their email address will be removed from the recipient list. Each recipient will also receive a [push notification](https://docs.cloud.google.com/looker/docs/mobile-app-alerts#push-notifications) to their mobile device if the following is true:

  * The Looker instance has the [Looker mobile application enabled](https://docs.cloud.google.com/looker/docs/mobile-app-enablement).
  * The Looker instance is on Looker 26.6 or later.
  * The user has the [Looker mobile application](https://docs.cloud.google.com/looker/docs/mobile-app-installation) installed on their mobile device.



#### Include custom link

For [embedded dashboards](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding), you can customize the URL that you provide for recipients to link back to Looker. To use this option, a Looker admin or a user with either the `schedule_look_emails` or the `create_alerts` permission first must specify allowed domains for the custom link and select the format of the custom link URL in the [**Embed**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#alerts_and_scheduling_custom_url) page in the **Admin** menu.

  * In the **Domain** field, select one of the available domains.
  * In the **Path** field, enter a path to the dashboard, such as `/dashboards/12` or `/reports/salesoverview`. The **Path** option is displayed only if **User defined URL** is selected in the **Select content path** field on the [**Embed**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#alerts_and_scheduling_custom_url) page in the **Admin** menu.
  * In the **URL label** field, optionally enter new text for the link that points to the content. This field will display any text that is entered in the **URL label** field in the [**Embed**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#alerts_and_scheduling_custom_url) page in the **Admin** menu by default and can be changed in this field.



### Sending alerts to the Slack Attachment (API Token) integration

The [Slack Attachment (API Token) action](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-looker-slack-attachment-api-token-action) is available from the [Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub). When this action is enabled on the **Actions** page in the **Admin** panel, **Slack Attachment (API Token)** will show up as an option in the **Where to send it** drop-down of the alert creation window.

**Note:** Admins of customer-hosted instances that use a self-hosted action hub server must restart their action hub server when they update their Looker instance.

Once a Looker admin has [enabled the Slack Attachment (API Token) action](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions) and the [Looker app bot user](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-looker-slack-attachment-api-token-action) has been set up in Slack, you can follow these steps to send alert notifications to Slack by using the Slack Attachment (API Token) integration:

  1. Select **Slack Attachment (API Token)** from the **Where to send it** drop-down.

The **Channel Type** and **Share In** fields will appear.

![](https://docs.cloud.google.com/static/looker/docs/images/modal-alert-create-slack-attachment-channel-2220.png)

**Note:** Even if embed users have permissions to send alert notifications to the Slack Attachment integration, they won't see the **Slack Attachment (API Token)** in the **Where to send it** drop-down unless their Slack workspace is configured for the Looker app bot user.
  2. Use the **Channel Type** field to specify the type of Slack recipient for the alert:

     * **Channels** : Send the alert to a Slack channel
     * **Users** : Send the alert in a direct message to a Slack user

Once you've selected the channel type, the **Share In** field is populated with the channel or direct message options that are applicable to the credentials of the [Looker app bot user](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-looker-slack-attachment-api-token-action) in the Slack workspace.

  3. In the **Share In** field, select the direct message or channel that you want to send the alert notification to. The selected user or channel will receive a [notification](https://docs.cloud.google.com/looker/docs/receiving-alerts#alert_notifications_to_slack) with information pertaining to the tile that the alert is set on:

     * A PNG image of the dashboard tile visualization
     * A message with the name of the dashboard or the custom alert title and the conditions that triggered the alert
     * A link to navigate to the tile's dashboard
     * A link to unsubscribe from the alert notification
**Note:** For [single value visualizations](https://docs.cloud.google.com/looker/docs/single-value-options), the notification will include the single value as text, rather than a PNG of the visualization.



### Sending alerts to the Slack integration

The [Slack action](https://docs.cloud.google.com/looker/docs/scheduling-slack) is available from the [Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub). When this action is enabled on the **Actions** page in the **Admin** panel, **Slack** will show up as an option in the **Where to send it** drop-down of the alert creation window. A Looker admin must also connect at least one Slack workspace to the Looker instance.

> The Slack integration is available to Looker-hosted deployments that satisfy these conditions:
> 
>   * The instance is on Looker 6.24 or later.
>   * The [IP Allowlist](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist) feature is not enabled on the Looker instance.
> 

> 
> This Slack integration is not supported for [customer-hosted](https://docs.cloud.google.com/looker/docs/glossary#customer-hosted) instances.

To enable installation of the Looker app, your Slack workspace owner may need to [adjust the app installation settings](https://slack.com/help/articles/222386767-Manage-app-installation-settings-for-your-workspace) for your Slack workspace.

Once a Looker admin has [enabled the Slack action](https://docs.cloud.google.com/looker/docs/scheduling-slack#enabling_the_integration_in_the_looker_action_hub) and [connected the appropriate Slack workspaces](https://docs.cloud.google.com/looker/docs/scheduling-slack#managing_slack_workspace_connections_to_looker), you can send alert notifications to Slack by following these steps:

  1. Select **Slack** from the **Where to send it** drop-down.

If you have not already authenticated into Slack, a **Sign in with Slack** button appears under the **Where to send it** drop-down.

![](https://docs.cloud.google.com/static/looker/docs/images/modal-alert-create-slack-signin-2220.png)

  2. Click **Sign in with Slack**. Looker will request access to the Slack workspace. If your Looker admin has connected multiple Slack workspaces to your Looker instance, a drop-down menu appears in the upper right of the OAuth page. Select the appropriate Slack workspace from the drop-down. Click **Allow**.

> You can also authenticate into Slack from your [personal account page](https://docs.cloud.google.com/looker/docs/scheduling-slack#authenticating_into_a_slack_workspace_from_the_account_page) in Looker. If your Looker admin has connected multiple Slack workspace to your Looker instance, you'll see a list of workspaces with options to sign in to each one individually.

After you have logged in to at least one Slack workspace, the **Channel Type** and **Share In** fields will appear.

![](https://docs.cloud.google.com/static/looker/docs/images/modal-alert-create-slack-channel-2206.png)

> Even if embed users have permissions to send alert notifications to the Slack integration, unless their Slack workspace is connected to the Looker instance, they won't see the **Slack** option in the **Where to send it** drop-down.

  3. The **Workspace** drop-down shows a list of any workspaces that you're signed in to. Select a workspace from the list. If you don't see the workspace to which you want to send the alert notification, you can see a list of the workspaces that your Looker admin has connected to your Looker instance and sign in to each one individually from your [personal account page](https://docs.cloud.google.com/looker/docs/scheduling-slack#authenticating_into_a_slack_workspace_from_the_account_page) in Looker.

  4. The **Share In** field is populated with the channel and direct message options that are based on the selected Slack workspace. Select the direct message or channel that you would like to send the alert notification to. Anyone in that channel will see a [notification](https://docs.cloud.google.com/looker/docs/receiving-alerts#alert_notifications_to_slack) with information pertaining to the tile that the alert is set on:

     * A PNG image of the dashboard tile visualization
     * A message with the name of the dashboard or the custom alert title and the conditions that triggered the alert
     * A link to navigate to the tile's dashboard
     * A link to [unsubscribe](https://docs.cloud.google.com/looker/docs/glossary#unsubscribe) from the alert notification
**Note:** For [single value visualizations](https://docs.cloud.google.com/looker/docs/single-value-options), the notification will include the single value as text, rather than a PNG of the visualization.



## Setting alert frequency

Under the **Frequency** section of the alert creation window, you can set the frequency at which Looker checks your data for changes (and sends an alert notification if the alert conditions are met). The default frequency is **Daily** at **05:00**. The available frequency options are as follows:

  * **Monthly** on a specified **Day** of the month (the default is the **1st** of the month) at a specified **Time** (the default is **05:00**)
  * **Weekly** on a specified **Day** of the week (the default is **Sun** for Sunday) at a specified **Time** (the default is **05:00**)
  * **Daily** at a specified **Time** (the default is **05:00**)
  * **Hourly** at a specified interval (the default is to check the data every hour) with specified **Start** and **End** times (the default is **05:00** and **17:00**). With hourly intervals you can have Looker check the data at these intervals: 
    * **Hour**
    * **2 hours**
    * **3 hours**
    * **4 hours**
    * **6 hours**
    * **8 hours**
    * **12 hours**
  * **Minutes** at a specified interval (the default is to check the data every 15 minutes) with specified **Start** and **End** times (the default is **05:00** and **17:00**). With minute-based intervals, you can have Looker check the data at these intervals: 
    * **15 minutes**
    * **30 minutes**



**Start** and **End** times are inclusive. For example, if you set **Check every** to **12 hours** with a **Start** time of **05:00** and an **End** time of **17:00** , Looker will check the data at 05:00 _and_ 17:00.

**Note:** Looker sends alerts according to the time zone that is indicated in the [**Application Time Zone**](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#application_time_zone) setting on the Admin **Settings** page, or, if enabled, the alert creator's [User Specific Time Zone](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#user_specific_time_zones).

## Setting alerts permissions

For security reasons, some alerts cannot be viewed or [followed](https://docs.cloud.google.com/looker/docs/following-alerts#unfollowable_alerts) by other users, and you cannot view or set their permissions.

You can set your alert's permissions by selecting the **Public** or **Private** options from the **Permissions** drop-down in the alert creation window. If an alert can be [followed](https://docs.cloud.google.com/looker/docs/following-alerts#unfollowable_alerts), it is marked **Public** by default, which means that any Looker user with [follow permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#follow_alerts) on the dashboard tile's underlying content can see your alert and its settings on the alert view window. They can also follow your alert so that they can receive email notifications when your alert's conditions are triggered.

You can set your alert to **Private** so that its settings are viewable only to you (and admins) by choosing the **Private** option from the **Permissions** drop-down in the alert creation window.

Alerts to the Slack and Slack Attachment (API Token) integrations cannot be followed; however, if you are creating an alert to one of these destinations and mark it **Public** , other users will be able to see and duplicate your alert settings.

## Including key driver analytics

When setting up your alert, you can also specify whether you want the alert notification to include results from **Gemini powered key driver analysis**. This analysis provides insight about the change in your data that triggered the alert, and why that change may have occurred. To include these insights, enable the **Gemini powered key driver analysis** setting when creating or editing the alert. This option is disabled by default.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
