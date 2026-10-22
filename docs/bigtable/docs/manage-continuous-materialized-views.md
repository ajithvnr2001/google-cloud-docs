---
url: https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views/
title: Create and manage continuous materialized views \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:10.833414+00:00
---

# Create and manage continuous materialized views  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage continuous materialized views

Continuous materialized views in Bigtable let you accelerate analytical queries by automatically maintaining precomputed aggregations from your source tables.

You can create and manage these views using the Google Cloud CLI, the Bigtable Studio query editor in the Google Cloud console, or the Bigtable client libraries for Java and Go.

## Before you begin

Review the [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) overview.

If you plan to use the gcloud CLI, take the following steps:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 



If the gcloud CLI returns a `Method not found` message, run the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command again.

### Required roles

To get the permissions that you need to create and manage continuous materialized views, ask your administrator to grant you the Bigtable Admin (`roles/bigtable.admin`) role on the instance. Otherwise, ask for the following permissions at the instance level, depending on the operation that you want to perform:

  * Create: `bigtable.materializedViews.create`
  * Update: `bigtable.materializedViews.update`
  * Delete: `bigtable.materializedViews.delete`
  * List: `bigtable.materializedViews.list`



To create a continuous materialized view, you must also have at least `bigtable.tables.readRows` permission on the source table.

To see all available roles and permissions, see [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).

## Create a continuous materialized view

Before you create a continuous materialized view, do the following:

  * Optional: As a best practice, enable [autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling) for clusters in your instance to make sure they can scale up if necessary while Bigtable processes and synchronizes the continuous materialized view and to handle any additional [storage usage](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views#storage).
  * Optional: Decide whether you want your continuous materialized view to be available across all clusters, or whether you want to isolate both its processing and query availability to a single cluster. For more information, see [Non-deterministic SQL functions](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views#non-deterministic-functions).
  * Identify a Bigtable table that you have permission to read to use as the source for the continuous materialized view.
  * Prepare the SQL query that defines your continuous materialized view. For query requirements, see [Continuous materialized view queries](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries).




###  Console 

**Note:** To create a continuous materialized view isolated to a single cluster, use the gcloud CLI.

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance.

  3. In the navigation pane, click **Bigtable Studio**.

  4. Open a new tab by clicking add and then choosing **Editor**.

     1. When the query editor appears, write your query. If the query is valid SQL, a **Valid** message is displayed.

     2. Optional: To format your statement in SQL style, click **Format**.

     3. Click **Run**. The results of your query appear in the **Results** table.

     4. When you're satisfied with the query, click the **Save as** expander arrow and choose **Save as materialized view**.

  5. In the **Save your materialized view** dialog, enter a name for the view, and then click **Save**.

For more information about using the query editor, see [Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).




###  gcloud 

To create a continuous materialized view, use the [`gcloud bigtable materialized-views create`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/create) command:
    
    
        gcloud bigtable materialized-views create VIEW \
                --instance=INSTANCE --query=QUERY
    

Replace the following:

  * `VIEW`: a unique identifier for the continuous materialized view. You use this ID as the table ID when querying the continuous materialized view.
  * `INSTANCE`: the identifier of the instance to create the continuous materialized view in. Must be the same instance as the source table.
  * `QUERY`: a valid SQL statement that defines the continuous materialized view.



#### Optional: Enable deletion protection

To enable deletion protection for the continuous materialized view, append the command with `--deletion-protection=DELETION_PROTECTION`. Replace `DELETION_PROTECTION` with either `true` or `false`.

#### Optional: Create a view isolated to a single cluster

By default, Bigtable replicates a continuous materialized across all clusters in an instance. To keep a view in a specific cluster only, define your view with `CLUSTER_ATTRIBUTE` and pass the `--ignore-warnings` flag:
    
    
    gcloud bigtable materialized-views create VIEW \
      --instance=INSTANCE \
      --query="SELECT ... WHERE CLUSTER_ATTRIBUTE('cluster_id') = 'CLUSTER_ID'" \
      --ignore-warnings
    

Replace the following:

  * `VIEW`: a unique identifier for the continuous materialized view. You use this ID as the table ID when querying the continuous materialized view.
  * `INSTANCE`: the identifier of the instance to create the continuous materialized view in. Must be the same instance as the source table.
  * `CLUSTER_ID`: the identifier of the cluster where you want to maintain the view.



Because `CLUSTER_ATTRIBUTE` produces different results across clusters, you must include the `--ignore-warnings` flag to acknowledge the differences. For more information about query syntax and requirements, see [Isolate a view to a single cluster](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries#isolate-view-to-cluster).

## Query a continuous materialized view

After a continuous materialized view is active, you can query it like any other table using Bigtable Studio in the Google Cloud console, or supported client libraries. For more information about query syntax and requirements, see [Continuous materialized view queries](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries).

To test and query a view before initial population completes, use the `@{allow_incomplete_view=true}` query hint. For more information, see [Read data during initial population](https://docs.cloud.google.com/bigtable/docs/reads#read-during-initial-population).

## Update a continuous materialized view

You can update deletion protection for a continuous materialized view. You can't update the SQL query that defines a continuous materialized view; if you need to modify the query, you must delete the continuous materialized view and then create a new one that includes your changes.

###  Console 

You can't update a continuous materialized view in the console. Use the gcloud CLI instead.

###  gcloud 

To enable or disable deletion protection for a continuous materialized view, use the [`gcloud bigtable materialized-views update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/update) command.
    
    
    gcloud bigtable materialized-views update VIEW \
            --instance=INSTANCE --deletion-protection=DELETION_PROTECTION
    

Replace the following:

  * `VIEW`: the unique identifier for the continuous materialized view that you want to update
  * `INSTANCE`: the identifier of the instance containing the continuous materialized view
  * `DELETION_PROTECTION`: either `true` or `false`



## Delete a continuous materialized view

You can delete a continuous materialized view that doesn't have deletion protection enabled. You can't undo this operation.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation pane, click **Bigtable Studio**.

  4. Expand **Materialized views**.

  5. Next to the view that you want to delete, click the more_vert action menu, and then click **Delete**.




###  gcloud 

To delete a continuous materialized view, use the [`gcloud bigtable materialized-views delete`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/delete) command:
    
    
    gcloud bigtable materialized-views delete VIEW \
          --instance=INSTANCE
    

Replace the following:

  * `VIEW`: the unique identifier for the continuous materialized view that you want to delete
  * `INSTANCE`: the identifier of the instance containing the continuous materialized view



## Get a list of continuous materialized views

You can see a list of continuous materialized views for an instance.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Select an instance from the list.

  3. In the navigation pane, click **Bigtable Studio.** A list of continuous materialized views is displayed.

  4. Optional: The first 10 views in the instance are listed. To see 10 more, click **Show more**.




###  gcloud 

To list all continuous materialized views for an instance, use the [`gcloud bigtable materialized-views list`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/materialized-views/list) command.
    
    
    gcloud bigtable materialized-views list --instance=INSTANCE
    

Replace `INSTANCE` with the instance ID.

## What's next

  * [Continuous materialized view queries](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries)
  * [Tables and views](https://docs.cloud.google.com/bigtable/docs/tables-and-views)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
