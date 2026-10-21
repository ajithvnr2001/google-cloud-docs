---
url: https://docs.cloud.google.com/data-studio/create-alerts-on-a-chart/
title: Create alerts on a chart \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:34:52.525257+00:00
---

# Create alerts on a chart  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-alerts-on-a-chart/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create alerts on a chart Stay organized with collections  Save and categorize content based on your preferences. 

You can set up an alert that will notify you and your stakeholders when a chart on your Data Studio report meets criteria that you specify. The notification includes a link to your original report.

**Data Studio Pro feature**

The features and functionality described in this page are available to Data Studio Pro users.

[Get Data Studio Pro.](https://docs.cloud.google.com/data-studio/about-pro)

## Requirements to use alerts

  * You must have at least the [**Viewer** role](https://docs.cloud.google.com/data-studio/roles-and-permissions) on a report to create an alert.
  * You must have at least the **Viewer** role on the underlying data source of a chart to create an alert on that chart.
  * You must have the [`create_alerts` Looker permission](https://docs.cloud.google.com/looker/docs/alerts-for-admins) to create an alert that is based on a Looker data source.
  * You can only create alerts on Data Studio Pro content. To upgrade your content, see the [Upgrade Data Studio content to Data Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-content-pro) article.



## Create a new alert

  1. View the report that you want to create an alert on. 
     * Make sure that you're in **View** mode. You can't add alerts while you're in **Edit** mode.
     * The report must be a Data Studio Pro report. To upgrade your content, see the [Upgrade Data Studio content to Data Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-content-pro) article.
  2. Hover over the chart that you want to create an alert on, and select the **Create & view alerts** bell icon.  
The **Create Alert** dialog appears.
  3. Enter the details for your alert: 
     * **Name:** In the **Name** field, enter a name for your alert.
     * **Description:** (Optional) In the **Description** field, add a description about the alert.
     * **Access:** In the **Access** field, select whether the alert rules are to all viewers of the report or to the alert owner only.
     * **Recipients:** (Optional) In the **Recipients** field, enter a list of email addresses. 
       * Recipients must be members of your organization. Because external email aliases aren't allowed, you can't send alerts directly to email addresses that are outside your organization, such as those provided by services like Slack for channel integrations. See the Limitations of alerts section for more details and workarounds.
       * As the alert's creator, you're always included in the recipient list.
     * **Alert rules:** In the **Alert rules** field, select a field that you want to alert on, and then select the condition that the field should meet. The condition options differ based on the data type of the field. 
       * To add another condition with AND logic, add a new field and conditions to the **Alert rules** field.
       * Alert conditions don't support OR logic. If you want to create another condition with OR logic, consider creating a separate alert with a different condition.
     * **Start time:** In the **Start time** field, set the date and time that you want Data Studio Pro to begin checking the alert conditions.
     * **Repeat:** In the **Repeat** field, select the frequency with which Data Studio Pro will check that the alert conditions have been met. When the alert conditions are met, Data Studio Pro will send the alert notification email.  
To create personalized alert frequencies, such as every Tuesday and Thursday or every two weeks on Friday, select **Custom** in the **Repeat** field.
  4. Select **Save**.



## Receive alert notifications

Data Studio Pro checks the alert condition at the specified frequency. If the alert condition is met, Data Studio Pro sends an email notification from [looker-studio-noreply@google.com](mailto:looker-studio-noreply@google.com) to all recipients. The notification includes the following information:

  * The condition that was met.
  * The time that the condition was met.
  * The value of the field that triggered the condition.
  * A link to the Data Studio report.
  * A link to unsubscribe from the alert. Clicking this link and providing confirmation removes the recipient from the **Recipients** list of the alert. 
    * This link isn't included in the notification that is sent to the alert creator.



Alerts run only against the default filter values. If you edit filter values, those edits won't be applied to the alert condition.

If the report changes such that the alert condition would no longer have the same meaning, Data Studio Pro deactivates the alert the next time the alert runs and sends a notification email to the alert owner with the reason for the deactivation. The following changes can trigger alert deactivation:

  * The alert condition query failed to run.
  * A chart with an alert was deleted.
  * A report with an alert was deleted.
  * The underlying data source of an alert condition was deleted.
  * The alert owner no longer had the **Viewer** role on the report.
  * The alert owner no longer had the **Viewer** role on the data source.
  * A report editor disabled all alerts on the report.
  * A field in the alert condition was deleted from the underlying data source.
  * The definition of a field that was used in an alert condition was edited.
  * A dimension was added to or removed from a chart with an alert.
  * The default filter values of a report were changed.



## Edit an existing alert

You can edit alerts that you have created. You can't edit alerts that other users have created. To edit one of your alerts, follow these steps:

  1. View the report that has the alert that you want to edit. (Make sure that you're in **View** mode. You can't edit alerts while you're in **Edit mode**.)
  2. Hover over the chart with the alert, and select the **Create & view alerts** bell icon.  
The **Create & view alerts** dialog appears.
  3. To the right of the alert that you want to edit, click the three-dot **More Options** button more_vert.
  4. Select **Edit**. The **Edit Alert** dialog appears.
  5. Update the alert details.
  6. Click **Save**.



## Pause or delete alerts

Alerts are active by default. You can pause or delete a single alert that you own, or you can pause all alerts on a report. You can't delete alerts that other users have created.

### Pause or delete an alert

To stop an individual alert that you own, you can either pause or delete it by following these steps:

  1. View the report that you want to edit an alert on. (Make sure that you're in **View** mode. You can't edit alerts while you're in **Edit mode**.)
  2. Hover over the chart that you want to create an alert on, and select the **Create & view alerts** bell icon.  
The **Create & view alerts** dialog appears.
  3. To the right of the alert that you want to edit, select **More** more_vert. 
     * If the **Active** toggle is enabled, the alert is active, which means that Data Studio Pro is checking the alert condition on the specified frequency.
     * To pause the alert, select the **Active** toggle. The toggle changes to **Inactive**.
     * To unpause the alert, select the **Inactive** toggle. The toggle changes to **Active**.
     * To delete the alert, select delete **Delete**.

**Important:** You can't restore a deleted alert.

### Pause all alerts on a report

To stop all alerts on a report, you can disable the creation and viewing of alerts on a report by following these steps:

  1. View the report that you want to disable alerts on.
  2. Click person_add **Share**.
  3. In the **Share with people and groups** dialog, click the **Open settings** gear button.
  4. In the **Report access settings** dialog, select **Disable alerts creation & viewing for viewers**.
  5. Click the **Return to sharing list** back arrow button arrow_back.
  6. Click **Done.**



All alerts will be deactivated, and users won't be able to create new alerts or see existing alerts.

If you later enable alert creation and viewing for the report, Data Studio Pro doesn't automatically reactivate any alerts. If you want Data Studio Pro to check an alert condition on the report, activate the alert.

## Effects of canceling your Data Studio Pro subscription

If you cancel your Data Studio Pro subscription, all alerts will be deactivated and can't be reactivated without a Data Studio Pro subscription. You won't be able to create new alerts or view existing alerts.

If you renew your Data Studio Pro subscription, you'll be able to view and reactivate any alerts that were previously created.

## Limitations of alerts

  * [Blended data sources](https://docs.cloud.google.com/data-studio/how-blends-work) aren't supported.
  * [Running totals](https://docs.cloud.google.com/data-studio/add-comparison-metrics-and-running-totals) aren't supported.
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields) aren't supported.
  * Alert conditions don't support OR logic. Consider creating multiple alerts instead.
  * You can include up to 50 email addresses on an alert.
  * The person who created the alert is always included in the recipient list. Additional recipients are optional.
  * Alert recipients must be members of your organization. External email aliases and trusted domains aren't allowed as direct recipients.

You can't send alerts directly to external services like Slack channels by using their provided email addresses. Attempting to add such an email may result in an error message such as `The highlighted email address is blocked by the administrator.` This error indicates that the email domain is outside of your organization, not that your Google Workspace administrator has blocked the domain.

**Workaround for Slack or other external systems** : To send alert notifications to a Slack channel or other external system that accepts emails, follow these steps:

    1. Set up the Data Studio alert to send to an email address within your organization (for example, your own email or a group).
    2. In that internal email account (for example, Gmail), create an auto-forwarding rule or filter to automatically forward these specific alert emails to the external email address that's provided by Slack or the other system.
**Note:** This limitation is specific to the alerts feature. The [Schedule automatic report delivery](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery) feature does support sending reports to email addresses that are outside your organization, if your Workspace administrator permits it.
  * The alert schedule is based on your operating system's time zone. You can't change this setting inside Data Studio.

  * Alert conditions run only against default filter values.

  * You can't test alerts.

  * You can't restore a deleted alert.

  * By default, alerts don't work with data that is protected by using IP-based access levels with VPC Service Controls. This is because the automated offline process that checks alerts doesn't originate from a specific user IP address. For workarounds, see [Limits of VPC Service Controls](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery#limitations-of-vpc-sc).




## Related resources

[Schedule automatic report delivery](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
