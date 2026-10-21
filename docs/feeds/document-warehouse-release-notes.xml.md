---
url: https://docs.cloud.google.com/feeds/document-warehouse-release-notes.xml
title: Document AI Warehouse - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:41:13.072261+00:00
---

# Document AI Warehouse - Release notes

> Source: https://docs.cloud.google.com/feeds/document-warehouse-release-notes.xml

tag:google.com,2016:document-warehouse-release-notesDocument AI Warehouse - Release notesGoogle Cloud Platform2024-01-16T00:00:00-08:00January 16, 2024tag:google.com,2016:document-warehouse-release-notes#January_16_20242024-01-16T00:00:00-08:00Deprecated 

Document AI Warehouse is deprecated and will no longer be available on Google Cloud after January 16, 2025. To safeguard your data, migrate any documents currently saved in Document AI Warehouse to an alternative like Cloud Storage. Ensure that your data migration is completed before the out of service date to prevent any data loss. See [Deprecations](https://cloud.google.com/document-warehouse/docs/deprecations/index) for details.

]]> November 02, 2023tag:google.com,2016:document-warehouse-release-notes#November_02_20232023-11-02T00:00:00-07:00Change 

Grant the `documentSchemaViewer`, `documentCreator`, and `documentViewer` roles the `contentwarehouse.googleapis.com/locations.getStatus` permission. This change enables the UI to render correctly, and does not change the security posture of these roles.

]]> October 10, 2023tag:google.com,2016:document-warehouse-release-notes#October_10_20232023-10-10T00:00:00-07:00Fixed 

Deletion operation can't be successful when raw document is missing

]]> October 02, 2023tag:google.com,2016:document-warehouse-release-notes#October_02_20232023-10-02T00:00:00-07:00Feature 

Support root folder filtering

]]> September 25, 2023tag:google.com,2016:document-warehouse-release-notes#September_25_20232023-09-25T00:00:00-07:00Feature 

Support "store_document_metadata_only" boolean flag in the Pipeline API Cloud Function response.

### Feature

Add the doc_ai_document_type and doc_ai_document_path fields to the Pipeline API Cloud Function request.

]]> September 11, 2023tag:google.com,2016:document-warehouse-release-notes#September_11_20232023-09-11T00:00:00-07:00Feature 

Validate the resource locations for all Document Warehouse API requests.

]]> August 11, 2023tag:google.com,2016:document-warehouse-release-notes#August_11_20232023-08-11T00:00:00-07:00Feature 

Pipelines support linking documents to a given folder during data ingestion.

]]> July 13, 2023tag:google.com,2016:document-warehouse-release-notes#July_13_20232023-07-13T00:00:00-07:00Feature 

Enable GenAI search (private preview) to support large documents up to 25K words.

]]> June 23, 2023tag:google.com,2016:document-warehouse-release-notes#June_23_20232023-06-23T00:00:00-07:00Fixed 

Fixed the bug where plain_text is overwritten during document creation.

]]> June 16, 2023tag:google.com,2016:document-warehouse-release-notes#June_16_20232023-06-16T00:00:00-07:00Feature 

Add support to filter for empty integer and float typed properties.

]]> April 19, 2023tag:google.com,2016:document-warehouse-release-notes#April_19_20232023-04-19T00:00:00-07:00Feature 

Added the skip_ingested_documents flag in the [Cloud Storage Ingest Pipelines](https://docs.cloud.google.com/document-warehouse/docs/gcs-ingest-pipeline) to skip ingested documents.

### Fixed

Fixed the bug that the Q&A search returns error when the search result is empty.

]]> April 07, 2023tag:google.com,2016:document-warehouse-release-notes#April_07_20232023-04-07T00:00:00-07:00Feature 

Datetime properties filtering is supported in the Document AI Warehouse UI.

]]> March 29, 2023tag:google.com,2016:document-warehouse-release-notes#March_29_20232023-03-29T00:00:00-07:00Feature 

Allow users to upload and view TIFF file types in the UI.

]]> March 28, 2023tag:google.com,2016:document-warehouse-release-notes#March_28_20232023-03-28T00:00:00-07:00Feature 

