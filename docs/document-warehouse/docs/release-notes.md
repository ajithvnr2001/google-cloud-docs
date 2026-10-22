---
url: https://docs.cloud.google.com/document-warehouse/docs/release-notes/
title: Document AI Warehouse release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:26.043084+00:00
---

# Document AI Warehouse release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Resources ](https://docs.cloud.google.com/document-warehouse/docs/resources)



Send feedback 

#  Document AI Warehouse release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Document AI Warehouse. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/document-warehouse-release-notes.xml) directly. 

## January 16, 2024

Deprecated

Document AI Warehouse is deprecated and will no longer be available on Google Cloud after January 16, 2025. To safeguard your data, migrate any documents currently saved in Document AI Warehouse to an alternative like Cloud Storage. Ensure that your data migration is completed before the out of service date to prevent any data loss. See [Deprecations](https://cloud.google.com/document-warehouse/docs/deprecations/index) for details.

## November 02, 2023

Change

Grant the `documentSchemaViewer`, `documentCreator`, and `documentViewer` roles the `contentwarehouse.googleapis.com/locations.getStatus` permission. This change enables the UI to render correctly, and does not change the security posture of these roles.

## October 10, 2023

Fixed

Deletion operation can't be successful when raw document is missing

## October 02, 2023

Feature

Support root folder filtering

## September 25, 2023

Feature

Support "store_document_metadata_only" boolean flag in the Pipeline API Cloud Function response.

Feature

Add the doc_ai_document_type and doc_ai_document_path fields to the Pipeline API Cloud Function request.

## September 11, 2023

Feature

Validate the resource locations for all Document Warehouse API requests.

## August 11, 2023

Feature

Pipelines support linking documents to a given folder during data ingestion.

## July 13, 2023

Feature

Enable GenAI search (private preview) to support large documents up to 25K words.

## June 23, 2023

Fixed

Fixed the bug where plain_text is overwritten during document creation.

## June 16, 2023

Feature

Add support to filter for empty integer and float typed properties.

## April 19, 2023

Feature

Added the skip_ingested_documents flag in the [Cloud Storage Ingest Pipelines](https://docs.cloud.google.com/document-warehouse/docs/gcs-ingest-pipeline) to skip ingested documents.

Fixed

Fixed the bug that the Q&A search returns error when the search result is empty.

## April 07, 2023

Feature

Datetime properties filtering is supported in the Document AI Warehouse UI.

## March 29, 2023

Feature

Allow users to upload and view TIFF file types in the UI.

## March 28, 2023

Feature

[BigQuery Connector](https://docs.cloud.google.com/document-warehouse/docs/bq-connector) (preview): Supports batch exports of document metadata into BigQuery, which enables users to do data analysis, create reports and dashboards. For example, data visualization using BI dashboards.

Feature

DocAI Warehouse Pipelines (preview):

  * [Cloud-storage-ingest pipelines](https://docs.cloud.google.com/document-warehouse/docs/gcs-ingest-pipeline)

  * [Export-to-Workbench pipeline](https://docs.cloud.google.com/document-warehouse/docs/export-to-cdw-pipeline)

  * [Process-with-DocAI pipeline](https://docs.cloud.google.com/document-warehouse/docs/process-with-docai-pipeline)




## March 22, 2023

Feature

Policy Engine: 

  * Modify RuleSet APIs logic to auto-populate RuleId field during create RuleSet call and allow Rules update using existing RuleId 
  * Publish action messages by default will include Schema name, Document name, RuleSet name, Rule Id, Action Id and trigger type information.



## February 23, 2023

Feature

TIFF file UI rendering support: when calling GetDocument API for a TIFF file, the API will return a converted PNG image inside cloud_ai_document field.

Change

Users do not need to grant the Cloud Storage roles to the Document AI Warehouse service account during the provisioning process.

## January 31, 2023

Feature

Add field to mark raw document file type as TIFF

Feature

Document table filter and text search state are synced with the URL to allow users to easily save and share filter settings.

## January 09, 2023

Fixed

Fix the exception thrown when customers type a non-existent project number.

Feature

Allow users to set Project ACLs with conditions based on document schema ID or property name.

## December 20, 2022

Change

update the GetOperation API to remove empty response strings in pending operations.

## December 13, 2022

Fixed

Text extracted flag (text_extraction_disabled) will be deprecated. While customers can still use it in the client library, it will be no-op in our server-side. Meanwhile, a new flag (text_extraction_enabled) will be used to replace the old one. UI will have a new button for this new flag to let customers control the behavior.

Fixed

CreateDocument response will only return document metadata instead of the whole document.

Change

Mark async_enabled field as internal only.

## December 08, 2022

Feature

Partially supports Google AIP-160 syntax (https://google.aip.dev/160) in search query. Search query now supports literals, logical operators, negation operators, comparison operators, and functions.

Fixed

Fix operation status fetching for pending AutoProvision long running operations.

Fixed

Disable text extraction for Google Cloud Storage based ingestion.

Feature

AutoProvision service will return an operation ID for immediate completed operations.

Feature

VPC Service Controls for Document AI Warehouse are publicly supported.

Feature

Enable operation service for Document AI Warehouse v1 service.

## November 17, 2022

Fixed

Fixed the bug that users are unable to preview documents created involving Doc AI processors.

## November 10, 2022

Fixed

Fix plain_text unintended movement in API response messages.

Feature

Enable the validation check for Enum property values by default. Enum values that are not defined in the schema will not be allowed to be set to the corresponding document property Enum fields. The `validationCheckDisabled` flag in `EnumTypeOptions` disables the ENUM Validation.

Feature

Enable text extraction feature.

Fixed

Fix partial document update which could cause loss of raw document name entry.

Fixed

Fix an issue when a user supplies multiple property filters for the same schema in the search query, the service returns error.

## October 17, 2022

Feature

Add a validationCheckDisabled flag in EnumTypeOptions to disable ENUM Validation. The default behavior is unchanged (no validation on ENUM values is enforced).

Feature

Add "LIKE" support in search conditions against text properties. Support search word stemming, semantic search and shuffled ordering of search query strings that run against a text property.

## October 10, 2022

Feature

Launched Document AI Warehouse V1 APIs.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
