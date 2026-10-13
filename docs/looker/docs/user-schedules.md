---
url: https://docs.cloud.google.com/looker/docs/user-schedules/
title: Viewing your scheduled data deliveries \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:16.039406+00:00
---

# Viewing your scheduled data deliveries  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/user-schedules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Viewing your scheduled data deliveries Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page describes schedule options for Looker. For information about Looker Studio schedules, see [Schedule automatic report delivery](https://docs.cloud.google.com/looker/docs/studio/schedule-automatic-report-delivery).

Once you have set up a recurring [delivery](https://docs.cloud.google.com/looker/docs/scheduling) of a [dashboard](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards) or [Look](https://docs.cloud.google.com/looker/docs/delivering-looks-explores), Looker displays that schedule on the **Schedules** page. This option is only visible if your Looker admin has given you permission to schedule dashboards and Looks.

To reach the **Schedules** page, select the user profile picture and choose **Schedules**.

![](https://docs.cloud.google.com/static/looker/docs/images/user-account-schedules-2214.png)

The **Schedules** page provides information about all the schedules that you have created and that have not been deleted.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-personal-schedule-manager-page-510-v2.png)

The columns in the **Schedules You've Created** table show these settings:

  * **ID** : A unique ID number associated with each of your scheduled data deliveries.

  * **Updated** : The time and date at which your schedule was created or most recently modified.

  * **Name** : The name of the schedule, which you can set when creating or editing the schedule.

  * **Scheduled Times** : The time and frequency of each of your schedules. For schedules based on a time, the column will show the time of delivery. If delivery is triggered by a [datagroup](https://docs.cloud.google.com/looker/docs/admin-panel-database-datagroups), it will show the name of that datagroup.

  * **Last Time Ran** : The most recent time that the data delivery occurred.

  * **Recipients** : The recipients' email addresses or the destination address of the data delivery.

  * **Type** : Whether the schedule is for the delivery of a Look or a dashboard.




### Filtering

You can limit the schedules Looker displays, based on criteria that you specify.

For example, to view only schedules whose titles contain the word _customer_ , enter the word `customer` in the Search bar. Or, if you want to view data deliveries that are scheduled only for weekdays, search on the term _weekdays_.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-user-menu-schedules-filtering-510-v2.png)

### Sorting

You can sort your schedules based on the **ID** , **Updated** , **Name** , **Last Time Ran** , or **Type** column in either ascending or descending order by clicking on the column heading.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-user-menu-schedules-sorting-510-v2.png)

### Deleting

> If all recipients unsubscribe from a scheduled email delivery, that schedule is deleted from Looker and from this page.

To delete a schedule, click the **Delete** button for that schedule's listing. Looker will display a window asking you to confirm the deletion.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-23 UTC."],[],[]] 
