---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeConversionWorkspaceRevisions/
title: Method: projects.locations.conversionWorkspaces.describeConversionWorkspaceRevisions \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:31.615137+00:00
---

# Method: projects.locations.conversionWorkspaces.describeConversionWorkspaceRevisions  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeConversionWorkspaceRevisions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  Method: projects.locations.conversionWorkspaces.describeConversionWorkspaceRevisions Stay organized with collections  Save and categorize content based on your preferences. 

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



Retrieves a list of committed revisions of a specific conversion workspace.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west15 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8

  
`GET https://datamigration.googleapis.com/v1/{conversionWorkspace}:describeConversionWorkspaceRevisions`

### Path parameters

Parameters  
---  
`conversionWorkspace` |  `string` Required. Name of the conversion workspace resource whose revisions are listed. Must be in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversionWorkspace}.  
  
### Query parameters

Parameters  
---  
`commitId` |  `string` Optional. Optional filter to request a specific commit ID.  
  
### Request body

The request body must be empty.

### Response body

Response message for 'conversionWorkspaces.describeConversionWorkspaceRevisions' request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "revisions": [
        {
          object ([ConversionWorkspace](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces#ConversionWorkspace))
        }
      ]
    }  
  
Fields  
---  
`revisions[]` |  `object (`[ConversionWorkspace](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces#ConversionWorkspace)`)` The list of conversion workspace revisions.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-datamigration `



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `conversionWorkspace` resource:

  * `datamigration.conversionworkspaces.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
