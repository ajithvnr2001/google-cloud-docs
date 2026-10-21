---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/fault-testing/experiments/create/
title: gcloud alpha fault-testing experiments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:40:55.385512+00:00
---

# gcloud alpha fault-testing experiments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/fault-testing/experiments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha fault-testing experiments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha fault-testing experiments create - create an experiment 
SYNOPSIS
    

`gcloud alpha fault-testing experiments create` `EXPERIMENT` `--experiment-template`=`EXPERIMENT_TEMPLATE` [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--location`=`LOCATION`] [`--start-on-create-enabled`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create an experiment. 
EXAMPLES
     To create an experiment `test-experiment-id` associated with experiment template `test-template-id` in location `asia-east1` with display name `test-experiment` run: 
    
    
    gcloud alpha fault-testing experiments create test-experiment-id --experiment-template=test-template-id --location=asia-east1 --display-name=test-experiment

POSITIONAL ARGUMENTS
    

Experiment resource - Identifier. Unique identifier for the experiment. Format: `projects/{project_id}/locations/{location}/experiments/{experiment_id}`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `experiment` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `experiment` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`EXPERIMENT`
     ID of the experiment or fully qualified identifier for the experiment. 

To set the `experiment` attribute: 

  * provide the argument `experiment` on the command line. 


REQUIRED FLAGS
    

ExperimentTemplate resource - The unique identifier of the reusable experiment template used to configure the experiment. This field determines the type of fault, target, and duration. Format: `projects/{project_id}/locations/{location}/experimentTemplates/{experimentTemplateId}`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--experiment-template` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--experiment-template` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--experiment-template`=`EXPERIMENT_TEMPLATE`
     ID of the experimentTemplate or fully qualified identifier for the experimentTemplate. 

To set the `experiment-template` attribute: 

  * provide the argument `--experiment-template` on the command line. 


OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Notes or details to describe the purpose or context of the experiment. Minimum length is 0, maximum length is 2000. 
`--display-name`=`DISPLAY_NAME`
     A human-readable name of the experiment. 
`--location`=`LOCATION`
     For resources [experiment, experiment-template], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
Arguments for the start on create enabled. 
`--start-on-create-enabled`
     If true, the experiment will be started immediately after creation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `faulttesting/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/fault-injection-testing>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
