---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/patch-deployments/create/
title: gcloud beta compute os-config patch-deployments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:17.463809+00:00
---

# gcloud beta compute os-config patch-deployments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/patch-deployments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute os-config patch-deployments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute os-config patch-deployments create - create a patch deployment for a project 
SYNOPSIS
    

`gcloud beta compute os-config patch-deployments create` `PATCH_DEPLOYMENT_ID` `--file`=`FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute os-config patch-deployments create` creates a patch deployment in a project from a specified file. A patch deployment triggers a patch job to run at specific time(s) according to a schedule, and applies instance filters and other patch configurations to the patch job at run time. Alternatively, to run a patch job on-demand, see `$ [gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` `beta compute os-config patch-jobs execute`. 
EXAMPLES
     To create a patch deployment `patch-deployment-1` in the current project, run: 
    
    
    gcloud beta compute os-config patch-deployments create patch-deployment-1 --file=path_to_config_file

POSITIONAL ARGUMENTS
    

`PATCH_DEPLOYMENT_ID`
     Name of the patch deployment to create. 

This name must contain only lowercase letters, numbers, and hyphens, start with a letter, end with a number or a letter, be between 1-63 characters, and unique within the project. 

REQUIRED FLAGS
    

`--file`=`FILE`
     The JSON or YAML file with the patch deployment to create. For information about the patch deployment format, see <https://cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchDeployments>. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud compute os-config patch-deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
