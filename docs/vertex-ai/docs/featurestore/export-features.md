---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/export-features/
title: Export feature values \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:02:03.999514+00:00
---

# Export feature values  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/export-features/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Export feature values Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

To learn more, run the "Example Feature Store workflow with sample data" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb)

Export feature values for all entities of a single entity type to a BigQuery table or a Cloud Storage bucket. You can choose to get a snapshot or to fully export feature values. A snapshot returns a single value per feature compared to a full export, which can return multiple values per feature. You can't select particular entity IDs or include multiple entity types when exporting feature values.

Exporting feature values is useful for archiving or for performing ad hoc analysis on your data. For example, you can store regular snapshots of your featurestore to save its state at different points in time. If you need to get feature values for building a training dataset, use [batch serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-batch) instead.

## Snapshot and full export comparison

Both the snapshot and full export options let you query data by specifying a single timestamp (either the start time or end time) or both timestamps. For snapshots, Vertex AI Feature Store (Legacy) returns the latest feature value within a given time range. In the output, the associated timestamp with each feature value is the snapshot timestamp (not the feature value timestamp).

For full exports, Vertex AI Feature Store (Legacy) returns all feature values within a given time range. In the output, the associated timestamp with each feature value is the feature timestamp (the specified timestamp when the feature value was ingested).

The following table summarizes what Vertex AI Feature Store (Legacy) returns based on the option that you choose and the timestamps that you provide.

Option | Start time only (inclusive) | End time only (inclusive) | Start and end time (inclusive)  
---|---|---|---  
Snapshot | Starting with the current time (when the request was received), returns the latest value, looking back until the start time.  
The snapshot timestamp is set to the current time.  | Starting with the end time, returns the latest value, looking back to the very first value for each feature.  
The snapshot timestamp is set to the specified end time.  | Returns the latest value within the specified time range.  
The snapshot timestamp is set to the specified end time.   
Full export | Returns all values on and after the start time and up to the current time (when the request was sent). | Returns all values up to the end time, going all the way back to the very first value for each feature. | Returns all values within the specified time range.  
  
## Null values

For snapshots, if the latest feature value is null at a given timestamp, Vertex AI Feature Store (Legacy) returns the previous non-null feature value. If there are no previous non-null values, Vertex AI Feature Store (Legacy) returns null.

For full exports, if a feature value is null at a given timestamp, Vertex AI Feature Store (Legacy) returns null for that timestamp.

## Examples

As an example, assume you had the following values in a featurestore, where the values for `Feature_A` and `Feature_B` share the same timestamp:

Entity ID | Feature value timestamp | Feature_A | Feature_B  
---|---|---|---  
123 | T1 | A_T1 | B_T1  
123 | T2 | A_T2 | NULL  
123 | T3 | A_T3 | NULL  
123 | T4 | A_T4 | B_T4  
123 | T5 | NULL | B_T5  
  
### Snapshot

For snapshots, Vertex AI Feature Store (Legacy) returns the following values based on the given timestamp values:

  * If only the **start** time is set to `T3`, the snapshot returns the following values:

Entity ID | Snapshot timestamp | Feature_A | Feature_B  
---|---|---|---  
123 | CURRENT_TIME | A_T4 | B_T5  
  
  * If only the **end** time is set to `T3`, the snapshot returns the following values:

Entity ID | Snapshot timestamp | Feature_A | Feature_B  
---|---|---|---  
123 | T3 | A_T3 | B_T1  
  
  * If the **start** and **end** times are set to `T2` and `T3`, the snapshot returns the following values:

Entity ID | Snapshot timestamp | Feature_A | Feature_B  
---|---|---|---  
123 | T3 | A_T3 | NULL  
  
### Full export

For full exports, Vertex AI Feature Store (Legacy) returns the following values based on the given timestamp values:

  * If only the **start** time is set to `T3`, the full export returns the following values:

Entity ID | Feature value timestamp | Feature_A | Feature_B  
---|---|---|---  
123 | T3 | A_T3 | NULL  
123 | T4 | A_T4 | B_T4  
123 | T5 | NULL | B_T5  
  
  * If only the **end** time is set to `T3`, the full export returns the following values:

Entity ID | Feature value timestamp | Feature_A | Feature_B  
---|---|---|---  
123 | T1 | A_T1 | B_T1  
123 | T2 | A_T2 | NULL  
123 | T3 | A_T3 | NULL  
  
  * If the **start** and **end** times are set to `T2` and `T4`, the full export returns the following values:

