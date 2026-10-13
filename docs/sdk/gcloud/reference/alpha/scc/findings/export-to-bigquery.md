---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/findings/export-to-bigquery/
title: gcloud alpha scc findings export-to-bigquery \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:14.544450+00:00
---

# gcloud alpha scc findings export-to-bigquery  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/findings/export-to-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc findings export-to-bigquery Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc findings export-to-bigquery - export Security Command Center findings to bigquery 
SYNOPSIS
    

`gcloud alpha scc findings export-to-bigquery` [`PARENT`] `--dataset`=`DATASET` [`--location`=`LOCATION`; default="global"] [`--source`=`SOURCE`; default="-"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Export Security Command Center findings to bigquery. 
EXAMPLES
     To export findings for a given parent ``organizations/123/sources/456/locations/global`` and dataset ``projects/project_id/datasets/dataset_id`` run: 
    
    
    gcloud alpha scc findings export-to-bigquery organizations/123 --dataset=projects/project_id/datasets/dataset_id --source=456 --location=global

POSITIONAL ARGUMENTS
    

Parent resource - parent organization, folder, or project in the Google Cloud resource hierarchy to be used for the `[gcloud scc](https://docs.cloud.google.com/sdk/gcloud/reference/scc)` command. Specify the argument as either [RESOURCE_TYPE/RESOURCE_ID] or [RESOURCE_ID], as shown in the preceding examples. This represents a Cloud resource. 
[`PARENT`]
     ID of the parent or fully qualified identifier for the parent. 

To set the `parent` attribute: 

  * provide the argument `parent` on the command line; 
  * Set the parent property in configuration using `gcloud config set scc/parent` if it is not specified in command line. 


REQUIRED FLAGS
    

`--dataset`=`DATASET`
     BigQuery dataset to export findings to. 
OPTIONAL FLAGS
    

`--location`=`LOCATION`; default="global"
     When data residency controls are enabled, this attribute specifies the location in which the resource is located and applicable. The `location` attribute can be provided as part of the fully specified resource name or with the `--location` argument on the command line. The default location is `global`. 

NOTE: If you override the endpoint to a [regional endpoint](https://cloud.google.com/security-command-center/docs/reference/rest/index.html?rep_location=global#regional-service-endpoint) you must specify the correct [data location](https://cloud.google.com/security-command-center/docs/data-residency-support#locations) using this flag. The default location on this command is unrelated to the default location that is specified when data residency controls are enabled for Security Command Center. 

NOTE: If no location is specified, the default location is `global` AND the request will be routed to the SCC V1 API. To use the SCC V2 API - please explicitly specify the flag. 

`--source`=`SOURCE`; default="-"
     Source id. Defaults to all sources. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the Security Command Center API. For more information, see [Security Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud scc findings export-to-bigquery](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/export-to-bigquery)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
