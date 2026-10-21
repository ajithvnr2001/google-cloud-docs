---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-stream/
title: Streaming import \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:06:50.116273+00:00
---

# Streaming import  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-stream/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Streaming import Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

To learn more, run the "Example Feature Store workflow with sample data" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Ffeature_store_legacy%2Fsdk-feature-store.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/feature_store_legacy/sdk-feature-store.ipynb)

Streaming import lets you make real-time updates to feature values. This method is useful when having the latest available data for online serving is a priority. For example, you can import streaming event data and, within a few seconds, Vertex AI Feature Store (Legacy) makes that data available for online serving scenarios.

If you must backfill data or if you compute feature values in batch, use [batch import](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch). Compared to streaming import requests, [batch import](https://docs.cloud.google.com/vertex-ai/docs/featurestore/ingesting-batch) requests can handle larger payloads but take longer to complete.

For information about the oldest feature value timestamp that you can import, see [Vertex AI Feature Store (Legacy)](https://docs.cloud.google.com/vertex-ai/docs/quotas#featurestore) in [Quotas and limits](https://docs.cloud.google.com/vertex-ai/docs/quotas). You can't import feature values for which the timestamps indicate future dates or times.

## Example use case

An online retail organization might provide a personalized shopping experience by using the current activity of a user. As users navigate through the website, you can capture their activity into a featurestore and then, soon after, serve all that information for online predictions. This real-time import and serving can help you show useful and relevant recommendations to customers during their shopping session.

## Online storage node usage

Writing feature values to an online store uses the featurestore's CPU resources (online storage nodes). [Monitor](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring#featurestore) your CPU usage to check that demand doesn't exceed supply, which can lead to serving errors. We recommend around a 70% usage rate or lower to avoid these errors. If you regularly exceed that value, you can update your featurestore to increase the number of nodes or use autoscaling. For more information, see [Manage featurestores](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores).

## Streaming import

Write a value to a particular feature. The feature value must be included as part of the import request. You can't stream data directly from a data source.

If you're writing to recently created features, wait a few minutes before you do so because the new features might not have propagated yet. If you don't, you might see a `resource not found` error.

You can import feature values for only one entity per write. For any specific project and region, you can simultaneously write feature values for multiple entities within a maximum of ten different entity types. This limit includes streaming import requests to all featurestores in a given project and region. If you exceed this limit, Vertex AI Feature Store (Legacy) might not write all of your data to the offline store. If this occurs, Vertex AI Feature Store (Legacy) logs the error in the **Logs Explorer**. For more information, see [Monitor offline storage write errors for streaming import](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring#monitor_offline_storage_write_errors).

### REST

To import feature values for existing features, send a POST request by using the [featurestores.entityTypes.writeFeatureValues](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/writeFeatureValues) method. If the names of the source data columns and the destination feature IDs are different, include the `sourceField` parameter. Note that [featurestores.entityTypes.writeFeatureValues](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/writeFeatureValues) lets you import feature values for only one entity at a time. 

Before using any of the request data, make the following replacements: 

  * LOCATION: Region where the featurestore is created. For example, `us-central1`.
  * PROJECT: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * FEATURE_ID: ID of an existing feature in the featurestore to write values for.
  * VALUE_TYPE: The [value type](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes.features#ValueType) of the feature.
  * VALUE: Value for the feature.
  * TIME_STAMP (optional): The time at which the feature was generated. The timestamp must be in the RFC3339 UTC format.



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:writeFeatureValues

Request JSON body: 
    
    
    {
      "payloads": [
        {
          "entityId": "ENTITY_ID",
          "featureValues": {
            "FEATURE_ID": {
              "VALUE_TYPE": VALUE,
              "metadata": {"generate_time": "TIME_STAMP"}
            }
          }
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
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:writeFeatureValues"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:writeFeatureValues" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    from google.cloud import aiplatform
    
    
    def write_feature_values_sample(
        project: str, location: str, entity_type_id: str, featurestore_id: str
    ):
    
        aiplatform.init(project=project, location=location)
    
        my_entity_type = aiplatform.featurestore.EntityType(
            entity_type_name=entity_type_id, featurestore_id=featurestore_id
        )
    
        my_data = {
            "movie_01": {
                "title": "The Shawshank Redemption",
                "average_rating": 4.7,
                "genre": "Drama",
            },
        }
    
        my_entity_type.write_feature_values(instances=my_data)
    
    

### Additional languages

You can [install](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries) and use the following Vertex AI client libraries to call the Vertex AI API. Cloud Client Libraries provide an optimized developer experience by using the natural conventions and styles of each supported language.

  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/overview)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest)



## What's next

  * Learn how to [monitor offline storage write errors for streaming import](https://docs.cloud.google.com/vertex-ai/docs/featurestore/monitoring#monitor_offline_storage_write_errors).
  * Learn how to serve features through [online serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-online) or [batch serving](https://docs.cloud.google.com/vertex-ai/docs/featurestore/serving-batch).
  * [Troubleshoot](https://docs.cloud.google.com/vertex-ai/docs/general/troubleshooting#feature-store) common Vertex AI Feature Store (Legacy) issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
