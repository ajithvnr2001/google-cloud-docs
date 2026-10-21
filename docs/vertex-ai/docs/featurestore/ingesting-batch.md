---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch/
title: Batch import feature values \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:03:35.787774+00:00
---

# Batch import feature values  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Batch import feature values Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

To learn more, run the "Example Feature Store workflow with sample data" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb)

Batch import lets you import feature values in bulk from a valid data source. In a batch import request, you can import values for up to 100 features for an entity type. Note that you can have only one batch import job running per entity type to avoid collisions.

In a batch import request, specify the location of your source data and how it maps to features in your featurestore. Because each batch import request is for a single entity type, your source data must also be for a single entity type.

After the import has successfully completed, feature values are available to subsequent read operations.

  * For information about source data requirements, see [Source data requirements](https://docs.cloud.google.com/vertex-ai/docs/featurestore/source-data).
  * For information about how long Vertex AI Feature Store (Legacy) retains your data in the offline store, see [Vertex AI Feature Store (Legacy)](https://docs.cloud.google.com/vertex-ai/docs/quotas#featurestore) in [Quotas and limits](https://docs.cloud.google.com/vertex-ai/docs/quotas).
  * For information about the oldest feature value timestamp that you can import, see [Vertex AI Feature Store (Legacy)](https://docs.cloud.google.com/vertex-ai/docs/quotas#featurestore) in [Quotas and limits](https://docs.cloud.google.com/vertex-ai/docs/quotas).
  * You can't import feature values for which the timestamps indicate future dates or times.



## Import job performance

Vertex AI Feature Store (Legacy) provides high throughput import, but the minimum latency can take a few minutes. Each request to Vertex AI Feature Store (Legacy) starts a job to complete the work. An import job takes a few minutes to complete even if you are importing a single record.

If you want to make adjustments to how a job performs, change the following two variables:

  * The number of featurestore online serving nodes.
  * The number of workers used for the import job. Workers process and write data into the featurestore.



The recommended number of workers is one worker for every 10 online serving nodes on the featurestore. You can go higher if the online serving load is low. You can specify a maximum of 100 workers. For more guidance, see [monitor and tune resources accordingly to optimize batch import](https://docs.cloud.google.com/vertex-ai/docs/featurestore/best-practices).

If the online serving cluster is under-provisioned, the import job might fail. In the event of a failure, retry the import request when the online serving load is low, or increase the node count of your featurestore and then retry the request.

If the featurestore doesn't have an online store (zero online serving nodes), the import job writes only to the offline store, and the performance of the job depends solely on the number of import workers.

## Data consistency

Inconsistencies can be introduced if the source data is modified during import. Ensure that any source data modifications are complete before you start an import job. Also, duplicate feature values can result in different values being served between online and batch requests. Ensure that you have one feature value for each entity ID and timestamp pair.

If an import operation fails, the featurestore might only have partial data, which can lead to inconsistent values being returned between online and batch serving requests. To avoid this inconsistency, retry the same import request again and wait until the request successfully completes.

## Null values and empty arrays

During import, Vertex AI Feature Store (Legacy) considers null scalar values or empty arrays as empty values. These include empty values in a CSV column. Vertex AI Feature Store (Legacy) doesn't support non-scalar null values, such as a `null` value in an array.

During online serving and batch serving, Vertex AI Feature Store (Legacy) returns the latest non-null or non-empty value of the feature. If a historical value of the feature isn't available, then Vertex AI Feature Store (Legacy) returns `null`.

## NaN values

Vertex AI Feature Store (Legacy) supports NaN (Not a Number) values in `Double` and `DoubleArray`. During import, you can enter `NaN` in the serving input CSV file to represent a NaN value. During online serving and batch serving, Vertex AI Feature Store (Legacy) returns `NaN` for NaN values.

**Note:** `NaN` is considered as valid data only if for the data type `Double`. For all other data types, `NaN` is considered as an invalid feature value. In such a scenario, Vertex AI Feature Store (Legacy) invalidates and ignores the entire row.

## Batch import

Import values in bulk into a featurestore for one or more features of a single entity type.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, view the **Entity type** column and find the entity type that contains the features that you want to import values for.
  4. Click the name of the entity type.
  5. From the action bar, click **Ingest values**.
  6. For **Data source** , select one of the following: 
     * **Cloud Storage CSV file** : Select this option to import data from multiple CSV files from Cloud Storage. Specify the path and name of the CSV file. To specify additional files, click **Add another file**.
     * **Cloud Storage AVRO file** : Select this option to import data from an AVRO file from Cloud Storage. Specify the path and name of the AVRO file.
     * **BigQuery table** : Select this option to import data from a BigQuery table or BigQuery view. Browse and select a table or view to use, which is in the following format: `PROJECT_ID.DATASET_ID.TABLE_ID`
  7. Click **Continue**.
  8. For **Map column to features** , specify which columns in your source data map to entities and features in your featurestore. 
     1. Specify the column name in your source data that contains the entity IDs.
     2. For the timestamp, specify a timestamp column in your source data or specify a single timestamp associated with all feature values that you import.
     3. In the list of features, enter the source data column name that maps to each feature. By default, Vertex AI Feature Store (Legacy) assumes that the feature name and column name match.
  9. Click **Ingest**.



### REST

To import feature values for existing features, send a POST request by using the [featurestores.entityTypes.importFeatureValues](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/importFeatureValues) method. Note that if the names of the source data columns and the destination feature IDs are different, include the `sourceField` parameter. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is created. For example, `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * ENTITY_SOURCE_COLUMN_ID: ID of source column that contains entity IDs.
  * FEATURE_TIME_ID: ID of source column that contains the feature timestamps for the feature values.
  * FEATURE_ID: ID of an existing feature in the featurestore to import values for.
  * FEATURE_SOURCE_COLUMN_ID: ID of source column that contain feature values for the entities.
  * SOURCE_DATA_DETAILS: The source data location, which also indicates the format, such as `"bigquerySource": { "inputUri": "bq://test.dataset.sourcetable" }` for a BigQuery table or BigQuery view.
  * WORKER_COUNT: The number of workers to use to write data to the featurestore.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:importFeatureValues

Request JSON body: 
    
    
    {
      "entityIdField": "ENTITY_SOURCE_COLUMN_ID",
      "featureTimeField": "FEATURE_TIME_ID",
      SOURCE_DATA_DETAILS,
      "featureSpecs": [{
        "id": "FEATURE_ID",
        "sourceField": "FEATURE_SOURCE_COLUMN_ID"
      }],
      "workerCount": WORKER_COUNT
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:importFeatureValues"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:importFeatureValues" | Select-Object -Expand Content

You should see output similar to the following. You can use the OPERATION_ID in the response to [get the status](https://docs.cloud.google.com/vertex-ai/docs/general/long-running-operations) of the operation.
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.ImportFeatureValuesOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-03-02T00:04:13.039166Z",
          "updateTime": "2021-03-02T00:04:13.039166Z"
        }
      }
    }
    

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    import datetime
    from typing import List, Union
    
    from google.cloud import aiplatform
    
    
    def import_feature_values_sample(
        project: str,
        location: str,
        entity_type_id: str,
        featurestore_id: str,
        feature_ids: List[str],
        feature_time: Union[str, datetime.datetime],
        gcs_source_uris: Union[str, List[str]],
        gcs_source_type: str,
    ):
    
        aiplatform.init(project=project, location=location)
    
        my_entity_type = aiplatform.featurestore.EntityType(
            entity_type_name=entity_type_id, featurestore_id=featurestore_id
        )
    
        my_entity_type.ingest_from_gcs(
            feature_ids=feature_ids,
            feature_time=feature_time,
            gcs_source_uris=gcs_source_uris,
            gcs_source_type=gcs_source_type,
        )
    
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[AvroSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AvroSource.html);
    import com.google.cloud.aiplatform.v1.[EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html);
    import com.google.cloud.aiplatform.v1.[ImportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[ImportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.html);
    import com.google.cloud.aiplatform.v1.[ImportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.html).[FeatureSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.FeatureSpec.html);
    import com.google.cloud.aiplatform.v1.[ImportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesResponse.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ImportFeatureValuesSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        String entityIdField = "YOUR_ENTITY_FIELD_ID";
        String featureTimeField = "YOUR_FEATURE_TIME_FIELD";
        String gcsSourceUri = "YOUR_GCS_SOURCE_URI";
        int workerCount = 2;
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 300;
        importFeatureValuesSample(
            project,
            featurestoreId,
            entityTypeId,
            gcsSourceUri,
            entityIdField,
            featureTimeField,
            workerCount,
            location,
            endpoint,
            timeout);
      }
    
      static void importFeatureValuesSample(
          String project,
          String featurestoreId,
          String entityTypeId,
          String gcsSourceUri,
          String entityIdField,
          String featureTimeField,
          int workerCount,
          String location,
          String endpoint,
          int timeout)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html) featurestoreServiceSettings =
            [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html) featurestoreServiceClient =
            [FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html).create(featurestoreServiceSettings)) {
          List<FeatureSpec> featureSpecs = new ArrayList<>();
    
          featureSpecs.add([FeatureSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.FeatureSpec.html).newBuilder().setId("title").build());
          featureSpecs.add([FeatureSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.FeatureSpec.html).newBuilder().setId("genres").build());
          featureSpecs.add([FeatureSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.FeatureSpec.html).newBuilder().setId("average_rating").build());
          [ImportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.html) importFeatureValuesRequest =
              [ImportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.html).newBuilder()
                  .setEntityType(
                      [EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html).of(project, location, featurestoreId, entityTypeId).toString())
                  .setEntityIdField(entityIdField)
                  .[setFeatureTimeField](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.Builder.html#com_google_cloud_aiplatform_v1_ImportFeatureValuesRequest_Builder_setFeatureTimeField_java_lang_String_)(featureTimeField)
                  .[addAllFeatureSpecs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.Builder.html#com_google_cloud_aiplatform_v1_ImportFeatureValuesRequest_Builder_addAllFeatureSpecs_java_lang_Iterable___extends_com_google_cloud_aiplatform_v1_ImportFeatureValuesRequest_FeatureSpec__)(featureSpecs)
                  .[setWorkerCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.Builder.html#com_google_cloud_aiplatform_v1_ImportFeatureValuesRequest_Builder_setWorkerCount_int_)(workerCount)
                  .[setAvroSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesRequest.Builder.html#com_google_cloud_aiplatform_v1_ImportFeatureValuesRequest_Builder_setAvroSource_com_google_cloud_aiplatform_v1_AvroSource_)(
                      [AvroSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AvroSource.html).newBuilder()
                          .setGcsSource([GcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.html).newBuilder().[addUris](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsSource.Builder.html#com_google_cloud_aiplatform_v1_GcsSource_Builder_addUris_java_lang_String_)(gcsSourceUri)))
                  .build();
          OperationFuture<ImportFeatureValuesResponse, ImportFeatureValuesOperationMetadata>
              importFeatureValuesFuture =
                  featurestoreServiceClient.[importFeatureValuesAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html#com_google_cloud_aiplatform_v1_FeaturestoreServiceClient_importFeatureValuesAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_EntityTypeName_)(importFeatureValuesRequest);
          System.out.format(
              "Operation name: %s%n", importFeatureValuesFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [ImportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportFeatureValuesResponse.html) importFeatureValuesResponse =
              importFeatureValuesFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(timeout, TimeUnit.SECONDS);
          System.out.println("Import Feature Values Response");
          System.out.println(importFeatureValuesResponse);
          featurestoreServiceClient.close();
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.\
     * (Not necessary if passing values as arguments)
     */
    
    // const project = 'YOUR_PROJECT_ID';
    // const featurestoreId = 'YOUR_FEATURESTORE_ID';
    // const entityTypeId = 'YOUR_ENTITY_TYPE_ID';
    // const avroGcsUri = 'AVRO_FILE_IN_THE_GCS_URI';
    // const entityIdField = 'ENTITY_ID_FIELD_IN_AVRO';
    // const featureTimeField = 'TIMESTAMP_FIELD_IN_AVRO';
    // const workerCount = <NO_OF_WORKERS_FOR_INGESTION_JOB>;
    // const location = 'YOUR_PROJECT_LOCATION';
    // const apiEndpoint = 'YOUR_API_ENDPOINT';
    // const timeout = <TIMEOUT_IN_MILLI_SECONDS>;
    
    // Imports the Google Cloud Featurestore Service Client library
    const {FeaturestoreServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: apiEndpoint,
    };
    
    // Instantiates a client
    const featurestoreServiceClient = new [FeaturestoreServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(
      clientOptions
    );
    
    async function importFeatureValues() {
      // Configure the entityType resource
      const entityType = `projects/${project}/locations/${location}/featurestores/${featurestoreId}/entityTypes/${entityTypeId}`;
    
      const avroSource = {
        gcsSource: {
          uris: [avroGcsUri],
        },
      };
    
      const featureSpecs = [{id: 'age'}, {id: 'gender'}, {id: 'liked_genres'}];
    
      const request = {
        entityType: entityType,
        avroSource: avroSource,
        entityIdField: entityIdField,
        featureSpecs: featureSpecs,
        featureTimeField: featureTimeField,
        workerCount: Number(workerCount),
      };
    
      // Import Feature Values Request
      const [operation] = await featurestoreServiceClient.importFeatureValues(
        request,
        {timeout: Number(timeout)}
      );
      const [response] = await operation.promise();
    
      console.log('Import feature values response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    importFeatureValues();

## View import jobs

Use the Google Cloud console to view batch import jobs in a Google Cloud project.

**Note:** For featurestores created during [Preview](https://cloud.google.com/products#product-launch-stages), the Google Cloud console lists both batch import and batch serving jobs. Featurestores created on or after General Availability (October 5, 2021) show only batch import jobs. If you see both job types and just want to view batch import jobs, you must [create](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores) and use a new featurestore.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. From the action bar, click **View ingestion jobs** to list import jobs for all featurestores.
  4. Click the ID of an import job to view its details such as its data source, number of import entities, and number of feature values imported.



## Overwrite existing data in a featurestore

You can re-import values to overwrite existing feature values if they both have the same timestamps. You don't need to delete existing feature values first. For example, you might rely on an underlying source data that was recently changed. To keep your featurestore consistent with that underlying data, import your feature values again. If you have mismatched timestamps, the imported values are considered unique and the old values continue to exist (they aren't overwritten).

To ensure consistency between online and batch serving requests, wait until the import job is complete before making any serving requests.

## Backfill historical data

If you're backfilling data, where you're importing past feature values, disable online serving for your import job. Online serving is for serving the latest feature values only, which backfilling doesn't include. Disabling online serving is useful because you eliminate any load on your online serving nodes and increase throughput for your import job, which can decrease its completion time.

You can disable online serving for import jobs when you use the API or client libraries. For more information, see the `disableOnlineServing` field for the [importFeatureValue method](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/importFeatureValues).

## What's next

  * Learn how to serve features through [online serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-online) or [batch serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-batch).
  * Learn how to [monitor imported feature values over time](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring#feature).
  * View the Vertex AI Feature Store (Legacy) [concurrent batch job quota](https://docs.cloud.google.com/vertex-ai/quotas#featurestore).
  * [Troubleshoot](https://docs.cloud.google.com/vertex-ai/docs/general/troubleshooting#feature-store) common Vertex AI Feature Store (Legacy) issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
