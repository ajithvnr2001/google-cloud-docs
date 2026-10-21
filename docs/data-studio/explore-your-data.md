---
url: https://docs.cloud.google.com/data-studio/explore-your-data/
title: Explore your data in Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:25:32.616689+00:00
---

# Explore your data in Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/explore-your-data/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Explore your data in Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

Once you've connected to your underlying dataset, created a report, and added some visualizations, you can search for insights by exploring the data in the following ways:

## Filters

Filters limit the data in a report to a specified value or set of values. You can apply the following types of filters in a Data Studio report:

### Filter properties

Filter properties are static and persistent filters that only report editors can create or modify. You can apply filter properties to a single component, a group of components, a page, or the entire report. Using filter properties lets you focus on the data that best communicates the story you want to tell, making your reports more relevant to your audience. You can also use filter properties to remove irrelevant data, such as null values.  
  
Learn how to [create persistent filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties).

### Controls

Controls provide a dynamic and flexible way for both viewers and editors to filter the data. Filters you apply using controls while editing a report persist when you switch to view mode, but refreshing the report resets controls to their default values. Controls affect only the data that you see; applying a filter control has no effect on other users' views of that data. You can, however, use controls to customize the data in a report and preserve those filters when you share the report with a link or scheduled delivery.  
  
Learn more [about controls](https://docs.cloud.google.com/data-studio/about-controls).

### Quick filters

Quick filters let editors filter a report without actually changing the report configuration for other users. Quick filters exist only in edit mode and don't persist in view mode. Quick filters that you add are visible only to you. They don't appear to other viewers or editors of the report.

> **Note:** Quick filters are a Data Studio Pro feature.

Learn how to [add a quick filter](https://docs.cloud.google.com/data-studio/add-a-quick-filter).

## Chart interactions

You can interact directly with charts in both view and edit modes to refine the data that you see in the chart.

### Cross filter

Cross-filtering turns your charts into interactive filters. When cross-filtering is enabled for a chart, interacting with that chart acts as a filter on other charts in the report.

Learn more about [chart cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

### Zoom and pan

Zoom and pan lets viewers magnify a portion of a chart. After you zoom into a chart, you can also pan on that chart to view all the data that is present. Zooming and panning can help you focus on specific areas of a data-dense visualization, such as when you want to highlight a portion of your data or review more granular details.

Learn more about [zoom and pan](https://docs.cloud.google.com/data-studio/zoom-and-pan-on-charts).

### Sort

Sorting lets both viewers and editors change the order of the data in a chart without editing the chart configuration.

As an editor, you have two ways to sort the data in the charts in your reports:

  * Sort the chart interactively by right-clicking the chart in view or edit mode and then selecting the desired sort option.
  * Specify the default sort order in the chart **SETUP** properties.



### Freeze columns in table charts

Freezing columns lets viewers and editors pin one or more columns to the left side of [table charts](https://docs.cloud.google.com/data-studio/table-reference). This ability is useful when you're scrolling horizontally through table charts with many columns.

To freeze columns, hover your cursor over a table chart and click the three-dot **More** menu. Then, select the **Freeze column** option.

## More ways to explore your data

These features add interactive data exploration capabilities to your reports.

### Optional metrics

Optional metrics let viewers and editors choose the metrics to display in charts and tables without editing the chart configuration.

Learn more about [optional metrics](https://docs.cloud.google.com/data-studio/optional-metrics).

### Drill down

Drilling down lets viewers and editors explore data hierarchies by revealing additional levels of detail within a chart.

Learn more about [chart drill down](https://docs.cloud.google.com/data-studio/add-drill-actions-to-charts).

## Share your insights

Data Studio offers a variety of ways to share the insights that you find from your data. Learn more about [ways to share your reports](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports).

## Related resources

  * [Types of charts in Data Studio](https://docs.cloud.google.com/data-studio/types-of-charts)
  * [Connect to your data](https://docs.cloud.google.com/data-studio/about-connectors-data-sources-and-credentials)
  * [Preview your data](https://docs.cloud.google.com/data-studio/preview-your-data)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
