---
url: https://docs.cloud.google.com/storage/docs/insights/configure-datasets/
title: Configure Storage Insights datasets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:26.523545+00:00
---

# Configure Storage Insights datasets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/configure-datasets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Configure Storage Insights datasets Stay organized with collections  Save and categorize content based on your preferences. 

You can configure [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets) to collect and analyze metadata and activity data from your Cloud Storage buckets and objects. Use the insights generated from these datasets to help identify opportunities for cost optimization, perform security audits, and support operational monitoring. This document shows you how to configure Storage Insights datasets.

## Before you begin

Before you configure a dataset, complete the following steps.

### Get the required roles

To get the permissions that you need to configure datasets, ask your administrator to grant you the following IAM roles on your source projects: 

  * To configure a dataset: [Storage Insights Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storageinsights#storageinsights.admin) (`roles/storageinsights.admin`) 
  * To link a dataset: 
    * [Storage Insights Analyst ](https://docs.cloud.google.com/iam/docs/roles-permissions/storageinsights#storageinsights.analyst) (`roles/storageinsights.analyst`)
    * [BigQuery Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure datasets. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure datasets:

  * Configure a dataset: 
    * `storageinsights.datasetConfigs.create`
    * `storage.buckets.getObjectInsights`
  * Link to BigQuery dataset: `storageinsights.datasetConfigs.linkDataset`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable the Storage Insights API

### Console

[Enable the storageinsights.googleapis.com API](https://console.cloud.google.com/apis/library/storageinsights.googleapis.com)

### Command line

To enable the Storage Insights API in your current project, run the [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command:
    
    
    gcloud services enable storageinsights.googleapis.com

For more information about enabling services for a Google Cloud project, see [Enabling and disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#gcloud).

### Configure Storage Intelligence

Ensure that [Storage Intelligence is configured](https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence) for the project, folder, or organization that you want to analyze with datasets.

## Create a dataset configuration

To create a dataset configuration, follow these steps. For more information about the fields you can specify for the dataset configuration, see [Dataset configuration properties](https://docs.cloud.google.com/storage/docs/insights/datasets#dataset-config).

**Note:** It can take up to 48 hours for the first data to appear as a linked dataset in BigQuery after you configure the dataset and link it to BigQuery. Data for any newly added objects or buckets are included in the next daily snapshot. New activity data is typically included within four hours of the activity; however, latency might occasionally be higher due to high data volume.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Storage Insights** page.  


[Go to Storage Insights](https://console.cloud.google.com/storage/storageinsights)

  2. Click **Configure dataset**.

  3. In the **Name your dataset** section, enter a name for your dataset. Optionally, enter a description for the dataset. Names identify dataset configurations and are immutable. The name can contain up to 128 characters, including letters, numbers, and underscores, and must start with a letter.

  4. In the **Define dataset scope** section, do the following:

     * Select one of the following options:

       * To get storage metadata for all projects in the current organization, select **Include the organization**.

       * To get storage metadata for all projects in the selected folders, select **Include folders (Sub-organization/departments)**. For information about getting folder IDs, see [Viewing or listing folders and projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). To add folders:

         1. In the **Folder 1** field, enter the folder ID.
         2. Optionally, to add multiple folder IDs, click **\+ Add another folder**.
       * To get storage metadata for the selected projects, select **Include projects by providing project numbers**. To learn how to find project numbers, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). To add projects, do the following:

         1. In the **Project 1** field, enter the project number.
         2. Optionally, to add multiple project numbers, click **\+ Add another project**.
       * To add projects or folders in bulk, select **Upload a list of projects/folders via CSV file**. The CSV file must contain the project numbers or folder IDs to include in the dataset. You can specify up to 10,000 projects or folders in one dataset configuration.

     * Specify whether to automatically include future buckets in the selected resource.

     * Optionally, to specify filters on buckets based on regions and bucket prefixes, expand the **Filters (optional)** section. Filters are applied additively on buckets.

You can include or exclude buckets from specific regions. For example, you can exclude buckets in the `me-central1` and `me-central2` regions. You can also include or exclude buckets by prefix. For example, to exclude buckets that start with `my-bucket`, enter the `my-bucket*` prefix.

  5. Click **Continue**.

  6. In the **Select retention period** section, select a [retention period](https://docs.cloud.google.com/storage/docs/insights/datasets#Retention-period-for-dataset) for the data in the dataset.

  7. [Activity data](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#activity-data-schema) is included in the dataset by default, and inherits the retention period of the dataset. To override the dataset retention period, select **Specify a retention period for activity data** , and then select the number of days to retain activity data for. To disable activity data, set the retention period to `0` days.

  8. In the **Select location to store configured dataset** section, select a [location](https://docs.cloud.google.com/bigquery/docs/locations) to store the linked dataset. For example, `us-central1`.

The linked dataset must be in a location supported by BigQuery, although source buckets can be in any Cloud Storage location.

  9. In the **Select service account type** section, select a service agent type for your dataset. Choose either a [configuration-scoped or project-scoped service agent](https://docs.cloud.google.com/storage/docs/insights/datasets#Service-agent-type) for your dataset.

  10. Click **Configure**.




### Command line

  1. To create a dataset configuration, run the [`gcloud storage insights dataset-configs create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/insights/dataset-configs/create) command with the required flags:
         
         gcloud storage insights dataset-configs create DATASET_CONFIG_ID \
           --location=LOCATION \
           --organization=SOURCE_ORG_NUMBER \
           --retention-period-days=DATASET_RETENTION_PERIOD_DAYS \
           (SCOPE_FLAG)
         

Replace:

     * `DATASET_CONFIG_ID` with the name for your dataset configuration. Names identify dataset configurations and are immutable. The name can contain up to 128 characters, including letters, numbers, and underscores, and must start with a letter.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) to store the linked dataset. For example, `us-central1`.

The linked dataset must be in a location supported by BigQuery, although source buckets can be in any Cloud Storage location.

     * `SOURCE_ORG_NUMBER` with the ID of the [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) to which the source projects belong. To find your organization ID, see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

     * `DATASET_RETENTION_PERIOD_DAYS` with the retention period for the data in the dataset.

     * `SCOPE_FLAG` with any one of the following flags that defines the scope of the data to collect:

       * `--enable-organization-scope`: Enables the dataset to collect insights from all buckets within the organization.
       * `--source-folders=[SOURCE_FOLDER_NUMBERS,...]`: Specifies a list of folder numbers to include in the dataset. To learn how to find a folder number, see [Listing all projects and folders in your hierarchy](https://docs.cloud.google.com/resource-manager/docs/listing-all-resources).
       * `--source-folders-file=FILE_PATH`: Specifies multiple folder numbers by uploading a CSV file to a bucket.
       * `--source-projects=[SOURCE_PROJECT_NUMBERS,...]`: Specifies a list of project numbers to include in the dataset. For example, `464036093014`. To find your project number, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
       * `--source-projects-file=FILE_PATH`: Specifies multiple project numbers by uploading a CSV file to a bucket.

Optionally, use the following additional flags to configure the dataset:

     * Use `--include-buckets=BUCKET_NAMES_OR_REGEX` to include specific buckets by name or regular expression. You can't use this flag with `--exclude-buckets`.

     * Use `--exclude-buckets=BUCKET_NAMES_OR_REGEX` to exclude specific buckets by name or regular expression. You can't use this flag with `--include-buckets`.

     * Use `--project=DESTINATION_PROJECT_ID` to specify a project for storing your dataset configuration and generated dataset. If you don't use this flag, the destination project is your active project. For more information about project IDs, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

     * Use `--auto-add-new-buckets` to automatically include any buckets added to source projects in the future.

     * Use `--skip-verification` to skip checks and failures from the verification process, which includes checks for required IAM permissions. If you use this flag, some or all buckets might be excluded from the dataset.

     * Use `--identity=IDENTITY_TYPE` to specify the scope of the service agent created with the dataset configuration. Values are `IDENTITY_TYPE_PER_CONFIG` or `IDENTITY_TYPE_PER_PROJECT`. If unspecified, the default is `IDENTITY_TYPE_PER_CONFIG`. For details, see [Service agent type](https://docs.cloud.google.com/storage/docs/insights/datasets#Service-agent-type).

     * Use `--description=DESCRIPTION` to add a description for the dataset configuration.

     * Use `--activity-data-retention-period-days=ACTIVITY_RETENTION_PERIOD_DAYS` to specify the retention period for the [activity data](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#activity-data-schema) in the dataset. By default, activity data is included in the dataset, and inherits the retention period of the dataset. To override the dataset retention period, specify the number of days to retain activity data for. To exclude activity data, set the ACTIVITY_RETENTION_PERIOD_DAYS to `0`.

The following example creates a dataset configuration named `my-dataset` in the `us-central1` region, for the organization with the ID `123456789`, with a retention period of `30` days, and a scope limited to the projects `987654321` and `123123123`:
    
    gcloud storage insights dataset-configs create my-dataset \
    --location=us-central1 \
    --organization=123456789 \
    --retention-period-days=30 \
    --source-projects=987654321,123123123
    




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "sourceProjects": {
             "project_numbers": ["PROJECT_NUMBERS", ...]
           },
           "retentionPeriodDays": "RETENTION_PERIOD_DAYS",
           "activityDataRetentionPeriodDays": "ACTIVITY_DATA_RETENTION_PERIOD_DAYS",
           "identity": {
             "type": "IDENTITY_TYPE"
           }
         }

Replace:

     * `PROJECT_NUMBERS` with the [numbers of the projects](https://docs.cloud.google.com/docs/overview#projects) you want to include in the dataset. You can specify one project or multiple projects. Projects must be specified as a list of strings.

Alternatively, you can add an organization, or one or multiple folders that contain buckets and objects for which you want to update the metadata. To include folders or organizations, use the `sourceFolders` or `organizationScope` fields. For more information, see the [`DatasetConfig`](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#DatasetConfig) reference.

     * `RETENTION_PERIOD_DAYS` with the number of days of data to capture in the dataset snapshot. For example, `90`.

     * `ACTIVITY_DATA_RETENTION_PERIOD_DAYS` with the number of days of [activity data](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#activity-data-schema) to capture in the dataset snapshot. By default, activity data is included in the dataset, and inherits the retention period of the dataset. To override the dataset retention period, specify the number of days to retain activity data for. To exclude activity data, set the ACTIVITY_RETENTION_PERIOD_DAYS to `0`.

     * `IDENTITY_TYPE` with the type of service account that gets created alongside the dataset configuration. Values are `IDENTITY_TYPE_PER_CONFIG` or `IDENTITY_TYPE_PER_PROJECT`. For details, see [Service agent type](https://docs.cloud.google.com/storage/docs/insights/datasets#Service-agent-type).

  3. To create the dataset configuration, use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Create` DatasetConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/create) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
         "https://storageinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasetConfigs?datasetConfigId=DATASET_CONFIG_ID" \
           --header "Authorization: Bearer $(gcloud auth print-access-token --impersonate-service-account=SERVICE_ACCOUNT)" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json"

Replace:

     * `JSON_FILE_NAME` with the path to the JSON file you created in the previous step. Alternatively, you can pass an instance of [`DatasetConfig`](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#DatasetConfig) in the request body.

     * `PROJECT_ID` with the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin) that the dataset configuration and dataset will belong to.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) where the dataset and dataset configuration will reside. For example, `us-central1`.

     * `DATASET_CONFIG_ID` with the name of your dataset configuration. Names identify dataset configurations and are immutable. The name can contain up to 128 characters, including letters, numbers, and underscores, and must start with a letter.

     * `SERVICE_ACCOUNT` with the service account. For example, `test-service-account@test-project.iam.gserviceaccount.com`.




To troubleshoot snapshot processing errors that are logged in `error_attributes_view`, see [Storage Insights dataset errors](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#troubleshoot-error-codes).

## Grant the required permissions to the service agent

Google Cloud creates a [configuration-scoped or project-scoped service agent](https://docs.cloud.google.com/storage/docs/insights/datasets#Service-agent-type) when you create a dataset configuration. The service agent follows the naming format `service-PROJECT_NUMBER@gcp-sa-storageinsights.iam.gserviceaccount.com` and appears on the [IAM page in the Google Cloud console](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId) when you select the **Include Google-provided role grants** checkbox. You can also find the name of the service agent by [viewing the `DatasetConfig` resource](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#DatasetConfig) using the JSON API.

To enable Storage Insights to generate and write datasets, ask your administrator to grant the service agent the Storage Insights Collector Service role (`roles/storage.insightsCollectorService`) on the organization that contains the source projects. You must grant this role to every configuration-scoped service agent created for each dataset configuration from which you want data. If you use a project-scoped service agent, you must grant this role only once on the service agent to read and write datasets for all dataset configurations within the project.

For instructions about granting roles for projects, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Link a dataset

To link a dataset to BigQuery, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Storage Insights** page.  


[Go to Storage Insights](https://console.cloud.google.com/storage/storageinsights)

  2. Click the name of the dataset configuration that generated the dataset you want to link.

  3. In the **BigQuery linked dataset** section, click **Link dataset** to link your dataset.




### Command line

  1. To link a dataset to BigQuery, run the [`gcloud storage insights dataset-configs create-link`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/insights/dataset-configs/create-link) command:
         
         gcloud storage insights dataset-configs create-link DATASET_CONFIG_ID --location=LOCATION

Replace:

     * `DATASET_CONFIG_ID` with the name of the dataset configuration that generated the dataset to link.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the dataset. For example, `us-central1`.

You can also specify a full dataset configuration path. For example:
    
    gcloud storage insights dataset-configs create-link projects/DESTINATION_PROJECT_ID/locations/LOCATION/datasetConfigs/DATASET_CONFIG_ID

Replace:

     * `DESTINATION_PROJECT_ID` with the ID of the project that contains the dataset configuration. For more information about project IDs, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

     * `DATASET_CONFIG_ID` with the name of the dataset configuration that generated the dataset to link.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) of your dataset and dataset configuration. For example, `us-central1`.




### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`linkDataset` DatasetConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/linkDataset) request:
         
         curl -X POST \
           "https://storageinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasetConfigsDATASET_CONFIG_ID:linkDataset?" \
             --header "Authorization: Bearer $(gcloud auth print-access-token --impersonate-service-account=SERVICE_ACCOUNT)" \
             --header "Accept: application/json" \
             --header "Content-Type: application/json"
         

Replace:

     * `JSON_FILE_NAME` with the path to the JSON file you created.

     * `PROJECT_ID` with the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin) to which the dataset configuration belongs.

     * `LOCATION` with the [location](https://docs.cloud.google.com/bigquery/docs/locations) where the dataset and dataset configuration reside. For example, `us-central1`.

     * `DATASET_CONFIG_ID` with the name of the dataset configuration that generated the dataset to link.

     * `SERVICE_ACCOUNT` with the service account. For example, `test-service-account@test-project.iam.gserviceaccount.com`.




## Analyze object data and metadata using BigQuery

To analyze object content or view object metadata, use the [`ref`](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#ref) column, which is returned as part of an Storage Insights dataset, to run [BigQuery `ObjectRef` functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/objectref_functions). Complete the steps in the following sections.

### Create a Cloud resource connection in BigQuery

In BigQuery, create a Cloud resource connection that accesses Cloud Storage. The Cloud resource connection lets BigQuery access Cloud Storage object data and metadata using its own service account. For details, see [Create a Cloud resource connection](https://docs.cloud.google.com/bigquery/docs/create-cloud-resource-connection).

### Use the Cloud resource connection with Storage Insights dataset

To analyze data referenced in the `ref` column that is returned as part of a Storage Insights dataset, use the `OBJ.MAKE_REF` function to combine the `URI` from the `ref` column with the connection that you created:
    
    
    SELECT
    OBJ.GET_ACCESS_URL(OBJ.MAKE_REF(ref.uri, "CONNECTION_ID"), "r")
    FROM `PROJECT_ID.INSIGHTS_DATASET.object_attributes_view` WHERE LOCATION = "US";

Replace:

  * `CONNECTION_ID`: the ID of the Cloud resource connection you created.
  * `PROJECT_ID`: the ID of the project that contains the Storage Insights dataset.
  * `INSIGHTS_DATASET`: the name of the Storage Insights dataset. For example, `storageinsights_dataset`.

**Note:** `ObjectRef` queries might incur Cloud Storage operations costs, BigQuery functions costs, and BigQuery query costs. For more information, see [BigQuery pricing](https://cloud.google.com/bigquery/pricing) and [Cloud Storage pricing](https://cloud.google.com/storage/pricing).

### Analyze a Storage Insights dataset using a custom model

BigQuery doesn't support creating models directly within a linked dataset. To analyze your Storage Insights data with a custom model, you must create and store the model in a standard BigQuery dataset. You can then reference that model in your queries while targeting the linked dataset for analysis:

  1. Create a model in a BigQuery dataset (`MODEL_DATASET`) in the same project as your linked dataset (`INSIGHTS_DATASET`):
         
         CREATE OR REPLACE MODEL `MODEL_DATASET.gemini_model`
         REMOTE WITH CONNECTION `CONNECTION_ID`
         OPTIONS (ENDPOINT = 'gemini-2.0-flash');

Replace:

     * `MODEL_DATASET`: the name of the dataset where you want to create the model.
     * `CONNECTION_ID`: the ID of the Cloud resource connection you created.
  2. Run a query that references the model to analyze the data in your Storage Insights dataset. The following example adds a description for images in the dataset:
         
         SELECT
          name,
          result AS ai_description
         FROM
          AI.GENERATE_TEXT(
            MODEL `MODEL_DATASET.gemini_model`,
            (
              SELECT
                name,
                (
                  'Describe this image',
                  OBJ.GET_ACCESS_URL(
                    OBJ.FETCH_METADATA(
                      OBJ.MAKE_REF(
                        ref.uri,
                        'CONNECTION_ID'
                      )
                    ),
                    'r'
                  )
                ) AS prompt
              FROM
                `INSIGHTS_DATASET.object_attributes_view`
              WHERE
                contentType LIKE 'image/%'
                AND NOT name LIKE '%/'
              LIMIT 3
            )
          );

Replace:

     * `INSIGHTS_DATASET`: the name of the Storage Insights dataset.
     * `MODEL_DATASET`: the name of the dataset where you created the model.
     * `CONNECTION_ID`: the ID of the Cloud resource connection you created.



### Analyze a Storage Insights dataset using a default model

You can use a default model to generate insights from unstructured data and help detect sensitive information.

#### Generate insights from unstructured data

The following example query generates descriptions for JPEG images:
    
    
    SELECT AI.GENERATE(
       (
         'Return a JSON object with fields: "description" (max 20 words)',
         OBJ.GET_ACCESS_URL(
           OBJ.MAKE_REF(ref.uri, `CONNECTION_ID`),
           'r'
         )
       )
    )
    FROM  `PROJECT_ID.INSIGHTS_DATASET.object_attributes_view`
    WHERE  name LIKE 'returns/electronics/%'
      AND contentType = 'image/jpeg';

Replace:

  * `CONNECTION_ID`: the ID of the Cloud resource connection you created.
  * `PROJECT_ID`: the ID of the project that contains the Storage Insights dataset.
  * `INSIGHTS_DATASET`: the name of the Storage Insights dataset.



#### Automated sensitive data detection

You can use multimodal models to help detect sensitive data, such as personally identifiable information (PII), in your documents.

The following query shows how you can scan PDF documents to check for sensitive information:
    
    
    SELECT AI.GENERATE(
       (
         'Does this document contain any credit card numbers or home addresses? Answer "SAFE" or "SENSITIVE".',
         OBJ.GET_ACCESS_URL(
           OBJ.MAKE_REF(ref.uri, `CONNECTION_ID`),
           'r'
         )
       )
    )
    FROM  `PROJECT_ID.INSIGHTS_DATASET.object_attributes_view`
    WHERE contentType = 'application/pdf';

Replace:

  * `CONNECTION_ID`: the ID of the Cloud resource connection you created.
  * `PROJECT_ID`: the ID of the project that contains the Storage Insights dataset.
  * `INSIGHTS_DATASET`: the name of the Storage Insights dataset.



### Analyze object contexts

If your dataset includes the [`object_contexts_catalog_view`](https://docs.cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#object-contexts-catalog-schema), you can query [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts) and [extended data](https://docs.cloud.google.com/storage/docs/object-contexts#extended-data) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) (such as labels, face detections, and bounding boxes) directly in BigQuery.

#### Image labeling: Find objects with a specific label

The following query finds images annotated with a specific label having a confidence score greater than 0.75:
    
    
    SELECT
      t.project,
      t.bucket,
      t.name,
      t.generation,
      label
    FROM
      `PROJECT_ID.INSIGHTS_DATASET.object_contexts_catalog_view` AS t,
      UNNEST(t.contexts) AS context,
      UNNEST(JSON_QUERY_ARRAY(context.extendedData.labelAnnotationGroup.labelAnnotations)) AS label
    WHERE
      context.key = "google:annotation:label-detector-v1"
      AND LOWER(STRING(label.description)) = 'LABEL_DESCRIPTION'
      AND FLOAT64(label.score) > 0.75;

Replace:

  * `PROJECT_ID`: the ID of the project that contains the Storage Insights dataset.
  * `INSIGHTS_DATASET`: the name of the Storage Insights dataset.
  * `LABEL_DESCRIPTION`: the label description to search for (for example, `car` or `clothing`).



#### Face detection: Find smiling photos

The following query filters for images containing faces where the joy probability is greater than 0.5:
    
    
    WITH
      face_stats AS (
        SELECT
          t.project,
          t.bucket,
          t.name,
          t.generation,
          FLOAT64(face.joyProbability) AS joy_probability,
          FLOAT64(face.rollAngle) AS roll_angle,
          FLOAT64(face.panAngle) AS pan_angle,
          FLOAT64(face.tiltAngle) AS tilt_angle
        FROM
          `PROJECT_ID.INSIGHTS_DATASET.object_contexts_catalog_view` AS t,
          UNNEST(t.contexts) AS context,
          UNNEST(JSON_QUERY_ARRAY(context.extendedData.faceAnnotationGroup.faceAnnotations)) AS face
        WHERE context.key = 'google:annotation:face-detector-v1'
      )
    SELECT *
    FROM face_stats
    WHERE
      joy_probability > 0.5
      AND roll_angle BETWEEN -10 AND 10
      AND pan_angle BETWEEN -10 AND 10
      AND tilt_angle BETWEEN -10 AND 10
    LIMIT 10;

Replace:

  * `PROJECT_ID`: the ID of the project that contains the Storage Insights dataset.
  * `INSIGHTS_DATASET`: the name of the Storage Insights dataset.



#### Object detection: Find bounding box coordinates for detected objects

The following query extracts bounding box coordinates for objects detected with a confidence score greater than 0.50:
    
    
    SELECT
      t.project,
      t.bucket,
      t.name AS object_name,
      t.generation,
      STRING(object.name) AS detected_object_name,
      FLOAT64(object.score) AS confidence_score,
      (
        SELECT AS STRUCT
          MIN(FLOAT64(v.x)) AS x_min,
          MIN(FLOAT64(v.y)) AS y_min,
          MAX(FLOAT64(v.x)) AS x_max,
          MAX(FLOAT64(v.y)) AS y_max
        FROM UNNEST(JSON_QUERY_ARRAY(object.boundingPoly.normalizedVertices)) AS v
      ).*
    FROM
      `PROJECT_ID.INSIGHTS_DATASET.object_contexts_catalog_view` AS t,
      UNNEST(t.contexts) AS context,
      UNNEST(JSON_QUERY_ARRAY(context.extendedData.objectAnnotationGroup.objectAnnotations)) AS object
    WHERE
      context.key = 'google:annotation:object-detector-v1'
      AND LOWER(STRING(object.name)) = 'DETECTED_OBJECT_NAME'
      AND FLOAT64(object.score) > 0.50
    LIMIT 20;

Replace:

  * `PROJECT_ID`: the ID of the project that contains the Storage Insights dataset.
  * `INSIGHTS_DATASET`: the name of the Storage Insights dataset.
  * `DETECTED_OBJECT_NAME`: the name of the detected object class to search for (for example, `drink` or `car`).



## What's next

  * [View linked datasets](https://docs.cloud.google.com/bigquery/docs/analytics-hub-view-subscribe-listings#view-linked-datasets).
  * [Query a linked dataset](https://docs.cloud.google.com/bigquery/docs/analytics-hub-view-subscribe-listings#query-linked-datasets).
  * [Analyze your stored data with Gemini Cloud Assist](https://docs.cloud.google.com/storage/docs/analyze-data-gemini-cloud-assist).
  * [Manage your dataset configurations](https://docs.cloud.google.com/storage/docs/insights/manage-datasets).
  * [Check the CEL filters reference for batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/cel-filters-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
