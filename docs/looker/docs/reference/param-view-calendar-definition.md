---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-calendar-definition/
title: calendar_definition \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:26.767140+00:00
---

# calendar_definition  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-calendar-definition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  calendar_definition Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: retail_custom_calendar {
      calendar_definition: {
        reference_date: ref_date
        timeframe_mapping: {
          custom_date: custom_date
          custom_period: custom_period
          custom_quarter: custom_quarter
          custom_season: custom_season
          custom_week: custom_week
          custom_year: custom_year
        }
        timeframe_ordinal_mapping: {
          custom_date: custom_date
          custom_period: custom_period
          custom_quarter: custom_quarter
          custom_season: custom_season
          custom_week: custom_week
          custom_year: custom_year
        }
        previous_ordinal_mapping: {
          custom_date: custom_date
          custom_week: custom_week
        }
      }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) `calendar_definition`  
---  
  
## Definition

As part of using [custom calendars](https://docs.cloud.google.com/looker/docs/custom-calendars) in Looker, the `calendar_definition` parameter lets you map Looker custom calendar timeframes to the columns of a [custom calendar table that you created in your database](https://docs.cloud.google.com/looker/docs/custom-calendars#database_calendar).

See the [Using custom calendars in Looker](https://docs.cloud.google.com/looker/docs/custom-calendars#define_custom_calendar_view) documentation page for information on setting up a custom calendar view file.

In the view file for your custom calendar, add the `calendar_definition` parameter block. For example:
    
    
      calendar_definition: {
        reference_date: ref_date
        timeframe_mapping: {
          custom_date: custom_date
          custom_period: custom_period
          custom_quarter: custom_quarter
          custom_season: custom_season
          custom_week: custom_week
          custom_year: custom_year
        }
        timeframe_ordinal_mapping: {
          custom_date: ordinal_custom_date
          custom_period: ordinal_custom_period
          custom_quarter: ordinal_custom_quarter
          custom_season: ordinal_custom_season
          custom_week: ordinal_custom_week
          custom_year: ordinal_custom_year
        }
        previous_ordinal_mapping: {
          custom_date: prev_day_num
          custom_week: prev_week_num
        }
      }
    

Note the following about the `calendar_definition` parameter block:

  * The `reference_date` parameter is required.
  * The `timeframe_mapping` and `timeframe_ordinal_mapping` parameters and all of their subparameters are required. See Mandatory timeframes for more information.
  * The `previous_ordinal_mapping` parameter block is used for custom calendars with [period-over-period measures](https://docs.cloud.google.com/looker/docs/period-over-period) to tell Looker how to process the previous week when the current week is 1 and how to process the previous day when the current day is 1. The `previous_ordinal_mapping` parameter is optional starting in Looker 26.8. 



See the Example section on this page.

After modeling the custom calendar table in LookML, you can then create a [dimension group of `type: custom_calendar`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#custom_calendar_type) that is based on the custom calendar view. Your end users can then create Explore queries using the custom calendar dimension timeframes.

### `reference_date`

The `reference_date` parameter specifies a dimension in your custom calendar view that maps to the column in your custom calendar database table that provides a standard calendar date, such as `2026-01-01`.

Note the following about the `reference_date` parameter:

  * The `reference_date` is required, since Looker uses it to calculate joins from your data tables to your custom calendar table to provide query results that use your custom timeframes.
  * The `reference_date` must be unique or a primary key.



Refer to the Example section on this page to see how the `reference_date` points to a dimension that models a column in your custom calendar table. 

### `timeframe_mapping`

The `timeframe_mapping` block maps each Looker custom timeframe to the dimension that models the equivalent column of your custom calendar database table. 
    
    
    timeframe_mapping: {
      custom_date: field-ref
      custom_period: field-ref
      custom_quarter: field-ref
      custom_season: field-ref
      custom_week: field-ref
      custom_year: field-ref
    }
    

**Note:** The `timeframe_mapping` parameter and all its subparameters are required. See Mandatory timeframes for more information.

Refer to the Example section on this page to see how each `timeframe_mapping` subparameter specifies a dimension that models a column in your custom calendar table. 

### `timeframe_ordinal_mapping`

The `timeframe_ordinal_mapping` block maps each Looker custom timeframe to the dimension that models the appropriate ordinal column of your custom calendar database table. 
    
    
    timeframe_ordinal_mapping: {
      custom_date: field-ref
      custom_period: field-ref
      custom_quarter: field-ref
      custom_season: field-ref
      custom_week: field-ref
      custom_year: field-ref
    }
    

**Note:** The `timeframe_ordinal_mapping` parameter and all its subparameters are required. See Mandatory timeframes for more information.

Refer to the Example section on this page to see how each `timeframe_ordinal_mapping` subparameter specifies a dimension that models a column in your custom calendar table.

### `previous_ordinal_mapping`

If you want to create [period-over-period (PoP) measures](https://docs.cloud.google.com/looker/docs/period-over-period#custom_calendar_period) that use your custom calendar, you can also add a `previous_ordinal_mapping` block to your `calendar_definition`. The `previous_ordinal_mapping` block maps the `custom_date` and `custom_week` Looker timeframes to the dimensions that model the columns of your custom calendar database table where the previous day and previous week are specified. 
    
    
    previous_ordinal_mapping: {
      custom_date: field-ref
      custom_week: field-ref
    }
    

  * The `custom_date` parameter tells Looker how to process the previous day when the current day is 1.
  * The `custom_week` parameter tells Looker how to process the previous week when the current week is 1.



The `previous_ordinal_mapping` parameter is optional starting in Looker 26.8. If the `previous_ordinal_mapping` block is omitted, Looker assumes a 52-week year, where the previous value for Week 1 is 52 and the previous value for Day 1 is 364.

### Mandatory timeframes

The timeframes subparameters of `timeframe_mapping` and `timeframe_ordinal_mapping` are required. If a specific timeframe, such as `custom_season`, is not relevant for your custom calendar, you must still include it by defining a placeholder dimension in your calendar view. For example:
    
    
     dimension: season {
        type: string
        sql: 'N/A' ;;
        hidden: yes
      }
      dimension: season_num {
        type: number
        sql: 0 ;;
        hidden: yes
      }
    

## Example

Here is an example view file called `fiscal_calendar.view.lkml` that models a custom calendar table called `fiscal_calendar_table`:
    
    
    view: fiscal_calendar {
      sql_table_name: fiscal_calendar_table ;;
    
      calendar_definition: {
        reference_date: reference_date
    
        timeframe_mapping: {
          custom_year: fiscal_year
          custom_quarter: fiscal_quarter_of_year
          custom_date: fiscal_date_of_month
          custom_week: fiscal_week_of_year
          custom_period: fiscal_period_of_year
          custom_season: season
        }
        timeframe_ordinal_mapping: {
          custom_year: fiscal_year_num
          custom_quarter: fiscal_quarter_of_year_num
          custom_date: fiscal_date_of_month_num
          custom_week: fiscal_week_of_year_num
          custom_period: fiscal_period_of_year_num
          custom_season: season_num
        }
        previous_ordinal_mapping: {
              custom_date: prev_custom_date
              custom_week: prev_custom_week
        }
      }
    
      dimension: reference_date {
        type: date
        primary_key: yes
        sql: ${TABLE}.reference_date ;; # Name of the column in your database table that shows the standard date, such as `2026-01-01`
      }
    
      dimension: fiscal_year {
        type: string
        sql: ${TABLE}.fiscal_year ;;
      }
    
      dimension: fiscal_year_num {
        type: number
        sql: ${TABLE}.fiscal_year_num ;;
      }
    
      dimension: prev_custom_week {
              type: number
              sql: ${TABLE}.prev_custom_week ;;
            }
    
      # ... other dimensions for quarters, weeks, periods, seasons, etc. ...
    
      # Example placeholder dimensions for unused timeframes
      dimension: season {
        type: string
        sql: 'N/A' ;;
        hidden: yes
      }
      dimension: season_num {
        type: number
        sql: 0 ;;
        hidden: yes
      }
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
