---
url: https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views/
title: Create and manage logical views \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:17.295804+00:00
---

# Create and manage logical views  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage logical views

_Logical views_ in Bigtable let you save SQL queries as virtual tables that other SQL queries can reference while data remains in the source table. Using these views helps you do the following:

  * Avoid repeating query logic
  * Present data in a relational format
  * Restrict read access to specific rows or columns



You can create and manage logical views using the Google Cloud CLI or the Bigtable Studio query editor in the Google Cloud console. You can query logical views using the query editor or any of the Bigtable [client libraries that support SQL](https://docs.cloud.google.com/bigtable/docs/googlesql-overview#client-libraries). For a comparison with continuous materialized views and authorized views, see [Tables and views](https://docs.cloud.google.com/bigtable/docs/tables-and-views).

## About logical views

Logical views let you do the following with your Bigtable data:

  * **Avoid query repetition** : You can store and evolve column mapping and cast logic in a logical view, which additional logical views can use instead of copying and pasting that logic or needing to understand it.
  * **Integrate with systems designed to read from relational databases** : Logical views let you make your Bigtable data read like a relational database table or Cassandra table.
  * **Run the same logical view against many tables** : By modifying the `FROM` clause, you can use the same view to query any table in your Bigtable instance.
  * **Provide a consistent interface** : Your application can use a logical view even if the source table changes.
  * **Limit read access to specific columns or rows** : You can expose only the data that you want to allow users to read, without giving them access to the entire table.



A logical view is an instance-level resource with the following characteristics:

  * Must use SQL features supported by [GoogleSQL for Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/sql/googlesql-reference-overview)
  * The SQL query that defines a logical view can't use `SELECT *`.
  * Read-only
  * Must be read with SQL rather than with a call to `ReadRows`
  * Can be queried using any of the Bigtable [client libraries that support SQL](https://docs.cloud.google.com/bigtable/docs/googlesql-overview#client-libraries)
  * Uses _definer rights_. You can query a logical view if you have permissions to read from it even if you don't have permission to read from the source table.



The row key, column qualifier, and column values that you use to define a logical view are treated as service data. For this reason, don't create a logical view using row key, column qualifier, or column values that contain [sensitive information](https://docs.cloud.google.com/bigtable/docs/schema-design#privacy). For information about how service data is handled, see the [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).

## Before you begin

Take the following steps if you plan to use the gcloud CLI:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

**Note:** If the gcloud CLI returns a `Method not found` message, run the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command again.

### Required roles

To work with logical views, you need the following permissions:

**To manage logical views:**

  * To create, update, or delete logical views, you need the Bigtable Admin (`roles/bigtable.admin`) role on the instance.
  * Alternatively, you can ask your administrator to grant you the following permissions at the instance level: 
    * Create: `bigtable.logicalViews.create`
    * Update: `bigtable.logicalViews.update`
    * Delete: `bigtable.logicalViews.delete`



**To view and query logical views:**

  * To list or describe logical views, you need the Bigtable Reader (`roles/bigtable.reader`) role on the instance.
  * Alternatively, you can ask your administrator to grant you the following permissions at the instance level:

    * List: `bigtable.logicalViews.list`
    * Describe: `bigtable.logicalViews.get`
  * To query a logical view, you need the `bigtable.logicalViews.readRows` permission on the logical view.

**Note:** You don't need permission to read the source table.



**To create a logical view:**

  * You must have at least `bigtable.tables.readRows` permission on the source table.



**To grant read access to a specific view:**

You can grant a user permission to read a specific logical view, even if they don't have any other Bigtable permissions. To do this, use an IAM condition to grant the `bigtable.logicalViews.readRows` permission only on that view:

  1. Grant the user the `bigtable.reader` role on the project.
  2. Create an IAM condition that limits the `bigtable.logicalViews.readRows` permission to the specific logical view. For example:
         
         resource.name == projects/PROJECT_ID/instances/INSTANCE_ID/logicalViews/VIEW
         

Replace the following:

     * `PROJECT_ID`: the Google Cloud project that your Bigtable instance is in.
     * `VIEW`: an ID up to 128 characters long for the new logical view. The ID must be unique among table IDs and view IDs in the instance.
     * `INSTANCE_ID`: the ID of instance to create the logical view in.

For more information, see [Manage access to resources using IAM conditions](https://docs.cloud.google.com/bigtable/docs/access-control#iam-conditions).




For more information about all available roles and permissions, see [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).

## Create a logical view

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance.

  3. In the navigation pane, click **Bigtable Studio**.

  4. Open a new tab by clicking add and then choosing **Editor**.

     1. In the query editor, write your query. If the query is valid SQL, a **Valid** message is displayed.

     2. Optional: To format your statement in SQL style, click **Format**.

     3. Click **Run**. The results of your query appear in the **Results** table.

     4. When you're satisfied with the query, click the **Save as** expander arrow and choose **Save as logical view**.

  5. In the **Save your logical view** dialog, enter a name for the view, and then click **Save**.

For more information about using the query editor, see [Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).




###  gcloud 

To create a logical view, use the [`gcloud bigtable logical-views create`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/create) command.
    
    
    gcloud bigtable logical-views create VIEW \
      --instance=INSTANCE --query=QUERY
    

Replace the following:

  * `VIEW`: an ID up to 128 characters long for the new logical view. The ID must be unique among table IDs and view IDs in the instance.
  * `QUERY`: a valid GoogleSQL for Bigtable query. The query can't use `SELECT *`.
  * `INSTANCE`: the ID of instance to create the logical view in



Optional:

  * To protect the logical view from deletion, append the command with the `--deletion-protection` flag. If you don't apply this setting, the logical view can be deleted. You can also explicitly allow logical view deletion by appending `--no-deletion-protection`. For more information, see the Update a logical view section of this document.



## Update a logical view

###  Console 

You can't update deletion protection for a logical view in the Google Cloud console. To enable or disable deletion protection, use the Google Cloud CLI.

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation pane, click **Bigtable Studio**. A list of views is displayed in the explorer.

  4. Optional: The first 10 views in the instance are listed. To see 10 more, click **Show more**.

  5. Next to the view that you want to update, click the more_vert action menu, and then click **View definition**.

  6. Modify the query.

  7. Click **Run**.

  8. After you've verified that the results pane shows data that should be included in the view, click **Save as**.

  9. In the dialog, enter the ID of the view that you modified.

The dialog displays a message warning you that you are overwriting the existing view.

  10. Click **Save**.




###  gcloud 

To update a logical view to run a different query or to modify deletion protection, use the [`gcloud bigtable logical-views update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/update) command. You must specify the query, deletion protection, or both.

To update a logical view's query:
    
    
    gcloud bigtable logical-views update VIEW  \
        --instance=INSTANCE --query=QUERY
    

To enable deletion protection for a logical view:
    
    
    gcloud bigtable logical-views update VIEW \
        --instance=INSTANCE \
        --deletion-protection=true
    

To disable deletion protection for a logical view:
    
    
    gcloud bigtable logical-views update VIEW \
        --instance=INSTANCE \
        --deletion-protection=false
    

Replace the following:

  * `VIEW`: the ID of the logical view to update
  * `INSTANCE`: the ID of instance that contains the logical view
  * `QUERY`: a valid GoogleSQL query



## Delete a logical view

This action is permanent.

If a logical view has deletion protection enabled, you can't delete it. To delete a logical view that has deletion protection enabled, you must update the logical view to disable deletion protection. For more information, see the Update a logical view section of this document.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation pane, click **Bigtable Studio**. A list of views is displayed in the explorer.

  4. Optional: The first 10 views in the instance are listed. To see 10 more, click **Show more**.

  5. Expand **Views**.

  6. Next to the view that you want to delete, click the more_vert action menu, and then click **Delete**.




###  gcloud 

To delete a logical view, use the [`gcloud bigtable logical-views delete`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/delete) command.
    
    
      gcloud bigtable logical-views delete VIEW \
        --instance=INSTANCE
    

Replace the following:

  * `VIEW`: the ID of the logical view to update
  * `INSTANCE`: the ID of instance that contains the logical view



## Get a list of logical views for an instance

You can see a list of logical views for an instance.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation pane, click **Bigtable Studio**. A list of views is displayed in the explorer.

  4. Optional: The first 10 views in the instance are listed. To see 10 more, click **Show more**.




###  gcloud 

To see a list of logical views for an instance, use the [`gcloud bigtable logical-views list`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/logical-views/list) command.
    
    
    gcloud bigtable logical-views list --instance=INSTANCE
    

Replace `INSTANCE` with the instance ID.

## Describe a logical view

To get details about a logical view, use the `gcloud bigtable logical-views describe` command.
    
    
      gcloud bigtable logical-views describe VIEW \
          --instance=INSTANCE
    

The terminal displays details similar to the following:
    
    
      createTime: '2025-03-07T19:49:56.316578Z'
      etag: W/"/v1/17919275593532352351"
      name: projects/my-project/instances/my-instance/logicalViews/my-view
      query: SELECT street FROM addresses
      updateTime: '2025-03-07T19:49:56.316578Z'
      deletion_protection: true
    

## Query a logical view

After you create a logical view, you can query it using SQL, much like you query a regular table. You can use logical views in the `FROM` clause of `SELECT` statements.

In the query editor, enter a GoogleSQL query that references the view name. For example, if your view is named `MyLogicalView`:
    
    
    SELECT *
    FROM MyLogicalView
    LIMIT 100;
    

For more information about executing SQL queries in Bigtable, see [Query your data with SQL in the query editor](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console#query-editor).

## What's next

  * To learn more about querying Bigtable data with SQL, see [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).
  * To precompute and cache query results from a source table, see [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views).
  * To configure fine-grained read and write access to specific subsets of data, see [Authorized views overview](https://docs.cloud.google.com/bigtable/docs/authorized-views).
  * To dynamically filter logical view data based on application context, see [Parameterized views overview](https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
