---
url: https://docs.cloud.google.com/data-studio/add-a-quick-filter/
title: Add a quick filter \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:52.440857+00:00
---

# Add a quick filter  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-a-quick-filter/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Add a quick filter Stay organized with collections  Save and categorize content based on your preferences. 

Quick filters provide a flexible, ad hoc way to explore your data. Report editors and viewers can use quick filters to quickly change how the data in the report is filtered. Changes made by viewers don't affect the original report configuration for other users.

## The filter bar

Add quick filters to your report by using the filter bar. The filter bar appears beneath the toolbar at the top of your screen. Report editors will always see the filter bar in edit mode. Report editors can also enable the filter bar for viewers. The filter bar shows all the quick filters, as well as any controls and chart cross-filters that you've applied.

![The Data Studio editor interface, with the Add quick filter and Filter bar buttons called out.](https://docs.cloud.google.com/static/data-studio/images/quick-filter-simplified-numbered.png)

To turn off the filter bar in edit mode, click ![](https://docs.cloud.google.com/static/data-studio/images/gmfilteraltgmgrey60024dp-2023-07-12.png)**Filter bar** in the panel.

**Tip:** If you don't see the panel manager, properties panel, or data panel, click ![](https://docs.cloud.google.com/static/data-studio/images/keyboardarrowleftgrey6002x24dp-2020-10-27.png)**Show panels**.

## Add a quick filter to your report

To add a quick filter to your report, whether as an editor or a viewer, click **Add filter** in the filter bar, and then select a dimension from the field list. If your report contains multiple data sources, you may need to expand the fields for that data source first.

Alternatively, editors can right-click a dimension in the data panel and select **Add to filter bar** from the context menu.

Quick filters appear as a chip in the filter bar, with a ![](https://docs.cloud.google.com/static/data-studio/images/filterlistgrey6002x48dp-2020-09-09.png) filter icon preceding the name of the field that you selected.

To configure the quick filter, click the chip, and then do the following:

  * For numeric dimensions, use the slider control to refine the range of values.
  * For date dimensions, select a date range using the date picker.
  * For text, geo, and other dimension types, select a value or values from the list.



## Edit a quick filter

To modify a quick filter, whether as an editor or a viewer, click its chip in the filter bar, and then select a new value to filter by.

**Note:** In addition to quick filters, the filter bar also shows all the filter controls and chart cross-filters that are affecting the data in the report. These controls and cross-filters appear with a ![](https://docs.cloud.google.com/static/data-studio/images/gmbarchartgmgrey60024dp-2023-07-12.png) bar chart icon.**Important:** You can't edit a filter control or change a chart cross-filter by using the filter bar.

## Remove a filter

Removing a filter control or chart cross-filter from the filter bar resets that individual control or cross-filter.

To remove an individual quick filter, whether as an editor or a viewer, click the **X** in the quick filter chip.

## Clear the filter bar

Clearing the filter bar removes filters from the filter bar. The result of clearing the filter bar depends on whether you are a report editor or viewer:

  * **Editors** : Clearing the filter bar deletes all quick filters and resets any filter controls or chart cross-filters.
  * **Viewers** : Clearing the filter bar deletes any quick filters that you have added. Filter controls and chart cross-filters will remain.



To clear the filter bar, click ![More options](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png), and then select **Clear filters** ![Remove.](https://docs.cloud.google.com/static/data-studio/images/deletegrey6002x48dp-2020-09-22.png).

## Reset the filter bar

Resetting the filter bar removes any values from existing quick filters, but leaves the filter chip in the filter bar. Resetting the filter bar also resets any filter controls or chart cross-filters on the report.

To reset the filter bar, whether as an editor or a viewer, click **Reset** in the filter bar.

> **Note:** The report-level **Reset** button will also reset the filter bar, filter controls, and chart cross-filters, but will also reset other report refinements, such as sorting, optional metrics, drill down, and so on.

![The Data Studio editor interface, with the report-level reset button and filter bar reset button called out.](https://docs.cloud.google.com/static/data-studio/images/reset-quick-filter-simplified-numbered.png)

Legend:

  1. Report-level reset button.
  2. Filter bar reset button.



## Share a filtered view

Viewers can share their current filter settings with others by generating a short link to the report.

  1. Apply the filters you want to the report.
  2. In the upper right, click the ![](https://docs.cloud.google.com/static/data-studio/images/gmarrowdropdowngmgrey60024dp-2023-06-21.png) down arrow next to **Share** and then select ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--link.png)**Get report link**.
  3. Ensure **Link to your current report view** is checked.
  4. Click **COPY LINK**.



When others open this link, they will see the report with the same filter configurations that you've applied.

[Learn more about report links](https://docs.cloud.google.com/data-studio/get-a-link-to-your-report).

## Enable and configure the filter bar for viewers

Report editors can enable and configure the filter bar for viewers by following these steps:

  1. If you aren't in edit mode, click **Edit** to [edit your report](https://docs.cloud.google.com/data-studio/edit-mode).
  2. In the toolbar, click **Add a control** , and then select **Viewer filter bar**.
  3. The **Viewer filter** pane opens.
  4. Toggle **Enable viewer filter bar** on.
  5. By default, viewers can use the filter bar to filter by any dimension from any data source in the report. To limit the dimensions that viewers can filter on, select **Choose data sources and fields** in the **Allowed viewer filter dimensions** section, and then select the data sources and dimensions that you want to be available to viewers.



## Limits of quick filters and the filter bar

  * You can only create quick filters on dimensions. Creating quick filters based on metrics is not supported.
  * Report editors can specify the dimensions that are available for viewers to use in ad hoc quick filters. By default, most dimensions are enabled.
  * With Looker connector data sources, viewers can add ad hoc filters using filter-only fields or parameters.
  * The filter bar doesn't show the effects of filter properties, date range controls, or data controls on the report.
  * Quick filters apply to the entire page. You can't apply a quick filter to a single component or group of components.
  * Viewers can reorder quick filter chips in the filter bar by right-clicking a filter chip and selecting **Shift left** or **Shift right**.



## Related resources

  * [About filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
