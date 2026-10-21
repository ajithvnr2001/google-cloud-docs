---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-features/
title: Manage and find features \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:57:38.197256+00:00
---

# Manage and find features  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-features/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Manage and find features Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

To learn more, run the "Example Feature Store workflow with sample data" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb)

Learn how to manage and find features.

## Create a feature

Create a single feature for an existing entity type. To create multiple features in a single request, see Batch creating features.

**Note:** Vertex AI has a limit on the number features that you can create per entity type. For more information, see the [Vertex AI Feature Store (Legacy) limits](https://docs.cloud.google.com/vertex-ai/quotas#featurestore).

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, view the **Entity type** column and click the entity type to add features to.
  4. Click **Add features** to open the **Add features** pane.
  5. Specify a name, value type, and (optionally) a description for the feature.
  6. To enable feature value monitoring ([Preview](https://cloud.google.com/products/#product-launch-stages)), under **Feature monitoring** , select **Override entity type monitoring config** and then enter the number of days between snapshots. This configuration overrides any existing or future monitoring configurations on the feature's entity type. For more information, see [Feature value monitoring](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring#feature).
  7. To add more features, click **Add another feature**.
  8. Click **Save**.



### REST

To create a feature for an existing entity type, send a POST request by using the [featurestores.entityTypes.features.create](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes.features/create) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * FEATURE_ID: An ID for the feature.
  * DESCRIPTION: Description of the feature.
  * VALUE_TYPE: The value type of the feature.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID?featureId=FEATURE_ID

Request JSON body: 
    
    
    {
      "description": "DESCRIPTION",
      "valueType": "VALUE_TYPE"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID?featureId=FEATURE_ID"

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
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID?featureId=FEATURE_ID" | Select-Object -Expand Content

You should see output similar to the following. You can use the OPERATION_ID in the response to [get the status](https://docs.cloud.google.com/vertex-ai/docs/general/long-running-operations) of the operation.
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.CreateFeatureOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-03-02T00:04:13.039166Z",
          "updateTime": "2021-03-02T00:04:13.039166Z"
        }
      }
    }
    

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    from google.cloud import aiplatform
    
    
    def create_feature_sample(
        project: str,
        location: str,
        feature_id: str,
        value_type: str,
        entity_type_id: str,
        featurestore_id: str,
    ):
    
        aiplatform.init(project=project, location=location)
    
        my_feature = aiplatform.Feature.create(
            feature_id=feature_id,
            value_type=value_type,
            entity_type_name=entity_type_id,
            featurestore_id=featurestore_id,
        )
    
        my_feature.wait()
    
        return my_feature
    
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[CreateFeatureOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest.html);
    import com.google.cloud.aiplatform.v1.[EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html);
    import com.google.cloud.aiplatform.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html);
    import com.google.cloud.aiplatform.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html).ValueType;
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateFeatureSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        String featureId = "YOUR_FEATURE_ID";
        String description = "YOUR_FEATURE_DESCRIPTION";
        ValueType valueType = ValueType.STRING;
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 900;
        createFeatureSample(
            project,
            featurestoreId,
            entityTypeId,
            featureId,
            description,
            valueType,
            location,
            endpoint,
            timeout);
      }
    
      static void createFeatureSample(
          String project,
          String featurestoreId,
          String entityTypeId,
          String featureId,
          String description,
          ValueType valueType,
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
    
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html) feature =
              [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html).newBuilder().setDescription(description).setValueType(valueType).build();
    
          [CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest.html) createFeatureRequest =
              [CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest.html).newBuilder()
                  .setParent(
                      [EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html).of(project, location, featurestoreId, entityTypeId).toString())
                  .setFeature(feature)
                  .setFeatureId(featureId)
                  .build();
    
          OperationFuture<Feature, CreateFeatureOperationMetadata> featureFuture =
              featurestoreServiceClient.createFeatureAsync(createFeatureRequest);
          System.out.format("Operation name: %s%n", featureFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html) featureResponse = featureFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(timeout, TimeUnit.SECONDS);
          System.out.println("Create Feature Response");
          System.out.format("Name: %s%n", featureResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html#com_google_cloud_aiplatform_v1_Feature_getName__)());
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
    // const featureId = 'YOUR_FEATURE_ID';
    // const valueType = 'FEATURE_VALUE_DATA_TYPE';
    // const description = 'YOUR_ENTITY_TYPE_DESCRIPTION';
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
    
    async function createFeature() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}/featurestores/${featurestoreId}/entityTypes/${entityTypeId}`;
    
      const feature = {
        valueType: valueType,
        description: description,
      };
    
      const request = {
        parent: parent,
        feature: feature,
        featureId: featureId,
      };
    
      // Create Feature request
      const [operation] = await featurestoreServiceClient.createFeature(request, {
        timeout: Number(timeout),
      });
      const [response] = await operation.promise();
    
      console.log('Create feature response');
      console.log(`Name : ${response.name}`);
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    createFeature();

## Batch create features

Create features in bulk for an existing type. For batch creation requests, Vertex AI Feature Store (Legacy) creates multiple features at once, which is faster for creating a large number of features compared to the `featurestores.entityTypes.features.create` method.

**Note:** Vertex AI has a limit on the number features that you can create per entity type. For more information, see the [Vertex AI Feature Store (Legacy) limits](https://docs.cloud.google.com/vertex-ai/quotas#featurestore).

### Web UI

See creating a feature.

### REST

To create one or more features for an existing entity type, send a POST request by using the [featurestores.entityTypes.features.batchCreate](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes.features/batchCreate) method, as shown in the following sample. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * PARENT: The resource name of the entity type to create the features under. Required format:  
`projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID`
  * FEATURE_ID: An ID for the feature.
  * DESCRIPTION: Description of the feature.
  * VALUE_TYPE: The value type of the feature.
  * DURATION: (Optional) The interval duration between snapshots in seconds. The value must end with an `s`.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features:batchCreate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "parent" : "PARENT_1",
          "feature": {
            "description": "DESCRIPTION_1",
            "valueType": "VALUE_TYPE_1",
            "monitoringConfig": {
              "snapshotAnalysis": {
                "monitoringInterval": "DURATION"
              }
            }
          },
          "featureId": "FEATURE_ID_1"
        },
        {
          "parent" : "PARENT_2",
          "feature": {
            "description": "DESCRIPTION_2",
            "valueType": "VALUE_TYPE_2",
            "monitoringConfig": {
              "snapshotAnalysis": {
                "monitoringInterval": "DURATION"
              }
            }
          },
          "featureId": "FEATURE_ID_2"
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features:batchCreate"

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
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features:batchCreate" | Select-Object -Expand Content

You should see output similar to the following. You can use the OPERATION_ID in the response to [get the status](https://docs.cloud.google.com/vertex-ai/docs/general/long-running-operations) of the operation.
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.BatchCreateFeaturesOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-03-02T00:04:13.039166Z",
          "updateTime": "2021-03-02T00:04:13.039166Z"
        }
      }
    }
    

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    from google.cloud import aiplatform
    
    
    def batch_create_features_sample(
        project: str,
        location: str,
        entity_type_id: str,
        featurestore_id: str,
        sync: bool = True,
    ):
    
        aiplatform.init(project=project, location=location)
    
        my_entity_type = aiplatform.featurestore.EntityType(
            entity_type_name=entity_type_id, featurestore_id=featurestore_id
        )
    
        FEATURE_CONFIGS = {
            "age": {"value_type": "INT64", "description": "User age"},
            "gender": {"value_type": "STRING", "description": "User gender"},
            "liked_genres": {
                "value_type": "STRING_ARRAY",
                "description": "An array of genres this user liked",
            },
        }
    
        my_entity_type.batch_create_features(feature_configs=FEATURE_CONFIGS, sync=sync)
    
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[BatchCreateFeaturesOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[BatchCreateFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesRequest.html);
    import com.google.cloud.aiplatform.v1.[BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesResponse.html);
    import com.google.cloud.aiplatform.v1.[CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest.html);
    import com.google.cloud.aiplatform.v1.[EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html);
    import com.google.cloud.aiplatform.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html);
    import com.google.cloud.aiplatform.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html).ValueType;
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class BatchCreateFeaturesSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 300;
        batchCreateFeaturesSample(project, featurestoreId, entityTypeId, location, endpoint, timeout);
      }
    
      static void batchCreateFeaturesSample(
          String project,
          String featurestoreId,
          String entityTypeId,
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
    
          List<CreateFeatureRequest> createFeatureRequests = new ArrayList<>();
    
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html) titleFeature =
              [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html).newBuilder()
                  .setDescription("The title of the movie")
                  .setValueType(ValueType.STRING)
                  .build();
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html) genresFeature =
              [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html).newBuilder()
                  .setDescription("The genres of the movie")
                  .setValueType(ValueType.STRING)
                  .build();
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html) averageRatingFeature =
              [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html).newBuilder()
                  .setDescription("The average rating for the movie, range is [1.0-5.0]")
                  .setValueType(ValueType.DOUBLE)
                  .build();
    
          createFeatureRequests.add(
              [CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest.html).newBuilder().setFeature(titleFeature).setFeatureId("title").build());
    
          createFeatureRequests.add(
              [CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest.html).newBuilder()
                  .setFeature(genresFeature)
                  .setFeatureId("genres")
                  .build());
    
          createFeatureRequests.add(
              [CreateFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateFeatureRequest.html).newBuilder()
                  .setFeature(averageRatingFeature)
                  .setFeatureId("average_rating")
                  .build());
    
          [BatchCreateFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesRequest.html) batchCreateFeaturesRequest =
              [BatchCreateFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesRequest.html).newBuilder()
                  .setParent(
                      [EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html).of(project, location, featurestoreId, entityTypeId).toString())
                  .addAllRequests(createFeatureRequests)
                  .build();
    
          OperationFuture<BatchCreateFeaturesResponse, BatchCreateFeaturesOperationMetadata>
              batchCreateFeaturesFuture =
                  featurestoreServiceClient.batchCreateFeaturesAsync(batchCreateFeaturesRequest);
          System.out.format(
              "Operation name: %s%n", batchCreateFeaturesFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [BatchCreateFeaturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCreateFeaturesResponse.html) batchCreateFeaturesResponse =
              batchCreateFeaturesFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(timeout, TimeUnit.SECONDS);
          System.out.println("Batch Create Features Response");
          System.out.println(batchCreateFeaturesResponse);
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
    
    async function batchCreateFeatures() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}/featurestores/${featurestoreId}/entityTypes/${entityTypeId}`;
    
      const ageFeature = {
        valueType: 'INT64',
        description: 'User age',
      };
    
      const ageFeatureRequest = {
        feature: ageFeature,
        featureId: 'age',
      };
    
      const genderFeature = {
        valueType: 'STRING',
        description: 'User gender',
      };
    
      const genderFeatureRequest = {
        feature: genderFeature,
        featureId: 'gender',
      };
    
      const likedGenresFeature = {
        valueType: 'STRING_ARRAY',
        description: 'An array of genres that this user liked',
      };
    
      const likedGenresFeatureRequest = {
        feature: likedGenresFeature,
        featureId: 'liked_genres',
      };
    
      const requests = [
        ageFeatureRequest,
        genderFeatureRequest,
        likedGenresFeatureRequest,
      ];
    
      const request = {
        parent: parent,
        requests: requests,
      };
    
      // Batch Create Features request
      const [operation] = await featurestoreServiceClient.batchCreateFeatures(
        request,
        {timeout: Number(timeout)}
      );
      const [response] = await operation.promise();
    
      console.log('Batch create features response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    batchCreateFeatures();

## List features

List all features in a given location. To search for features across all entity types and featurestores in a given location, see the Searching for features method.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, view the **Features** column to see the features in your project for the selected region.



### REST

To list all features for a single entity type, send a GET request by using the [featurestores.entityTypes.features.list](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes.features/list) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.



HTTP method and URL: 
    
    
    GET https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "features": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features/FEATURE_ID_1",
          "description": "DESCRIPTION",
          "valueType": "VALUE_TYPE",
          "createTime": "2021-03-01T22:41:20.626644Z",
          "updateTime": "2021-03-01T22:41:20.626644Z",
          "labels": {
            "environment": "testing"
          },
          "etag": "AMEw9yP0qJeLao6P3fl9cKEGY4ie5-SanQaiN7c_Ca4QOa0u7AxwO6i75Vbp0Cr51MSf"
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features/FEATURE_ID_2",
          "description": "DESCRIPTION",
          "valueType": "VALUE_TYPE",
          "createTime": "2021-02-25T01:27:00.544230Z",
          "updateTime": "2021-02-25T01:27:00.544230Z",
          "labels": {
            "environment": "testing"
          },
          "etag": "AMEw9yMdrLZ7Waty0ane-DkHq4kcsIVC-piqJq7n6A_Y-BjNzPY4rNlokDHNyUqC7edw"
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features/FEATURE_ID_3",
          "description": "DESCRIPTION",
          "valueType": "VALUE_TYPE",
          "createTime": "2021-03-01T22:41:20.628493Z",
          "updateTime": "2021-03-01T22:41:20.628493Z",
          "labels": {
            "environment": "testing"
          },
          "etag": "AMEw9yM-sAkv-u-jzkUOToaAVovK7GKbrubd9DbmAonik-ojTWG8-hfSRYt6jHKRTQ35"
        }
      ]
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html);
    import com.google.cloud.aiplatform.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturesRequest.html);
    import java.io.IOException;
    
    public class ListFeaturesSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
    
        listFeaturesSample(project, featurestoreId, entityTypeId, location, endpoint);
      }
    
      static void listFeaturesSample(
          String project, String featurestoreId, String entityTypeId, String location, String endpoint)
          throws IOException {
        [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html) featurestoreServiceSettings =
            [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html) featurestoreServiceClient =
            [FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html).create(featurestoreServiceSettings)) {
    
          [ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturesRequest.html) listFeaturesRequest =
              [ListFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListFeaturesRequest.html).newBuilder()
                  .setParent(
                      [EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html).of(project, location, featurestoreId, entityTypeId).toString())
                  .build();
          System.out.println("List Features Response");
          for ([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html) element :
              featurestoreServiceClient.listFeatures(listFeaturesRequest).iterateAll()) {
            System.out.println(element);
          }
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
    
    async function listFeatures() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}/featurestores/${featurestoreId}/entityTypes/${entityTypeId}`;
    
      const request = {
        parent: parent,
      };
    
      // List Features request
      const [response] = await featurestoreServiceClient.listFeatures(request, {
        timeout: Number(timeout),
      });
    
      console.log('List features response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    listFeatures();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

## Search for features

Search for features based on one or more of their properties, such as feature ID, entity type ID, or feature description. Vertex AI Feature Store (Legacy) searches across all featurestores and entity types in a given location. You can also limit results by filtering on specific featurestores, value types, and labels.

To list all features, see Listing features.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. Click the features table's **Filter** field.
  4. Select a property to filter on such as **Feature** , which returns features that contain a matching string anywhere in their ID.
  5. Type a value for the filter and then press enter. Vertex AI Feature Store (Legacy) returns results in the features table.
  6. To add additional filters, click the **Filter** field again.



### REST

To search for features, send a GET request by using the [featurestores.searchFeatures](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores/searchFeatures) method. The following sample uses multiple search parameters, written as `featureId:test AND valueType=STRING`. The query returns features that contain `test` in their ID and whose values are of type `STRING`. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .



HTTP method and URL: 
    
    
    GET https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores:searchFeatures?query="featureId:test%20AND%20valueType=STRING"

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores:searchFeatures?query="featureId:test%20AND%20valueType=STRING""

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores:searchFeatures?query="featureId:test%20AND%20valueType=STRING"" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "features": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_IDfeature-delete.html/featurestores/featurestore_demo/entityTypes/testing/features/test1",
          "description": "featurestore test1",
          "createTime": "2021-02-26T18:16:09.528185Z",
          "updateTime": "2021-02-26T18:16:09.528185Z",
          "labels": {
            "environment": "testing"
          }
        }
      ]
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html);
    import com.google.cloud.aiplatform.v1.[SearchFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchFeaturesRequest.html);
    import java.io.IOException;
    
    public class SearchFeaturesSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String query = "YOUR_QUERY";
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        searchFeaturesSample(project, query, location, endpoint);
      }
    
      static void searchFeaturesSample(String project, String query, String location, String endpoint)
          throws IOException {
        [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html) featurestoreServiceSettings =
            [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html) featurestoreServiceClient =
            [FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html).create(featurestoreServiceSettings)) {
    
          [SearchFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchFeaturesRequest.html) searchFeaturesRequest =
              [SearchFeaturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchFeaturesRequest.html).newBuilder()
                  .setLocation([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.LocationName.html).of(project, location).toString())
                  .setQuery(query)
                  .build();
          System.out.println("Search Features Response");
          for ([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html) element :
              featurestoreServiceClient.searchFeatures(searchFeaturesRequest).iterateAll()) {
            System.out.println(element);
          }
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
    
    async function searchFeatures() {
      // Configure the locationResource resource
      const locationResource = `projects/${project}/locations/${location}`;
    
      const request = {
        location: locationResource,
        query: query,
      };
    
      // Search Features request
      const [response] = await featurestoreServiceClient.searchFeatures(request, {
        timeout: Number(timeout),
      });
    
      console.log('Search features response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    searchFeatures();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

## View feature details

View details about a feature, such as its value type or description. If you use the Google Cloud console and have feature monitoring enabled, you can also view the distribution of feature values over time.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, view the **Features** column to find the feature that you want to view details for.
  4. Click the name of a feature to view its details.
  5. To view its metrics, click **Metrics**. Vertex AI Feature Store (Legacy) provides feature distribution metrics for the feature.



### REST

To get details about a feature, send a GET request by using the [featurestores.entityTypes.features.get](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes.features/get) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * FEATURE_ID: ID of the feature.



HTTP method and URL: 
    
    
    GET https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features/FEATURE_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features/FEATURE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features/FEATURE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features/FEATURE_ID",
      "description": "DESCRIPTION",
      "valueType": "VALUE_TYPE",
      "createTime": "2021-03-01T22:41:20.628493Z",
      "updateTime": "2021-03-01T22:41:20.628493Z",
      "labels": {
        "environment": "testing"
      },
      "etag": "AMEw9yOZbdYKHTyjV22ziZR1vUX3nWOi0o2XU3-OADahSdfZ8Apklk_qPruhF-o1dOSD",
      "monitoringConfig": {}
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html);
    import com.google.cloud.aiplatform.v1.[FeatureName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureName.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[GetFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureRequest.html);
    import java.io.IOException;
    
    public class GetFeatureSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        String featureId = "YOUR_FEATURE_ID";
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
    
        getFeatureSample(project, featurestoreId, entityTypeId, featureId, location, endpoint);
      }
    
      static void getFeatureSample(
          String project,
          String featurestoreId,
          String entityTypeId,
          String featureId,
          String location,
          String endpoint)
          throws IOException {
    
        [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html) featurestoreServiceSettings =
            [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html) featurestoreServiceClient =
            [FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html).create(featurestoreServiceSettings)) {
    
          [GetFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureRequest.html) getFeatureRequest =
              [GetFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetFeatureRequest.html).newBuilder()
                  .setName(
                      [FeatureName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureName.html).of(project, location, featurestoreId, entityTypeId, featureId)
                          .toString())
                  .build();
    
          [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Feature.html) feature = featurestoreServiceClient.getFeature(getFeatureRequest);
          System.out.println("Get Feature Response");
          System.out.println(feature);
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
    // const featureId = 'YOUR_FEATURE_ID';
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
    
    async function getFeature() {
      // Configure the name resource
      const name = `projects/${project}/locations/${location}/featurestores/${featurestoreId}/entityTypes/${entityTypeId}/features/${featureId}`;
    
      const request = {
        name: name,
      };
    
      // Get Feature request
      const [response] = await featurestoreServiceClient.getFeature(request, {
        timeout: Number(timeout),
      });
    
      console.log('Get feature response');
      console.log(`Name : ${response.name}`);
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    getFeature();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

## Delete a feature

Delete a feature and all of its values.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, view the **Feature** column and find the feature to delete.
  4. Click the name of the feature.
  5. From the action bar, click **Delete**.
  6. Click **Confirm** to delete the feature and its values.



### REST

To delete a feature, send a DELETE request by using the [featurestores.entityTypes.features.delete](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes.features/delete) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * FEATURE_ID: ID of the feature.



HTTP method and URL: 
    
    
    DELETE https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features/FEATURE_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features/FEATURE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID/features/FEATURE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.DeleteOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-02-26T17:32:56.008325Z",
          "updateTime": "2021-02-26T17:32:56.008325Z"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty"
      }
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureRequest.html);
    import com.google.cloud.aiplatform.v1.[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[FeatureName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureName.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteFeatureSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        String featureId = "YOUR_FEATURE_ID";
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 300;
    
        deleteFeatureSample(
            project, featurestoreId, entityTypeId, featureId, location, endpoint, timeout);
      }
    
      static void deleteFeatureSample(
          String project,
          String featurestoreId,
          String entityTypeId,
          String featureId,
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
    
          [DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureRequest.html) deleteFeatureRequest =
              [DeleteFeatureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteFeatureRequest.html).newBuilder()
                  .setName(
                      [FeatureName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureName.html).of(project, location, featurestoreId, entityTypeId, featureId)
                          .toString())
                  .build();
    
          OperationFuture<Empty, DeleteOperationMetadata> operationFuture =
              featurestoreServiceClient.deleteFeatureAsync(deleteFeatureRequest);
          System.out.format("Operation name: %s%n", operationFuture.getInitialFuture().get().getName());
          System.out.println("Waiting for operation to finish...");
          operationFuture.get(timeout, TimeUnit.SECONDS);
          System.out.format("Deleted Feature.");
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
    // const featureId = 'YOUR_FEATURE_ID';
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
    
    async function deleteFeature() {
      // Configure the name resource
      const name = `projects/${project}/locations/${location}/featurestores/${featurestoreId}/entityTypes/${entityTypeId}/features/${featureId}`;
    
      const request = {
        name: name,
      };
    
      // Delete Feature request
      const [operation] = await featurestoreServiceClient.deleteFeature(request, {
        timeout: Number(timeout),
      });
      const [response] = await operation.promise();
    
      console.log('Delete feature response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    deleteFeature();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

## What's next

  * Learn how to [batch import feature values](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch).
  * Learn how to [monitor feature values imported over time](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring#feature).
  * Learn how to serve features through [online serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-online) or [batch serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-batch).
  * [Troubleshoot](https://docs.cloud.google.com/vertex-ai/docs/general/troubleshooting#feature-store) common Vertex AI Feature Store (Legacy) issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
