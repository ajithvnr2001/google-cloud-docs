---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create/
title: gcloud alpha ai tensorboard-experiments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:28.827521+00:00
---

# gcloud alpha ai tensorboard-experiments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/tensorboard-experiments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ai tensorboard-experiments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ai tensorboard-experiments create - create a new Vertex AI Tensorboard experiment 
SYNOPSIS
    

`gcloud alpha ai tensorboard-experiments create` (`TENSORBOARD` : `--region`=`REGION`) `--tensorboard-experiment-id`=`TENSORBOARD_EXPERIMENT_ID` [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Vertex AI Tensorboard experiment. 
EXAMPLES
     To create a Tensorboard Experiment in a Tensorboard `12345`, with the display name `my tensorboard experiment`: 
    
    
    gcloud alpha ai tensorboard-experiments create 12345 --tensorboard-experiment-id=my-tensorboard-experiment --display-name="my tensorboard experiment"

You may also provide a description and/or labels: 
    
    
    gcloud alpha ai tensorboard-experiments create 12345 --tensorboard-experiment-id=my-tensorboard-experiment --description="my description" --labels="label1=value1" --labels="label2=value2"

To create a Tensorboard Experiment `my-tensorboard-experiment` in a Tensorboard `12345`, region `us-central1`, and project `my-project`: 
    
    
    gcloud alpha ai tensorboard-experiments create projects/my-project/locations/us-central1/tensorboards/12345 --tensorboard-experiment-id=my-tensorboard-experiment

POSITIONAL ARGUMENTS
    

Tensorboard resource - The tensorboard to create a Tensorboard experiment. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `tensorboard` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TENSORBOARD`
     ID of the tensorboard or fully qualified identifier for the tensorboard. 

To set the `name` attribute: 

  * provide the argument `tensorboard` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the tensorboard. 

To set the `region` attribute: 

  * provide the argument `tensorboard` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


REQUIRED FLAGS
    

`--tensorboard-experiment-id`=`TENSORBOARD_EXPERIMENT_ID`
     Id of the Tensorboard experiment. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Description of the tensorboard-experiment. 
`--display-name`=`DISPLAY_NAME`
     Display name of the tensorboard-experiment. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta ai tensorboard-experiments create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/tensorboard-experiments/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
