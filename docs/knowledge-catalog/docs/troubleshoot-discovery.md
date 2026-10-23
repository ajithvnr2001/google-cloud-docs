---
url: https://docs.cloud.google.com/knowledge-catalog/docs/troubleshoot-discovery/
title: Troubleshoot Knowledge Catalog data discovery issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:04.099438+00:00
---

# Troubleshoot Knowledge Catalog data discovery issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/troubleshoot-discovery/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Troubleshoot Knowledge Catalog data discovery issues Stay organized with collections  Save and categorize content based on your preferences. 

This guide helps you troubleshoot and resolve common issues with Knowledge Catalog data discovery scans (also called standalone discovery), including table publishing failures and schema incompatibility errors.

## BigQuery table publishing failure (FAILED_BIGQUERY_TABLE_PUBLISH)

When a discovery scan executes, it can fail to publish tables to BigQuery. In this case, the scan logs a `FAILED_BIGQUERY_TABLE_PUBLISH` action in Cloud Logging.

This issue occurs because of the following conditions:

  * **Insufficient IAM permissions** : The Knowledge Catalog service account or the BigQuery connection service account lacks the required roles to delegate connections, access Cloud Storage, or write to the destination dataset.
  * **BigQuery connection or dataset mismatch** : The specified connection ID is invalid, or the connection and destination dataset are located in different regions.
  * **Table configuration errors** : Table creation or modification applies incorrect or unsupported settings.



To resolve this issue, perform the following checks:

  * **Verify service account roles** : Confirm that the Knowledge Catalog service account `service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com` has the Dataplex Discovery BigLake Publishing Service Agent (`roles/dataplex.discoveryBigLakePublishingServiceAgent`) role.
  * **Verify connection permissions** : If you create BigLake tables, verify that the BigQuery connection service account has read access to the Cloud Storage bucket (using `roles/storage.objectViewer` or `roles/dataplex.discoveryServiceAgent`).
  * **Check connection and dataset location** : Ensure that the BigQuery connection and the BigQuery dataset exist in the same region, and that they are compatible with the location of the Cloud Storage bucket.
  * **Inspect logs for details** : Explore your DataScan job logs in Cloud Logging. If the error contains `BigQuery: Permission denied`, check the service account permissions. If it contains `TABLE_CONFIG`, verify that the data files conform to BigQuery requirements.



## BigLake table creation fails for large Cloud Storage buckets

When a discovery scan processes Cloud Storage buckets with a large volume of data or large individual files (for example, Avro files larger than 30 MB), the scan can successfully create the BigQuery dataset but fail to publish the BigLake tables.

When this occurs, you might observe the following errors in Cloud Logging:

  * `FAILED_BIGQUERY_TABLE_PUBLISH`
  * `com.google.cloud.bigquery.BigQueryException: Read timed out`



This issue is a known scalability limitation. If you require immediate table provisioning, configure your discovery scan to include a smaller, filtered subset of your bucket data.

## Cloud Storage folder schema mismatches

A data discovery scan fails to register external tables, or it doesn't detect files in certain folders.

This issue occurs if your Cloud Storage folders contain files with incompatible schemas or different formats. The discovery scan groups files into a single table only if they are in the same folder and have a compatible schema.

When a data discovery scan analyzes a Cloud Storage path, it expects the files within a folder and the partition structure across folders to be consistent. The scan flags an action if it detects any of the following:

  * **Invalid data format (`INVALID_DATA_FORMAT`)**: Inconsistent data formats are found within the same folder or across partitions (for example, mixing `.csv` and `.parquet` files in the same directory).
  * **Invalid partition definition (`INVALID_PARTITION_DEFINITION`)**: Partition keys are inconsistent or missing. For example, using `Year=2023/Mon=Jan` in one path and `Year=2023/Dept=Sales` in another.
  * **Incompatible data schema (`INCOMPATIBLE_DATA_SCHEMA`)**: Inconsistent or incompatible schemas are detected across files within the same folder or table.



For strongly typed formats like Avro and Parquet, schema mismatches occur due to:

  * **Incompatible data types** : A column has a `string` type in one file and an `int` or `boolean` type in another.
  * **Missing default values** : New fields are added or deleted in newer files without specifying default values in the schema definition, preventing correct schema evolution.
  * **Corrupt file format** : One or more files are malformed or corrupt, causing the scan to fail to read and extract the schema.



To resolve this issue, check your file structure and schema definitions:

  * **Organize files by schema and format** : Verify that all files in a single folder share the same format and schema structure. Move files with different columns, primitive types, or formats to separate folders or prefixes so they can be registered as separate tables.
  * **Use consistent partition definitions** : Ensure that partition keys and structures are consistent across all partition folders (for example, consistently using `Year=YYYY/Month=MM/`).
  * **Follow schema evolution rules** : When you update schemas (such as adding or removing fields from Avro files), always define default values so the discovery service can merge the schema variants successfully.
  * **Identify corrupt files** : Check the scan output or logs to identify if a particular file fails to decode. Temporarily move files to find if a specific file causes the scan to fail.



## Discovered tables don't update with schema changes

After you modify files in Cloud Storage or run a new scan, the updated schema is not reflected in the published BigQuery tables.

This issue occurs if the published table has the `metadata-managed-mode` label set to `user_managed`. By default, discovery publishes tables as `discovery_managed`. If you or another user manually edit the table schema properties, you must change the label to `user_managed` to block automated updates.

To resolve this issue, check the table labels in BigQuery:

  1. In the Google Cloud console, go to the **BigQuery** page.
  2. In the **Explorer** pane, expand your project, select the dataset, and click the affected table.
  3. Click the **Details** tab.
  4. In the **Labels** section, check the value of the `metadata-managed-mode` key.
  5. If you want the discovery scan to resume managing and updating the schema, click **Edit details** , and change the value to `discovery_managed`.

**Note:** When the label is updated to `discovery_managed`, the discovery scan overwrites any manually applied schema changes during its next run.



## Get support

If you need help resolving an issue that isn't addressed in this document, contact [Cloud Customer Care](https://docs.cloud.google.com/support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
