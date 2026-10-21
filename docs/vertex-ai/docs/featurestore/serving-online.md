---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-online/
title: Online serving \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:07:44.150097+00:00
---

# Online serving  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-online/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Online serving Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

To learn more, run the "Example Feature Store workflow with sample data" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb)

Online serving lets you serve feature values for small batches of entities at low latency. For each request, you can only serve feature values from a single entity type. Vertex AI Feature Store (Legacy) returns only the latest _non-null_ value of each feature.

Typically, you use online serving to serve feature values to deployed models for online inferences. For example, you might have a bike-sharing company and you want to predict how long a particular user will rent a bike. You can include real-time inputs from the user and data from the featurestore to perform an online inference. That way, you can determine resource allocation in real time.

## Null values

For online serving results, if the latest value for a feature is null, Vertex AI Feature Store (Legacy) returns the latest non-null value. If there is no previous value, Vertex AI Feature Store (Legacy) returns null.

## Before you begin

Check that the featurestore you're making calls against has an online store (the number of nodes must be greater than `0`). Otherwise, online serving requests return an error. For more info, see [Manage featurestores](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores).

## Serve values from a single entity

Serve feature values from a single entity for a particular entity type.

### REST

To get feature values from an entity, send a POST request by using the [featurestores.entityTypes.readFeatureValues](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/readFeatureValues) method. 

