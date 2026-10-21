---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/known-issues/
title: Known issues \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:41:03.032190+00:00
---

# Known issues  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/known-issues/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Resources ](https://docs.cloud.google.com/sensitive-data-protection/docs/resources)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

This page lists known issues with Sensitive Data Protection, along with ways you can avoid or recover from the following issues.

## Storing results to BigQuery

When a job or discovery scan is storing results to BigQuery, an `Already exists` error appears in the logs. The error does not indicate that there is a problem; your results will be stored as expected.

## BigQuery scanning

This section describes issues you might encounter when [inspecting](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage) or [profiling](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) BigQuery data.

### Issues common to inspection and profiling operations

The following issues are applicable to both BigQuery inspection and profiling operations.

#### Rows with row-level security can't be scanned

[Row-level security policies](https://docs.cloud.google.com/bigquery/docs/row-level-security-intro) can prevent Sensitive Data Protection from inspecting and profiling the protected BigQuery tables. If you have row-level security policies applied to your BigQuery tables, we recommend that you [set a TRUE filter](https://docs.cloud.google.com/bigquery/docs/using-row-level-security-with-features#the_true_filter) and include the service agent in the grantee list:

  * If you're [profiling data at the organization or folder level](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder), include the [service agent of the container project](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#service-agent-container) in the grantee list.
  * If you're [profiling data at the project level](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project) or running an [inspection job](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage) on a table, include the [service agent](https://docs.cloud.google.com/sensitive-data-protection/docs/iam-permissions#service_account) of the project in the grantee list.



#### Duplicate rows

When writing data to a BigQuery table, Sensitive Data Protection might write duplicate rows.

#### Recently streamed data

Sensitive Data Protection doesn't scan recently streamed data (formerly known as _streaming buffer_). For more information, see [Streaming data availability](https://docs.cloud.google.com/bigquery/streaming-data-into-bigquery#dataavailability) in the BigQuery documentation.

### BigQuery inspection issues

The following issues are only applicable to inspection operations on BigQuery data. They don't affect data profiles.

#### Exported findings do not have values for the row_number field

When you configure Sensitive Data Protection to save findings to BigQuery, the `location.content_locations.record_location.record_key.big_query_key.row_number` field in the generated BigQuery table is inferred at the time the input table is scanned. Its value is nondeterministic, can't be queried, and can be null for inspection jobs.

If you need to identify specific rows where findings are present, specify `inspectJob.storageConfig.bigQueryOptions.identifyingFields` at job creation time.

Identifying fields can be found in the generated BigQuery table, in the `location.content_locations.record_location.record_key.id_values` field.

#### Limiting scans to new BigQuery content

If you're [limiting scans to only new content](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#limit_scans_to_only_new_content), and you use the [BigQuery Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api) to populate the input table, Sensitive Data Protection might skip scanning some rows.

To mitigate this issue, in your [inspection job](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig), make sure the `timestampField` of the [`TimespanConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#timespanconfig) object is a commit timestamp that BigQuery auto-generates. However, there's still no guarantee that no rows are skipped, because Sensitive Data Protection doesn't read from recently streamed data.

If you want to auto-generate commit timestamps for a column, and you use the [legacy streaming API](https://docs.cloud.google.com/bigquery/streaming-data-into-bigquery) to populate your input table, do the following:

  1. In the input table's schema, make sure that the timestamp column is of type `TIMESTAMP`.

**Example schema**

The following example defines the `commit_time_stamp` field and sets its type to `TIMESTAMP`:
         
         ...
         {
          "name": "commit_time_stamp",
          "type": "TIMESTAMP"
         }
         ...
         

  2. In the `rows[].json` field of the [`tabledata.insertAll`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tabledata/insertAll) method, make sure that the values in the timestamp column are set to `AUTO`.

**Example JSON**

The following example sets the value of the `commit_time_stamp` field to `AUTO`:
         
         {
           ...
           "commit_time_stamp": "AUTO",
           ...
         }
         




#### Limiting scans by setting a maximum percentage or rows

When you set a sampling limit based on a percentage of the total number of table rows ([`rowsLimitPercent`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#BigQueryOptions.FIELDS.rows_limit_percent)), Sensitive Data Protection can inspect more rows than expected. If you need to put a hard limit on the number of rows to scan, we recommend setting a maximum number of rows ([`rowsLimit`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#BigQueryOptions.FIELDS.rows_limit)) instead.

### BigQuery profiling issues

The following issues are only applicable to profiling operations on BigQuery data. For more information, see [Data profiles for BigQuery data](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

#### Organizations or projects with more than 500 million tables

Sensitive Data Protection returns an error if you attempt to profile an organization or project that has more than 500 million tables. If you encounter this error, follow the instructions in the error message.

If your organization's table count has more than 500 million tables, and you have a project with a lower table count, try to do a project-level scan instead.

For information about table and column limits, see [Data profiling limits](https://docs.cloud.google.com/sensitive-data-protection/limits#data-profiling-limits).

#### Inspection templates

The [inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates) must be in the same region as the data to be profiled. If you have data in multiple regions, use multiple inspection templates—one for each region where you have data. You can also use an inspection template that is stored in the `global` region. If you include a template in the `global` region, Sensitive Data Protection uses it for any data that doesn't have a region-specific template. For more information, see [Data residency considerations](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency).

#### Stored infoTypes

A [stored infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes) (also known as a _stored custom dictionary detector_) that is referenced in your inspection template must be stored in either of the following:

  * The `global` region.
  * The same region as the inspection template.



Otherwise, the profiling operation fails with the error, `Resource not found`.

#### Resource visibility

In a table data profile, the resource visibility classification given to a BigQuery table depends on the visibility of the dataset that contains the table, rather than the visibility of the table. Therefore, if a table's IAM permissions differ from the dataset's IAM permissions, then the resource visibility of the table indicated in the data profile can be incorrect. This issue affects [discovery for BigQuery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#bq-biglake) and [discovery for Vertex AI](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#vertex-ai).

In the Google Cloud console, the resource visibility is indicated in the table data profile's **Public** field. In the Cloud Data Loss Prevention API, the resource visibility is indicated in the [`resourceVisibility`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility) field of the [`TableDataProfile`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles#resource:-tabledataprofile).

#### Incorrect expiration timestamp for tables that don't expire

Between July 2025 and June 2026, some [table data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#table-data-profile) saved to BigQuery contained an incorrect `1970-01-01` timestamp instead of `NULL` in `[expiration_time](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles#TableDataProfile.FIELDS.expiration_time)` for tables that don't expire.

## Cloud Storage scanning

This section describes issues you might encounter when [inspecting](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage) or [de-identifying](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-deidentify-storage) data.

### Inspection of Strict XLSX files is not supported

A file with an `.xlsx` extension can be one of two types. One type is a Strict Office Open XML spreadsheet, which is not supported by Sensitive Data Protection. The other type is a default Microsoft Excel workbook, which is supported.

### Structured files being scanned in binary mode

In certain cases, files that are typically scanned in structured parsing mode might be scanned in binary mode, which doesn't include the enhancements of the structured parsing mode. For more information, see [Scanning structured files in structured parsing mode](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#structured-parsing-mode).

### De-identifying delimited files

When you [de-identify](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-deidentify-storage) a delimited file (for example, a CSV file) with an [inspection job](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage), the output might have additional empty cells in some rows. A workaround to avoid these extra cells is to instead de-identify data using the [`content.deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data) method.

## Discovery for Cloud SQL

### Security Command Center duplicate findings

Cloud SQL data profiling supports [publishing findings to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc).

Prior to April 25, 2024, a bug caused Sensitive Data Protection to occasionally generate duplicate findings for Cloud SQL instances in Security Command Center. These findings were generated with unique finding IDs, but they pertain to the same Cloud SQL instances. The issue has been resolved, but the duplicate findings still exist. You can [mute](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings) the duplicates to hide them on the Security Command Center **Findings** page.

## Discovery for Amazon S3

Findings for Amazon S3 that Sensitive Data Protection sends to Security Command Center might not have information about the affected resource's AWS account ID or display name. This typically happens in the following cases:

  * The [AWS connector](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws) had only been valid for about 24 hours by the time the finding was sent to Security Command Center.
  * The AWS account had only been included in the AWS connector for about 24 hours by the time the finding was sent to Security Command Center.



To resolve this issue, after approximately 24 hours, regenerate the data profiles by [deleting them](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-data-profiles#force-reprofile) or by [setting a profiling schedule](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-amazon-s3#manage-schedules). The full finding details are sent to Security Command Center.

## Intelligent document parsing

This section contains known issues related to document parsing.

### The `DocumentLocation` object isn't populated

The `location.content_locations.document_location.file_offset` field isn't populated for Intelligent Document Parsing scanning mode.

## Detection

The following known issues describe issues with detection, regardless of the operation you're performing—inspection, de-identification, or discovery.

### Dictionary words

Dictionary words containing characters in the [Supplementary Multilingual Plane](https://en.wikipedia.org/wiki/Plane_%28Unicode%29#Supplementary_Multilingual_Plane) of the Unicode standard can yield unexpected findings. Examples of such characters are emojis, scientific symbols, and historical scripts. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
