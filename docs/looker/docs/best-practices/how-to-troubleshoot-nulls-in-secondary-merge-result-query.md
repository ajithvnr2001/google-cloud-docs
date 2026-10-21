---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-nulls-in-secondary-merge-result-query/
title: Why are there nulls in my secondary merged results query? \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:21:48.897257+00:00
---

# Why are there nulls in my secondary merged results query?  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-nulls-in-secondary-merge-result-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Why are there nulls in my secondary merged results query? Stay organized with collections  Save and categorize content based on your preferences. 

[Merged Results](https://docs.cloud.google.com/looker/docs/merged-results) is a convenient feature for combining data from different Explores quickly and without developing in LookML. Merged results effectively perform a left join between the primary query and secondary queries — meaning that field names, matching values, and the ending results table are dependent upon how data from the secondary queries match to the primary. 

This can potentially cause unexpected results when you are performing merges between Explores. The merged results documentation addresses a few of these conditions,such as: 

  * When [one query doesn't have a matching data value](https://docs.cloud.google.com/looker/docs/merged-results#what_if_one_query_doesnt_have_a_matching_data_value)
  * When [one query has multiple rows for the same value](https://docs.cloud.google.com/looker/docs/merged-results#what_if_one_query_has_multiple_rows_for_the_same_value)



However, what do you do when you expect a value from a secondary query to match a value in the primary query, but the end result displays null values? 

This page addresses how to troubleshoot this unexpected result. 

## Example use case

The following example use case is based on a sample e-commerce dataset that contains user and order information. For this example, you want to merge one query — a count of users per city (**Users Count** grouped by **Users City**) — with a secondary query — a count of orders (**Orders Count**) grouped by **Users City** and **Users State** : 

**Primary query**

The primary query is **Users Count** grouped by **Users City** : 

![Explore merged results data table showing the primary query results.](https://docs.cloud.google.com/static/looker/docs/images/hc-merge-result-nulls-primary-query-2210.png)

**Secondary query**

The secondary query is **Orders Count** grouped by **Users City** and **Users State** : 

![Explore merged results data table showing the secondary query results.](https://docs.cloud.google.com/static/looker/docs/images/hc-merge-result-nulls-secondary-query-2210.png)

The merge rule is set to merge both queries by **Users City** , the field both queries have in common. Given familiarity with the dataset and expected merged results behavior explained by the documentation linked previously, you know thatin each row, every city should be matched with a state and a count of users. You are expecting that your merged results will match all values and display no null values. 

However, there _are_ nulls in the results. Over half of the cities are not matched with a state or a count of orders: 

![Merged results data table showing null values for secondary query fields.](https://docs.cloud.google.com/static/looker/docs/images/hc-merge-result-nulls-in-query-2210.png)

## Solutions

**Don't panic.** If you are certain there are matching values in your data (try running a separate query to confirm that this is the case), there are several possible solutions to remedy this outcome, including: 

  * Sort each source query the same way. 
  * Increase the source query row limit. 



### Sort each source query the same way

Because merged results are based on Explores, which are [limited](https://docs.cloud.google.com/looker/docs/best-practices/row-limits-in-looker) to 500 rows by default, sometimes the query results you are merging are not included in the final result. 

To fix this, you can [edit](https://docs.cloud.google.com/looker/docs/merged-results#editing_the_source_queries) and [sort](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#sorting_data) your individual source queries to better match each other. 

In the example use case, the primary query is sorted by **Users City** ascending. The secondary query is not. To better match the results of the two queries, you can **sort** the secondary query the same way as the primary query — in this case, by **Users City** ascending. 

Sorting the secondary query similarly to the primary query matches the results more accurately in the final merge: 

![Merged results data table displaying non-null values for primary and secondary query fields.](https://docs.cloud.google.com/static/looker/docs/images/hc-merge-result-sort-same-way-result-2210.png)

### Increase the source query row limit

Similarly to the first solution outlined previously, unexpected nulls can be caused by the [row limits](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#row_limits) set in the source queries. Specifically in this case, the secondary query (limited by the 500 row default) does not have enough rows to match all of the rows generated by primary query, causing null results to be displayed in the final merge. 

To increase the number of rows in the secondary query to match the primary query, you can increase the secondary query row limit. This results in more possible rows to match to the primary query and fewer null values in the secondary query columns: 

![Merged results data table displaying non-null values for primary and secondary query fields.](https://docs.cloud.google.com/static/looker/docs/images/hc-merge-result-increase-limit-result-2210.png)

## Summary

When faced with unexpected merged results, you can take the following steps to troubleshoot: 

  1. Select the [**Clear Cache and Refresh**](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#forcing_new_results_to_be_generated_from_the_database) option from the Explore's gear menu to ensure the query is pulling the most up-to-date results. 
  2. Confirm that there are matching values between source queries where nulls are displayed, as outlined in the [What if one query doesn't have a matching data value?](https://docs.cloud.google.com/looker/docs/merged-results#what_if_one_query_doesnt_have_a_matching_data_value) section of the Merged Results documentation. 
  3. Sort the source queries to better match each other. 
  4. Increase the row limit of source queries beyond the default to expose more rows that can be matched and merged. 
  5. If none of the solutions discussed here resolves the behavior, hardcode the [join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) logic into LookML for a more precise result, if possible. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
