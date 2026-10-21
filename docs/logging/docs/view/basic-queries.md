---
url: https://docs.cloud.google.com/logging/docs/view/basic-queries/
title: Build and save queries by using the Logging query language \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:25:44.307781+00:00
---

# Build and save queries by using the Logging query language  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/view/basic-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Build and save queries by using the Logging query language Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to retrieve and analyze logs when you use the Logs Explorer by writing queries in the query-editor field and by selecting from predefined filter options. The queries you build are written in the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

You can also save your queries in the Logs Explorer page, or by using the Logging API method [`savedQueries.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/create).

## Before you begin

The Logs Viewer role (`roles/logging.viewer`) provides access to view logs. For example, when granted this role, you can write and run queries. You can also save queries as private queries, and run both private and shared queries. However, this role doesn't let you save or modify shared queries. If you want to save or modify shared queries, then ensure that you have been granted the Logging Admin role (`roles/logging.admin`), which provides full access to Cloud Logging.

Do one of the following:

  * To get the permissions that you need to write and run queries, to run and save private queries, and to run shared queries, ask your administrator to grant you the [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) IAM role on your project. 




  * To get the permissions that you need to write and run queries, to run and save private queries, and to run, create, and manage shared queries, ask your administrator to grant you the [Logging Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.admin) (`roles/logging.admin`) IAM role on your project. 




For more information about the necessary IAM permissions, see [Permissions for the Google Cloud console](https://docs.cloud.google.com/logging/docs/access-control#console_permissions).

## Build queries

To build queries by using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select the Google Cloud project or other Google Cloud resource for which you want to view logs.

  3. Use the **Query** pane to build your query.

The **Query** pane provides multiple ways to build and run query expressions:

     * Search for text across all log fields.
     * Select options from filter menus.
     * Write or modify queries by using the query editor.
     * View and run saved, recent, and suggested queries from the _menu_book_ **Query library**.



## Search for text across log fields

To search for text across all log fields and find all matching log entries, in the toolbar of the query pane, enter your search terms in the _search_ **Search all fields** field. The search terms you enter in this field are converted into a Logging query language expression.

You can search for words and phrases, and your search terms can include Boolean operators and [regular expressions](https://docs.cloud.google.com/logging/docs/view/logging-query-language#regular-expressions):

  * To perform a case-sensitive search, you must use a [regular expression](https://docs.cloud.google.com/logging/docs/view/logging-query-language#regular-expressions).

  * To perform a case-insensitive search along token boundaries, enter the search terms without backticks or double quotes.

For example, to search for log entries that contain the word `hello` and the word `world`, enter `hello world`. This command, which is converted to `SEARCH("hello world")`, matches log entries that contain the tokens `hello` and `world`, in any order. Because the search is case-insensitive, the search also matches a log entry that contains the tokens `Hello` and `World`. The search doesn't match the token `worlds`.

  * To perform a case-insensitive search for a phrase along token boundaries, wrap the phrase in backticks.

For example, to search for the phrase `hello world`, enter ``hello world``. This command, which is converted to `SEARCH("`hello world`")`, matches log entries that contain the token `hello world`. The search doesn't match the token `hello worlds`.

  * To perform a case-insensitive search for a substring, wrap the text in double quotes. For example, `"hello world"` matches `Hello World` and `Hello world`. The same query also matches `hello worlds`, because the search isn't performed along token boundaries.

**Note:** Substring searches are slower than token-based searches. Therefore, we recommend that you use token-based searches when possible.



To see your search terms within the query expression, enable **Show query**.

After you enter your search terms, click **Run query** or press the **Enter** key. The results of the query are displayed in the **Query results** pane.

### Boolean operators and the search field

The _search_ **Search all fields** field supports the usage of the Boolean operators `AND`, `OR`, and `NOT`. If you use Boolean operators, then do the following:

  * Capitalize Boolean operators. Lowercase `and`, `or`, and `not` are parsed as search terms, not as operators.

  * Don't use parentheses to nest rules. The search terms are parsed according to precedence rules. Parentheses are parsed like any other character.




If you don't include any operators, all search terms and phrases are joined by `AND`. That is, you can omit the `AND` operator between search terms.

#### Examples

Suppose you enter `request AND localhost OR client` into the _search_ **Search all fields** field. Due to the precedence rules, the search terms are converted into the following query:
    
    
    SEARCH("`request`")
    SEARCH("`localhost`") OR SEARCH("client")
    

Next, suppose that you want to list log entries that contain the string `client` or that contain both `request` and `localhost`. You can't use the _search_ **Search all fields** field to generate a query that matches your goal. When your search terms contain both an `AND` and an `OR` statement, the precedence rules specify that the `OR` operation is always performed first. Parentheses aren't treated as special characters when they are included in search terms.

However, you can use the **Query** pane and enter a query. In the **Query** pane, you can use parentheses to specify order in which commands are processed. For example, the following query satisfies your goal:
    
    
    (SEARCH("`request`") AND SEARCH("`localhost`")) OR SEARCH("`client`")
    

#### Operator precedence

The `AND` and `OR` operators are [short-circuit operators](https://en.wikipedia.org/wiki/Short-circuit_evaluation). You can combine`AND` and `OR` rules in the same expression. For example, when the two operators are mixed, the expression `a AND b OR c AND d` turns into the following Logging query language expression:
    
    
    "a"
    "b" OR "c"
    "d"
    

The `NOT` operator has the highest precedence, followed by `OR` and `AND` in that order.

The `NOT` operator performs a negation of the subsequent term. For example, `NOT error` returns log entries that don't contain `error`. You can also replace the `NOT` operator with the `-` (minus) operator. For example, the following two queries are the same:
    
    
    "response" AND "successful" AND NOT "error"
    
    
    
    "response successful" -"error"
    

This logic also works with a phrase, if the `-` (minus) operator is outside the quotation marks. For example, the following two queries are the same:
    
    
    -"response successful"
    
    
    
    NOT "response successful"
    

## Construct queries with filter menus

You can use the filter menus in the **Query** pane to add resource, log name, log severity, and correlation parameters to the query-editor field. These options correspond to the [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) fields for all logs in Logging.

The options in the **Resource** and **Log name** menus are derived from the log entries that are stored by Cloud Logging.

  * **Resource** : Lets you specify the [resource.type](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) and associated `resource.labels`. You can select a single resource type using this filter menu, and zero or more resource labels to apply to your query. The resource parameters are joined by the logical operator `AND`.
  * **Log name** : Lets you specify the [logName](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). You can select multiple log names to apply to your query. When selecting multiple log names, the logical operator `OR` is used.
  * **Severity** : Lets you specify the [severity](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity). You can select multiple severity levels at the same time to add to apply to your query. When selecting multiple severity levels, the logical operator `OR` is used.
  * **Correlate by** : Lets you group and view log entries in a "parent-child" format. For more information, see [Correlate log entries](https://docs.cloud.google.com/logging/docs/view/correlate-logs).



To use any of the filter menus, do the following:

  1. Expand the _arrow_drop_down_ **Menu** on any of the filter menus in the **Query** pane.

  2. Refine the filter parameters.

  3. Click **Apply**. You see the parameters in the query-editor field.

To see your search terms within the query expression, enable **Show query**.

  4. After you review the query, click **Run query**. The results of the query are displayed in the **Query results** pane.




For certain Compute Engine resource types, such as `gce_instance` and `gce_network`, you see the resource name with the resource ID as subtext. For example, for the `gce_instance` resource type, you see the VM name alongside the VM ID. The resource names help you identify the correct resource ID, on which you can build queries.

## View logs by time range

There are two ways to display logs that were written in a specific time range:

  1. Use the time-range selector.
  2. Include a timestamp expression in the query-editor field.



### Use the time-range selector

The options in the time-range selector let you select from preset time options, specify a custom start and end time, or center the time range around a specific timestamp. For example, if you want to view the data for the past week, then select **Last 1 week** from the time-range selector.

You can also set your time zone preferences by using the time-range selector.

### Include a timestamp expression in the query-editor field

To add a timestamp expression directly to the query-editor field, use the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language).

If the query-editor field contains an expression with a timestamp, then the time-range selector is disabled, and the query uses the timestamp expression as its time-range restriction. If a query doesn't use a timestamp expression, then the query uses the time-range selector as its time-range restriction.

## Write advanced queries using the Logging query language

You can use the [Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) to build more advanced queries in the Logs Explorer query-editor field:

  1. If you don't see the query-editor field in the **Query** pane, enable **Show query**.

  2. Enter your query expressions directly into the query-editor field.

If you added any search terms in the search field or selected any parameters in the filter menus, then those also appear in the query-editor field and are evaluated as part of your query expression.

  3. After you review your query, click **Run query**.

Logs that match your query are listed under the [**Query results**](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#query-results) pane. The [**Histogram**](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#histogram-panel) and [**Log fields**](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#logs-field-panel) panes also adjust according to the query expression.




For examples of common queries you might want to use, see [Sample queries using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/query-library-preview).

**Note:** The length of a query can't exceed 20,000 characters.

## Use recent queries

When you run any query, the query is added to the _menu_book_ **Query library** , which contains the last 10,000 unique queries over a 30-day period.

To view your recent queries, select the _menu_book_ **Query library** button in the primary toolbar. For recent queries, you have the following options:

  * **Stream** : To run the query and [stream](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) the results, choose this option.
  * **Run** : To run the query, choose this option.
  * _more_vert_ **More options** : Lets you view the query expression with the options to run the query or save it to your list of **Saved** queries. You can also select the query directly to get these options.

To save the query, do the following:

    1. Click **Save**. The **Save query** dialog opens.
    2. Complete the following fields:

       * **Name** (Required): Provide a name for your query. Names are limited to 64 characters.
       * **Description** (Optional): Provide a description to help identify the purpose of the query.
       * **Include summary fields** (Optional): Enable **Include summary fields** and enter the [summary fields](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#add_summary_fields) that you want to display.
       * **Truncate summary fields** (Optional): Enable **Truncate summary fields** and select the number of characters to truncate to and whether truncation occurs at the beginning or end of the fields.
    3. Click **Save query**. The query is now available in your Saved queries list.




You can also sort and filter your recent queries; the filter matches on the text in your query expression.

## Save and share queries

**Note:** If your data is managed through an [Assured Workloads environment](https://docs.cloud.google.com/assured-workloads/docs/key-concepts), then this feature might be impacted or restricted. For information, see [Restrictions and limitations in Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/eu-sovereign-controls-restrictions-limitations#features_logging).

Saved queries let you store query expressions to help you explore your logs more consistently and efficiently. The Logs Explorer features a **Query library** , where you can access your saved queries. You can also save your queries by using the Logging API method [`savedQueries.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/create).