[BigQuery Connector](https://docs.cloud.google.com/document-warehouse/docs/bq-connector) (preview): Supports batch exports of document metadata into BigQuery, which enables users to do data analysis, create reports and dashboards. For example, data visualization using BI dashboards.

### Feature

DocAI Warehouse Pipelines (preview):

  * [Cloud-storage-ingest pipelines](https://docs.cloud.google.com/document-warehouse/docs/gcs-ingest-pipeline)

  * [Export-to-Workbench pipeline](https://docs.cloud.google.com/document-warehouse/docs/export-to-cdw-pipeline)

  * [Process-with-DocAI pipeline](https://docs.cloud.google.com/document-warehouse/docs/process-with-docai-pipeline)


]]> March 22, 2023tag:google.com,2016:document-warehouse-release-notes#March_22_20232023-03-22T00:00:00-07:00Feature 

Policy Engine: 

  * Modify RuleSet APIs logic to auto-populate RuleId field during create RuleSet call and allow Rules update using existing RuleId 
  * Publish action messages by default will include Schema name, Document name, RuleSet name, Rule Id, Action Id and trigger type information.

]]> February 23, 2023tag:google.com,2016:document-warehouse-release-notes#February_23_20232023-02-23T00:00:00-08:00Feature 

TIFF file UI rendering support: when calling GetDocument API for a TIFF file, the API will return a converted PNG image inside cloud_ai_document field.

### Change

Users do not need to grant the Cloud Storage roles to the Document AI Warehouse service account during the provisioning process.

]]> January 31, 2023tag:google.com,2016:document-warehouse-release-notes#January_31_20232023-01-31T00:00:00-08:00Feature 

Add field to mark raw document file type as TIFF

### Feature

Document table filter and text search state are synced with the URL to allow users to easily save and share filter settings.

]]> January 09, 2023tag:google.com,2016:document-warehouse-release-notes#January_09_20232023-01-09T00:00:00-08:00Fixed 

Fix the exception thrown when customers type a non-existent project number.

### Feature

Allow users to set Project ACLs with conditions based on document schema ID or property name.

]]> December 20, 2022tag:google.com,2016:document-warehouse-release-notes#December_20_20222022-12-20T00:00:00-08:00Change 

update the GetOperation API to remove empty response strings in pending operations.

]]> December 13, 2022tag:google.com,2016:document-warehouse-release-notes#December_13_20222022-12-13T00:00:00-08:00Fixed 

Text extracted flag (text_extraction_disabled) will be deprecated. While customers can still use it in the client library, it will be no-op in our server-side. Meanwhile, a new flag (text_extraction_enabled) will be used to replace the old one. UI will have a new button for this new flag to let customers control the behavior.

### Fixed

CreateDocument response will only return document metadata instead of the whole document.

### Change

Mark async_enabled field as internal only.

]]> December 08, 2022tag:google.com,2016:document-warehouse-release-notes#December_08_20222022-12-08T00:00:00-08:00Feature 

Partially supports Google AIP-160 syntax (https://google.aip.dev/160) in search query. Search query now supports literals, logical operators, negation operators, comparison operators, and functions.

### Fixed

Fix operation status fetching for pending AutoProvision long running operations.

### Fixed

Disable text extraction for Google Cloud Storage based ingestion.

### Feature

AutoProvision service will return an operation ID for immediate completed operations.

### Feature

VPC Service Controls for Document AI Warehouse are publicly supported.

### Feature

Enable operation service for Document AI Warehouse v1 service.

]]> November 17, 2022tag:google.com,2016:document-warehouse-release-notes#November_17_20222022-11-17T00:00:00-08:00Fixed 

Fixed the bug that users are unable to preview documents created involving Doc AI processors.

]]> November 10, 2022tag:google.com,2016:document-warehouse-release-notes#November_10_20222022-11-10T00:00:00-08:00Fixed 

Fix plain_text unintended movement in API response messages.

### Feature

Enable the validation check for Enum property values by default. Enum values that are not defined in the schema will not be allowed to be set to the corresponding document property Enum fields. The `validationCheckDisabled` flag in `EnumTypeOptions` disables the ENUM Validation.

### Feature

Enable text extraction feature.

### Fixed

Fix partial document update which could cause loss of raw document name entry.

### Fixed

Fix an issue when a user supplies multiple property filters for the same schema in the search query, the service returns error.

]]> October 17, 2022tag:google.com,2016:document-warehouse-release-notes#October_17_20222022-10-17T00:00:00-07:00Feature 

Add a validationCheckDisabled flag in EnumTypeOptions to disable ENUM Validation. The default behavior is unchanged (no validation on ENUM values is enforced).

### Feature

Add "LIKE" support in search conditions against text properties. Support search word stemming, semantic search and shuffled ordering of search query strings that run against a text property.

]]> October 10, 2022tag:google.com,2016:document-warehouse-release-notes#October_10_20222022-10-10T00:00:00-07:00Feature 

Launched Document AI Warehouse V1 APIs.

]]>
