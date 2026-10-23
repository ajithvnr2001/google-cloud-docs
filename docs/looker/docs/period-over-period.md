---
url: https://docs.cloud.google.com/looker/docs/period-over-period/
title: Period-over-period measures in Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:24.809003+00:00
---

# Period-over-period measures in Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/period-over-period/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Period-over-period measures in Looker Stay organized with collections  Save and categorize content based on your preferences. 

Period-over-period (PoP) analysis is a pattern of analysis that measures something in the present and compares it to the same measurement in a comparable period of time in the past.

For dialects that support PoP measures, Looker developers can add PoP measures to LookML projects to enable PoP analysis in the corresponding Looker Explores.

For example, the following Looker Explore query shows the number of orders that were created in the current month, along with PoP measures for the number of orders created last year, the difference from last year, and the percentage change from last year. You can verify the year-over-year comparison by spot-checking the values. For example, the value for **Orders Last Year** for `2012-03` is the same as the value for **Orders Count** for `2011-03`:

![Looker Explore showing the Orders Last Year for 2012-03 is 89 and the Orders Count for 2011-03 is also 89.](https://docs.cloud.google.com/static/looker/docs/images/pop-measure-explore-2506.png)

To add a PoP measure to a LookML project, a Looker developer must create a `measure` of `type: period_over_period` and include the subparameters that are described in the following section of this page.

For example, here is the LookML for a PoP measure that provides the order count for the previous year:
    
    
      measure: order_count_last_year {
        type: period_over_period
        description: "Order count from the previous year"
        based_on: orders.count
        based_on_time: orders.created_year
        period: year
        kind: previous
      }
    

This PoP measure has the following attributes:

  * It is defined with `based_on: orders.count`, so the PoP measure will provide data about order count from the previous time period.
  * It is defined as `kind: previous`, meaning that it provides the count value from the previous time period (as opposed to providing a difference in order count from the previous time period, or a percentage of change in order count from the previous time period).
  * It is defined with `period: year`, so it will provide order counts from a comparable amount of time from the previous year.



## Subparameters of PoP measures

A PoP measure is a `measure` of `type: period_over_period` that includes the subparameters that are described in the following sections:

  * `based_on`
  * `based_on_time`
  * `kind`
  * `period`
  * `custom_calendar_period`
  * `value_to_date`



As described in the Explore queries with PoP measures section, PoP measures calculate their values based on both the PoP measure's LookML definition and the fields in an Explore query. Because of this, you should adhere to the following best practices when creating a PoP measure in LookML:

  * Provide to your Explore users an indication of the PoP measure's period, either in the name of the PoP measure or in the measure's `description` subparameter.
  * Provide to your Explore users an indication of the PoP measure's `based_on` measure, either in the name of the PoP measure or in the measure's `description` subparameter.



For example, the following PoP measure is named `order_count_last_year`, and a description is included to let users know that the measure provides the number of orders from the previous year:
    
    
      measure: order_count_last_year {
        type: period_over_period
        description: "Order count from the previous year"
        based_on: orders.count
        based_on_time: orders.created_year
        period: year
        kind: previous
      }
    

### `based_on`

Use the `based_on` field to specify the LookML measure that the PoP measure is based on. For example, to base a PoP measure on the `orders.count` field, you would enter the following:
    
    
        based_on: orders.count
    

A PoP measure based on `orders.count` will provide information about the number of orders from a previous time period so that you can compare the number of sales between a current period and a previous period.

The LookML measure that you specify in the `based on` field must be one of the following types of measures:

  * [`average`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average)
  * [`average_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average_distinct)
  * [`count`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count)
  * [`count_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count_distinct)
  * [`list`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#list)
  * [`max`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#max)
  * [`median`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median)
  * [`median_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median_distinct)
  * [`number`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#number)
  * [`min`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#min)
  * [`percentile`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile)
  * [`percentile_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile_distinct)
  * [`sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum)
  * [`sum_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum_distinct)



### `based_on_time`

Use the `based_on_time` subparameter to provide Looker with a time field that it can use to calculate the PoP measure values. This time field can be one of the following:

  * A [time-based dimension](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#individual-timeframes). If you specify a time-based dimension in the `based_on_time` subparameter, your users must include the exact same time-based dimension in all queries that use the PoP measure. Also, the timeframe of the time-based dimension must be equal to or smaller than the PoP measure's `period` value. For example, if the PoP measure is defined with `based_on_time: created_month`, the PoP measure's `period` value can't be `week` or `date`.
  * One of the following timeframes of a [dimension group of `type: time`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_time):

    * `year`
    * `fiscal_year`
    * `month`
    * `fiscal_quarter`
    * `quarter`
    * `week`
    * `date`
    * `raw`
  * One of the following timeframes of a [dimension group of `type: custom_calendar`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#custom_calendar_type)

    * `custom_date`
    * `custom_period`
    * `custom_quarter`
    * `custom_season`
    * `custom_week`
    * `custom_year`



If you specify a dimension group timeframe in the `based_on_time` subparameter, the specific timeframe that you use is irrelevant -- you just need to point the PoP measure at a dimension group of `type: time` so that the PoP measure can use the underlying timestamp of the dimension group. You can't specify a timeframe from a [dimension group of `type: duration`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_duration); duration type dimension groups are not supported and will produce a runtime error in the Explore.

### `kind`

Use the `kind` parameter to specify the type of calculation that you want the PoP measure to make for the previous period. You can specify one of the following values for `kind`:

  * `previous`: (default) The value from the previous period.
  * `difference`: The difference between periods (the previous period subtracted from the current period).
  * `relative_change`: The percentage change from previous period. The percentage change is calculated by the following equation:

$$ relativeChange = (current - previous)/previous $$ 




### `period`

Use the `period` subparameter to specify the PoP measure's _cadence_ , how far back you want to jump in your comparison. For example, a PoP measure that's defined with `period: year` will show the values for the previous year. If you run an Explore query on monthly order count, the `period: year` PoP measure will show the values for the same month in the previous year, so that you can compare the order count for November 2025 to the sales count of November 2024.

The `period` subparameter supports the following values:

  * `year`
  * `fiscal_year`
  * `quarter`
  * `fiscal_quarter`
  * `month`
  * `week`
  * `date`



### `custom_calendar_period`

If your PoP measure is based on a [custom calendar](https://docs.cloud.google.com/looker/docs/custom-calendars) (if the PoP measure's `based_on_time` parameter specifies a timeframe of a [dimension group of `type: custom_calendar`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#custom_calendar_type)), you must use the `custom_calendar_period` parameter instead of the `period` parameter.

Use the `custom_calendar_period` subparameter to specify the PoP measure's _cadence_ , how far back you want to jump in your comparison. For example, a PoP measure that's defined with `custom_calendar_period: custom_year` will show the values for the previous year (as defined in your custom calendar). If you run an Explore query on custom_monthly order count, the `custom_calendar_period: custom_year` PoP measure will show the values for the same month in the previous year, so that you can compare the order count for the custom month in 2026 to the sales count of the same custom month in 2025.

The `custom_calendar_period` subparameter supports the following values:

  * `custom_date`
  * `custom_period`
  * `custom_quarter`
  * `custom_season`
  * `custom_week`
  * `custom_year`



See the Using PoP measures with custom calendars section for more information on creating PoP measures that use a custom calendar.

### `value_to_date`

Use the `value_to_date` subparameter to indicate whether Looker should calculate the values for the PoP measure by using the amount of time that has elapsed in the current timeframe at the time the query is run. The `value_to_date` subparameter can be `no` (default) or `yes`.

  * A value of `no` will assume the whole timeframe window when aggregating data.
  * A value of `yes` will calculate the amount of time observed in the current period and apply it to the PoP measure.



For example, with a month-over-month PoP measure that is defined with `value_to_date: yes`, if at 13:10:00 on June 6 you run an Explore query with the PoP measure and a date timeframe dimension, Looker will apply the amount of time that has elapsed on June 6 (13 hours, 10 minutes, and 0 seconds) to the calculations for each of the dates in the query. For each date, Looker will provide the values for the first 13 hours and 10 minutes.

If you had the same PoP measure that was defined with `value_to_date: no` and you ran the same Explore query on June 6 at 13:10:00, Looker would calculate the value for the PoP using all of the data that is available for each date. If you are trying to compare values from June 6 to the 6th of the previous month, be aware that since June 6 isn't over yet it's possible that there will be additional data after 13:10:00.

See How `value_to_date` affects PoP measure values for an example of how `value_to_date: yes` affects the results in an Explore query.

As described in the Requirements for Explore queries with PoP measures section, when you run an Explore query with a PoP measure, Looker automatically applies the minimum timeframe granularity from the query to the timeframe that's used by the PoP measure. For Explore queries with a PoP measure defined with `value_to_date: yes`, Looker takes the smallest timeframe dimension in the query and calculates the portion of that timeframe that has passed when the query is run, and then applies that portion to all of the values for the PoP measure.

## Explore queries with PoP measures

The calculation that's performed for a PoP measure is based on the PoP measure's LookML definition and also on the timeframes that are specified in the Explore query itself; the PoP measure adapts its calculation to the timeframes that are selected in the Explore query. For example, if the PoP measure is defined with `period: year`, and the Explore query contains the `orders.created_month` timeframe dimension, the PoP measure will calculate monthly values, comparing January 2025 to January 2024. If you want to see the yearly values, you would have to run an Explore query with the PoP measure and only the `orders.created_year` timeframe.

Here are some examples of how a PoP measure's `period` interacts with the timeframes that are selected in an Explore query:

  * If a PoP measure is defined with `period: year`, and you run an Explore query with a quarter timeframe, the PoP measure will return values from the same quarter in the previous year (Q1 of 2025 compared to Q1 of 2024).
  * If a PoP measure is defined with `period: year`, and you run an Explore query with a month timeframe, the PoP measure will return values from the same month in the previous year (April 2025 compared to April 2024).
  * If a PoP measure is defined with `period: month`, and you run an Explore query with a month timeframe, the PoP measure will return values for the previous month (April 2025 compared to March 2025).



### Requirements for Explore queries with PoP measures

Because a PoP measure makes calculations based on both the LookML definition of the PoP measure and the fields that you select in the Explore query, at a minimum you must include the following fields in an Explore query that has a PoP measure:

  * The PoP measure.
  * A time dimension that is appropriate for the `period` associated with the PoP measure. The time dimension can be included in the query either from the Explore's field picker or in the Explore's filters: 
    * PoP measure queries support timeframe granularities of date or larger, such as month, quarter, or year. PoP measure queries don't support dimensions with timeframes of hours or minutes.
    * If the PoP measure is defined with a `based_on_time` that is a timeframe of a dimension group, then the Explore query must include a timeframe from the same dimension group that uses an equal or smaller timeframe than what is specified in the `period` parameter of the PoP measure. You can include the dimension group in the Explore itself (by selecting the dimension group from the Explore's field picker) or by filtering on the dimension group. For example, if the PoP measure's `based_on_time` value is defined with a timeframe from the `orders.created` dimension group and the PoP measure is defined with `period: month`, the Explore query must include a timeframe from the `orders.created` dimension group that is equal to or smaller than a month, such as `orders.created_date`. The timeframe in the Explore query must match or be smaller because, for example, you can't do a month-over-month comparison of a year timeframe.
    * If the PoP measure is defined with a `based_on_time` that is a [time-based dimension](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#individual-timeframes), then the Explore query must include the exact same time-based dimension, either by including the dimension from the Explore's field picker, or by specifying a filter on the dimension. The time-based dimension must be of an equal or smaller timeframe than what is specified in the `period` parameter of the PoP measure. For example, if the PoP measure is defined with `based_on_time: created_date` and the PoP measure is defined with `period: month`, the Explore query must include the `created_date` dimension.



If the PoP measure is defined with a `based_on_time` that is a timeframe of a dimension group, note the following requirements for the timeframe in the Explore query:

  * The timeframe in the Explore query must be an equal or smaller timeframe than what is specified in the `period` parameter of the PoP measure. For example, if the PoP measure's `based_on_time` is defined with a timeframe from the `orders.created` dimension group and the PoP measure is defined with `period: month`, the Explore query must include a timeframe from the `orders.created` dimension group that is equal to or smaller than a month, such as `orders.created_date`. The timeframe in the Explore query must be smaller because, for example, you can't do a month-over-month comparison of a year timeframe.
  * The timeframe in the Explore query must itself contain timestamp information. For example, the `year`, `month`, and `date` timeframes of a dimension group provide actual timestamp information. In contrast, the `day_of_week` timeframe is abstracted from the underlying timestamp to provide a value such as `Wednesday`. Similarly, timeframes such as `month_name`, `month_num`, and `day_of_month` don't provide timestamp information themselves, so they can't be used by PoP measures to calculate values for the previous period. However, if you include in the Explore query a timestamp such as `date`, that will provide the PoP measure with timestamp information that it can use to calculate values for the previous period. You can _also_ include the `day_of_week` timeframe in the Explore query, because the PoP measure can use the `date` timeframe information for calculations.



As long as you meet these requirements in your Explore query, you can add other fields and timeframe dimensions in the Explore query, but all of the timeframes in the Explore query must be equal to or smaller than the timeframe from the PoP measure's `period` timeframe. When you run an Explore query with a PoP measure, Looker automatically applies the minimum timeframe granularity from the query to the timeframe used by the PoP measure. In the example Explore shown at the beginning of this page, the PoP measures have all been defined in LookML with `period: year`. This means that for whatever timeframe is selected in the Explore query -- in this case, a monthly timeframe -- the PoP measure will return the results for the same timeframe in the previous year.

If you want to see which timeframes are supported with your PoP measure in an Explore, you can test different timeframes without having to run queries. Click the **SQL** tab of the Explore's **Data** section, and then add fields and filters from the Explore's field picker. If the PoP measure can't calculate your the query with your selected fields and filters, the **SQL** tab will show a message that the SQL can't be generated.

![](https://docs.cloud.google.com/static/looker/docs/images/pop-measure-sql-tab-2506.png)

If you do run a query where the SQL can't be generated, the Explore window will return an error with the details and a link to the relevant LookML.

![](https://docs.cloud.google.com/static/looker/docs/images/pop-measure-error-msg-2506.png)

## Using PoP measures with custom calendars

To create a PoP measure that uses a [custom calendar](https://docs.cloud.google.com/looker/docs/custom-calendars), you must do the following:

  * In the [view file where you model your custom calendar](https://docs.cloud.google.com/looker/docs/custom-calendars#define_custom_calendar_view), optionally include a [`previous_ordinal_mapping`](https://docs.cloud.google.com/looker/docs/reference/param-view-calendar-definition#previous_ordinal_mapping) parameter block in your `calendar_definition` parameter block. The `previous_ordinal_mapping` parameter is optional starting in Looker 26.8. In Looker 26.8 and later, Looker assumes for custom calendars that the previous week for Week 1 is Week 52, and the previous day for Day 1 is Day 364. If this isn't the case for your custom calendar, you need to use the `previous_ordinal_mapping` parameter block.
  * In the PoP measure's LookML definition, in the `based_on_time` parameter, specify the year timeframe of a [dimension group of `type: custom_calendar`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#custom_calendar_type)
  * In the PoP measure's LookML definition, use the `custom_calendar_period` parameter instead of the `period` parameter.



For example, here is the LookML for a custom calendar dimension group and a PoP measure that uses the custom calendar:
    
    
    dimension_group: cust_created {
        type: custom_calendar
        sql: {TABLE}.created_at;;
        based_on_calendar: cust_retail_calendar
        custom_timeframes: [custom_year, custom_quarter]
    
      }
    
    measure: count_last_custom_year {
        type: period_over_period
        based_on: count
        based_on_time: cust_created_custom_year
        custom_calendar_period: custom_year
        kind: previous
      }
    
    

## Examples

The following sections show some examples of different PoP measures and Explore queries:

  * Comparing counts to year-over-year and month-over-month PoP measures
  * How `value_to_date` affects PoP measure values



### Comparing counts to year-over-year and month-over-month PoP measures

Here is the LookML for an example `total_births` measure, a `birth` dimension group of `type:time`, and two PoP measures that are based on the `total_births` measure and that use the `birth` dimension group as their `based_on_time` field:
    
    
      dimension_group: birth {
        type: time
        timeframes: [raw, time, date, week, month, quarter, year]
        sql: ${TABLE}.birth_date ;;
      }
    
      measure: total_births {
        type: sum
        sql: ${TABLE}.total_births ;;
      }
    
      measure: total_births_last_year {
        type: period_over_period
        kind: previous
        based_on: total_births
        based_on_time: birth_year
        period: year
        value_to_date: no
        value_format_name: decimal_0
      }
    
      measure: total_births_last_month {
        type: period_over_period
        kind: previous
        based_on: total_births
        based_on_time: birth_year
        period: month
        value_to_date: no
        value_format_name: decimal_0
      }
    

Note the following about these fields:

  * Both of the PoP measures are defined with `kind: previous`, so they both provide the value of the measure from the previous period.
  * Both of the PoP measures are defined with `value_to_date: no`, so they both calculate the value of the measure for the entire timeframe (that is, the minimum timeframe granularity from the query).
  * Both of the PoP measures are defined with `based_on_time: birth_year`, so they both use the underlying timestamp of the `birth` dimension group.
  * The `total_births_last_year` PoP measure is defined with `period: year`, and the `total_births_last_month` PoP measure is defined with `period: month`.



Here is an Explore query that includes all three of the measures and the `birth_month` dimension timeframe:

![Looker Explore showing columns for Birth Month, Total Births, Total Births Last Month, Total Births Last Year. The Total Births Last Month value for 2024-07 is 290,699, which matches the Total Births value for 2024-06. The Total Births Last Year value for 2024-07 is 310,347, which matches the Total Births value for 2023-07.](https://docs.cloud.google.com/static/looker/docs/images/pop-measure-explore-mnth-year-2506.png)

Note the following about the Explore results:

  * The smallest dimension timeframe in the Explore query is `birth_month`, so the PoP measure provides monthly values.
  * In the row for the most recent month, **2024-07** , the **Total Births Last Month** value shows the total births for the previous month, 2024-06. You can verify this by looking at the **Total Births** value for the **2024-06** row. The two values match.
  * In the row for the most recent month, **2024-07** , the **Total Births Last Year** value shows the total births for the same month (07) in the previous year (2023). You can verify this by looking at the **Total Births** value for the **2023-07** row. The two values match.



### How `value_to_date` affects PoP measure values

Similar to the previous example, here is the LookML for the `total_births` measure and the `birth` dimension group of `type:time` and two PoP measures that are based on the `total_births` measure and that use the `birth` dimension group as their `based_on_time` field. However, in this example, the `total_births_last_year_value_to_date` PoP measure is defined with `value_to_date: yes` and the `total_births_last_year` PoP measure is defined with `value_to_date: no`:
    
    
      dimension_group: birth {
        type: time
        timeframes: [raw, time, date, week, month, quarter, year]
        sql: ${TABLE}.birth_date ;;
      }
    
      measure: total_births {
        type: sum
        sql: ${TABLE}.total_births ;;
      }
    
      measure: total_births_last_year {
        type: period_over_period
        kind: previous
        based_on: total_births
        based_on_time: birth_year
        period: year
        value_to_date: no
        value_format_name: decimal_0
      }
    
      measure: total_births_last_year_value_to_date {
        type: period_over_period
        kind: previous
        based_on: total_births
        based_on_time: birth_year
        value_to_date: yes
        period: year
        value_format_name: decimal_0
      }
    
    

Here is an Explore query that includes all three of the measures and the `birth_year` dimension timeframe. This Explore query was run on June 4 at 16:25:08, which is significant for the `value_to_date: yes` PoP measure.

![Looker Explore showing columns for Birth Year, Total Births, Total Births Last Year, Total Births Last Year Value to Date. The Total Births Last Year value for 2024 is 3,581,036, which matches the Total Births value for 2023. The Births Last Year Value to Date value for 2024 is 1,743,505.](https://docs.cloud.google.com/static/looker/docs/images/pop-measure-value-to-date-2510.png)

The Explore results show how the `value_to_date` subparameter changes the calculation for the PoP measures:

Note the following about the Explore results:

  * In the row for the most recent year, **2024** , the **Total Births Last Year** value shows the total births for the previous year, 2023. You can verify the calculation by looking at the **Total Births** value for the **2023** row. The two values match.
  * In the row for the most recent year, **2024** , the **Total Births Last Year Value to Date** value is less than the **Total Births Last Year** value. This is because the Explore query was run on June 4 at 16:25:08, and because the `total_births_last_year_value_to_date` PoP measure is defined with `value_to_date: yes`, so Looker calculated the yearly values using only the data up to June 4 at 16:25:08 for each year.



## Filtering Explore queries that include PoP measures

Note the following for filtering Explore queries that include PoP measures:

  * Filtering is supported for Explore queries that include PoP measures. However, you can't filter on a PoP measure itself. For example, in the first example Explore that queries on the `birth_month` dimension and the `total_births`, `total_births_last_year`, and `total_births_last_month` PoP measures, you couldn't filter that query on the `total_births`, `total_births_last_year`, or `total_births_last_month` PoP measures.
  * When you filter on a field that's associated with the `based_on_time` parameter of a PoP measure, if the timeframe of the filter is finer than the timeframe of the query, the PoP measure will show only the results for the filter-value portion of the query's timeframe. For example, if you query on the `orders.created_year` dimension and you filter the query for the month of January, for each year the PoP measure will show the values for January only. This can be mistaken for being the results for the full year.
  * For PoP measure Explore queries, to calculate data for the PoP measure, Looker retrieves data for an extra time period at the least granular time period granularity of the query. For example, if you create an Explore query with a monthly dimension, a PoP measure defined with `period: year`, and a filter for the last 6 months, Looker will identify the least granular granularity in the query, which in this example would be the PoP measure's `year` time period. In this example, Looker would retrieve the last 6 months of data plus an additional year's worth of data so that it can compare each of the last 6 months to the same month in the previous year.
  * As described in Requirements for Explore queries with PoP measures, Explore queries that include PoP measures must have a time dimension that is appropriate for the `period` that is associated with the PoP measure. If you don't select a time dimension from the Explore's field picker, Looker can derive the required information from time dimensions in the Explore's filters. In this case, Looker will sort the Explore query results by the filter's time dimension.



## Visualizations with PoP measures

The [table chart visualization](https://docs.cloud.google.com/looker/docs/table-options) is recommended for PoP measures. Other visualization options may work as well, depending on the fields in your Explore query.

If you use a visualization other than a table chart, verify that your visualization is clear. Because PoP measures provide comparisons to a previous time period, visualizations with PoP measures may be misleading. For example, a year-over-year PoP measure that's defined as `kind: previous` will show last year's value for this year's date. If your Explore query includes the current year's value along with the year-over-year PoP measure, the current year will have two values in the visualization.

If you use a visualization other than a table chart, verify that your visualization clearly indicates that any PoP measures are a comparison to a previous time period.

## Limitations for PoP measures

Note the following limitations of PoP measures:

  * PoP measures are supported only for LookML projects that use the [new LookML runtime](https://docs.cloud.google.com/looker/docs/best-practices/lookml-runtime-migration). If the [**Use Legacy LookML Runtime**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#current_legacy_features) legacy feature is enabled on your instance, the [manifest file](https://docs.cloud.google.com/looker/docs/lookml-project-files#project_manifest_files) for your project must include a [`new_lookml_runtime:yes`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime) statement.
  * PoP measures aren't supported with the [Looker connector in Data Studio](https://docs.cloud.google.com/looker/docs/looker-studio-connector).
  * PoP measures must be based on an aggregate measure, as described in the `based_on` section. You cannot base a PoP measure on a non-aggregate measure.
  * For BigQuery connections on instances where the [**BI Engine Symmetric Aggregates**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#bi_engine_symmetric_aggregates) Labs feature is enabled, PoP measures are supported, but SQL queries with PoP measures won't use the BI Engine Symmetric Aggregates feature.
  * PoP measures don't support cohort analysis.
  * PoP measures don't support rolling calculations.
  * PoP measures always compare the current period to the previous period. You can't configure a PoP measure to compare the current period to a different period other than the previous period. For example, you cannot create a PoP measure to compare May of last year to December of this year.
  * PoP measures are not supported with arbitrary intervals, such as the current two weeks compared to the previous two weeks.
  * [Liquid parameters](https://docs.cloud.google.com/looker/docs/templated-filters) are not supported in the parameters of a PoP measure. However, if the `based_on` or `based_on_time` fields of a PoP measure point to a dimension that is defined with Liquid, that Liquid will be processed.
  * For [PoP measures that use custom calendars](https://docs.cloud.google.com/looker/docs/period-over-period#custom_calendar_example):

    * (Before Looker 26.8) The `based_on_time` parameter must reference the `custom_year` timeframe of a [dimension group of `type: custom_calendar`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#custom_calendar_type).
    * (Before Looker 26.8) For PoP measures that are defined with `custom_calendar_period: custom_year`, if the user query contains `custom_week` or `custom_date`, Looker will provide the value for the previous week or date of the previous year.
  * PoP measures are not supported with the following Looker features:

    * [Aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness)
    * [Row totals](https://docs.cloud.google.com/looker/docs/table-options#row_totals)
    * [Subtotals](https://docs.cloud.google.com/looker/docs/table-options#subtotals)
    * [Totals](https://docs.cloud.google.com/looker/docs/table-options#totals)
  * PoP measures can't be used to create a [custom field](https://docs.cloud.google.com/looker/docs/custom-fields).

  * For week-based comparisons, it is recommended that you create a [PoP measure that uses a custom calendar](https://docs.cloud.google.com/looker/docs/period-over-period#custom_calendar_example).

  * PoP measures with periods that are defined with fiscal timeframes can't be used in Explore queries with non-fiscal timeframes. Also, PoP measures with periods that are defined with non-fiscal timeframes can't be used in queries with fiscal timeframe dimensions.

  * PoP measures support fiscal month offset, in that the PoP measure's `based_on_time` parameter will inherit the [`fiscal_month_offset`](https://docs.cloud.google.com/looker/docs/reference/param-model-fiscal-month-offset) value from the LookML model file that is associated with the Explore. If you define a PoP measure with `fiscal_year` or `fiscal_quarter`, the PoP measure will be supported in an Explore query only if the Explore query specifies a `fiscal_year` or `fiscal_quarter` timeframe. In that case, the `fiscal_offset_month` is honored.

  * The `period` of the PoP measure must be equal to or larger than the timeframe that's selected in the Explore query. For example, for a PoP measure that's defined with `period: month`, the Explore query must have a timeframe dimension of a month or smaller, such as week or day.

  * Always include the matching timeframe dimension in the Explore alongside the `date_time` dimension when using PoP measures. For example, if you define a PoP measure to calculate values for the corresponding month in the previous quarter, you must include the matching quarter dimension (such as `[dimension_name]_quarter`) in the Explore alongside the month dimension. Without the matching timeframe dimension, the generated SQL applies a truncation function (such as `TIMESTAMP_TRUNC(..., QUARTER)`) to the date before calculating the previous period, causing the query to evaluate based on the beginning of the quarter.

For example, in a comparison for February, the generated SQL would retrieve the value for the first month of the previous quarter (October) instead of the corresponding month (November). Including the matching timeframe dimension in the Explore ensures proper SQL generation and grouping.




## Supported database dialects for PoP measures

The following table shows which dialects support PoP measures in the latest release of Looker:

Dialect | Supported?  
---|---  
Actian Avalanche|   
Amazon Athena|   
Amazon Aurora MySQL|   
Amazon Redshift|   
Amazon Redshift 2.1+|   
Amazon Redshift Serverless 2.1+|   
Apache Druid|   
Apache Druid 0.13.x - 0.17.x|   
Apache Druid 0.18+|   
Apache Hive 2.3+|   
Apache Hive 3.1.2+|   
Apache Spark 3+|   
ClickHouse|   
ClickHouse 26+|   
Cloudera Impala 3.1+|   
Cloudera Impala 3.1+ with Native Driver|   
Cloudera Impala with Native Driver|   
DataVirtuality|   
Databricks|   
Denodo 7|   
Denodo 8 & 9|   
Dremio|   
Dremio 11+|   
Dremio 26+ with Arrow Flight SQL|   
Exasol|   
Google BigQuery Legacy SQL|   
Google BigQuery Standard SQL|   
Google Cloud AlloyDB for PostgreSQL|   
Google Cloud PostgreSQL|   
Google Cloud SQL|   
Google Spanner|   
Greenplum|   
HyperSQL|   
IBM Netezza|   
MariaDB|   
Microsoft Azure PostgreSQL|   
Microsoft Azure SQL Database|   
Microsoft Azure Synapse Analytics|   
Microsoft SQL Server 2008+|   
Microsoft SQL Server 2012+|   
Microsoft SQL Server 2016|   
Microsoft SQL Server 2017+|   
MongoBI|   
MongoSQL|   
MySQL|   
MySQL 8.0.12+|   
Oracle|   
Oracle ADWC|   
PostgreSQL 9.5+|   
PostgreSQL pre-9.5|   
PrestoDB|   
PrestoSQL|   
SAP HANA|   
SAP HANA 2+|   
SingleStore|   
SingleStore 7+|   
Snowflake|   
Teradata|   
Trino|   
Vector|   
Vertica|   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
