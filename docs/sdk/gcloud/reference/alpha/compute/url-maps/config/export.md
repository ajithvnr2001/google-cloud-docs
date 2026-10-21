---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/url-maps/config/export/
title: gcloud alpha compute url-maps config export \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:34:29.733328+00:00
---

# gcloud alpha compute url-maps config export  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/url-maps/config/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute url-maps config export Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute url-maps config export - export the configuration for a URL map 
SYNOPSIS
    

`gcloud alpha compute url-maps config export` ([[`URL_MAP`] `--global` | `--region`=`REGION`] `--all`) [`--path`=`PATH`; default="-"] [`--resource-format`=`RESOURCE_FORMAT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute url-maps config export` exports the configuration for a URL map. 

Url map configurations can be exported in Kubernetes Resource Model (krm) or Terraform HCL formats. The default format is `krm`. 

Specifying `--all` allows you to export the configurations for all URL maps within the project. 

Specifying `--path` allows you to export the configuration(s) to a local directory. 

EXAMPLES
     To export the configuration for a URL map, run: 
    
    
    gcloud alpha compute url-maps config export my-url-map

To export the configuration for a URL map to a file, run: 
    
    
    gcloud alpha compute url-maps config export my-url-map --path=/path/to/dir/

To export the configuration for a URL map in Terraform HCL format, run: 
    
    
    gcloud alpha compute url-maps config export my-url-map --resource-format=terraform

To export the configurations for all URL maps within a project, run: 
    
    
    gcloud alpha compute url-maps config export --all

POSITIONAL ARGUMENTS
    

Exactly one of these must be specified: 

[`URL_MAP`]
     Name of the URL map to export. 

At most one of these can be specified: 

`--global`
     If set, the URL map is global. 
`--region`=`REGION`
     Region of the URL map to export. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

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
