---
url: https://docs.cloud.google.com/chronicle/docs/reports/schedule-reports/
title: Schedule dashboard reports \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:35:57.983481+00:00
---

# Schedule dashboard reports  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/schedule-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Schedule dashboard reports

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This page explains how you can schedule the delivery of Google SecOps dashboard reports over email.

You can schedule the delivery of Google SecOps reports for both the default dashboards and custom dashboards. When you schedule delivery of a Google SecOps dashboard report, you perform the following tasks:

  * Schedule the delivery of the dashboard report immediately or on a recurring schedule.
  * Specify the email addresses to deliver the report.
  * Specify the format of the report such as CSV, PDF, or PNG file.
  * Filter the report based on a specified time period.
  * Set the pagination details and test the delivery of the scheduled report.



## Control access to scheduling dashboard reports

You must have the Administrator role or Editor role to schedule dashboard reports. For more information about managing Users and Groups, or assigning roles, see [Role-based Access Control](https://docs.cloud.google.com/chronicle/docs/administration/rbac).

![Roles-based access to schedule reports](https://docs.cloud.google.com/chronicle/images/schedule_roles.png)

**Figure: Administrator role and Editor role provide access to schedule reports**

## Create a new schedule for report delivery

If you do not have any pre-existing schedules for the dashboard report, create a schedule for dashboard reports and customize the recurrence, destination email, format, filters, and pagination.

**Note:** This feature is built on Looker. For detailed information on the features and capabilities of Looker dashboards, see the [Looker documentation](https://docs.looker.com/).

  1. Select the default or custom dashboard for which you want to schedule the report delivery. 
     1. In the navigation bar, click **Dashboards & Reports > SIEM Dashboards**. For Google Security Operations SIEM customers, just click **Dashboards**.
     2. From the list of default and personal dashboards, select the dashboard for which you want to schedule the report delivery.
  2. To schedule the delivery of a dashboard report, on the dashboard page, click the _more_vert_ **More** icon and select **Schedule delivery**. If report schedules exist for the dashboard, the **Schedules** dialog appears with options to edit or create new schedules. If report schedules don't exist for the dashboard, the **Schedule** dialog appears with the dashboard name appended in the following format: Schedule <Dashboard Name>.
  3. In the **Schedule** dialog, specify the following details on the **Settings** tab:

     1. Select the interval of delivery from the **Recurrence** list and select the time of delivery. You can also specify the delivery timezone on the **Advanced options** tab.
     2. In the **Email addresses** field, enter a comma-separated list of email addresses to which you want to deliver the report. The email domain must be the same as the user domain that you use to login to Google SecOps. For example, if you login to Google SecOps using `sara@altostrat.com`, you can specify only emails that uses the `altostrat.com` domain, such as `alex@altostrat.com`. By default, you cannot send emails to other external email domains.

To send emails to an additional domain or to allow emails to be sent to any domain by disabling email domain validation, contact Google SecOps Support.

     3. In the **Format** list, select the CSV, PDF, or PNG file format for the report.

  4. On the **Filters** tab, specify the time period based on which you want to filter the report. If the dashboard does not contain filters, a message that the dashboard has no filters appears.

     1. To specify a filter, click the **Time** field and specify the filter condition, month, and year.
     2. To add more time filters, click _add_ **Add** icon.
  5. On the **Advanced options** tab, specify the pagination options for the email.

     1. To include a custom message in the email, in the **Custom Message** field, add a custom message.
     2. If necessary, select the following options: 
        * **Include links** : includes links in emails to the dashboards for which you have scheduled report delivery.
        * **Expand tables to show all rows**.
        * **Arrange dashboard tiles in a single column**.
     3. In the **Paper size** list, select the paper size.
     4. In the **Delivery time zone** list, select the timezone to deliver the message.
  6. To test the delivery of the report over email, click **Test now**.

  7. Click **Save**. The **Schedules** dialog appears.

  8. To edit, duplicate, or delete the scheduled delivery, in the **Schedules** dialog, click the _more_vert_ **More** icon.

  9. To send the report immediately, click **Send now**.

  10. To create another new schedule, click **New**.

  11. To close the dialog, click **Done**.




## Use an existing schedule for report delivery

If a schedule for the dashboard report delivery exists, you can immediately send the report or modify the report delivery options.

  1. Select the default or custom dashboard for which you want to update the report schedule. 
     1. In the navigation bar, click **Dashboards & Reports > SIEM Dashboards**.
     2. From the list of default and personal dashboards, select the dashboard for which you want to schedule the report delivery.
  2. On the dashboard page, click the _more_vert_ **More** icon and select **Schedule delivery**. If report schedules exist for the dashboard, the **Schedules** dialog appears with options to edit or create new schedules.
  3. To edit, duplicate, or delete the scheduled delivery, in the **Schedules** dialog, click the _more_vert_ **More** icon.
  4. To send the report immediately, click **Send now**.
  5. To create another new schedule, click **New**.
  6. To close the dialog, click **Done**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
