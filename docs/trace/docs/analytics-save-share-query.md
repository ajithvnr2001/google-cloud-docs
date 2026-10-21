---
url: https://docs.cloud.google.com/trace/docs/analytics-save-share-query/
title: Save and share queries \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:57.498033+00:00
---

# Save and share queries  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/analytics-save-share-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Save and share queries Stay organized with collections  Save and categorize content based on your preferences. 

Observability Analytics lets you save and share [SQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) queries so that you can rerun frequent Cloud Trace investigations and collaborate with team members across your project. Saved queries can be kept private for your own use or shared with other project members. If you haven't written queries in Observability Analytics, then first see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

## Before you begin

Configure your project, your IAM roles, and select the interface that you plan to use.

### Configure your project and roles

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

  8. To get the permissions that you need to load the **Observability Analytics** page, write, run, and save private queries on your trace data, ask your administrator to grant you the following IAM roles: 

     * [Observability View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewAccessor) (`roles/observability.viewAccessor`) on the observability views that you want to query. This role supports IAM conditions, which let you restrict the grant to a specific view. If you don't attach a condition to the role grant, then the principal can access all observability views.
     * [Observability Analytics User ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`) on your project. This role contains the permissions required to save and run private queries, and to run shared queries.

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note** : If you want to create and manage shared queries, then the previous IAM roles aren't sufficient. To create and manage shared queries, your IAM roles must include the `logging.queries.{share, updateShared, deleteShared}` permissions.



### Select the interface you plan to use

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

## Save a query

All queries that you run are automatically saved for 30 days and are accessible by selecting the **Recent** tab on the **Observability Analytics** page. You can search, view, run, and share the queries that are listed on the **Recent** tab.

To reuse a query, add custom descriptions, or share it with teammates, save the query. You can search and sort your saved queries by their name, their description, and their visibility label. You can also edit and delete these queries. Queries that you save are retained until you delete them.

You can save 10,000 queries per Google Cloud project.

**Note:** Queries that you save by using the Google Cloud console are stored in the `global` location. To specify where your queries are stored, use the Google Cloud CLI or the Cloud Logging API.

###  Console 

To save a query, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Populate the **Query** pane with a query.

You can populate the **Query** pane by entering a new query, by selecting a query from the **Recent** tab, or by selecting a query from the **Saved** tab.

Your query can include any valid view, multiple views, and [analytics views](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views).

When the query in the **Query** pane is valid, the save **Save** button is enabled.

  3. Click save **Save** , select **Save query** , and complete the **Name** and **Description** fields. The values you set for these fields are shown on the **Saved** tab.

  4. Optional: To let everyone with access to the **Observability Analytics** page for the Google Cloud project view and run your saved query, enable the **Share with project** toggle.

By default, this toggle is disabled and the visibility is restricted to you.

  5. Click **Save query**.

  6. Optional: To view, sort, and run saved queries that are visible to you, select the **Saved** tab.

You can sort and filter your saved queries by their name, description, and visibility label. You can also filter by the contents of the query.




You can edit and delete queries that you created by using options on the **Saved** tab:

  * To edit a query, click _more_vert_ **More Options** and select **Edit**. You can modify the values for the **Name** and **Description** fields; however, the query itself can't be modified.

  * To delete a saved query, click _more_vert_ **More Options** and select **Delete**.




###  gcloud 

To create and save a query, do the following:

  1. Before using any of the command data below, make the following replacements: 

     * DISPLAY_NAME: The display name of the saved query.
     * LOCATION: The location for the saved query.
     * VISIBILITY: Set to `private` or to `shared`.
     * SQL_QUERY: A SQL query. If single backquotes `(`)` wrap the path or fields within the path, then you must escape those backquotes: 
           
           "SELECT * FROM \`PROJECT_ID.LOCATION.my-log-bucket._AllLogs\`"
               

or
           
           "SELECT * FROM \`PROJECT_ID.LOCATION._Trace.Spans._AllSpans\`"
               

Backquotes `(`)` are required when a path element contains a period `(.)` character.

     * ID: The ID of the saved query. This ID is a required input for commands that describe, update, or delete a saved query. If you don't provide the ID when creating a saved query, then the system generates a numeric ID.
     * DESCRIPTION: A text description of the query. Optional.
     * PROJECT_ID: The identifier of the project.

Execute the [`gcloud logging saved-queries create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/saved-queries/create) command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud logging saved-queries create --display-name=DISPLAY_NAME \
     --location=LOCATION --visibility=VISIBILITY --sql-query-text=SQL_QUERY \
     --id=ID --description=DESCRIPTION --project=PROJECT_ID

