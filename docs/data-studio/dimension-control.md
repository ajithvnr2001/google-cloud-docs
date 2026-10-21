---
url: https://docs.cloud.google.com/data-studio/dimension-control/
title: Dimension control \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:07:21.751591+00:00
---

# Dimension control  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/dimension-control/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Dimension control Stay organized with collections  Save and categorize content based on your preferences. 

The dimension control lets report viewers change the dimension on one or more charts without needing to edit the report. Using a dimension control eliminates the need to create separate charts and reports to show related data and different levels of granularity.

## Add a dimension control to your report

To add a dimension control to a report, follow these steps:

  1. Edit your report.
  2. In the toolbar, select **Add a control** ![Control icon.](https://docs.cloud.google.com/static/data-studio/images/filterlistgrey6002x48dp-2020-09-09.png).
  3. Select **Dimension control** , and then place the control on your report.
  4. On the right, configure the chart using the [properties panel](https://docs.cloud.google.com/data-studio/properties-panel). 
     1. Select the data source that this dimension controller should use.
     2. Add one or more dimensions that viewers should be able to swap between.



## How the dimension control works

When a viewer selects a dimension in the dimension control, all charts in the dimension control's scope will use the selected dimension. Then, all affected charts will reload their data.

If a chart has no dimensions, then it won't be updated. If a chart has more than one dimension, the dimension control only affects the first dimension.

You can have multiple dimension controls in a single report. If a viewer selects a dimension in a dimension control, and that dimension has a different value in another dimension control in the same scope, then the value of the other dimension control will be cleared.

## Dimension control scope

By default, a dimension control affects all charts on the current page of the report that use the control's data source.

To limit the scope of the dimension control, [group](https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components) the dimension control with one or more charts.

Ungrouped dimension controls will ignore any charts that are grouped with a dimension control.

To expand the scope of the dimension control to the entire report, make it a [report-level](https://docs.cloud.google.com/data-studio/component-report-level) component.

## Use cases

The application of the dimension control is demonstrated in the following use cases.

### Change geographical granularity

Suppose your organization tracks purchases by location. Using a dimension control, you could allow users to swap among the **Country** , **State** , and **City** dimensions for varying granularity.

### Change product granularity

Suppose you have a dataset with purchase data, and each product has a **Product Type,** a **Product Brand** , and a **Product Name.** Using a dimension control, you could allow users to simultaneously update multiple charts on a report to swap among the three product granularities.

## Related resources

  * [Configure report components](https://docs.cloud.google.com/data-studio/configure-report-components)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
