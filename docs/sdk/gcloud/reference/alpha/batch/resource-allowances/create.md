---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/create/
title: gcloud alpha batch resource-allowances create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:28:13.571318+00:00
---

# gcloud alpha batch resource-allowances create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/batch/resource-allowances/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha batch resource-allowances create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha batch resource-allowances create - create a Batch resource allowance 
SYNOPSIS
    

`gcloud alpha batch resource-allowances create` [[`RESOURCE_ALLOWANCE`] `--location`=`LOCATION`] `--config`=`PATH_TO_FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command creates a Batch resource allowance. 
EXAMPLES
     The following command submit a resource allowance with config.json sample config file `projects/foo/locations/us-central1/resousrceAllowances/bar`: 
    
    
    gcloud alpha batch resource-allowances create projects/foo/locations/us-central1/resousrceAllowances/bar --config config.json

POSITIONAL ARGUMENTS
    

ResourceAllowance resource - The Batch resource allowance resource. If \--location not specified,the current batch/location is used. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `RESOURCE_ALLOWANCE` on the command line with a fully specified name; 
  * resource allowance ID is optional and will be generated if not specified with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


[`RESOURCE_ALLOWANCE`]
     ID of the resourceAllowance or fully qualified identifier for the resourceAllowance. 

To set the `resource_allowance` attribute: 

  * provide the argument `RESOURCE_ALLOWANCE` on the command line; 
  * resource allowance ID is optional and will be generated if not specified. 


`--location`=`LOCATION`
     Google Cloud location for the resourceAllowance. 

To set the `location` attribute: 

  * provide the argument `RESOURCE_ALLOWANCE` on the command line with a fully specified name; 
  * resource allowance ID is optional and will be generated if not specified with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `batch/location`. 


REQUIRED FLAGS
    

`--config`=`PATH_TO_FILE`
     The config file of a resource allowance. Use a full or relative path to a local file containing the value of config. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
