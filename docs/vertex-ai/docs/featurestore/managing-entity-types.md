---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-entity-types/
title: Manage entity types \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:31:29.228614+00:00
---

# Manage entity types  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-entity-types/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Manage entity types Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

To learn more, run the "Example Feature Store workflow with sample data" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb)

Learn how to create, list, and delete entity types.

## Create an entity type

Create an entity type so that you can create its related features.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. From the action bar, click **Create entity type** to open the **Create entity type** pane.
  3. Select a region from the **Region** drop-down list that includes the featurestore where you want to create an entity type.
  4. Select a featurestore.
  5. Specify a name for the entity type.
  6. If you want to include a description for the entity type, enter a description.
  7. To enable feature value monitoring ([Preview](https://cloud.google.com/products/#product-launch-stages)), set monitoring to **Enabled** and then specify the snapshot interval in days. This monitoring configuration applies to all features under this entity type. For more information, see [Feature value monitoring](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring#feature).
  8. Click **Create**.



### Terraform

The following sample creates a new featurestore and then uses the [`google_vertex_ai_featurestore_entitytype`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vertex_ai_featurestore_entitytype) Terraform resource to create an entity type named `featurestore_entitytype` within that feature store.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    # Featurestore name must be unique for the project
    resource "random_id" "featurestore_name_suffix" {
      byte_length = 8
    }
    
    resource "google_vertex_ai_featurestore" "featurestore" {
      name   = "featurestore_${random_id.featurestore_name_suffix.hex}"
      region = "us-central1"
      labels = {
        environment = "testing"
      }
    
      online_serving_config {
        fixed_node_count = 1
      }
    
      force_destroy = true
    }
    
    output "featurestore_id" {
      value = google_vertex_ai_featurestore.featurestore.id
    }
    
    resource "google_vertex_ai_featurestore_entitytype" "entity" {
      name = "featurestore_entitytype"
      labels = {
        environment = "testing"
      }
    
      featurestore = google_vertex_ai_featurestore.featurestore.id
    
      monitoring_config {
        snapshot_analysis {
          disabled = false
        }
      }
    
      depends_on = [google_vertex_ai_featurestore.featurestore]
    }

### REST

To create an entity type, send a POST request by using the [featurestores.entityTypes.create](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/create) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * DESCRIPTION: Description of the entity type.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes?entityTypeId=ENTITY_TYPE_ID

Request JSON body: 
    
    
    {
      "description": "DESCRIPTION"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes?entityTypeId=ENTITY_TYPE_ID"

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
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes?entityTypeId=ENTITY_TYPE_ID" | Select-Object -Expand Content

You should see output similar to the following. You can use the OPERATION_ID in the response to [get the status](https://docs.cloud.google.com/vertex-ai/docs/general/long-running-operations) of the operation.
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/bikes/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.CreateEntityTypeOperationMetadata",
        "genericMetadata": {
          "createTime": "2021-03-02T00:04:13.039166Z",
          "updateTime": "2021-03-02T00:04:13.039166Z"
        }
      }
    }
    

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    from google.cloud import aiplatform
    
    
    def create_entity_type_sample(
        project: str,
        location: str,
        entity_type_id: str,
        featurestore_name: str,
    ):
    
        aiplatform.init(project=project, location=location)
    
        my_entity_type = aiplatform.EntityType.create(
            entity_type_id=entity_type_id, featurestore_name=featurestore_name
        )
    
        my_entity_type.wait()
    
        return my_entity_type
    
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.aiplatform.v1.[CreateEntityTypeOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[CreateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeRequest.html);
    import com.google.cloud.aiplatform.v1.[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreName.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateEntityTypeSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        String description = "YOUR_ENTITY_TYPE_DESCRIPTION";
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 300;
        createEntityTypeSample(
            project, featurestoreId, entityTypeId, description, location, endpoint, timeout);
      }
    
      static void createEntityTypeSample(
          String project,
          String featurestoreId,
          String entityTypeId,
          String description,
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
    
          [EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType.html) entityType = [EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType.html).newBuilder().setDescription(description).build();
    
          [CreateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeRequest.html) createEntityTypeRequest =
              [CreateEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEntityTypeRequest.html).newBuilder()
                  .setParent([FeaturestoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreName.html).of(project, location, featurestoreId).toString())
                  .setEntityType(entityType)
                  .setEntityTypeId(entityTypeId)
                  .build();
    
          OperationFuture<EntityType, CreateEntityTypeOperationMetadata> entityTypeFuture =
              featurestoreServiceClient.[createEntityTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html#com_google_cloud_aiplatform_v1_FeaturestoreServiceClient_createEntityTypeAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_FeaturestoreName_com_google_cloud_aiplatform_v1_EntityType_)(createEntityTypeRequest);
          System.out.format(
              "Operation name: %s%n", entityTypeFuture.getInitialFuture().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getName());
          System.out.println("Waiting for operation to finish...");
          [EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType.html) entityTypeResponse = entityTypeFuture.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(timeout, TimeUnit.SECONDS);
          System.out.println("Create Entity Type Response");
          System.out.format("Name: %s%n", entityTypeResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType.html#com_google_cloud_aiplatform_v1_EntityType_getName__)());
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
    
    async function createEntityType() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}/featurestores/${featurestoreId}`;
    
      const entityType = {
        description: description,
      };
    
      const request = {
        parent: parent,
        entityTypeId: entityTypeId,
        entityType: entityType,
      };
    
      // Create EntityType request
      const [operation] = await featurestoreServiceClient.createEntityType(
        request,
        {timeout: Number(timeout)}
      );
      const [response] = await operation.promise();
    
      console.log('Create entity type response');
      console.log(`Name : ${response.name}`);
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    createEntityType();

## List entity types

List all entity types in a featurestore.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, view the **Entity type** column to see the entity types in your project for the selected region.



### REST

To list entity types, send a GET request by using the [featurestores.entityTypes.list](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/list) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.



HTTP method and URL: 
    
    
    GET https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "entityTypes": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID_1",
          "description": "ENTITY_TYPE_DESCRIPTION",
          "createTime": "2021-02-25T01:20:43.082628Z",
          "updateTime": "2021-02-25T01:20:43.082628Z",
          "etag": "AMEw9yOBqKIdbBGZcxdKLrlZJAf9eTO2DEzcE81YDKA2LymDMFB8ucRbmKwKo2KnvOg="
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID_2",
          "description": "ENTITY_TYPE_DESCRIPTION",
          "createTime": "2021-02-25T01:34:26.198628Z",
          "updateTime": "2021-02-25T01:34:26.198628Z",
          "etag": "AMEw9yNuv-ILYG8VLLm1lgIKc7asGIAVFErjvH2Cyc_wIQm7d6DL4ZGv59cwZmxTumU="
        }
      ]
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreName.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[ListEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEntityTypesRequest.html);
    import java.io.IOException;
    
    public class ListEntityTypesSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        listEntityTypesSample(project, featurestoreId, location, endpoint);
      }
    
      static void listEntityTypesSample(
          String project, String featurestoreId, String location, String endpoint) throws IOException {
    
        [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html) featurestoreServiceSettings =
            [FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html) featurestoreServiceClient =
            [FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html).create(featurestoreServiceSettings)) {
    
          [ListEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEntityTypesRequest.html) listEntityTypeRequest =
              [ListEntityTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEntityTypesRequest.html).newBuilder()
                  .setParent([FeaturestoreName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreName.html).of(project, location, featurestoreId).toString())
                  .build();
          System.out.println("List Entity Types Response");
          for ([EntityType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityType.html) element :
              featurestoreServiceClient.listEntityTypes(listEntityTypeRequest).iterateAll()) {
            System.out.println(element);
          }
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
    
    async function listEntityTypes() {
      // Configure the parent resource
      const parent = `projects/${project}/locations/${location}/featurestores/${featurestoreId}`;
    
      const request = {
        parent: parent,
      };
    
      // List EntityTypes request
      const [response] = await featurestoreServiceClient.listEntityTypes(
        request,
        {timeout: Number(timeout)}
      );
    
      console.log('List entity types response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    listEntityTypes();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

## Delete an entity type

Delete an entity type. If you use the Google Cloud console, Vertex AI Feature Store (Legacy) deletes the entity type and all of its contents. If you use the API, enable the `force` query parameter to delete the entity type and all of its contents.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, view the **Entity type** column and find the entity type to delete.
  4. Click the name of the entity type.
  5. From the action bar, click **Delete**.
  6. Click **Confirm** to delete the entity type.



### REST

To delete an entity type, send a DELETE request by using the [featurestores.entityTypes.delete](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/delete) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * BOOLEAN: Whether to delete the entity type even if it contains features. The `force` query parameter is optional and is `false` by default.



HTTP method and URL: 
    
    
    DELETE https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID?force=BOOLEAN

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID?force=BOOLEAN"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID?force=BOOLEAN" | Select-Object -Expand Content

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
    import com.google.cloud.aiplatform.v1.[DeleteEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteEntityTypeRequest.html);
    import com.google.cloud.aiplatform.v1.[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata.html);
    import com.google.cloud.aiplatform.v1.[EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceSettings.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteEntityTypeSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 300;
        deleteEntityTypeSample(project, featurestoreId, entityTypeId, location, endpoint, timeout);
      }
    
      static void deleteEntityTypeSample(
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
    
          [DeleteEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteEntityTypeRequest.html) deleteEntityTypeRequest =
              [DeleteEntityTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteEntityTypeRequest.html).newBuilder()
                  .setName(
                      [EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html).of(project, location, featurestoreId, entityTypeId).toString())
                  .setForce(true)
                  .build();
    
          OperationFuture<Empty, DeleteOperationMetadata> operationFuture =
              featurestoreServiceClient.[deleteEntityTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreServiceClient.html#com_google_cloud_aiplatform_v1_FeaturestoreServiceClient_deleteEntityTypeAsync__org_jspecify_annotations_Nullable_com_google_cloud_aiplatform_v1_EntityTypeName_)(deleteEntityTypeRequest);
          System.out.format("Operation name: %s%n", operationFuture.getInitialFuture().get().getName());
          System.out.println("Waiting for operation to finish...");
          operationFuture.get(timeout, TimeUnit.SECONDS);
    
          System.out.format("Deleted Entity Type.");
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
    // const force = <BOOLEAN>;
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
    
    async function deleteEntityType() {
      // Configure the name resource
      const name = `projects/${project}/locations/${location}/featurestores/${featurestoreId}/entityTypes/${entityTypeId}`;
    
      const request = {
        name: name,
        force: Boolean(force),
      };
    
      // Delete EntityType request
      const [operation] = await featurestoreServiceClient.deleteEntityType(
        request,
        {timeout: Number(timeout)}
      );
      const [response] = await operation.promise();
    
      console.log('Delete entity type response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    deleteEntityType();

### Additional languages

To learn how to install and use the Vertex AI SDK for Python, see [Use the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk). For more information, see the [Vertex AI SDK for Python API reference documentation.](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)

## What's next

  * Learn how to manage [features](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-features).
  * Learn how to [monitor feature values imported over time](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring#feature).
  * View the Vertex AI Feature Store (Legacy) [entity types quota](https://docs.cloud.google.com/vertex-ai/quotas#featurestore).
  * [Troubleshoot](https://docs.cloud.google.com/vertex-ai/docs/general/troubleshooting#feature-store) common Vertex AI Feature Store (Legacy) issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
