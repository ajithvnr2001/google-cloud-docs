---
url: https://docs.cloud.google.com/storage/docs/object-enrichments/configure-object-enrichments/
title: Configure object enrichments \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:30.588395+00:00
---

# Configure object enrichments  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/object-enrichments/configure-object-enrichments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Configure object enrichments Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To generate structured metadata for images and PDF documents in your Cloud Storage buckets, create a [feature configuration (`FeatureConfig`)](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs) resource. You must also authorize the object enrichments service agent to access your data. After you configure object enrichments, Cloud Storage evaluates matching objects with your chosen machine learning models asynchronously and attaches the results directly to your objects as [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts).

This page explains how to create, list, view, update, and delete feature configurations. It also explains how to grant the required Identity and Access Management (IAM) permissions to the service agent.

The complete workflow involves the following steps:

  1. Create a feature configuration (`FeatureConfig`) resource to define your scope and select models.
  2. Authorize the service agent to access your storage buckets.
  3. [View and manage enrichment metadata on your objects](https://docs.cloud.google.com/storage/docs/object-enrichments/manage-object-enrichments).
  4. [Analyze your enrichments in bulk by using SQL in BigQuery](https://docs.cloud.google.com/storage/docs/object-enrichments/analyze-bigquery).
  5. Update or delete feature configurations as your workload evolves.



For conceptual details and supported use cases, see the [object enrichments overview](https://docs.cloud.google.com/storage/docs/object-enrichments/overview).

## Before you begin

Before you configure object enrichments, complete the following setup steps:

### Get the required roles

To get the permissions that you need to create and manage feature configurations, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage feature configurations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage feature configurations:

  * `storage.featureConfigs.create`
  * `storage.featureConfigs.list`
  * `storage.featureConfigs.get`
  * `storage.featureConfigs.update`
  * `storage.featureConfigs.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### (Optional) Prepare Storage Insights datasets for SQL analysis

If you plan to query and analyze enrichment metadata across millions of objects by using SQL in BigQuery, you must first [configure Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets). Storage Insights datasets automatically export your object contexts directly into queryable BigQuery tables.

If you only want to inspect individual objects by using the Google Cloud console, the Google Cloud CLI, or an API, you can skip this step.

## Create a feature configuration

A feature configuration (`FeatureConfig`) specifies which storage buckets Cloud Storage monitors and which machine learning models evaluate your objects. Specify exact bucket names in your configuration; object enrichments doesn't support regular expressions or wildcards. If you create, recreate (delete and create again), or relocate buckets after creating a configuration, you must update your feature configuration to include them. For more information, see [Configuration and scope management](https://docs.cloud.google.com/storage/docs/object-enrichments/overview#scope-management).

**Note:** Changes to a feature configuration (`FeatureConfig`) propagate asynchronously. Creating or updating a configuration can take up to 24 hours to take effect. During this propagation period, Cloud Storage might continue to process objects based on the previous configuration. However, deleting a configuration typically takes effect within a few minutes.

You can create a feature configuration by using the Google Cloud console, the Google Cloud CLI, or the JSON API.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Object enrichments** page.

[Go to Object enrichments](https://console.cloud.google.com/storage/smart-storage/object-enrichments)

  2. Click **Create**.

  3. In the **Define source** step, specify the configuration name and target buckets:

     1. In the **Name** field, enter a unique name for the feature configuration. The name must be 1–63 characters and contain only lowercase letters, numbers, or hyphens. It must start with a lowercase letter and can't end with a hyphen. You can't change this name after creating the configuration.
     2. Optional: To help identify the configuration, enter a description (up to 256 characters) in the **Description** field.
     3. To specify the buckets that you want to enrich, enter one or more bucket names separated by commas or spaces in the **Bucket Names** field. Alternatively, click **Browse** , select a bucket, and then click **Select**.
     4. Click **Continue**.
  4. In the **Select models** step, select the checkboxes for one or more machine learning models that you want to enable, and then click **Continue** :

     * **Image Object Detection** (`object-detector`): Identifies and locates multiple objects within an image.
     * **Image Face Detection** (`face-detector`): Detects human faces and their attributes within images.
     * **Image Labeling** (`label-detector`): Assigns labels to images based on their content.
     * **Image Explicit Content Detection** (`content-safety`): Detects adult, violent, or other sensitive content.
     * **PDF Classification** (`pdf-classification`): Identifies the document subject-matter category.

For details about each model and its output schema, see [Supported models and schemas](https://docs.cloud.google.com/storage/docs/object-enrichments/models).

  5. In the **Select processing location** step, from the **Processing location** menu, select a multi-region location (**us** , **eu** , or **asia**), and then click **Continue**.

  6. In the **Grant required permissions** step, choose how to grant the required IAM roles to the object enrichments service agent:

     * **Grant project-wide permission** : Automatically grants the service agent the required roles (`roles/storage.annotationGeneratorService` and `roles/storage.bucketViewer`) to process all current and future Cloud Storage buckets in the project. Selecting this option requires the `resourcemanager.projects.setIamPolicy` permission on the project. If you don't have this permission, the option is unavailable.
     * **Manually provide grant permission later** : Creates the configuration without granting permissions immediately. You must grant permissions to the service agent before Cloud Storage can process objects.
  7. Click **Create**.

Creating a feature configuration starts a long-running operation. When the operation completes, the Google Cloud console opens the configuration details page. If you selected **Grant project-wide permission** , the Google Cloud console applies the IAM policy bindings after creating the configuration.




### Command line

To create a feature configuration, use the [`gcloud alpha storage feature-configs create`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/feature-configs/create) command:
    
    
    gcloud alpha storage feature-configs create FEATURE_CONFIG_ID \
        --description="DESCRIPTION" \
        --auto-annotate-models=MODELS \
        --auto-annotate-processing-location=PROCESSING_LOCATION \
        --include-bucket-id-regexes=BUCKET_NAME

Where:

  * `FEATURE_CONFIG_ID` is a unique ID for your feature configuration. Must be 1–63 characters, start with a lowercase letter, and contain only lowercase letters, numbers, or hyphens. Can't end with a hyphen.
  * `DESCRIPTION` is an optional description for the feature configuration. For example, `Scan invoices and receipts`.
  * `MODELS` is a comma-separated list of the machine learning models to enable: `face-detector`, `object-detector`, `label-detector`, `content-safety`, or `pdf-classification`. For details about each model and its output schema, see [Supported models and schemas](https://docs.cloud.google.com/storage/docs/object-enrichments/models).
  * `PROCESSING_LOCATION` is the multi-regional processing location where data processing occurs. Supported values are `us`, `eu`, or `asia`.
  * `BUCKET_NAME` is the exact name of a bucket to include in this configuration. You can specify a comma-separated list of exact bucket names.



### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the feature configuration:
         
         {
           "description": "DESCRIPTION",
           "autoAnnotateConfig": {
             "models": [
               { "name": "MODEL_NAME" }
             ],
             "processingLocation": "PROCESSING_LOCATION"
           },
           "filter": {
             "includedCloudStorageBuckets": {
               "bucketIdRegexes": [
                 "BUCKET_NAME"
               ]
             }
           }
         }

Where:

     * `DESCRIPTION` is an optional description for the feature configuration. For example, `Scan invoices and receipts`.

     * `MODEL_NAME` is the name of a machine learning model to enable: `face-detector`, `object-detector`, `label-detector`, `content-safety`, or `pdf-classification`. For details about each model and its output schema, see [Supported models and schemas](https://docs.cloud.google.com/storage/docs/object-enrichments/models). To enable multiple models, add additional model objects to the `models` array.

     * `PROCESSING_LOCATION` is the multi-regional processing location where data processing occurs. Supported values are `us`, `eu`, or `asia`.

     * `BUCKET_NAME` is the exact name of a bucket to include in the configuration. For example, `my-bucket`. To include multiple buckets, specify additional bucket name strings in the `bucketIdRegexes` array.

  3. Use [`cURL`](https://curl.se/) to send a [`featureConfigs.create` request](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/create) to the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/featureConfigs?featureConfigId=FEATURE_CONFIG_ID"

Where:

     * `JSON_FILE_NAME` is the path to the JSON file that you created in the previous step. For example, `config.json`.
     * `PROJECT_ID` is your Google Cloud project ID. For example, `my-project`.
     * `FEATURE_CONFIG_ID` is a unique ID for your feature configuration. For example, `my-feature-config`. Must be 1–63 characters, start with a lowercase letter, and contain only lowercase letters, numbers, or hyphens. Can't end with a hyphen.
  4. Optional: To check the status of the [long-running operation](https://docs.cloud.google.com/storage/docs/using-long-running-operations) for creating the feature configuration, use [`cURL`](https://curl.se/) to send an [`operations.get` request](https://docs.cloud.google.com/storage/docs/json_api/v1/operations/get) to the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/operations/OPERATION_ID"

Where:

     * `PROJECT_ID` is your Google Cloud project ID. For example, `my-project`.
     * `OPERATION_ID` is the operation ID returned in the creation response.
  5. Optional: To list all active and historical operations, use [`cURL`](https://curl.se/) to send an `operations.list` request to the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/operations"

Where `PROJECT_ID` is your Google Cloud project ID. For example, `my-project`.




## Grant permissions to the service agent

When you create a feature configuration, Google Cloud provisions a dedicated service agent for your project: `service-PROJECT_NUMBER@gcp-sa-autoannotate.iam.gserviceaccount.com`.

To let this service agent scan your buckets, read unstructured objects, and attach enrichment metadata, you must grant it the required IAM roles.

### Console

If you selected **Manually provide grant permission later** when creating a feature configuration, or if you need to reapply project-wide permissions, you can grant permissions from the configuration details page:

  1. In the Google Cloud console, go to the Cloud Storage **Object enrichments** page.

[Go to Object enrichments](https://console.cloud.google.com/storage/smart-storage/object-enrichments)

  2. In the **Configuration Name** column, click the name of the feature configuration.

  3. In the action bar, click **Grant permissions**.

  4. In the **Grant permissions** pane, click **Grant project-wide permissions**.

This action grants the service agent the **Storage Annotation Generator Service** (`roles/storage.annotationGeneratorService`) and **Storage Bucket Viewer** (`roles/storage.bucketViewer`) roles on the project. Granting project-wide permissions in the Google Cloud console requires the `resourcemanager.projects.setIamPolicy` permission on the project.

To grant the `roles/storage.annotationGeneratorService` role on individual buckets instead of the entire project, use the Google Cloud CLI.




### Command line

  1. Grant the **Storage Annotation Generator Service** (`roles/storage.annotationGeneratorService`) role to the service agent on each monitored bucket or at the project level:

     * To grant the role on a specific bucket, use the [`gcloud storage buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) command:
           
           gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
               --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-autoannotate.iam.gserviceaccount.com \
               --role=roles/storage.annotationGeneratorService

Where:

       * `BUCKET_NAME` is the name of the bucket where you want to grant permissions.
       * `PROJECT_NUMBER` is your Google Cloud project number.
     * To grant the role across all buckets in your project, use the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
           
           gcloud projects add-iam-policy-binding PROJECT_ID \
               --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-autoannotate.iam.gserviceaccount.com \
               --role=roles/storage.annotationGeneratorService

Where:

       * `PROJECT_ID` is your Google Cloud project ID.
       * `PROJECT_NUMBER` is your Google Cloud project number.
  2. To grant the **Storage Bucket Viewer** (`roles/storage.bucketViewer`) role at the project level so the service agent can inspect bucket configurations, use the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-autoannotate.iam.gserviceaccount.com \
             --role=roles/storage.bucketViewer

Where:

     * `PROJECT_ID` is your Google Cloud project ID.
     * `PROJECT_NUMBER` is your Google Cloud project number.



After you grant roles, IAM permissions might take a few minutes to propagate before asynchronous processing begins.

## List all feature configurations

To list all feature configurations in your project, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Object enrichments** page.

[Go to Object enrichments](https://console.cloud.google.com/storage/smart-storage/object-enrichments)

The **Configuration** tab lists all feature configurations in your project, including their enabled models, processing location, scope, bucket filters, creation date, and last updated date.

  2. Optional: To filter the list, enter a property name or value in the **Filter** field.




### Command line

Use the [`gcloud alpha storage feature-configs list`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/feature-configs/list) command:
    
    
    gcloud alpha storage feature-configs list

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.se/) to send a [`featureConfigs.list` request](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/list) to the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Accept: application/json" \
           "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/featureConfigs"

Where `PROJECT_ID` is the ID of your Google Cloud project. For example, `my-project`.




## View feature configuration details

To inspect the models, target buckets, and processing location of a specific feature configuration, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Object enrichments** page.

[Go to Object enrichments](https://console.cloud.google.com/storage/smart-storage/object-enrichments)

  2. In the **Configuration Name** column, click the name of the feature configuration that you want to inspect.

The configuration details page displays the configuration name, description, scope, included buckets, processing location, enabled models, creation date, and last updated date.




### Command line

Use the [`gcloud alpha storage feature-configs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/feature-configs/describe) command:
    
    
    gcloud alpha storage feature-configs describe FEATURE_CONFIG_ID

Replace `FEATURE_CONFIG_ID` with the ID of the feature configuration.

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.se/) to send a [`featureConfigs.get` request](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/get) to the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Accept: application/json" \
           "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/featureConfigs/FEATURE_CONFIG_ID"

Where:

     * `PROJECT_ID` is the ID of your Google Cloud project. For example, `my-project`.
     * `FEATURE_CONFIG_ID` is the ID of the feature configuration. For example, `my-feature-config`.



## Update a feature configuration

You can update an existing feature configuration to add or remove machine learning models, change target buckets, modify the processing location, or update the description.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Object enrichments** page.

[Go to Object enrichments](https://console.cloud.google.com/storage/smart-storage/object-enrichments)

  2. In the **Configuration Name** column, click the name of the feature configuration that you want to update.

  3. On the configuration details page, update the settings that you want to change:

     * To update the description, click edit **Edit configuration description** next to **Configuration description**. In the **Edit description** pane, update the text in the **Description** field, and then click **Save**.
     * To update the bucket scope, click edit **Edit configuration scope** next to **Configuration scope**. In the **Define scope** step, add or remove target buckets in the **Bucket Names** field, and then click **Continue**. In the **Grant required permissions** step, select a permission option for the service agent, and then click **Save**.
     * To update the processing location, click edit **Edit configuration processing location** next to **Processing location**. In the **Edit processing location** pane, select a multi-region location (**us** , **eu** , or **asia**) from the **Processing location** menu, and then click **Save**.
     * To update the enabled models, click edit **Edit configuration enabled models** next to **Enabled models**. In the **Edit models** pane, select or clear the checkboxes for the models that you want to update, and then click **Save**.



### Command line

Use the [`gcloud alpha storage feature-configs update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/feature-configs/update) command to update the description, models, processing location, or bucket filters:
    
    
    gcloud alpha storage feature-configs update FEATURE_CONFIG_ID \
        --description="DESCRIPTION" \
        --auto-annotate-models=MODELS \
        --auto-annotate-processing-location=PROCESSING_LOCATION \
        --include-bucket-id-regexes=BUCKET_NAME

Replace the following:

  * `FEATURE_CONFIG_ID`: The ID of the feature configuration you are updating.
  * `DESCRIPTION`: An optional description for the feature configuration. For example, `Scan invoices and receipts`.
  * `MODELS`: A comma-separated list of machine learning models to enable: `face-detector`, `object-detector`, `label-detector`, `content-safety`, or `pdf-classification`.
  * `PROCESSING_LOCATION`: The multi-regional processing location where data processing occurs. Valid values are `us`, `eu`, or `asia`.
  * `BUCKET_NAME`: A comma-separated list of exact bucket names to scan. Object enrichments doesn't support wildcards or regular expressions. If you create, recreate, or relocate buckets, you must update this list to include them.



### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings you want to update. For example, to update the description, enabled models, and target buckets:
         
         {
           "description": "DESCRIPTION",
           "autoAnnotateConfig": {
             "models": [
               { "name": "MODEL_NAME" }
             ],
             "processingLocation": "PROCESSING_LOCATION"
           },
           "filter": {
             "includedCloudStorageBuckets": {
               "bucketIdRegexes": [
                 "BUCKET_NAME"
               ]
             }
           }
         }

Where:

     * `DESCRIPTION` is an optional description for the feature configuration. For example, `Scan invoices and receipts`.

     * `MODEL_NAME` is the machine learning model to include: `face-detector`, `object-detector`, `label-detector`, `content-safety`, or `pdf-classification`. For details about each model and its output schema, see [Supported models and schemas](https://docs.cloud.google.com/storage/docs/object-enrichments/models). To enable multiple models, add additional model objects to the `models` array.

     * `PROCESSING_LOCATION` is the multi-regional processing location where data processing occurs. Valid values are `us`, `eu`, or `asia`.

     * `BUCKET_NAME` is the exact name of a bucket to include in the scan. For example, `my-bucket`. Object enrichments doesn't support regular expressions or wildcards. If you create, recreate, or relocate buckets, you must update this list to include them. To include multiple buckets, specify additional bucket name strings in the `bucketIdRegexes` array.

  3. Use [`cURL`](https://curl.se/) to send a [`featureConfigs.patch` request](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/patch) to the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -H "Accept: application/json" \
           "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/featureConfigs/FEATURE_CONFIG_ID?updateMask=UPDATE_MASK"

Where:

     * `JSON_FILE_NAME` is the local path to your JSON request file that you created in Step 2. For example, `update.json`.
     * `PROJECT_ID` is the ID of your Google Cloud project. For example, `my-project`.
     * `FEATURE_CONFIG_ID` is the ID of the feature configuration to update. For example, `my-feature-config`.
     * `UPDATE_MASK` is a comma-separated list of fields that you want to update, such as `description,filter` or `autoAnnotateConfig.models`. For syntax rules, see [`FieldMask`](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask).



## Delete a feature configuration

Deleting a feature configuration stops Cloud Storage from generating new enrichments for matching buckets. Deleting a configuration doesn't delete existing enrichments already attached to your stored objects.

To delete a feature configuration, complete the following steps:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Object enrichments** page.

[Go to Object enrichments](https://console.cloud.google.com/storage/smart-storage/object-enrichments)

  2. In the **Configuration Name** column, click the name of the feature configuration that you want to delete, and then click delete **Delete**.

  3. In the confirmation dialog, click **Confirm**.




### Command line

Use the [`gcloud alpha storage feature-configs delete`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/feature-configs/delete) command:
    
    
    gcloud alpha storage feature-configs delete FEATURE_CONFIG_ID

Replace `FEATURE_CONFIG_ID` with the ID of the feature configuration.

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.se/) to send a [`featureConfigs.delete` request](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/delete) to the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X DELETE \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Accept: application/json" \
           "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/featureConfigs/FEATURE_CONFIG_ID"

Where:

     * `PROJECT_ID` is the ID of your Google Cloud project. For example, `my-project`.
     * `FEATURE_CONFIG_ID` is the ID of the feature configuration to delete. For example, `my-feature-config`.



## What's next

  * [Manage object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/manage-object-enrichments).
  * [Analyze object enrichments in BigQuery](https://docs.cloud.google.com/storage/docs/object-enrichments/analyze-bigquery).
  * [Review supported models and schemas](https://docs.cloud.google.com/storage/docs/object-enrichments/models).
  * [Troubleshoot object enrichments issues](https://docs.cloud.google.com/storage/docs/storage-intelligence/troubleshooting#object-enrichments-errors).
  * [Review the `featureConfigs` JSON API resource](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
