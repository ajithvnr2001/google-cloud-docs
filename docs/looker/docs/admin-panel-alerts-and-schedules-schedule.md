---
url: https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule/
title: Admin settings - Schedules \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:11.729914+00:00
---

# Admin settings - Schedules  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Schedules Stay organized with collections  Save and categorize content based on your preferences. 

As users navigate through folders, the [listing for each Look and dashboard](https://docs.cloud.google.com/looker/docs/finding-content#navigating_to_dashboards_and_looks_from_folders) indicates whether they have scheduled that content.

Looker administrators and users who have either the `manage_schedules` or `see_schedules` permission can also see the **Scheduler Plans** page by selecting **Schedules** in the **Alerts & Schedules** section of the **Admin** menu, which lists information about any [scheduled content](https://docs.cloud.google.com/looker/docs/scheduling) that is upcoming or ongoing.

## Information included

The **Schedules** page displays the following information about scheduled content:

Column | Definition  
---|---  
Name | Name of the scheduled plan, with a hyperlink to the scheduled content. This column also includes the frequency with which Looker will send the scheduled content.   
Owner | User who owns the schedule. This is typically the user who created the schedule. However, an administrator can change the owner of a schedule. Also, an administrator can create a schedule for another user through the API.  
Content Type | Type of content that is scheduled, either a Look or a dashboard.   
Summary | Summary of a scheduled delivery's format and destination.  
Recipients | Address of recipients of the schedule — either an email address or a URI for webhooks.  
Options | Additional schedule options, including **History**, **Reassign**, and **Delete**.   
  
## Filter the list of schedules

Click the **Filter List** bar to filter the list of scheduled plans by one or more of the following criteria:

  * **Schedule Name**
  * **Recipient**
  * **First Name** (of the schedule owner)
  * **Last Name** (of the schedule owner)
  * **Destination Type**
  * **Delivery Format**



## Sort the list of schedules

Click the **Name** header to sort the list of scheduled plans by the schedule name. The schedule name is the only field on which you can sort the list.

## View schedule history

To view a schedule's history, click the schedule's three-dot **Options** icon more_vert and select **History** to visit the [**Schedule History** page](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule-history), which is filtered for this scheduled plan.

## Reassign a schedule

To reassign ownership of a schedule to another user, click a schedule's three-dot **Options** icon more_vert and select **Reassign**. You must be an administrator to reassign schedules.

**Warning:** Be sure to reassign ownership of a schedule before you delete or disable a user account. Make sure that the new owner has the necessary roles (permissions and model sets) plus any access filter settings needed to allow them to run the schedule successfully.

## Delete a schedule

To delete a schedule, click a schedule's three-dot **Options** icon more_vert and select **Delete**. A dialog asks you to confirm this action because it cannot be undone. You must be an administrator to delete schedules.

**Warning:** If all recipients unsubscribe from a scheduled email delivery, that schedule is automatically deleted from Looker and from this page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
