---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning/
title: Method: analyzeIamPolicyLongrunning \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:02.578405+00:00
---

# Method: analyzeIamPolicyLongrunning  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: analyzeIamPolicyLongrunning Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Response body
  * Authorization scopes
  * IamPolicyAnalysisOutputConfig
    * JSON representation
  * GcsDestination
    * JSON representation
  * BigQueryDestination
    * JSON representation
  * PartitionKey
  * Try it!



Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination. For Cloud Storage destination, the output format is the JSON format that represents a `[AnalyzeIamPolicyResponse](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#body.AnalyzeIamPolicyResponse)`. This method implements the `[google.longrunning.Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Operation)`, which allows you to track the operation status. We recommend intervals of at least 2 seconds with exponential backoff retry to poll the operation result. The metadata contains the metadata for the long-running operation.

### HTTP request

`POST https://cloudasset.googleapis.com/v1/{analysisQuery.scope=*/*}:analyzeIamPolicyLongrunning`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`analysisQuery.scope` |  `string` Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed.This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `scope`:

  * `cloudasset.assets.analyzeIamPolicy`
  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.searchAllIamPolicies`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "analysisQuery": {
        "scope": string,
        "resourceSelector": {
          "fullResourceName": string
        },
        "identitySelector": {
          "identity": string
        },
        "accessSelector": {
          "roles": [
            string
          ],
          "permissions": [
            string
          ]
        },
        "options": {
          "expandGroups": boolean,
          "expandRoles": boolean,
          "expandResources": boolean,
          "outputResourceEdges": boolean,
          "outputGroupEdges": boolean,
          "analyzeServiceAccountImpersonation": boolean
        },
        "conditionContext": {
    
          // Union field TimeContext can be only one of the following:
          "accessTime": string
          // End of list of possible types for union field TimeContext.
        }
      },
      "savedAnalysisQuery": string,
      "outputConfig": {
        object ([IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning#IamPolicyAnalysisOutputConfig))
      }
    }  
  
Fields  
---  
`analysisQuery.resourceSelector` |  `object (`[ResourceSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#ResourceSelector)`)` Optional. Specifies a resource for analysis.  
`analysisQuery.identitySelector` |  `object (`[IdentitySelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#IdentitySelector)`)` Optional. Specifies an identity for analysis.  
`analysisQuery.accessSelector` |  `object (`[AccessSelector](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#AccessSelector)`)` Optional. Specifies roles or permissions for analysis. This is optional.  
`analysisQuery.options` |  `object (`[Options](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#Options)`)` Optional. The query options.  
`analysisQuery.conditionContext` |  `object (`[ConditionContext](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#ConditionContext)`)` Optional. The hypothetical context for IAM conditions evaluation.  
`savedAnalysisQuery` |  `string` Optional. The name of a saved query, which must be in the format of:

  * projects/projectNumber/savedQueries/savedQueryId
  * folders/folder_number/savedQueries/savedQueryId
  * organizations/organization_number/savedQueries/savedQueryId

If both `analysisQuery` and `savedAnalysisQuery` are provided, they will be merged together with the `savedAnalysisQuery` as base and the `analysisQuery` as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) doc.Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn't support field presence yet.  
`outputConfig` |  `object (`[IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning#IamPolicyAnalysisOutputConfig)`)` Required. Output configuration indicating where the results will be output to.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## IamPolicyAnalysisOutputConfig

Output configuration for export IAM policy analysis destination.

JSON representation  
---  
      
    
    {
    
      // Union field destination can be only one of the following:
      "gcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning#GcsDestination))
      },
      "bigqueryDestination": {
        object ([BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning#BigQueryDestination))
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
Union field `destination`. IAM policy analysis export destination. `destination` can be only one of the following:  
`gcsDestination` |  `object (`[GcsDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning#GcsDestination)`)` Destination on Cloud Storage.  
`bigqueryDestination` |  `object (`[BigQueryDestination](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning#BigQueryDestination)`)` Destination on BigQuery.  
  
## GcsDestination

A Cloud Storage location.

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` Required. The URI of the Cloud Storage object. It's the same URI that is used by gcloud storage. Example: "gs://bucket_name/object_name". See [Viewing and Editing Object Metadata](https://cloud.google.com/storage/docs/viewing-editing-metadata) for more information.If the specified Cloud Storage object already exists and there is no [hold](https://cloud.google.com/storage/docs/object-holds), it will be overwritten with the analysis result.  
  
## BigQueryDestination

A BigQuery destination.

JSON representation  
---  
      
    
    {
      "dataset": string,
      "tablePrefix": string,
      "partitionKey": enum ([PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning#PartitionKey)),
      "writeDisposition": string
    }  
  
Fields  
---  
`dataset` |  `string` Required. The BigQuery dataset in format "projects/projectId/datasets/datasetId", to which the analysis results should be exported. If this dataset does not exist, the export call will return an INVALID_ARGUMENT error.  
`tablePrefix` |  `string` Required. The prefix of the BigQuery tables to which the analysis results will be written. Tables will be created based on this tablePrefix if not exist: * _analysis table will contain export operation's metadata. * _analysis_result will contain all the `[IamPolicyAnalysisResult](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicy#IamPolicyAnalysisResult)`. When [partitionKey] is specified, both tables will be partitioned based on the [partitionKey].  
`partitionKey` |  `enum (`[PartitionKey](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning#PartitionKey)`)` The partition key for BigQuery partitioned table.  
`writeDisposition` |  `string` Optional. Specifies the action that occurs if the destination table or partition already exists. The following values are supported:

  * WRITE_TRUNCATE: If the table or partition already exists, BigQuery overwrites the entire table or all the partitions data.
  * WRITE_APPEND: If the table or partition already exists, BigQuery appends the data to the table or the latest partition.
  * WRITE_EMPTY: If the table already exists and contains data, an error is returned.

The default value is WRITE_APPEND. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Details are at <https://cloud.google.com/bigquery/docs/loading-data-local#appending_to_or_overwriting_a_table_using_a_local_file>.  
  
## PartitionKey

This enum determines the partition key column for the bigquery tables. Partitioning can improve query performance and reduce query cost by filtering partitions. Refer to <https://cloud.google.com/bigquery/docs/partitioned-tables> for details.

Enums  
---  
`PARTITION_KEY_UNSPECIFIED` | Unspecified partition key. Tables won't be partitioned using this option.  
`REQUEST_TIME` | The time when the request is received. If specified as partition key, the result table(s) is partitioned by the RequestTime column, an additional timestamp column representing when the request was received.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-24 UTC."],[],[]] 
