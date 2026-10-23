---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-filter-suggestion-issues/
title: Troubleshooting common filter suggestion issues \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:24.225645+00:00
---

# Troubleshooting common filter suggestion issues  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-filter-suggestion-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting common filter suggestion issues Stay organized with collections  Save and categorize content based on your preferences. 

[Filter suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions#default_behavior) are a powerful tool in Looker. It's crucial to understand where they come from and how they work so that you can troubleshoot effectively when filter suggestions don't behave as expected. This page addresses how filter suggestions work, why they may be wrong, and why they may fail to populate. 

## How do filter suggestions work?

Filter suggestions save time when users input values in filters and ensure that users choose options that exist in the data. When users select a filter box, a list of suggestions appears below the field. In this example, selecting the box for a filter on the field **Status** from the **Orders** Explore reveals a drop-down list with the values "cancelled", "complete", and "pending" as options. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-filter-suggestion-example.png)

### Where does this list of suggestions come from?

Looker runs a `SELECT distinct <field>` query against the database to retrieve all possible options for that field. The query looks similar to the following SQL: 
    
    
    SELECT DISTINCT <field_name>
    FROM <table>
    WHERE (<field_name> LIKE '%' OR <field_name> LIKE '% %')
    GROUP BY 1
    ORDER BY 1
    LIMIT 1000
    

When users enter characters in the filter box, Looker substitutes the appropriate conditions in the `WHERE` clause to filter the results. Looker then shows the first 1000 of those results in filter suggestions. 

### Can I change what suggestions are populated?

Developers can use various LookML parameters to change and customize the suggestions that appear. See the [Changing filter suggestions](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions) documentation page for more details. 

### Are suggestions cached?

