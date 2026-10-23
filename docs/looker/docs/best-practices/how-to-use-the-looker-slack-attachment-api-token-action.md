---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-looker-slack-attachment-api-token-action/
title: Sending Looker content to Slack with the Slack Attachment (API Token) integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:31.182620+00:00
---

# Sending Looker content to Slack with the Slack Attachment (API Token) integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-looker-slack-attachment-api-token-action/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Sending Looker content to Slack with the Slack Attachment (API Token) integration Stay organized with collections  Save and categorize content based on your preferences. 

You can schedule recurring or one-off deliveries of Looker content to [third-party services that are integrated with Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions#list_of_integrated_services) through the Looker Action Hub, which implements Looker's Action API and exposes popular integrations — also known as _actions_ — for all Looker users. The Slack Attachment (API Token) integration posts an attachment with your Looker data to a Slack channel or direct message (DM). Unlike the [Slack](https://docs.cloud.google.com/looker/docs/scheduling-slack) action that is offered in the Looker Action Hub, the Slack Attachment (API Token) integration is available for customer-hosted Looker deployments. 

You can also send Looker content to Slack when [specified thresholds in your data have been met or exceeded](https://docs.cloud.google.com/looker/docs/alerts-overview#sending_alerts_to_the_slack_attachment_\(api_token\)_integration). 

The integration uses a Slack app with specific permissions called _bot token scopes_ , which govern what parts of your Slack workspace your app can access. Before you can use the Slack Attachment (API Token) integration in Looker, you must follow the setup instructions for configuring the integration on the Slack side, provided in the [Slack Attachment (API Token) GitHub repo README file](https://github.com/looker-open-source/actions/blob/master/src/actions/slack/legacy_slack/README.md). 

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Enabling the Slack Attachment (API Token) integration in Looker

After the integration is set up on the Slack side, a Looker admin must must enable the Slack Attachment (API Token) action in the list of actions on the [**Actions**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions) page in the **Admin** menu: 

  1. Scroll down the list of integrations and click the **Enable** button next to the Slack Attachment (API Token) listing.
  2. Enable the **Enabled** toggle.
  3. Enter the **Bot User OAuth Access Token** [from the Slack side setup](https://github.com/looker-open-source/actions/blob/master/src/actions/slack/legacy_slack/README.md) in the **Slack API Token** field.
  4. Click **Save**.



The integration is now configured. The Slack Attachment (API Token) option will now appear as a destination option in the Looker Scheduler and when you create [alerts](https://docs.cloud.google.com/looker/docs/creating-alerts#sending_alerts_to_the_slack_attachment_api_token_integration). 

## Delivering Looker content to Slack using the Looker Scheduler

To deliver your file attachment to Slack using the Slack Attachment (API Token) integration: 

  1. Navigate to your Looker content, and then [schedule a content delivery](https://docs.cloud.google.com/looker/docs/scheduling). 
  2. When configuring the Scheduler, choose the **Slack Attachment (API Token)** option in the **Destination** field. Looker will display delivery options that are specific to Slack, including channel type, a list of channels, and options to add a comment that will be included with your delivery and to name the file attachment. 
     * In the **Channel Type** field, select **Channels** to send the attachment to a Slack channel or **Users** to send the attachment to a Slack user. 
     * In the **Share In** field, select the Slack channel or user where you want to post your attachment. This channel or user list is based on the [bot credentials that you provided when you set up the Slack Attachment (API Token) app](https://github.com/looker-open-source/actions/blob/master/src/actions/slack/legacy_slack/README.md) on the Slack side, and it may include public and private channels and DMs to which the bot has been invited. If you do not see a channel listed, verify that the bot has been invited to that Slack channel. 
     * In the **Comment** field, enter any text you want to include with the attachment delivery. 
     * In the **Filename** field, enter a filename for the attachment file. You do not need to include the file extension. 

> For Slack attachments, the advanced delivery options available depend on whether you are delivering a [dashboard](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#advanced_options) or a [Look](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#applying_advanced_delivery_options). 

  3. Click **Save** to save your schedule's settings, or click **Send now** to immediately send your attachment to Slack. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
