---
url: https://docs.cloud.google.com/trace/docs/create-and-manage-analytics-views/
title: Create, query, and manage analytics views \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:28.491509+00:00
---

# Create, query, and manage analytics views  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/create-and-manage-analytics-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Create, query, and manage analytics views Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Analytics views in Observability Analytics let you define a SQL query with a custom schema over your Cloud Trace data so that you can simplify and reuse complex transformations. After you create an analytics view, you can query its results in the `FROM` clause of other SQL queries, just like you query observability views.

For an overview of analytics views, see [About analytics views](https://docs.cloud.google.com/trace/docs/about-analytics-views).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  8. To get the permissions that you need to create, manage, and use analytics views, ask your administrator to grant you the following IAM roles: 

     * [Observability View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewAccessor) (`roles/observability.viewAccessor`) on the observability views that you want to query. This role supports IAM conditions, which let you restrict the grant to a specific view. If you don't attach a condition to the role grant, then the principal can access all observability views.
     * [Observability Analytics User ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`) on your project. This role contains the permissions required to save and run private queries and to run shared queries.

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  9. Make sure that you have an observability view. To learn more, see [Cloud Trace storage model](https://docs.cloud.google.com/stackdriver/docs/observability/storage-overview#trace-data-storage). 



## Create an analytics view

**Note:** An analytics view can query observability views. If an analytics view queries multiple views, then those views must be in the same location. 

To create an analytics view, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Configure the **Observability Analytics** page: 
     1. Make sure that the toolbar displays **Run query**. If the toolbar displays **Run in BigQuery** , then click _settings_ **Settings** and select **Observability Analytics (default)**.
     2. If the **Views** menu isn't shown, then go to the navigation pane and click _last_page_ **Views and Schema**.
  3. Enter and validate the query that you want to save as an analytics view.

You might want to load and edit the default query for the observability view that your analytics view will query. To load the default query, do the following:

     1. In the **Views** menu, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Traces** section, and then select `_Trace.Spans._AllSpans`. 
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

You query an analytics view in a manner analogous to querying observability views. To query analytics views, use the following format for the `FROM` clause:
    
    
    FROM `analytics_view.PROJECT_ID.LOCATION.ANALYTICS_VIEW_ID`
    

The fields in the previous expressions have the following meaning:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The location of the analytics view.
  * ANALYTICS_VIEW_ID: The ID of the analytics view, which is limited to 100 characters and can include only letters, digits, underscores, and hyphens.



To learn more, see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

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

  * An analytics view can only query observability views.
  * The parent resource of an analytics view must be a Google Cloud project.
  * You can only query an analytics view by using the **Observability Analytics** page, and only when you use the **Observability Analytics (default)** query engine.
  * All views that an analytics view queries must be in the same location.
  * You must use the Google Cloud console to create or manage your analytics views.
  * You can create at most 100 analytics views per Google Cloud project.
  * You can create at most 50 analytics views per region.
  * Per Google Cloud project, at most 10 regions can contain an analytics view.



## What's next

  * [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics)
  * [Chart SQL query results](https://docs.cloud.google.com/trace/docs/analytics-chart)
  * [Save and share queries](https://docs.cloud.google.com/trace/docs/analytics-save-share-query)
  * [Sample SQL queries](https://docs.cloud.google.com/trace/docs/analytics-samples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
