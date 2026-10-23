---
url: https://docs.cloud.google.com/storage/docs/insights/manage-datasets/
title: Manage Storage Insights dataset configurations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:26:51.295547+00:00
---

# Manage Storage Insights dataset configurations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/manage-datasets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Manage Storage Insights dataset configurations Stay organized with collections  Save and categorize content based on your preferences. 

Storage Insights datasets let you collect metadata and activity data from your Cloud Storage buckets and objects, and then analyze that data in BigQuery. You can configure the data source, scope, and retention settings for a dataset to help optimize storage costs, manage data lifecycles, and support compliance.

This document shows you how to view, update, and delete dataset configurations, and how to query or unlink linked BigQuery datasets. For background information, see [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets).

## Get the required roles

To get the permissions that you need to manage dataset configurations, ask your administrator to grant you the following IAM roles on your source projects: 

  * To list, update, delete, and view dataset configurations: [Storage Insights Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storageinsights#storageinsights.admin) (`roles/storageinsights.admin`) 
  * To view and unlink datasets: 
    * [Storage Insights Analyst ](https://docs.cloud.google.com/iam/docs/roles-permissions/storageinsights#storageinsights.analyst) (`roles/storageinsights.analyst`)
    * [BigQuery Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)
  * To delete linked datasets: [BigQuery Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`) 
  * To view and query datasets in BigQuery: 
    * [Storage Insights Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storageinsights#storageinsights.viewer) (`roles/storageinsights.viewer`)
    * [BigQuery Job User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.jobUser) (`roles/bigquery.jobUser`)
    * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage dataset configurations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage dataset configurations:

  * View and list dataset configuration: 
    * `storageinsights.datasetConfigs.get`
    * `storageinsights.datasetConfigs.list`
    * `storage.buckets.getObjectInsights`
  * Update and delete dataset configuration: 
    * `storageinsights.datasetConfigs.update`
    * `storageinsights.datasetConfigs.delete`
    * `storage.buckets.getObjectInsights`
  * Unlink a BigQuery dataset: `storageinsights.datasetConfigs.unlinkDataset`
  * Query BigQuery linked datasets: `bigquery.jobs.create or bigquery.jobs.*`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View and query linked datasets

To view and query linked datasets, follow these steps:

  1. In the Google Cloud console, go to the Cloud Storage **Storage Insights** page.  


[Go to Storage Insights](https://console.cloud.google.com/storage/storageinsights)

Your project shows a list of created dataset configurations.

  2. Click the BigQuery linked dataset for the dataset configuration you want to view.

The Google Cloud console displays the BigQuery linked dataset. For information about the dataset schema of metadata, see [Dataset schema of metadata](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#metadata-schema).

  3. Query tables and views in your linked datasets as you would [query any other BigQuery table](https://docs.cloud.google.com/bigquery/docs/managing-table-data#querying_table_data).




## Unlink a dataset

To stop the dataset configuration from publishing to the BigQuery dataset, unlink the dataset. To unlink a dataset, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Storage Insights** page.  


[Go to Storage Insights](https://console.cloud.google.com/storage/storageinsights)

  2. Click the name of the dataset configuration that generated the dataset you want to unlink.

  3. In the **BigQuery linked dataset** section, click **Unlink dataset**.




### Command line

  1. To unlink the dataset, run the [`gcloud storage insights dataset-configs delete-link`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/insights/dataset-configs/delete-link) command:
         
         gcloud storage insights dataset-configs delete-link DATASET_CONFIG_ID --location=LOCATION

Replace:

     * `DATASET_CONFIG_ID` with the name of the dataset configuration that generated the dataset you want to unlink.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of your dataset and dataset configuration. For example, `us-central1`.

You can also specify a full dataset configuration path. For example:
    
    gcloud storage insights dataset-configs delete-link projects/DESTINATION_PROJECT_ID/locations/LOCATION/datasetConfigs/DATASET_CONFIG_ID

Replace:

     * `DESTINATION_PROJECT_ID` with the ID of the project that contains the dataset configuration. For more information about project IDs, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

     * `DATASET_CONFIG_ID` with the name of the dataset configuration that generated the dataset you want to unlink.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of your dataset and dataset configuration. For example, `us-central1`.




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "name": "DATASET_NAME"
         }

Replace:

`DATASET_NAME` with the name of the dataset you want to unlink. For example, `my_project.my_dataset276daa7e_2991_4f4f_b9d4_e354b48426a2`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with an [`unlinkDataset` DatasetConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/unlinkDataset) request:
         
         curl --request POST --data-binary @JSON_FILE_NAME \
         "https://storageinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasetConfigs/DATASET_CONFIG_ID:unlinkDataset?" \
           --header "Authorization: Bearer $(gcloud auth print-access-token --impersonate-service-account=SERVICE_ACCOUNT)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json"
         

Replace:

     * `JSON_FILE_NAME` with the path to the JSON file you created in the previous step.

     * `PROJECT_ID` with the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin) that the dataset configuration belongs to.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the dataset and dataset configuration. For example, `us-central1`.

     * `DATASET_CONFIG_ID` with the name of the dataset configuration that generated the dataset you want to unlink.

     * `SERVICE_ACCOUNT` with the service account. For example, `test-service-account@test-project.iam.gserviceaccount.com`.




## View a dataset configuration

To view a dataset configuration, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Storage Insights** page.  


[Go to Storage Insights](https://console.cloud.google.com/storage/storageinsights)

  2. Click the name of the dataset configuration you want to view.

The dataset configuration details are displayed.




### Command line

  1. To describe a dataset configuration, run the [`gcloud storage insights dataset-configs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/insights/dataset-configs/describe) command:
         
         gcloud storage insights dataset-configs describe DATASET_CONFIG_ID \
           --location=LOCATION

Replace:

     * `DATASET_CONFIG_ID` with the name of the dataset configuration.

     * `LOCATION` with the location of the dataset and dataset configuration.

You can also specify a full dataset configuration path. For example:
    
    gcloud storage insights dataset-configs describe projects/DESTINATION_PROJECT_ID/locations/LOCATION/datasetConfigs/DATASET_CONFIG_ID

Replace:

     * `DESTINATION_PROJECT_ID` with the ID of the project that contains the dataset configuration. For more information about project IDs, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

     * `DATASET_CONFIG_ID` with the name of the dataset configuration that generated the dataset you want to view.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of your dataset and dataset configuration. For example, `us-central1`.




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with an [`Get` DatasetConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/get) request:
         
         curl -X GET \
         "https://storageinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasetConfigs/DATASET_CONFIG_ID" \
           --header "Authorization: Bearer $(gcloud auth print-access-token --impersonate-service-account=SERVICE_ACCOUNT)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json"
         

Replace:

     * `PROJECT_ID` with the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin) that the dataset configuration belongs to.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the dataset and dataset configuration. For example, `us-central1`.

     * `DATASET_CONFIG_ID` with the name of the dataset configuration.

     * `SERVICE_ACCOUNT` with the service account. For example, `test-service-account@test-project.iam.gserviceaccount.com`.




## List dataset configurations

To list the dataset configurations in a project, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Storage Insights** page.  


[Go to Storage Insights](https://console.cloud.google.com/storage/storageinsights)

The list of dataset configurations is displayed.




### Command line

  1. To list dataset configurations in a project, run the [`gcloud storage insights dataset-configs list`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/insights/dataset-configs/list) command:
         
         gcloud storage insights dataset-configs list --location=LOCATION

Replace:

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the dataset and dataset configuration. For example, `us-central1`.

You can use the following optional flags to specify the behavior of the listing call:

     * Use `--page-size` to specify the maximum number of results to return per page.

     * Use `--filter=FILTER` to filter results. For more information on how to use the `--filter` flag, run `gcloud topic filters` and refer to the documentation.

     * Use `--sort-by=SORT_BY_VALUE` to specify a comma-separated list of resource field key names to sort by. For example, `--sort-by=DATASET_CONFIG_ID`.




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Get` DatasetConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/get) request:
         
         curl -X GET \
         "https://storageinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasetConfigs" \
           --header "Authorization: Bearer $(gcloud auth print-access-token --impersonate-service-account=SERVICE_ACCOUNT)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json"
         

Replace:

     * `PROJECT_ID` with the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin) that the dataset configuration belongs to.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the dataset and dataset configuration. For example, `us-central1`.

     * `SERVICE_ACCOUNT` with the service account. For example, `test-service-account@test-project.iam.gserviceaccount.com`.




## Update a dataset configuration

To update a dataset configuration, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Storage Insights** page.  


[Go to Storage Insights](https://console.cloud.google.com/storage/storageinsights)

  2. Click the name of the dataset configuration you want to update.

  3. In the **Dataset configuration** tab, click **Edit** edit to update the fields.




### Command line

  1. To update a dataset configuration, run the [`gcloud storage insights dataset-configs update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/insights/dataset-configs/update) command:
         
         gcloud storage insights dataset-configs update DATASET_CONFIG_ID \
           --location=LOCATION

Replace:

     * `DATASET_CONFIG_ID` with the name of the dataset configuration.

     * `LOCATION` with the location of the dataset and dataset configuration.

Use the following flags to update properties of the dataset configuration:

     * Use `--skip-verification` to skip checks and failures from the verification process, which includes checks for required IAM permissions. If used, some or all buckets might be excluded from the dataset.

     * Use `--retention-period-days=DAYS` to specify the moving number of days of data to capture in the dataset snapshot. For example, `90`.

     * Use `--activity-data-retention-period-days=ACTIVITY_RETENTION_PERIOD_DAYS` to specify the retention period for the [activity data](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs) in the dataset. By default, activity data is included in the dataset, and inherits the retention period of the dataset. To override the dataset retention period, specify the number of days to retain activity data for. To exclude activity data, set the ACTIVITY_RETENTION_PERIOD_DAYS to `0`.

     * Use `--description=DESCRIPTION` to write a description for the dataset configuration.

     * Use `--organization=ORGANIZATION_ID` to specify the organization ID of the source project. If unspecified, defaults to the source project's organization ID.




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following optional information:
         
         {
           "organization_number": "ORGANIZATION_ID",
           "source_projects": {
             "project_numbers": "PROJECT_NUMBERS"
           },
           "retention_period_days": "RETENTION_PERIOD",
           "activityDataRetentionPeriodDays": "ACTIVITY_DATA_RETENTION_PERIOD_DAYS"
         }

Replace:

     * `ORGANIZATION_ID` with the resource ID of the [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) to which the source projects belong to. If unspecified, defaults to the source project's organization ID.

     * `PROJECT_NUMBERS` with the [project numbers](https://docs.cloud.google.com/docs/overview#projects) to include in the dataset. You can specify one or more projects in a list format.

     * `RETENTION_PERIOD` with the moving number of days of data to capture in the dataset snapshot. For example, `90`.

     * `ACTIVITY_DATA_RETENTION_PERIOD_DAYS` with the number of days of [activity data](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#activity-data-schema) to capture in the dataset snapshot. By default, activity data is included in the dataset, and inherits the retention period of the dataset. To override the dataset retention period, specify the number of days to retain activity data for. To exclude activity data, set the ACTIVITY_RETENTION_PERIOD_DAYS to `0`.

  3. To update the dataset configuration, use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Patch` DatasetConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
         "https://storageinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasetConfigs/DATASET_CONFIG_ID?updateMask=UPDATE_MASK" \
           --header "Authorization: Bearer $(gcloud auth print-access-token --impersonate-service-account=SERVICE_ACCOUNT)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json"
         

Replace:

     * `JSON_FILE_NAME` with the path to the JSON file you created in the previous step.

     * `PROJECT_ID` with the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin) that the dataset configuration belongs to.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the dataset and dataset configuration. For example, `us-central1`.

     * `DATASET_CONFIG_ID` with the name of the dataset configuration you want to update.

     * `UPDATE_MASK` is the comma-separated list of field names that this request updates. The fields use the [fieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format and are part of the [`DatasetConfig`](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs) resource.

     * `SERVICE_ACCOUNT` with the service account. For example, `test-service-account@test-project.iam.gserviceaccount.com`.




## Delete a dataset configuration

To delete a dataset configuration, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Storage Insights** page.  


[Go to Storage Insights](https://console.cloud.google.com/storage/storageinsights)

  2. Click the name of the dataset configuration you want to delete.

  3. Click **Delete** delete.




### Command line

  1. To delete a dataset configuration, run the [`gcloud storage insights dataset-configs delete`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/insights/dataset-configs/delete) command:
         
         gcloud storage insights dataset-configs delete DATASET_CONFIG_ID \
           --location=LOCATION

Replace:

     * `DATASET_CONFIG_ID` with the name of the dataset configuration you want to delete.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the dataset and dataset configuration. For example, `us-central1`.

Use the following flags to delete a dataset configuration:

     * Use `--auto-delete-link` to unlink the dataset that was generated from the dataset configuration you want to delete. You must unlink a dataset before you can delete the dataset configuration that generated the dataset.

You can also specify a full dataset configuration path. For example:
    
    gcloud storage insights dataset-configs delete projects/DESTINATION_PROJECT_ID/locations/LOCATION/datasetConfigs/DATASET_CONFIG_ID




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with an [`Delete` DatasetConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/delete) request:
         
         curl -X DELETE \
           "https://storageinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasetConfigs/DATASET_CONFIG_ID" \
           --header "Authorization: Bearer $(gcloud auth print-access-token --impersonate-service-account=SERVICE_ACCOUNT)" \
             --header "Accept: application/json" \
             --header "Content-Type: application/json"
         

Replace:

     * `PROJECT_ID` with the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin) that the dataset configuration belongs to.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the dataset and dataset configuration. For example, `us-central1`.

     * `DATASET_CONFIG_ID` with the name of the dataset configuration you want to delete.

     * `SERVICE_ACCOUNT` with the service account. For example, `test-service-account@test-project.iam.gserviceaccount.com`.




## What's next

  * [View linked datasets](https://docs.cloud.google.com/bigquery/docs/analytics-hub-view-subscribe-listings#view-linked-datasets).
  * [Query a linked dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-view-subscribe-listings#query-linked-datasets).
  * [Analyze your stored data with Gemini Cloud Assist](https://docs.cloud.google.com/storage/docs/analyze-data-gemini-cloud-assist).
  * [Check the CEL filters reference for batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