By default, Looker caches query results for one hour. You can use the [`suggest_persist_for`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-persist-for) LookML parameter to customize the cache length for filter suggestions. The `suggest_persist_for` parameter has a default value of "6 hours". Suggestions have their own cache, which cannot be cleared manually from an Explore page. If you need to clear cache for suggestions, here are some options: 

  * If the Explore is cached using a [datagroup](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup) with a `sql_trigger`, you can manually [reset the cache for the entire datagroup](https://docs.cloud.google.com/looker/docs/admin-panel-database-datagroups#datagroup_actions) in the [**Datagroups**](https://docs.cloud.google.com/looker/docs/admin-panel-database-datagroups) page in the Looker **Admin** panel, but this will refresh the cache for all queries that are persisted using that datagroup.
  * You can use the `suggest_persist_for` parameter at the field level and set it to "0 seconds" to bust the filter suggestion cache for that field. 

> _Cache is global for all users. One user refreshing cache for suggestions will affect the results other users see._




## Why are the filter suggestions wrong?

Now that you understand how filter suggestions are populated, you can determine why filter suggestions may be wrong. The most common explanation is that the data has changed or updated between the time the filter suggestions were cached and the time the wrong results were noticed. 

As an example, suppose User A runs an Explore first thing in the morning. User A selects some filter values from the suggestion drop-down list. The database's ETL process finishes a half hour or so later. Then, User B views the same Explore that User A previously ran. User B wonders why the filter suggestions are incorrect. The reason for the disparity is that the cached suggestion query did not update with the database's newly completed ETL process and therefore showed unexpected results. 

If this is the case, you can refresh the suggestions cache using the methods described in the Are suggestions cached? section earlier on this page. 

## Why are filter suggestions not populating?

There can be several reasons for filter suggestions not populating. The following troubleshooting steps highlight potential causes: 

  1. Check the filter type.
  2. Check if there is an `access_filter` or a `sql_always_where` restricting suggestions.
  3. Check if there is a `suggest_dimension parameter`.
  4. Check if there is an attempt to load suggestions when a user selects or enters text in the filter.
  5. Check the Chrome network console.
  6. Find evidence of the suggestions query that Looker is trying to run.



### Check the filter type

If this is for a [LookML dashboard](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#type) filter, make sure the filter type is **Field**. Other filter types will not populate suggestions. 

  * Make sure the filter field is of [`type: string`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#string) in its LookML definition. Filters on [`number`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#number) type fields will not populate suggestions. 
  * Is it a [matches (advanced)](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#advanced_matches_filters) filter? Matches (advanced) filters require [ Looker expressions](https://docs.cloud.google.com/looker/docs/filter-expressions), so suggestions will not populate. 



### Check if there is an `access_filter` or a `sql_always_where` restricting suggestions

Typically, when [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) or [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter) is used, filter suggestions are restricted for that Explore. This prevents users from seeing a filter suggestion that they cannot access. If you are certain that there are no possible values in a particular [dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) or [filter](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) field that would reveal sensitive information, you can use [`bypass_suggest_restrictions`](https://docs.cloud.google.com/looker/docs/reference/param-field-bypass-suggest-restrictions) to re-enable filter suggestions. 

### Check if there is a `suggest_dimension parameter`

When the [`suggest_dimension`](https://docs.cloud.google.com/looker/docs/changing-filter-suggestions#suggest_dimension_field_and_suggest_explore_field) parameter is used, the filter suggestions will not populate unless the suggested dimension is being referenced in an Explore with that dimension's view defined as the Explore's [base](https://docs.cloud.google.com/looker/docs/reference/param-explore-join#definition) view. 

For Explores where the suggested dimension's view is not the base view, add the [`suggest_explore`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-explore) parameter, referencing the Explore where that view is the base view. 

### Check if there is an attempt to load suggestions when you select or enter text in the filter

Check whether Looker appears to attempt to load suggestions when you select or enter text in the filter box. Looker should display a spinning loading circle in the right side of the filter box. 

Your browser does not support the embedded video. 

If not, then Looker isn't trying to populate suggestions. Check that the conditions described in the first step are met and that suggestions are not turned off at the [`field`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions), [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-suggestions), or Explore level (with [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) or [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter)) in LookML. Note that Hadoop dialects will add `suggestions: no` on all view files by default. 

If there is an attempt to load suggestions, proceed to the instructions for checking the Chrome network console. 

### Check the Chrome network console

The [Chrome network console](https://developers.google.com/web/tools/chrome-devtools/network) may highlight an error with the query itself or show whether there are results returned from cache. 

  1. Open the Network tab on your browser with the shortcut Ctrl + Shift +J (on Windows) or command + option + J (on Mac), or by selecting **View** > **Develop** > **Developer tools** from the Chrome options bar at the top of the browser.
  2. Select in the filter box on your Look, Explore, or dashboard.
  3. The Developer tools panel should display a request for the filter suggestions, which you can select for more information.
  4. The headers will surface the internal API request that Looker is making to retrieve the suggestion values. In this example, suppose Looker is making the following API request, where `<yourinstance>` represents the URL for your instance: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-filter-suggestions-api-request.png)
         
         <yourinstance>/api/internal/models/the_look/views/order_items/fields/users.state/suggestions?term=

  5. In the API request, check that the model listed after `/models/` exists. In this example, the model is called `the_look`.
  6. Although the URL says `/views/`, this refers to the Explore that the field is coming from. Check that the Explore listed after `/views/` exists. In this example, the Explore is called `order_items`.
  7. Check that the field listed after `/fields/` exists. In this example, the field is `users.state`.



The response for this API request will surface the exact error message. For example, the status code for the suggestions is **404 Not Found** : 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-js-console-404.png)

Select the response for this request for more details. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-suggestions-field-not-found.png)

In this case, you can see that the suggestions are failing because the field can't be found based on the response to the request: 
    
    
    {"class":"FieldNotFound","text":"Field not found."}
    

If there are no errors, but also no suggestions when expected, check to see if the suggestion query is pulling from cache (`cache: true` in the Network Console) — this may suggest that the cache needs to be busted, using a [`suggest_persist_for`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-persist-for) parameter on the dimension that is serving suggestions. 

### Find evidence of the suggestions query that Looker is trying to run

You can check the [**Queries**](https://docs.cloud.google.com/looker/docs/admin-panel-database-queries) page in the Looker **Admin** panel to make sure the query that is generating the filter (the **Source** field on the **Queries** page will say **Filter Suggestion**) is not generating an error. Select the query's [**Details**](https://docs.cloud.google.com/looker/docs/admin-panel-database-queries#the_details_button) button and select the **Open in SQL Runner** option. Verify that the SQL is syntactically correct. If you notice anomalies such as missing field names or errant special characters, check to make sure that you are not using Liquid parameters or templated filters. 

  * If the query requires a [templated filter](https://docs.cloud.google.com/looker/docs/templated-filters) input to run, no filter suggestions will populate.
  * If the query uses a [parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) with a [`default_value`](https://docs.cloud.google.com/looker/docs/reference/param-field-default-value), that value will be inserted in the filter suggestion query. In this scenario, the filter suggestion query will not dynamically update based on the user input. Depending on the default value, this can either cause no filter suggestions or wrong filter suggestions. Instead, consider using [linked filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#setting_up_linked_filters) in a dashboard.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
