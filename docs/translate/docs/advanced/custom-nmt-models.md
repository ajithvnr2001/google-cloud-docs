---
url: https://docs.cloud.google.com/translate/docs/advanced/custom-nmt-models/
title: Create and manage models \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:28.120588+00:00
---

# Create and manage models  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/custom-nmt-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage models

**Note** : You can customize the Google Neural Machine Translation (NMT) model using the Cloud Translation - Advanced API. We recommend that you use the Cloud Translation API to create datasets and models because any future enhancements will apply only to the Cloud Translation API. If you have existing AutoML resources, you can upgrade them to work with the Cloud Translation API. For more information, see [Upgrade AutoML resources](https://docs.cloud.google.com/translate/docs/advanced/automl-upgrade). 

Create a custom model by using a prepared dataset. Cloud Translation uses the segment pairs from the dataset to train, test, and evaluate a new model.

**Caution:** Custom models run on a managed platform that is regularly upgraded. Custom models must be re-trained at least every **18 months** to ensure consistent performance and stability in translations over time and to get any benefits of the upgrades since original training.

## Train models

After you have a dataset with enough segment pairs, you can create a custom model from that dataset.

### Web UI

  1. Go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation pane, click **Datasets** to view a list of your datasets.

  3. Click the dataset to use to train a custom model.

The console shows the segment pairs in the dataset along with their respective labels: `Training`, `Validation`, or `Testing`.

  4. When you are done reviewing the dataset, click the **Train** tab.

  5. Click **Start Training** to open the **Train new model** dialog.

  6. Specify a name for the model.

  7. Click **Start Training** to begin training your custom model.

Training a model can take several hours to complete. You can check the training status by viewing recent activity.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The region where the model will be located, such as `us-central1`. The source dataset must also be in the same location.
  * MODEL_NAME: A name for the model.
  * DATASET_ID: The ID of the source dataset that Cloud Translation uses to create the model.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models

Request JSON body: 
    
    
    {
      "display_name": "MODEL_NAME",
      "dataset": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID",
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID"
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Get the status of a training job

You can check the status of a long-running task, like training a model, by using the Google Cloud console or Cloud Translation API.

### Web UI

You can monitor the training job status in the **Recent activities** pane. 

  1. Go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation pane, click **Datasets**.

  3. From the action bar, click **View recent activities**.

Find the related **CreateModel** operation. The icon next to operation ID indicates the current status of the operations.




### REST

To get the status of your training operation, send a `GET` request to the [`operations`](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.operations/get) resource along with the operation ID that was included in the response after you submitted the training request. 

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * location-id: the location you chose for your Cloud Storage bucket
  * operation-id: operation ID you received above



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/location-id/operations/operation-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/location-id/operations/operation-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID/locations/location-id/operations/operation-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/project-number/locations/location-id/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.SomeOperationMetadata",
        "state": "SUCCEEDED",
        "submitTime": "2019-11-27T22:59:40Z"
      }
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Getting information about a model

After training is complete, you can get information about the model such as the model ID. To get details about a model's accuracy and readiness, see [Evaluate models](https://docs.cloud.google.com/translate/docs/advanced/translation-model-evaluation).

### Web UI

You can monitor the training job status in the **Recent activities** pane. 

  1. To see a list of the available models, go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation pane, click **Models** to view a table that lists of your models.

The table includes information like the source and target language, BLEU score, and total segment pairs.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The region where the model to describe is located, such as `us-central1`.
  * MODEL_ID: The ID of the model to describe.



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models/MODEL_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models/MODEL_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models/MODEL_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/us-central1/models/MODEL_ID",
      "displayName": "MODEL_DISPLAY_NAME",
      "dataset": "projects/PROJECT_NUMBER/locations/us-central1/datasets/DATASET_ID"
      "sourceLanguageCode": "SOURCE_LANG_CODE",
      "targetLanguageCode": "TARGET_LANG_CODE",
      "trainExampleCount": NUM_TRAINING_SEGMENTS,
      "validateExampleCount": NUM_VALIDATION_SEGMENTS,
      "createTime": "2022-12-02T21:53:26.788521838Z",
      "updateTime": "2022-12-03T00:42:27.946594016Z"
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Listing models

List the available models in your project.

### Web UI

  1. To see a list of the available models, go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation pane, click **Models** to view a list of your models.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The region where the models to list are located, such as `us-central1`.



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "models": [
        {
          "name": "projects/PROJECT_NUMBER/locations/us-central1/models/MODEL_ID",
          "displayName": "MODEL_DISPLAY_NAME",
          "dataset": "projects/PROJECT_NUMBER/locations/us-central1/datasets/DATASET_ID"
          "sourceLanguageCode": "SOURCE_LANG_CODE",
          "targetLanguageCode": "TARGET_LANG_CODE",
          "trainExampleCount": NUM_TRAINING_SEGMENTS,
          "validateExampleCount": NUM_VALIDATION_SEGMENTS,
          "createTime": "2022-12-02T21:53:26.788521838Z",
          "updateTime": "2022-12-03T00:42:27.946594016Z"
        },
        ...
      ]
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Delete a model

Delete a model to remove it from your project.

### Web UI

  1. To see a list of the available models, go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. From the navigation pane, click **Models** to view a list of your models.

  3. For the model to delete, select more_vert **More > Delete**.

  4. Click **Confirm** to start the deletion.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The region where the model to delete is located, such as `us-central1`.
  * MODEL_ID: The ID of the model to delete.



HTTP method and URL: 
    
    
    DELETE https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models/MODEL_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models/MODEL_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/models/MODEL_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.DeleteModelMetadata"
      },
      "done": true
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
