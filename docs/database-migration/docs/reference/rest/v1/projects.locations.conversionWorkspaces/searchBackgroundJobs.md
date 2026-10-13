---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs/
title: Method: projects.locations.conversionWorkspaces.searchBackgroundJobs \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:37.850319+00:00
---

# Method: projects.locations.conversionWorkspaces.searchBackgroundJobs  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  Method: projects.locations.conversionWorkspaces.searchBackgroundJobs Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * BackgroundJobLogEntry
    * JSON representation
  * BackgroundJobType
  * JobCompletionState
  * SeedJobDetails
    * JSON representation
  * ImportRulesJobDetails
    * JSON representation
  * ConvertJobDetails
    * JSON representation
  * ApplyJobDetails
    * JSON representation
  * Examples
  * Try it!



Searches/lists the background jobs for a specific conversion workspace.

The background jobs are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are a way to expose the data plane jobs log.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west15 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8

  
`GET https://datamigration.googleapis.com/v1/{conversionWorkspace}:searchBackgroundJobs`

### Path parameters

Parameters  
---  
`conversionWorkspace` |  `string` Required. Name of the conversion workspace resource whose jobs are listed, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversionWorkspace}.  
  
### Query parameters

Parameters  
---  
`returnMostRecentPerJobType` |  `boolean` Optional. Whether or not to return just the most recent job per job type,  
`maxSize` |  `integer` Optional. The maximum number of jobs to return. The service may return fewer than this value. If unspecified, at most 100 jobs are returned. The maximum value is 100; values above 100 are coerced to 100.  
`completedUntilTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. If provided, only returns jobs that completed until (not including) the given timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Request body

The request body must be empty.

### Response body

Response message for 'conversionWorkspaces.searchBackgroundJobs' request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "jobs": [
        {
          object ([BackgroundJobLogEntry](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#BackgroundJobLogEntry))
        }
      ]
    }  
  
Fields  
---  
`jobs[]` |  `object (`[BackgroundJobLogEntry](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#BackgroundJobLogEntry)`)` The list of conversion workspace mapping rules.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-datamigration `



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `conversionWorkspace` resource:

  * `datamigration.conversionworkspaces.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## BackgroundJobLogEntry

Execution log of a background job.

JSON representation  
---  
      
    
    {
      "id": string,
      "jobType": enum ([BackgroundJobType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#BackgroundJobType)),
      "startTime": string,
      "finishTime": string,
      "completionState": enum ([JobCompletionState](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#JobCompletionState)),
      "completionComment": string,
      "requestAutocommit": boolean,
    
      // Union field job_details can be only one of the following:
      "seedJobDetails": {
        object ([SeedJobDetails](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#SeedJobDetails))
      },
      "importRulesJobDetails": {
        object ([ImportRulesJobDetails](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#ImportRulesJobDetails))
      },
      "convertJobDetails": {
        object ([ConvertJobDetails](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#ConvertJobDetails))
      },
      "applyJobDetails": {
        object ([ApplyJobDetails](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#ApplyJobDetails))
      }
      // End of list of possible types for union field job_details.
    }  
  
Fields  
---  
`id` |  `string` The background job log entry ID.  
`jobType` |  `enum (`[BackgroundJobType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#BackgroundJobType)`)` The type of job that was executed.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when the background job was started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`finishTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp when the background job was finished.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`completionState` |  `enum (`[JobCompletionState](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#JobCompletionState)`)` Output only. Job completion state, i.e. the final state after the job completed.  
`completionComment` |  `string` Output only. Job completion comment, such as how many entities were seeded, how many warnings were found during conversion, and similar information.  
`requestAutocommit` |  `boolean` Output only. Whether the client requested the conversion workspace to be committed after a successful completion of the job.  
Union field `job_details`.`job_details` can be only one of the following:  
`seedJobDetails` |  `object (`[SeedJobDetails](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#SeedJobDetails)`)` Output only. Seed job details.  
`importRulesJobDetails` |  `object (`[ImportRulesJobDetails](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#ImportRulesJobDetails)`)` Output only. Import rules job details.  
`convertJobDetails` |  `object (`[ConvertJobDetails](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#ConvertJobDetails)`)` Output only. Convert job details.  
`applyJobDetails` |  `object (`[ApplyJobDetails](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs#ApplyJobDetails)`)` Output only. Apply job details.  
  
## BackgroundJobType

The types of jobs that can be executed in the background.

Enums  
---  
`BACKGROUND_JOB_TYPE_UNSPECIFIED` | Unspecified background job type.  
`BACKGROUND_JOB_TYPE_SOURCE_SEED` | Job to seed from the source database.  
`BACKGROUND_JOB_TYPE_CONVERT` | Job to convert the source database into a draft of the destination database.  
`BACKGROUND_JOB_TYPE_APPLY_DESTINATION` | Job to apply the draft tree onto the destination.  
`BACKGROUND_JOB_TYPE_IMPORT_RULES_FILE` | Job to import and convert mapping rules from an external source such as an ora2pg config file.  
  
## JobCompletionState

Final state after a job completes.

Enums  
---  
`JOB_COMPLETION_STATE_UNSPECIFIED` | The status is not specified. This state is used when job is not yet finished.  
`SUCCEEDED` | Success.  
`FAILED` | Error.  
  
## SeedJobDetails

Details regarding a Seed background job.

JSON representation  
---  
      
    
    {
      "connectionProfile": string
    }  
  
Fields  
---  
`connectionProfile` |  `string` Output only. The connection profile which was used for the seed job.  
  
## ImportRulesJobDetails

Details regarding an Import Rules background job.

JSON representation  
---  
      
    
    {
      "files": [
        string
      ],
      "fileFormat": enum ([ImportRulesFileFormat](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/ImportRulesFileFormat))
    }  
  
Fields  
---  
`files[]` |  `string` Output only. File names used for the import rules job.  
`fileFormat` |  `enum (`[ImportRulesFileFormat](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/ImportRulesFileFormat)`)` Output only. The requested file format.  
  
## ConvertJobDetails

Details regarding a Convert background job.

JSON representation  
---  
      
    
    {
      "filter": string
    }  
  
Fields  
---  
`filter` |  `string` Output only. AIP-160 based filter used to specify the entities to convert  
  
## ApplyJobDetails

Details regarding an Apply background job.

JSON representation  
---  
      
    
    {
      "connectionProfile": string,
      "filter": string
    }  
  
Fields  
---  
`connectionProfile` |  `string` Output only. The connection profile which was used for the apply job.  
`filter` |  `string` Output only. AIP-160 based filter used to specify the entities to apply  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
