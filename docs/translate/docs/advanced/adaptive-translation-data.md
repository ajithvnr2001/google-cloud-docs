---
url: https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation-data/
title: Manage datasets \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:43.212167+00:00
---

# Manage datasets  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/adaptive-translation-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage datasets

Manage existing adaptive translation datasets by using the Cloud Translation API. You can list datasets, list files that are used by a dataset, delete all entries from a given file, or delete datasets.

## List datasets

View a list of all existing adaptive translation datasets in your project.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * LOCATION: The region where your source dataset is located, such as `us-central1`.



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "adaptiveMtDatasets": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID",
          "displayName": "DISPLAY_NAME",
          "sourceLanguageCode": "SOURCE_LANGUAGE",
          "targetLanguageCode": "TARGET_LANGUAGE"
        }
      ]
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /** Lists all AdaptiveMtDatasets in a project. */
    private static void listAdaptiveMtDatasets(
        TranslationServiceClient translationServiceClient, String projectId) {
      ListAdaptiveMtDatasetsRequest listAdaptiveMtDatasetsRequest =
          ListAdaptiveMtDatasetsRequest.newBuilder()
              .setParent(LocationName.of(projectId, "LOCATION").toString())
              .build();
      ListAdaptiveMtDatasetsPagedResponse response =
          translationServiceClient.listAdaptiveMtDatasets(listAdaptiveMtDatasetsRequest);
    
      System.out.println("Listing datasets:");
      for (AdaptiveMtDataset dataset : response.iterateAll()) {
        System.out.println(dataset);
      }
    }
      

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function listAdaptiveMtDatasets() {
      const request = {
        parent: `projects/${projectId}/locations/${location}`
      } const [response] = await translationClient.listAdaptiveMtDatasets(request)
      console.log('Listing datasets')
      console.log(response)
    }
      

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_adaptive_mt_datasets():
      # Create a client
      client = translate.TranslationServiceClient()
      # Initialize the request
      request = translate.ListAdaptiveMtDatasetsRequest(
          parent="projects/PROJECT_ID/locations/LOCATION",
      )
      # Make the request
      response = client.list_adaptive_mt_datasets(request)
      # Handle the response
      print(response)
      

## List files in dataset

List files in your dataset to view which files were used to populate the dataset. Cloud Translation outputs the file names and the number of sentence pairs (entries) imported from each file.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * LOCATION: The region where your dataset is located, such as `us-central1`.
  * DATASET_ID: The unique identifier of your dataset that contains files to list. 



HTTP method and URL: 
    
    
    GET https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID/adaptiveMtFiles

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID/adaptiveMtFiles"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID/adaptiveMtFiles" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "adaptiveMtFile": [
        {
          "name": "FILE_NAME",
          "displayName": "DESCRIPTIVE_NAME",
          "entryCount": TOTAL_ENTRIES
        }
      ]
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /** Lists all AdaptiveMtFiles in a dataset. */
    private static void listAdaptiveMtFiles(
        TranslationServiceClient translationServiceClient, String projectId, String datasetId) {
      String adaptiveMtDatasetName =
          String.format(
              "projects/%s/locations/LOCATION/adaptiveMtDatasets/%s", projectId, datasetId);
      TranslationServiceClient.ListAdaptiveMtFilesPagedResponse response =
          translationServiceClient.listAdaptiveMtFiles(adaptiveMtDatasetName);
    
      System.out.println("Listing dataset files:");
      for (AdaptiveMtFile file : response.iterateAll()) {
        System.out.println(file.toString());
      }
    }
      

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function listAdaptiveMtFiles() {
      const request = {
        parent: `projects/${projectId}/locations/${location}/adaptiveMtDatasets/${
            adaptiveMtDatasetName}`,
      } const [response] = await translationClient.listAdaptiveMtFiles(request)
      console.log('Listing files')
      console.log(response)
    }
      

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_adaptive_mt_files():
      # Create a client
      client = translate.TranslationServiceClient()
      # Initialize the request
      request = translate.ListAdaptiveMtFilesRequest(
          parent="projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID"
      )
      # Make the request
      response = client.list_adaptive_mt_files(request)
      # Handle the response
      print(response)
      

## Delete dataset file

Delete entries from a particular file for a given dataset. You must provide the file's ID, which is part of the file's resource name that is returned from the list files method.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * LOCATION: The region where your dataset is located, such as `us-central1`.
  * DATASET_ID: The unique identifier of your dataset that contains files to list. 
  * FILE_ID: The unique identifier of the file to delete, which is given when you list dataset files. 



