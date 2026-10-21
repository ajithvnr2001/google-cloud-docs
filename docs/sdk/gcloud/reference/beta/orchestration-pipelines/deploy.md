---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/orchestration-pipelines/deploy/
title: gcloud beta orchestration-pipelines deploy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:57:29.775414+00:00
---

# gcloud beta orchestration-pipelines deploy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/orchestration-pipelines/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta orchestration-pipelines deploy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta orchestration-pipelines deploy - deploy a pipelines bundle 
SYNOPSIS
    

`gcloud beta orchestration-pipelines deploy` `--environment`=`ENVIRONMENT` [`--async`] [`--local`] [`--[no-]paused`] [`--pipeline`=`PIPELINE`] [`--rollback`] [`--substitutions`=[`KEY`=`VALUE`,…]] [`--substitutions-file`=`SUBSTITUTIONS_FILE`] [`--validate`] [`--version`=`VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Deploy a pipelines bundle. 
REQUIRED FLAGS
    

`--environment`=`ENVIRONMENT`
     The target environment for the deployment. 
OPTIONAL FLAGS
    

`--async`
     If set, deploys asynchronously without waiting for the information about all the pipelines in the bundle to become available. 
`--local`
     If set, performs a local deployment without requiring Git. Rollback logic will be disabled. 
`--[no-]paused`
     Adds the deployed pipelines to the paused_pipelines list. Defaults to true for local deployments, meaning the pipeline will be automatically paused. Use `--no-paused` to explicitly unpause. Currently only supported when using the `--local` flag. Use `--paused` to enable and `--no-paused` to disable. 
`--pipeline`=`PIPELINE`
     Deploy a specific pipeline by ID, name, or source file. Particularly useful for speeding up `--local` deployments. 
`--rollback`
     If set, performs a rollback to a specified version. 
`--substitutions`=[`KEY`=`VALUE`,…]
     Variables to substitute in the pipeline configuration. 
`--substitutions-file`=`SUBSTITUTIONS_FILE`
     Path to a YAML file containing variable substitutions for the pipeline configuration. 
`--validate`
     If set, performs full validation for resources and pipelines. 
`--version`=`VERSION`
     The git SHA version to rollback to. Required if `--rollback` is set. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
