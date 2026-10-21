---
url: https://docs.cloud.google.com/looker/docs/and-or-filters-in-explores/
title: AND/OR Filters in Explores \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:21.590777+00:00
---

# AND/OR Filters in Explores  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/and-or-filters-in-explores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  AND/OR Filters in Explores Stay organized with collections  Save and categorize content based on your preferences. 

Group and use AND/OR [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting) logic without the need to manually create filter expressions in an Explore.

## Creating AND/OR filters

AND/OR filters appear in the **Filters** section in an Explore. You can customize filters with AND/OR logic when you add or edit a filter on an Explore.

![](https://docs.cloud.google.com/static/looker/docs/images/filter-create-options-and-or-23.10.png)

You can add a filter in several ways:

  * Select a field's **Filter by field** icon filter_list in the Explore [field picker](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#field_picker).
  * Select the **Filter** option from a field's data table gear menu.
  * Select the **Filter** button in the **Filters** section of the Explore.



To remove a filter, click the **Remove** `X` icon next to the filter.

### Filter section options

When you add more than one filter, the option to specify between `AND` and `OR` filter logic and switch between them appears to the left of the filter fields. A new filter group creates a separate set of filters with the option to specify between `AND` and `OR` filter logic between groups. The filters section contains the following options:

![](https://docs.cloud.google.com/static/looker/docs/images/and-or-filter-options-23.10.png)

  1. **AND/OR** logic button — Select this option to switch filter logic. It will say **AND** or **OR** depending on the logic selected. Important: Depending on the filter conditions, the **AND** or **OR** buttons may be unactionable, indicating that the logic cannot be switched.
  2. **\+ Filter** button — Select this option to add another filter in the same group.
  3. **\+ New Group** button — Select this option to create a new filter group.
  4. **\+ Custom expression** button — Select this option to create a custom expression manually using [Lexp](https://docs.cloud.google.com/looker/docs/creating-looker-expressions).



### Filter groups

Filters can be sorted into separate groups that are connected through AND/OR filter logic. For example, there can be multiple filters in groups A and B, and you can set the Explore to filter on `group A` OR `group B`. Groups allow you to filter Explores for multiple conditions that are not directly related.

For example, the following Explore filters contain two groups separated with OR logic:

  1. **Orders Status** is `pending` AND **Users State** is `California` OR
  2. **Products Category** is `active` AND **Inventory Items Cost** is <= `100`



![](https://docs.cloud.google.com/static/looker/docs/images/multiple-filter-groups-23.10.png)

The resulting explore will show order data of `pending` orders in `California` OR orders that contain `Active` category goods costing `less than or equal to 100`.

**Caution:** There is no limit to the number of groups that can be created; however, excessive filter groups may impact browser performance.

## Limitations

The following are limitations for AND/OR filters in Explores:

  * Multiple filters default to using `AND` filter logic.
  * `OR` filters aren't supported when you filter on a measure.
  * `AND` filters aren't supported for [filter-only fields](https://docs.cloud.google.com/looker/docs/reference/param-field-filter).
  * Two or more filter groups default to using `OR` filter logic, unless the filter in the first group includes a required filter. `AND` filter logic is the default if the first filter group includes a required filter.



## Things to know

The following sections include things to know about AND/OR filters and required filters, and AND/OR filters on dashboards.

### AND/OR filters and required filters

Required filters (for example, a filter that is required with the [`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) parameter or [`conditionally_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter) parameter) always appear in the first filter group, or `group A`.

To add multiple filter conditions to a field that is referenced by a required filter, click the **Add** button add next to each condition. `OR` filter logic will automatically be applied between each condition that is added to the required filter field.

You can add multiple filters to `group A` by clicking the **\+ Filter** button, and you can add subsequent filter groups by clicking **\+ New Group**.

**Important:** When `group A` contains a required filter, `AND` filter logic will be applied between all filters within `group A`, and between all subsequent filter groups and `group A`. You can switch the logic between filters within additional filter groups (between filters within `group B`, for example) by clicking the **AND/OR** logic button.

### AND/OR filters on dashboards

AND/OR filters are created in the Explore Filters section and are translated into [Looker expressions](https://docs.cloud.google.com/looker/docs/functions-and-operators) before the query is run. As a result, AND/OR filters behave differently from [basic filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#basic_filters) on dashboards.

If a query that uses both AND and OR filters is added to a dashboard, the filters won't appear in the [dashboard filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#adding_dashboard_filters) section. The filters are still applied to that query, and can be [edited in the corresponding query tile](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_tiles).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
