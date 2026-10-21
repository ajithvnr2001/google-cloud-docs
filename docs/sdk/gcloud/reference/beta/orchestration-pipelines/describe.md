---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/orchestration-pipelines/describe/
title: gcloud beta orchestration-pipelines describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:57:30.032043+00:00
---

# gcloud beta orchestration-pipelines describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/orchestration-pipelines/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta orchestration-pipelines describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta orchestration-pipelines describe - get details about an orchestration pipeline 
SYNOPSIS
    

`gcloud beta orchestration-pipelines describe` `--bundle`=`BUNDLE` `--pipeline`=`PIPELINE` (`--environment`=`ENVIRONMENT` | `--runner`=`RUNNER`) [`--substitutions`=[`KEY`=`VALUE`,…]] [`--substitutions-file`=`SUBSTITUTIONS_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Get details about an orchestration pipeline. 
REQUIRED FLAGS
    

`--bundle`=`BUNDLE`
     The ID of the bundle the pipeline belongs to. 
`--pipeline`=`PIPELINE`
     The ID of the pipeline to describe. 
Exactly one of these must be specified: 

`--environment`=`ENVIRONMENT`
     The target environment of the pipeline, as defined in deployment.yaml. 
`--runner`=`RUNNER`
     The full resource name of the runner to describe a pipeline from. 
OPTIONAL FLAGS
    

`--substitutions`=[`KEY`=`VALUE`,…]
     Variables to substitute in the pipeline configuration. 
`--substitutions-file`=`SUBSTITUTIONS_FILE`
     Path to a YAML file containing variable substitutions for the pipeline configuration. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