Entity ID | Feature value timestamp | Feature_A | Feature_B  
---|---|---|---  
123 | T2 | A_T2 | NULL  
123 | T3 | A_T3 | NULL  
123 | T4 | A_T4 | B_T4  
  
## Export feature values

When you export feature values, you choose which features to query and whether it is a snapshot or a full export. The following sections show a sample for each option.

For both options, the output destination must be in the same region as the source featurestore. For example, if your featurestore is in `us-central1`, then the destination Cloud Storage bucket or BigQuery table must also be in `us-central1`.

### Snapshot

Export the latest feature values for a given time range.

### Web UI

Use another method. You cannot export feature values from the Google Cloud console.

### REST

To export feature values, send a POST request by using the [entityTypes.exportFeatureValues](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/exportFeatureValues) method. 

The following sample outputs a BigQuery table, but you can also output to a Cloud Storage bucket. Each output destination might have some prerequisites before you can submit a request. For example, if you specify a table name for the `bigqueryDestination` field, you must have an existing dataset. These requirements are documented in the API reference. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located. For example, `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * START_TIME and END_TIME: (Optional) If you specify the start time only, returns the latest value starting from the current time (when the request is sent) and looking back until the start time. If you specify the end time only, returns the latest value starting from the end time (inclusive) and looking back to the very first value. If you specify a start time and end time, returns the latest value within the specified time range (inclusive). If you specify neither, returns the latest values for each feature, starting from the current time and looking back to the very first value.
  * DATASET_NAME: Name of the destination BigQuery dataset.
  * TABLE_NAME: Name of the destination BigQuery table.
  * FEATURE_ID: ID of one or more features. Specify a single `*` (asterisk) to select all features.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:exportFeatureValues

Request JSON body: 
    
    
    {
      "snapshotExport": {
        "start_time": "START_TIME",
        "snapshot_time": "END_TIME"
      },
      "destination" : {
        "bigqueryDestination": {
          "outputUri": "bq://PROJECT_ID.DATASET_NAME.TABLE_NAME"
        }
      },
      "featureSelector": {
        "idMatcher": {
          "ids": ["FEATURE_ID", ...]
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:exportFeatureValues"

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
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:exportFeatureValues" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.ExportFeatureValuesOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-12-03T22:55:25.974976Z",
          "updateTime": "2021-12-03T22:55:25.974976Z"
        }
      }
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html);
    import com.google.cloud.aiplatform.v1.[EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html);
    import com.google.cloud.aiplatform.v1.[ExportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.html);
    import com.google.cloud.aiplatform.v1.[ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.html).[SnapshotExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.SnapshotExport.html);
    import com.google.cloud.aiplatform.v1.[ExportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesResponse.html);
    import com.google.cloud.aiplatform.v1.[FeatureSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.html);
    import com.google.cloud.aiplatform.v1.[FeatureValueDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureValueDestination.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[IdMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IdMatcher.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ExportFeatureValuesSnapshotSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        String destinationTableUri = "YOUR_DESTINATION_TABLE_URI";
        List<String> featureSelectorIds = Arrays.asList("title", "genres", "average_rating");
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 300;
        exportFeatureValuesSnapshotSample(
            project,
            featurestoreId,
            entityTypeId,
            destinationTableUri,
            featureSelectorIds,
            location,
            endpoint,
            timeout);
      }
    
      static void exportFeatureValuesSnapshotSample(
          String project,
          String featurestoreId,
          String entityTypeId,
          String destinationTableUri,
          List<String> featureSelectorIds,
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
    
          [FeatureSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.html) featureSelector =
              [FeatureSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.html).newBuilder()
                  .[setIdMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.Builder.html#com_google_cloud_aiplatform_v1_FeatureSelector_Builder_setIdMatcher_com_google_cloud_aiplatform_v1_IdMatcher_)([IdMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IdMatcher.html).newBuilder().addAllIds(featureSelectorIds).build())
                  .build();
    
          [ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.html) exportFeatureValuesRequest =
              [ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.html).newBuilder()
                  .setEntityType(
                      [EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html).of(project, location, featurestoreId, entityTypeId).toString())
                  .setDestination(
                      [FeatureValueDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureValueDestination.html).newBuilder()
                          .setBigqueryDestination(
                              [BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html).newBuilder().setOutputUri(destinationTableUri)))
                  .setFeatureSelector(featureSelector)
                  .[setSnapshotExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.Builder.html#com_google_cloud_aiplatform_v1_ExportFeatureValuesRequest_Builder_setSnapshotExport_com_google_cloud_aiplatform_v1_ExportFeatureValuesRequest_SnapshotExport_)([SnapshotExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.SnapshotExport.html).newBuilder())
                  .build();
    
          OperationFuture<ExportFeatureValuesResponse, ExportFeatureValuesOperationMetadata>
              exportFeatureValuesFuture =
                  featurestoreServiceClient.[exportFeatureValuesAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html#com_google_cloud_aiplatform_v1_FeaturestoreServiceClient_exportFeatureValuesAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_EntityTypeName_)(exportFeatureValuesRequest);
          System.out.format(
              "Operation name: %s%n", exportFeatureValuesFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [ExportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesResponse.html) exportFeatureValuesResponse =
              exportFeatureValuesFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(timeout, TimeUnit.SECONDS);
          System.out.println("Snapshot Export Feature Values Response");
          System.out.println(exportFeatureValuesResponse);
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
    // const destinationTableUri = 'YOUR_BQ_DESTINATION_TABLE_URI';
    // const timestamp = <STARTING_TIMESTAMP_OF_SNAPSHOT_IN_SECONDS>;
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
    
    async function exportFeatureValuesSnapshot() {
      // Configure the entityType resource
      const entityType = `projects/${project}/locations/${location}/featurestores/${featurestoreId}/entityTypes/${entityTypeId}`;
    
      const destination = {
        bigqueryDestination: {
          // # Output to BigQuery table created earlier
          outputUri: destinationTableUri,
        },
      };
    
      const featureSelector = {
        idMatcher: {
          ids: ['age', 'gender', 'liked_genres'],
        },
      };
    
      const snapshotExport = {
        startTime: {
          seconds: Number(timestamp),
        },
      };
    
      const request = {
        entityType: entityType,
        destination: destination,
        featureSelector: featureSelector,
        snapshotExport: snapshotExport,
      };
    
      // Export Feature Values Request
      const [operation] = await featurestoreServiceClient.exportFeatureValues(
        request,
        {timeout: Number(timeout)}
      );
      const [response] = await operation.promise();
    
      console.log('Export feature values snapshot response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    exportFeatureValuesSnapshot();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

### Full export

Export all feature values within a given time range.

### Web UI

Use another method. You cannot export feature values from the Google Cloud console.

### REST

To export feature values, send a POST request by using the [entityTypes.exportFeatureValues](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/exportFeatureValues) method. 

The following sample outputs a BigQuery table, but you can also output to a Cloud Storage bucket. Each output destination might have some prerequisites before you can submit a request. For example, if you specify a table name for the `bigqueryDestination` field, you must have an existing dataset. These requirements are documented in the API reference. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located. For example, `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * START_TIME and END_TIME: (Optional) If you specify the start time only, returns all values between the current time (when the request is sent) and the start time (inclusive). If you specify the end time only, returns all values between the end time (inclusive) and the very first value timestamp (for each feature). If you specify a start time and end time, returns all values within the specified time range (inclusive). If you specify neither, returns all values between the current time and the very first value timestamp (for each feature).
  * DATASET_NAME: Name of the destination BigQuery dataset.
  * TABLE_NAME: Name of the destination BigQuery table.
  * FEATURE_ID: ID of one or more features. Specify a single `*` (asterisk) to select all features.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:exportFeatureValues

