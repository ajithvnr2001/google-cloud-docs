---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import/
title: Method: ragFiles.import \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:20:32.992441+00:00
---

# Method: ragFiles.import  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: ragFiles.import Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.ragCorpora.ragFiles.import

Import files from Google Cloud Storage or Google Drive into a RagCorpus.

### Endpoint

post  `https://{service-endpoint}/v1/{parent}/ragFiles:import`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The name of the RagCorpus resource into which to import files. Format: `projects/{project}/locations/{location}/ragCorpora/{ragCorpus}`

### Request body

The request body contains data with the following structure: | Fields  
  
`importRagFilesConfig` `object (`[ImportRagFilesConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import#ImportRagFilesConfig)`)` Required. The config for the RagFiles to be synced and imported into the RagCorpus. `[VertexRagDataService.ImportRagFiles](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import#google.cloud.aiplatform.v1.VertexRagDataService.ImportRagFiles)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

## ImportRagFilesConfig

Config for importing RagFiles. | Fields  
  
`ragFileTransformationConfig` `object (`[RagFileTransformationConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagFileTransformationConfig)`)` Specifies the transformation config for RagFiles. | `ragFileParsingConfig` `object (`[RagFileParsingConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import#RagFileParsingConfig)`)` Optional. Specifies the parsing config for RagFiles. RAG will use the default parser if this field is not set. | `maxEmbeddingRequestsPerMin` `integer` Optional. The max number of queries per minute that this job is allowed to make to the embedding model specified on the corpus. This value is specific to this job and not shared across other import jobs. Consult the Quotas page on the project to set an appropriate value here. If unspecified, a default value of 1,000 QPM would be used. | `rebuildAnnIndex` `boolean` Rebuilds the ANN index to optimize for recall on the imported data. Only applicable for RagCorpora running on RagManagedDb with `retrieval_strategy` set to `ANN`. The rebuild will be performed using the existing ANN config set on the RagCorpus. To change the ANN config, please use the UpdateRagCorpus API.Default is false, i.e., index is not rebuilt. | `import_source` `Union type`  
  
The source of the import. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`gcsSource` `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GcsSource)`)` Google Cloud Storage location. Supports importing individual files as well as entire Google Cloud Storage directories. Sample formats: - `gs://bucketName/my_directory/objectName/my_file.txt` \- `gs://bucketName/my_directory` | `googleDriveSource` `object (`[GoogleDriveSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#GoogleDriveSource)`)` Google Drive location. Supports importing individual files as well as Google Drive folders. | `slackSource` `object (`[SlackSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SlackSource)`)` Slack channels with their corresponding access tokens. | `jiraSource` `object (`[JiraSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#JiraSource)`)` Jira queries with their corresponding authentication. | `sharePointSources` `object (`[SharePointSources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SharePointSources)`)` SharePoint sources. End of mutually exclusive fields. | `partial_failure_sink` `Union type`  
  
Optional. If provided, all partial failures are written to the sink. Deprecated. Prefer to use the `import_result_sink`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`partialFailureGcsSink  
**(deprecated)**` `object (`[GcsDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#GcsDestination)`)` This item is deprecated!The Cloud Storage path to write partial failures to. Deprecated. Prefer to use `importResultGcsSink`. | `partialFailureBigquerySink  
**(deprecated)**` `object (`[BigQueryDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/BigQueryDestination)`)` This item is deprecated!The BigQuery destination to write partial failures to. It should be a bigquery table resource name (e.g. "bq://projectId.bqDatasetId.bqTableId"). The dataset must exist. If the table does not exist, it will be created with the expected schema. If the table exists, the schema will be validated and data will be added to this existing table. Deprecated. Prefer to use `import_result_bq_sink`. End of mutually exclusive fields. | `import_result_sink` `Union type`  
  
Optional. If provided, all successfully imported files and all partial failures are written to the sink. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`importResultGcsSink` `object (`[GcsDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#GcsDestination)`)` The Cloud Storage path to write import result to. | `importResultBigquerySink` `object (`[BigQueryDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/BigQueryDestination)`)` The BigQuery destination to write import result to. It should be a bigquery table resource name (e.g. "bq://projectId.bqDatasetId.bqTableId"). The dataset must exist. If the table does not exist, it will be created with the expected schema. If the table exists, the schema will be validated and data will be added to this existing table. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "ragFileTransformationConfig": {
        object ([RagFileTransformationConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagFileTransformationConfig))
      },
      "ragFileParsingConfig": {
        object ([RagFileParsingConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import#RagFileParsingConfig))
      },
      "maxEmbeddingRequestsPerMin": integer,
      "rebuildAnnIndex": boolean,
    
      // import_source
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GcsSource))
      },
      "googleDriveSource": {
        object ([GoogleDriveSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#GoogleDriveSource))
      },
      "slackSource": {
        object ([SlackSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SlackSource))
      },
      "jiraSource": {
        object ([JiraSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#JiraSource))
      },
      "sharePointSources": {
        object ([SharePointSources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles#SharePointSources))
      }
      // Union type
    
      // partial_failure_sink
      "partialFailureGcsSink": {
        object ([GcsDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#GcsDestination))
      },
      "partialFailureBigquerySink": {
        object ([BigQueryDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/BigQueryDestination))
      }
      // Union type
    
      // import_result_sink
      "importResultGcsSink": {
        object ([GcsDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#GcsDestination))
      },
      "importResultBigquerySink": {
        object ([BigQueryDestination](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/BigQueryDestination))
      }
      // Union type
    }  
  
## RagFileParsingConfig

Specifies the parsing config for RagFiles.

Fields  
  
`parser` `Union type`  
  
The parser to use for RagFiles. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`layoutParser` `object (`[LayoutParser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import#LayoutParser)`)` The Layout Parser to use for RagFiles. | `llmParser` `object (`[LlmParser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import#LlmParser)`)` The LLM Parser to use for RagFiles. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // parser
      "layoutParser": {
        object ([LayoutParser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import#LayoutParser))
      },
      "llmParser": {
        object ([LlmParser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import#LlmParser))
      }
      // Union type
    }  
  
## LayoutParser

Document AI Layout Parser config.

Fields  
  
`processorName` `string` The full resource name of a Document AI processor or processor version. The processor must have type `LAYOUT_PARSER_PROCESSOR`. If specified, the `additionalConfig.parse_as_scanned_pdf` field must be false. Format: * `projects/{projectId}/locations/{location}/processors/{processorId}` * `projects/{projectId}/locations/{location}/processors/{processorId}/processorVersions/{processor_version_id}` | `maxParsingRequestsPerMin` `integer` The maximum number of requests the job is allowed to make to the Document AI processor per minute. Consult <https://cloud.google.com/document-ai/quotas> and the Quota page for your project to set an appropriate value here. If unspecified, a default value of 120 QPM would be used. | JSON representation  
---  
      
    
    {
      "processorName": string,
      "maxParsingRequestsPerMin": integer
    }  
  
## LlmParser

Specifies the LLM parsing for RagFiles.

Fields  
  
`modelName` `string` The name of a LLM model used for parsing. Format: * `projects/{projectId}/locations/{location}/publishers/{publisher}/models/{model}` | `maxParsingRequestsPerMin` `integer` The maximum number of requests the job is allowed to make to the LLM model per minute. Consult <https://cloud.google.com/vertex-ai/generative-ai/docs/quotas> and your document size to set an appropriate value here. If unspecified, a default value of 5000 QPM would be used. | `customParsingPrompt` `string` The prompt to use for parsing. If not specified, a default prompt will be used. | JSON representation  
---  
      
    
    {
      "modelName": string,
      "maxParsingRequestsPerMin": integer,
      "customParsingPrompt": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
