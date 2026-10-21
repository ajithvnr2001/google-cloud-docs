---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CodeCompilationConfig/
title: CodeCompilationConfig \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:25.431433+00:00
---

# CodeCompilationConfig  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CodeCompilationConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  CodeCompilationConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * NotebookRuntimeOptions
    * JSON representation
  * GcsRepositorySnapshotDestination
    * JSON representation



Configures various aspects of Dataform code compilation.

JSON representation  
---  
      
    
    {
      "defaultDatabase": string,
      "defaultSchema": string,
      "defaultLocation": string,
      "assertionSchema": string,
      "vars": {
        string: string,
        ...
      },
      "databaseSuffix": string,
      "schemaSuffix": string,
      "tablePrefix": string,
      "builtinAssertionNamePrefix": string,
      "defaultNotebookRuntimeOptions": {
        object ([NotebookRuntimeOptions](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CodeCompilationConfig#NotebookRuntimeOptions))
      },
      "pipelineConfig": {
        object ([PipelineConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PipelineConfig))
      }
    }  
  
Fields  
---  
`defaultDatabase` |  `string` Optional. The default database (Google Cloud project ID).  
`defaultSchema` |  `string` Optional. The default schema (BigQuery dataset ID).  
`defaultLocation` |  `string` Optional. The default BigQuery location to use. Defaults to "US". See the BigQuery docs for a full list of locations: <https://cloud.google.com/bigquery/docs/locations>.  
`assertionSchema` |  `string` Optional. The default schema (BigQuery dataset ID) for assertions.  
`vars` |  `map (key: string, value: string)` Optional. User-defined variables that are made available to project code during compilation.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`databaseSuffix` |  `string` Optional. The suffix that should be appended to all database (Google Cloud project ID) names.  
`schemaSuffix` |  `string` Optional. The suffix that should be appended to all schema (BigQuery dataset ID) names.  
`tablePrefix` |  `string` Optional. The prefix that should be prepended to all table names.  
`builtinAssertionNamePrefix` |  `string` Optional. The prefix to prepend to built-in assertion names.  
`defaultNotebookRuntimeOptions` |  `object (`[NotebookRuntimeOptions](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CodeCompilationConfig#NotebookRuntimeOptions)`)` Optional. The default notebook runtime options.  
`pipelineConfig` |  `object (`[PipelineConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PipelineConfig)`)` Optional. The pipeline options which define the pipeline type and path within the Git repository.  
  
## NotebookRuntimeOptions

Configures various aspects of Dataform notebook runtime.

JSON representation  
---  
      
    
    {
      "aiPlatformNotebookRuntimeTemplate": string,
    
      // Union field execution_sink can be only one of the following:
      "gcsOutputBucket": string
      // End of list of possible types for union field execution_sink.
    
      // Union field repository_snapshot_storage can be only one of the following:
      "gcsRepositorySnapshotDestination": {
        object ([GcsRepositorySnapshotDestination](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CodeCompilationConfig#GcsRepositorySnapshotDestination))
      }
      // End of the list of possible types for union field repository_snapshot_storage.
    }  
  
Fields  
---  
`aiPlatformNotebookRuntimeTemplate` |  `string` Optional. The resource name of the [Colab runtime template](https://cloud.google.com/colab/docs/runtimes), from which a runtime is created for notebook executions. If not specified, a runtime is created with Colab's default specifications.  
Union field `execution_sink`. The location to store the notebook execution result. `execution_sink` can be only one of the following:  
`gcsOutputBucket` |  `string` Optional. The Google Cloud Storage location to upload the result to. Format: `gs://bucket-name`.  
Union field `repository_snapshot_storage`. The destination of the snapshot of repository files to be available for read-only access inside a notebook runtime `repository_snapshot_storage` can be only one of the following:  
`gcsRepositorySnapshotDestination` |  `object (`[GcsRepositorySnapshotDestination](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/CodeCompilationConfig#GcsRepositorySnapshotDestination)`)` Optional. The Google Cloud Storage destination to upload the snapshot to. For empty URI it defaults to the provided gcsOutputBucket. Format: `gs://bucket-name/path/`.  
  
## GcsRepositorySnapshotDestination

Configures the destination for a repository snapshot.

JSON representation  
---  
      
    
    {
      "repositorySnapshotUri": string
    }  
  
Fields  
---  
`repositorySnapshotUri` |  `string` Optional. The Google Cloud Storage destination to upload the repository snapshot to. Format: `gs://bucket-name/path/`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
