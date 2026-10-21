---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/tensorboard-runs/describe/
title: gcloud beta ai tensorboard-runs describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:23.688300+00:00
---

# gcloud beta ai tensorboard-runs describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/tensorboard-runs/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai tensorboard-runs describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai tensorboard-runs describe - get detailed Tensorboard run information about the given Tensorboard run id 
SYNOPSIS
    

`gcloud beta ai tensorboard-runs describe` (`TENSORBOARD_RUN` : `--region`=`REGION` `--tensorboard-experiment-id`=`TENSORBOARD_EXPERIMENT_ID` `--tensorboard-id`=`TENSORBOARD_ID`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Get detailed Tensorboard run information about the given Tensorboard run id. 
EXAMPLES
     To describe a Tensorboard Run `my-tensorboard-run` in Tensorboard `12345`, Tensorboard Experiment `my-tensorboard-experiment`, region `us-central1`, and project `my-project`: 
    
    
    gcloud beta ai tensorboard-runs describe projects/my-project/locations/us-central1/tensorboards/12345/experiments/my-tensorboard-experiment/runs/my-tensorboard-run

Or with flags: 
    
    
    gcloud beta ai tensorboard-runs describe my-tensorboard-run --tensorboard-id=12345 --tensorboard-experiment-id=my-tensorboard-experiment

POSITIONAL ARGUMENTS
    

Tensorboard run resource - The Tensorboard run to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `tensorboard_run` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TENSORBOARD_RUN`
     ID of the tensorboard_run or fully qualified identifier for the tensorboard_run. 

To set the `name` attribute: 

  * provide the argument `tensorboard_run` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the tensorboard_run. 

To set the `region` attribute: 

  * provide the argument `tensorboard_run` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


`--tensorboard-experiment-id`=`TENSORBOARD_EXPERIMENT_ID`
     ID of the tensorboard experiment for the tensorboard_run. 

To set the `tensorboard-experiment-id` attribute: 

  * provide the argument `tensorboard_run` on the command line with a fully specified name; 
  * provide the argument `--tensorboard-experiment-id` on the command line. 


`--tensorboard-id`=`TENSORBOARD_ID`
     ID of the tensorboard for the tensorboard_run. 

To set the `tensorboard-id` attribute: 

  * provide the argument `tensorboard_run` on the command line with a fully specified name; 
  * provide the argument `--tensorboard-id` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha ai tensorboard-runs describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