HTTP method and URL: 
    
    
    DELETE https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID/adaptiveMtFiles/FILE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID/adaptiveMtFiles/FILE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID/adaptiveMtFiles/FILE_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /** Deletes an AdaptiveMtFile. */
    private static void deleteAdaptiveMtFile(
        TranslationServiceClient translationServiceClient, String fileId) {
      System.out.println("Deleting AdaptiveMtFile");
      translationServiceClient.deleteAdaptiveMtFile(fileId);
    }
      

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function deleteAdaptiveMtFile() {
      const request = {
        name: `projects/${projectId}/locations/${location}/adaptiveMtDatasets/${
            adaptiveMtDatasetName}/adaptiveMtFiles/${adaptive_mt_file_id}`,
      } const [response] = await translationClient.deleteAdaptiveMtFile(request)
      console.log('Deleting file')
      console.log(response)
    }
      

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_adaptive_mt_file():
      # Create a client
      client = translate.TranslationServiceClient()
      # Initialize the request
      request = translate.DeleteAdaptiveMtFileRequest(
          name="projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID/adaptiveMtFiles/FILE_ID"
      )
      # Make the request
      response = client.delete_adaptive_mt_file(request)
      # Handle the response
      print(response)
      

## Delete datasets

Delete a dataset to remove all its data.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER_OR_ID: the numeric or alphanumeric ID of your Google Cloud project
  * LOCATION: The region where your source dataset is located, such as `us-central1`.
  * DATASET_ID: The unique identifier of the dataset to delete. 



HTTP method and URL: 
    
    
    DELETE https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /** Deletes an AdaptiveMtDataset. */
    private static void deleteAdaptiveMtDataset(
        TranslationServiceClient translationServiceClient, String projectId, String datasetId) {
      System.out.println("Deleting AdaptiveMtDataset");
      String adaptiveMtDatasetName =
          String.format(
              "projects/%s/locations/LOCATION/adaptiveMtDatasets/%s", projectId, datasetId);
      translationServiceClient.deleteAdaptiveMtDataset(adaptiveMtDatasetName);
    }
    
    public static void main(String[] args) {
    
      String projectName = "PROJECT_NAME";
      String datasetId = "java-dataset-test";
      String gcsUri = "gs://SOURCE_LOCATION/FILE.tsv";
    
      try (TranslationServiceClient translationServiceClient = TranslationServiceClient.create()) {
    
        createAdaptiveMtDataset(translationServiceClient, projectName, datasetId);
        listAdaptiveMtDatasets(translationServiceClient, projectName);
        getAdaptiveMtDataset(translationServiceClient, projectName, datasetId);
    
        String fileId =
            importAdaptiveMtFile(translationServiceClient, projectName, datasetId, gcsUri);
    
        listAdaptiveMtFiles(translationServiceClient, projectName, datasetId);
        getAdaptiveMtFile(translationServiceClient, fileId);
    
        adaptiveMtTranslate(translationServiceClient, projectName, datasetId);
    
        deleteAdaptiveMtFile(translationServiceClient, fileId);
        deleteAdaptiveMtDataset(translationServiceClient, projectName, datasetId);
      } catch (java.io.IOException e) {
        System.out.println(e.toString());
      }
    }
      

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Node.js API reference documentation](https://googleapis.dev/nodejs/translate/latest/index.html). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    async function deleteAdaptiveMtDataset() {
      const request = {
        name: `projects/${projectId}/locations/${location}/adaptiveMtDatasets/${
            adaptiveMtDatasetName}`
      } await translationClient.deleteAdaptiveMtDataset(request)
      console.log('Deleted dataset')
    }
      

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Translation quickstart using client libraries](https://docs.cloud.google.com/translate/docs/quickstart-client-libraries). For more information, see the [Cloud Translation Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/translate/latest). 

To authenticate to Cloud Translation, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_adaptive_mt_dataset():
      # Create a client
      client = translate.TranslationServiceClient()
      # Initialize the request
      request = translate.DeleteAdaptiveMtDatasetRequest(
          name="projects/PROJECT_ID/locations/LOCATION/adaptiveMtDatasets/DATASET_ID"
      )
      # Make the request
      response = client.delete_adaptive_mt_dataset(request)
      # Handle the response
      print(response)
      

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
