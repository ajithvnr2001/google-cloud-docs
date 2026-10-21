---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/rolloutsequences/create/
title: gcloud beta container hub rolloutsequences create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:33:23.489418+00:00
---

# gcloud beta container hub rolloutsequences create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/rolloutsequences/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub rolloutsequences create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub rolloutsequences create - create a rollout sequence resource 
SYNOPSIS
    

`gcloud beta container hub rolloutsequences create` `ROLLOUTSEQUENCE` `--stage-config`=`PATH_TO_FILE` [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a rollout sequence resource. 
EXAMPLES
     To create a rollout sequence, run: 
    
    
    gcloud beta container hub rolloutsequences create ROLLOUTSEQUENCE --stage-config=path/to/config.yaml

POSITIONAL ARGUMENTS
    

RolloutSequence resource - The group of arguments defining a Rollout Sequence. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `rolloutSequence` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `rolloutSequence` on the command line with a fully specified name; 
  * global is the only supported location. 



This must be specified. 

`ROLLOUTSEQUENCE`
     ID of the rolloutSequence or fully qualified identifier for the rolloutSequence. 

To set the `rollout_sequence` attribute: 

  * provide the argument `rolloutSequence` on the command line. 


REQUIRED FLAGS
    

`--stage-config`=`PATH_TO_FILE`
     Path to the YAML file containing the stage configurations. The YAML file should contain a list of stages. Fleet projects and soak_duration are required. If label_selector is not specified, there is no filtering. A fleet project is the project where the fleet is hosted. Example: 
    
    
    - stage:
      fleet-projects:
      # Expected format: projects/{project}
      - projects/my-dev-project
      soak-duration: 7d # Or 168h or 604800s
    - stage:
      fleet-projects:
      - projects/my-prod-project
      soak-duration: 3600s
      label-selector: resource.labels.canary=='true'
    - stage:
      fleet-projects:
      # Expected format: projects/{project}
      - projects/my-prod-project
      soak-duration: 30m

Use a full or relative path to a local file containing the value of stage_config. 

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     Display name of the rollout sequence. 
`--labels`=[`KEY`=`VALUE`,…]
     Labels for the rollout sequence. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container hub rolloutsequences create](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/rolloutsequences/create)
    
    
    [gcloud alpha container hub rolloutsequences create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/rolloutsequences/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
