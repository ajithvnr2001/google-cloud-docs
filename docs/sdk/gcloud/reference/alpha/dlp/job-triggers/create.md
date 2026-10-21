---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dlp/job-triggers/create/
title: gcloud alpha dlp job-triggers create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:59.604712+00:00
---

# gcloud alpha dlp job-triggers create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dlp/job-triggers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dlp job-triggers create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dlp job-triggers create - creates a Cloud DLP job trigger 
SYNOPSIS
    

`gcloud alpha dlp job-triggers create` `JOB_TRIGGER` `--trigger-schedule`=`TRIGGER_SCHEDULE` (`--datastore-kind`=`DATASTORE_KIND` | `--input-table`=`INPUT_TABLE` | `--path`=`PATH`) (`--output-table`=[`OUTPUT_TABLE`,…] | `--output-topics`=[`OUTPUT_TOPICS`,…]) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--exclude-info-types`] [`--include-quote`] [`--info-types`=[`INFOTYPE`,…]] [`--max-findings`=`MAX_FINDINGS`] [`--max-findings-per-item`=`MAX_FINDINGS_PER_ITEM`] [`--min-likelihood`=`MIN_LIKELIHOOD`; default="possible"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a Cloud DLP job trigger. 
EXAMPLES
     The following command creates a job trigger named `my_job_trigger`: 
    
    
    gcloud alpha dlp job-triggers create my_job_trigger --display-name Daily_Inspect_Trigger --description 'My New Trigger' --input-table myproject.mydataset.input --output-topics my-topic --max-findings-per-item 3 --max-findings 1000 --info-types PHONE_NUMBER,US_DRIVERS_LICENSE --min-likelihood very-likely --include-quote --exclude-info-types --trigger-schedule 8400s

POSITIONAL ARGUMENTS
    

Job trigger resource - The Cloud DLP job trigger to create. The job trigger name can contain uppercase and lowercase letters, numbers, and hyphens -- that is, it must match the regular expression:`[a-zA-Z\\d-]+`. The maximum length is 100 characters. If not supplied, the system generates one. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `job_trigger` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`JOB_TRIGGER`
     ID of the job_trigger or fully qualified identifier for the job_trigger. 

To set the `job_trigger` attribute: 

  * provide the argument `job_trigger` on the command line. 


REQUIRED FLAGS
    

`--trigger-schedule`=`TRIGGER_SCHEDULE`
     Duration specifying how often the triggered job will be run. A scheduled start time will be skipped if the previous execution has not ended when its scheduled time occurs. Value must be a time duration greater than or equal to 1 day and can be no longer than 60 days. 

See `$ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats.`

Exactly one of these must be specified: 

`--datastore-kind`=`DATASTORE_KIND`
     The Cloud Datastore kind or table to scan. The kind can optionally be prefixed with the Cloud Datastore namespace ID - for example `namespace:example-kind` or simply `example-kind`
`--input-table`=`INPUT_TABLE`
     BigQuery table to scan. BigQuery tables are uniquely identified by their project_id, dataset_id, and table_id in the format `<project_id>.<dataset_id>.<table_id>`. 
`--path`=`PATH`
     Google Cloud Storage URL to scan for files with optional wildcard character (`*`) -- for example, gs://my-bucket/`*`. 
Exactly one of these must be specified: 

`--output-table`=[`OUTPUT_TABLE`,…]
     Publishes results of a Cloud DLP job a BigQuery table. BigQuery tables are uniquely identified by their project_id, dataset_id, and table_id in the format `<project_id>.<dataset_id>.<table_id>`. 
`--output-topics`=[`OUTPUT_TOPICS`,…]
     Publishes the results of a Cloud DLP job to one or more Cloud Pub/Sub topics. 

Note: The topic must have given publishing access rights to the DLP API service account executing the Cloud DLP job. 

OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     User provided description (maximum 256 characters) 
`--display-name`=`DISPLAY_NAME`
     Display name of the job trigger (maximum 100 characters) 
`--exclude-info-types`
     Whether or not to exclude type information of the findings. Type information is included by default. 
`--include-quote`
     If True, a contextual quote from the data that triggered a finding is included in the response. Even if the content is not text, it may be converted to a textual representation in the response. For example, given the input value 'My phone number is (415) 555-0890' and a search for the infoType PHONE_NUMBER, the contextual quote would be '(415) 555-0890.' 
`--info-types`=[`INFOTYPE`,…]
     Which infoTypes to scan input for. The values must correspond to infoType values found in documentation. For more information about valid infoTypes, see [infoTypes Reference](https://cloud.google.com/dlp/docs/infotypes-reference)
`--max-findings`=`MAX_FINDINGS`
     Maximum number of findings that will be returned per execution. 

If not specified, no limits are applied. 

`--max-findings-per-item`=`MAX_FINDINGS_PER_ITEM`
     Maximum number of findings that will be returned for each item scanned. 

If not specified, no limits are applied. 

`--min-likelihood`=`MIN_LIKELIHOOD`; default="possible"
     Only return findings equal to or above this threshold. `MIN_LIKELIHOOD` must be one of: `likely`, `possible`, `unlikely`, `very-likely`, `very-unlikely`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `dlp/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/sensitive-data-protection/docs/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
