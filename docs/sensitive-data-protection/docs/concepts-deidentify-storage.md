---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-deidentify-storage/
title: De-identification of sensitive Cloud Storage data \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:23.155695+00:00
---

# De-identification of sensitive Cloud Storage data  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-deidentify-storage/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  De-identification of sensitive Cloud Storage data Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Sensitive Data Protection can create de-identified copies of data stored in Cloud Storage. It also lists the limitations of this operation and the points that you should consider before you start.

For information about how to use Sensitive Data Protection to create de-identified copies of your Cloud Storage data, see the following:

  * [Create de-identified copies of data stored in Cloud Storage using the Google Cloud console](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-storage-console)
  * [Create de-identified copies of data stored in Cloud Storage using the API](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-storage)



## About de-identification

_De-identification_ is the process of removing identifying information from data. Its goal is to enable the use and sharing of personal information—such as health, financial, or demographic information—while meeting privacy requirements. For more information about de-identification, see [De-identifying sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data "De-identifying sensitive data").

For more in-depth information about de-identification transformations in Sensitive Data Protection, see [Transformation reference](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference "Transformation reference"). For more information about how Sensitive Data Protection redacts sensitive data from images, see [Image inspection and redaction](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-image-redaction "Image inspection and redaction").

## When to use storage de-identification

The following are some common use cases:

  * **Generate anonymized datasets for non-production environments** : Create de-identified copies of production files stored in Cloud Storage before staging data into development, testing, or training environments.
  * **Share sanitized file repositories with third parties** : Obfuscate sensitive fields in bulk documents and unstructured files while preserving the original folder hierarchy for external business partners or auditors.
  * **Automate privacy pipelines for ingested documents** : Transform sensitive data across newly uploaded files into a designated output bucket without altering source files or disrupting upstream pipelines.
  * **Enforce data residency and compartmentalization** : Store de-identified mirror copies of sensitive assets in separate Cloud Storage buckets with distinct Identity and Access Management access controls.



## De-identification process

This section describes the de-identification process in Sensitive Data Protection for content in Cloud Storage.

