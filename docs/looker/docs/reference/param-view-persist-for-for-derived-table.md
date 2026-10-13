---
url: https://docs.cloud.google.com/looker/docs/reference/param-view-persist-for-for-derived-table/
title: persist_for (for derived tables) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:31.484103+00:00
---

# persist_for (for derived tables)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-view-persist-for-for-derived-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  persist_for (for derived tables) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `persist_for` parameter that is part of a [derived_table](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table).
> 
> `persist_for` can also be used as part of an Explore, described on the [`persist_for` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-for) parameter documentation page.
> 
> `persist_for` can also be used as part of a model, described on the [`persist_for` (for models)](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-for) parameter documentation page.

## Usage
    
    
    view: my_view {
      derived_table: {
        persist_for: "24 hours"
        ...
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [`derived_table`](https://docs.cloud.google.com/looker/docs/reference/param-view-derived-table) `persist_for` |  Default Value None Accepts A string containing an integer followed by a timeframe (seconds, minutes, or hours)   
---|---  
  
## Definition

> Consider instead using a [`datagroup` parameter](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) and [`datagroup_trigger` parameter](https://docs.cloud.google.com/looker/docs/reference/param-view-datagroup-trigger), described in the documentation on [caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#using_a_datagroup_for_a_pdt).

`persist_for` lets you set the maximum amount of time that a [persistent derived table](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_\(pdts\)) may be used before it is regenerated. When a user runs a query that relies on a `persist_for` derived table, Looker checks the age of the table against `persist_for`. If the age is greater than the `persist_for` setting, the derived table is regenerated before the query is run. If the age is less than the `persist_for` setting, the existing derived table is used.

`persist_for` for a PDT runs independently of `persist_for` parameters for [models](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-for) and [Explores](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-for).

If your admin has given you [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission, you can force a derived table to regenerate before its `persist_for` age has been reached. Select the **Rebuild Derived Tables & Run** option from the **Explore actions** gear drop-down menu.

See the [Derived tables in Looker](https://docs.cloud.google.com/looker/docs/derived-tables#manually_rebuilding_persistent_tables_for_a_query) documentation page for further details about the **Rebuild Derived Tables & Run** option.

## Examples

Regenerate the derived table if it is older than 1 hour
    
    
    persist_for: "1 hour"
    

Regenerate the derived table if it is older than 1.5 hours
    
    
    persist_for: "90 minutes"
    

Regenerate the derived table if it is older than 1 day
    
    
    persist_for: "24 hours"
    

## Things to consider

### `persist_for` requires that you have enabled persistent derived tables

`persist_for` will have no effect unless you have [enabled persistence for derived tables](https://docs.cloud.google.com/looker/docs/dialects) on your Looker instance. Most customers do set up persistent derived tables when they initially configure Looker. The most common exception to this rule is for customers that connect Looker to a PostgreSQL read-only, hot-swap replica database.

### `persist_for` works differently between Development Mode and Production Mode

`persist_for` should work as expected in Production Mode. In Development Mode all derived tables are persisted for a maximum of 24 hours, even if you set `persist_for` to a longer value.

See the [Persisted tables in Development Mode](https://docs.cloud.google.com/looker/docs/derived-tables#persisted_tables_in_development_mode) section of the [Derived tables in Looker](https://docs.cloud.google.com/looker/docs/derived-tables) documentation page for more information.

### Alternatives to `persist_for`

Once the `persist_for` timeframe expires, Looker does not automatically regenerate a new derived table. Rather, the table is dropped, and a new derived table will be generated the next time a user queries it. Instead of waiting for a user query to trigger the generation of a derived table, you can schedule the automatic regeneration of a derived table using [`sql_trigger_value`](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-trigger-value).

### Difference between `datagroup` and `max_cache_age`

Using the [`datagroup`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) parameter with a [`datagroup_trigger`](https://docs.cloud.google.com/looker/docs/reference/param-view-datagroup-trigger) parameter gives you more flexibility in triggering your PDT rebuild. However, the [`max_cache_age`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup#max_cache_age) parameter only invalidates the cache; it does not cause PDTs to expire. Use `persist_for` with a derived table if you want to set a maximum time period before dropping a PDT from the scratch schema.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
