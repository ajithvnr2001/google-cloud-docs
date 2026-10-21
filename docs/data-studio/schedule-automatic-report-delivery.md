---
url: https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery/
title: Schedule automatic report delivery \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:52:03.789776+00:00
---

# Schedule automatic report delivery  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Schedule automatic report delivery Stay organized with collections  Save and categorize content based on your preferences. 

You can regularly send a PDF of your Data Studio report to yourself and your stakeholders by setting up a delivery schedule. The PDF can include a link back to your original report.

**Note:** To create, edit, or delete a delivery schedule on a report, you must have [scheduling permissions](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports) on the report, be an editor of the report, or be the owner of the report.

## Create a delivery schedule in Data Studio

To create a new email delivery schedule for Data Studio, follow these steps:

  1. View the report that you want to schedule.
  2. Click **Share** , and then select **Schedule delivery** ![Schedule report delivery icon](https://docs.cloud.google.com/static/data-studio/images/icschedulegrey6002xweb48dp-2019-02-25-.png). 

The **Create schedule** dialog appears.
  3. (Optional) Enter a list of recipients. You are always included in the recipient list.
  4. (Optional) Select the report pages that you want to include.
  5. Set the date and time that you want to begin sending the report.
  6. Use the **Repeat** options to set the delivery frequency.

To create a personalized schedule for sending a report — such as every Tuesday and Thursday, or every two weeks on Friday — select **Custom**.
  7. Click **Schedule**.



## Create a delivery schedule in Data Studio Pro

If you have [Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro), to create a new email delivery schedule follow these steps:

  1. View the report that you want to schedule.
  2. Click **Share** , and then select **Schedule delivery** ![Schedule report delivery icon](https://docs.cloud.google.com/static/data-studio/images/icschedulegrey6002xweb48dp-2019-02-25-.png). If you're creating a schedule for this report for the first time, click **Add schedule** in the dialog that appears. 

The **Create schedule** dialog appears.
  3. In the **Destination** field, select **Email**.
  4. (Optional) Enter a list of recipients. You are always included in the recipient list. 

**Note** : Your Data Studio Pro administrator can [restrict allowed recipients](https://support.google.com/a/answer/9699595). If you enter a restricted recipient, Data Studio displays an error message until you remove the recipient.
  5. (Optional) Enter a custom subject and message. 
     * You can't set a custom subject and message for any reports in the **Owned by me** folder. To remove this limitation, you can [upgrade a report to Data Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-content-pro).
  6. (Optional) Select the report pages that you want to include.
  7. Set the date and time that you want to begin sending the report.
  8. Use the **Repeat** options to set the delivery frequency.

To create a personalized schedule for sending a report — such as every Tuesday and Thursday, or every two weeks on Friday — select **Custom**.
  9. Click **Schedule**.



## How scheduled email delivery works

Scheduled email delivery lets you regularly send an email with the report attached as a PDF file. The email will also contain a preview of the report's first page, along with a link to view the complete report. You can include other recipients by entering individual addresses or group email aliases.

See the [PDF download options](https://docs.cloud.google.com/data-studio/download-a-report-as-pdf#download_options) for more information. The options for downloading a PDF are the same as the options for scheduling a PDF.

## Change filters for a schedule

By default, the PDF version of a report uses the report's default filter control settings and date range properties.

To change the filter control values for a schedule, edit the schedule and then select the **Filters** tab. This tab displays all the controls and date ranges on the report. You can change any of the control values, but you cannot add or delete controls.

If you modify a filter's default values on a report, it won't affect the filter values for the report's schedules. However, if you remove a filter from a report, the filter is removed from all schedules on the report.

**Note:** The **Filters** tab displays only filter controls and date range controls. Data controls and buttons are not displayed. Also, you can't change filter properties in the **Filters** tab. Learn more about [controls](https://docs.cloud.google.com/data-studio/about-controls) and [filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties).

## Edit a schedule

  1. View the report that you want to reschedule.
  2. In the upper right, select **Share** , and then select **Schedule delivery** ![Schedule report delivery icon](https://docs.cloud.google.com/static/data-studio/images/icschedulegrey6002xweb48dp-2019-02-25-.png).
  3. (Data Studio Pro users) Select an existing schedule.
  4. Click **More** ![More](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--more-vertical.png).
  5. Select **Edit**.
  6. Enter the new schedule details.
  7. Click **Save**.



## Stop or delete a schedule

Schedules are active by default. To stop automatic report delivery, you can either pause or delete the schedule by following these steps:

  1. View the report.
  2. In the upper right, click **Share** , and then select **Schedule delivery** ![Schedule report delivery icon](https://docs.cloud.google.com/static/data-studio/images/icschedulegrey6002xweb48dp-2019-02-25-.png).
  3. (Data Studio Pro users) Select an existing schedule.
  4. Click **More** ![More](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--more-vertical.png). 
     * If you have Data Studio Pro, you can pause the schedule by toggling the **Active** switch to **Inactive**.
     * To delete the schedule, click **Delete schedule** ![Remove](https://docs.cloud.google.com/static/data-studio/images/gmdeletegrey60048dp-2020-03-09.png).

**Important:** You can't restore a deleted schedule.

## Send a scheduled report immediately (Pro feature)

If you have [Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro), to send a scheduled report immediately follow these steps:

  1. View the report.
  2. In the upper right, click **Share** , and then select **Schedule delivery** ![Schedule report delivery icon](https://docs.cloud.google.com/static/data-studio/images/icschedulegrey6002xweb48dp-2019-02-25-.png).
  3. Select an existing schedule.
  4. Click **Send now**.

**Note:** You can't send a report immediately for any reports in the **Owned by me** folder. To remove this limitation, you can [upgrade a report to Data Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-content-pro).

## Create a Google Chat delivery schedule (Pro feature)

If you have [Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro), you can send reports to individual users and Chat spaces by following these steps:

  1. View the report that you want to schedule.
  2. In the upper right, select **Share** , and then select **Schedule delivery** ![Schedule report delivery icon](https://docs.cloud.google.com/static/data-studio/images/icschedulegrey6002xweb48dp-2019-02-25-.png).
  3. (Data Studio Pro users) In the **Destination** field, select **Google Chat**.
  4. (Optional) Enter a list of recipients.

**Note:** If you have Data Studio Pro, your administrator can [restrict allowed recipients](https://knowledge.workspace.google.com/admin/data-studio/set-sharing-permissions). If you enter a restricted recipient, Data Studio displays an error message until you remove the recipient.
  5. Enter a custom subject and message.

     * You can't set a custom subject and message for any reports in the **Owned by me** folder. To remove this limitation, you can [upgrade a report to Data Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-content-pro).
  6. (Optional) Select the report pages that you want to include.

  7. Set the date and time that you want to begin sending the report.

  8. Set the delivery frequency.

  9. Click **Save**.




You can apply filters to a Chat schedule, just as you can for an email schedule.

### How scheduled Google Chat delivery works

Scheduled Google Chat delivery posts a message to the recipient users or spaces. The message is posted from the Google Chat account of the schedule's sender. The message includes the following elements:

  * A PDF attachment of the report
  * A **View in Data Studio** link
  * An **Unsubscribe** link that unsubscribes the user or space from the schedule



## Create a Slack delivery schedule (Pro feature)

If you have [Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro), you can send reports to Slack users and Slack channels by following these steps:

  1. View the report that you want to schedule.
  2. In the upper right, select **Share** , and then select ![Schedule report delivery icon](https://docs.cloud.google.com/static/data-studio/images/icschedulegrey6002xweb48dp-2019-02-25-.png)**Schedule delivery**.
  3. In the **Destination** field, select **Slack**.
  4. If your admin has [connected multiple Slack workspaces](https://docs.cloud.google.com/data-studio/slack#connect-slack) to Data Studio, select a workspace.
  5. If prompted, click **Sign in with Slack**.
  6. In the **Send to** field, select either **Channels** , **Users** , or **Manual ID**.

To find the **Manual ID** , follow these steps:

     1. Open Slack in your web browser and go to the selected channel.
     2. Look at the URL in your browser's address bar.
     3. The channel ID or user ID is the long string of letters and numbers that appears in the URL, typically following `/client/{workspace-id}/` and starting with a "C" for public channels, "G" for private channels, or "D" for users. For example, the URL might look like the following: `https://your-workspace.slack.com/client/T0123456789/C01ABCD1234`, where `C01ABCD1234` is the channel ID.
     4. If you are using the Slack mobile app, long-press the channel or username to copy the link, and then extract the final segment of the link, which will resemble the ID format that was mentioned in the previous step.
     5. Enter the channel ID or user ID in the **Manual ID** field.
  7. If you selected **Channels** or **Users** in the **Send to** field, next enter the list of channels or users.

     * You can add multiple channels or multiple users to a single schedule, but not a mix of channels and users.
  8. (Optional) Enter a custom message to accompany the report.

     * You can't set a custom message for any reports in the **Owned by me** folder. To remove this limitation, you can [upgrade a report to Data Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-content-pro).
  9. (Optional) Select the report pages that you want to include.

  10. Set the date and time that you want to begin sending the report.

  11. Set the delivery frequency.

  12. (Optional) Click **Send now** to send the Slack delivery immediately.

  13. Click **Save** to save the schedule.




You can apply filters to a Slack schedule, just as you can for an email schedule.

### How scheduled Slack delivery works

Scheduled Slack delivery posts a message to the recipient users or channels. The message is posted from the Slack account of the schedule's sender. The message includes the following elements:

  * A PDF attachment of the report
  * A **View in Data Studio** link



## Add multiple schedules (Pro feature)

If you have [Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro), you can add multiple schedules to a report.

  1. In the upper right, select **Share** , and then select **Schedule delivery** ![Schedule report delivery icon](https://docs.cloud.google.com/static/data-studio/images/icschedulegrey6002xweb48dp-2019-02-25-.png). 
     * If your report doesn't have any schedules, you will be prompted to create a schedule.
     * If your report has at least one schedule, Data Studio displays a list of all schedules for this report.
  2. Click **Add Schedule.**



Each report can have up to 200 schedules. Any user who is an owner or editor on the report can add or edit schedules on the report. The user who most recently edited a schedule, including toggling the **Active** switch, is the sender of the schedule.

## Filter by recipient email address (Pro feature)

If you have [Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro), you can personalize the data in the scheduled reports that are delivered by email. To use this feature, you must first [specify an email address field](https://docs.cloud.google.com/data-studio/filter-by-email-address) for each data source in the report that you want to personalize. You'll then see the **Filter the delivered report data by recipient's email address** option when you create or edit your schedule.

**Note:** Filter by recipient email address isn't available for Chat schedules and Slack schedules.

## Limits and troubleshooting

The following sections cover the limits of scheduled delivery and some common troubleshooting steps.

### Quotas for scheduled email delivery

Data Studio limits the number of recipients that a user can send scheduled emails to per day and per month.

If you have Data Studio Pro, no such quotas apply. If your organization uses Google Workspace, the quotas are higher. Refer to the following table for details:

Account Type | Individual | Google Workspace | Data Studio Pro  
---|---|---|---  
Daily email limit | 200 | 500 | Unlimited  
Monthly email limit | 800 | 3000 | Unlimited  
  
Note the following limitations regarding quotas:

  * If you exceed one of the quotas, further emails from your account won't be sent.
  * It's not possible to check your progress against each quota.
  * Any reports in the **Owned by me** folder are considered to be personal reports and will be subject to quotas. To remove this limitation, you can [upgrade a report to Data Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-content-pro).



### Limits of scheduled email delivery

Scheduled email delivery has the following limits:

  * You can include no more than 50 recipient addresses.
  * The person who created the schedule must be included in the recipient list. Additional recipients are optional.
  * Scheduled emails can include no more than 5 pages as a preview of the report. The attached PDF includes all selected pages.
  * The delivery schedule is based on your operating system's timezone. You can't change this inside Data Studio.
  * When editing a schedule, you cannot add filters that are not already present in the report nor delete filters from the report.
  * You can't edit or send tests for inactive schedules.
  * By default, scheduled email delivery doesn't work with data that is protected by using IP-based access levels with VPC Service Controls. This is because the automated offline process that generates scheduled emails doesn't originate from a specific user IP address. For workarounds, see Limits of VPC Service Controls.
  * Data Studio checks for potentially inappropriate content in the subject and message fields and may prevent you from creating or updating a schedule if it detects inappropriate content.
  * If you don't have Data Studio Pro, each report can have no more than one schedule. If you have Data Studio Pro, each report can have up to 200 schedules.
  * If you don't have Data Studio Pro, the highest frequency you can set a schedule is once per day. If you have Data Studio Pro, you can send a schedule up to once per hour.
  * You can create multiple schedules on reports only where the report owner has Data Studio Pro.
  * You can select **Send now** only if you have Data Studio Pro. Also, you can't send a report immediately for any reports in the **Owned by me** folder. To remove this limitation, you can [upgrade a report to Data Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-content-pro).
  * You can set a custom subject and message only if you have Data Studio Pro. Also, you can't set a custom subject and message for any reports in the **Owned by me** folder. To remove this limitation, you can [upgrade a report to Data Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-content-pro).
  * Your reports will display an inline preview only if you have Data Studio Pro. Also, inline previews won't display for any reports in the **Owned by me** folder. To remove this limitation, you can [upgrade a report to Data Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-content-pro).
  * If you downgrade from Data Studio Pro to Data Studio, the oldest created email schedule remains active for each report. Additional schedules for that report become Inactive.



### Limits of scheduled Google Chat delivery

Scheduled Google Chat delivery has the following limits:

  * You must be a Data Studio Pro user to schedule delivery using Chat.
  * You must be an owner or editor of the report that you want to schedule.
  * You can schedule a report only to Google Chat spaces that you are a member of.
  * You can schedule a report only to Google Chat users who are in your organization.
  * You can schedule delivery using Google Chat to a maximum of 10 individual users and 10 Chat spaces. To send to more recipients, create additional schedules.
  * You can't filter by recipient email address when delivering a report with Google Chat.



### Limits of scheduled Slack delivery

Scheduled Slack delivery has the following limits:

  * You must be a Data Studio Pro user to schedule delivery using Slack.
  * You must be an owner or editor of the report that you want to schedule.
  * You can schedule a report only to Slack channels that you are a member of.
  * For a single report, you can schedule delivery using Slack to a maximum of 5 Slack channels or 10 Slack users. To send to more recipients, create additional schedules.
  * You can't filter by recipient email address when delivering a report with Slack. All recipients of the scheduled delivery will receive the same version of the report.
  * You can add multiple Slack channels or multiple Slack users to a single schedule, but not a mix of channels and users.



### Limits of VPC Service Controls

If a report connects to a BigQuery data source that is protected by a VPC Service Controls (VPC-SC) perimeter with IP-based access levels, scheduled email delivery might fail.

  * **Symptom** : Scheduled emails contain only a link to the report without inline images or PDF attachments. The email body or attachment might display this error: "Organization VPC Service Controls prohibit access to dataset used by this component."
  * **Cause** : The automated offline process that generates scheduled emails doesn't originate from a specific end-user IP address, so it can't satisfy IP-based access level restrictions.
  * **Workarounds** : To enable scheduled email delivery for data sources that are protected by VPC Service Controls, use either of the following workarounds: 
    * **Use service account credentials (recommended)** : Configure your BigQuery data source to use a [service account](https://docs.cloud.google.com/data-studio/set-up-a-google-cloud-service-account) instead of asset-level [data credentials](https://docs.cloud.google.com/data-studio/data-credentials) (either owner's credentials or viewer's credentials). Because service accounts authenticate by using identity rather than an end-user IP address, automated delivery functions reliably behind a VPC Service Controls perimeter.
    * **Configure an identity-based access level** : Create or modify an [access level](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) to include the Google Account (email address) of the user who schedules the report. When you add the scheduling user's identity to an exempt access level that bypasses perimeter checks for BigQuery, the offline rendering service can access the data.



### Troubleshoot scheduled delivery errors

The following sections describe common errors that you might encounter when you schedule a report delivery.

#### Creating schedules on the report is disabled as the report does not belong to a Data Studio Pro organization

This error indicates that the report is not located in a Data Studio Pro content management area. Data Studio Pro features like scheduling require assets to be within a Team Workspace or Sandbox.

To resolve this issue, move the report and its associated data sources into a Team Workspace or your personal Sandbox.

#### Scheduling functionalities are limited because the owner of this report doesn't have an active Data Studio Pro subscription

This error can occur for one of the following reasons:

  * **Report location** : The report might be in the **Owned by me** section. Data Studio Pro features require reports to be in a Team Workspace or Sandbox.

To resolve this issue, move the report and its data sources to a Team Workspace or your Sandbox.

  * **Subscription or license propagation delay** : If your organization recently upgraded to Data Studio Pro, or if user licenses were just assigned, these changes can take up to 24 hours to fully propagate.

To resolve this issue, ensure that the report is in a Pro workspace. If subscription or license changes were made recently, wait up to 24 hours. Confirm that the report owner has an active Data Studio Pro license assigned by your administrator.




#### Scheduled deliveries to Google Chat fail with "failed" or "not_member_of_space_error"

This error can occur for one of the following reasons:

  * **Schedule owner is inactive or has lost permissions** : Schedules run by using the credentials and permissions of the user who last saved the schedule. If that user's account becomes inactive (for example, if they leave the organization) or loses the necessary permissions on the report or data, the schedule will fail.

To resolve this issue, an active user with Edit access to the report must take over the schedule:

    1. Open the report in Data Studio.
    2. Click **Share** , and then select **Schedule delivery**.
    3. Find the failing schedule.
    4. Click **More** ![More](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--more-vertical.png), and then select **Edit**.
    5. Review the settings, and then click **Save**. This action updates the schedule to run as the current user.
    6. Alternatively, delete the old schedule and create a new one.
    7. Ensure that the user saving the schedule maintains the required access to the report and all underlying data sources.



### Why didn't my report get delivered?

If your reports aren't being delivered according to the schedule that you set up, one of the following issues might be occurring.

  * If the downloaded report contains an error, the report won't be sent. Make sure that the report can be [manually downloaded](https://docs.cloud.google.com/data-studio/download-a-report-as-pdf) successfully.
  * If you have Data Studio Pro, your administrator can [restrict the recipients](https://support.google.com/a/answer/9699595) to whom you can send content. If at least one recipient of a schedule is restricted, the schedule won't send. Data Studio will display an error in the **View Schedule** dialog and send a warning email to the last user that edited the schedule. Remove any restricted recipients to resume schedule delivery.



### Scheduled reports always use US English formats

When you schedule a report delivery, the content of the report, such as numbers, currency, and dates, appears using US English formatting, even if your Google Account is set to another language.

### Scheduled reports show system errors on individual charts

Large or complex reports might display a generic "System Error" on individual charts. This error occurs when the automatic export process times out. To ensure that your scheduled emails arrive with all charts rendered correctly, you can try the following:

  * Divide the report: Split the report into two or more smaller reports.
  * Stagger the schedule: Set the delivery times for the smaller reports at least 30 minutes apart. This provides a buffer for the scheduling system to refresh resources between jobs.



## Related resources

  * [Filter by email address](https://docs.cloud.google.com/data-studio/filter-by-email-address)
  * [Set scheduling permissions for Data Studio users](https://support.google.com/a/answer/13889857)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
