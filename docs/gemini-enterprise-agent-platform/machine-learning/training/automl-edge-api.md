---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-edge-api/
title: Train an AutoML Edge model using the Agent Platform API \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:44:33.954121+00:00
---

# Train an AutoML Edge model using the Agent Platform API  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-edge-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Train an AutoML Edge model using the Agent Platform API Stay organized with collections  Save and categorize content based on your preferences. 

You create an AutoML model directly in the [Google Cloud console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-edge-console), or by creating a training pipeline programmatically, using the API or one of the [Agent Platform client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries).

This model is created using a prepared dataset provided by you using the [console](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/automl-edge-console) or the Agent Platform API. The Agent Platform API uses the items from the dataset to train the model, test it, and evaluate model performance. Review the evaluations results, adjust the training dataset as needed, and create a new training pipeline using the improved dataset.

Model training can take several hours to complete. The Agent Platform API lets you get the status of the training job.

**Note:** AutoML Edge object detection is in maintenance mode. Only severe failures will be addressed. We recommend migrating to alternative solutions such as open source (OSS) models.

## Create an AutoML Edge training pipeline

When you have a dataset with a representative set of training items, you are ready to create an AutoML Edge training pipeline.

Select the tab below for your objective:

### Classification

At training time you can choose the type of AutoML Edge model you want, depending on your specific use case:

  * low latency (`MOBILE_TF_LOW_LATENCY_1`)
  * general purpose usage (`MOBILE_TF_VERSATILE_1`)
  * higher prediction quality (`MOBILE_TF_HIGH_ACCURACY_1`)