#### Windows (PowerShell)
    
    gcloud logging saved-queries create --display-name=DISPLAY_NAME `
     --location=LOCATION --visibility=VISIBILITY --sql-query-text=SQL_QUERY `
     --id=ID --description=DESCRIPTION --project=PROJECT_ID

#### Windows (cmd.exe)
    
    gcloud logging saved-queries create --display-name=DISPLAY_NAME ^
     --location=LOCATION --visibility=VISIBILITY --sql-query-text=SQL_QUERY ^
     --id=ID --description=DESCRIPTION --project=PROJECT_ID

The following is an example response when the ID provided in the command was `my-saved-query`:
    
    Created saved query [projects/PROJECT_ID/locations/LOCATION/savedQueries/my-saved-query].
    

The response to the `create` command lists the full name of the query, which includes the query's ID. The query ID, which in this example is `my-saved-query`, is a required input for Google Cloud CLI commands that describe, delete, or update a saved query.

  2. To inspect the saved query, run the following command:
         
         gcloud logging saved-queries list --location=- --project=PROJECT_ID
         

In the preceding expression, the value for the location is a hyphen `(-)`, which acts as a wildcard. You can also provide a specific location.




There are Google Cloud CLI commands for deleting, listing, describing, and updating saved queries. For more information, see [`gcloud logging saved-queries` overview](https://docs.cloud.google.com/sdk/gcloud/reference/logging/saved-queries).

###  REST 

You can save a query by using the Cloud Logging API. To save a query, use the [`savedQueries.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/create) method.

To execute this method, do the following:

  1. Select [`savedQueries.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/create).
  2. On the reference page, use the [APIs Explorer](https://docs.cloud.google.com/logging/docs/api) to issue a command. You must specify the `opsAnalyticsQuery` field.



The following example illustrates a sample request body, which contains an instance of `SavedQuery`:
    
    
    {
       "parent": "projects/my-project/locations/global"
       "saved_query":
       {
          "ops_analytics_query":
          {
             "sql_query_text" :
                "SELECT
                timestamp, log_name, severity, json_payload, resource, labels
                FROM
                `VIEW`
                WHERE
                timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR)
                ORDER BY timestamp ASC
                LIMIT 100"
          }
       "visibility": "PRIVATE"
       }
    }
    

## Share a query

You can share a saved query with everyone that has access to your Google Cloud project. However, the principal's IAM roles determine whether the query can be run and the data that the query returns.

###  Console 

When troubleshooting a problem, or when you see anomalous results, you might want to share a query and its results with a teammate. When you are viewing query results on the **Observability Analytics** page, you can copy a URL that, when opened, displays the query you ran and its results.

To share a query and results with a teammate, do the following:

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Populate the **Query** pane with a query and then click **Run query**.

You can populate the **Query** pane by entering a new query, by selecting a query from the **Recent** tab, or by selecting a query from the **Saved** tab.

  3. Click _link_ **Share link**.

  4. Send the link to your teammate.

When your teammate opens the link, the **Observability Analytics** page opens and displays, but doesn't run, the query. Your teammate must manually run the query.

The **Observability Analytics** page displays a warning dialog when the query runs on the BigQuery engine and the queried resources aren't in the same ownership boundary. Ownership boundaries are determined by several factors, one of which is the hierarchy of the resources the query uses.

To open the URL successfully, your teammate's IAM role on the Google Cloud project must include the permissions required to view the **Observability Analytics** page.




###  gcloud 

When you want to create a saved query that can be run by others, set the value of the `visibility` field to `shared`:
    
    
    --visibility=shared
    

To change the visibility of an existing saved query, use the `update` command. For more information about the available commands, see [`gcloud logging saved-queries` overview](https://docs.cloud.google.com/sdk/gcloud/reference/logging/saved-queries).

###  REST 

You can use the Logging API to create a shared query by using the `savedQueries.create` method, and specifying a value of `SHARED` in the `visibility` field. For more information, see the reference page for [`savedQueries.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.savedQueries/create).

## View and run recent or saved queries

To view or re-run a query, select the **Recent** tab on the **Observability Analytics** page and find the query:

  * To run the query, click **Run**.
  * To view the query, use the options in the _more_vert_ **More Options** menu.



To view, edit, or run a saved query, select the **Saved** tab on the **Observability Analytics** page and find the query:

  * To run the query, click **Run**.
  * To edit, view, or delete the query, use the options in the _more_vert_ **More Options** menu.



## What's next

  * [Chart SQL query results](https://docs.cloud.google.com/trace/docs/analytics-chart)
  * [Sample SQL queries](https://docs.cloud.google.com/trace/docs/analytics-samples)
  * [Query a linked BigQuery dataset in BigQuery](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