You can save your query so that it is private and visible only to you, or you can share it with other members of the Google Cloud project. Once you share a query, the query is no longer owned by you, and any member in the project with the necessary permissions can access the query.

###  Console 

To save a query expression that you've built in the query-editor field, do the following:

  1. Click **Save** in the **Query** pane. The **Save query** dialog opens, with your query expression in the query-editor field.

  2. Complete the following fields:

     * **Name** (Required): Provide a name for your query. Names are limited to 64 characters.
     * **Description** (Optional): Provide a description to help identify the purpose of the query.
     * **Include custom summary fields** (Optional): Enable **Include summary fields** and enter the [summary fields](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface#add_summary_fields) that you want to display.
     * **Truncate summary fields** (Optional): Enable **Truncate summary fields** and select the number of characters to truncate to and whether truncation occurs at the beginning or end of the fields.
     * **Share with project** : Optionally, enable **Share with project** to share your query with other members of the Google Cloud project.
  3. Click **Save query**. Your saved queries appear in a list under the **Saved** tab.




To run a saved query, click **Run**. To run the query and [stream](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) the results, click **Stream**.

To modify a saved query, select _more_vert_ **More options** , and then select _edit_ **Edit**. You can also select the query, make modifications, and then save the modified query.

To delete a saved query, select _more_vert_ **More options** , and then select delete **Delete**.

You can also sort and filter your saved queries; the filter matches the text in your query expression.

###  API 

To save a query by using the Logging API, use the `savedQueries.create` method. For more information about this method, its parameters, and the response data, see the reference page for [`savedQueries.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/create).

You can execute the `savedQueries.create` method by using the [APIs Explorer](https://docs.cloud.google.com/logging/docs/api) widget on the method's reference page. For Logs Explorer queries, you must specify the `loggingQuery` field. The following example illustrates a sample request body, which contains an instance of `SavedQuery`:
    
    
    {
      "parent": "projects/my-project/locations/global"
      "savedQueryId": "compute-query"
      {
        "displayName": "compute-admin-activity-query",
        "description": "Queries for Compute Engine Admin Activity logs.",
    
        "loggingQuery":
          {
            "filter": resource.type="gce_instance" AND log_id("cloudaudit.googleapis.com/activity"),
          },
        "visibility": "PRIVATE"
      }
    }
    

To share the query with other members of the Google Cloud project, specify a value of `SHARED` in the `visibility` field.

### View saved queries

You can view both private queries and queries that are shared with other members in the Google Cloud project by clicking the _menu_book_ **Query library** button:

###  Console 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select the Google Cloud project or other Google Cloud resource for which you want to view logs.

  3. Click the _menu_book_ **Query library** button, and click **Saved**.




You can sort the table by any header. The **Visibility** column indicates if the queries are shared or private:

  * **Shared** : Queries that are shared with other members of the Google Cloud project.
  * **Private** : Queries that you have saved and are only visible to you.



###  API 

You can use the Logging API to view private and shared queries by using the [`savedQueries.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/list) method.

For example, the following request body lists all shared Logs Explorer queries with a wildcard location ID:
    
    
    {
      "parent": "name": projects/PROJECT_ID/locations/-
      "visibility": "SHARED"
      "filter": "explorer"
    }
    

## Use suggested queries

Logging generates suggested queries based on the context of your Google Cloud project, such as the Google Cloud products you're using. Suggested queries can help you identify issues and provide you with insights into the overall health of your systems. For example, detecting that you're using Google Kubernetes Engine, Logging might suggest a query that finds all the error logs for your containers.

To view and run suggested queries, click the _menu_book_ **Query library** button and click **Suggested**. In the **Suggested** tab, you have the following options:

  * **Stream** : To run the query and [stream](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) the results, choose this option.
  * **Run** : To run the query, choose this option.
  * _more_vert_ **More options** : Lets you view the details of the query expression with the options to run the query or save it. You can also select the query directly to get these options.

To review the details of a suggested query, do either of the following:

    * Select the query's row.

    * Click _more_vert_ **More** and select **View**. The **Query details** dialog opens.

In the **Query details** dialog, you see the query and the options to **Run** , **Stream** or **Save as** :

    * To save the query, do the following:

      1. Click **Save query**.
      2. Complete the fields in the **Save query** dialog.

The edited query shows up in your **Saved** list, where you can choose to run the query later.

    * To run the query now, click **Run**. The query runs and appears in the query-editor field.

    * To run the query now and [stream](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) the results, click **Stream**.

    * To close the dialog and return to the suggested queries list, click **Close**.




Note the following expected behaviors:

  * Successive page loads might not show the same queries in the same order.
  * You might see zero suggested queries.
  * Sometimes running a suggested query returns zero logs.



## Select queries from the library

Logging provides a library of queries based on common use cases and Google Cloud products. These queries can help you efficiently find logs during time-critical troubleshooting sessions and explore your logs to better understand what Logging data is available.

To view and run the library's queries, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select the Google Cloud project or other Google Cloud resource for which you want to view logs.

  3. Click the _menu_book_ **Query library** button. You see categories of available queries and subsets of queries based on Google Cloud products. To narrow the selection of queries that you see, click any of the products.

You can also use the search field to search the available queries by category, description, or the contents of the query expression.

  4. To review a query expression, do either of the following:

a. Click the query's row.

b. Click _more_vert_ **More** and select **View**.

  5. In the **Query details** dialog, you see the query and the options to **Run** , **Stream** or **Save as** :

     * To save the query, do the following:

       1. Click **Save query**.
       2. Complete the fields in the **Save query** dialog.

The edited query shows up in your **Saved** list, where you can choose to run the query later.

     * To run the query now, click **Run**. The query runs and appears in the query-editor field.

     * To run the query now and [stream](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) the results, click **Stream**.

     * To close the dialog and return to the suggested queries list, click **Close**.




## What's next

  * [Sample queries](https://docs.cloud.google.com/logging/docs/view/query-library)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
