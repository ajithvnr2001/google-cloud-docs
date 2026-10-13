---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores
title: REST Resource: organizations.analytics.datastores \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:15.917521+00:00
---

# REST Resource: organizations.analytics.datastores  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.analytics.datastores Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Datastore
    * JSON representation
  * DatastoreConfig
    * JSON representation
  * Methods



## Resource: Datastore

The data store defines the connection to export data repository (Cloud Storage, BigQuery), including the credentials used to access the data repository.

JSON representation  
---  
      
    
    {
      "self": string,
      "displayName": string,
      "org": string,
      "targetType": string,
      "createTime": string,
      "lastUpdateTime": string,
      "datastoreConfig": {
        object ([DatastoreConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores#DatastoreConfig))
      }
    }  
  
Fields  
---  
`self` |  `string` Output only. Resource link of Datastore.Example: `/organizations/{org}/analytics/datastores/{uuid}`  
`displayName` |  `string` Required. Display name in UI  
`org` |  `string` Output only. Organization that the datastore belongs to  
`targetType` |  `string` Destination storage type. Supported types `gcs` or `bigquery`.  
`createTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Datastore create time, in milliseconds since the epoch of 1970-01-01T00:00:00Z  
`lastUpdateTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Datastore last update time, in milliseconds since the epoch of 1970-01-01T00:00:00Z  
`datastoreConfig` |  `object (`[DatastoreConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores#DatastoreConfig)`)` Datastore Configurations.  
  
## DatastoreConfig

Configuration detail for datastore

JSON representation  
---  
      
    
    {
      "projectId": string,
      "bucketName": string,
      "path": string,
      "datasetName": string,
      "tablePrefix": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. Google Cloud project in which the datastore exists  
`bucketName` |  `string` Name of the Cloud Storage bucket. Required for `gcs` targetType.  
`path` |  `string` Path of Cloud Storage bucket Required for `gcs` targetType.  
`datasetName` |  `string` BigQuery dataset name Required for `bigquery` targetType.  
`tablePrefix` |  `string` Prefix of BigQuery table Required for `bigquery` targetType.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/create)`

|  Create a Datastore for an org  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/delete)`

|  Delete a Datastore from an org.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/get)`

|  Get a Datastore  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/list)`

|  List Datastores  
  
### `[test](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/test)`

|  Test if Datastore configuration is correct.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.analytics.datastores/update)`

|  Update a Datastore  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
