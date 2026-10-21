---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-timeframe-vs-timeframe-analysis-with-templated-filters/
title: Timeframe versus timeframe analysis using templated filters \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:36.745720+00:00
---

# Timeframe versus timeframe analysis using templated filters  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-create-timeframe-vs-timeframe-analysis-with-templated-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Timeframe versus timeframe analysis using templated filters Stay organized with collections  Save and categorize content based on your preferences. 

To compare a metric filtered by several timeframes in the same Look or dashboard, you can use [ filtered measures](https://docs.cloud.google.com/looker/docs/reference/param-field-filters). Filtered measures let you apply a hardcoded filter directly to a measure, rather than applying a filter to an entire query. 

**Note:** For [dialects that support period-over-period measures](https://docs.cloud.google.com/looker/docs/period-over-period#supported_dialects_for_period_over_period), you can create a LookML measure of `type: period_over_period` to create a period-over-period measure. See the [Period-over-period measures in Looker](https://docs.cloud.google.com/looker/docs/period-over-period) documentation page for more information. 

If you had a limited number of timeframes that you were interested in comparing, you could define a few measures with hardcoded timeframe filters (for example, "this year" and "last year") and display them in an Explore, a Look, or a dashboard. You can also take this approach a step further to make timeframe comparisons dynamic — or measures that change with timeframes specified by users in [Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores), [Looks](https://docs.cloud.google.com/looker/docs/viewing-looks), or [dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards) — by using [ templated filters](https://docs.cloud.google.com/looker/docs/templated-filters) in filtered measures. 

##  Pattern overview 

On a high level, this approach involves three components: 

  1. Define a templated filter of `type: date` for each timeframe that will appear as a [filter-only field](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) on your Explore, Look, or dashboard. 
  2. Create a [`yesno`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#yesno) type dimension to tie to the templated filter so that when a user selects a value for the filter-only field, the `yesno` dimension returns "yes" for records that meet the filter's conditions. 
  3. Create a filtered measure that references the `yesno` dimension with the condition `value = "yes"`. This ensures that the measure only aggregates records that meet the timeframe condition that is specified in the filter that is defined in step 1. 



This logic lets users create analyses and visualizations that compare values from different timeframes, like the following Explore: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-timeframe-vs-timeframe-analysis-2210.png)

Users can change the values in the **Timeframe A** and **Timeframe B** filters and only impact the values for **Orders Count A** and **Orders Count B**. **Orders Count A** and **Orders Count B** are measures with filters that reference the timeframe conditions in the timeframe filters. **Timeframe A** impacts the values for **Orders Count A** , and **Timeframe B** impacts the values for **Orders Count B**. 

The following section provides the LookML for this example. 

##  The LookML 

The following LookML assumes that you have a dimension group with a [`raw`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframe_options) timeframe named `created_raw`: 
    
    
      dimension_group: created {
        type: time
        timeframes: [
          raw,
          time,
          date,
        ]
        sql: ${TABLE}.created_at ;;
      }
      

The LookML for comparing count measures — **Orders Count A** and **Orders Count B** — filtered by two dynamic timeframes — **Timeframe A** and **Timeframe B** — based on `created_raw` looks like this: 
    
    
      ## filter determining time range for all "A" measures
      filter: timeframe_a {
        type: date_time
      }
    
    
      ## flag for "A" measures to only include appropriate time range
      dimension: group_a_yesno {
        hidden: yes
        type: yesno
        sql: {% condition timeframe_a %} ${created_raw} {% endcondition %} ;;
      }
    
    
      ## filtered measure A
       measure: count_a {
        type: count
        filters: [group_a_yesno: "yes"]
       }
    
    
      ## filter determining time range for all "B" measures
       filter: timeframe_b {
        type: date_time
       }
    
    
      ## flag for "B" measures to only include appropriate time range
      dimension: group_b_yesno {
        hidden: yes
        type: yesno
        sql: {% condition timeframe_b %} ${created_raw} {% endcondition %} ;;
       }
    
    
       measure: count_b {
        type: count
        filters: [group_b_yesno: "yes"]
       }
    

You can use this logic to create as many timeframe comparisons as you need. 

## Filtering an entire query with dynamic timeframes

Filtered measures do not apply a filter condition to overall query results. If you want to limit the overall query results within the specified timeframes, you can: 

  1. Create the following `yesno` dimension 
  2. Filter the dimension values by "yes" in Explores, Looks, or dashboards: 


    
    
      dimension: is_in_time_a_or_b {
        group_label: "Time Comparison Filters"
        type: yesno
        sql:
          {% condition timeframe_a %} ${created_raw} {% endcondition %} OR
          {% condition timeframe_b %} ${created_raw} {% endcondition %} ;;
      }
    

This prevents the database from scanning more data than needed for the query — and may help with performance and query cost. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
