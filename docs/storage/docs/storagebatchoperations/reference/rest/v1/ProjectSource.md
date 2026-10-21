---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource/
title: ProjectSource \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:10:26.485321+00:00
---

# ProjectSource  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  ProjectSource Stay organized with collections  Save and categorize content based on your preferences. 

Describes the project source where the objects satisfying the filters will be transformed.

JSON representation  
---  
      
    
    {
      "project": string,
      "insightsDatasetConfig": string,
      "bucketFilters": {
        object ([Expr](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource#Expr))
      },
      "objectFilters": {
        object ([Expr](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource#Expr))
      },
      "dryRunJobId": string,
      "targetLocations": {
        object ([TargetLocations](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource#TargetLocations))
      },
      "snapshotTime": string
    }  
  
Fields  
---  
`project` |  `string` Required. Project name of the objects to be transformed, for example, `projects/my-project` or `projects/123456`.  
`insightsDatasetConfig` |  `string` Required. The resource identifier of the Storage Insights dataset configuration. Storage batch operations uses the latest snapshot from this dataset as the source to list and filter target objects. Format: `projects/{projectId}/locations/{location}/datasetConfigs/{dataset_config}`.  
`bucketFilters` |  `object (`[Expr](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource#Expr)`)` Optional. Filters expressed in Common Expression Language (CEL) to apply to buckets to identify buckets with objects to be transformed.  
`objectFilters` |  `object (`[Expr](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource#Expr)`)` Optional. Filters expressed in Common Expression Language (CEL) to apply to objects to identify objects to be transformed.  
`dryRunJobId` |  `string` Optional. The unique identifier of a dry run job to use as the baseline for the current job.Specifying this ID ensures the job is executed against the same set of objects validated during the dry run. The value corresponds to the {jobId} segment of the resource name: `projects/{projectId}/locations/{location}/jobs/{jobId}`.  
`targetLocations` |  `object (`[TargetLocations](https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/ProjectSource#TargetLocations)`)` Optional. Specifies the Cloud Storage locations to include in the job. If provided, only buckets and objects within these locations will be discovered from the Storage Insights dataset as configured in the `insightsDatasetConfig`. If omitted, the job will discover buckets and objects from all locations configured in the `insightsDatasetConfig`.  
`snapshotTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The snapshot time used by the job to read the Storage Insights dataset for bucket and object discovery. This field is populated by the service and reflects the exact timestamp of the dataset snapshot used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Expr

Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at <https://github.com/google/cel-spec>.

Example (Comparison):
    
    
    title: "Summary size limit"
    description: "Determines if a summary is less than 100 chars"
    expression: "document.summary.size() < 100"
    

Example (Equality):
    
    
    title: "Requestor is owner"
    description: "Determines if requestor is the document owner"
    expression: "document.owner == request.auth.claims.email"
    

Example (Logic):
    
    
    title: "Public documents"
    description: "Determine whether the document should be publicly visible"
    expression: "document.type != 'private' && document.type != 'internal'"
    

Example (Data Manipulation):
    
    
    title: "Notification string"
    description: "Create a notification string with a timestamp."
    expression: "'New message received at ' + string(document.create_time)"
    

The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information.

JSON representation  
---  
      
    
    {
      "expression": string,
      "title": string,
      "description": string,
      "location": string
    }  
  
Fields  
---  
`expression` |  `string` Textual representation of an expression in Common Expression Language syntax.  
`title` |  `string` Optional. Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression.  
`description` |  `string` Optional. Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI.  
`location` |  `string` Optional. String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.  
  
## TargetLocations

Describes the Cloud Storage locations to include in a ProjectSource job.

JSON representation  
---  
      
    
    {
      "locations": [
        string
      ],
      "snapshotTime": string
    }  
  
Fields  
---  
`locations[]` |  `string` Required. A list of Cloud Storage locations (for example, `us-central1`) to include in the job.If `snapshotTime` is omitted, the job automatically defaults to the most recent snapshot timestamp that is successfully populated in both the `object_attributes_view` and `bucket_attributes_view` across all specified locations.For details about Storage Insights dataset snapshots and views, see [Storage Insights dataset tables and schemas](https://cloud.google.com/storage/docs/insights/dataset-tables-and-schemas#schema).  
`snapshotTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The exact Storage Insights dataset snapshot timestamp to use for the job compatible with the RFC 3339 format (for example, `2024-01-02T03:04:05Z`).If specified, this exact snapshot must exist in both the `object_attributes_view` and `bucket_attributes_view` for every location listed in `locations`. If the snapshot is missing from either view in any of the locations, the job fails.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
