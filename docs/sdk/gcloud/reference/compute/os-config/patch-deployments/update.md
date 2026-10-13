---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/update/
title: gcloud compute os-config patch-deployments update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:59.080478+00:00
---

# gcloud compute os-config patch-deployments update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-deployments/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute os-config patch-deployments update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute os-config patch-deployments update - update patch deployment in a project 
SYNOPSIS
    

`gcloud compute os-config patch-deployments update` `PATCH_DEPLOYMENT_ID` `--file`=`FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Updates a patch deployment in a project. To update the patch deployment, you must specify a configuration file. 
EXAMPLES
     To update a patch deployment `patch-deployment-1` in the current project, run: 
    
    
    gcloud compute os-config patch-deployments update patch-deployment-1 --file=path_to_config_file

POSITIONAL ARGUMENTS
    

`PATCH_DEPLOYMENT_ID`
     Name of the patch deployment to update. 

To get a list of patch deployments that are available for update, run the `gcloud compute os-config patch-deployments list` command. 

REQUIRED FLAGS
    

`--file`=`FILE`
     The JSON or YAML file with the patch deployment to update. For information about the patch deployment format, see <https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments>. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta compute os-config patch-deployments update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-config/patch-deployments/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