To use this feature, you [create an inspection job](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage "Inspecting storage and databases for sensitive data") ([`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob "Documentation for the DlpJob object")) that's configured to make de-identified copies of the Cloud Storage files. Sensitive Data Protection scans the files in the specified location, inspecting them according to your configuration. As it inspects each file, Sensitive Data Protection de-identifies any data that matches your criteria for sensitive data, and then writes the content to a new file. The new file always has the same filename as the original file. It stores this new file in an output directory that you specify. If a file is included in your scan, but no data matches your de-identification criteria, and there are no errors in its processing, then the file is copied, unaltered, to the output directory.

The output directory that you set must be in a Cloud Storage bucket that's different from the bucket containing your input files. In your output directory, Sensitive Data Protection creates a file structure that mirrors the file structure of the input directory.

For example, suppose you set the following input and output directories:

  * Input directory: `gs://input-bucket/folder1/folder1a`
  * Output directory: `gs://output-bucket/output-directory`



During de-identification, Sensitive Data Protection stores the de-identified files in `gs://output-bucket/output-directory/folder1/folder1a`.

If a file exists in the output directory with the same filename as a de-identified file, that file is overwritten. If you don't want existing files to be overwritten, change the output directory before running this operation. Alternatively, consider [enabling object versioning on the output bucket](https://docs.cloud.google.com/storage/docs/using-object-versioning "Use object versioning").

File-level access control lists (ACLs) for the original files are copied to the new files, regardless of whether sensitive data was found and de-identified. However, if the output bucket is configured only for uniform bucket-level permissions, and not fine-grained (object-level) permissions, then the ACLs aren't copied to the de-identified files.

The following diagram shows the de-identification process for four files stored in a Cloud Storage bucket. Each file is copied regardless of whether Sensitive Data Protection detects any sensitive data. Each copied file is named the same as the original.

[ ![De-identification of files stored in Cloud Storage.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/deidentify-storage.svg)](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/deidentify-storage.svg) De-identification of files stored in Cloud Storage (click to enlarge).

## Pricing

For pricing information, see [Inspection and transformation of data in storage](https://cloud.google.com/sensitive-data-protection/pricing#inspection_and_transformation_pricing "Inspection and transformation pricing").

## Supported file types

Sensitive Data Protection can de-identify the following [file type groups](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FileType "API documentation for the FileType object"):

  * CSV
  * Image
  * Text
  * TSV



## Default de-identification behavior

If you want to define how Sensitive Data Protection transforms the findings, you can provide [de-identify templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid "Creating de-identification templates") for the following types of files:

  * Unstructured files, like text files with freeform text
  * Structured files, like CSV files
  * Images



If you don't provide any de-identify template, Sensitive Data Protection transforms the findings as follows:

  * In unstructured and structured files, Sensitive Data Protection replaces all findings with their corresponding infoType, as described in [InfoType replacement](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference#infotype-replacement "InfoType replacement").
  * In images, Sensitive Data Protection covers all findings with a black box.



## Limitations and considerations

Consider the following points before creating de-identified copies of Cloud Storage data.

### Disk space

This operation only supports content stored in Cloud Storage.

This operation makes a copy of each file as Sensitive Data Protection inspects it. It does not modify or remove the original content. The copied data will take up roughly the same amount of additional disk space as the original data.

### Write access to the storage

Because Sensitive Data Protection creates a copy of the original files, the service agent of your project must have write access on the Cloud Storage output bucket.

### Sampling and setting finding limits

This operation doesn't support sampling. Specifically, you can't limit how much of each file Sensitive Data Protection scans and de-identifies. That is, if you're using the Cloud Data Loss Prevention API, you can't use `bytesLimitPerFile` and `bytesLimitPerFilePercent` in the [`CloudStorageOptions`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#CloudStorageOptions "Documentation for the CloudStorageOptions object") object of your [`DlpJob`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob "Documentation for the DlpJob object").

Also, you can't control the maximum number of findings to be returned. If you're using the DLP API, you can't set a [`FindingLimits`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FindingLimits "Documentation for the FindingLimits object") object in your `DlpJob`.

### Requirement to inspect data

When running your inspection job, Sensitive Data Protection first inspects the data, according to your inspection configuration, before it performs de-identification. It can't skip the inspection process.

### Requirement to use file extensions

Sensitive Data Protection relies on file extensions to identify the file types of the files in your input directory. It might not de-identify files that don't have file extensions, even if those files are of supported types.

### Skipped files

When de-identifying files in storage, Sensitive Data Protection skips the following files:

  * Files that exceed 60,000 KB. If you have large files that exceed this limit, consider breaking them into smaller chunks.
  * File types that aren't listed in Supported file types on this page.
  * File types that you purposely excluded from the de-identification configuration. If you're using the DLP API, the file types that you excluded from the `file_types_to_transform` field of the [`Deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Action#Deidentify "Documentation for the Deidentify action") action of your `DlpJob` are skipped.
  * Files that encountered transformation errors.



### Order of output rows in de-identified tables

There is no guarantee that the order of rows in a de-identified table matches the order of rows in the original table. If you want to compare the original table to the de-identified table, you can't rely on the row number to identify the corresponding rows. If you intend to compare rows of the tables, you must use a unique identifier to identify each record.

**Note:** The inspection findings summary shows the row number of each finding. The referenced rows belong to the original table, not the de-identified table.

### Transient keys

If you choose a [cryptographic method](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization#supported-methods "Supported cryptographic methods") as your transformation method, you must first [create a wrapped key using Cloud Key Management Service](https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key "Create a wrapped key"). Then, provide that key in your de-identification template. Transient (raw) keys aren't supported.

## What's next

  * Learn how to [de-identify sensitive data stored in Cloud Storage using the DLP API](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-storage "De-identify sensitive data stored in Cloud Storage").
  * Learn how to [de-identify sensitive data stored in Cloud Storage using the Google Cloud console](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-storage-console "De-identify sensitive data stored in Cloud Storage using the Google Cloud console").
  * Work through the [Creating a De-identified Copy of Data in Cloud Storage](https://www.cloudskillsboost.google/focuses/47127?parent=catalog) codelab.
  * Learn how to [inspect storage for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage "Inspecting storage and databases for sensitive data").



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
