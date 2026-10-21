---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/datascans/create/data-documentation/
title: gcloud alpha dataplex datascans create data-documentation \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:27.029513+00:00
---

# gcloud alpha dataplex datascans create data-documentation  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/datascans/create/data-documentation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex datascans create data-documentation Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex datascans create data-documentation - create a Dataplex data documentation scan job 
SYNOPSIS
    

`gcloud alpha dataplex datascans create data-documentation` (`DATASCAN` : `--location`=`LOCATION`) (`--data-source-entity`=`DATA_SOURCE_ENTITY` | `--data-source-resource`=`DATA_SOURCE_RESOURCE`) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--enable-catalog-publishing`] [`--labels`=[`KEY`=`VALUE`,…]] [`--async` | `--validate-only`] [`--on-demand`=`ON_DEMAND` | `--schedule`=`SCHEDULE` | `--one-time` `--ttl-after-scan-completion`=`TTL_AFTER_SCAN_COMPLETION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Allows users to generate documentation for Dataplex BigQuery tables. 
EXAMPLES
     To create a data documentation scan `data-documentation-datascan` in project `test-project` located in `us-central1` on entity `test-entity`, run: 
    
    
    gcloud alpha dataplex datascans create data-documentation data-documentation-datascan --project=test-project --location=us-central1 --data-source-resource="//bigquery.{universe_domain}/projects/test-project/datasets/test-dataset/tables/test-table"

POSITIONAL ARGUMENTS
    

Datascan resource - Arguments and flags that define the Dataplex datascan you want to create a data documentation scan for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `datascan` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATASCAN`
     ID of the datascan or fully qualified identifier for the datascan. 

To set the `dataScans` attribute: 

  * provide the argument `datascan` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Dataplex resource. 

To set the `location` attribute: 

  * provide the argument `datascan` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


REQUIRED FLAGS
    

Data source for the data documentation scan. 

Exactly one of these must be specified: 

`--data-source-entity`=`DATA_SOURCE_ENTITY`
     The Dataplex entity that contains the data for the data documentation scan, of the form: projects/{project_id_or_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{entity_id}. Currently only BigQuery table is supported. 
`--data-source-resource`=`DATA_SOURCE_RESOURCE`
     Fully-qualified service resource name of the cloud resource that contains the data for the data documentation scan, of the form: //bigquery.{universe_domain}/projects/{project_id_or_number}/datasets/{dataset_id}/tables/{table_id}. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Description of the data documentation scan. 
`--display-name`=`DISPLAY_NAME`
     Display name of the data documentation scan. 
Data documentation scan settings. 
`--enable-catalog-publishing`
     Publish data documentation results to Knowledge Catalog. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of --async | --validate-only can be specified. 

At most one of these can be specified: 

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--validate-only`
     Validate the create action, but don't actually perform it. 
Data documentation scan execution settings. 
Data documentation scan trigger settings. 

At most one of these can be specified: 

`--on-demand`=`ON_DEMAND`
     If set, the scan runs one-time shortly after data documentation scan creation. 
`--schedule`=`SCHEDULE`
     Cron schedule (https://en.wikipedia.org/wiki/Cron) for running scans periodically. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, `CRON_TZ=America/New_York 1 * * * *` or `TZ=America/New_York 1 * * * *`. This field is required for RECURRING scans. The argument is only valid when --on-demand is not set. 
Or at least one of these can be specified: 

Data documentation scan one-time trigger settings. 
`--one-time`
     If set, the data documentation scan runs once, and is auto-deleted once the ttl_after_scan_completion expires. 
`--ttl-after-scan-completion`=`TTL_AFTER_SCAN_COMPLETION`
     The time to live for one-time scans. Default value is 24 hours, minimum value is 0 seconds, and maximum value is 365 days. The time is calculated from the data scan job completion time. If value is set as 0 seconds, the scan will be immediately deleted upon job completion, regardless of whether the job succeeded or failed. The value should be a number followed by a unit suffix "s". Example: "100s" for 100 seconds. The argument is only valid when --one-time is set. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex datascans create data-documentation](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/create/data-documentation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