Select the tab below for your language or environment:

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: Region where dataset is located and Model is created. For example, `us-central1`.
  * PROJECT: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * TRAININGPIPELINE_DISPLAYNAME: Required. A display name for the trainingPipeline. 
  * DATASET_ID: The ID number for the dataset to use for training.
  * fractionSplit: Optional. One of several possible ML use [split options](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines#inputdataconfig) for your data. For `fractionSplit`, values must sum to 1. For example: 
    * `{"trainingFraction": "0.7","validationFraction": "0.15","testFraction": "0.15"}`
  * MODEL_DISPLAYNAME*: A display name for the model uploaded (created) by the TrainingPipeline.
  * MODEL_DESCRIPTION*: A description for the model.
  * modelToUpload.labels*: Any set of key-value pairs to organize your models. For example: 
    * "env": "prod"
    * "tier": "backend"
  * EDGE_MODELTYPE†: The type of Edge model to train. The options are: 
    * `MOBILE_TF_LOW_LATENCY_1`
    * `MOBILE_TF_VERSATILE_1`
    * `MOBILE_TF_HIGH_ACCURACY_1`
  * NODE_HOUR_BUDGET†: The actual training cost will be equal or less than this value. For Edge models the budget must be: 1,000 - 100,000 milli node hours (inclusive). 
  * PROJECT_NUMBER: Your project's automatically generated [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers)

* | Schema file's description you specify in `trainingTaskDefinition` describes the use of this field.  
---|---  
† | Schema file you specify in `trainingTaskDefinition` declares and describes this field.  
  
HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines

Request JSON body: 
    
    
    {
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": "DECIMAL",
          "validationFraction": "DECIMAL",
          "testFraction": "DECIMAL"
        }
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "description": "MODEL_DESCRIPTION",
        "labels": {
          "KEY": "VALUE"
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml",
      "trainingTaskInputs": {
        "multiLabel": "false",
        "modelType": ["EDGE_MODELTYPE"],
        "budgetMilliNodeHours": NODE_HOUR_BUDGET
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
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines" | Select-Object -Expand Content

The response contains information about specifications as well as the TRAININGPIPELINE_ID. 

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID",
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": 0.7,
          "validationFraction": 0.15,
          "testFraction": 0.15
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml",
      "trainingTaskInputs": {
        "modelType": "EDGE_MODELTYPE",
        "budgetMilliNodeHours": "NODE_HOUR_BUDGET"
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "labels": {
          "KEY1": "VALUE1",
          "KEY2": "VALUE2"
        }
      },
      "state": "PIPELINE_STATE_PENDING",
      "createTime": "2020-07-14T17:16:55.098953Z",
      "updateTime": "2020-07-14T17:16:55.098953Z"
    }
    

You can get the status of the trainingPipeline job using the TRAININGPIPELINE_ID.

### Classification

At training time you can choose the type of AutoML Edge model you want, depending on your specific use case:

  * low latency (`MOBILE_TF_LOW_LATENCY_1`)
  * general purpose usage (`MOBILE_TF_VERSATILE_1`)
  * higher prediction quality (`MOBILE_TF_HIGH_ACCURACY_1`)



Select the tab below for your language or environment:

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: Region where dataset is located and Model is created. For example, `us-central1`.
  * PROJECT: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * TRAININGPIPELINE_DISPLAYNAME: Required. A display name for the trainingPipeline. 
  * DATASET_ID: The ID number for the dataset to use for training.
  * fractionSplit: Optional. One of several possible ML use [split options](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines#inputdataconfig) for your data. For `fractionSplit`, values must sum to 1. For example: 
    * `{"trainingFraction": "0.7","validationFraction": "0.15","testFraction": "0.15"}`
  * MODEL_DISPLAYNAME*: A display name for the model uploaded (created) by the TrainingPipeline.
  * MODEL_DESCRIPTION*: A description for the model.
  * modelToUpload.labels*: Any set of key-value pairs to organize your models. For example: 
    * "env": "prod"
    * "tier": "backend"
  * EDGE_MODELTYPE†: The type of Edge model to train. The options are: 
    * `MOBILE_TF_LOW_LATENCY_1`
    * `MOBILE_TF_VERSATILE_1`
    * `MOBILE_TF_HIGH_ACCURACY_1`
  * NODE_HOUR_BUDGET†: The actual training cost will be equal or less than this value. For Edge models the budget must be: 1,000 - 100,000 milli node hours (inclusive). 
  * PROJECT_NUMBER: Your project's automatically generated [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers)

* | Schema file's description you specify in `trainingTaskDefinition` describes the use of this field.  
---|---  
† | Schema file you specify in `trainingTaskDefinition` declares and describes this field.  
  
HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines

Request JSON body: 
    
    
    {
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": "DECIMAL",
          "validationFraction": "DECIMAL",
          "testFraction": "DECIMAL"
        }
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "description": "MODEL_DESCRIPTION",
        "labels": {
          "KEY": "VALUE"
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml",
      "trainingTaskInputs": {
        "multiLabel": "true",
        "modelType": ["EDGE_MODELTYPE"],
        "budgetMilliNodeHours": NODE_HOUR_BUDGET
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
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines" | Select-Object -Expand Content

The response contains information about specifications as well as the TRAININGPIPELINE_ID. 

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID",
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": 0.7,
          "validationFraction": 0.15,
          "testFraction": 0.15
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml",
      "trainingTaskInputs": {
        "modelType": "EDGE_MODELTYPE",
        "budgetMilliNodeHours": "NODE_HOUR_BUDGET"
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "labels": {
          "KEY1": "VALUE1",
          "KEY2": "VALUE2"
        }
      },
      "state": "PIPELINE_STATE_PENDING",
      "createTime": "2020-07-14T17:16:55.098953Z",
      "updateTime": "2020-07-14T17:16:55.098953Z"
    }
    

You can get the status of the trainingPipeline job using the TRAININGPIPELINE_ID.

### Object detection

At training time you can choose the type of AutoML Edge model you want, depending on your specific use case:

  * low latency (`MOBILE_TF_LOW_LATENCY_1`)
  * general purpose usage (`MOBILE_TF_VERSATILE_1`)
  * higher prediction quality (`MOBILE_TF_HIGH_ACCURACY_1`)



Select the tab below for your language or environment:

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: Region where dataset is located and Model is created. For example, `us-central1`.
  * PROJECT: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * TRAININGPIPELINE_DISPLAYNAME: Required. A display name for the trainingPipeline. 
  * DATASET_ID: The ID number for the dataset to use for training.
  * `fractionSplit`: Optional. One of several possible ML use [split options](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.trainingPipelines#inputdataconfig) for your data. For `fractionSplit`, values must sum to 1. For example: 
    * `{"trainingFraction": "0.7","validationFraction": "0.15","testFraction": "0.15"}`
  * MODEL_DISPLAYNAME*: A display name for the model uploaded (created) by the TrainingPipeline.
  * MODEL_DESCRIPTION*: A description for the model.
  * modelToUpload.labels*: Any set of key-value pairs to organize your models. For example: 
    * "env": "prod"
    * "tier": "backend"
  * EDGE_MODELTYPE†: The type of Edge model to train. The options are: 
    * `MOBILE_TF_LOW_LATENCY_1`
    * `MOBILE_TF_VERSATILE_1`
    * `MOBILE_TF_HIGH_ACCURACY_1`
  * NODE_HOUR_BUDGET†: The actual training cost will be equal or less than this value. For Cloud models the budget must be: 20,000 - 900,000 milli node hours (inclusive). The default value is 216,000 which represents one day in wall time, assuming 9 nodes are used. 
  * PROJECT_NUMBER: Your project's automatically generated [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers)

* | Schema file's description you specify in `trainingTaskDefinition` describes the use of this field.  
---|---  
† | Schema file you specify in `trainingTaskDefinition` declares and describes this field.  
  
HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines

Request JSON body: 
    
    
    {
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": "DECIMAL",
          "validationFraction": "DECIMAL",
          "testFraction": "DECIMAL"
        }
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "description": "MODEL_DESCRIPTION",
        "labels": {
          "KEY": "VALUE"
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_object_detection_1.0.0.yaml",
      "trainingTaskInputs": {
        "modelType": ["EDGE_MODELTYPE"],
        "budgetMilliNodeHours": NODE_HOUR_BUDGET
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
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines" | Select-Object -Expand Content

The response contains information about specifications as well as the TRAININGPIPELINE_ID. 

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID",
      "displayName": "TRAININGPIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": 0.7,
          "validationFraction": 0.15,
          "testFraction": 0.15
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_object_detection_1.0.0.yaml",
      "trainingTaskInputs": {
        "modelType": "EDGE_MODELTYPE",
        "budgetMilliNodeHours": "NODE_HOUR_BUDGET"
      },
      "modelToUpload": {
        "displayName": "MODEL_DISPLAYNAME",
        "labels": {
          "KEY1": "VALUE1",
          "KEY2": "VALUE2"
        }
      },
      "state": "PIPELINE_STATE_PENDING",
      "createTime": "2020-07-14T17:16:55.098953Z",
      "updateTime": "2020-07-14T17:16:55.098953Z"
    }
    

You can get the status of the trainingPipeline job using the TRAININGPIPELINE_ID.

## Get `trainingPipeline` status

Use the following code to programmatically get the status of `trainingPipeline` creation.

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: Region where TrainingPipeline is located.
  * PROJECT: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * TRAININGPIPELINE_ID: The ID of the specific TrainingPipeline.
  * PROJECT_NUMBER: Your project's automatically generated [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers)



HTTP method and URL: 
    
    
    GET https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID" | Select-Object -Expand Content

The `"state"` field shows the current status of the operation. A completed trainingPipeline shows 

You should see output similar to the following for a completed **create trainingPipeline operation** : 

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID",
      "displayName": "PIPELINE_DISPLAYNAME",
      "inputDataConfig": {
        "datasetId": "DATASET_ID",
        "fractionSplit": {
          "trainingFraction": 0.7,
          "validationFraction": 0.15,
          "testFraction": 0.15
        }
      },
      "trainingTaskDefinition": "gs://google-cloud-aiplatform/schema/trainingjob/definition/automl_image_classification_1.0.0.yaml",
      "trainingTaskInputs": {
        "modelType": "MOBILE_TF_VERSATILE_1",
        "budgetMilliNodeHours": "1000"
      },
      "modelToUpload": {
        "name": "projects/PROJECT_NUMBER/locations/LOCATION/models/4030440191519883264",
        "displayName": "image_classification_edge_model1",
        "labels": {
          "env": "prod",
          "tier": "backend"
        }
      },**"state": "PIPELINE_STATE_SUCCEEDED",**
      "createTime": "2020-07-14T17:16:55.098953Z",
      "startTime": "2020-07-14T17:16:55.360691Z",
      "endTime": "2020-07-14T18:46:08.169170Z",
      "updateTime": "2020-07-14T18:46:08.169170Z"
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). For more information, see the [Agent Platform Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[DeployedModelRef](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelRef.html);
    import com.google.cloud.aiplatform.v1.[EnvVar](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EnvVar.html);
    import com.google.cloud.aiplatform.v1.[FilterSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html);
    import com.google.cloud.aiplatform.v1.[FractionSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html);
    import com.google.cloud.aiplatform.v1.[InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html);
    import com.google.cloud.aiplatform.v1.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html);
    import com.google.cloud.aiplatform.v1.[ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html);
    import com.google.cloud.aiplatform.v1.[PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[Port](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Port.html);
    import com.google.cloud.aiplatform.v1.[PredefinedSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html);
    import com.google.cloud.aiplatform.v1.[PredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html);
    import com.google.cloud.aiplatform.v1.[TimestampSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html);
    import com.google.cloud.aiplatform.v1.[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html);
    import com.google.cloud.aiplatform.v1.[TrainingPipelineName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipelineName.html);
    import com.google.rpc.[Status](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html);
    import java.io.IOException;
    
    public class GetTrainingPipelineSample {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String trainingPipelineId = "YOUR_TRAINING_PIPELINE_ID";
        getTrainingPipeline(project, trainingPipelineId);
      }
    
      static void getTrainingPipeline(String project, String trainingPipelineId) throws IOException {
        [PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html) pipelineServiceSettings =
            [PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html) pipelineServiceClient =
            [PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.html).create(pipelineServiceSettings)) {
          String location = "us-central1";
          [TrainingPipelineName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipelineName.html) trainingPipelineName =
              [TrainingPipelineName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipelineName.html).of(project, location, trainingPipelineId);
    
          [TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html) trainingPipelineResponse =
              pipelineServiceClient.getTrainingPipeline(trainingPipelineName);
    
          System.out.println("Get Training Pipeline Response");
          System.out.format("\tName: %s\n", trainingPipelineResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getName__)());
          System.out.format("\tDisplay Name: %s\n", trainingPipelineResponse.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getDisplayName__)());
          System.out.format(
              "\tTraining Task Definition: %s\n", trainingPipelineResponse.[getTrainingTaskDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskDefinition__)());
          System.out.format(
              "\tTraining Task Inputs: %s\n", trainingPipelineResponse.[getTrainingTaskInputs](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskInputs__)());
          System.out.format(
              "\tTraining Task Metadata: %s\n", trainingPipelineResponse.[getTrainingTaskMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getTrainingTaskMetadata__)());
          System.out.format("\tState: %s\n", trainingPipelineResponse.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getState__)());
          System.out.format("\tCreate Time: %s\n", trainingPipelineResponse.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getCreateTime__)());
          System.out.format("\tStart Time: %s\n", trainingPipelineResponse.[getStartTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getStartTime__)());
          System.out.format("\tEnd Time: %s\n", trainingPipelineResponse.[getEndTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getEndTime__)());
          System.out.format("\tUpdate Time: %s\n", trainingPipelineResponse.[getUpdateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getUpdateTime__)());
          System.out.format("\tLabels: %s\n", trainingPipelineResponse.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getLabelsMap__)());
          [InputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html) inputDataConfig = trainingPipelineResponse.[getInputDataConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getInputDataConfig__)();
    
          System.out.println("\tInput Data Config");
          System.out.format("\t\tDataset Id: %s\n", inputDataConfig.[getDatasetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getDatasetId__)());
          System.out.format("\t\tAnnotations Filter: %s\n", inputDataConfig.[getAnnotationsFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getAnnotationsFilter__)());
          [FractionSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html) fractionSplit = inputDataConfig.[getFractionSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getFractionSplit__)();
    
          System.out.println("\t\tFraction Split");
          System.out.format("\t\t\tTraining Fraction: %s\n", fractionSplit.[getTrainingFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getTrainingFraction__)());
          System.out.format("\t\t\tValidation Fraction: %s\n", fractionSplit.[getValidationFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getValidationFraction__)());
          System.out.format("\t\t\tTest Fraction: %s\n", fractionSplit.[getTestFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FractionSplit.html#com_google_cloud_aiplatform_v1_FractionSplit_getTestFraction__)());
          [FilterSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html) filterSplit = inputDataConfig.[getFilterSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getFilterSplit__)();
    
          System.out.println("\t\tFilter Split");
          System.out.format("\t\t\tTraining Filter: %s\n", filterSplit.[getTrainingFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getTrainingFilter__)());
          System.out.format("\t\t\tValidation Filter: %s\n", filterSplit.[getValidationFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getValidationFilter__)());
          System.out.format("\t\t\tTest Filter: %s\n", filterSplit.[getTestFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.FilterSplit.html#com_google_cloud_aiplatform_v1_FilterSplit_getTestFilter__)());
          [PredefinedSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html) predefinedSplit = inputDataConfig.[getPredefinedSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getPredefinedSplit__)();
    
          System.out.println("\t\tPredefined Split");
          System.out.format("\t\t\tKey: %s\n", predefinedSplit.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredefinedSplit.html#com_google_cloud_aiplatform_v1_PredefinedSplit_getKey__)());
          [TimestampSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html) timestampSplit = inputDataConfig.[getTimestampSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.InputDataConfig.html#com_google_cloud_aiplatform_v1_InputDataConfig_getTimestampSplit__)();
    
          System.out.println("\t\tTimestamp Split");
          System.out.format("\t\t\tTraining Fraction: %s\n", timestampSplit.[getTrainingFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getTrainingFraction__)());
          System.out.format("\t\t\tTest Fraction: %s\n", timestampSplit.[getTestFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getTestFraction__)());
          System.out.format("\t\t\tValidation Fraction: %s\n", timestampSplit.[getValidationFraction](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getValidationFraction__)());
          System.out.format("\t\t\tKey: %s\n", timestampSplit.[getKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TimestampSplit.html#com_google_cloud_aiplatform_v1_TimestampSplit_getKey__)());
          [Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html) modelResponse = trainingPipelineResponse.[getModelToUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getModelToUpload__)();
    
          System.out.println("\t\tModel to upload");
          System.out.format("\t\tName: %s\n", modelResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getName__)());
          System.out.format("\t\tDisplay Name: %s\n", modelResponse.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDisplayName__)());
          System.out.format("\t\tDescription: %s\n", modelResponse.[getDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDescription__)());
          System.out.format("\t\tMetadata Schema Uri: %s\n", modelResponse.[getMetadataSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getMetadataSchemaUri__)());
          System.out.format("\t\tMeta Data: %s\n", modelResponse.[getMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getMetadata__)());
          System.out.format("\t\tTraining Pipeline: %s\n", modelResponse.[getTrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getTrainingPipeline__)());
          System.out.format("\t\tArtifact Uri: %s\n", modelResponse.[getArtifactUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getArtifactUri__)());
          System.out.format(
              "\t\tSupported Deployment Resources Types: %s\n",
              modelResponse.[getSupportedDeploymentResourcesTypesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedDeploymentResourcesTypesList__)().toString());
          System.out.format(
              "\t\tSupported Input Storage Formats: %s\n",
              modelResponse.[getSupportedInputStorageFormatsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedInputStorageFormatsList__)().toString());
          System.out.format(
              "\t\tSupported Output Storage Formats: %s\n",
              modelResponse.[getSupportedOutputStorageFormatsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedOutputStorageFormatsList__)().toString());
          System.out.format("\t\tCreate Time: %s\n", modelResponse.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getCreateTime__)());
          System.out.format("\t\tUpdate Time: %s\n", modelResponse.[getUpdateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getUpdateTime__)());
          System.out.format("\t\tLabels: %s\n", modelResponse.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getLabelsMap__)());
          [PredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html) predictSchemata = modelResponse.[getPredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getPredictSchemata__)();
    
          System.out.println("\tPredict Schemata");
          System.out.format("\t\tInstance Schema Uri: %s\n", predictSchemata.[getInstanceSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getInstanceSchemaUri__)());
          System.out.format(
              "\t\tParameters Schema Uri: %s\n", predictSchemata.[getParametersSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getParametersSchemaUri__)());
          System.out.format(
              "\t\tPrediction Schema Uri: %s\n", predictSchemata.[getPredictionSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getPredictionSchemaUri__)());
    
          for ([Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html).[ExportFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.ExportFormat.html) supportedExportFormat :
              modelResponse.[getSupportedExportFormatsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedExportFormatsList__)()) {
            System.out.println("\tSupported Export Format");
            System.out.format("\t\tId: %s\n", supportedExportFormat.getId());
          }
          [ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html) containerSpec = modelResponse.[getContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getContainerSpec__)();
    
          System.out.println("\tContainer Spec");
          System.out.format("\t\tImage Uri: %s\n", containerSpec.[getImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getImageUri__)());
          System.out.format("\t\tCommand: %s\n", containerSpec.[getCommandList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getCommandList__)());
          System.out.format("\t\tArgs: %s\n", containerSpec.[getArgsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getArgsList__)());
          System.out.format("\t\tPredict Route: %s\n", containerSpec.[getPredictRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getPredictRoute__)());
          System.out.format("\t\tHealth Route: %s\n", containerSpec.[getHealthRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getHealthRoute__)());
    
          for ([EnvVar](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EnvVar.html) envVar : containerSpec.[getEnvList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getEnvList__)()) {
            System.out.println("\t\tEnv");
            System.out.format("\t\t\tName: %s\n", envVar.getName());
            System.out.format("\t\t\tValue: %s\n", envVar.getValue());
          }
    
          for ([Port](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Port.html) port : containerSpec.[getPortsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getPortsList__)()) {
            System.out.println("\t\tPort");
            System.out.format("\t\t\tContainer Port: %s\n", port.getContainerPort());
          }
    
          for ([DeployedModelRef](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelRef.html) deployedModelRef : modelResponse.[getDeployedModelsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDeployedModelsList__)()) {
            System.out.println("\tDeployed Model");
            System.out.format("\t\tEndpoint: %s\n", deployedModelRef.getEndpoint());
            System.out.format("\t\tDeployed Model Id: %s\n", deployedModelRef.getDeployedModelId());
          }
    
          [Status](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html) status = trainingPipelineResponse.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline.html#com_google_cloud_aiplatform_v1_TrainingPipeline_getError__)();
          System.out.println("\tError");
          System.out.format("\t\tCode: %s\n", status.[getCode](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getCode__)());
          System.out.format("\t\tMessage: %s\n", status.[getMessage](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.rpc.Status.html#com_google_rpc_Status_getMessage__)());
        }
      }
    }

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    from google.cloud import aiplatform
    
    
    def get_training_pipeline_sample(
        project: str,
        training_pipeline_id: str,
        location: str = "us-central1",
        api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    ):
        # The AI Platform services require regional API endpoints.
        client_options = {"api_endpoint": api_endpoint}
        # Initialize client that will be used to create and send requests.
        # This client only needs to be created once, and can be reused for multiple requests.
        client = aiplatform.gapic.PipelineServiceClient(client_options=client_options)
        name = client.training_pipeline_path(
            project=project, location=location, training_pipeline=training_pipeline_id
        )
        response = client.get_training_pipeline(name=name)
        print("response:", response)
    
    

## Get model information

After the `trainingPipeline` creation completes you can use the model's display name to get more detailed model information.

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: Region where Model is located. For example, `us-central1`
  * PROJECT: .
  * MODEL_DISPLAYNAME: The display name of your model that you specified when creating a trainingPipeline job.
  * PROJECT_NUMBER: Your project's automatically generated [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers)



HTTP method and URL: 
    
    
    GET https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/models?filter=display_name=MODEL_DISPLAYNAME

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/models?filter=display_name=MODEL_DISPLAYNAME"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT/locations/LOCATION/models?filter=display_name=MODEL_DISPLAYNAME" | Select-Object -Expand Content

You should see output similar to the following for a trained AutoML Edge model. The following sample output is for an image AutoML Edge model: 

#### Response
    
    
    {
      "models": [
        {
          "name": "projects/PROJECT/locations/LOCATION/models/MODEL_ID",
          "displayName": "MODEL_DISPLAYNAME",
          "predictSchemata": {
            "instanceSchemaUri": "https://storage.googleapis.com/google-cloud-aiplatform/schema/predict/instance/image_classification_1.0.0.yaml",
            "parametersSchemaUri": "https://storage.googleapis.com/google-cloud-aiplatform/schema/predict/params/image_classification_1.0.0.yaml",
            "predictionSchemaUri": "https://storage.googleapis.com/google-cloud-aiplatform/schema/predict/prediction/classification_1.0.0.yaml"
          },
          "metadataSchemaUri": "https://storage.googleapis.com/google-cloud-aiplatform/schema/model/metadata/automl_image_classification_1.0.0.yaml",
          "metadata": {
            "modelType": "MOBILE_TF_VERSATILE_1",
            "trainingDataItemsCount": "2174",
            "validationDataItemsCount": "467",
            "trainingAnnotationsCount": "2174",
            "validationAnnotationsCount": "467",
            "eligibleAsBaseModel": true
          },
          "trainingPipeline": "projects/PROJECT_NUMBER/locations/LOCATION/trainingPipelines/TRAININGPIPELINE_ID",
          "supportedDeploymentResourcesTypes": [
            "AUTOMATIC_RESOURCES"
          ],
          "supportedInputStorageFormats": [
            "jsonl"
          ],
          "supportedOutputStorageFormats": [
            "jsonl"
          ],
          "createTime": "2020-07-14T17:16:55.098953Z",
          "updateTime": "2020-07-14T18:46:08.169225Z",
          "etag": "AMEw9yNjhttIyiGUgec8vGNeidfX8mGcFT1owDOq1iDT6mmQ7HLHwoomie30pLCTtJ4=",
          "labels": {
            "env": "prod",
            "tier": "backend"
          },
          "supportedExportFormats": [
            {
              "id": "tflite"
            },
            {
              "id": "edgetpu-tflite"
            },
            {
              "id": "tf-saved-model"
            },
            {
              "id": "core-ml"
            },
            {
              "id": "tf-js"
            }
          ]
        }
      ]
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). For more information, see the [Agent Platform Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.aiplatform.v1.[DeployedModelRef](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelRef.html);
    import com.google.cloud.aiplatform.v1.[EnvVar](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EnvVar.html);
    import com.google.cloud.aiplatform.v1.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html);
    import com.google.cloud.aiplatform.v1.[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html).[ExportFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.ExportFormat.html);
    import com.google.cloud.aiplatform.v1.[ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html);
    import com.google.cloud.aiplatform.v1.[ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html);
    import com.google.cloud.aiplatform.v1.[ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.html);
    import com.google.cloud.aiplatform.v1.[ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings.html);
    import com.google.cloud.aiplatform.v1.[Port](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Port.html);
    import com.google.cloud.aiplatform.v1.[PredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html);
    import java.io.IOException;
    
    public class GetModelSample {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "YOUR_PROJECT_ID";
        String modelId = "YOUR_MODEL_ID";
        getModelSample(project, modelId);
      }
    
      static void getModelSample(String project, String modelId) throws IOException {
        [ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings.html) modelServiceSettings =
            [ModelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceSettings.html).newBuilder()
                .setEndpoint("us-central1-aiplatform.googleapis.com:443")
                .build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.html) modelServiceClient = [ModelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceClient.html).create(modelServiceSettings)) {
          String location = "us-central1";
          [ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html) modelName = [ModelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelName.html).of(project, location, modelId);
    
          [Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html) modelResponse = modelServiceClient.getModel(modelName);
          System.out.println("Get Model response");
          System.out.format("\tName: %s\n", modelResponse.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getName__)());
          System.out.format("\tDisplay Name: %s\n", modelResponse.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDisplayName__)());
          System.out.format("\tDescription: %s\n", modelResponse.[getDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDescription__)());
    
          System.out.format("\tMetadata Schema Uri: %s\n", modelResponse.[getMetadataSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getMetadataSchemaUri__)());
          System.out.format("\tMetadata: %s\n", modelResponse.[getMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getMetadata__)());
          System.out.format("\tTraining Pipeline: %s\n", modelResponse.[getTrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getTrainingPipeline__)());
          System.out.format("\tArtifact Uri: %s\n", modelResponse.[getArtifactUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getArtifactUri__)());
    
          System.out.format(
              "\tSupported Deployment Resources Types: %s\n",
              modelResponse.[getSupportedDeploymentResourcesTypesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedDeploymentResourcesTypesList__)());
          System.out.format(
              "\tSupported Input Storage Formats: %s\n",
              modelResponse.[getSupportedInputStorageFormatsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedInputStorageFormatsList__)());
          System.out.format(
              "\tSupported Output Storage Formats: %s\n",
              modelResponse.[getSupportedOutputStorageFormatsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedOutputStorageFormatsList__)());
    
          System.out.format("\tCreate Time: %s\n", modelResponse.[getCreateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getCreateTime__)());
          System.out.format("\tUpdate Time: %s\n", modelResponse.[getUpdateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getUpdateTime__)());
          System.out.format("\tLabels: %s\n", modelResponse.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getLabelsMap__)());
    
          [PredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html) predictSchemata = modelResponse.[getPredictSchemata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getPredictSchemata__)();
          System.out.println("\tPredict Schemata");
          System.out.format("\t\tInstance Schema Uri: %s\n", predictSchemata.[getInstanceSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getInstanceSchemaUri__)());
          System.out.format(
              "\t\tParameters Schema Uri: %s\n", predictSchemata.[getParametersSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getParametersSchemaUri__)());
          System.out.format(
              "\t\tPrediction Schema Uri: %s\n", predictSchemata.[getPredictionSchemaUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PredictSchemata.html#com_google_cloud_aiplatform_v1_PredictSchemata_getPredictionSchemaUri__)());
    
          for ([ExportFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.ExportFormat.html) exportFormat : modelResponse.[getSupportedExportFormatsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getSupportedExportFormatsList__)()) {
            System.out.println("\tSupported Export Format");
            System.out.format("\t\tId: %s\n", exportFormat.getId());
          }
    
          [ModelContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html) containerSpec = modelResponse.[getContainerSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getContainerSpec__)();
          System.out.println("\tContainer Spec");
          System.out.format("\t\tImage Uri: %s\n", containerSpec.[getImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getImageUri__)());
          System.out.format("\t\tCommand: %s\n", containerSpec.[getCommandList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getCommandList__)());
          System.out.format("\t\tArgs: %s\n", containerSpec.[getArgsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getArgsList__)());
          System.out.format("\t\tPredict Route: %s\n", containerSpec.[getPredictRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getPredictRoute__)());
          System.out.format("\t\tHealth Route: %s\n", containerSpec.[getHealthRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getHealthRoute__)());
    
          for ([EnvVar](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EnvVar.html) envVar : containerSpec.[getEnvList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getEnvList__)()) {
            System.out.println("\t\tEnv");
            System.out.format("\t\t\tName: %s\n", envVar.getName());
            System.out.format("\t\t\tValue: %s\n", envVar.getValue());
          }
    
          for ([Port](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Port.html) port : containerSpec.[getPortsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelContainerSpec.html#com_google_cloud_aiplatform_v1_ModelContainerSpec_getPortsList__)()) {
            System.out.println("\t\tPort");
            System.out.format("\t\t\tContainer Port: %s\n", port.getContainerPort());
          }
    
          for ([DeployedModelRef](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModelRef.html) deployedModelRef : modelResponse.[getDeployedModelsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model.html#com_google_cloud_aiplatform_v1_Model_getDeployedModelsList__)()) {
            System.out.println("\tDeployed Model");
            System.out.format("\t\tEndpoint: %s\n", deployedModelRef.getEndpoint());
            System.out.format("\t\tDeployed Model Id: %s\n", deployedModelRef.getDeployedModelId());
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). For more information, see the [Agent Platform Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.\
     * (Not necessary if passing values as arguments)
     */
    
    // const modelId = 'YOUR_MODEL_ID';
    // const project = 'YOUR_PROJECT_ID';
    // const location = 'YOUR_PROJECT_LOCATION';
    
    // Imports the Google Cloud Model Service Client library
    const {ModelServiceClient} = require('[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)');
    
    // Specifies the location of the api endpoint
    const clientOptions = {
      apiEndpoint: 'us-central1-aiplatform.googleapis.com',
    };
    
    // Instantiates a client
    const modelServiceClient = new [ModelServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)(clientOptions);
    
    async function getModel() {
      // Configure the parent resource
      const name = `projects/${project}/locations/${location}/models/${modelId}`;
      const request = {
        name,
      };
      // Get and print out a list of all the endpoints for this resource
      const [response] = await modelServiceClient.getModel(request);
    
      console.log('Get model response');
      console.log(`\tName : ${response.name}`);
      console.log(`\tDisplayName : ${response.displayName}`);
      console.log(`\tDescription : ${response.description}`);
      console.log(`\tMetadata schema uri : ${response.metadataSchemaUri}`);
      console.log(`\tMetadata : ${JSON.stringify(response.metadata)}`);
      console.log(`\tTraining pipeline : ${response.trainingPipeline}`);
      console.log(`\tArtifact uri : ${response.artifactUri}`);
      console.log(
        `\tSupported deployment resource types : \
          ${response.supportedDeploymentResourceTypes}`
      );
      console.log(
        `\tSupported input storage formats : \
          ${response.supportedInputStorageFormats}`
      );
      console.log(
        `\tSupported output storage formats : \
          ${response.supportedOutputStoragFormats}`
      );
      console.log(`\tCreate time : ${JSON.stringify(response.createTime)}`);
      console.log(`\tUpdate time : ${JSON.stringify(response.updateTime)}`);
      console.log(`\tLabels : ${JSON.stringify(response.labels)}`);
    
      const predictSchemata = response.predictSchemata;
      console.log('\tPredict schemata');
      console.log(`\tInstance schema uri : ${predictSchemata.instanceSchemaUri}`);
      console.log(
        `\tParameters schema uri : ${predictSchemata.prametersSchemaUri}`
      );
      console.log(
        `\tPrediction schema uri : ${predictSchemata.predictionSchemaUri}`
      );
    
      const [supportedExportFormats] = response.supportedExportFormats;
      console.log('\tSupported export formats');
      console.log(`\t${supportedExportFormats}`);
    
      const containerSpec = response.containerSpec;
      console.log('\tContainer Spec');
      if (!containerSpec) {
        console.log(`\t\t${JSON.stringify(containerSpec)}`);
        console.log('\t\tImage uri : {}');
        console.log('\t\tCommand : {}');
        console.log('\t\tArgs : {}');
        console.log('\t\tPredict route : {}');
        console.log('\t\tHealth route : {}');
        console.log('\t\tEnv');
        console.log('\t\t\t{}');
        console.log('\t\tPort');
        console.log('\t\t{}');
      } else {
        console.log(`\t\t${JSON.stringify(containerSpec)}`);
        console.log(`\t\tImage uri : ${containerSpec.imageUri}`);
        console.log(`\t\tCommand : ${containerSpec.command}`);
        console.log(`\t\tArgs : ${containerSpec.args}`);
        console.log(`\t\tPredict route : ${containerSpec.predictRoute}`);
        console.log(`\t\tHealth route : ${containerSpec.healthRoute}`);
        const env = containerSpec.env;
        console.log('\t\tEnv');
        console.log(`\t\t\t${JSON.stringify(env)}`);
        const ports = containerSpec.ports;
        console.log('\t\tPort');
        console.log(`\t\t\t${JSON.stringify(ports)}`);
      }
    
      const [deployedModels] = response.deployedModels;
      console.log('\tDeployed models');
      console.log('\t\t', deployedModels);
    }
    getModel();

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    def get_model_sample(project: str, location: str, model_name: str):
    
        aiplatform.init(project=project, location=location)
    
        model = aiplatform.Model(model_name=model_name)
    
        print(model.display_name)
        print(model.resource_name)
        return model
    
    

## What's next

  * [Evaluate AutoML models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training-overview#automl).
  * [Export AutoML Edge models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/export/export-edge-model). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
