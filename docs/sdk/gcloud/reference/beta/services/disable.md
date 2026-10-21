---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/disable/
title: gcloud beta services disable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:41.216924+00:00
---

# gcloud beta services disable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta services disable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta services disable - disable a service for consumption for a project, folder or organization 
SYNOPSIS
    

`gcloud beta services disable` `SERVICE` [`SERVICE` …] [`--async`] [`--bypass-api-usage-check`] [`--force`] [`--validate-only`] [`--bypass-dependency-service-check` | `--disable-dependency-services`] [`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command disables one or more previously-enabled services for consumption. 

To see a list of the enabled services for a project, run: 
    
    
    [gcloud beta services list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/list)

More information on listing services can be found at: <https://cloud.google.com/service-usage/docs/list-services> and on disabling a service at: <https://cloud.google.com/service-usage/docs/enable-disable>

EXAMPLES
     To disable a service called `my-consumed-service` for the current project, run: 
    
    
    gcloud beta services disable my-consumed-service

To disable a service called `my-consumed-service` for the project `my-project`, run: 
    
    
    gcloud beta services disable my-consumed-service --project=my-project

To disable a service called `my-consumed-service` for the folder `my-folder`, run: 
    
    
    gcloud beta services disable my-consumed-service --folder=my-folder

To disable a service called `my-consumed-service` for the organization `my-organization`, run: 
    
    
    gcloud beta services disable my-consumed-service --organization=my-organization

To run the same command asynchronously (non-blocking), run: 
    
    
    gcloud beta services disable my-consumed-service --async

POSITIONAL ARGUMENTS
    

`SERVICE` [`SERVICE` …]
     The name of the service(s) to disable. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bypass-api-usage-check`
     If specified, the system will bypass usage checks for services that are being removed. Otherwise, the system will check if the service to be removed was used in the last 30 days or enabled in the last 3 days. If so, the system will return an error. 
`--force`
     If specified, the disable call will proceed even if there are enabled services which depend on the service to be disabled, or the service to be disabled was used in the last 30 days, or the service to be disabled was enabled in the last 3 days. Forcing the call means that the services which depend on the service to be disabled will also be disabled. (Note): If --bypass-api-usage-check, \--bypass-dependency-service-check, or --disable-dependency-services flags are used, they will take precedence over --force. 
`--validate-only`
     Validate the disable action, but don't actually perform it 
At most one of these can be specified: 

`--bypass-dependency-service-check`
     If specified, the disable call will bypass the check for dependencies and the dependencies will remain enabled. 
`--disable-dependency-services`
     If specified, the disable call will proceed disabling the service and all the enabled services depend on the service to be disabled 
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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud services disable](https://docs.cloud.google.com/sdk/gcloud/reference/services/disable)
    
    
    [gcloud alpha services disable](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/disable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
