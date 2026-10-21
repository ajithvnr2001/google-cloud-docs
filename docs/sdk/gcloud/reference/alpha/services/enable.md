---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/enable/
title: gcloud alpha services enable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:20.563615+00:00
---

# gcloud alpha services enable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha services enable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha services enable - enables a service for consumption for a project, folder or organization 
SYNOPSIS
    

`gcloud alpha services enable` `SERVICE` [`SERVICE` …] [`--async`] [`--group`=`GROUP`; default="dependencies"] [`--skip-dependency`] [`--validate-only`] [`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command enables a service for consumption for a project, folder or organization. 
    
    
    To see a list of available services for a project, run:
    
    
    [gcloud alpha services list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/list) --available

More information on listing services can be found at: <https://cloud.google.com/service-usage/docs/list-services> and on disabling a service at: <https://cloud.google.com/service-usage/docs/enable-disable>

EXAMPLES
     To enable a service called `my-consumed-service` on the current project, run: 
    
    
    gcloud alpha services enable my-consumed-service

To enable a service called `my-consumed-service` on the project `my-project`, run: 
    
    
    gcloud alpha services enable my-consumed-service --project=my-project

To enable a service called `my-consumed-service` on the project `my-project` in group `groups`, run: 
    
    
    gcloud alpha services enable my-consumed-service --project=my-project --group=groups

To enable a service called `my-consumed-service` on the folder `my-folder, run: 
    
    
    gcloud alpha services enable my-consumed-service --folder=my-folder

To enable a service called 

`my-consumed-service` on the organization `my-organization`, run: 
    
    
    gcloud alpha services enable my-consumed-service --organization=my-organization

To run the same command asynchronously (non-blocking), run: 
    
    
    gcloud alpha services enable my-consumed-service --async

To enable services called 

`service1`, `service2`, and `service3` on the current project, run: 
    
    
    gcloud alpha services enable service1 service2 service3

`

POSITIONAL ARGUMENTS
    

`SERVICE` [`SERVICE` …]
     The name of the service(s) to enable. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--group`=`GROUP`; default="dependencies"
     The service group name. 
`--skip-dependency`
     If set, the dependencies of the service to be enabled will not be enabled. 
`--validate-only`
     Validate the enable action, but don't actually perform it 
At most one of these can be specified: 

`--folder`=`FOLDER_ID`
     The Google Cloud Platform folder ID to use for this invocation. 
`--organization`=`ORGANIZATION_ID`
     The Google Cloud Platform organization ID to use for this invocation. 
`--project`=`PROJECT_ID`
     The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation. It specifies the project of the resource to operate on. It also specifies the project for API enablement check, quota, and billing. To specify a different project for quota and billing, use `--billing-project` or `billing/quota_project` property. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud services enable](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable)
    
    
    [gcloud beta services enable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/enable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
