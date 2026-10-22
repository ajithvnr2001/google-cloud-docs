---
url: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-authorized-view-tutorial/
title: Create an authorized view \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:46.345478+00:00
---

# Create an authorized view  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/samples/bigquery-authorized-view-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Samples ](https://docs.cloud.google.com/bigquery/docs/samples)



#  Create an authorized view Stay organized with collections  Save and categorize content based on your preferences. 

Create an authorized view using GitHub public data.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Authorized views](https://docs.cloud.google.com/bigquery/docs/authorized-views)
  * [Create an authorized view](https://docs.cloud.google.com/bigquery/docs/create-authorized-views)



## Code sample

### Java

Before trying this sample, follow the Java setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/overview). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    // Create a source dataset to store your table.
    final Dataset sourceDataset = bigquery.create(DatasetInfo.of(sourceDatasetId));
    // Populate a source table
    String tableQuery =
        "SELECT commit, author, committer, repo_name"
            + " FROM `bigquery-public-data.github_repos.commits`"
            + " LIMIT 1000";
    QueryJobConfiguration queryConfig =
        QueryJobConfiguration.newBuilder(tableQuery)
            .setDestinationTable(TableId.of(sourceDatasetId, sourceTableId))
            .build();
    bigquery.query(queryConfig);
    // Create a separate dataset to store your view
    Dataset sharedDataset = bigquery.create(DatasetInfo.of(sharedDatasetId));
    // Create the view in the new dataset
    String viewQuery =
        String.format(
            "SELECT commit, author.name as author, "
                + "committer.name as committer, repo_name FROM %s.%s.%s",
            projectId, sourceDatasetId, sourceTableId);
    ViewDefinition viewDefinition = ViewDefinition.of(viewQuery);
    Table view =
        bigquery.create(TableInfo.of(TableId.of(sharedDatasetId, sharedViewId), viewDefinition));
    // Assign access controls to the dataset containing the view
    List<Acl> viewAcl = new ArrayList<>(sharedDataset.getAcl());
    viewAcl.add(Acl.of(new Acl.Group("example-analyst-group@google.com"), Acl.Role.READER));
    sharedDataset.toBuilder().setAcl(viewAcl).build().update();
    // Authorize the view to access the source dataset
    List<Acl> srcAcl = new ArrayList<>(sourceDataset.getAcl());
    srcAcl.add(Acl.of(new Acl.View(view.getTableId())));
    sourceDataset.toBuilder().setAcl(srcAcl).build().update();

### Python

Before trying this sample, follow the Python setup instructions in the [BigQuery quickstart using client libraries](https://docs.cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries). For more information, see the [BigQuery Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/bigquery/latest). 

To authenticate to BigQuery, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigquery/docs/authentication#client-libs). 
    
    
    # Create a source dataset
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    from google.cloud.bigquery.enums import [EntityTypes](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.EntityTypes.html)
    
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)()
    source_dataset_id = "github_source_data"
    source_dataset_id_full = "{}.{}".format(client.project, source_dataset_id)
    
    
    source_dataset = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html)(source_dataset_id_full)
    # Specify the geographic location where the dataset should reside.
    source_dataset.location = "US"
    source_dataset = client.[create_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_dataset)(source_dataset)  # API request
    
    # Populate a source table
    source_table_id = "github_contributors"
    job_config = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[QueryJobConfig](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.QueryJobConfig.html)()
    job_config.destination = source_dataset.[table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_table)(source_table_id)
    sql = """
        SELECT commit, author, committer, repo_name
        FROM `bigquery-public-data.github_repos.commits`
        LIMIT 1000
    """
    client.[query_and_wait](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_query_and_wait)(
        sql,
        # Location must match that of the dataset(s) referenced in the query
        # and of the destination table.
        location="US",
        job_config=job_config,
    )  # API request - starts the query and waits for query to finish
    
    # Create a separate dataset to store your view
    shared_dataset_id = "shared_views"
    shared_dataset_id_full = "{}.{}".format(client.project, shared_dataset_id)
    
    
    shared_dataset = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html)(shared_dataset_id_full)
    shared_dataset.location = "US"
    shared_dataset = client.[create_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_dataset)(shared_dataset)  # API request
    
    # Create the view in the new dataset
    shared_view_id = "github_analyst_view"
    view = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table.html)(shared_dataset.[table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_table)(shared_view_id))
    sql_template = """
        SELECT
            commit, author.name as author,
            committer.name as committer, repo_name
        FROM
            `{}.{}.{}`
    """
    [view](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.AccessEntry.html#google_cloud_bigquery_dataset_AccessEntry_view).[view_query](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.table.Table.html#google_cloud_bigquery_table_Table_view_query) = sql_template.format(
        client.project, source_dataset_id, source_table_id
    )
    view = client.[create_table](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_table)(view)  # API request
    
    # Assign access controls to the dataset containing the view
    # analyst_group_email = 'data_analysts@example.com'
    access_entries = shared_dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries)
    [access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries).append(
        [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[AccessEntry](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.AccessEntry.html)("READER", [EntityTypes](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.EntityTypes.html).GROUP_BY_EMAIL, analyst_group_email)
    )
    shared_dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries) = access_entries
    shared_dataset = client.[update_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_update_dataset)(
        shared_dataset, ["access_entries"]
    )  # API request
    
    # Authorize the view to access the source dataset
    access_entries = source_dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries)
    [access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries).append(
        [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[AccessEntry](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.AccessEntry.html)(None, [EntityTypes](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.enums.EntityTypes.html).VIEW, [view](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.AccessEntry.html#google_cloud_bigquery_dataset_AccessEntry_view).reference.to_api_repr())
    )
    source_dataset.[access_entries](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html#google_cloud_bigquery_dataset_Dataset_access_entries) = access_entries
    source_dataset = client.[update_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_update_dataset)(
        source_dataset, ["access_entries"]
    )  # API request

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    # Creates an authorized view.
    
    # Create a dataset to contain the view.
    resource "google_bigquery_dataset" "view_dataset" {
      dataset_id  = "view_dataset"
      description = "Dataset that contains the view"
      location    = "us-west1"
    }
    
    # Create the view to authorize.
    resource "google_bigquery_table" "movie_view" {
      project     = google_bigquery_dataset.view_dataset.project
      dataset_id  = google_bigquery_dataset.view_dataset.dataset_id
      table_id    = "movie_view"
      description = "View to authorize"
    
      view {
        query          = "SELECT item_id, avg(rating) FROM `movie_project.movie_dataset.movie_ratings` GROUP BY item_id ORDER BY item_id;"
        use_legacy_sql = false
      }
    }
    
    
    # Authorize the view to access the dataset
    # that the query data originates from.
    resource "google_bigquery_dataset_access" "view_authorization" {
      project    = "movie_project"
      dataset_id = "movie_dataset"
    
      view {
        project_id = google_bigquery_table.movie_view.project
        dataset_id = google_bigquery_table.movie_view.dataset_id
        table_id   = google_bigquery_table.movie_view.table_id
      }
    }
    
    # Specify the IAM policy for principals that can access
    # the authorized view. These users should already
    # have the roles/bigqueryUser role at the project level.
    data "google_iam_policy" "principals_policy" {
      binding {
        role = "roles/bigquery.dataViewer"
        members = [
          "group:example-group@example.com",
        ]
      }
    }
    
    # Set the IAM policy on the authorized  view.
    resource "google_bigquery_table_iam_policy" "authorized_view_policy" {
      project     = google_bigquery_table.movie_view.project
      dataset_id  = google_bigquery_table.movie_view.dataset_id
      table_id    = google_bigquery_table.movie_view.table_id
      policy_data = data.google_iam_policy.principals_policy.policy_data
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigquery). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
