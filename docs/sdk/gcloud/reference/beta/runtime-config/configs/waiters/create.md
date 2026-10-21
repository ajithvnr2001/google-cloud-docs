---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/waiters/create/
title: gcloud beta runtime-config configs waiters create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:00.162139+00:00
---

# gcloud beta runtime-config configs waiters create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/runtime-config/configs/waiters/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta runtime-config configs waiters create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta runtime-config configs waiters create - create waiter resources 
SYNOPSIS
    

`gcloud beta runtime-config configs waiters create` `NAME` `--config-name`=`CONFIG_NAME` `--success-cardinality-path`=`SUCCESS_CARDINALITY_PATH` `--timeout`=`TIMEOUT` [`--async`] [`--failure-cardinality-number`=`FAILURE_CARDINALITY_NUMBER`; default=1] [`--failure-cardinality-path`=`FAILURE_CARDINALITY_PATH`] [`--success-cardinality-number`=`SUCCESS_CARDINALITY_NUMBER`; default=1] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command creates a new waiter resource with the specified name and parameters. 
EXAMPLES
     To create a waiter in "my-config" with success and failure paths nested under "/status", run: 
    
    
    gcloud beta runtime-config configs waiters create my-waiter --config-name=my-config --timeout=15m --success-cardinality-path=/status/success --success-cardinality-number=5 --failure-cardinality-path=/status/failure --failure-cardinality-number=1

This waiter will wait for at most 15 minutes for the first of two possible scenarios: 1) five or more variables are written to the /status/success/ path; or 2) one or more variables are written to the /status/failure/ path. 

To create a waiter without a failure path, run: 
    
    
    gcloud beta runtime-config configs waiters create my-waiter --config-name=my-config --timeout=15m --success-cardinality-path=/status/success --success-cardinality-number=5

This waiter will wait until 5 or more success variables are written, or the 15 minute timeout elapses. 

POSITIONAL ARGUMENTS
    

`NAME`
     The waiter name. 
REQUIRED FLAGS
    

`--config-name`=`CONFIG_NAME`
     The name of the configuration resource to use. 
`--success-cardinality-path`=`SUCCESS_CARDINALITY_PATH`
     The path where success variables are written. 
`--timeout`=`TIMEOUT`
     The amount of time to wait before failing with DEADLINE_EXCEEDED. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--failure-cardinality-number`=`FAILURE_CARDINALITY_NUMBER`; default=1
     The minimum required number of failure variables. 
`--failure-cardinality-path`=`FAILURE_CARDINALITY_PATH`
     The path where failure variables are written. 
`--success-cardinality-number`=`SUCCESS_CARDINALITY_NUMBER`; default=1
     The minimum required number of success variables. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
