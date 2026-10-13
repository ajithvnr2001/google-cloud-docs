---
url: https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-for/
title: persist_for (for Explores) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:23.921553+00:00
---

# persist_for (for Explores)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-for/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  persist_for (for Explores) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `persist_for` parameter that is part of an [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore).
> 
> `persist_for` can also be used as part of a model, described on the [`persist_for` (for models)](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-for) parameter documentation page.
> 
> `persist_for` can also be used as part of a derived table, described on the [`persist_for` (for derived tables)](https://docs.cloud.google.com/looker/docs/reference/param-view-persist-for-for-derived-table) parameter documentation page.

## Usage
    
    
    
    explore: explore_name {
      persist_for: "1 hour"
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) `persist_for` |  Default Value The `persist_for` setting of the model Accepts A string containing an integer followed by a timeframe (seconds, minutes, or hours) Special Rules A `persist_for` setting at the `explore` level will override the `persist_for` setting at the model level   
---|---  
  
## Definition

> For more robust cache management, including synchronizing your Looker cache policy to your database's ETL (extract, transform, and load) process, consider using a [`datagroup`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) and [`persist_with`](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-with), as described on the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page.

`persist_for` lets you modify the amount of time that cached query results are used for a given Explore. The default cache length in Looker is 1 hour. Cache results are stored in an encrypted file on your Looker instance.

The caching mechanism in Looker works as follows: Once a user runs a specific query, the result of that query is cached. If precisely the same query (_everything_ must be the same, including things such as the row limits, etc.) is run again, in less than the interval specified by `persist_for`, the cached results are returned. Otherwise, a new query is run against your database.

When the `persist_for` interval expires, data is deleted from the cache. See the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page for information on how long data is stored in the cache.

If `persist_for` is set for both an Explore and [its model](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-for), the value set for the Explore will take priority for queries based on that Explore.

> From an Explore, you can [see whether a query was returned from cache](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#seeing_whether_a_query_was_returned_from_cache) or you can [force new results to be generated from the database](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#forcing_new_results_to_be_generated_from_the_database). See the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page for more information.

## Examples

Adjust the cache length to 2 hours:
    
    
    explore: my_explore {
      persist_for: "2 hours"
    }
    

Adjust the cache length to 30 minutes:
    
    
    explore: my_explore {
      persist_for: "30 minutes"
    }
    

Turn off caching so that users never get cached results for a query:
    
    
    explore: my_explore {
      persist_for: "0 seconds"
    }
    

## Things to consider

When `persist_for` is set to `0 seconds`, your users' queries will not retrieve data from the cache. However, Looker requires the disk cache for internal processes, so your encrypted data will always be written to the cache, even when `persist_for` is set to `0 seconds`. Once written to the cache, the data will be flagged for deletion but may live up to 10 minutes on disk. See the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#data_delete) documentation page for details.

### `persist_for` does not necessarily align with your data import

Many companies have a daily data import to their analytics database. Sometimes, they reason that there is no purpose running fresh queries if the data isn't constantly updated anyway, so they set the cache length to 24 hours (like `persist_for: 24 hours`). However, this will not prevent users from getting data that is older than the most recent refresh.

For example, a query is run at noon on January 1st, new data is imported the morning of January 2nd, and then the query is run again at noon on January 2nd. Since the query was run within the 24 hour window specified by `persist_for`, the data from January 1st will be returned, even though new data was loaded on January 2nd.

> If you want your caching to be aligned with data imports, use a [datagroup](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) and [`persist_with`](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-with), as described in the documentation on [caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters).

### Scheduled Looks will cache results

When a scheduled Look is run, it creates a cached result set in the same way that a user run query would. To precache a certain Look, consider saving and [scheduling](https://docs.cloud.google.com/looker/docs/scheduling) it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
