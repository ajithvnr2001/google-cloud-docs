---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-audit-log/
title: Audit log dashboard \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:30.523576+00:00
---

# Audit log dashboard  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-audit-log/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Audit log dashboard Stay organized with collections  Save and categorize content based on your preferences. 

The audit log dashboard helps you track changes to the configuration of your instance. The dashboard tracks changes to the settings on the **Settings > Developer Settings** page, and displays information such as the type of change, who made the change, and when. This information can help you identify updates to your instance that might affect operations, such as unexpected changes to business hours, queue settings, and user permissions.

## Permissions

To access this dashboard, you need a role with the **Dashboard > Audit Dashboard** permission. The administrator role has this permission by default. To create a custom role with this permission, see [Create a new custom role](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions#create-new-custom-role).

## Use the dashboard

To use the dashboard, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Audit Dashboard**. If you don't see the **Settings** menu, expand the window horizontally until the **Settings** menu appears. The **Audit Log** dashboard appears.

  2. Click the **Date** field to select a date range, and then do one of the following:

     * Select a preset date range. To do this, follow these steps:

       1. Click expand_more **More** to view all of the preset date ranges.

       2. Click the date range that you want.

     * Select a custom range. To do this, follow these steps:

       1. Click **Custom**.

       2. In the **Custom** field, enter a start and end date for your date range. You can type your date range or click ![Click the calendar icon to see the
calendar.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-calendar.png)**Open calendar** to select start and end dates.

**Note:** The maximum date range that you can specify is 45 days. If you specify a date range of more than 45 days, the dashboard returns an error. 
  3. Filter your results using the following fields:

     * **User**. Filter by the email address of a user. Displays changes to settings made by that user.

     * **Page**. Filter by a page in the CCAI Platform portal. Displays changes to settings made on that page.

     * **Setting**. Filter by the category of settings that were changed.

     * **Setting Name**. Filter by the setting that was changed.

  4. Click ![Click the update icon to update.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-update.png)**Update**.




## Tiles

This dashboard contains the following metric tiles:

  * **Total Changes Applied** : the number of settings added, changed, or deleted.

  * **Total Added** : the number of settings added

  * **Total Modified** : the number of settings changed

  * **Total Deleted** : the number of settings deleted

  * **Changes Applied** : a bar chart that displays settings changes by setting name. The bars are color coded by **Added** , **Deleted** , and **Modified**.




## Tables

This dashboard contain the following metrics table. Hold the pointer over a table heading to see its description.

  * **Change Details** : a list of settings changes that displays details for each change.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
