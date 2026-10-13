---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action/
title: Action \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:42.139278+00:00
---

# Action  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Action Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SaveFindings
    * JSON representation
  * OutputStorageConfig
    * JSON representation
  * OutputSchema
  * PublishToPubSub
    * JSON representation
  * PublishSummaryToCscc
  * PublishFindingsToCloudDataCatalog
  * PublishFindingsToDataplexCatalog
  * Deidentify
    * JSON representation
  * TransformationConfig
    * JSON representation
  * TransformationDetailsStorageConfig
    * JSON representation
  * JobNotificationEmails
  * PublishToStackdriver



A task to execute on the completion of a job. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions> to learn more.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "saveFindings": {
        object ([SaveFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#SaveFindings))
      },
      "pubSub": {
        object ([PublishToPubSub](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishToPubSub))
      },
      "publishSummaryToCscc": {
        object ([PublishSummaryToCscc](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishSummaryToCscc))
      },
      "publishFindingsToCloudDataCatalog": {
        object ([PublishFindingsToCloudDataCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishFindingsToCloudDataCatalog))
      },
      "publishFindingsToDataplexCatalog": {
        object ([PublishFindingsToDataplexCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishFindingsToDataplexCatalog))
      },
      "deidentify": {
        object ([Deidentify](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#Deidentify))
      },
      "jobNotificationEmails": {
        object ([JobNotificationEmails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#JobNotificationEmails))
      },
      "publishToStackdriver": {
        object ([PublishToStackdriver](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishToStackdriver))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Extra events to execute after the job has finished. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`saveFindings` |  `object (`[SaveFindings](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#SaveFindings)`)` Save resulting findings in a provided location.  
`pubSub` |  `object (`[PublishToPubSub](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishToPubSub)`)` Publish a notification to a Pub/Sub topic.  
`publishSummaryToCscc` |  `object (`[PublishSummaryToCscc](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishSummaryToCscc)`)` Publish summary to Cloud Security Command Center (Alpha).  
`publishFindingsToCloudDataCatalog  
**(deprecated)**` |  `object (`[PublishFindingsToCloudDataCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishFindingsToCloudDataCatalog)`)` This item is deprecated!Deprecated because Data Catalog is being turned down. Use publishFindingsToDataplexCatalog to publish findings to Dataplex Universal Catalog.  
`publishFindingsToDataplexCatalog` |  `object (`[PublishFindingsToDataplexCatalog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishFindingsToDataplexCatalog)`)` Publish findings as an aspect to Dataplex Universal Catalog.  
`deidentify` |  `object (`[Deidentify](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#Deidentify)`)` Create a de-identified copy of the input data.  
`jobNotificationEmails` |  `object (`[JobNotificationEmails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#JobNotificationEmails)`)` Sends an email when the job completes. The email goes to IAM project owners and technical [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).  
`publishToStackdriver` |  `object (`[PublishToStackdriver](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#PublishToStackdriver)`)` Enable Stackdriver metric dlp.googleapis.com/findingCount.  
End of mutually exclusive fields.  
  
## SaveFindings

If set, the detailed findings will be persisted to the specified OutputStorageConfig. Only a single instance of this action can be specified. Compatible with: Inspect, Risk

JSON representation  
---  
      
    
    {
      "outputConfig": {
        object ([OutputStorageConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#OutputStorageConfig))
      }
    }  
  
Fields  
---  
`outputConfig` |  `object (`[OutputStorageConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#OutputStorageConfig)`)` Location to store findings outside of DLP.  
  
## OutputStorageConfig

Cloud repository for storing output.

JSON representation  
---  
      
    
    {
      "outputSchema": enum ([OutputSchema](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#OutputSchema)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "table": {
        object ([BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable))
      },
      "storagePath": {
        object ([CloudStoragePath](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/CloudStoragePath))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`outputSchema` |  `enum (`[OutputSchema](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#OutputSchema)`)` Schema used for writing the findings for Inspect jobs. This field is only used for Inspect and must be unspecified for Risk jobs. Columns are derived from the `Finding` object. If appending to an existing table, any columns from the predefined schema that are missing will be added. No columns in the existing table will be deleted.If unspecified, then all available columns will be used for a new table or an (existing) table with no schema, and no changes will be made to an existing table that has a schema. Only for use with external storage.  
Output storage types. * The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`table` |  `object (`[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable)`)` Store findings in an existing table or a new table in an existing dataset. If tableId is not set a new one will be generated for you with the following format: dlp_googleapis_yyyy_mm_dd_[dlp_job_id]. Pacific time zone will be used for generating the date details.For Inspect, each column in an existing output table must have the same name, type, and mode of a field in the `Finding` object.For Risk, an existing output table should be the output of a previous Risk analysis job run on the same source table, with the same privacy metric and quasi-identifiers. Risk jobs that analyze the same table but compute a different privacy metric, or use different sets of quasi-identifiers, cannot store their results in the same table.  
`storagePath` |  `object (`[CloudStoragePath](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/CloudStoragePath)`)` Store findings in an existing Cloud Storage bucket. Files will be generated with the job ID and file part number as the filename and will contain findings in textproto format as `[SaveToGcsFindingsOutput](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SaveToGcsFindingsOutput)`. The filename will follow the naming convention `<jobId>-<shard_number>`. Example: `my-job-id-2`.Supported for `[Inspect jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig)`. The bucket must not be the same as the bucket being inspected. If storing findings to Cloud Storage, the output schema field should not be set. If set, it will be ignored.  
End of mutually exclusive fields.  
  
## OutputSchema

Predefined schemas for storing findings. Only for use with external storage.

Enums  
---  
`OUTPUT_SCHEMA_UNSPECIFIED` | Unused.  
`BASIC_COLUMNS` | Basic schema including only `infoType`, `quote`, `certainty`, and `timestamp`.  
`GCS_COLUMNS` | Schema tailored to findings from scanning Cloud Storage.  
`DATASTORE_COLUMNS` | Schema tailored to findings from scanning Google Datastore.  
`BIG_QUERY_COLUMNS` | Schema tailored to findings from scanning Google BigQuery.  
`ALL_COLUMNS` | Schema containing all columns.  
  
## PublishToPubSub

Publish a message into a given Pub/Sub topic when DlpJob has completed. The message contains a single field, `DlpJobName`, which is equal to the finished job's [`DlpJob.name`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob). Compatible with: Inspect, Risk

JSON representation  
---  
      
    
    {
      "topic": string
    }  
  
Fields  
---  
`topic` |  `string` Cloud Pub/Sub topic to send notifications to. The topic must have given publishing access rights to the DLP API service account executing the long running DlpJob sending the notifications. Format is projects/{project}/topics/{topic}.  
  
## PublishSummaryToCscc

This type has no fields.

Publish the result summary of a DlpJob to [Security Command Center](https://cloud.google.com/security-command-center). This action is available for only projects that belong to an organization. This action publishes the count of finding instances and their infoTypes. The summary of findings are persisted in Security Command Center and are governed by [service-specific policies for Security Command Center](https://cloud.google.com/terms/service-terms). Only a single instance of this action can be specified. Compatible with: Inspect

## PublishFindingsToCloudDataCatalog

This type has no fields.

Publish findings of a DlpJob to Data Catalog. In Data Catalog, tag templates are applied to the resource that Cloud DLP scanned. Data Catalog tag templates are stored in the same project and region where the BigQuery table exists. For Cloud DLP to create and apply the tag template, the Cloud DLP service agent must have the `roles/datacatalog.tagTemplateOwner` permission on the project. The tag template contains fields summarizing the results of the DlpJob. Any field values previously written by another DlpJob are deleted. `[InfoType naming patterns](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)` are strictly enforced when using this feature.

Findings are persisted in Data Catalog storage and are governed by service-specific policies for Data Catalog. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms).

Only a single instance of this action can be specified. This action is allowed only if all resources being scanned are BigQuery tables. Compatible with: Inspect

## PublishFindingsToDataplexCatalog

This type has no fields.

Publish findings of a DlpJob to Dataplex Universal Catalog as a `sensitive-data-protection-job-result` aspect. For more information, see [Send inspection results to Dataplex Universal Catalog as aspects](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job).

Aspects are stored in Dataplex Universal Catalog storage and are governed by service-specific policies for Dataplex Universal Catalog. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms).

Only a single instance of this action can be specified. This action is allowed only if all resources being scanned are BigQuery tables. Compatible with: Inspect

## Deidentify

Create a de-identified copy of a storage bucket. Only compatible with Cloud Storage buckets.

A TransformationDetail will be created for each transformation.

Compatible with: Inspection of Cloud Storage

JSON representation  
---  
      
    
    {
      "transformationConfig": {
        object ([TransformationConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#TransformationConfig))
      },
      "transformationDetailsStorageConfig": {
        object ([TransformationDetailsStorageConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#TransformationDetailsStorageConfig))
      },
      "fileTypesToTransform": [
        enum ([FileType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FileType))
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cloudStorageOutput": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`transformationConfig` |  `object (`[TransformationConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#TransformationConfig)`)` User specified deidentify templates and configs for structured, unstructured, and image files.  
`transformationDetailsStorageConfig` |  `object (`[TransformationDetailsStorageConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#TransformationDetailsStorageConfig)`)` Config for storing transformation details.This field specifies the configuration for storing detailed metadata about each transformation performed during a de-identification process. The metadata is stored separately from the de-identified content itself and provides a granular record of both successful transformations and any failures that occurred.Enabling this configuration is essential for users who need to access comprehensive information about the status, outcome, and specifics of each transformation. The details are captured in the `[TransformationDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/TransformationDetails)` message for each operation.Key use cases:

  * **Auditing and compliance**
    * Provides a verifiable audit trail of de-identification activities, which is crucial for meeting regulatory requirements and internal data governance policies.
    * Logs what data was transformed, what transformations were applied, when they occurred, and their success status. This helps demonstrate accountability and due diligence in protecting sensitive data.
  * **Troubleshooting and debugging**
    * Offers detailed error messages and context if a transformation fails. This information is useful for diagnosing and resolving issues in the de-identification pipeline.
    * Helps pinpoint the exact location and nature of failures, speeding up the debugging process.
  * **Process verification and quality assurance**
    * Allows users to confirm that de-identification rules and transformations were applied correctly and consistently across the dataset as intended.
    * Helps in verifying the effectiveness of the chosen de-identification strategies.
  * **Data lineage and impact analysis**
    * Creates a record of how data elements were modified, contributing to data lineage. This is useful for understanding the provenance of de-identified data.
    * Aids in assessing the potential impact of de-identification choices on downstream analytical processes or data usability.
  * **Reporting and operational insights**
    * You can analyze the metadata stored in a queryable BigQuery table to generate reports on transformation success rates, common error types, processing volumes (e.g., transformedBytes), and the types of transformations applied.
    * These insights can inform optimization of de-identification configurations and resource planning.

To take advantage of these benefits, set this configuration. The stored details include a description of the transformation, success or error codes, error messages, the number of bytes transformed, the location of the transformed content, and identifiers for the job and source data.  
`fileTypesToTransform[]` |  `enum (`[FileType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FileType)`)` List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.  
Where to store the output. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cloudStorageOutput` |  `string` Required. User settable Cloud Storage bucket and folders to store de-identified files. This field must be set for Cloud Storage deidentification. The output Cloud Storage bucket must be different from the input bucket. De-identified files will overwrite files in the output path.Form of: gs://bucket/folder/ or gs://bucket  
End of mutually exclusive fields.  
  
## TransformationConfig

User specified templates and configs for how to deidentify structured, unstructures, and image files. User must provide either a unstructured deidentify template or at least one redact image config.

JSON representation  
---  
      
    
    {
      "deidentifyTemplate": string,
      "structuredDeidentifyTemplate": string,
      "imageRedactTemplate": string
    }  
  
Fields  
---  
`deidentifyTemplate` |  `string` De-identify template. If this template is specified, it will serve as the default de-identify template. This template cannot contain `recordTransformations` since it can be used for unstructured content such as free-form text files. If this template is not set, a default `ReplaceWithInfoTypeConfig` will be used to de-identify unstructured content.  
`structuredDeidentifyTemplate` |  `string` Structured de-identify template. If this template is specified, it will serve as the de-identify template for structured content such as delimited files and tables. If this template is not set but the `deidentifyTemplate` is set, then `deidentifyTemplate` will also apply to the structured content. If neither template is set, a default `ReplaceWithInfoTypeConfig` will be used to de-identify structured content.  
`imageRedactTemplate` |  `string` Image redact template. If this template is specified, it will serve as the de-identify template for images. If this template is not set, all findings in the image will be redacted with a black box.  
  
## TransformationDetailsStorageConfig

Config for storing transformation details.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "table": {
        object ([BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Location to store the transformation summary. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`table` |  `object (`[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable)`)` The BigQuery table in which to store the output. This may be an existing table or in a new table in an existing dataset. If tableId is not set a new one will be generated for you with the following format: dlp_googleapis_transformation_details_yyyy_mm_dd_[dlp_job_id]. Pacific time zone will be used for generating the date details.  
End of mutually exclusive fields.  
  
## JobNotificationEmails

This type has no fields.

Sends an email when the job completes. The email goes to IAM project owners and technical [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

## PublishToStackdriver

This type has no fields.

Enable Stackdriver metric dlp.googleapis.com/findingCount. This will publish a metric to stack driver on each infotype requested and how many findings were found for it. CustomDetectors will be bucketed as 'Custom' under the Stackdriver label 'infoType'.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
