---
url: https://docs.cloud.google.com/logging/docs/analyze/create-and-manage-analytics-views/
title: Create, query, and manage analytics views \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:25.790136+00:00
---

# Create, query, and manage analytics views  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/analyze/create-and-manage-analytics-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Create, query, and manage analytics views Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Analytics views in Observability Analytics let you define a SQL query with a custom schema over your Cloud Logging data so that you can simplify and reuse complex transformations. After you create an analytics view, you can query its results in the `FROM` clause of other SQL queries, just like you query log views.

For an overview of analytics views, see [About analytics views](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views).

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. To get the permissions that you need to create, manage, and use analytics views, ask your administrator to grant you the following IAM roles on your project: 

     * [Observability Analytics User ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)

You can restrict a principal to a specific log view either by adding an IAM condition to the Logs View Accessor role grant made at the project level, or by adding an IAM binding to the policy file of the log view. For more information, see [Control access to a log view](https://docs.cloud.google.com/logging/docs/logs-views#about-iam-policies).

For information about additional roles that you need to query views on user-defined buckets or to query the `_AllLogs` view of the `_Default` log bucket, see [Cloud Logging roles](https://docs.cloud.google.com/logging/docs/access-control#considerations).

  3. Make sure that you have a log bucket that is upgraded to use Observability Analytics. For information about this step, see [Configure log buckets](https://docs.cloud.google.com/logging/docs/analyze/query-and-view). 



## Create an analytics view

**Note:** An analytics view can query log views. If an analytics view queries multiple views, then those views must be in the same location. For example, if you have two log buckets in the `us-east1` location, then you can create an analytics view that queries log views on those two log buckets. 

To create an analytics view, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Configure the **Observability Analytics** page: 
     1. Make sure that the toolbar displays **Run query**. If the toolbar displays **Run in BigQuery** , then click _settings_ **Settings** and select **Observability Analytics (default)**.
     2. If the **Views** menu isn't shown, then go to the navigation pane and click _last_page_ **Views and Schema**.
  3. Enter and validate the query that you want to save as an analytics view.

You might want to load and edit the default query for the log view that your analytics view will query. To load the default query, do the following:

     1. In the **Views** menu, go to the segment **Logs** section, find and then select the log view that you want to query.

     2. In the **Schema** toolbar, click **Query** , and then click **Overwrite**.

The **Query** pane is updated with a SQL query.

     3. Update the query until you're satisfied with the query results.

  4. Create an analytics view:

     1. In the toolbar, click save **Save** , and then select **Save as analytics view**.

     2. Enter a name and description for the analytics view.

The name is limited to 100 characters and can include only letters, digits, underscores, and hyphens.. You can't change the name after you create the analytics view.

     3. Click **Save**.

The system creates your analytics view and lists it in the **Views** pane, in the data_table **Analytics Views** section.




## Query an analytics view

You query an analytics view in a manner analogous to querying log views. To query analytics views, use the following format for the `FROM` clause:
    
    
    FROM `analytics_view.PROJECT_ID.LOCATION.ANALYTICS_VIEW_ID`
    

The fields in the previous expressions have the following meaning:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The location of the analytics view.
  * ANALYTICS_VIEW_ID: The ID of the analytics view, which is limited to 100 characters and can include only letters, digits, underscores, and hyphens.



To learn more, see [Query and analyze logs overview](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).

## List analytics views

To list the analytics views in your Google Cloud project, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Configure the **Observability Analytics** page: 
     1. Make sure that the toolbar displays **Run query**. If the toolbar displays **Run in BigQuery** , then click _settings_ **Settings** and select **Observability Analytics (default)**.
     2. If the **Views** menu isn't shown, then go to the navigation pane and click _last_page_ **Views and Schema**.
  3. In the **Views** menu, go to the data_table **Analytics Views** section.



## Get details about an analytics view

You can use options in the **Schema** pane to display the following information about an analytics view:

  * Name
  * Create date
  * Last update
  * Schema
  * Query



To view the details for an analytics view, list the analytics views in your project, and then do the following:

  1. Select the analytics view whose information you want to view.
  2. In the **Schema** toolbar, click _more_vert_ **View analytics view options** , and select **View details**.



## Modify an analytics view

To modify an analytics view, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Configure the **Observability Analytics** page: 
     1. Make sure that the toolbar displays **Run query**. If the toolbar displays **Run in BigQuery** , then click _settings_ **Settings** and select **Observability Analytics (default)**.
     2. If the **Views** menu isn't shown, then go to the navigation pane and click _last_page_ **Views and Schema**.
  3. In the **Views** menu, go to the data_table **Analytics Views** section, and select the analytics view that you want to modify.
  4. In the **Schema** toolbar, click _more_vert_ **View analytics view options** , and select **Edit view**.

A dialog opens that displays information about the analytics view. You can modify the description and query.

  5. After you complete your modifications, click **Overwrite saved view**.




## Delete an analytics view

**Note:** If you've written queries against an analytics view and delete the analytics view, then those queries will fail.

To delete an analytics view, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Configure the **Observability Analytics** page: 
     1. Make sure that the toolbar displays **Run query**. If the toolbar displays **Run in BigQuery** , then click _settings_ **Settings** and select **Observability Analytics (default)**.
     2. If the **Views** menu isn't shown, then go to the navigation pane and click _last_page_ **Views and Schema**.
  3. In the **Views** menu, go to the data_table **Analytics Views** section, and select the analytics view that you want to delete.
  4. In the **Schema** toolbar, click _more_vert_ **View analytics view options** , select **Delete view** , and complete the dialog.



## Limitations

The following limitations apply to analytics views:

  * An analytics view can only query log views.
  * The parent resource of an analytics view must be a Google Cloud project.
  * You can only query an analytics view by using the **Observability Analytics** page, and only when you use the **Observability Analytics (default)** query engine.
  * All views that an analytics view queries must be in the same location.
  * You must use the Google Cloud console to create or manage your analytics views.
  * You can create at most 100 analytics views per Google Cloud project.
  * You can create at most 50 analytics views per region.
  * Per Google Cloud project, at most 10 regions can contain an analytics view.



## What's next

  * [Query and analyze logs overview](https://docs.cloud.google.com/logging/docs/log-analytics)
  * [Save and share a SQL query](https://docs.cloud.google.com/logging/docs/analyze/save-share-query)
  * [Chart SQL query results](https://docs.cloud.google.com/logging/docs/analyze/charts)
  * [Sample SQL queries](https://docs.cloud.google.com/logging/docs/analyze/examples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
