---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-fanout-on/
title: fanout_on \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:35.540329+00:00
---

# fanout_on  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-fanout-on/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  fanout_on Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        fanout_on: repeated_record_name
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `fanout_on` |  Possible Field Types Dimension, Dimension Group, Measure Accepts A Google BigQuery Legacy SQL REPEATED subrecord  
---|---  
  
## Definition

The `fanout_on` parameter specifies the Google BigQuery Legacy SQL `REPEATED` subrecord on which a dimension or measure should fanout.

Google BigQuery Legacy SQL supports nested records in which a single record can hold multiple subrecords. Expressing these subrecords in Looker causes the result set to "fanout", which means that the parent record gets repeated multiple times. In order for Looker to properly associate the normal data with the repeated data, you can specify the fanout relationship of a subrecord using the `fanout_on` parameter.

Consider this example data table:

Column Name | Type  
---|---  
name | String, required  
age | Integer, required  
citiesLived | Record, repeated  
citiesLived.place | String, nullable  
citiesLived.numberOfYears | Integer, nullable  
  
Data without the `citiesLived` record may look like this:

name | age  
---|---  
Wilbur Wright | 45  
  
However, adding the repeated `citiesLived` record causes a fanout, where the `name` and `age` data is repeated multiple times:

name | age | citiesLived.place | citiesLived.numberOfYears  
---|---|---|---  
Wilbur Wright | 45 | Dayton | 40  
Wilbur Wright | 45 | Paris | 2  
Wilbur Wright | 45 | Kitty Hawk | 1  
  
When modeling this type of data the `citiesLived` record causes the fanout, so it is used in the `fanout_on` parameter:
    
    
    dimension: city_lived {
      sql: ${TABLE}.citiesLived.place ;;
      fanout_on: "citiesLived"
    }
    dimension: years_lived {
      sql: ${TABLE}.citiesLived.numberOfYears ;;
      fanout_on: "citiesLived"
    }
    measure: cities_count {
      type: count_distinct
      sql: ${city_lived} ;;
      fanout_on: "citiesLived"
    }
    measure: city_list {
      type: list
      list_field: city_lived
      fanout_on: "citiesLived"
    }
    

-

Note that both dimensions and measures must use `fanout_on` if they include a repeated record in their calculation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