Request JSON body: 
    
    
    {
      "fullExport": {
        "start_time": "START_TIME",
        "end_time": "END_TIME"
      },
      "destination" : {
        "bigqueryDestination": {
          "outputUri": "bq://PROJECT.DATASET_NAME.TABLE_NAME"
        }
      },
      "featureSelector": {
        "idMatcher": {
          "ids": ["FEATURE_ID", ...]
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:exportFeatureValues"

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
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:exportFeatureValues" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.ExportFeatureValuesOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-12-03T22:55:25.974976Z",
          "updateTime": "2021-12-03T22:55:25.974976Z"
        }
      }
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html);
    import com.google.cloud.aiplatform.v1.[EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html);
    import com.google.cloud.aiplatform.v1.[ExportFeatureValuesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.html);
    import com.google.cloud.aiplatform.v1.[ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.html).[FullExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.FullExport.html);
    import com.google.cloud.aiplatform.v1.[ExportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesResponse.html);
    import com.google.cloud.aiplatform.v1.[FeatureSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.html);
    import com.google.cloud.aiplatform.v1.[FeatureValueDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureValueDestination.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[IdMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IdMatcher.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ExportFeatureValuesSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        String destinationTableUri = "YOUR_DESTINATION_TABLE_URI";
        List<String> featureSelectorIds = Arrays.asList("title", "genres", "average_rating");
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 300;
        exportFeatureValuesSample(
            project,
            featurestoreId,
            entityTypeId,
            destinationTableUri,
            featureSelectorIds,
            location,
            endpoint,
            timeout);
      }
    
      static void exportFeatureValuesSample(
          String project,
          String featurestoreId,
          String entityTypeId,
          String destinationTableUri,
          List<String> featureSelectorIds,
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
    
          [FeatureSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.html) featureSelector =
              [FeatureSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.html).newBuilder()
                  .[setIdMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.Builder.html#com_google_cloud_aiplatform_v1_FeatureSelector_Builder_setIdMatcher_com_google_cloud_aiplatform_v1_IdMatcher_)([IdMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IdMatcher.html).newBuilder().addAllIds(featureSelectorIds).build())
                  .build();
    
          [ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.html) exportFeatureValuesRequest =
              [ExportFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.html).newBuilder()
                  .setEntityType(
                      [EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html).of(project, location, featurestoreId, entityTypeId).toString())
                  .setDestination(
                      [FeatureValueDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureValueDestination.html).newBuilder()
                          .setBigqueryDestination(
                              [BigQueryDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BigQueryDestination.html).newBuilder().setOutputUri(destinationTableUri)))
                  .setFeatureSelector(featureSelector)
                  .[setFullExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.Builder.html#com_google_cloud_aiplatform_v1_ExportFeatureValuesRequest_Builder_setFullExport_com_google_cloud_aiplatform_v1_ExportFeatureValuesRequest_FullExport_)([FullExport](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesRequest.FullExport.html).newBuilder())
                  .build();
    
          OperationFuture<ExportFeatureValuesResponse, ExportFeatureValuesOperationMetadata>
              exportFeatureValuesFuture =
                  featurestoreServiceClient.[exportFeatureValuesAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html#com_google_cloud_aiplatform_v1_FeaturestoreServiceClient_exportFeatureValuesAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_EntityTypeName_)(exportFeatureValuesRequest);
          System.out.format(
              "Operation name: %s%n", exportFeatureValuesFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [ExportFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportFeatureValuesResponse.html) exportFeatureValuesResponse =
              exportFeatureValuesFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(timeout, TimeUnit.SECONDS);
          System.out.println("Export Feature Values Response");
          System.out.println(exportFeatureValuesResponse);
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
    // const destinationTableUri = 'YOUR_BQ_DESTINATION_TABLE_URI';
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
    
    async function exportFeatureValues() {
      // Configure the entityType resource
      const entityType = `projects/${project}/locations/${location}/featurestores/${featurestoreId}/entityTypes/${entityTypeId}`;
    
      const destination = {
        bigqueryDestination: {
          // # Output to BigQuery table created earlier
          outputUri: destinationTableUri,
        },
      };
    
      const featureSelector = {
        idMatcher: {
          ids: ['age', 'gender', 'liked_genres'],
        },
      };
    
      const request = {
        entityType: entityType,
        destination: destination,
        featureSelector: featureSelector,
        fullExport: {},
      };
    
      // Export Feature Values Request
      const [operation] = await featurestoreServiceClient.exportFeatureValues(
        request,
        {timeout: Number(timeout)}
      );
      const [response] = await operation.promise();
    
      console.log('Export feature values response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    exportFeatureValues();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

## What's next

  * Learn how to [batch ingest feature values](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch).
  * Learn how to serve features through [online serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-online).
  * View the Vertex AI Feature Store (Legacy) [concurrent batch job quota](https://docs.cloud.google.com/vertex-ai/quotas#featurestore).
  * [Troubleshoot](https://docs.cloud.google.com/vertex-ai/docs/general/troubleshooting#feature-store) common Vertex AI Feature Store (Legacy) issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
