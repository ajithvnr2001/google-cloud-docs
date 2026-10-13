---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments
title: REST Resource: organizations.environments.archiveDeployments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:51.456732+00:00
---

# REST Resource: organizations.environments.archiveDeployments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.environments.archiveDeployments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ArchiveDeployment
    * JSON representation
  * Methods



## Resource: ArchiveDeployment

Archive Deployment information.

JSON representation  
---  
      
    
    {
      "name": string,
      "labels": {
        string: string,
        ...
      },
      "createdAt": string,
      "updatedAt": string,
      "operation": string,
    
      // Union field source can be only one of the following:
      "gcsUri": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`name` |  `string` Name of the Archive Deployment in the following format: `organizations/{org}/environments/{env}/archiveDeployments/{id}`.  
`labels` |  `map (key: string, value: string)` User-supplied key-value pairs used to organize ArchiveDeployments.Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}Label values must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63}No more than 64 labels can be associated with a given store.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The time at which the Archive Deployment was created in milliseconds since the epoch.  
`updatedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The time at which the Archive Deployment was updated in milliseconds since the epoch.  
`operation` |  `string` Output only. A reference to the LRO that created this Archive Deployment in the following format: `organizations/{org}/operations/{id}`  
Union field `source`. The location of the data used to create this ArchiveDeployment. `source` can be only one of the following:  
`gcsUri` |  `string` Input only. The Google Cloud Storage signed URL returned from archiveDeployments.generateUploadUrl and used to upload the Archive zip file.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/create)`

|  Creates a new ArchiveDeployment.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/delete)`

|  Deletes an archive deployment.  
  
### `[generateDownloadUrl](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/generateDownloadUrl)`

|  Generates a signed URL for downloading the original zip file used to create an Archive Deployment.  
  
### `[generateUploadUrl](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/generateUploadUrl)`

|  Generates a signed URL for uploading an Archive zip file to Google Cloud Storage.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/get)`

|  Gets the specified ArchiveDeployment.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/list)`

|  Lists the ArchiveDeployments in the specified Environment.  
  
### `[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/patch)`

|  Updates an existing ArchiveDeployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
