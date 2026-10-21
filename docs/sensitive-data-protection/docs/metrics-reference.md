---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference/
title: Metrics reference \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:07.320111+00:00
---

# Metrics reference  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Metrics reference Stay organized with collections  Save and categorize content based on your preferences. 

This page lists and describes all metrics that are gathered in data profiles.

There are three types of data profiles—[project data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#project-data-profile), [table data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#table-data-profile), and [column data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/metrics-reference#column-data-profile).

## Project data profiles

Each project data profile has the following fields. The values for these fields are aggregated based on the resources profiled within the project.

### Insights

Project data profiles provide the following insights:

Data risk
    Level of risk associated with the data at its current state. For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).
Sensitivity
    Score indicating the sensitivity level for this project. For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

### Metadata

Project data profiles provide the following metadata:

Last profile generated
    Date and time the profile was last generated.
Project ID
    ID of the project that was profiled.
Resource name
    Fully qualified name of the data profile.
Status
    Icon that indicates the status of the profiling operation.

## Table data profiles

Each table data profile has the following fields:

### Insights

Table data profiles provide the following insights:

Data risk
    Level of risk associated with the data at its current state. For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).
Sensitivity
    Score indicating the sensitivity level for this table. For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

### Metadata

Table data profiles provide the following metadata:

Database
    The database containing the table that was profiled. This field applies only to [Cloud SQL discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder-cloud-sql).
Dataset ID
    ID of the dataset that contains this table.
Encryption
    Whether encryption for this table is managed by Google or by your organization.
Expiration time
    

Optional. The time when this table expires.

