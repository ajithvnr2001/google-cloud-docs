---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores/trainCustomModel/
title: Method: projects.locations.collections.dataStores.trainCustomModel \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:02.982881+00:00
---

# Method: projects.locations.collections.dataStores.trainCustomModel  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores/trainCustomModel/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.trainCustomModel Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * GcsTrainingInput
    * JSON representation



Trains a custom model.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1/{dataStore=projects/*/locations/*/collections/*/dataStores/*}:trainCustomModel`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`dataStore` |  `string` Required. The resource name of the Data Store, such as `projects/*/locations/global/collections/default_collection/dataStores/default_data_store`. This field is used to identify the data store where to train the models.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "modelType": string,
      "errorConfig": {
        object ([ImportErrorConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/ImportErrorConfig))
      },
      "modelId": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gcsTrainingInput": {
        object ([GcsTrainingInput](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores/trainCustomModel#GcsTrainingInput))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`modelType` |  `string` Model to be trained. Supported values are:

  * **search-tuning** : Fine tuning the search system based on data provided.

  
`errorConfig` |  `object (`[ImportErrorConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/ImportErrorConfig)`)` The desired location of errors incurred during the data ingestion and training.  
`modelId` |  `string` If not provided, a UUID will be generated.  
Model training input. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gcsTrainingInput` |  `object (`[GcsTrainingInput](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores/trainCustomModel#GcsTrainingInput)`)` Cloud Storage training input.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `dataStore` resource:

  * `discoveryengine.dataStores.trainCustomModel`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## GcsTrainingInput

Cloud Storage training data input.

JSON representation  
---  
      
    
    {
      "corpusDataPath": string,
      "queryDataPath": string,
      "trainDataPath": string,
      "testDataPath": string
    }  
  
Fields  
---  
`corpusDataPath` |  `string` The Cloud Storage corpus data which could be associated in train data. The data path format is `gs://<bucket_to_data>/<jsonl_file_name>`. A newline delimited jsonl/ndjson file.For search-tuning model, each line should have the Id, title and text. Example: `{"Id": "doc1", title: "relevant doc", "text": "relevant text"}`  
`queryDataPath` |  `string` The gcs query data which could be associated in train data. The data path format is `gs://<bucket_to_data>/<jsonl_file_name>`. A newline delimited jsonl/ndjson file.For search-tuning model, each line should have the Id and text. Example: {"Id": "query1", "text": "example query"}  
`trainDataPath` |  `string` Cloud Storage training data path whose format should be `gs://<bucket_to_data>/<tsv_file_name>`. The file should be in tsv format. Each line should have the docId and queryId and score (number).For search-tuning model, it should have the query-id corpus-id score as tsv file header. The score should be a number in `[0, inf+)`. The larger the number is, the more relevant the pair is. Example:

  * `query-id\tcorpus-id\tscore`
  * `query1\tdoc1\t1`

  
`testDataPath` |  `string` Cloud Storage test data. Same format as trainDataPath. If not provided, a random 80/20 train/test split will be performed on trainDataPath.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
