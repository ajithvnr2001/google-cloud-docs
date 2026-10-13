---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/query/
title: gcloud alpha bq query \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:49.224829+00:00
---

# gcloud alpha bq query  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bq/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bq query Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bq query - execute a BigQuery SQL query 
SYNOPSIS
    

`gcloud alpha bq query` [`SQL_QUERY`] [`--async`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--job-creation-mode`=`JOB_CREATION_MODE`] [`--job-id`=`JOB_ID`] [`--location`=`LOCATION`] [`--[no-]use-cache`] [`--[no-]use-legacy-sql`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha bq query` executes a SQL query on Google Cloud BigQuery. 

The query can be passed as a positional argument or read from standard input (stdin). 

EXAMPLES
     To execute a simple query: 
    
    
    gcloud alpha bq query 'SELECT 1'

To execute a query passed through stdin: 
    
    
    echo 'SELECT 1' | gcloud alpha bq query

To run a query asynchronously with a custom job ID: 
    
    
    gcloud alpha bq query 'SELECT 1' --async --job-id=my-job-id

POSITIONAL ARGUMENTS
    

[`SQL_QUERY`]
     SQL query to execute. If not specified, query will be read from stdin. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--job-creation-mode`=`JOB_CREATION_MODE`
     Specifies whether a job should be created. `JOB_CREATION_MODE` must be one of: `JOB_CREATION_REQUIRED`, `JOB_CREATION_OPTIONAL`. 
`--job-id`=`JOB_ID`
     A unique job ID to use for the query job. Forces a job to be created and is incompatible with `--job-creation-mode=JOB_CREATION_OPTIONAL`. 
`--location`=`LOCATION`
     The geographic location where the query should run. 
`--[no-]use-cache`
     Whether to look for the result in the query cache. Use `--use-cache` to enable and `--no-use-cache` to disable. 
`--[no-]use-legacy-sql`
     Whether to use BigQuery's legacy SQL dialect for this query. Use `--use-legacy-sql` to enable and `--no-use-legacy-sql` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