**Note:** For information about a known issue related to this field, see [Incorrect expiration timestamp for tables that don't expire](https://docs.cloud.google.com/sensitive-data-protection/docs/known-issues#incorrect-timestamp-bq).
Failed column count
    

The number of columns skipped in this table because of an error.

Inspect config snapshot
    

Snapshot of the [inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#inspection-template) that was used when the profile was generated. For more information, see [Data profile snapshots](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-profile-snapshots).

Instance
    

The instance containing the table that was profiled. This field applies only to [Cloud SQL discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder-cloud-sql).

Last profile generated
    

Date and time the profile was last generated.

Latest update in BigQuery
    

Date and time this table was last modified.

Project ID
    

ID of the project that contains this table.

Public
    

Whether this table is available to all users or restricted to certain users.

**Note:** For information about a known issue related to this field, see [Resource visibility](https://docs.cloud.google.com/sensitive-data-protection/docs/known-issues#dp-resource-visibility).
Resource labels
    

[Labels](https://docs.cloud.google.com/bigquery/docs/labels-intro) that the table had at the time the profile was generated.

Resource tags
    

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) that the table had at the time the profile was generated.

Resource name
    

Fully qualified name of the data profile.

Row count
    

Number of rows in this table when the profile was generated.

Scanned column count
    

The number of columns profiled in this table.

Service account
    

Number of service accounts with IAM permissions to access this table.

Status
    

Indication of whether the profile succeeded in generation.

Table ID
    

ID of this table.

Table creation time
    

Date and time the table was created.

Table size
    

The size of this table when the profile was generated.

Type
    

The [type of discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#discovery-type) performed.

## Column data profiles

Each column data profile has the following fields:

### Insights

Column data profiles provide the following insights:

Data risk
    Level of risk associated with the data at its current state. For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).
Sensitivity
    Score indicating the sensitivity level for this column. For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).
Predicted infoType
    

If a single [built-in](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) or [custom](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes#custom) infoType clearly predominates over others in the column, Sensitive Data Protection sets this field to that infoType. Otherwise, this field has no value.

To view a list of all infoTypes detected in the column, refer to the **Other infoTypes** field.

Sensitive Data Protection scans for only the infoTypes that you specified in the [inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#inspection-template). Thus, only those infoTypes can appear in the **Predicted infoType** field. For example, if the column has email addresses, but you didn't include the `EMAIL_ADDRESS` infoType detector in your inspection template, then this field doesn't contain `EMAIL_ADDRESS`.

If the column data predominantly matches several closely related infoTypes that belong to the same general category, Sensitive Data Protection sets this field to the more general infoType. For example, if the column predominantly has a mix of `PASSPORT`, `AUSTRALIA_PASSPORT`, and `CANADA_PASSPORT` infoTypes, the **Predicted infoType** field is set to `PASSPORT`. The **Other infoTypes** field shows the more specific infoTypes and their estimated prevalence.

Other infoTypes
    

InfoTypes detected in the column that don't have a strong enough signal to be considered that column's _predicted infoType_. In this document, see Predicted infoType.

For data profiles generated after October 13, 2022, each infoType listed in this field has an _estimated prevalence_. The estimated prevalence is an approximate percentage of non-null rows in which the infoType was detected.

For example, suppose you have a column that has the following metrics:

  * **Predicted infoType:** `FDA_CODE`
  * **Other infoTypes:** `PERSON_NAME (2%)`, `STREET_ADDRESS (1%)`



In this example, there is a strong indication that the column contains FDA codes. Sensitive Data Protection also determined that approximately 2% of non-null rows in the column might contain person names and 1% might contain street addresses.

Sensitive Data Protection scans for only the infoTypes that you specified in the [inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#inspection-template). Thus, only those infoTypes can appear in the **Other infoTypes** field. For example, if the column has email addresses, but you didn't include the `EMAIL_ADDRESS` infoType detector in your inspection template, then this field doesn't contain `EMAIL_ADDRESS`.

Estimated null proportion
    

Approximate proportion of null values in this column, categorized as high, medium, low, or very low. This value is high if a large proportion of entries in this column is null.

Estimated uniqueness
    

An estimate of how much of the data in this column is unique, categorized as high, medium, or low. A high uniqueness level suggests that the column contains distinct values. A high presence of unique values can indicate that the column contains identifiers.

A low uniqueness level suggests that the column contains many common values such as enums or boolean values.

If Sensitive Data Protection determines that there aren't enough rows in the table for it to calculate this metric, this value is blank.

Free text score
    

The probability that this column contains freeform text. A value close to 1 indicates the column is likely to contain freeform or natural-language text. Possible values range from 0 through 1.

A high free text score can increase a column's [data risk and sensitivity levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

### Metadata

Column data profiles provide the following metadata:

Database
    The database containing the table column that was profiled. This field applies only to [Cloud SQL discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder-cloud-sql).
Data type
    The data type of the contents of this column.
Dataset ID
    ID of the dataset that contains this table column.
Field ID
    Name of the column.
Instance
    The instance containing the table column that was profiled. This field applies only to [Cloud SQL discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/profile-org-folder-cloud-sql).
Instance location
    Location of the instance containing the table column that was profiled. This field applies only to Cloud SQL discovery.
Last profile generated
    Date and time the profile was last generated.
Policy tags
    Indicates if a policy tag is applied to the column. For information on best practices for using policy tags, see [Using policy tags in BigQuery](https://docs.cloud.google.com/bigquery/docs/best-practices-policy-tags).
Project ID
    ID of the project that contains this table column.
Resource name
    Fully qualified name of the data profile.
Status
    Icon that indicates the status of the profiling operation.
Table ID
    ID of the table that contains this column.

## File store data profiles

Sensitive Data Protection uses the term _file store_ to refer to a file storage bucket or container.

Each file store data profile has the following fields.

### Insights

File store data profiles provide the following insights:

Data risk
    Level of risk associated with the data at its current state. For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).
File clusters
    Provides a summary for each file cluster that was detected when this file store was profiled. For more information about each summary, see File cluster summaries on this page.
Sensitivity
    Score indicating the sensitivity level for this file store. For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

### Metadata

File store data profiles provide the following metadata:

Data storage locations
    

If you profiled a [dual-region Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/locations#location-dr), then this field lists the two regions.

If you profiled a file store from another cloud provider, then this value is the region where the cloud provider stores the file store.

Encryption
    

Whether encryption for this file store is managed by Google or by your organization.

File store type
    

The source of the of data that was profiled—Cloud Storage, Amazon S3, or Azure Blob Storage.

File store path
    

The name of the file store.

Inspect config snapshot
    

Snapshot of the [inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#inspection-template) that was used when the profile was generated. For more information, see [Data profile snapshots](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-profile-snapshots).

Location type
    

Type of location where the file store is stored: `region`, `dual-region`, or `multi-region`.

Profile first created
    

Date and time the profile was created for the first time.

Profile last generated
    

Date and time the profile was last generated.

Parent ID
    

The resource that owns the data that was profiled.

  * If the data profile is for a Google Cloud resource, then this is the ID of the project that contains the data.
  * If the data profile is for an Amazon S3 bucket, then this is the ID of the AWS account that contains the bucket.
  * If the data profile is for an Azure Blob Storage container, then this is the ID of the Azure subscription that contains the container.


Public
    

Whether this file store is available to all users or restricted to certain users.

Resource labels
    

Labels that the file store had at the time the profile was generated.

Resource tags
    

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) that the file store had at the time the profile was generated.

Resource location
    

Region or multi-region that contains the file store.

If you profiled a [dual-region Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/locations#location-dr), then this value depends on whether the bucket is stored in a predefined dual region:

  * For [predefined dual regions](https://docs.cloud.google.com/storage/docs/locations#predefined), Sensitive Data Protection sets this value to the predefined dual-region name.
  * For standard dual regions, Sensitive Data Protection sets this value to the multi-region that contains the dual regions. For information about how regions map to multi-regions, see [Dual regions](https://docs.cloud.google.com/storage/docs/locations#location-dr).


Resource name
    

Fully qualified name of the data profile.

Status
    

Indication of whether the profile succeeded in generation.

## File cluster summaries

When a file store data profile is generated, the files are grouped into file clusters. Sensitive Data Protection provides a summary for each file cluster.

Each file cluster summary has the following fields:

Data risk
    Level of risk associated with the data in this file cluster. For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).
Errors
    Any errors detected when the file store data profile was generated.
File extensions scanned
    List of file types detected and scanned to generate the file store data profile.
File extensions seen
    List of file types detected but not necessarily scanned.
InfoTypes
    List of [built-in](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) and [custom](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes#custom) infoTypes that were detected in this file cluster.
Sensitivity
    Score indicating the sensitivity level for this file cluster. For more information, see [Sensitivity and data risk levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).
Type
    

Indicates the category of files in this cluster. For more information about all supported file clusters, see [Supported file clusters in discovery operations](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types#file_clusters).

**Note:** If Sensitive Data Protection scans a file within an archive file, the value of this field is `ARCHIVE_FILE_EXTENSION/SCANNED_FILE_EXTENSION`—for example, `zip/csv`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
