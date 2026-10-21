---
url: https://docs.cloud.google.com/translate/docs/advanced/custom-nmt-datasets/
title: Create and manage datasets \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:12.085179+00:00
---

# Create and manage datasets  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/custom-nmt-datasets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage datasets

**Note** : You can customize the Google Neural Machine Translation (NMT) model using the Cloud Translation - Advanced API. We recommend that you use the Cloud Translation API to create datasets and models because any future enhancements will apply only to the Cloud Translation API. If you have existing AutoML resources, you can upgrade them to work with the Cloud Translation API. For more information, see [Upgrade AutoML resources](https://docs.cloud.google.com/translate/docs/advanced/automl-upgrade). 

A dataset contains representative samples of the type of content that you want to translate, as matching segment pairs in the source and target languages. The dataset serves as the input for training a model.

A project can have multiple datasets; each one can be used to train a separate model.

## Create a dataset

Create a dataset to contain the training data for your model. When you create a dataset, you specify the source and target languages of your training data. For more information about the supported languages and variants, see [Language support for custom models](https://docs.cloud.google.com/translate/docs/languages).

### Web UI

The Cloud Translation console lets you create a new dataset and import items into it. 

  1. Go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. In the navigation pane, click **Datasets**.

  3. On the **Datasets** page, click **Create dataset**.

  4. In the **Create dataset** dialog, specify details about the dataset:

     * Enter a name for the dataset.
     * Select the source and target languages from the drop-down lists.
     * Click **Create**. 



### REST

The following example shows how to send a `POST` request to the [`project.locations.datasets/create`](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.datasets/create) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The region where the dataset will be located, such as `us-central1`.
  * DATASET_NAME: A name for the dataset.
  * SOURCE_LANG_CODE: The [language code](https://docs.cloud.google.com/translate/docs/languages#automl) that specifies the dataset's source language.
  * TARGET_LANG_CODE: The [language code](https://docs.cloud.google.com/translate/docs/languages#automl) that specifies the dataset's target language.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets

Request JSON body: 
    
    
    {
      "display_name": "DATASET_NAME",
      "source_language_code": "SOURCE_LANG_CODE",
      "target_language_code": "TARGET_LANG_CODE"
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
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets"

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
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NAME/locations/LOCATION/operations/OPERATION_ID"
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Import segments into a dataset

After you have created a dataset, you can import segment pairs into the dataset. For details on preparing your source data, see [Preparing training data](https://docs.cloud.google.com/translate/docs/advanced/custom-nmt-prepare).

For each file, the Google Cloud console lets you tag imported segment pairs with one or more key-value pairs. Tagging makes it easier to find and filter segments by source. For example, a key-value pair could be `Domain:costmetics` or `Year:2020`.

You can add tags when you import segments through the Google Cloud console; tagging isn't supported by the API. Also, you can't modify tags or add tags to segments that have already been imported.

### Web UI

The following steps import items into an existing dataset.

  1. Go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. In the navigation pane, click **Datasets**.

  3. From the dataset list, click the name of the dataset that want to add training data to.

  4. Go to the **Import** tab.

  5. Add files to import segment pairs for model training.

Upload files from your local computer to a Cloud Storage bucket or select existing files from Cloud Storage.

By default, Cloud Translation automatically splits your data into training, validation, and test sets. If you want to upload separate files for each split, select **Use separate files for training, validation, and testing (advanced)**. Use this option if your dataset has more than 100,000 segment pairs to avoid exceeding the maximum 10,000 segment pair limit for the validation and test sets.

  6. To add tags to segment pairs, expand **Tags (optional)**.

     1. From the list of files, click edit **Edit** to add one or more tags to all segment pairs for a given file.

     2. In the **Tags** pane, click **Add tag**.

     3. Enter a key and value. You'll be able to filter segments by this key-value pair.

     4. To add more tags, click **Add tag**.

     5. Click **Continue** when you're done adding tags.

  7. Click **Continue** to import segment pairs.

After the import is complete, you can view the imported sentence pairs in the **Sentences** tab of your dataset. You filter segments by split (training, validation, or testing) and by one or more tags.




### REST

Use the [`projects.locations.datasets.importData`](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.datasets/importData) method to import items into a dataset. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The region where the dataset will be located, such as `us-central1`.
  * DATASET_ID: The ID of the dataset to add data to.
  * FILE_DISPLAY_NAME: The name of the file that contains data to import.
  * USAGE: Specifies the data split for these segment pairs (`TRAIN`, `VALIDATION`, or `TEST`).
  * FILE_PATH: The path to the source data file in Cloud Storage.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID:importData

Request JSON body: 
    
    
    {
      "input_config": {
        "input_files": [
          {
            "display_name": "FILE_DISPLAY_NAME",
            "usage": "USAGE",
            "gcs_source": {
              "input_uris": "gs://FILE_PATH"
            }
          },
          ...
        ]
      }
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
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID:importData"

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
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID:importData" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID"
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

After you have created and populated the dataset, you can train a model. For more information, see [Creating and managing models](https://docs.cloud.google.com/translate/docs/advanced/automl-models)).

### Import issues

When you create a dataset, Cloud Translation might drop segment pairs if they are too long, if segments in the source and target languages are identical (untranslated), or if there are duplicates (multiple segments with the same source language text).

For segment pairs that are too long, we recommend that you break up segments to roughly 200 words or less, and then recreate the dataset. The 200 word limit is an estimate for the maximum length. While processing your data, Cloud Translation uses an internal process to tokenize your input data, which can increase the size of your segments. This tokenized data is what Cloud Translation uses to measure data size.

For segment pairs that are identical, remove them from your dataset. If you want to prevent some segments from being translated, use a [glossary resource](https://docs.cloud.google.com/translate/docs/advanced/glossary) to build a custom dictionary instead.

## Export data

You can export segment pairs from existing datasets to a Cloud Storage bucket.

### Web UI

  1. Go to the Cloud Translation console.

[Go to the Translation page](https://console.cloud.google.com/translation)

  2. In the navigation pane, click **Datasets** to view a list of your datasets.

  3. Click the name of the dataset for which you want to export data.

  4. On the dataset details page, click **Export data**.

  5. Select a Cloud Storage destination where the exported TSV files are saved.

  6. Click **Export**.

Cloud Translation outputs TSV files that are named according to their dataset set (train, validation, and test).




### REST

Use the [`projects.locations.datasets.exportData`](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.datasets/exportData) method to export data to Cloud Storage as TSV files. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The region where the dataset to export is located, such as `us-central1`.
  * DATASET_ID: The ID of the dataset to export.
  * DESTINATION_DIRECTORY: The Cloud Storage path where the output is sent.



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID:exportData

Request JSON body: 
    
    
    {
      "output_config": {
        "gcs_destination": {
          "output_uri_prefix": "gs://DESTINATION_DIRECTORY"
        }
      }
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
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID:exportData"

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
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID:exportData" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID"
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## List datasets

List the available datasets in your project.

### Web UI

To see a list of the available datasets by using the [Cloud Translation console](https://console.cloud.google.com/), click **Datasets** from the navigation pane.

To see the datasets for a different project, select the project from the drop-down list in the upper right of the title bar.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The region where the datasets to list are located, such as `us-central1`.



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "datasets": [
        {
          "name": "projects/PROJECT_NUMBER/locations/us-central1/datasets/DATASET_ID",
          "displayName": "DATASET_NAME",
          "sourceLanguageCode": "SOURCE_LANG_CODE",
          "targetLanguageCode": "TARGET_LANG_CODE",
          "exampleCount": 8720,
          "createTime": "2022-10-19T23:24:34.734549Z",
          "updateTime": "2022-10-19T23:24:35.357525Z"
        },
        ...
      ]
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

## Deleting a dataset

### Web UI

  1. In the [Cloud Translation console](https://console.cloud.google.com/), click **Datasets** from the navigation pane to display the list of available datasets.

  2. For the dataset to delete, select more_vert **More > Delete**.

  3. Click **Confirm** in the confirmation dialog box.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The region where the datasets to list are located, such as `us-central1`.
  * DATASET_ID: The ID of the dataset to delete.



HTTP method and URL: 
    
    
    DELETE https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.translation.v3.DeleteDatasetMetadata"
      },
      "done": true
    }
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Translate.V3/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-translate/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/translate/docs/reference/api-overview#client_libraries) on the client libraries page and then visit the [Cloud Translation reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-translate/latest/Google/Cloud/Translate.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
