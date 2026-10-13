---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/list/
title: Method: projects.locations.migrationJobs.objects.list \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:39.613917+00:00
---

# Method: projects.locations.migrationJobs.objects.list  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  Method: projects.locations.migrationJobs.objects.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Use this method to list the objects of a specific migration job.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west15 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8

  
`GET https://datamigration.googleapis.com/v1/{parent}/objects`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent migration job that owns the collection of objects.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of objects to return. Default is 50. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. Page token received from a previous `ListMigrationJObObjectsRequest` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListMigrationJobObjectsRequest` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response containing the objects for a migration job.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "migrationJobObjects": [
        {
          object ([MigrationJobObject](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects#MigrationJobObject))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`migrationJobObjects[]` |  `object (`[MigrationJobObject](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects#MigrationJobObject)`)` List of migration job objects.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-datamigration `



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `datamigration.objects.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