The following sample gets the latest values for two different features for a particular entity. Note that for the `ids` field you can specify `["*"]` instead of the feature IDs to select all features for the entity. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is created. For example, `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * ENTITY_ID: ID of the entity to get feature values for.
  * FEATURE_ID: ID of feature to get values for.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:readFeatureValues

Request JSON body: 
    
    
    {
      "entityId": "ENTITY_ID",
      "featureSelector": {
        "idMatcher": {
          "ids": ["FEATURE_ID_1", "FEATURE_ID_2"]
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
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:readFeatureValues"

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
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:readFeatureValues" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "header": {
        "entityType": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID",
        "featureDescriptors": [
          {
            "id": "FEATURE_ID_1"
          },
          {
            "id": "FEATURE_ID_2"
          }
        ]
      },
      "entityView": {
        "entityId": "ENTITY_ID",
        "data": [
          {
            "value": {
              "VALUE_TYPE_1": "FEATURE_VALUE_1",
              "metadata": {
                "generateTime": "2019-10-28T15:38:10Z"
              }
            }
          },
          {
            "value": {
              "VALUE_TYPE_2": "FEATURE_VALUE_2",
              "metadata": {
                "generateTime": "2019-10-28T15:38:10Z"
              }
            }
          }
        ]
      }
    }
    

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    from typing import List, Union
    
    from google.cloud import aiplatform
    
    
    def read_feature_values_sample(
        project: str,
        location: str,
        entity_type_id: str,
        featurestore_id: str,
        entity_ids: Union[str, List[str]],
        feature_ids: Union[str, List[str]] = "*",
    ):
    
        aiplatform.init(project=project, location=location)
    
        my_entity_type = aiplatform.featurestore.EntityType(
            entity_type_name=entity_type_id, featurestore_id=featurestore_id
        )
    
        my_dataframe = my_entity_type.read(entity_ids=entity_ids, feature_ids=feature_ids)
    
        return my_dataframe
    
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html);
    import com.google.cloud.aiplatform.v1.[FeatureSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceClient.html);
    import com.google.cloud.aiplatform.v1.[FeaturestoreOnlineServingServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[IdMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IdMatcher.html);
    import com.google.cloud.aiplatform.v1.[ReadFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesRequest.html);
    import com.google.cloud.aiplatform.v1.[ReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesResponse.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeoutException;
    
    public class ReadFeatureValuesSample {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        // Feature Store ID
        String featurestoreId = "YOUR_FEATURESTORE_ID";
        // Entity Type ID
        String entityTypeId = "YOUR_ENTITY_TYPE_ID";
        // Entity ID
        String entityId = "YOUR_ENTITY_ID";
        // Features to read with batch or online serving.
        List<String> featureSelectorIds = Arrays.asList("title", "genres", "average_rating");
        String location = "us-central1";
        String endpoint = "us-central1-aiplatform.googleapis.com:443";
        int timeout = 300;
    
        readFeatureValuesSample(
            project,
            featurestoreId,
            entityTypeId,
            entityId,
            featureSelectorIds,
            location,
            endpoint,
            timeout);
      }
    
      /*
       * Reads Feature values of a specific entity of an EntityType.
       * See: https://cloud.google.com/vertex-ai/docs/featurestore/serving-online
       */
      public static void readFeatureValuesSample(
          String project,
          String featurestoreId,
          String entityTypeId,
          String entityId,
          List<String> featureSelectorIds,
          String location,
          String endpoint,
          int timeout)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        [FeaturestoreOnlineServingServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceSettings.html) featurestoreOnlineServiceSettings =
            [FeaturestoreOnlineServingServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceSettings.html).newBuilder().setEndpoint(endpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceClient.html) featurestoreOnlineServiceClient =
            [FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeaturestoreOnlineServingServiceClient.html).create(featurestoreOnlineServiceSettings)) {
          [ReadFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesRequest.html) readFeatureValuesRequest =
              [ReadFeatureValuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesRequest.html).newBuilder()
                  .setEntityType(
                      [EntityTypeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EntityTypeName.html).of(project, location, featurestoreId, entityTypeId).toString())
                  .setEntityId(entityId)
                  .setFeatureSelector(
                      [FeatureSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.html).newBuilder()
                          .[setIdMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FeatureSelector.Builder.html#com_google_cloud_aiplatform_v1_FeatureSelector_Builder_setIdMatcher_com_google_cloud_aiplatform_v1_IdMatcher_)([IdMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IdMatcher.html).newBuilder().addAllIds(featureSelectorIds)))
                  .build();
    
          [ReadFeatureValuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReadFeatureValuesResponse.html) readFeatureValuesResponse =
              featurestoreOnlineServiceClient.readFeatureValues(readFeatureValuesRequest);
          System.out.println("Read Feature Values Response" + readFeatureValuesResponse);
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
    // const entityId = 'ENTITY_ID_TO_SERVE';
    // const location = 'YOUR_PROJECT_LOCATION';
    // const apiEndpoint = 'YOUR_API_ENDPOINT';
    // const timeout = <TIMEOUT_IN_MILLI_SECONDS>;
    
    // Imports the Google Cloud Featurestore Service Client library
    const {FeaturestoreOnlineServingServiceClient} =
      require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)').v1;
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: apiEndpoint,
    };
    
    // Instantiates a client
    const featurestoreOnlineServingServiceClient =
      new [FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function readFeatureValues() {
      // Configure the entityType resource
      const entityType = `projects/${project}/locations/${location}/featurestores/${featurestoreId}/entityTypes/${entityTypeId}`;
    
      const featureSelector = {
        idMatcher: {
          ids: ['age', 'gender', 'liked_genres'],
        },
      };
    
      const request = {
        entityType: entityType,
        entityId: entityId,
        featureSelector: featureSelector,
      };
    
      // Read Feature Values Request
      const [response] =
        await featurestoreOnlineServingServiceClient.readFeatureValues(request, {
          timeout: Number(timeout),
        });
    
      console.log('Read feature values response');
      console.log('Raw response:');
      console.log(JSON.stringify(response, null, 2));
    }
    readFeatureValues();

## Serve values from multiple entities

Serve feature values from one or more entities for a particular entity type. For better performance, use the `streamingReadFeatureValues` method instead of sending parallel requests to the `readFeatureValues` method.

### REST

To get feature values from multiple entities, send a POST request by using the [featurestores.entityTypes.streamingReadFeatureValues](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/streamingReadFeatureValues) method. 

The following sample gets the latest values for two different features for two different entities. Note that for the `ids` field you can specify `["*"]` instead of the feature IDs to select all features for the entity. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is created. For example, `us-central1`.
  * PROJECT_ID: .
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * ENTITY_ID: ID of the entity to get feature values for.
  * FEATURE_ID: ID of feature to get values for.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:streamingReadFeatureValues

Request JSON body: 
    
    
    {
      "entityIds": ["ENTITY_ID_1", "ENTITY_ID_2"],
      "featureSelector": {
        "idMatcher": {
          "ids": ["FEATURE_ID_1", "FEATURE_ID_2"]
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
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:streamingReadFeatureValues"

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
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:streamingReadFeatureValues" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    [{
      "header": {
        "entityType": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID",
        "featureDescriptors": [
          {
            "id": "FEATURE_ID_1"
          },
          {
            "id": "FEATURE_ID_2"
          }
        ]
      }
    },
    {
      "entityView": {
        "entityId": "ENTITY_ID_1",
        "data": [
          {
            "value": {
              "VALUE_TYPE_1": "FEATURE_VALUE_A",
              "metadata": {
                "generateTime": "2019-10-28T15:38:10Z"
              }
            }
          },
          {
            "value": {
              "VALUE_TYPE_2": "FEATURE_VALUE_B",
              "metadata": {
                "generateTime": "2019-10-28T15:38:10Z"
              }
            }
          }
        ]
      }
    },
    {
      "entityView": {
        "entityId": "ENTITY_ID_2",
        "data": [
          {
            "value": {
              "VALUE_TYPE_1": "FEATURE_VALUE_C",
              "metadata": {
                "generateTime": "2019-10-28T21:21:37Z"
              }
            }
          },
          {
            "value": {
              "VALUE_TYPE_2": "FEATURE_VALUE_D",
              "metadata": {
                "generateTime": "2019-10-28T21:21:37Z"
              }
            }
          }
        ]
      }
    }]
    

### Additional languages

You can [install](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries) and use the following Vertex AI client libraries to call the Vertex AI API. Cloud Client Libraries provide an optimized developer experience by using the natural conventions and styles of each supported language.

  * [Vertex AI SDK for Python](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/overview)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest)



## What's next

  * Learn how to [batch ingest feature values](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch).
  * Learn how to serve features through [batch serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-batch).
  * View the Vertex AI Feature Store (Legacy) [online serving quotas](https://docs.cloud.google.com/vertex-ai/quotas#featurestore).
  * [Troubleshoot](https://docs.cloud.google.com/vertex-ai/docs/general/troubleshooting#feature-store) common Vertex AI Feature Store (Legacy) issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
