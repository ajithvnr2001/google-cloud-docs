---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/datascans/update/data-profile/
title: gcloud alpha dataplex datascans update data-profile \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:38.993770+00:00
---

# gcloud alpha dataplex datascans update data-profile  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/datascans/update/data-profile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex datascans update data-profile Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex datascans update data-profile - update a Dataplex data profile scan job 
SYNOPSIS
    

`gcloud alpha dataplex datascans update data-profile` (`DATASCAN` : `--location`=`LOCATION`) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`--async` | `--validate-only`] [`--data-profile-spec-file`=`DATA_PROFILE_SPEC_FILE` | `--enable-catalog-publishing` `--exclude-field-names`=`EXCLUDE_FIELD_NAMES` `--include-field-names`=`INCLUDE_FIELD_NAMES` `--mode`=`MODE` `--row-filter`=`ROW_FILTER` `--sampling-percent`=`SAMPLING_PERCENT`] [`--on-demand`=`ON_DEMAND` | `--schedule`=`SCHEDULE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Represents a user-visible job which provides the insights for the related data source about the structure, content and relationships (such as null percent, cardinality, min/max/mean, etc). 
EXAMPLES
     To update description of a data profile scan `data-profile-datascan` in project `test-project` located in `us-central1`, run: 
    
    
    gcloud alpha dataplex datascans update data-profile data-profile-datascan --project=test-project --location=us-central1 --description="Description is updated."

POSITIONAL ARGUMENTS
    

Datascan resource - Arguments and flags that define the Dataplex datascan you want to update a data profile scan for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--description`=`DESCRIPTION`
     Description of the data profile scan 
`--display-name`=`DISPLAY_NAME`
     Display name of the data profile scan 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of --async | --validate-only can be specified. 

At most one of these can be specified: 

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--validate-only`
     Validate the update action, but don't actually perform it. 
Data spec for the data profile scan. 

At most one of these can be specified: 

`--data-profile-spec-file`=`DATA_PROFILE_SPEC_FILE`
     path to the JSON/YAML file containing the spec for the data profile scan. The JSON representation reference: <https://cloud.google.com/dataplex/docs/reference/rest/v1/DataProfileSpec>
Or at least one of these can be specified: 

Command line spec arguments for the data profile scan. 
`--enable-catalog-publishing`
     Publish data profile results to Dataplex catalog. 
`--exclude-field-names`=`EXCLUDE_FIELD_NAMES`
     Names of the fields to exclude from data profile. If specified, the respective fields will be excluded from data profile, regardless of the fields specified in the `--include-field-names` flag. 
`--include-field-names`=`INCLUDE_FIELD_NAMES`
     Names of the fields to include in data profile. If not specified, all fields at the time of profile scan job execution are included. The fields listed in the `--exclude-field-names` flag are excluded. 
`--mode`=`MODE`
     The execution mode for the profile scan. `MODE` must be one of: 

`LIGHTWEIGHT`
     Get quick insights with a low-latency, low-fidelity scan. 
`STANDARD`
     Profile your data with customizable scan settings. 
`--row-filter`=`ROW_FILTER`
     A filter applied to all rows in a single data profile scan job. 
`--sampling-percent`=`SAMPLING_PERCENT`
     The percentage of the records to be selected from the dataset for data profile scan. 
Data profile scan execution settings. 
Data profile scan scheduling and trigger settings 

At most one of these can be specified: 

`--on-demand`=`ON_DEMAND`
     If set, the scan runs one-time shortly after data profile scan updation. 
`--schedule`=`SCHEDULE`
     Cron schedule (https://en.wikipedia.org/wiki/Cron) for running scans periodically. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, `CRON_TZ=America/New_York 1 * * * *` or `TZ=America/New_York 1 * * * *`. This field is required for RECURRING scans. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex datascans update data-profile](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-profile)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
