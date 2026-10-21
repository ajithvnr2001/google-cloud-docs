---
url: https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page/
title: View IoCs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:09:07.475217+00:00
---

# View IoCs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View IoCs 

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

When Applied Threat Intelligence is enabled, the **IOC Matches** tab displays additional columns. The **IOC matches** tab displays all the indicators of compromise (IOC) that were matched in your Google Security Operations data. You can view and filter IOCs curated by Applied Threat Intelligence.

On the **IOC matches** page you can do the following.

  * [View the IOCs](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page#viewioc)

  * [View data](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page#viewingdata)

  * [Filter IOCs](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page#filter)

  * [View IOC details](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page#iocdetails)




## View IOCs

The **IOC matches** page displays all the IOCs and their details, such as type, priority, status, categories, assets, campaigns, sources, IOC ingest time, first seen, and last seen. The color-coded icons and symbols help you to quickly identify which IOCs need your attention.

## View data

Click the  calendar_month  to display the calendar. You can adjust the time range for the displayed data. Adjust the time range by choosing one of the pre-set time ranges on the left side (ranging from last five minutes to last month). You can also specify a custom time range by choosing a start and end date anywhere on the calendar.

## Filter IOCs

In the left column, select the category to filter by. You can use the following options to filter:

  * **Type**

  * **GCTI Priority**

  * **Status**

  * **Categories**

  * **Sources**

  * **Associations**

  * **Campaigns**




To select more advanced filters, click the _filter_alt_ icon and then select the elements to filter on. You also need to select a logical operator:

  * OR. Must match any of the combined conditions

  * AND. Must match all of the combined conditions




To add more filters, click _add_ Add filter.

When you add a filter, it appears as a chip above the table.

To use two filters from the same category, the filters appear in the same chip. To find IOCs labeled as Active IR or High (both under the **GCTI Priority** label), complete the following steps:

  1. Select a logical operator.

  2. Select the first filter.

  3. Select the second filter. When you click the second filter, there are two new options: **Show only** and **Filter out** instead. Click **Show only**.




### View applied intelligence IOCs

  1. In the left column, click **Sources**.

  2. Click **Mandiant** to filter the data and view applied intelligence IOCs.




### Clear filters

  * Click the _delete_ icon next to the filter you want to delete.

  * Click **Clear all** to clear all the existing filters from the page.




## View IOC details

You can click an IOC to view details such as priority, type, source, Google Threat Intelligence score, and category. If you're getting IOC mapping but there are no events, then there is either a mistake in the field mapping or there are no rules. For more information, contact Google SecOps [Support](https://docs.cloud.google.com/chronicle/docs/getting-support).

For a selected indicator, on the **IOC details** page, you can do the following:

  * [View event prioritization](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page#viewevent)

  * [View associations](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page#associations)




### Event viewer

On the **Events** tab, on a selected indicator, you can view how an event is prioritized and the details for an event. For each event, you can view priority and rationale, UDM fields, and event details. The priority and rationale displays how priority is determined for the event.

### Associations

On the **Associations** tab, on a selected indicator, you can investigate potential breaches. You can view associations for any actor or malware. This also helps to prioritize alerts.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
