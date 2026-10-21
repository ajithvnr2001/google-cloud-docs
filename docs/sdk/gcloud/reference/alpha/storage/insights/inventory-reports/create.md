---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/insights/inventory-reports/create/
title: gcloud alpha storage insights inventory-reports create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:29:12.593856+00:00
---

# gcloud alpha storage insights inventory-reports create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/insights/inventory-reports/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage insights inventory-reports create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage insights inventory-reports create - create a new inventory report config 
SYNOPSIS
    

`gcloud alpha storage insights inventory-reports create` `SOURCE_BUCKET_URL` [`--destination`=`DESTINATION_URL`] [`--display-name`=`DISPLAY_NAME`] [`--metadata-fields`=[`METADATA_FIELDS`,…]; default="project,bucket,name,location,size,timeCreated,timeDeleted,updated,storageClass,etag,retentionExpirationTime,crc32c,md5Hash,generation,metageneration,contentType,contentEncoding,timeStorageClassUpdated"] [`--schedule-repeats`=`FREQUENCY`; default="daily"] [`--schedule-repeats-until`=`END_DATE`] [`--schedule-starts`=`START_DATE`] [`--parquet` | `--csv-delimiter`=`DELIMITER` `--[no-]csv-header` `--csv-separator`=`SEPARATOR`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create an inventory report config that defines how often inventory reports are generated, the metadata fields you want the reports to include, and a bucket/prefix in which to store the reports, also known as the destination. 
EXAMPLES
     To create an inventory report about "my-bucket" that will store report details in "report-bucket" with the prefix "save-path/". 
    
    
    gcloud alpha storage insights inventory-reports create gs://my-bucket --destination=gs://report-bucket/save-path/

POSITIONAL ARGUMENTS
    

`SOURCE_BUCKET_URL`
     URL of the source bucket that will contain the inventory report configuration. 
FLAGS
    

`--destination`=`DESTINATION_URL`
     Sets the URL of the destination bucket and path where generated reports are stored. Defaults to <SOURCE_BUCKET_URL>/inventory_reports/. 
`--display-name`=`DISPLAY_NAME`
     Sets the editable name of the report configuration. 
`--metadata-fields`=[`METADATA_FIELDS`,…]; default="project,bucket,name,location,size,timeCreated,timeDeleted,updated,storageClass,etag,retentionExpirationTime,crc32c,md5Hash,generation,metageneration,contentType,contentEncoding,timeStorageClassUpdated"
     The metadata fields to be included in the inventory report. The fields: "project, bucket, name" are REQUIRED. Defaults to all fields being included. `METADATA_FIELDS` must be one of: `project`, `bucket`, `name`, `location`, `size`, `timeCreated`, `timeDeleted`, `updated`, `storageClass`, `etag`, `retentionExpirationTime`, `crc32c`, `md5Hash`, `generation`, `metageneration`, `contentType`, `contentEncoding`, `timeStorageClassUpdated`. 
`--schedule-repeats`=`FREQUENCY`; default="daily"
     Sets how often the inventory report configuration will run. Defaults to DAILY. `FREQUENCY` must be one of: `daily`, `weekly`. 
`--schedule-repeats-until`=`END_DATE`
     Sets date after which you want to stop generating inventory reports. For example, 2022-03-30. Defaults to one year from --schedule-starts value. 
`--schedule-starts`=`START_DATE`
     Sets the date you want to start generating inventory reports. For example, 2022-01-30. Should be tomorrow or later based on UTC timezone. Defaults to tomorrow. 
Report format configuration. Any combination of CSV flags is valid as long as the Parquet flag is not present. 

At most one of these can be specified: 

`--parquet`
     Generate reports in parquet format. 
Or at least one of these can be specified: 

Flags for setting CSV format options. 
`--csv-delimiter`=`DELIMITER`
     Sets the delimiter that separates the fields in the inventory report CSV file. For example, ``,`` 
`--[no-]csv-header`
     Indicates whether or not headers are included in the inventory report CSV file. Default is None. Use `--csv-header` to enable and `--no-csv-header` to disable. 
`--csv-separator`=`SEPARATOR`
     Sets the character used to separate the records in the inventory report CSV file. For example, ``\n``. `SEPARATOR` must be one of: `\n`, `\r\n`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud storage insights inventory-reports create](https://docs.cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
