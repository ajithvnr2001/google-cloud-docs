---
url: https://docs.cloud.google.com/storage/docs/insights/inventory-reports/
title: Inventory reports \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:28.975168+00:00
---

# Inventory reports  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/inventory-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Inventory reports Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage inventory reports help you manage object storage at scale. Inventory reports provide a faster, scheduled alternative to the [`Objects: list`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) API operation. You can use inventory reports to validate the migration of large buckets without performance impact or to check the integrity of objects in a single bucket.

Inventory reports contain metadata about your objects, such as storage class, ETag, and content type. You can use this information to analyze storage costs, audit and validate objects, and help ensure data security and compliance.

You can export inventory reports as comma-separated value (CSV) or Apache Parquet files so you can further analyze your data by using tools such as [BigQuery](https://docs.cloud.google.com/bigquery/docs#docs).

For steps to use inventory reports, see [Create and manage inventory reports](https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports).

## Overview of inventory reports

_Inventory reports_ contain a list of objects and their associated metadata for a given bucket, also known as the source bucket. To generate inventory reports, you must first create an _inventory report configuration_ that defines how often the reports are generated, the metadata fields you want the reports to include, and a bucket to generate and store the reports, also known as the destination bucket.

When you create an inventory report configuration, it automatically gets assigned a universally unique identifier (UUID). This field is non-editable. However, you can edit the following fields of an inventory report configuration:

  * The display name of the inventory report configuration
  * The object metadata fields that are included in the inventory reports
  * The destination bucket that stores the inventory reports
  * The schedule that determines how often inventory reports are generated
  * The file format in which inventory reports are generated (CSV or Apache Parquet)



When you delete an inventory report configuration, new inventory reports are no longer generated for the configuration, but existing inventory reports remain.

**Caution:** Timeliness and completeness of inventory reports delivery might vary. Reports might not generate daily, and some objects might be missing. For a complete and daily analysis, we recommend using the [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets).

## When to use inventory reports

Inventory reports are designed for quick analysis of individual buckets. You can use them to do the following:

  * List all objects within a bucket

  * Validate the success of data transfers

  * Generate audit reports for a particular bucket




## When not to use inventory reports

Manually collating and analyzing inventory reports from many buckets and projects can be challenging, especially for large-scale analysis. For use cases such as organization-wide visibility, security analysis, or cost management, you can use [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets). Storage Insights datasets provide flexibility to configure a custom scope either at the bucket, folder, project, or organization level. Storage Insights datasets also provide additional object insights like operational data, error information, aggregated bucket and project activity data, and custom metadata.

For Storage Insights datasets, data is refreshed daily for metadata views and every 4-6 hours for activity views. You can analyze the data using SQL in BigQuery or natural language questions with Gemini.

Use Storage Insights datasets if your goals are as follows:

  * Cross-organizational data discovery
  * Analysis for cost optimization and lifecycle management
  * Time-series analysis to identify trends
  * Troubleshoot operations
  * Monitor activity occurring on buckets and projects



Storage Insights datasets are an exclusive feature only available through the [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview) subscription.

## Source and destination buckets

The _source bucket_ contains the objects for which you want to generate inventory reports. It also contains the inventory report configuration. You can have up to 100 inventory report configurations in a source bucket.

The _destination bucket_ stores the generated inventory reports. The destination bucket must meet the following requirements:

  * It must be in the same [location](https://docs.cloud.google.com/storage/docs/locations) as the source bucket.
  * It must be in the same project as the source bucket.
  * It can be the same as the source bucket.



When you first create an inventory report configuration, a service agent is automatically created on your behalf. In order to create inventory report configurations and write inventory reports to the destination bucket, both you and your service agent must have required IAM permissions. See required permissions [for yourself](https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports#get_required_roles) and for your [service agent](https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports#grant-permissions-to-service-account).

Inventory reports use the source and destination buckets' names to determine which buckets to use when running jobs. If you delete a source or destination bucket and later create a new bucket with the same name, inventory reports will run jobs using the new bucket.

## Object metadata fields

The following metadata fields can be included in an inventory report. Metadata fields marked as "Required" must be included in the inventory report.

Metadata field | Description | Notes  
---|---|---  
project | The ID of the project where the source bucket resides. | Required  
bucket | The name of the source bucket. | Required  
name | The name of the object. | Required  
location | The [location](https://docs.cloud.google.com/storage/docs/locations) of the source bucket. | Optional  
size | The size of the object. | Optional  
timeCreated | The creation time of the object in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. | Optional  
timeDeleted | The deletion time of the object in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. Returned if and only if this version of the object is no longer a live version, but remains in the bucket as a noncurrent version. | Optional  
updated | The modification time of the object metadata in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. | Optional  
storageClass | The [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of the object. | Optional  
etag | HTTP 1.1 [Entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for the object. | Optional  
retentionExpirationTime | The earliest time that the object can be deleted, which depends on any [retention configuration](https://docs.cloud.google.com/storage/docs/object-lock) set for the object and any [retention policy](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-policy) set for the bucket that contains the object. The value for `retentionExpirationTime` is given in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. | Optional  
crc32c | The CRC32C checksum, as described in [RFC 4960 Appendix B](https://datatracker.ietf.org/doc/html/rfc4960#appendix-B), encoded using [base64](https://datatracker.ietf.org/doc/html/rfc4648#section-4) in big-endian byte order. For more information about the CRC32C checksum, see [Object metadata](https://docs.cloud.google.com/storage/docs/metadata#checksums). | Optional  
md5Hash | The MD5 hash of the data, encoded using [base64](https://datatracker.ietf.org/doc/html/rfc4648#section-4). This field is not present for [composite objects](https://docs.cloud.google.com/storage/docs/composite-objects). For more information about the MD5 hash, see [Object metadata](https://docs.cloud.google.com/storage/docs/metadata#checksums). | Optional  
generation | The content [generation of this object](https://docs.cloud.google.com/storage/docs/metadata#generation-number). Used for object versioning. | Optional  
metageneration | The version of the metadata for this object at this [generation](https://docs.cloud.google.com/storage/docs/metadata#generation-number). Used for preconditions and for detecting changes in metadata. A metageneration number is only meaningful in the context of a particular generation of a particular object. | Optional  
contentType | The [Content-Type](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.1.5) of the object data. If an object is stored without a Content-Type, it is served as application/octet-stream. | Optional  
contentEncoding | The [Content-Encoding](https://datatracker.ietf.org/doc/html/rfc7231#section-3.1.2.2) of the object data. | Optional  
timeStorageClassUpdated | The time at which the object's [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) was last changed. When the object is initially created, it is set to timeCreated. | Optional  
  
For more information about object metadata fields, see [Object metadata](https://docs.cloud.google.com/storage/docs/metadata).

## Inventory report shards

When an inventory report contains more than 1,000,000 objects, one or more shard objects are generated to compose the inventory report. When all the shards of an inventory report have been successfully generated, a manifest file is generated in the same destination bucket as the shards.

### Inventory report manifest file

The presence of a manifest file indicates that all the shards composing an inventory report have been generated. The manifest file also provides the names of the inventory report shard objects.

The manifest file follows the naming convention `REPORT_CONFIG_UUID_TARGET_DATETIME_manifest.json`, where:

  * `REPORT_CONFIG_UUID` is the auto-generated UUID of the inventory report configuration.

  * `TARGET_DATETIME` is the auto-generated UTC date and time at which an inventory report is generated.




An example manifest filename is `fc95c52f-157a-494f-af4a-d4a53a69ba66_2022-11-30T00:00_manifest.json`.

The `manifest.json` file contains the following auto-populated fields:
    
    
    {
      "report_config": REPORT_CONFIG_FIELDS,
      "records_processed": NUMBER_OF_INCLUDED_OBJECTS,
      "snapshot_time": "SNAPSHOT_TIME,
      "target_datetime": "TARGET_DATETIME,
      "shard_count": SHARD_COUNT,
      "report_shards_file_names": [
        SHARD_FILE_NAME
        ...]
    }

Where:

  * `REPORT_CONFIG_FIELDS` includes fields contained within the [ReportConfig resource](https://docs.cloud.google.com/storage/docs/insights/v1/reportConfig).

  * `NUMBER_OF_INCLUDED_OBJECTS` is the number of objects included in the inventory report.

  * `SNAPSHOT_TIME` is the auto-generated UTC datetime at which the data snapshot occurs. All the data in an inventory report is captured at the snapshot.

  * `TARGET_DATETIME` is the auto-generated UTC datetime at which an inventory report is generated.

  * `SHARD_COUNT` is the total number of generated shards that compose the inventory report.

  * `SHARD_FILE_NAME` is the name of a shard that composes an inventory report.




An example `manifest.json` file looks like the following:
    
    
    {
      "report_config":
         {
           "name": "projects/123456789098/locations/us/reportConfigs/fcec5187-afa6-48b0-938a-543d16493dc0",
           "createTime": "2023-06-08T08:07:53.397366139Z",
           "updateTime": "2023-06-08T08:07:53.552347723Z",
           "frequencyOptions": {
             "frequency": "DAILY",
             "startDate": {
               "year": 2023,
               "month": 6,
               "day": 9
             }
             "endDate": {
               "year": 2023,
               "month": 6,
               "day": 23
             }
           },
           "csvOptions": {
             "recordSeparator": "\n",
             "delimiter": ","
           },
           "objectMetadataReportOptions": {
             "metadataFields": [
               "project",
               "bucket",
               "name",
               "location",
               "updated",
               "storageClass",
             ],
             "storageFilters": {
               "bucket": "my-test-bucket"
             },
             "storageDestinationOptions": {
               "bucket": "example-bucket",
               "destinationPath": "folder/subfolder"
             }
           }
         },
      "records_processed": 3993900,
      "snapshot_time" : "2023-06-06T00:07:27Z",
      "target_datetime": {
        "year": 2023,
        "month": 6,
        "day": 6
      },
      "shard_count": 4,
      "report_shards_file_names": [
        "fc95c52f-157a-494f-af4a-d4a53a69ba66_2022-11-30T00:54_0.csv",
        "fc95c52f-157a-494f-af4a-d4a53a69ba66_2022-11-30T00:54_1.csv",
        ...
      ],
    }

## Pricing

Using inventory reports is subject to pricing, which is dependent on the bucket's location. For more information about inventory reports pricing, see [Pricing](https://docs.cloud.google.com/storage/pricing).

## Audit logging

Cloud Storage creates [audit logs](https://docs.cloud.google.com/storage/docs/audit-logging) when inventory reports are generated in the destination bucket. Cloud Storage generates audit logs whenever inventory report configurations are created, updated, or deleted.

Cloud Storage **does not** create audit logs when an inventory report configuration reads object metadata from a source bucket.

## Integration with VPC Service Controls

You can provide an additional layer of security for inventory reports resources by using VPC Service Controls. When you use VPC Service Controls, you add projects to service perimeters that protect resources and services from requests that originate from outside of the perimeter. To learn more about VPC Service Controls and service perimeters, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

## Limitations

Inventory reports has the following limitations.

  * Enabling [IP filtering](https://docs.cloud.google.com/storage/docs/ip-filtering-overview) on Cloud Storage buckets restricts inventory reports from being able to access the bucket, regardless of whether they use a [service agent](https://docs.cloud.google.com/iam/docs/service-agents) to interact with Cloud Storage. To prevent service disruptions, we recommend not using IP filtering on Cloud Storage buckets if you are creating inventory reports for that bucket.

  * Inventory reports aren't supported in the following locations:

    * Regions:

      * `africa-south1`
      * `asia-southeast3`
      * `europe-north2`
      * `europe-west10`
      * `europe-west12`
      * `me-central1`
      * `me-central2`
      * `northamerica-south1`
    * Dual-regions:

      * `eur5`
      * `eur7`
      * `eur8`



## What's next

Learn how to [create an inventory report configuration](https://docs.cloud.google.com/storage/docs/insights/using-inventory-reports) and start generating inventory reports.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
