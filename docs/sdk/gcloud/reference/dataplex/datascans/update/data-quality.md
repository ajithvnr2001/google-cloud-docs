---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality/
title: gcloud dataplex datascans update data-quality \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:56:17.851194+00:00
---

# gcloud dataplex datascans update data-quality  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/datascans/update/data-quality/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataplex datascans update data-quality Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataplex datascans update data-quality - update a Dataplex data quality scan job 
SYNOPSIS
    

`gcloud dataplex datascans update data-quality` (`DATASCAN` : `--location`=`LOCATION`) [`--data-quality-spec-file`=`DATA_QUALITY_SPEC_FILE`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`--async` | `--validate-only`] [`--on-demand`=`ON_DEMAND` | `--schedule`=`SCHEDULE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Represents a user-visible job which provides the insights for the related data source and generates queries based on the rules and runs against the data to get data quality check results. 
EXAMPLES
     To update description of a data quality scan `data-quality-datascan` in project `test-project` located in `us-central1`, run: 
    
    
    gcloud dataplex datascans update data-quality data-quality-datascan --project=test-project --location=us-central1 --description="Description is updated."

POSITIONAL ARGUMENTS
    

Datascan resource - Arguments and flags that define the Dataplex datascan you want to update a data quality scan for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--data-quality-spec-file`=`DATA_QUALITY_SPEC_FILE`
     Path to the JSON/YAML file containing the spec for the data quality scan. The JSON representation reference: <https://cloud.google.com/dataplex/docs/reference/rest/v1/DataQualitySpec> The YAML representation reference: <https://cloud.google.com/dataplex/docs/use-auto-data-quality#create-scan-using-gcloud>
`--description`=`DESCRIPTION`
     Description of the data quality scan 
`--display-name`=`DISPLAY_NAME`
     Display name of the data quality scan 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of --async | --validate-only can be specified. 

At most one of these can be specified: 

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--validate-only`
     Validate the update action, but don't actually perform it. 
Data quality scan execution settings. 
Data quality scan scheduling and trigger settings 

At most one of these can be specified: 

`--on-demand`=`ON_DEMAND`
     If set, the scan runs one-time shortly after data quality scan updation. 
`--schedule`=`SCHEDULE`
     Cron schedule (https://en.wikipedia.org/wiki/Cron) for running scans periodically. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, `CRON_TZ=America/New_York 1 * * * *` or `TZ=America/New_York 1 * * * *`. This field is required for RECURRING scans. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha dataplex datascans update data-quality](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/datascans/update/data-quality)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
