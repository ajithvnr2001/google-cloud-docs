---
url: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-example-based/
title: Configure example-based explanations \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:03:41.202879+00:00
---

# Configure example-based explanations  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-example-based/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Configure example-based explanations Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Vertex Explainable AI is deprecated as of March 16, 2026. Access to Vertex Explainable AI will no longer be available on or after March 16, 2027. For more information, see the [deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations) page. 

To use example-based explanations, you must configure explanations by specifying an [`explanationSpec`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models#Model.FIELDS.explanation_spec) when you import or upload the [`Model`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models) resource into the [Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction).

Then, when you request online explanations, you can override some of those configuration values by specifying an [`ExplanationSpecOverride`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/explain#ExplanationSpecOverride) in the request. You cannot request batch explanations; they are not supported.

This page describes how to configure and update these options.

## Configure explanations when importing or uploading the model

Before you begin, make sure that you have following:

  1. A Cloud Storage location that contains your model artifacts. Your model either needs to be a deep neural network (DNN) model where you provide the name of a layer, or signature, whose output can be used as the latent space, or you can provide a model that directly outputs embeddings (latent space representation). This latent space captures the example representations that are used for generating explanations.

  2. A Cloud Storage location that contains the instances to be indexed for approximate nearest neighbor search. For more information, see input data requirements.


**Note:** You must specify either a [`Preset`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#presets) search configuration or the full `NearestNeighborSearchConfig`.**Note:** Allow 1-2 hours for model upload to complete. This step includes two time consuming operations: running a [`batchPredictionJob`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs) to generate the latent representations (embeddings) and using [Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview) to index them for nearest neighbor search. The actual time for your model and data will vary. This is typically the most time consuming step when using example-based explanations. The other steps, such as deploying the model and getting online explanations, don't require batch inference or indexing.

###  Console 

Follow the guide to [importing a model](https://docs.cloud.google.com/vertex-ai/docs/model-registry/import-model#import_a_model_using) using the Google Cloud console.

In the **Explainability** tab, select **Example-based explanation** and fill in the fields.

For information about each field, see the tips in Google Cloud console (shown below) as well as the reference documentation for [`Example`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#examples) and [`ExplanationMetadata`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#explanationmetadata).

![Import model screen in the console showing available options in the Explainability tab.](https://docs.cloud.google.com/static/vertex-ai/docs/explainable-ai/images/import-ebe-model.png)

###  gcloud CLI

  1. Write the following [`ExplanationMetadata`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#explanationmetadata) to a JSON file in your local environment. The filename does not matter, but for this example, call the file `explanation-metadata.json`:


    
    
    {
      "inputs": {
        "my_input": {
          "inputTensorName": "INPUT_TENSOR_NAME",
          "encoding": "IDENTITY",
        },
        "id": {
          "inputTensorName": "id",
          "encoding": "IDENTITY"
        }
      },
      "outputs": {
        "embedding": {
          "outputTensorName": "OUTPUT_TENSOR_NAME"
        }
      }
    }
    

  1. (Optional) If you are specifying the full `NearestNeighborSearchConfig`, write the following to a JSON file in your local environment. The filename does not matter, but for this example, call the file `search_config.json`:


    
    
    {
      "contentsDeltaUri": "",
      "config": {
          "dimensions": 50,
          "approximateNeighborsCount": 10,
          "distanceMeasureType": "SQUARED_L2_DISTANCE",
          "featureNormType": "NONE",
          "algorithmConfig": {
              "treeAhConfig": {
                  "leafNodeEmbeddingCount": 1000,
                  "fractionLeafNodesToSearch": 1.0
              }
          }
        }
      }
    

  1. Run the following command to upload your [`Model`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models#Model).



If you are using a `Preset` search configuration, remove the `--explanation-nearest-neighbor-search-config-file` flag. If you are specifying `NearestNeighborSearchConfig`, remove the `--explanation-modality` and `--explanation-query` flags.

The flags most pertinent to example-based explanations are bolded.
    
    
    gcloud ai models upload \
        --region=LOCATION \
        --display-name=MODEL_NAME \
        --container-image-uri=IMAGE_URI \
        --artifact-uri=MODEL_ARTIFACT_URI \
        **-- explanation-method**=examples \
        **-- uris**=[URI, ...] \
        **-- explanation-neighbor-count**=NEIGHBOR_COUNT \
        **-- explanation-metadata-file**=explanation-metadata.json \
        **-- explanation-modality**=IMAGE|TEXT|TABULAR \
        **-- explanation-query**=PRECISE|FAST \
        **-- explanation-nearest-neighbor-search-config-file**=search_config.json
    

See [gcloud ai models upload](https://docs.cloud.google.com/sdk/gcloud/reference/ai/models/upload) for more information.

  1. The upload action returns an `OPERATION_ID` that can be used to check when the operation is finished. You can poll for the status of the operation until the response includes `"done": true`. Use the [gcloud ai operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/ai/operations/describe) command to poll the status, for example: 
         
         gcloud ai operations describe <operation-id>
         

You will not be able to request explanations until the operation is done. Depending on the size of the dataset and model architecture, this step can take several hours to build the index used to query for examples. 




###  REST 

Before using any of the request data, make the following replacements: 

  * PROJECT
  * LOCATION



To learn about the other placeholders, see [`Model`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models#Model), [`explanationSpec`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec), and [`Examples`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#examples).

To learn more about uploading models, see the [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload) method and [Importing models](https://docs.cloud.google.com/vertex-ai/docs/model-registry/import-model).

The JSON request body below specifies a `Preset` search configuration. Alternatively, you can specify the full`NearestNeighborSearchConfig`. 

HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/models:upload

Request JSON body: 
    
    
    {
      "model": {
        "displayName": "my-model",
        "artifactUri": "gs://your-model-artifact-folder",
        "containerSpec": {
          "imageUri": "us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-11:latest",
        },
        "explanationSpec": {
          "parameters": {
            "examples": {
              "gcsSource": {
                "uris": ["gs://your-examples-folder"]
              },
              "neighborCount": 10,
              "presets": {
                "modality": "image"
              }
            }
          },
          "metadata": {
            "outputs": {
                "embedding": {
                    "output_tensor_name": "embedding"
                }
            },
            "inputs": {
              "my_fancy_input": {
                "input_tensor_name": "input_tensor_name",
                "encoding": "identity",
                "modality": "image"
              },
              "id": {
                "input_tensor_name": "id",
                "encoding": "identity"
              }
            }
          }
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/models:upload"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/models:upload" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/models/MODEL_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1.UploadModelOperationMetadata",
        "genericMetadata": {
          "createTime": "2022-01-08T01:21:10.147035Z",
          "updateTime": "2022-01-08T01:21:10.147035Z"
        }
      }
    }
    

The upload action returns an `OPERATION_ID` that can be used to check when the operation is finished. You can poll for the status of the operation until the response includes `"done": true`. Use the [gcloud ai operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/ai/operations/describe) command to poll the status, for example:
    
    
    gcloud ai operations describe <operation-id>
    

You will not be able to request explanations until the operation is done. Depending on the size of the dataset and model architecture, this step can take several hours to build the index used to query for examples. 

###  Python 

See the section **Upload the model** in the [image classification example-based explanations notebook](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/gapic/custom/showcase_custom_image_classification_online_explain_example_based_api.ipynb).

### `NearestNeighborSearchConfig`

The following JSON request body demonstrates how to specify the full `NearestNeighborSearchConfig` (instead of presets) in an [`upload`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/upload#request-body) request.
    
    
    {
      "model": {
        "displayName": displayname,
        "artifactUri": model_path_to_deploy,
        "containerSpec": {
          "imageUri": DEPLOY_IMAGE,
        },
        "explanationSpec": {
          "parameters": {
            "examples": {
              "gcsSource": {
                "uris": [DATASET_PATH]
              },
              "neighborCount": 5,
              "nearest_neighbor_search_config": {
                "contentsDeltaUri": "",
                "config": {
                  "dimensions": dimensions,
                  "approximateNeighborsCount": 10,
                  "distanceMeasureType": "SQUARED_L2_DISTANCE",
                  "featureNormType": "NONE",
                  "algorithmConfig": {
                      "treeAhConfig": {
                          "leafNodeEmbeddingCount": 1000,
                          "fractionLeafNodesToSearch": 1.0
                      }
                    }
                  }
              }
            }
          },
          "metadata": { ... }
        }
      }
    }
    

These tables list the fields for `NearestNeighborSearchConfig`.

Fields  
---  
`dimensions` |  `int32` Required. The number of dimensions of the input vectors. Used for dense embeddings only.   
`approximateNeighborsCount` |  `int32` Required if tree-AH algorithm is used. The default number of neighbors to find through approximate search before exact reordering is performed. Exact reordering is a procedure where results returned by an approximate search algorithm are reordered using a more expensive distance computation.   
`ShardSize` |  [`ShardSize`](https://docs.cloud.google.com/vertex-ai/docs/vector-search/configuring-indexes#shard-size) The size of each shard. When an index is large, it is sharded based on the specified shard size. During serving, each shard is served on a separate node and scales independently.   
`distanceMeasureType` |  [`DistanceMeasureType`](https://docs.cloud.google.com/vertex-ai/docs/vector-search/configuring-indexes#distance-measure-type) The distance measure used in nearest neighbor search.  
`featureNormType` |  [`FeatureNormType`](https://docs.cloud.google.com/vertex-ai/docs/vector-search/configuring-indexes#feature-norm-type) Type of normalization to be carried out on each vector.   
`algorithmConfig` |  `oneOf:`

  * [`TreeAhConfig`](https://docs.cloud.google.com/vertex-ai/docs/vector-search/configuring-indexes#tree-ah-config)
  * [`BruteForceConfig`](https://docs.cloud.google.com/vertex-ai/docs/vector-search/configuring-indexes#brute-force-config)

The configuration for the algorithms that Vector Search uses for efficient search. Used for dense embeddings only.

  * `TreeAhConfig`: Configuration options for using the tree-AH algorithm. For more information, see this blog [Scaling deep retrieval with TensorFlow Recommenders and Vector Search](https://cloud.google.com/blog/products/ai-machine-learning/scaling-deep-retrieval-tensorflow-two-towers-architecture)
  * `BruteForceConfig`: This option implements the standard linear search in the database for each query. There are no fields to configure for a brute force search. To select this algorithm, pass an empty object for `BruteForceConfig`. 

  
  
#### `DistanceMeasureType`

Enums  
---  
`SQUARED_L2_DISTANCE` | Euclidean (L2) Distance  
`L1_DISTANCE` | Manhattan (L1) Distance  
`DOT_PRODUCT_DISTANCE` | Default value. Defined as a negative of the dot product. Note that a sparse index only supports dot product distance.  
`COSINE_DISTANCE` | Cosine Distance. We strongly suggest using DOT_PRODUCT_DISTANCE + UNIT_L2_NORM instead of the COSINE distance. Our algorithms have been more optimized for the DOT_PRODUCT distance, and when combined with UNIT_L2_NORM, it offers the same ranking and mathematical equivalence as the COSINE distance.   
  
#### `FeatureNormType`

Enums  
---  
`UNIT_L2_NORM` | Unit L2 normalization type.  
`NONE` |  Default value. No normalization type is specified.   
  
#### `TreeAhConfig`

These are the fields to select for the tree-AH algorithm (Shallow tree + Asymmetric Hashing). 

Fields  
---  
`fractionLeafNodesToSearch` | `double`  
|  The default fraction of leaf nodes that any query may be searched. Must be in range 0.0 - 1.0, exclusive. The default value is 0.05 if not set.   
`leafNodeEmbeddingCount` | `int32`  
|  Number of embeddings on each leaf node. The default value is 1000 if not set.   
`leafNodesToSearchPercent` | `int32`  
|  Deprecated, use `fractionLeafNodesToSearch`.  
  
The default percentage of leaf nodes that any query may be searched. Must be in range 1-100, inclusive. The default value is 10 (means 10%) if not set.   
  
#### `BruteForceConfig`

This option implements the standard linear search in the database for each query. There are no fields to configure for a brute force search. To select this algorithm, pass an empty object for `BruteForceConfig` to `algorithmConfig`.

### Input data requirements

Upload your dataset to a Cloud Storage location. Make sure the files in the JSON Lines format.

The files must be in JSON Lines format. The following sample is from the [image classification example-based explanations notebook](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/gapic/custom/showcase_custom_image_classification_online_explain_example_based_api.ipynb):
    
    
    {"id": "0", "bytes_inputs": {"b64": "..."}}
    {"id": "1", "bytes_inputs": {"b64": "..."}}
    {"id": "2", "bytes_inputs": {"b64": "..."}}
    

## Update the index or configuration

Vertex AI lets you update a model's nearest neighbor index or [`Example`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#examples) configuration. This is useful if you'd like to update your model without re-indexing its dataset. For example, if your model's index contains 1,000 instances, and you'd like to add 500 more instances, you can call [`UpdateExplanationDataset`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/updateExplanationDataset) to add to the index without re-processing the original 1,000 instances.

To update the explanation dataset:

### Python
    
    
    def update_explanation_dataset(model_id, new_examples):
        response = clients["model"].update_explanation_dataset(model=model_id,  examples=new_examples)
        update_dataset_response = response.result()
        return update_dataset_response
    
    PRESET_CONFIG = {
        "modality": "TEXT",
        "query": "FAST"
    }
    NEW_DATASET_FILE_PATH = "new_dataset_path"
    NUM_NEIGHBORS_TO_RETURN = 10
    
    EXAMPLES = aiplatform.Examples(presets=PRESET_CONFIG,
                                        gcs_source=aiplatform.types.io.GcsSource(uris=[NEW_DATASET_FILE_PATH]),
                                          neighbor_count=NUM_NEIGHBORS_TO_RETURN)
    
    MODEL_ID = 'model_id'
    update_dataset_response = update_explanation_dataset(MODEL_ID, EXAMPLES)
    

Usage notes:

  * The `model_id` remains unchanged after the [`UpdateExplanationDataset`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/updateExplanationDataset) operation.

  * The `UpdateExplanationDataset` operation affects only the [`Model`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models) resource; it does not update any associated [`DeployedModel`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/deployModel)s. This means that a `deployedModel`'s index contains the dataset at the time it was deployed. To update a `deployedModel`'s index, you must re-deploy the updated model to an endpoint.




## Override the configuration when getting online explanations

When you request an explanation, you can override some of the parameters on the fly by specifying the [`ExplanationSpecOverride`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/explain#ExplanationSpecOverride) field.

Depending on the application, some constraints might be desirable on the kind of explanations that are returned. For example, to ensure diversity of explanations, a user can specify a crowding parameter which dictates that no single type of examples are over-represented in the explanations. Concretely, if a user is trying to understand why a bird was labeled as a plane by their model, they might not be interested in seeing too many bird examples as explanations to better investigate the root cause.

The following table summarizes the parameters that can be overridden for an example-based explanation request:

Property Name | Property Value | Description  
---|---|---  
neighborCount | `int32` | The number of examples to return as explanation  
crowdingCount | `int32` | Maximum number of examples to return with the same crowding tag  
allow | `String Array` | The tags that are allowed for explanations to have  
deny | `String Array` | The tags that are not allowed for explanations to have  
  
The [Vector Search Filtering](https://docs.cloud.google.com/vertex-ai/docs/vector-search/filtering#json) describes these parameters in more details.

Here's an example of a JSON request body with overrides:
    
    
    {
      "instances":[
        {
          "id": data[0]["id"],
          "bytes_inputs": {"b64": bytes},
          "restricts": "",
          "crowding_tag": ""
        }
      ],
      "explanation_spec_override": {
        "examples_override": {
          "neighbor_count": 5,
          "crowding_count": 2,
          "restrictions": [
            {
              "namespace_name": "label",
              "allow": ["Papilloma", "Rift_Valley", "TBE", "Influenza", "Ebol"]
            }
          ]
        }
      }
    }
    
    

## What's next

  * [Deploy your `Model` to an `Endpoint`](https://docs.cloud.google.com/vertex-ai/docs/predictions/deploy-model-api) and [get example-based explanations](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-online-predictions#explain-request).



Here's an example of the response from an example-based [`explain`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/explain) request:
    
    
    [
       {
          "neighbors":[
             {
                "neighborId":"311",
                "neighborDistance":383.8
             },
             {
                "neighborId":"286",
                "neighborDistance":431.4
             }
          ],
          "input":"0"
       },
       {
          "neighbors":[
             {
                "neighborId":"223",
                "neighborDistance":471.6
             },
             {
                "neighborId":"55",
                "neighborDistance":392.7
             }
          ],
          "input":"1"
       }
    ]
    

## Pricing

See the section on example-based explanations in the [pricing page](https://cloud.google.com/vertex-ai/pricing#explanations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-15 UTC."],[],[]] 
