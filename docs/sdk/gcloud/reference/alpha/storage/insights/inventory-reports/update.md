---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/insights/inventory-reports/update/
title: gcloud alpha storage insights inventory-reports update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:54:45.204506+00:00
---

# gcloud alpha storage insights inventory-reports update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/insights/inventory-reports/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage insights inventory-reports update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage insights inventory-reports update - update an inventory report config 
SYNOPSIS
    

`gcloud alpha storage insights inventory-reports update` (`REPORT_CONFIG` : `--location`=`LOCATION`) [`--destination`=`DESTINATION_URL`] [`--display-name`=`DISPLAY_NAME`] [`--schedule-repeats`=`FREQUENCY`] [`--schedule-repeats-until`=`END_DATE`] [`--schedule-starts`=`START_DATE`] [`--metadata-fields`=[`METADATA_FIELDS`,…] | `--add-metadata-fields`=[`METADATA_FIELDS`,…] `--remove-metadata-fields`=[`METADATA_FIELDS`,…]] [`--parquet` | `--csv-delimiter`=`DELIMITER` `--[no-]csv-header` `--csv-separator`=`SEPARATOR`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update an inventory report config. 
EXAMPLES
     To update the display-name of an inventory report config with ID=1234, location=us-central1, and project=foo: 
    
    
    gcloud alpha storage insights inventory-reports update 1234 --location=us-central1 --project=foo --display-name=bar

To update the same inventory report config with fully specified name: 
    
    
    gcloud alpha storage insights inventory-reports update /projects/foo/locations/us-central1/reportConfigs/1234 --display-name=bar

POSITIONAL ARGUMENTS
    

Report config resource - The Report config to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `report_config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`REPORT_CONFIG`
     ID of the report-config or fully qualified identifier for the report-config. 

To set the `report-config` attribute: 

  * provide the argument `report_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location for the report-config. 

To set the `location` attribute: 

  * provide the argument `report_config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--destination`=`DESTINATION_URL`
     Sets the URL of the destination bucket and path where generated reports are stored. 
`--display-name`=`DISPLAY_NAME`
     Sets the editable name of the report configuration. 
`--schedule-repeats`=`FREQUENCY`
     Sets how often the inventory report configuration will run. `FREQUENCY` must be one of: `daily`, `weekly`. 
`--schedule-repeats-until`=`END_DATE`
     Sets date after which you want to stop generating inventory reports. For example, 2022-03-30. 
`--schedule-starts`=`START_DATE`
     Sets the date you want to start generating inventory reports. For example, 2022-01-30. Should be tomorrow or later based on UTC timezone. 
At most one of these can be specified: 

`--metadata-fields`=[`METADATA_FIELDS`,…]
     The metadata fields to be included in the inventory report. The fields: "project, bucket, name" are REQUIRED. `METADATA_FIELDS` must be one of: `project`, `bucket`, `name`, `location`, `size`, `timeCreated`, `timeDeleted`, `updated`, `storageClass`, `etag`, `retentionExpirationTime`, `crc32c`, `md5Hash`, `generation`, `metageneration`, `contentType`, `contentEncoding`, `timeStorageClassUpdated`. 
Or at least one of these can be specified: 

Add and Remove flags for metadata fields 
`--add-metadata-fields`=[`METADATA_FIELDS`,…]
     Adds fields to the metadata_fields list. `METADATA_FIELDS` must be one of: `location`, `size`, `timeCreated`, `timeDeleted`, `updated`, `storageClass`, `etag`, `retentionExpirationTime`, `crc32c`, `md5Hash`, `generation`, `metageneration`, `contentType`, `contentEncoding`, `timeStorageClassUpdated`. 
`--remove-metadata-fields`=[`METADATA_FIELDS`,…]
     Removes fields from the metadata_fields list. `METADATA_FIELDS` must be one of: `location`, `size`, `timeCreated`, `timeDeleted`, `updated`, `storageClass`, `etag`, `retentionExpirationTime`, `crc32c`, `md5Hash`, `generation`, `metageneration`, `contentType`, `contentEncoding`, `timeStorageClassUpdated`. 
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
    
    
    [gcloud storage insights inventory-reports update](https://docs.cloud.google.com/sdk/gcloud/reference/storage/insights/inventory-reports/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
