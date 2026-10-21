---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/describe/
title: gcloud ai-platform jobs describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:24:44.359382+00:00
---

# gcloud ai-platform jobs describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai-platform jobs describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai-platform jobs describe - describe an AI Platform job 
SYNOPSIS
    

`gcloud ai-platform jobs describe` `JOB` [`--summarize`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe an AI Platform job. 
EXAMPLES
     To describe the AI Platform job named ``my-job``, run: 
    
    
    gcloud ai-platform jobs describe my-job

POSITIONAL ARGUMENTS
    

`JOB`
     Name of the job. 
FLAGS
    

`--summarize`
     Summarize job output in a set of human readable tables instead of rendering the entire resource as json or yaml. The tables currently rendered are: 

  * `Job Overview`: Overview of job including, jobId, status and create time. 
  * `Training Input Summary`: Summary of input for a training job including region, main training python module and scale tier. 
  * `Training Output Summary`: Summary of output for a training job including the amount of ML units consumed by the job. 
  * `Training Output Trials`: Summary of hyperparameter trials run for a hyperparameter tuning training job. 
  * `Predict Input Summary`: Summary of input for a prediction job including region, model verion and output path. 
  * `Predict Output Summary`: Summary of output for a prediction job including prediction count and output path. 



This flag overrides the `--format` flag. If both are present on the command line, a warning is displayed. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai-platform jobs describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/jobs/describe)
    
    
    [gcloud beta ai-platform jobs describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/jobs/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
