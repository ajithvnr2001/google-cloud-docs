---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-google-sheets-integration/
title: Looker actions: Google Sheets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:27.816913+00:00
---

# Looker actions: Google Sheets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-google-sheets-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Looker actions: Google Sheets Stay organized with collections  Save and categorize content based on your preferences. 

Integrate your Looker data directly into Google Sheets to streamline your operational workflows and ensure timely data access. The Looker Google Sheets action uses OAuth for authorization to send Looker content as CSV files. You can send this data once or on a recurring schedule.

Looker administrators can enable the Google Sheets action through the Looker Action Hub. Once enabled, users with appropriate permissions can select Google Sheets as a destination. This lets them send or schedule Looks and Explores, infusing data directly into their everyday business processes.

**Note:** You can also connect Google Sheets to Looker directly by using the **Connected Sheets for Looker** feature. This feature lets users interactively explore data from LookML models through the familiar Google Sheets spreadsheet interface. For more information, see the [Using Connected Sheets for Looker](https://docs.cloud.google.com/looker/docs/connected-sheets) documentation page. For an overview of all the ways that Looker integrates with Google Sheets, see the [How Looker integrates with Google](https://docs.cloud.google.com/looker/docs/looker-google-integrations#google_sheets) documentation page.

## Things to know

There are several things to know about the Google Sheets action:

  * **Customer-hosted instances may be unable to enable actions from the Looker Action Hub** , especially actions that [support streamed results](https://docs.cloud.google.com/looker/docs/action-hub#uses_streaming) or that use [OAuth](https://docs.cloud.google.com/looker/docs/action-hub#configuring_an_action_for_oauth), if the customer-hosted Looker instance does not fulfill the [Looker Action Hub requirements](https://docs.cloud.google.com/looker/docs/action-hub#looker_action_hub_requirements). See the [Sharing data through an action hub](https://docs.cloud.google.com/looker/docs/action-hub#considerations_for_customer-hosted_instances) documentation page for suggested solutions to this potential issue.
  * **You can't schedule or send dashboards to Google Sheets.** Dashboards require formats that support multiple tiles or archives (such as PDF, PNG, or ZIP), but the Google Sheets action only supports streaming a single query's results in plain CSV format. To deliver data to Google Sheets, schedule the delivery from the Look or Explore UI instead, and ensure that the output format is set to plain CSV.
  * **Google Sheets are[limited to 10 million cells](https://support.google.com/drive/answer/37603) for the entire Sheet.** If your data table has columns, rows, or tabs that exceed this limit, any deliveries to the Google Sheets integration will fail.



## Enabling the Google Sheets action in Looker

Looker admins can enable the Google Sheets action in Looker with the following steps:

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

  1. Go to the **Admin** panel and, under **Platform** , go to the **Actions** page.
  2. On the list of Action Hub actions, scroll to Google Sheets and click the **Enable** button.
  3. On the **Google Sheets** action page, click the **Enabled** toggle to the on position, and click **Save**.
  4. When you return to the list of Action Hub actions, your Google Sheets action should be enabled.



Any users with the `send_to_integration` permission can now send or schedule Looks or Explores in CSV format to a Google Sheet.

## Delivering data in CSV format to a Google Sheet

Any Looker user who has `send_to_integration` permissions can send or schedule Looks or Explores in CSV format to a Google Sheet.

To prepare your data before sending or scheduling it, follow these steps:

  * **Horizontal scaling:** If your data table contains more than 26 columns and you plan to import the data to an existing Google Sheet, you'll need to manually expand the Google Sheet before you can import your data into it.
  * **Vertical scaling:** If your data table contains more than 1,000 rows, Looker will add those rows to your Google Sheet by default.
  * **Overwriting:** If you're going to import your data into an existing Google Sheet, write any formulas on a separate tab of your Google Sheet to preserve the logic in your formulas. If you use the Google Sheets action's overwrite function, the action dynamically updates your Google Sheet, and your data will automatically be loaded into the first or leftmost tab of your Google Sheet. If you'd prefer to create a new spreadsheet with each data delivery so that you have a full history of your data and can track changes over time, don't use the Google Sheets action's overwrite function.



To send or schedule your content, follow these steps:

  1. From the [Scheduler](https://docs.cloud.google.com/looker/docs/delivering-looks-explores), next to **Where should this data go?** , select **Google Sheets** as your delivery destination.
  2. If you're delivering to Google Drive for the first time, you'll need to authenticate with your Google credentials. Click **Sign in with Google** , specify your Google Account, and then click **Allow** to connect your Looker account to your Google OAuth credentials. You can connect only one set of Google OAuth 2.0 credentials to this integration.
  3. In the Scheduler, click **Verify credentials** to load your Google Drive.
  4. From the **Select Drive to save file** drop-down, choose the Google Drive where your CSV file will be saved.

Next, you can either enter the URL for a folder in this Drive or fetch all folders in your Drive.

     * In the **Google Drive Destination URL** field, enter the full Google Drive URL of the folder where you want to save your data. For example: `https://drive.google.com/corp/drive/folders/abcxyz`. If this URL isn't accessible, your data will be saved to the root folder of your Google Drive.
     * From the **Select Fetch to fetch a list of folders in this drive** drop-down, select **Fetch**. After the Scheduler dialog refreshes, from the **Select folder to save file** drop-down, select the Google Drive folder where your CSV file will be saved.
  5. Specify the name of your Google Sheet file in the **Enter a filename** field. You don't need to include the file extension — the Google Sheets action will automatically append it during delivery.

  6. In the **Overwrite Existing Files** drop-down, select **Yes** or **No**. Selecting **No** will generate a new Google Sheet with a snapshot of your data with every data delivery. Selecting **Yes** will load your data in the first or leftmost tab of your existing Google Sheet.

**Important:** Because of [Google Sheets cell limits](https://support.google.com/drive/answer/37603), if you choose the overwrite option, keep in mind that the tabs that are added during each delivery cannot cause the Sheet to exceed the 10 million cell limit. Once the cell limit is exceeded, subsequent schedules will fail.
  7. Advanced options for CSVs include customizable [limit](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#limit) and [format](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#format_options). Click **Send** or **Schedule**.

  8. Refresh your Google Drive folder to see your file delivery.




## Switching Google Accounts

To associate a different Google Account with this action, you must delete the account's connection to the Looker instance. To learn more, see [Manage connections between your Google Account and third-parties](https://support.google.com/accounts/answer/13533235).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
