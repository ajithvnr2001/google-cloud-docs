---
url: https://docs.cloud.google.com/monitoring/charts/share-dashboards/
title: Share a custom dashboard \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:42.772884+00:00
---

# Share a custom dashboard  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/share-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Share a custom dashboard Stay organized with collections  Save and categorize content based on your preferences. 

Sharing a custom dashboard in Cloud Monitoring lets you collaborate with teammates or groups in your organization when investigating a system issue or reviewing service performance. When you share a dashboard from the Google Cloud console, Monitoring emails the dashboard URL to your recipients, checks whether they have viewing access, and—if your role permits—prompts you to grant the required Identity and Access Management role.

To share a dashboard's JSON configuration across projects instead of sharing a link to the live dashboard, see [Copy a dashboard definition to another project](https://docs.cloud.google.com/monitoring/charts/dashboards#copy-dashboard).

## Best practice

To eliminate permission barriers when sharing dashboards, we recommend that a principal with an IAM role of [Owner (`roles/owner`)](https://docs.cloud.google.com/monitoring/access-control#gcp_roles_desc) for a Google Cloud project grant the role of [Monitoring Viewer (`roles/monitoring.viewer`)](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) to all people, groups, or domains who might need to view a dashboard stored in that Google Cloud project. For more information, see [Grant access to Cloud Monitoring](https://docs.cloud.google.com/monitoring/access-control#grant-monitoring-access).

## Before you begin

Complete the following in the Google Cloud project that stores the dashboards that you want to share:

  1. In the Google Cloud console, go to the **IAM** page: 

[Go to **IAM**](https://console.cloud.google.com/iam-admin/iam)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. Select the Google Cloud project.

If you receive a permission-denied error, then you might not have an IAM role on the project, or your role isn't project-scoped. To view the **IAM** page, you must have a project-scoped IAM role. Project-scoped roles are the roles of Owner (`roles/owner`), Editor (`roles/editor`), and Viewer (`roles/viewer`).




## Share a dashboard

When you are investigating a data anomaly, you might want another person or a group of people to view a custom dashboard. For example, you might see an unexpected drop or spike in a performance metric and want to consult with a teammate. In this scenario, you want to share a dashboard with your teammate.

To share a dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard.
  4. Click share **Share** and then use the following table to complete the dialog.

###  Owner 

Use these instructions when your IAM role is Owner (`roles/owner`).

     1. Click **Add people and groups** and enter the names of the people or groups.
     2. Click **Message** and enter the information that you want included in the email. You don't need to include the URL of the dashboard.
     3. Optional: To have the dashboard display data for a specific time range, select **Open dashboard at custom time range** and then enter the start and end times.

By default, the dashboard displays the most recent hour of data.

     4. Click **Send**.

Monitoring evaluates whether the email recipients have permission to view the dashboard. Because Monitoring doesn't have access to the members of a group, those members might be identified as requiring permissions to view a dashboard.

When all recipients have permission to view the dashboard, the recipients are sent an email that invites them to view your dashboard. The email includes your message and the URL of the dashboard.

     5. If a dialog opens that prompts you to grant access to a recipient, then Monitoring determined that a recipient might not have permission to view the dashboard.

To grant the minimal permissions to view the dashboard, select the role of **Monitoring viewer** , and then click **Send**.

**Note:** The role of Monitoring viewer (`roles/monitoring.viewer`) grants permission to all Monitoring pages.

Each recipient is sent an email that invites them to view your dashboard. The email includes your message and the URL of the dashboard.

###  Editor or Viewer 

Use these instructions when your IAM role is Editor (`roles/editor`) or Viewer (`roles/viewer`).

     1. Click **Add people and groups** and enter the names of the people or groups.
     2. Click **Message** and enter the information that you want included in the email. You don't need to include the URL of the dashboard.
     3. Optional: To have the dashboard display data for a specific time range, select **Open dashboard at custom time range** and then enter the start and end times.

By default, the dashboard displays the most recent hour of data.

     4. Click **Send**.

Monitoring evaluates whether the email recipients have permission to view the dashboard. Because Monitoring doesn't have access to the members of a group, those members might be identified as requiring permissions to view a dashboard.

When all recipients have permission to view the dashboard, the recipients are sent an email that invites them to view your dashboard. The email includes your message and the URL of the dashboard.

     5. If a dialog with the title "Someone might not have access" is shown, then Monitoring determined that a recipient might not have permission to view the dashboard. To continue with the share command, click **Send** , and then click **OK**.

Each recipient is sent an email that invites them to view your dashboard. The email includes your message and the URL of the dashboard.

### All other roles

     1. Click **Add people and groups** and enter the names of the people or groups.
     2. Click **Message** and enter the information that you want included in the email. You don't need to include the URL of the dashboard.
     3. Optional: To have the dashboard display data for a specific time range, select **Open dashboard at custom time range** and then enter the start and end times.

By default, the dashboard displays the most recent hour of data.

     4. Click **Send**.

Monitoring sends an email that invites the recipients to view your dashboard. The email includes your message and the URL of the dashboard.

**Note:** To view the dashboard, the recipients of your email must have an IAM role that includes the permissions in the [Monitoring Viewer (`roles/monitoring.viewer`)][mon-role] role.




## Troubleshoot

This section describes how to resolve errors that might occur when sharing a dashboard.

### Error message occurs when sharing a dashboard

Two different errors can occur when sharing a dashboard:

  * You have the Owner (`roles/owner`) role, but the share dialog displays the following error message:

`Unable to grant access to the following account due to organization configurations`

The policies of your organization prevent you from granting a principal a role. To resolve this error, contact your organization administrator.

  * You selected one or more recipients without an email address, and the share dialog displays the following error message:

`Error: Email addresses and domains must be associated with an active Google Account, Google Workspace account, or Cloud Identity account.`

However, an email notification has been sent to all recipients with valid email addresses.




### Shared dashboard can't be viewed

You are emailed a URL of the dashboard; however, when you access the URL, you can't view the dashboard. Instead, you see the following message:

`You do not have sufficient permissions to view this page`

To resolve this situation, contact a project owner and ask them to grant you the Monitoring Viewer (`roles/monitoring.viewer`) role.

### Chart displays a warning about sensitive metadata

You open a custom dashboard and expect all widgets to display data. However, one or more widgets that contain SQL queries display messages similar to the following:
    
    
    This SQL query is configured to run on the BigQuery engine using [PROJECT_ID],
    and references resources from [RESOURCE, ...]. Sensitive metadata,
    including table contents, may be written to [PROJECT_ID].
    

The warning message indicates that the query crosses ownership boundaries and it provides you an opportunity to verify the query before it is executed. Ownership boundaries are determined by several factors, one of which is the hierarchy of the resources the query uses.

The system performs boundary checks each time a dashboard is opened. You can't prevent or dismiss these warnings.

**Note:** If you determine that a query isn't safe to execute, then close the dashboard. You should also consider deleting the dashboard. Don't run the query.

If a widget displays the warning message, then you can do any of the following:

  * If you know the query is safe to run and if you want to view the query results, then click **Confirm and Run**.

  * Ignore the error message. This widget won't show data for your current session.

  * Analyze the query and, if necessary, disable it. For example, you might do the following:

    1. Inspect the query and evaluate what data is queried.
    2. Review the history of the dashboard to determine who added the widget and when.
    3. If you were sent a dashboard link, then verify that the sender is a trusted source.
    4. For future reference, save your analysis to the dashboard by adding a **Text** widget.



Google Cloud provides some features that can help prevent data exfiltration through phishing, insider attacks, or external entities. To learn more, see [Data security with Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/data-security-with-analytics).

## What's next

  * [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts)
  * Add filters to dashboards:

    * [Add temporary filters](https://docs.cloud.google.com/monitoring/charts/filter-dashboard)
    * [Add permanent filters](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent)
  * [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
