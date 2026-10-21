---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dlp/datasources/bigquery/analyze/
title: gcloud alpha dlp datasources bigquery analyze \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:57.874269+00:00
---

# gcloud alpha dlp datasources bigquery analyze  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dlp/datasources/bigquery/analyze/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dlp datasources bigquery analyze Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dlp datasources bigquery analyze - schedule a risk analysis job for content in a BigQuery table 
SYNOPSIS
    

`gcloud alpha dlp datasources bigquery analyze` `INPUT_TABLE` (`--categorical-stat-field`=`CATEGORICAL_STAT_FIELD` | `--numerical-stat-field`=`NUMERICAL_STAT_FIELD` | [`--quasi-ids`=[`QUASI_IDS`,…] : `--sensitive-attribute`=`SENSITIVE_ATTRIBUTE`]) (`--output-table`=[`OUTPUT_TABLE`,…] | `--output-topics`=[`OUTPUT_TOPICS`,…]) [`--job-id`=`JOB_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Schedules a job to compute risk analysis metrics on content in a BigQuery table. 
EXAMPLES
     To create a job `my-bq-analysis` to analyze records in a BigQuery table `myproject.myds.mytable`, run: 
    
    
    gcloud alpha dlp datasources bigquery analyze `myproject.myds.mytable` --job-id my-ds-job --output-topics my-topic --numerical-stat-field col2

POSITIONAL ARGUMENTS
    

`INPUT_TABLE`
     BigQuery table to scan. BigQuery tables are uniquely identified by their project_id, dataset_id, and table_id in the format `<project_id>.<dataset_id>.<table_id>`. 
REQUIRED FLAGS
    

Privacy analysis metrics. 

Exactly one of these must be specified: 

`--categorical-stat-field`=`CATEGORICAL_STAT_FIELD`
     An individual column to compute numerical stats on, including number of distinct values and value count distribution. 
`--numerical-stat-field`=`NUMERICAL_STAT_FIELD`
     Individual column to compute numerical stats on. Supported types are integer, float, date, datetime, timestamp, time. 
Or at least one of these can be specified: 

l-diversity analysis options. 
`--quasi-ids`=[`QUASI_IDS`,…]
     A set of quasi-identifiers indicating how equivalence classes are defined for the l-diversity computation. When multiple fields are specified, they are considered a single composite key. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--sensitive-attribute`=`SENSITIVE_ATTRIBUTE`
     Sensitive field for computing the l-diversity value. 
Exactly one of these must be specified: 

`--output-table`=[`OUTPUT_TABLE`,…]
     Publishes results of a Cloud DLP job to a BigQuery table. BigQuery tables are uniquely identified by their project_id, dataset_id, and table_id in the format `<project_id>.<dataset_id>.<table_id>`. If no table_id is specified, DLP will create a new table. 
`--output-topics`=[`OUTPUT_TOPICS`,…]
     Publishes the results of a Cloud DLP job to one or more Cloud Pub/Sub topics. 

Note: The topic must have given publishing access rights to the DLP API service account executing the Cloud DLP job. 

OPTIONAL FLAGS
    

`--job-id`=`JOB_ID`
     Optional job ID to use for the created job. If not provided, a job ID will automatically be generated. Must be unique within the project. The job ID can contain uppercase and lowercase letters, numbers, and hyphens; that is, it must match the regular expression: `[a-zA-Z\\d-]+`. The maximum length is 100 characters. Can be empty to allow the system to generate one. 
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
