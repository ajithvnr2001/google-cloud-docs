---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/tensorboard-time-series/create/
title: gcloud beta ai tensorboard-time-series create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:23.891518+00:00
---

# gcloud beta ai tensorboard-time-series create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/tensorboard-time-series/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai tensorboard-time-series create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai tensorboard-time-series create - create a new Vertex AI Tensorboard time series 
SYNOPSIS
    

`gcloud beta ai tensorboard-time-series create` (`TENSORBOARD_RUN` : `--region`=`REGION` `--tensorboard-experiment-id`=`TENSORBOARD_EXPERIMENT_ID` `--tensorboard-id`=`TENSORBOARD_ID`) `--display-name`=`DISPLAY_NAME` `--type`=`TYPE` [`--description`=`DESCRIPTION`] [`--plugin-data`=`PLUGIN_DATA`] [`--plugin-name`=`PLUGIN_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new Vertex AI Tensorboard time series. 
EXAMPLES
     To create a Tensorboard Time Series in Tensorboard `12345`, Tensorboard Experiment `my-tensorboard-experiment, and in Tensorboard Run `my-tensorboard-run`, with the display name `my tensorboard time series` and type Scalar: 
    
    
    gcloud beta ai tensorboard-time-series create my-tensorboard-run --tensorboard-experiment-id=my-tensorboard-experiment --tensorboard-id=12345 --display-name="my tensorboard time series" --type=SCALAR

You may also provide a description: 
    
    
    gcloud beta ai tensorboard-time-series create my-tensorboard-run --tensorboard-experiment-id=my-tensorboard-experiment --tensorboard-id=12345 --display-name="my tensorboard time series" --type=SCALAR --description="my description"

To create a Tensorboard Time Series in Tensorboard 

`12345`, Tensorboard Experiment `my-tensorboard-experiment, Tensorboard Run `my-tensorboard-run`, region `us-central1`, and project `my-project`: 
    
    
    gcloud beta ai tensorboard-time-series create projects/my-project/locations/us-central1/tensorboards/12345/experiments/my-tensorboard-experiment/runs/my-tensorboard-run --display-name="my tensorboard time series" --type=SCALAR

POSITIONAL ARGUMENTS
    

Tensorboard run resource - The Tensorboard run to create a Tensorboard time series. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Display name of the tensorboard-time-series. 
`--type`=`TYPE`
     Value type of the tensorboard-time-series. `TYPE` must be one of: 

`blob-sequence`
     Used for tensorboard-time-series that is a list of blob sequences. E.g. set of sample images with labels over epochs/time. 
`scalar`
     Used for tensorboard-time-series that is a list of scalars. E.g. accuracy of a model over epochs/time. 
`tensor`
     Used for tensorboard-time-series that is a list of tensors. E.g. histograms of weights of layer in a model over epoch/time. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Description of the tensorboard-time-series. 
`--plugin-data`=`PLUGIN_DATA`
     Plugin data of the tensorboard-time-series. 
`--plugin-name`=`PLUGIN_NAME`
     Plugin name of the tensorboard-time-series. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha ai tensorboard-time-series create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-time-series/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
