---
url: https://docs.cloud.google.com/data-studio/slack/
title: Share and schedule reports with Slack \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:52:46.125068+00:00
---

# Share and schedule reports with Slack  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/slack/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Share and schedule reports with Slack Stay organized with collections  Save and categorize content based on your preferences. 

You can send Data Studio reports to Slack channels and Slack users on your Slack workspaces.

## Prerequisites

  * You must be a user under a Data Studio Pro subscription.
  * Your Google Workspace admin must have enabled Slack delivery for your organization. The Slack delivery channel is allowed by default in Google Workspace. If you want to change this setting, a Google Workspace admin can change it for you by follow these steps in the Google Admin console: 
    1. In the Admin console, go to **Menu** > **Apps** > **Additional Google services** > **Data Studio**.
    2. Click **Content distribution settings**.
    3. In the **Pro Features** section, modify the **Allow Slack delivery** setting.



## Connect Slack to your Data Studio organization

Once Slack delivery has been enabled by your Google Workspace admin, a Data Studio Pro admin can connect one or more Slack workspaces to your Data Studio organization by following these steps:

  1. Click the **Settings** icon in Data Studio and select **Enterprise admin**.
  2. In the **Slack Integration** section, click **Add Slack Workspace**.
  3. Sign in to Slack as prompted.



### Remove connected Slack workspaces

An admin can remove Slack workspaces by following these steps:

  1. Click the **Settings** icon in Data Studio and select **Enterprise admin**.
  2. In the **Slack Integration** section, next to the Slack workspace that you want to remove, click **Delete**.



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



## Manage your Slack access

To re-authenticate or revoke your access to connected Slack workspaces, follow these steps:

  1. Click the **Settings** icon in Data Studio and select **Share settings**.
  2. The **Slack Integration** section displays a list of available Slack workspaces along with some options for each workspace: 
     * If you have never connected to a workspace, click the **Sign-in to Slack** next to the workspace name.
     * If you have lost access to a workspace, click **Reconnect** next to the workspace name.
     * If you want to remove access to a workspace, click **Revoke** next the workspace name.
     * If you want to remove access to a workspace, click **Revoke** next to the workspace name.



## Limits of scheduled Slack delivery

Scheduled Slack delivery has the following limits:

  * You must be a Data Studio Pro user to schedule delivery using Slack.
  * You must be an owner or editor of the report that you want to schedule.
  * You can schedule a report only to Slack channels that you are a member of.
  * For a single report, you can schedule delivery using Slack to a maximum of 5 Slack channels or 10 Slack users. To send to more recipients, create additional schedules.
  * You can't filter by recipient email address when delivering a report with Slack. All recipients of the scheduled delivery will receive the same version of the report.
  * You can add multiple Slack channels or multiple Slack users to a single schedule, but not a mix of channels and users.



## Troubleshoot a Slack delivery

If you are not receiving a Slack delivery, follow these troubleshooting steps:

  1. Check that the workspace is connected to Data Studio.
  2. Check that your Data Studio user has access to the Slack workspace.
  3. Check that your Slack user is a member of the Slack channel that you're trying to send to.



See the [Why didn't my report get delivered?](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery#why_didnt_my_report_get_delivered) section of the main scheduling page for more troubleshooting tips.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
