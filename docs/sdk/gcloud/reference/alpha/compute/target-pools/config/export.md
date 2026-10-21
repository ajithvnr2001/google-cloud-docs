---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-pools/config/export/
title: gcloud alpha compute target-pools config export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:03:37.706099+00:00
---

# gcloud alpha compute target-pools config export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-pools/config/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute target-pools config export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute target-pools config export - export the configuration for a Compute Engine target pool 
SYNOPSIS
    

`gcloud alpha compute target-pools config export` ([`TARGET_POOL` : `--region`=`REGION`] `--all`) [`--path`=`PATH`; default="-"] [`--resource-format`=`RESOURCE_FORMAT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute target-pools config export` exports the configuration for a Compute Engine target pool. 

Target pool configurations can be exported in Kubernetes Resource Model (krm) or Terraform HCL formats. The default format is `krm`. 

Specifying `--all` allows you to export the configurations for all target pools within the project. 

Specifying `--path` allows you to export the configuration(s) to a local directory. 

EXAMPLES
     To export the configuration for a target pool, run: 
    
    
    gcloud alpha compute target-pools config export my-target-pool

To export the configuration for a target pool to a file, run: 
    
    
    gcloud alpha compute target-pools config export my-target-pool --path=/path/to/dir/

To export the configuration for a target pool in Terraform HCL format, run: 
    
    
    gcloud alpha compute target-pools config export my-target-pool --resource-format=terraform

To export the configurations for all target pools within a project, run: 
    
    
    gcloud alpha compute target-pools config export --all

POSITIONAL ARGUMENTS
    

Exactly one of these must be specified: 

Target pool resource - Target pool to export the configuration for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `target_pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



`TARGET_POOL`
     ID of the target pool or fully qualified identifier for the target pool. 

To set the `target_pool` attribute: 

* provide the argument `target_pool` on the command line. 

This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Google Compute Engine region. 

To set the `region` attribute: 

* provide the argument `target_pool` on the command line with a fully specified name; 
* provide the argument `--region` on the command line; 
* set the property `compute/region`. 
`--all`
     Retrieve all resources within the project. If `--path` is specified and is a valid directory, resources will be output as individual files based on resource name and scope. If `--path` is not specified, resources will be streamed to stdout. 
FLAGS
    

`--path`=`PATH`; default="-"
     Path of the directory or file to output configuration(s). To output configurations to stdout, specify "--path=-". 
`--resource-format`=`RESOURCE_FORMAT`
     Format of the configuration to export. Available configuration formats are Kubernetes Resource Model YAML (krm) or Terraform HCL (terraform). Command defaults to "krm". `RESOURCE_FORMAT` must be one of: `krm`, `terraform`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
