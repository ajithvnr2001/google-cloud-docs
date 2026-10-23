---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/transformation-details/
title: Transformation details reference \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:29.349320+00:00
---

# Transformation details reference  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/transformation-details/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Transformation details reference Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the contents of a transformation details table and provides example queries that you can run on it.

When you [de-identify data in storage](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-storage-console "De-identify sensitive data stored in Cloud Storage using the Google Cloud console"), you can configure the inspection job to provide details about each transformation that it makes. Sensitive Data Protection writes these details in a BigQuery table that you specify. In this document, that table is called a _transformation details table_.

## Contents of a transformation details table

This section lists and describes the contents of the transformation details table.

### resource_name

The name of the inspection job that completed the transformation.

### container_name

The file that contains the data that was transformed.

### transformation

Details about the transformation. This field contains the following properties:

type
    

The [transformation method](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference "Transformation reference") that Sensitive Data Protection applied to the finding. The following are some of the possible values:

  * `TRANSFORMATION_TYPE_UNSPECIFIED`
  * [`RECORD_SUPPRESSION`](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#record_suppressions "Record suppressions")
  * [`REPLACE_VALUE`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#replacevalueconfig "API reference for ReplaceValueConfig")
  * [`REPLACE_DICTIONARY`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#replacedictionaryconfig "API reference for ReplaceDictionaryConfig")
  * [`REDACT`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#redactconfig "API reference for RedactConfig")
  * [`CHARACTER_MASK`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#charactermaskconfig "API reference for CharacterMaskConfig")
  * [`CRYPTO_REPLACE_FFX_FPE`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig "API reference for CryptoReplaceFfxFpeConfig")
  * [`FIXED_SIZE_BUCKETING`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#fixedsizebucketingconfig "API reference for FixedSizeBucketingConfig")
  * [`BUCKETING`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#bucketingconfig "API reference for BucketingConfig")
  * [`REPLACE_WITH_INFO_TYPE`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#replacewithinfotypeconfig "API reference for ReplaceWithInfoTypeConfig")
  * [`TIME_PART`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#timepartconfig "API reference for TimePartConfig")
  * [`CRYPTO_HASH`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptohashconfig "API reference for CryptoHashConfig")
  * [`DATE_SHIFT`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#dateshiftconfig "API reference for DateShiftConfig")
  * [`CRYPTO_DETERMINISTIC_CONFIG`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptodeterministicconfig "API reference for CryptoDeterministicConfig")
  * [`REDACT_IMAGE`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ImageRedactionConfig "API reference for ImageTransformation")


description
    

A string representation of the transformation. The value is the output of a `toString()` call on the [`PrimitiveTransformation`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#primitivetransformation "API reference for PrimitiveTransformation") protocol buffer message for all types of transformations, except for a [`RecordSuppression`](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#record_suppressions "Record suppressions"). If the transformation method is a record suppression, this field is empty.

condition
    

A string representation of the [`RecordCondition`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#recordcondition "API reference for RecordCondition") for the transformation. This field is set only if a record condition was used to determine whether Sensitive Data Protection must apply the transformation. Examples:

  * `(age_field <= 18)`
  * `(zip_field exists)`
  * `(zip_field == 01234) && (age_field <= 18) && (city_field exists)`


infoType
    

Details about the type of information detected in the finding. This field contains the following properties:

name
    Name of the [built-in](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference "InfoType detector reference") or [custom](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes "Creating custom infoType detectors") `infoType`.
version
    Version of the `infoType`.

### status_details

Details about the status of the transformation. If the transformation was unsuccessful, this field specifies what caused the failure. This field contains the following properties:

result_status_type
    

A code representing the status of the transformation attempt. The following are the possible values:

  * `STATE_TYPE_UNSPECIFIED`: Sensitive Data Protection couldn't determine the status of the transformation.
  * `INVALID_TRANSFORM`: Sensitive Data Protection couldn't transform the finding.
  * `METADATA_UNRETRIEVABLE`: there's a finding in the custom metadata of a file. While writing the transformed file, Sensitive Data Protection couldn't retrieve the metadata.
  * `SUCCESS`: the transformation was successful.


details
    

Additional status details. This field follows the specifications defined in [`Status`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rpc/google.rpc#status "RPC API reference for Status"). This field contains the following properties:

code
    The error code.
message
    The error message.
details
    A list of messages that contain the error details.

### transformed_bytes

The number of bytes that Sensitive Data Protection transformed. If the transformation was unsuccessful or if there was no content to transform, the value is `0`.

### transformation_location

Details about the location of the transformation.

The following is a JSON example of a transformation location, where Sensitive Data Protection performed an [infoType transformation](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#infotype_transformations "InfoType transformations"):
    
    
    {
        "finding_id": "2022-05-23T23:51:29.775337Z831678185946560283",
        "record_transformation": null,
        "container_type": "TRANSFORM_BODY"
    }
    

The following is a JSON example of a transformation location, where Sensitive Data Protection performed a [record transformation](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#record_transformations "Record transformations"):
    
    
    {
        "finding_id": null,
        "record_transformation": {
          "field_id": {
            "name": " \"Name\""
          },
          "container_timestamp": {
            "timestamp": null,
            "seconds": "1654796423",
            "nanos": "763000000"
          },
          "container_version": "1654796423733485"
        },
        "container_type": "TRANSFORM_TABLE"
      }
    }
    

As the examples show, Sensitive Data Protection populates either `finding_id` or `record_transformation`, depending on the type of transformation it performed. The two fields are mutually exclusive.

finding_id
    This field is set if Sensitive Data Protection performed an infotype transformation. Each finding ID correlates to an entry in the _findings output table_. The findings output table contains all of the findings that Sensitive Data Protection detected during inspection. This table is created only if you configured your inspection job to save findings to BigQuery.
record_transformation
    

This field is set if Sensitive Data Protection performed a record transformation on tabular data. This field contains the following properties:

field_id
    The table column that contains the finding.
container_timestamp
    Modification timestamp of the file.
container_version
    [Generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number "Generation and metageneration numbers") of the file that contains the finding.
container_type
    

Information about the functionality of the data that contains the finding. The following are the possible values:

  * `TRANSFORM_UNKNOWN_CONTAINER`: Sensitive Data Protection couldn't determine the type of the data that contains the finding.
  * `TRANSFORM_BODY`: Sensitive Data Protection detected the finding in the body of a file.
  * `TRANSFORM_METADATA`: Sensitive Data Protection detected the finding in the metadata of a file.
  * `TRANSFORM_TABLE`: Sensitive Data Protection detected the finding in table.



## Example queries

The following are example queries that you can run on the transformation details table. For information about how to query a BigQuery table, see [Running interactive queries](https://docs.cloud.google.com/bigquery/docs/running-queries#queries "Running interactive queries").

### Select all failed transformations
    
    
    SELECT *
        FROM `PROJECT_ID.DATASET_ID.TABLE_ID`
        WHERE status_details.result_status_type != "SUCCESS";
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the transformation details table.
  * `DATASET_ID`: the ID of the BigQuery dataset that contains the transformation details table.
  * `TABLE_ID`: the ID of the transformation details table.



### Count the number of files that have transformation failures
    
    
    SELECT COUNT(DISTINCT(container_name))
        FROM `PROJECT_ID.DATASET_ID.TABLE_ID`
        WHERE status_details.result_status_type != "SUCCESS";
    

### Select all transformations that used character masking
    
    
    SELECT resource_name, container_name, info_type.name
        FROM `PROJECT_ID.DATASET_ID.TABLE_ID`,
        UNNEST(transformation) AS tr
        WHERE tr.type LIKE "CHARACTER_MASK";
    

## What's next

  * Learn more about the [process of de-identifying data in storage](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-deidentify-storage "De-identification of sensitive data in storage").
  * Learn how to [de-identify data in storage using the Google Cloud console](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-storage-console "De-identify sensitive data stored in Cloud Storage using the Google Cloud console").
  * Learn how to [de-identify sensitive data stored in Cloud Storage using the DLP API](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-storage).
  * Work through the [Creating a De-identified Copy of Data in Cloud Storage](https://www.cloudskillsboost.google/focuses/47127?parent=catalog) codelab.
  * Learn more about [de-identification transformations](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference "Transformation reference").



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
