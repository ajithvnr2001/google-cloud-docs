---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/projects/link/
title: gcloud alpha billing accounts projects link \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:18.477804+00:00
---

# gcloud alpha billing accounts projects link  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/projects/link/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha billing accounts projects link Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha billing accounts projects link - link a project with a billing account 
SYNOPSIS
    

`gcloud alpha billing accounts projects link` `PROJECT_ID` (`--account-id`=`ACCOUNT_ID` | `--billing-account`=`ACCOUNT_ID`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` The `[gcloud alpha billing accounts projects](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/billing/accounts/projects)` group has been moved to `gcloud billing projects`. Please use the new, shorter commands instead. 

This command links a billing account to a project. 

If the specified billing account is open, this enables billing on the project. 

EXAMPLES
     To link a billing account `0X0X0X-0X0X0X-0X0X0X` with a project `my-project`, run: 
    
    
    gcloud alpha billing accounts projects link my-project --billing-account=0X0X0X-0X0X0X-0X0X0X

POSITIONAL ARGUMENTS
    

`PROJECT_ID`
     Specify a project id. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--account-id`=`ACCOUNT_ID`
     (DEPRECATED) Specify a billing account ID. Billing account IDs are of the form `0X0X0X-0X0X0X-0X0X0X`. To see available IDs, run `$ [gcloud billing accounts list](https://docs.cloud.google.com/sdk/gcloud/reference/billing/accounts/list)`. 

The `--account-id` flag has been renamed `--billing-account`. 

`--billing-account`=`ACCOUNT_ID`
     Specify a billing account ID. Billing account IDs are of the form `0X0X0X-0X0X0X-0X0X0X`. To see available IDs, run `$ [gcloud billing accounts list](https://docs.cloud.google.com/sdk/gcloud/reference/billing/accounts/list)`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
