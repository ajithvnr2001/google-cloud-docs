---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/config/export/
title: gcloud alpha compute disks config export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:00.330369+00:00
---

# gcloud alpha compute disks config export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/disks/config/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute disks config export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute disks config export - export the configuration for a Compute Engine disk 
SYNOPSIS
    

`gcloud alpha compute disks config export` ([`DISK` : `--zone`=`ZONE`] `--all`) [`--path`=`PATH`; default="-"] [`--resource-format`=`RESOURCE_FORMAT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute disks config export` exports the configuration for a Compute Engine disk. 

Disk configurations can be exported in Kubernetes Resource Model (krm) or Terraform HCL formats. The default format is `krm`. 

Specifying `--all` allows you to export the configurations for all disks within the project. 

Specifying `--path` allows you to export the configuration(s) to a local directory. 

EXAMPLES
     To export the configuration for a disk, run: 
    
    
    gcloud alpha compute disks config export my-disk

To export the configuration for a disk to a file, run: 
    
    
    gcloud alpha compute disks config export my-disk --path=/path/to/dir/

To export the configuration for a disk in Terraform HCL format, run: 
    
    
    gcloud alpha compute disks config export my-disk --resource-format=terraform

To export the configurations for all disks within a project, run: 
    
    
    gcloud alpha compute disks config export --all

POSITIONAL ARGUMENTS
    

Exactly one of these must be specified: 

Disk resource - Disk to export the configuration for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `disk` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



`DISK`
     ID of the disk or fully qualified identifier for the disk. 

To set the `disk` attribute: 

* provide the argument `disk` on the command line. 

This positional argument must be specified if any of the other arguments in this group are specified. 

`--zone`=`ZONE`
     The name of the Google Compute Engine zone. 

To set the `zone` attribute: 

* provide the argument `disk` on the command line with a fully specified name; 
* provide the argument `--zone` on the command line; 
* set the property `compute/zone`. 
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
