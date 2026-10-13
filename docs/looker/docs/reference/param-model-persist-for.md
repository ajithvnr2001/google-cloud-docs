---
url: https://docs.cloud.google.com/looker/docs/reference/param-model-persist-for/
title: persist_for (for models) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:19.448699+00:00
---

# persist_for (for models)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-model-persist-for/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  persist_for (for models) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `persist_for` parameter that is part of a [model](https://docs.cloud.google.com/looker/docs/reference/param-model).
> 
> `persist_for` can also be used as part of an Explore, described on the [`persist_for` (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-for) parameter documentation page.
> 
> `persist_for` can also be used as part of a derived table, described on the [`persist_for` (for derived tables)](https://docs.cloud.google.com/looker/docs/reference/param-view-persist-for-for-derived-table) parameter documentation page.

## Usage
    
    
    
    persist_for: "5 hours"
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) `persist_for` |  Default Value 1 hour Accepts A string containing an integer followed by a timeframe (seconds, minutes, or hours)   
---|---  
  
## Definition

> Consider instead using a [`datagroup`](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) and [`persist_with`](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-with), as described on the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page.

`persist_for` lets you modify the amount of time that cached query results are used for a given [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore). The default cache length in Looker is 1 hour. Cache results are stored in an encrypted file on your Looker instance.

The caching mechanism in Looker works as follows: once a user runs a specific query, the result of that query is cached. If someone runs precisely the same query again (_everything_ must be the same, including minor things such as the row limit) in less than the interval specified by `persist_for`, then the cached results are returned. Otherwise, a new query is run against your database.

When the `persist_for` interval expires, data is deleted from the cache. See the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page for information on how long data is stored in the cache.

Explores also support [`persist_for`](https://docs.cloud.google.com/looker/docs/reference/param-explore-persist-for). When an Explore and its model both have `persist_for` settings, the value set for the Explore will take priority for queries based on that Explore.

> From an Explore, you can [see whether a query was returned from cache](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#seeing_whether_a_query_was_returned_from_cache) or you can [force new results to be generated from the database](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#forcing_new_results_to_be_generated_from_the_database). See the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page for more information.

## Examples

Adjust the cache length to 2 hours:
    
    
    persist_for: "2 hours"
    

Adjust the cache length to 30 minutes:
    
    
    persist_for: "30 minutes"
    

Turn off caching so that users never get cached results for a query:
    
    
    persist_for: "0 seconds"
    

## Things to consider

### Data is always written to the cache

When `persist_for` is set to `0 seconds`, your users' queries will not retrieve data from the cache. However, Looker requires the disk cache for internal processes, so your encrypted data will always be written to the cache, even when `persist_for` is set to `0 seconds`. Once written to the cache, the data will be flagged for deletion but may live up to 10 minutes on disk. See [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page for details.

### `persist_for` does not necessarily align with your data import

Many companies have a daily data import to their analytics database. Sometimes, they reason that there is no purpose running fresh queries if the data isn't constantly updated anyway, so they set the cache length to 24 hours (like `persist_for: 24 hours`). However, this will not prevent users from getting data that is older than the most recent refresh.

For example, suppose a query is run at noon on January 1st, new data is imported the morning of January 2nd, and then the query is run again at noon on January 2nd. Since the query was run within the 24 hour window specified by `persist_for`, the data from January 1st will be returned, even though new data was loaded on January 2nd.

> If you want your caching to be aligned with data imports, use [datagroups](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) and [`persist_with`](https://docs.cloud.google.com/looker/docs/reference/param-model-persist-with), as described on the [Caching queries](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) documentation page.

### Scheduled Looks will cache results

When a scheduled Look is run, it will create a cached result set in the same way that a user run query would. If you want to precache a certain Look, you may want to consider saving and [scheduling](https://docs.cloud.google.com/looker/docs/scheduling) it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
