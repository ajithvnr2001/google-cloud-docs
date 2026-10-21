---
url: https://docs.cloud.google.com/looker/docs/2610/filtering-and-limiting/
title: Filtering and limiting data \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:27.011866+00:00
---

# Filtering and limiting data  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2610/filtering-and-limiting/

You are viewing documentation for Looker 26.10. Click this link to see the [most recent documentation](https://docs.cloud.google.com/looker/docs/intro). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/2610/intro)



Send feedback 

#  Filtering and limiting data Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are using Looker's [new Explore experience](https://docs.cloud.google.com/looker/docs/2610/new-explore-experience-overview), see the [Filtering and limiting data in the new Explore experience](https://docs.cloud.google.com/looker/docs/2610/filtering-and-limiting-new-explore-experience) documentation page.**Note:** This page is part of the [Retrieve and chart data](https://docs.cloud.google.com/looker/docs/2610/retrieve-and-chart-data) learning series.

This page explains how a user can filter and limit data in a Looker [Explore](https://docs.cloud.google.com/looker/docs/2610/creating-and-editing-explores). For example, a user can filter the Explore's query results to the last three months or for a certain customer. Users can also limit the number of rows that are displayed in an Explore or the number of pivot columns that are displayed in an Explore.

**Note:** Other ways to filter data with Looker include the following: 

  * You can set up your Looker dashboards with optional or required filters for your users to filter the data that they see on dashboards. See [Adding and editing user-defined dashboard filters](https://docs.cloud.google.com/looker/docs/2610/filters-user-defined-dashboards) for more information.
  * Looker developers can specify required filter behavior using LookML. See [Creating required filters with LookML](https://docs.cloud.google.com/looker/docs/2610/creating-required-filters-with-lookml) for more information.



## Filtering data

Filters let you restrict the data that you are viewing to items of interest. Any field in your Looker instance can become a filter.

You also don't necessarily need to add a dimension or measure to your results to filter on it. For example, you can create a query that filters the **Order Date** to the last 90 days, even though your results only show **Customer** and **Number of Orders**.

You can use any combination of these filter types in your query:

  * **Basic Filters** are the most commonly used; Looker provides appropriate drop-down lists, calendar widgets, and text fields.

  * **Advanced Matches** allow for a more advanced condition for a field, such as intricate text searches, or a date range that starts in the past and extends for a certain number of days.

  * **Custom Filters** let you specify detailed business logic, combine `AND` and `OR` logic, or use Looker functions.




### Basic filters

You can add a basic filter in a couple of different ways:

  * In the Field Picker, select **Filter by field** to the right of the field name.
  * In the **Results** tab of the **Data** panel, select the gear in the field header, and then select **Filter**.



Filters appear in the **Filters** section. To remove a filter, select **Remove** to the right of the filter clause.

#### Standard filters

Standard filter options vary by filter type. For example, a time dimension lets you select a time range; a numeric dimension provides you with options such as **is** or **is >**.

**Note:** For date and time filters, the condition **is in the last** refers to the current time period and the previous number of time periods minus the current time period. For example:

  * **is in the last 7 days** means the current day and the previous six days.
  * **is in the last 1 week** means the current week.
  * **is in the last 6 months** refers to the current month and the previous five months.



For text dimensions, Looker displays a list of existing data values for the field. As you type, Looker narrows the list to values that include that text.

To filter on a large set of values, paste a list of values into the filter field. The maximum number of values that you can paste may be limited by your browser or other elements in your network, and may be as small as 2,000.

To enter a special character in a standard filter, first add a leading backslash. For example, to filter on `Santa Cruz, CA`, you would enter `Santa Cruz \, CA`.

To add another option to the filter, select **\+ Filter**. This action opens the **Add Filter** dialog, which lets you choose a field on which to create the new filter option. To add a new filter [group](https://docs.cloud.google.com/looker/docs/2610/and-or-filters-in-explores#filter_groups), select **\+ New group** in the **Filters** section.

When you add more than one filter, the option to specify between [`AND` and `OR` filter logic](https://docs.cloud.google.com/looker/docs/2610/and-or-filters-in-explores) and switch between them appears to the left of the filter fields. A new filter [group](https://docs.cloud.google.com/looker/docs/2610/and-or-filters-in-explores#filter_groups) creates a separate set of filters with the option to specify between `AND` and `OR` filter logic between groups.

#### Custom calendar filters

[Custom calendars](https://docs.cloud.google.com/looker/docs/2610/custom-calendars) let you define a business calendar, such as a fiscal or retail calendar, and apply it to a date-based dimension group in your LookML model.

Filter options for custom calendars appear only when you filter on a custom calendar dimension group. These options let you filter by custom timeframes, such as **is in the last 3 custom years** or **is this custom period**. Custom calendar filters support timeframes such as custom period, custom season, custom year, custom quarter, custom week, and custom day.

#### Filters with user attributes

Looker admins can [configure user attributes](https://docs.cloud.google.com/looker/docs/2610/admin-panel-users-user-attributes) that specify user-specific values. For example, an admin can define a user attribute for a sales region and assign the appropriate values to individual users or groups of users.

User attributes let you automatically customize a Look or dashboard for each user who views it. The **matches a user attribute** condition provides this user-specific flexibility. For example, you can filter a sales region dimension in a Look to equal a sales region user attribute. The Look will filter for the user's specific sales region and automatically adjust to show each user the data for their own sales region.

### Advanced matches filters

To add an advanced matches filter, select the **matches (advanced)** option from the filter's condition drop-down menu.

In the text field, enter your filter expression. To view all available filter expressions, see the [Looker filter expressions](https://docs.cloud.google.com/looker/docs/2610/filter-expressions) documentation page.

To enter a special character in an advanced matches filter, first add a leading carat (`^`). For example, to filter on `Santa Cruz, CA`, you would enter `Santa Cruz ^, CA`.

Your Looker admin can configure user-specific values, called **user attributes** , that let you automatically customize a Look for each user. To reference a user attribute in an advanced matches filter, use the following syntax:
    
    
    {{ _user_attributes['USER_ATTRIBUTE_NAME'] }}
    

### Custom filters

Custom filters let you write the fields, constants, functions, and operators to customize your filtering. Looker lets you build an expression that evaluates as `yes` or `no`. When you run the query, Looker only returns rows for which that condition is `yes`.

#### Adding a custom filter

To add a custom filter from the **Filters** section, follow these steps:

  1. Select **\+ Custom expression**.
  2. Enter a dimension or function to have Looker display a list of functions, operators, and field names to use in your expression. Select a term in the drop-down to add it to your expression. When finished, your custom filter expression must evaluate to `yes` or `no`.
  3. Select **Save**.
  4. Select **Run** (or use the keyboard shortcut Command-Enter for Mac or Ctrl+Enter for Windows) to run your query with your custom filter applied.



The **[Creating Looker expressions](https://docs.cloud.google.com/looker/docs/2610/creating-looker-expressions)** documentation page explains how to create Looker expressions and how the editor can assist you.

Looker expressions can use as many fields, functions, and operators as your business logic requires. The more complex your condition, the more work your database must do to evaluate it; complex conditions may lengthen query times.

**Note:** Because custom filters are used to create a database query, you cannot refer to measures in a custom filter or use any functions that rely on query results. The [Creating Looker expressions](https://docs.cloud.google.com/looker/docs/2610/creating-looker-expressions) documentation page explains how to use Looker expressions in custom fields in more detail. The [Looker functions and operators](https://docs.cloud.google.com/looker/docs/2610/functions-and-operators) documentation page shows you the available functions and identifies which can be used in a custom filter.

#### Removing a custom filter

To remove a custom filter expression from the query, select **Remove** from the **Custom Filter** header. If you leave the browser page open, Looker remembers what you typed and your expression reappears if you select **Custom Filter** again.

### Filtering dimensions: restricts raw data before calculations

When you filter on a dimension, you restrict the raw data _before_ any calculations are made.

For example, say you've created an Explore to view how many orders were placed each day. The Explore includes the **Orders Created Date** and **Orders Count** fields. Then, you add a filter on an **Order Status** dimension with the condition `is COMPLETED`.

![](https://docs.cloud.google.com/static/looker/docs/images/orders-filter-dimension-2420.png)

Looker removes all orders that have _not_ been completed from the data. The measure still counts the remaining orders for each day, but the measure values are lower.

### Filtering measures: restricts results after calculating measures

When you filter on a measure, you restrict the results _after_ the measure has been calculated.

For example, say you've created an Explore to view how many orders were placed each day. The Explore includes the **Orders Created Date** and **Orders Count** fields. Then, you add a filter on the **Order Count** measure with the condition `is < 20`.

![](https://docs.cloud.google.com/static/looker/docs/images/orders-filter-measure-2420.png)

Looker first counts all orders for each day. Then, the filter is applied. The filter limits the dataset to only the days that had fewer than 20 orders. You may need to turn off Looker's [**dimension fill**](https://docs.cloud.google.com/looker/docs/2610/creating-visualizations#filling_in_missing_dates_and_values) option if Looker is returning null values.

## Limiting data

Looker supports up to 5,000, or up to 50,000 rows [if a higher limit is specified by your admin](https://docs.cloud.google.com/looker/docs/2610/admin-panel-performance-center-content-guardrails#visualization-limits). Looker supports up to 200 columns for pivoted or unpivoted query results. For browser performance, 50 or fewer columns is recommended. Looker sets a default column limit of 50 columns for pivoted query results.

To see a subset of your complete query results, you can set a row limit, a column limit, or both.

### Row limits

You can set a row limit of up to 5,000 rows, or up to 50,000 rows [if a higher limit is specified by your admin](https://docs.cloud.google.com/looker/docs/2610/admin-panel-performance-center-content-guardrails#visualization-limits). Looker warns you if you might be hiding data by setting a row limit that is too low. The sort order is important: Looker _first_ applies the sort and _then_ applies the limit. For example, in a query that contains the fields **Orders Created Month** and **Orders Count** , sort by **Orders Count** and then specify a row limit of **5** to see the months that had the top five number of orders.

![](https://docs.cloud.google.com/static/looker/docs/images/filter-data-row-limit-2420.png)

For more information about row limits in other parts of Looker, see the [What are all the row limits in Looker?](https://docs.cloud.google.com/looker/docs/2610/best-practices/row-limits-in-looker) Best Practices page.

**Note:** If you reach a row limit, you cannot sort by [row totals](https://docs.cloud.google.com/looker/docs/2610/creating-and-editing-explores#cant-sort-row-totals) or [table calculations](https://docs.cloud.google.com/looker/docs/2610/table-calculations#cannot-sort).

### Column limits

If you added a pivot to your query results, you can apply a column limit of up to 200. Looker warns you if you might be hiding data by setting a column limit that is too low. The sort order of your pivot is important: Looker _first_ applies the sort and _then_ applies the limit. For example, in a query that contains the field **Orders Count** and that is pivoted by the **Orders Created Month** field, sort by **Orders Created Month** to see the five most recent months when orders were created.

![The Column Limit field appears in the data bar.](https://docs.cloud.google.com/static/looker/docs/images/d-data-column-limit-2304.png)

Dimensions, dimension table calculations, row total columns, and measure table calculations outside of pivots are not counted toward the column limit. Pivoted groups count as one column toward the column limit.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
