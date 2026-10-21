---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/describe/
title: gcloud alpha ai tensorboard-time-series describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:30.028852+00:00
---

# gcloud alpha ai tensorboard-time-series describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ai tensorboard-time-series describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ai tensorboard-time-series describe - get detailed Tensorboard time series information about the given Tensorboard time series id 
SYNOPSIS
    

`gcloud alpha ai tensorboard-time-series describe` (`TENSORBOARD_TIME_SERIES` : `--region`=`REGION` `--tensorboard-experiment-id`=`TENSORBOARD_EXPERIMENT_ID` `--tensorboard-id`=`TENSORBOARD_ID` `--tensorboard-run-id`=`TENSORBOARD_RUN_ID`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Get detailed Tensorboard time series information about the given Tensorboard time series id. 
EXAMPLES
     To describe a Tensorboard Time Series `123` in Tensorboard `12345`, Tensorboard Experiment `my-tensorboard-experiment, Tensorboard Run `my-tensorboard-run`, region `us-central1`, and project `my-project`: 
    
    
    gcloud alpha ai tensorboard-time-series describe projects/my-project/locations/us-central1/tensorboards/12345/experiments/my-tensorboard-experiment/runs/my-tensorboard-run/timeSeries/123

Or with flags: 
    
    
    gcloud alpha ai tensorboard-time-series describe 123 --tensorboard-id=12345 --tensorboard-experiment-id=my-tensorboard-experiment --tensorboard-run-id=my-tensorboard-run

`
POSITIONAL ARGUMENTS
    

Tensorboard time series resource - The Tensorboard time series to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `tensorboard_time_series` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TENSORBOARD_TIME_SERIES`
     ID of the tensorboard_time_series or fully qualified identifier for the tensorboard_time_series. 

To set the `name` attribute: 

  * provide the argument `tensorboard_time_series` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the tensorboard_time_series. 

To set the `region` attribute: 

  * provide the argument `tensorboard_time_series` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


`--tensorboard-experiment-id`=`TENSORBOARD_EXPERIMENT_ID`
     ID of the tensorboard experiment for the tensorboard_time_series. 

To set the `tensorboard-experiment-id` attribute: 

  * provide the argument `tensorboard_time_series` on the command line with a fully specified name; 
  * provide the argument `--tensorboard-experiment-id` on the command line. 


`--tensorboard-id`=`TENSORBOARD_ID`
     ID of the tensorboard for the tensorboard_time_series. 

To set the `tensorboard-id` attribute: 

  * provide the argument `tensorboard_time_series` on the command line with a fully specified name; 
  * provide the argument `--tensorboard-id` on the command line. 


`--tensorboard-run-id`=`TENSORBOARD_RUN_ID`
     ID of the tensorboard run for the tensorboard_time_series. 

To set the `tensorboard-run-id` attribute: 

  * provide the argument `tensorboard_time_series` on the command line with a fully specified name; 
  * provide the argument `--tensorboard-run-id` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta ai tensorboard-time-series describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/tensorboard-time-series/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
