---
url: https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/unlink/
title: gcloud billing projects unlink \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:34.860126+00:00
---

# gcloud billing projects unlink  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/billing/projects/unlink/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud billing projects unlink Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud billing projects unlink - unlink the account (if any) linked with a project 
SYNOPSIS
    

`gcloud billing projects unlink` `PROJECT_ID` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command unlinks a project from its associated billing account. This action disables billing on the project. Any billable resources and services in use in your project are stopped, and your application stops functioning. Any costs accrued prior to disabling billing on the project are charged to the previously associated billing account. 

Note: To link a project to a different billing account, use the `billing projects link` command. You do not need to unlink the project first. 

EXAMPLES
     To unlink the project `my-project` from its linked billing account, run: 
    
    
    gcloud billing projects unlink my-project

POSITIONAL ARGUMENTS
    

`PROJECT_ID`
     Specify a project id. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudbilling/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/billing/v1/getting-started>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha billing projects unlink](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/projects/unlink)
    
    
    [gcloud beta billing projects unlink](https://docs.cloud.google.com/sdk/gcloud/reference/beta/billing/projects/unlink)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
