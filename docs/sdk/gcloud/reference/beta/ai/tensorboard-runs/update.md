---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/tensorboard-runs/update/
title: gcloud beta ai tensorboard-runs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:23.516439+00:00
---

# gcloud beta ai tensorboard-runs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/tensorboard-runs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai tensorboard-runs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai tensorboard-runs update - update an existing Vertex AI Tensorboard run 
SYNOPSIS
    

`gcloud beta ai tensorboard-runs update` (`TENSORBOARD_RUN` : `--region`=`REGION` `--tensorboard-experiment-id`=`TENSORBOARD_EXPERIMENT_ID` `--tensorboard-id`=`TENSORBOARD_ID`) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an existing Vertex AI Tensorboard run. 
EXAMPLES
     To update Tensorboard Time Run `my-tensorboard-run` in Tensorboard `12345`, Tensorboard Experiment `my-tensorboard-experiment`, with the display name `updated display name`: 
    
    
    gcloud beta ai tensorboard-runs update projects/my-project/locations/us-central1/tensorboards/12345/experiments/my-tensorboard-experiment/runs/my-tensorboard-run --display-name="updated display name"

Or with flags: 
    
    
    gcloud beta ai tensorboard-runs update my-tensorboard-run --tensorboard-id=12345 --tensorboard-experiment-id=my-tensorboard-experiment --display-name="updated display name"

POSITIONAL ARGUMENTS
    

Tensorboard run resource - The Tensorboard run to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--description`=`DESCRIPTION`
     Description of the tensorboard run. 
`--display-name`=`DISPLAY_NAME`
     Display name of the tensorboard run. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta ai tensorboard-runs update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta ai tensorboard-runs update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha ai tensorboard-runs update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-runs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
